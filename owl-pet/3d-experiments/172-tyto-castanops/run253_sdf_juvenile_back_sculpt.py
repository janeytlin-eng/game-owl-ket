#!/usr/bin/env python3
"""Run253 research-only: native Hunyuan voxel signed-distance posterior resurfacing.
No simple primitive assembly: sculpt an already learned continuous organic mesh.
Licensed source: user project's Run251 A original Hunyuan mesh, SHA256 pin.
Y up, +Z front. Output is NOT art approved unless separately visually reviewed.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np, scipy.ndimage as ndi
from scipy.spatial import cKDTree
from skimage.measure import marching_cubes
import trimesh
PIN='cd1513ac0822eef25bb56f9f8d08d244cac64d209ea8c92333693d287c926eb6'
CORE='real_neural_owl_juvenile_core'
DOWN='real_3d_surface_following_wispy_down'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def smooth(a,b,x):
    t=np.clip((x-a)/(b-a),0,1)
    return t*t*(3-2*t)
def native_juvenile_sdf(core,variant,pitch=0.016):
    vox=core.voxelized(pitch).fill();pad=15
    occ=np.pad(vox.matrix.astype(np.float32),pad)
    xyz=[np.arange(occ.shape[j])*pitch+vox.translation[j]-pad*pitch for j in range(3)]
    x,y,z=np.meshgrid(*xyz,indexing='ij',sparse=True)
    # Existing true Hunyuan 3D signed distance retains learned face and body surface detail.
    sm=ndi.gaussian_filter(occ,1.5)
    inside=sm>.48
    sdf=ndi.distance_transform_edt(~inside).astype(np.float32)*pitch-ndi.distance_transform_edt(inside).astype(np.float32)*pitch
    # Native posterior feather carve: continuously move only the learned rear surface
    # forward, while preserving actual feet/chest/head, no separate owl shape added.
    if variant=='A':
        rear=-.225-.08*smooth(-.2,.5,y)
        cutstrength=.98
        sigma=1.45
    elif variant=='B':
        rear=-.155-.075*smooth(-.1,.5,y)
        cutstrength=1.0
        sigma=2.15
    else:raise ValueError(variant)
    trimfield=(rear-z).astype(np.float32)
    shoulder=1-smooth(.49,.76,y)
    lower=smooth(-.69,-.48,y)
    cutmask=np.clip(shoulder*lower,0,1)
    field=np.maximum(sdf,cutstrength*trimfield*cutmask)
    blurred=ndi.gaussian_filter(field,sigma)
    smoothzone=(1-smooth(.1,.3,z))*(1-smooth(.56,.76,y))
    field=(1-smoothzone)*field+smoothzone*blurred
    if variant=='B':
        torso=smooth(-.70,-.45,y)*(1-smooth(.10,.42,y))*(1-smooth(.25,.53,z))
        tor_smooth=ndi.gaussian_filter(field,2.4)
        field=field*(1-.44*torso)+tor_smooth*(.44*torso)
    fv,ff,_,_=marching_cubes(field,level=0.,spacing=(pitch,)*3)
    fv += np.array([q[0] for q in xyz]); out=trimesh.Trimesh(vertices=fv,faces=ff,process=False)
    chunks=sorted(out.split(only_watertight=False),key=lambda g:len(g.faces),reverse=True)
    assert len(chunks)>0
    out=chunks[0]
    if out.volume<0:out.invert()
    assert out.is_watertight and out.volume>0
    tree=cKDTree(core.vertices)
    dist, neighbors=tree.query(out.vertices, k=12)
    out.visual=trimesh.visual.TextureVisuals(material=core.visual.material.copy())
    if 'color' in core.visual.vertex_attributes:
        # Weighted local interpolation, not nearest-neighbor-only vertex color.
        weight=np.exp(-0.5*(dist/.075)**2) / np.maximum(dist, .008)**.65
        weight=weight/np.maximum(weight.sum(axis=1,keepdims=True),1e-6)
        colors=core.visual.vertex_attributes['color'][neighbors].astype(np.float32)
        out.visual.vertex_attributes['color']=np.clip(np.sum(colors*weight[:,:,None],axis=1),0,255).astype(np.uint8)
    info={'pitch':pitch,'grid':occ.shape,'original_vertices':len(core.vertices),'remesh_vertices':len(out.vertices),'remesh_triangles':len(out.faces),'core_watertight':bool(out.is_watertight),'core_volume':float(out.volume),'rear_min_z':float(out.bounds[0,2]),'core_bounds':out.bounds.tolist(),'components':len(chunks),'dropped_component_triangles':[len(c.faces) for c in chunks[1:]]}
    return out,info

def generate(src,outdir):
    src=Path(src); outdir=Path(outdir);outdir.mkdir(parents=True,exist_ok=True)
    assert sha(src)==PIN, ('source integrity wrong',sha(src))
    source=trimesh.load(src,force='scene')
    report={'run':'Run253','source_sha256':PIN,'source_kind':'original Hunyuan learned native 3D neural owl','independent_scene_owl_spheres':False,'axis':'Y_UP','art_approved':False,'phone_gpu':'UNTESTED','extra_paid_usd':0,'release':'NO_RELEASE','variants':{}}
    for variant in 'AB':
        scene=trimesh.load(src,force='scene');oldcore=scene.geometry[CORE];fur=scene.geometry[DOWN]
        newcore,metrics=native_juvenile_sdf(oldcore,variant)
        nearestold=cKDTree(oldcore.vertices).query(fur.vertices,k=1)[1]
        nearestnew=cKDTree(newcore.vertices).query(oldcore.vertices[nearestold],k=1)[1]
        old_fur=fur.vertices.copy()
        offset=old_fur-oldcore.vertices[nearestold]
        norm=np.linalg.norm(offset,axis=1,keepdims=True)
        fur.vertices=newcore.vertices[nearestnew]+offset*np.minimum(1,.023/np.maximum(norm,1e-7))
        scene.geometry[CORE]=newcore
        target=outdir/f'run253_{variant}_native_neural_juvenile_posterior_resculpt_ART_UNAPPROVED_NO_RELEASE.glb'
        target.write_bytes(scene.export(file_type='glb',include_normals=True))
        reloaded=trimesh.load(target,force='scene')
        cc=reloaded.geometry[CORE];pupil=reloaded.geometry['sculpt_anatomical_eye_detail_1']
        assert cc.is_watertight and cc.volume>0
        assert len(reloaded.geometry)==len(source.geometry)==9
        assert pupil.visual.material.baseColorFactor[0]<20
        assert all(np.isfinite(g.vertices).all() for g in reloaded.geometry.values())
        metrics.update({'file':target.name,'sha256':sha(target),'bytes':target.stat().st_size,'meshes':len(reloaded.geometry),'triangles':int(sum(len(g.faces) for g in reloaded.geometry.values())),'eye_pbr_dark_maintained':True,'actual_3d_down_vertices':len(fur.vertices),'technical_native_glb':'PASS','art_approved':False})
        report['variants'][variant]=metrics
        print(variant,json.dumps(metrics),flush=True)
    (outdir/'run253_geometry_report.json').write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--outdir',required=True);a=p.parse_args();generate(a.source,a.outdir)
