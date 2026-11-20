#!/usr/bin/env python3
"""Run250: TRUE native neural 3D volumetric juvenile torso reconstruction + VTK LOD.
Research only. No primitive owl, no SVG, no art approval, no phone GPU test.
Y up and +Z front. Source is SHA-pinned authentic Run248 neural GLB.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import scipy.ndimage as ndi
import trimesh
import vtk
from PIL import Image
from scipy.spatial import cKDTree
from skimage.measure import marching_cubes
from run250_neural_color_transfer import pin_neural_colors
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray,vtk_to_numpy

SOURCE_SHA="247d820538920735783072a204686fcf2f02ddb3ce1958a5472895a3ed7c1845"
CORE="real_neural_owl_juvenile_core"
DOWN="real_3d_surface_following_wispy_down"
BARK="run246_authentic_Y_UP_horizontal_eucalypt_bark_ledge_A"
VARIANTS={"A":(5.0,0.85),"B":(9.0,1.0)}
PITCH=.018
PAD=28

def hashfile(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def smoothstep(a,b,v):
    s=np.clip((v-a)/(b-a),0,1)
    return s*s*(3-2*s)

def decimate(mesh,face_count):
    """Real quadric edge-collapse mesh simplification, not shape assembly."""
    if len(mesh.faces)<=face_count:
        return mesh.copy()
    pol=vtk.vtkPolyData()
    pts=vtk.vtkPoints()
    pts.SetData(numpy_to_vtk(mesh.vertices.astype(np.float32),deep=True))
    pol.SetPoints(pts)
    face_items=np.column_stack((np.full(len(mesh.faces),3,dtype=np.int64),mesh.faces)).ravel()
    ca=vtk.vtkCellArray()
    ca.SetCells(len(mesh.faces),numpy_to_vtkIdTypeArray(face_items,deep=True))
    pol.SetPolys(ca)
    filt=vtk.vtkQuadricDecimation()
    filt.SetInputData(pol)
    filt.SetTargetReduction(1-face_count/len(mesh.faces))
    filt.VolumePreservationOn()
    filt.Update()
    done=filt.GetOutput()
    vertices=vtk_to_numpy(done.GetPoints().GetData()).astype(np.float64).copy()
    faces=vtk_to_numpy(done.GetPolys().GetConnectivityArray()).reshape(-1,3).astype(np.int64).copy()
    result=trimesh.Trimesh(vertices=vertices,faces=faces,process=False)
    result.visual=mesh.visual.copy()
    if result.volume<0:
        result.invert()
    assert len(result.faces)>10000 and result.is_watertight
    return result

def weathered_bark_texture(mesh,seed=172):
    """An experimental weathered-wood PBR texture for the true 3D bark shelf."""
    N=512
    rng=np.random.default_rng(seed)
    n0=rng.normal(size=(N,N))
    fine=ndi.gaussian_filter(n0,1.5)
    mid=ndi.gaussian_filter(n0,8)
    broad=ndi.gaussian_filter(n0,29)
    mid/=max(mid.std(),1e-6)
    fine/=max(fine.std(),1e-6)
    broad/=max(broad.std(),1e-6)
    yy,xx=np.mgrid[:N,:N]
    grain=np.sin(2*np.pi*(xx/56+0.17*mid+0.05*broad))
    ridge=np.maximum(0,np.abs(grain)-.75)*2.5
    noise=7*fine+5*mid+4*broad-26*ridge
    rgb=np.empty((N,N,3),dtype=np.uint8)
    for ch,base in enumerate((144,126,106)):
        rgb[:,:,ch]=np.clip(base+noise+(2 if ch==0 else (-2 if ch==2 else 0))*mid,0,255).astype(np.uint8)
    image=Image.fromarray(rgb,"RGB")
    xyz=mesh.vertices
    bounds=np.maximum(mesh.extents,1e-4)
    uv=np.column_stack(((xyz[:,0]-mesh.bounds[0,0])/bounds[0],
                        (xyz[:,2]-mesh.bounds[0,2])/bounds[2]))
    material=trimesh.visual.material.PBRMaterial(
        baseColorTexture=image,baseColorFactor=[255,255,255,255],
        metallicFactor=0.,roughnessFactor=.98,doubleSided=False)
    mesh.visual=trimesh.visual.texture.TextureVisuals(uv=uv,material=material)
    return image

def run(source,outdir):
    source=Path(source)
    assert hashfile(source)==SOURCE_SHA, "Wrong or unverified neural base"
    master=trimesh.load(source,force="scene")
    assert len(master.geometry)==9 and CORE in master.geometry and DOWN in master.geometry and BARK in master.geometry
    native=master.geometry[CORE]
    assert len(native.faces)==46856
    voxel=native.voxelized(PITCH).fill()
    mat=np.pad(voxel.matrix.astype(np.float32),PAD)
    X,Y,Z=np.meshgrid(np.arange(mat.shape[0],dtype=np.float32),
                      np.arange(mat.shape[1],dtype=np.float32),
                      np.arange(mat.shape[2],dtype=np.float32),indexing="ij")
    x,y,z=(np.stack((X,Y,Z),axis=0)-PAD)*PITCH+voxel.translation[:,None,None,None]
    w=smoothstep(-.70,-.30,y)*(1-smoothstep(.28,.55,y))*(1-smoothstep(.50,.75,z))
    w*=.25+.75*smoothstep(.08,.28,np.abs(x))
    raw=ndi.gaussian_filter(mat,.95)
    outdir.mkdir(parents=True,exist_ok=True)
    report={"run":"Run250",
            "study":"authentic neural 3D volumetric flank wing reconstruction + mobile-oriented native geometry LOD",
            "source_glb_sha256":SOURCE_SHA,"source_owl_core_triangles":46856,
            "art_approved":False,"phone_gpu":"UNTESTED","release":"NO_RELEASE",
            "source_geometry":"Hunyuan genuine neural 3D, NOT a geometric-proxy owl",
            "variants":{}}
    for name,(sigma,strength) in VARIANTS.items():
        blurred=ndi.gaussian_filter(mat,sigma)
        density=raw*(1-strength*w)+blurred*(strength*w)
        verts,faces,_,_=marching_cubes(density,.47,spacing=(PITCH,)*3)
        verts+=voxel.translation-PITCH*PAD
        newcore=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
        pieces=[part for part in newcore.split(only_watertight=False) if len(part.faces)>500]
        assert len(pieces)==1, "Detached component"
        newcore=pieces[0]
        if newcore.volume<0:newcore.invert()
        original_rebuilt_faces=len(newcore.faces)
        newcore=decimate(newcore,34000)
        newcore.visual=native.visual.copy()
        assert newcore.is_watertight and newcore.volume>0
        scene=trimesh.Scene()
        scene.add_geometry(newcore,geom_name=CORE,node_name=CORE)
        oldpoints=native.vertices
        newpoints=newcore.vertices
        f=master.geometry[DOWN].copy()
        dp=f.vertices.copy()
        ii=cKDTree(oldpoints).query(dp)[1]
        jj=cKDTree(newpoints).query(oldpoints[ii])[1]
        f.vertices=newpoints[jj]+np.clip(dp-oldpoints[ii],-.04,.04)
        scene.add_geometry(f,geom_name=DOWN,node_name=DOWN)
        for k,g in master.geometry.items():
            if k in (CORE,DOWN,BARK):continue
            scene.add_geometry(g.copy(),geom_name=k,node_name=k)
        bark=decimate(master.geometry[BARK],11000)
        im=weathered_bark_texture(bark)
        tex=outdir/f"run250_{name}_weathered_eucalyptus_experiment.png"
        im.save(tex)
        scene.add_geometry(bark,geom_name=BARK,node_name=BARK)
        output=outdir/f"run250_{name}_native_neural_volumetric_juvenile_rebuild_LOD_RESEARCH_NO_RELEASE.glb"
        output.write_bytes(scene.export(file_type="glb",include_normals=True))
        color_report=pin_neural_colors(source,output,native.vertices,newcore.vertices)
        loaded=trimesh.load(output,force="scene")
        assert len(loaded.geometry)==9
        assert len(loaded.geometry[CORE].faces)==len(newcore.faces)
        assert len(loaded.geometry[BARK].faces)==len(bark.faces)
        assert len(loaded.geometry[DOWN].faces)==36651
        assert loaded.geometry[CORE].is_watertight and loaded.geometry[CORE].volume>0
        ntri=sum(len(g.faces) for g in loaded.geometry.values())
        assert 80000<=ntri<=100000, ("total triangles outside budget",ntri)
        assert all(np.isfinite(g.vertices).all() for g in loaded.geometry.values())
        report["variants"][name]={
          "sigma_voxels":sigma,"blend_strength":strength,
          "volumetric_3d_isosurface_triangles_before_LOD":original_rebuilt_faces,
          "body_triangles_after_LOD":len(newcore.faces),
          "bark_triangles_after_LOD":len(bark.faces),
          "down_triangles_preserved":36651,
          "all_native_scene_triangles":ntri,"scene_mesh_count":len(loaded.geometry),
          "native_body_watertight":True,
          "native_body_positive_volume":float(newcore.volume),
          "bounds":np.round(loaded.bounds,4).tolist(),
          "bark_texture_sha256":hashfile(tex),
          "glb_filename":output.name,"glb_bytes":output.stat().st_size,
          "neural_vertex_rgb_source_transfer":color_report,
          "glb_sha256":hashfile(output),"art_approved":False,
          "physical_phone_gpu":"UNTESTED","release":"NO_RELEASE"}
    (outdir/"run250_machine_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",required=True)
    ap.add_argument("--outdir",required=True)
    a=ap.parse_args()
    run(a.source,Path(a.outdir))
