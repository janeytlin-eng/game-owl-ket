#!/usr/bin/env python3
"""Run245b: independent TRUE 3-D organic hollow support test for the real learned owl.
This makes a watertight weathered tree hollow with a smooth implicit 3-D volume.
It does NOT replace the original neural owl with primitives. Research only, NO RELEASE.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import scipy.ndimage as ndi
from scipy.spatial import cKDTree
from skimage.measure import marching_cubes
import trimesh

EXPECTED = "19274685ed19bb4c61b36a55b09048649a3db5c691aff2d75b1fe33831abf1ee"
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def organic_hollow(pitch=.028):
    rng=np.random.default_rng(172)
    xx=np.arange(-1.40,1.42,pitch,dtype=np.float32)
    yy=np.arange(-1.56,1.40,pitch,dtype=np.float32)
    zz=np.arange(-1.32,.64,pitch,dtype=np.float32)
    x,y,z=np.meshgrid(xx,yy,zz,indexing="ij",sparse=True)
    angle=np.arctan2(x,y+.18)
    outer=np.sqrt((x/1.06)**2+((y+.18)/1.09)**2)
    inner=np.sqrt((x/.78)**2+((y+.16)/.76)**2)
    crown=-.655+.98*(.5-.5*np.cos(angle))+.11*np.sin(angle)**4
    crown=crown+.055*np.sin(9*angle+3*z)+.025*np.sin(21*angle-8*z)
    floor=-.66+.018*np.sin(13*x+7*y)+.014*np.cos(8*y-5*x)
    detail=.042*np.sin(23*angle+2.2*z)+.022*np.sin(43*angle-7*z)
    shape=(len(xx),len(yy),len(zz))
    noise=ndi.zoom(rng.normal(0,1,(23,24,15)).astype("float32"),
                   (len(xx)/23,len(yy)/24,len(zz)/15),order=3)
    noise=noise[:len(xx),:len(yy),:len(zz)]
    detail=detail+.028*noise
    outer_field=1-outer+detail
    hollow_field=1-inner+.018*noise+.025*np.sin(17*angle+5*z)
    solid=np.minimum(np.minimum(.62*outer_field,2*(crown-z)),4*(z+1.29))
    cavity=np.minimum(.60*hollow_field,3*(z-floor))
    surface=ndi.gaussian_filter(np.minimum(solid,-cavity).astype(np.float32),sigma=.76)
    vertices,faces,_,_=marching_cubes(surface,level=0,spacing=(pitch,pitch,pitch))
    vertices+=np.array([xx[0],yy[0],zz[0]])
    bark=trimesh.Trimesh(vertices=vertices,faces=faces,process=False)
    bark.fix_normals()
    vx,vy,vz=vertices.T
    phi=np.arctan2(vx,vy+.18)
    radius=np.sqrt((vx/1.06)**2+((vy+.18)/1.09)**2)
    ridge=.5+.5*np.sin(27*phi+2*vz)+.24*np.sin(55*phi-7*vz)
    grain=.5+.5*np.sin(8*vz+11*phi)+.12*np.sin(19*vz+26*phi)
    t=np.clip(.52*ridge+.48*grain,0,1)
    inner_darken=(radius<.84).astype(float)
    color=np.stack([90+37*t,66+29*t,48+24*t],axis=1)
    color*=1-.28*inner_darken[:,None]
    color+=np.stack([2*np.sin(17*vz+vx),3*np.sin(11*vz+vy),
                     np.sin(13*vz+vx)],axis=1)
    colors=np.clip(np.c_[color,np.full(len(vx),255)],0,255).astype(np.uint8)
    mat=trimesh.visual.material.PBRMaterial(name="run245b_nonmetallic_weathered_eucalyptus",
        metallicFactor=0.0,roughnessFactor=.96,baseColorFactor=[255,255,255,255],
        doubleSided=True)
    vis=trimesh.visual.TextureVisuals(material=mat)
    vis.vertex_attributes["color"]=colors
    bark.visual=vis
    assert len(bark.faces)>10000 and bark.is_watertight
    return bark,dict(grid=list(map(int,shape)),vertices=len(bark.vertices),
                     triangles=len(bark.faces),watertight=bool(bark.is_watertight),
                     bbox=bark.bounds.round(4).tolist(),volume=float(bark.volume))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",required=True)
    ap.add_argument("--outdir",required=True)
    a=ap.parse_args()
    source=Path(a.source);out=Path(a.outdir);out.mkdir(parents=True,exist_ok=True)
    assert digest(source)==EXPECTED,"source neural GLB SHA mismatch"
    scene=trimesh.load(source,force="scene")
    assert len(scene.geometry)==8 and sum(len(g.faces) for g in scene.geometry.values())==86867
    originals={name:(len(mesh.vertices),len(mesh.faces))
               for name,mesh in scene.geometry.items()}
    bark,stats=organic_hollow()
    scene.add_geometry(bark,geom_name="organic_eucalypt_hollow_original_3D_SDF")
    path=out/"run245b_native_neural_owl_with_nonmetallic_organic_hollow_RESEARCH_ART_UNAPPROVED.glb"
    scene.export(path,include_normals=True)
    checked=trimesh.load(path,force="scene")
    assert len(checked.geometry)==9
    for name,mesh in checked.geometry.items():
        assert np.all(np.isfinite(mesh.vertices))
        if name in originals:
            assert (len(mesh.vertices),len(mesh.faces))==originals[name]
    core=checked.geometry["real_neural_owl_juvenile_core"]
    d,_=cKDTree(bark.vertices).query(core.vertices,k=1)
    low=core.vertices[:,2]<-.40
    report=dict(run="Run245b",source_sha256=EXPECTED,
                source_neural_owl_meshes_unchanged=True,
                output_file=path.name,output_bytes=path.stat().st_size,
                output_sha256=digest(path),scene_meshes=len(checked.geometry),
                all_geometry_explicit_normals=True,nonmetallic_bark_pbr=True,
                scene_triangles=sum(len(m.faces) for m in checked.geometry.values()),
                organic_hollow=stats,
                near_support_core_vertices=int(np.count_nonzero((d<.13)&low)),
                low_core_vertices=int(low.sum()),
                art_approved=False,physical_phone_gpu="UNTESTED",
                release="NO_RELEASE",paid_usd=0,
                status="TRUE_NATIVE_SCENE_TECH_ONLY_REQUIRES_ART_QA_NO_RELEASE")
    (out/"run245b_machine_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__":
    main()
