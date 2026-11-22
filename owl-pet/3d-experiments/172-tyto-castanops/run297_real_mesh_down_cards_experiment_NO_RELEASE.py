#!/usr/bin/env python3
"""#172 Run297 experimental physical 3D down feather ribbons on Run296 native GLB.
Research only / ART_REJECTED / RIGHTS_HOLD / NO_RELEASE.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from PIL import Image
import trimesh

P=argparse.ArgumentParser()
P.add_argument('--glb', required=True)
P.add_argument('--photo', required=True)
P.add_argument('--out', required=True)
P.add_argument('--tufts', type=int, default=9000)
P.add_argument('--seed', type=int, default=172297)
args=P.parse_args()
OUT=Path(args.out);OUT.mkdir(parents=True,exist_ok=True)
rng=np.random.default_rng(args.seed)
src=trimesh.load(args.glb,force='scene')
base=src.dump(concatenate=True)
assert len(base.faces)>10000, 'Run296 true native mesh absent'
original_triangles=len(base.faces)
trimesh.smoothing.filter_taubin(base,lamb=0.42,nu=-0.46,iterations=8)
V=base.vertices.copy(); N=base.vertex_normals.copy(); F=base.faces.copy()
photo=np.asarray(Image.open(args.photo).convert('RGB'))
H,W=photo.shape[:2]
lo=V.min(axis=0);hi=V.max(axis=0)
px=(V[:,0]-lo[0])/(hi[0]-lo[0])
py=(hi[1]-V[:,1])/(hi[1]-lo[1])
uvx=np.clip((px*.94+.03)*W,0,W-1).astype(int)
uvy=np.clip((py*.96+.02)*H,0,H-1).astype(int)
projected=photo[uvy,uvx].astype(float)
base_palette=np.array([226.,210.,185.])
frontweight=np.clip((N[:,2]-0.02)/0.55,0,1)*np.clip((V[:,2]-0.03)/0.4,0,1)
white=np.all(projected>245,axis=1);frontweight[white]*=.12
color=base_palette[None,:]*(1-frontweight[:,None])+projected*frontweight[:,None]
noise=rng.normal(0,3,len(V))[:,None]
color=np.clip(color+noise,20,250).astype(np.uint8)
mesh=trimesh.Trimesh(vertices=V,faces=F,process=False)
mesh.visual.vertex_colors=np.column_stack([color,np.full(len(color),255,dtype=np.uint8)])
P3,face_index=trimesh.sample.sample_surface(mesh,int(args.tufts*1.5),seed=args.seed)
M=mesh.face_normals[face_index]
protected=(P3[:,1]>.10)&(P3[:,2]>.35)&(abs(P3[:,0])<.45)
foot=P3[:,1]<-.72
mask=(~protected)&(~foot)&(np.linalg.norm(M,axis=1)>.95)
P3=P3[mask][:args.tufts]; M=M[mask][:args.tufts]
verts=[]; faces=[]; vc=[]
for k,(p,n) in enumerate(zip(P3,M)):
    tang=rng.normal(size=3);tang-=tang.dot(n)*n;tang/=max(np.linalg.norm(tang),1e-6)
    side=np.cross(n,tang);side/=max(np.linalg.norm(side),1e-6)
    length=float(rng.uniform(.018,.067))
    if p[1]>.50:length*=.68
    if p[2]<-.25:length*=1.15
    width=float(rng.uniform(.0022,.0072))
    lean=tang*rng.uniform(-.28,.28)+np.array([0,-.25,0])
    root=p-n*.002;mid=root+n*(length*.55)+lean*(length*.19)
    tip=root+n*length+lean*(length*.65)
    start=len(verts)
    verts.extend([root-side*width,root+side*width,mid-side*width*.58,mid+side*width*.58,tip])
    faces.extend([(start,start+1,start+2),(start+1,start+3,start+2),(start+2,start+3,start+4),
                  (start+2,start+1,start),(start+2,start+3,start+1),(start+4,start+3,start+2)])
    tint=np.clip(base_palette+rng.normal(0,9,3)+rng.choice([-10,0,10],p=[.15,.7,.15]),100,255)
    if p[1]>.48:tint=np.clip(tint+10,110,255)
    vc.extend([list(tint)+[255]]*2+[list(np.clip(tint+3,0,255))+[255]]*2+
              [list(np.clip(tint+10,0,255))+[255]])
fur=trimesh.Trimesh(vertices=np.asarray(verts),faces=np.asarray(faces),process=False)
fur.visual.vertex_colors=np.asarray(vc,dtype=np.uint8)
scene=trimesh.Scene()
scene.add_geometry(mesh,geom_name='smoothed-original-native-owl')
scene.add_geometry(fur,geom_name='down-feather-triangle-ribbons')
path=OUT/'run297-real-owl-with-down-UNAPPROVED.glb';scene.export(path)
verify=trimesh.load(path,force='scene')
rep={'run':297,'source_hash':hashlib.sha256(Path(args.glb).read_bytes()).hexdigest(),
 'photo_hash':hashlib.sha256(Path(args.photo).read_bytes()).hexdigest(),
 'base_original_triangles':original_triangles,'base_export_triangles':len(mesh.faces),
 'feather_strips':len(P3),'feather_triangles':len(fur.faces),
 'triangles_total':sum(len(g.faces) for g in verify.geometry.values()),
 'model_bytes':path.stat().st_size,'model_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'mesh_count':len(verify.geometry),'real_native_3d':True,
 'side_back_anatomy_verified':False,'face_and_juvenile_anatomy_verified':False,
 'physical_phone_verified':False,'rights_cleared':False,'art_approved':False,
 'release_allowed':False,'external_cost_usd':0,
 'technique':'real mesh, photo projected vertex colour, physically oriented geometry down ribbons',
 'warning':'Research only; fur does not fix wedge-shaped side, back, wing or facial topology.'}
(OUT/'run297_mesh_metrics.json').write_text(json.dumps(rep,indent=2),encoding='utf-8')
print(json.dumps(rep,indent=2))
