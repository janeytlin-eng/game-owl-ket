#!/usr/bin/env python3
"""Run255: native learned 3D source; UV/PBR warm cream-down microtexture and actual 3D ocular enlargement experiment. Not art approved."""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw,ImageFilter
import trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals
SRC_SHA='cd1513ac0822eef25bb56f9f8d08d244cac64d209ea8c92333693d287c926eb6'
CORE='real_neural_owl_juvenile_core'
DOW='real_3d_surface_following_wispy_down'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def texture(seed,amount=1.0,sz=1024):
    rng=np.random.default_rng(seed)
    a=rng.normal(size=(sz,sz)).astype(np.float32)
    im=Image.fromarray(np.uint8(np.clip((a+3)*255/6,0,255)))
    blurred=np.asarray(im.filter(ImageFilter.GaussianBlur(radius=18)),dtype=np.float32)/255
    soft=np.asarray(im.filter(ImageFilter.GaussianBlur(radius=2)),dtype=np.float32)/255
    v=np.linspace(0,1,sz,dtype=np.float32)[:,None]
    warm=(.80+.055*np.cos((v-.36)*3.1)+.045*(blurred-.5)+.03*(soft-.5))*amount+(1-amount)*.85
    base=np.empty((sz,sz,3),dtype=np.uint8)
    base[:,:,0]=np.clip(246+28*(warm-.82),0,255).astype(np.uint8)
    base[:,:,1]=np.clip(237+30*(warm-.82),0,255).astype(np.uint8)
    base[:,:,2]=np.clip(218+28*(warm-.82),0,255).astype(np.uint8)
    layer=Image.new('RGBA',(sz,sz),(0,0,0,0));d=ImageDraw.Draw(layer,'RGBA')
    count=14000 if seed==2551 else 24000
    for i in range(count):
        x=int(rng.integers(0,sz));y=int(rng.integers(0,sz))
        l=float(rng.uniform(3,12 if seed==2551 else 15))
        bend=float(rng.normal(0,2.2))
        col=(121,96,61,int(rng.uniform(4,15))) if rng.random()<.42 else (255,249,225,int(rng.uniform(18,35)))
        d.line([(x,y),(x+bend*.3,y+l*.48),(x+bend,y+l)],fill=col,width=1,joint='curve')
    merged=Image.alpha_composite(Image.fromarray(base,'RGB').convert('RGBA'),layer).convert('RGB')
    hf=np.array(layer.getchannel('A').filter(ImageFilter.GaussianBlur(.9)),dtype=np.float32)/255
    gy,gx=np.gradient(hf)
    strength=2.7 if seed==2551 else 3.5
    nx=-strength*gx;ny=-strength*gy;nz=np.ones_like(nx)
    norm=np.sqrt(nx**2+ny**2+nz**2)
    nrm=np.stack((nx/norm,ny/norm,nz/norm),axis=-1)
    normal=Image.fromarray(np.clip((nrm*.5+.5)*255,0,255).astype(np.uint8),'RGB')
    return merged,normal,count
def main(src,outdir):
    src=Path(src);outdir=Path(outdir);outdir.mkdir(parents=True,exist_ok=True)
    assert sha(src)==SRC_SHA,(sha(src),'WRONG_BASE')
    base=trimesh.load(src,force='scene');assert CORE in base.geometry and DOW in base.geometry
    r={'run':'255','source':src.name,'source_sha256':SRC_SHA,'release':'NO_RELEASE','art_approved':False,'phone_hardware':'UNTESTED','variants':{}}
    for v,seed in [('A',2551),('B',2552)]:
        scene=trimesh.load(src,force='scene');g=scene.geometry[CORE]
        uv=np.column_stack(((np.arctan2(g.vertices[:,0],g.vertices[:,2])/(2*np.pi)+.5)%1,np.clip((g.vertices[:,1]+.82)/1.80,0,1)))
        albedo,normal,strokes=texture(seed)
        albedo.save(outdir/f'run255_{v}_cream_down_albedo.png');normal.save(outdir/f'run255_{v}_normal.png')
        g.visual=TextureVisuals(uv=uv,material=PBRMaterial(baseColorTexture=albedo,normalTexture=normal,metallicFactor=0,roughnessFactor=.98,baseColorFactor=[255,255,255,255],doubleSided=True))
        scale=1.16 if v=='A' else 1.25
        for start in (0,3):
            eye=scene.geometry[f'sculpt_anatomical_eye_detail_{start}']
            c=np.array(eye.centroid);c[2]-=.005
            for j in range(3):
                eg=scene.geometry[f'sculpt_anatomical_eye_detail_{start+j}']
                eg.vertices=c+(eg.vertices-c)*np.array([scale,scale,1.06 if v=='A' else 1.10])
        path=outdir/f'run255_{v}_native_neural_cream_down_PBR_UNAPPROVED_NO_RELEASE.glb'
        path.write_bytes(scene.export(file_type='glb',include_normals=True))
        chk=trimesh.load(path,force='scene')
        assert len(chk.geometry)==9 and len(chk.geometry[CORE].faces)==34000
        assert chk.geometry[CORE].visual.uv is not None
        assert chk.geometry[CORE].visual.material.baseColorTexture is not None
        assert chk.geometry[CORE].visual.material.normalTexture is not None
        assert chk.geometry[CORE].is_watertight and chk.geometry[CORE].volume>0
        assert len(chk.geometry[DOW].faces)==36651
        meta={'sha256':sha(path),'bytes':path.stat().st_size,'meshes':len(chk.geometry),
              'triangles':sum(len(q.faces) for q in chk.geometry.values()),
              'core_closed':bool(chk.geometry[CORE].is_watertight),'source_triangles':34000,
              'groom_faces':36651,'uv_vertices':len(uv),'normalTexture_pass':True,
              'baked_fiber_strokes':strokes,'eye_scale':scale,'art_approved':False}
        r['variants'][v]=meta;print(json.dumps({v:meta}),flush=True)
    (outdir/'run255_geometry_report.json').write_text(json.dumps(r,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--outdir',required=True);a=p.parse_args();main(a.source,a.outdir)
