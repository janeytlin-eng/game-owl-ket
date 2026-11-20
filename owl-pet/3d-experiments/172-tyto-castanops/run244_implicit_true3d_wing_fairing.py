#!/usr/bin/env python3
"""Run244: actual Hunyuan owl mesh, volumetric wing-groove fairing (NOT a released character).
Preserves the continuous learned mesh topology, all RGB vertex attributes, eye geometry,
and native down-card UV / alpha texture. Never substitutes a geometric-primitives owl.
"""
import argparse, hashlib, json, struct, time
from pathlib import Path
import numpy as np
import trimesh
from scipy.ndimage import gaussian_filter, binary_closing, binary_fill_holes
from scipy.spatial import cKDTree
from skimage.measure import marching_cubes

PIN="ef60639bbba95a0e876ac427b277fa500063b9ce05d9b9c8bae5811a5c0518d1"
def sha(b): return hashlib.sha256(b).hexdigest()
def parse(raw):
    assert raw[:4]==b"glTF" and struct.unpack_from("<II",raw,4)==(2,len(raw))
    n,t=struct.unpack_from("<I4s",raw,12); assert t==b"JSON"
    doc=json.loads(raw[20:20+n])
    bl,t=struct.unpack_from("<I4s",raw,20+n)
    assert t==b"BIN\0" and bl+n+28==len(raw)
    return doc,bytearray(raw[28+n:])
def access(doc,buf,idx):
    a=doc["accessors"][idx];v=doc["bufferViews"][a["bufferView"]]
    dtype={5121:np.uint8,5125:np.uint32,5126:np.float32}[a["componentType"]]
    dims={"SCALAR":1,"VEC2":2,"VEC3":3,"VEC4":4}[a["type"]]
    assert v.get("byteStride",np.dtype(dtype).itemsize*dims)==np.dtype(dtype).itemsize*dims
    return np.ndarray((a["count"],dims),dtype=dtype,buffer=buf,
                      offset=v.get("byteOffset",0)+a.get("byteOffset",0))
def pack(doc,buf):
    doc["buffers"][0]["byteLength"]=len(buf)
    j=json.dumps(doc,ensure_ascii=False,separators=(",",":")).encode("utf8")
    j+=b" "*((-len(j))%4)
    assert len(buf)%4==0
    return (struct.pack("<4sII",b"glTF",2,28+len(j)+len(buf))
           +struct.pack("<I4s",len(j),b"JSON")+j
           +struct.pack("<I4s",len(buf),b"BIN\0")+buf)
def recalc_normals(doc,buf,idx):
    p=doc["meshes"][idx]["primitives"][0];v=access(doc,buf,p["attributes"]["POSITION"])
    f=access(doc,buf,p["indices"]).ravel().reshape(-1,3)
    x=v[f];nf=np.cross(x[:,1]-x[:,0],x[:,2]-x[:,0]);nv=np.zeros_like(v)
    for k in range(3): np.add.at(nv,f[:,k],nf)
    nv/=np.maximum(np.linalg.norm(nv,axis=1,keepdims=True),1e-10)
    access(doc,buf,p["attributes"]["NORMAL"])[:]=nv
    for a in ("POSITION","NORMAL"):
        n=p["attributes"][a];arr=access(doc,buf,n)
        doc["accessors"][n]["min"]=arr.min(axis=0).astype(float).tolist()
        doc["accessors"][n]["max"]=arr.max(axis=0).astype(float).tolist()
def smooth(a,b,x):
    t=np.clip((x-a)/(b-a),0,1)
    return t*t*(3-2*t)
