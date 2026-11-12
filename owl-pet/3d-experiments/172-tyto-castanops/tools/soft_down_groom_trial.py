#!/usr/bin/env python3
"""#172 RESEARCH-ONLY alpha microdown groom over CC0 owl mesh; never art-approved.

Adult owl anatomy does not become a Tasmanian masked owl chick just because
cream hair cards are added. Requires a real downloaded source GLB.
"""
import argparse, hashlib, json, math
from pathlib import Path
import numpy as np
from PIL import Image
import trimesh
from trimesh.visual.texture import TextureVisuals
from trimesh.visual.material import PBRMaterial

MATERIALS={'Authored owl coat','Original overlapping avian coverts','Original closed folded remiges'}

def feather_texture():
    w,h=96,192
    yy,xx=np.mgrid[0:h,0:w].astype(np.float32)
    t=yy/(h-1)
    traverse=(xx/(w-1)-.5)*2
    center=.075*np.sin(t*18)+.035*np.sin(t*61)
    taper=.78*(1-t)**.72+.055
    edge=np.clip((taper-np.abs(traverse-center))/.18,0,1)
    alpha=(edge*np.clip((1-t)*6,0,1)*np.clip(t*18,0,1)*
           (.72+.18*np.cos(traverse*25+t*13)**2)*250).astype(np.uint8)
    a=np.ones((h,w,4),dtype=np.uint8)
    a[:,:,:3]=[250,245,229]
    a[:,:,3]=alpha
    return Image.fromarray(a,'RGBA')

def build(source,out,clumps=7000,alpha_mode='MASK',seed=172):
    rng=np.random.default_rng(seed)
    scene=trimesh.load(str(source),force='scene',process=False)
    selected=[]; meta=[]
    for k,g in scene.geometry.items():
        if len(g.faces)<40:continue
        mat=getattr(g.visual,'material',None)
        name=getattr(mat,'name','')
        if name in MATERIALS:
            selected.append(g)
            meta.append({'mesh':k,'material':name,'area':round(float(g.area),5),
                         'triangles':int(len(g.faces))})
    if not selected:raise ValueError('No material-qualified real owl mesh: do not create pretend geometry')
    main=trimesh.util.concatenate(selected)
    bounds=scene.bounds
    height=float(bounds[1,1]-bounds[0,1])
    width=float(bounds[1,0]-bounds[0,0])
    zmax=float(bounds[1,2]); zmin=float(bounds[0,2]);depth=zmax-zmin
    if not (.05<height<20 and width>0 and depth>0):raise ValueError('Invalid source bounds')
    attempt=int(clumps*2.0)
    area=main.area_faces
    ids=rng.choice(len(main.faces),size=attempt,p=area/area.sum())
    triangles=main.triangles[ids]
    r1=np.sqrt(rng.random(attempt));r2=rng.random(attempt)
    points=(triangles[:,0]*(1-r1)[:,None]+triangles[:,1]*(r1*(1-r2))[:,None]+
            triangles[:,2]*(r1*r2)[:,None])
    normals=main.face_normals[ids]
    yr=(points[:,1]-bounds[0,1])/height
    xr=(points[:,0]-(bounds[0,0]+bounds[1,0])/2)/(width/2)
    zr=(points[:,2]-zmin)/depth
    # Exclude supposed forward face region; orientation must be independently QA'd.
    face_zone=(yr>.58)&(yr<.92)&(np.abs(xr)<.63)&(zr>.78)
    keep=(yr>.20)&(~face_zone)&(np.linalg.norm(normals,axis=1)>.99)
    points=points[keep][:clumps];normals=normals[keep][:clumps]
    if len(points)<clumps*.6:raise ValueError('Actual surface points insufficient')
    vertices=[];uv=[];faces=[]
    base_len=height*.035
    for p,n in zip(points,normals):
        n=n/np.linalg.norm(n)
        axis=np.array([0.,1.,0.]) if abs(n[1])<.85 else np.array([1.,0.,0.])
        t1=np.cross(n,axis);t1/=np.linalg.norm(t1)
        t2=np.cross(n,t1)
        angle=rng.uniform(0,2*math.pi)
        tangent=t1*math.cos(angle)+t2*math.sin(angle)
        d=n*.79+tangent*.61;d/=np.linalg.norm(d)
        length=base_len*rng.uniform(.63,1.33)
        halfw=length*rng.uniform(.13,.24)
        for ang in (0,math.pi/2):
            wvec=t1*math.cos(ang+angle)+t2*math.sin(ang+angle)
            root=p+n*(height*.0015);tip=root+d*length
            i=len(vertices)
            vertices.extend([root-wvec*halfw,root+wvec*halfw,
                             tip+wvec*halfw*.10,tip-wvec*halfw*.10])
            uv.extend([[0,0],[1,0],[1,1],[0,1]])
            faces.extend([[i,i+1,i+2],[i,i+2,i+3]])
    mat=PBRMaterial(name='Research-only cream transparent mesoptile down',
                    baseColorTexture=feather_texture(),metallicFactor=0.,
                    roughnessFactor=.98,alphaMode=alpha_mode,alphaCutoff=.32,doubleSided=True)
    groom=trimesh.Trimesh(vertices=np.asarray(vertices),faces=np.asarray(faces),
                         process=False,visual=TextureVisuals(uv=np.asarray(uv),material=mat))
    scene.add_geometry(groom,geom_name=f'down_groom_{alpha_mode}_{len(points)}')
    scene.export(str(out))
    check=trimesh.load(str(out),force='scene',process=False)
    return {'source':str(source),'source_sha256':hashlib.sha256(Path(source).read_bytes()).hexdigest(),
            'output':str(out),'sha256':hashlib.sha256(Path(out).read_bytes()).hexdigest(),
            'selected_meshes':len(meta),'materials':sorted({m['material'] for m in meta}),
            'groom_cards':len(points)*2,'groom_triangles':len(groom.faces),
            'scene_triangles':sum(len(g.faces) for g in check.geometry.values()),
            'size_bytes':Path(out).stat().st_size,
            'model_approved':False,'source_is_Tyto_castanops_juvenile':False,
            'face_orientation_verified':False,'mobile_webgl_verified':False,
            'alpha_overdraw':'not yet measured',
            'note':'Adult geometry/eyes/feet remain anatomically unsuitable; first test of microdown only'}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('source');p.add_argument('output')
    p.add_argument('--count',type=int,default=7000)
    p.add_argument('--mode',choices=['MASK','BLEND'],default='MASK')
    p.add_argument('--stats')
    a=p.parse_args()
    result=build(a.source,a.output,a.count,a.mode)
    text=json.dumps(result,indent=2)
    print(text)
    if a.stats:Path(a.stats).write_text(text)
