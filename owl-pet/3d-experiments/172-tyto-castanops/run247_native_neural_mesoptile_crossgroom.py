#!/usr/bin/env python3
"""Run247: actual Hunyuan learned mesh + two crossed 3D alpha-feather groom studies.

We DO NOT fabricate an owl from primitives or replace the learned 3D geometry.
The previous Run246 A tree ledge is retained for comparison (not art approved).
Outputs and all images are research only / NO_RELEASE.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import trimesh
from PIL import Image, ImageFilter

PIN = "7864afc8a220c7edfa069f4d5bf2498db0fe0810c7e917a0451fc8201f22312b"
CORE = "real_neural_owl_juvenile_core"
OLD_DOWN = "real_3d_surface_following_wispy_down"
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def unit(v): return v / np.maximum(np.linalg.norm(v,axis=-1,keepdims=True), 1.e-8)
def ss(a,b,x):
    t=np.clip((x-a)/(b-a),0,1)
    return t*t*(3-2*t)

def atlas():
    """512x512 RGBA plume texture, four nonidentical branched soft-down panels."""
    rng=np.random.default_rng(172247)
    y,x=np.mgrid[:512,:512].astype(np.float32)
    t=(y+.5)/512
    u=(x%128+.5)/128
    alpha=np.zeros((512,512),np.float32)
    for cell in range(4):
        band=(x>=128*cell)&(x<128*(cell+1))
        fibers=np.zeros_like(alpha)
        for j in range(24):
            root=.50+rng.uniform(-.11,.11)
            sway=rng.uniform(-.27,.27)
            phase=rng.uniform(0,6.28)
            center=root+sway*t+rng.uniform(.01,.055)*np.sin(1.2*np.pi*t+phase)*t
            width=(.009+rng.uniform(0,.008))*(1-.68*t)
            strand=np.exp(-.5*((u-center)/np.maximum(width,.003))**2)
            envelope=np.maximum(np.sin(np.pi*t),0)**.55
            fibers=np.maximum(fibers,strand*envelope*rng.uniform(.59,.93))
            for k in range(2):
                t0=.24+.25*k
                offset=(.04+k*.035)*np.maximum((t-t0)/.35,0)
                center2=center+offset*(-1 if (j+k)%2 else 1)
                barb=np.exp(-.5*((u-center2)/.008)**2)
                barb*=np.maximum(0,1-np.abs((t-(.40+.24*k))/.21))*.30
                fibers=np.maximum(fibers,barb)
        mist=np.exp(-((t-.19)/.23)**2)*np.exp(-((u-.5)/.32)**2)*.13
        alpha=np.where(band,np.maximum(fibers,mist),alpha)
    img=np.empty((512,512,4),np.uint8)
    variation=4*np.sin(x*.031+y*.017)+3*np.cos(x*.012+y*.039)
    for i,c in enumerate((244,233,217)):
        img[:,:,i]=np.clip(c+variation+i*1.5,0,255).astype(np.uint8)
    img[:,:,3]=np.clip(alpha*255,0,255).astype(np.uint8)
    return Image.fromarray(img,"RGBA").filter(ImageFilter.GaussianBlur(.48))

def groom(core, count, variant, texture):
    """Sample real triangle surface weighted to cover bald back and adult wing.

    Root cross cards are anchored into actual neural mesh and oriented using
    the native face normals; natural branched alpha comes from a shared atlas.
    """
    rng=np.random.default_rng(172247+(0 if variant=="A" else 200))
    triangles=core.vertices[core.faces]
    center=core.triangles_center
    shield=ss(.39,.68,center[:,2])*ss(.14,.45,center[:,1])
    weights=core.area_faces*(1+.96*(center[:,2]<.12)+.65*(abs(center[:,0])>.28))
    weights*=np.clip(1-.987*shield,.025,1)
    weights*=.11+.89*ss(-.74,-.40,center[:,1])
    weights/=weights.sum()
    face_id=rng.choice(len(core.faces),size=count,p=weights)
    t=triangles[face_id]
    u=rng.random((count,1));v=rng.random((count,1))
    outside=(u+v)>1
    u=np.where(outside,1-u,u);v=np.where(outside,1-v,v)
    p=t[:,0]+u*(t[:,1]-t[:,0])+v*(t[:,2]-t[:,0])
    n=unit(core.face_normals[face_id].astype(np.float32))
    j=unit(rng.normal(size=(count,3)).astype(np.float32))
    tang=unit(j-(j*n).sum(axis=1,keepdims=True)*n)
    up=np.tile(np.array([[0,1,0]],np.float32),(count,1))
    # A remains a sparse protruding fluff stress test, C a short laid-down
    # alternate groom to test if hedgehog spikes can be avoided.
    direction=unit(n*.74+up*.21+tang*.27) if variant=="A" else unit(n*.35+up*.29+tang*.64)
    e1=unit(np.cross(direction,n))
    bad=np.linalg.norm(e1,axis=1)<.05
    if np.any(bad): e1[bad]=unit(np.cross(direction[bad],np.array([1,0,0],np.float32)))
    e2=unit(np.cross(direction,e1))
    angle=rng.uniform(-np.pi,np.pi,count).astype(np.float32)
    rear=p[:,2]<.15
    wing=(abs(p[:,0])>.35)&(p[:,1]<.37)
    length=(rng.uniform(.048,.105,count) if variant=="A" else rng.uniform(.039,.085,count))
    length=length.astype(np.float32)*(1+.18*rear+.15*wing)
    length*=np.where(p[:,1]>.70,.65,1.)
    width=length*rng.uniform(.10,.22,count).astype(np.float32)
    start=p+n*.012
    tip=start+direction*length[:,None]
    verts=np.empty((count,2,4,3),np.float32)
    uv=np.empty((count,2,4,2),np.float32)
    for k in range(2):
        side=unit(e1*np.cos(angle[:,None]+k*np.pi/2)+e2*np.sin(angle[:,None]+k*np.pi/2))
        verts[:,k,0]=start-side*(width*.13)[:,None]
        verts[:,k,1]=start+side*(width*.13)[:,None]
        verts[:,k,2]=tip+side*(width*.78)[:,None]
        verts[:,k,3]=tip-side*(width*.78)[:,None]
        cell=rng.integers(0,4,count)
        lo=(cell+.04)/4;hi=(cell+.96)/4
        uv[:,k,0]=np.stack([lo,np.full(count,.03)],axis=1)
        uv[:,k,1]=np.stack([hi,np.full(count,.03)],axis=1)
        uv[:,k,2]=np.stack([hi,np.full(count,.97)],axis=1)
        uv[:,k,3]=np.stack([lo,np.full(count,.97)],axis=1)
    ix=np.arange(count*2).reshape(-1,1)*4
    faces=np.concatenate([np.concatenate([ix,ix+1,ix+2],axis=1),
                          np.concatenate([ix,ix+2,ix+3],axis=1)],axis=0)
    mesh=trimesh.Trimesh(vertices=verts.reshape(-1,3),faces=faces,process=False)
    mat=trimesh.visual.material.PBRMaterial(name="run247_cream_second_down_plumules",
        baseColorTexture=texture,alphaMode="MASK",alphaCutoff=.12,
        doubleSided=True,metallicFactor=0,roughnessFactor=1,
        baseColorFactor=[255,255,255,255])
    mesh.visual=trimesh.visual.TextureVisuals(uv=uv.reshape(-1,2),material=mat)
    return mesh,{"crossed_tufts":count,"groom_triangles":len(mesh.faces),
                 "rear_root_fraction":float(rear.mean()),
                 "wing_root_fraction":float(wing.mean()),
                 "length_range":[float(length.min()),float(length.max())]}

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--source",required=True)
    a.add_argument("--outdir",required=True)
    args=a.parse_args()
    if sha(args.source)!=PIN:raise ValueError("SHA-verified neural source required")
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    original=trimesh.load(args.source,force="scene")
    assert len(original.geometry)==9 and sum(len(m.faces) for m in original.geometry.values())==131835
    original_counts={k:(len(v.vertices),len(v.faces)) for k,v in original.geometry.items()}
    pic=atlas();pic.save(out/"run247_branching_down_RGBA_512.png")
    report={"run":"Run247","source_sha256":PIN,"real_neural_owl_preserved":True,
            "research_only":True,"art_approved":False,"phone_gpu":"UNTESTED",
            "extra_paid_usd":0,"release":"NO_RELEASE","variants":{}}
    for variant,count in (("A",14000),("C",36000)):
        scene=trimesh.load(args.source,force="scene")
        if variant=="C":scene.delete_geometry(OLD_DOWN)
        fur,details=groom(original.geometry[CORE],count,variant,pic)
        name="run247_actual_neural_surface_plumulaceous_crosscards_"+variant
        scene.add_geometry(fur,geom_name=name)
        output=out/("run247_"+variant+"_native_neural_mesoptile_ART_UNAPPROVED_NO_RELEASE.glb")
        output.write_bytes(scene.export(file_type="glb",include_normals=True))
        checked=trimesh.load(output,force="scene")
        assert len(checked.geometry)==(10 if variant=="A" else 9)
        assert len(checked.geometry[name].faces)==4*count
        for key,shape in original_counts.items():
            if key==OLD_DOWN and variant=="C":continue
            assert (len(checked.geometry[key].vertices),len(checked.geometry[key].faces))==shape
        assert all(np.isfinite(mesh.vertices).all() for mesh in checked.geometry.values())
        details.update({"output_file":output.name,"output_sha256":sha(output),
                        "bytes":output.stat().st_size,"triangles":int(sum(len(v.faces) for v in checked.geometry.values())),
                        "meshes":len(checked.geometry),"original_neural_owl_unmodified":True})
        report["variants"][variant]=details
    (out/"run247_machine_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":main()