def variant(raw,pitch,sigma,threshold,name,outdir):
    doc,buf=parse(raw);baseline,oldbuf=parse(raw)
    prim=doc["meshes"][0]["primitives"][0]
    pts=access(doc,buf,prim["attributes"]["POSITION"])
    original=pts.copy()
    faces=access(doc,buf,prim["indices"]).ravel().reshape(-1,3)
    learned=trimesh.Trimesh(vertices=original,faces=faces,process=False)
    started=time.time()
    vox=learned.voxelized(pitch).fill()
    occupancy=binary_fill_holes(binary_closing(vox.matrix.astype(bool),iterations=2))
    density=gaussian_filter(occupancy.astype(np.float32),sigma=sigma,mode="constant")
    vertices,triangles,_,_=marching_cubes(density,level=threshold)
    candidate=(vox.transform@np.c_[vertices,np.ones(len(vertices))].T).T[:,:3]
    _,ids=cKDTree(candidate).query(original)
    x,y,z=original.T
    side=smooth(.22,.54,np.abs(x))
    rear=1-smooth(-.24,.55,z)
    torso=smooth(-.71,-.56,y)*(1-smooth(.32,.61,y))
    back=(1-smooth(-.46,.03,z))*smooth(-.69,-.51,y)
    blend=np.clip((.83*side*rear+.37*back)*torso,0,1)
    blend*=1-smooth(.46,.68,z)
    blend=np.clip(blend*1.12,0,.94)
    delta=np.clip((candidate[ids]-original)*blend[:,None],-.2,.2)
    # New: nearest implicit-vertex projection is discontinuous at small triangle
    # scales. Graph-Laplacian FAIR THE DISPLACEMENT on original learned triangle
    # adjacency to prevent folded/inverted real 3D faces. No primitive rebuilt.
    i,j,k=faces.T
    edges_from=np.concatenate([i,j,j,k,k,i])
    edges_to=np.concatenate([j,i,k,j,i,k])
    degree=np.bincount(edges_from,minlength=len(original)).astype(float)
    for _ in range(32):
        average=np.zeros_like(delta)
        np.add.at(average,edges_from,delta[edges_to])
        average/=np.maximum(degree[:,None],1)
        delta=.46*delta+.54*average
    delta[(original[:,2]>.68)&(original[:,1]>.37)]=0
    newpoints=original+delta
    oldtr=original[faces];newtr=newpoints[faces]
    n0=np.cross(oldtr[:,1]-oldtr[:,0],oldtr[:,2]-oldtr[:,0])
    n1=np.cross(newtr[:,1]-newtr[:,0],newtr[:,2]-newtr[:,0])
    inverted=int(np.count_nonzero(np.einsum("ij,ij->i",n0,n1)<0))
    assert inverted==0,("inverted learned 3D core faces",inverted)
    pts[:]=newpoints.astype(np.float32)
    recalc_normals(doc,buf,0)
    # Retarget original genuine feather cards by interpolated learned-core displacement.
    down=doc["meshes"][1]["primitives"][0]
    fur=access(doc,buf,down["attributes"]["POSITION"]);fur0=fur.copy()
    distances,neighbors=cKDTree(original).query(fur0,k=3)
    w=1/np.maximum(distances,.015)**2;w/=w.sum(axis=1,keepdims=True)
    furshift=np.einsum("ij,ijk->ik",w,delta[neighbors])
    fur[:]=fur0+furshift.astype(np.float32)
    recalc_normals(doc,buf,1)
    assert len(doc["meshes"])==8
    # Exact scientific source and core/eyes colour/UV/topology integrity gates.
    for i in range(8):
        before=baseline["meshes"][i]["primitives"][0]
        after=doc["meshes"][i]["primitives"][0]
        assert np.array_equal(access(baseline,oldbuf,before["indices"]),
                              access(doc,buf,after["indices"]))
        for a in ("COLOR_0","TEXCOORD_0"):
            if a in before["attributes"]:
                assert np.array_equal(access(baseline,oldbuf,before["attributes"][a]),
                                      access(doc,buf,after["attributes"][a]))
        if i>=2:
            for a in ("POSITION","NORMAL"):
                assert np.array_equal(access(baseline,oldbuf,before["attributes"][a]),
                                      access(doc,buf,after["attributes"][a]))
    blob=pack(doc,buf)
    output=outdir/("run244_"+name+"_real_neural_implicit_clad_ART_UNAPPROVED_NO_RELEASE.glb")
    output.write_bytes(blob)
    scene=trimesh.load(output,force="scene")
    tris=sum(len(m.faces) for m in scene.geometry.values())
    assert len(scene.geometry)==8 and tris==86867
    assert all(np.isfinite(m.vertices).all() for m in scene.geometry.values())
    movement=np.linalg.norm(delta,axis=1)
    return dict(file=output.name,bytes=len(blob),sha256=sha(blob),
                real_meshes=len(scene.geometry),triangles=tris,
                implicit_volumetric_mesh_vertices=len(vertices),
                implicit_volumetric_mesh_triangles=len(triangles),
                nonrigid_moved_gt_0p01=int((movement>.01).sum()),
                max_3d_displacement=float(movement.max()),
                avg_3d_displacement=float(movement.mean()),
                max_surface_down_retarget=float(np.linalg.norm(furshift,axis=1).max()),
                voxel_grid=list(map(int,occupancy.shape)),sigma_voxels=sigma,
                threshold=threshold,execution_seconds=round(time.time()-started,2),
                inverted_learned_core_triangles=inverted,
                six_eye_meshes_exact_preserved=True,vertex_colors_and_uv_preserved=True)
def main():
    a=argparse.ArgumentParser()
    a.add_argument("--source",required=True);a.add_argument("--outdir",required=True)
    args=a.parse_args()
    raw=Path(args.source).read_bytes(); assert sha(raw)==PIN,"real source SHA mismatch"
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    report={"run":"Run244","method":"real neural mesh, volumetric fairing and genuine down reattachment",
            "source_sha256":PIN,"release":"NO_RELEASE","art_approved":False,
            "physical_phone_gpu":"UNTESTED","external_paid_usd":0,"variants":{}}
    for label,sigma,threshold in (("E",3.25,.52),("F",4.75,.55)):
        report["variants"][label]=variant(raw,.025,sigma,threshold,label,out)
    report["status"]="TWO_REAL_3D_TEST_MODELS_NEED_ART_REVIEW_NO_RELEASE"
    (out/"run244_machine_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":main()
