#!/usr/bin/env python3
"""Run250: real neural owl core, screened-graph surface-relief inpainting.
Research only. Does not create a bird using primitive components. Y-up, +Z-front.
"""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
import trimesh
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix,diags
from scipy.sparse.linalg import factorized

SOURCE_SHA='247d820538920735783072a204686fcf2f02ddb3ce1958a5472895a3ed7c1845'
CORE='real_neural_owl_juvenile_core'; DOWN='real_3d_surface_following_wispy_down'
def smooth(a,b,x):
 t=np.clip((x-a)/(b-a),0,1);return t*t*(3-2*t)
def gauss(x,s):return np.exp(-(x/s)**2)
def inverts(orig,now,faces):
 a=np.cross(orig[faces[:,1]]-orig[faces[:,0]],orig[faces[:,2]]-orig[faces[:,0]])
 b=np.cross(now[faces[:,1]]-now[faces[:,0]],now[faces[:,2]]-now[faces[:,0]])
 return int(((a*b).sum(axis=1)<0).sum())

def sculpt(v,f,variant):
 p=v.astype(float).copy();x,y,z=p.T
 front_face=smooth(.29,.60,y)*smooth(.42,.72,z)
 foot=(1-smooth(-.57,-.34,y))*smooth(.08,.39,z)
 head=smooth(.27,.50,y)
 side=smooth(.19,.42,np.abs(x))*smooth(-.57,-.37,y)*(1-head)
 wing=side*smooth(-.42,-.22,z)*(1-smooth(.21,.37,z))
 mask=np.clip(wing + .26*side*(1-front_face),0,1)
 protect=1-(1-front_face)*(1-foot)
 mask*=1-protect
 mask*=smooth(-.72,-.42,y)
 edges=np.unique(np.sort(np.vstack([f[:,[0,1]],f[:,[1,2]],f[:,[2,0]]]),axis=1),axis=0)
 I=np.r_[edges[:,0],edges[:,1]];J=np.r_[edges[:,1],edges[:,0]]
 deg=np.bincount(I,minlength=len(p)).astype(float)
 adj=coo_matrix((np.ones(len(I)),(I,J)),shape=(len(p),len(p))).tocsr()
 iters,base_weight,compact={'A':(12.,.85,.04),'B':(24.,1.0,.06)}[variant]
 strength=np.clip(mask*base_weight,0,1)
 L=diags(deg)-adj
 lam=float(iters)
 anchor=1/(1+lam*strength)**2
 anchor=np.maximum(anchor,.00025)
 A=(diags(anchor)+ 0.0018*L).tocsc()
 sol=factorized(A)
 fair=np.column_stack([sol(anchor*p[:,i]) for i in range(3)])
 d=fair-p
 q=p+strength[:,None]*d
 belly=smooth(.20,.48,np.abs(x))*gauss(y+.18,.27)*gauss(z-.24,.38)*(1-front_face)*(1-foot)
 q[:,0]+=np.sign(x)*compact*belly
 inv=inverts(p,q,f);alpha=1.
 while inv and alpha>1/512:
  alpha/=2
  inv=inverts(p,p+alpha*(q-p),f)
 q=p+alpha*(q-p)
 return q,dict(variant=variant,wing_vertices=int((mask>.3).sum()),smoothed_vertices=int((strength>.15).sum()),fairing_scale=alpha,flipped_faces=inverts(p,q,f),max_shift=float(np.linalg.norm(q-p,axis=1).max()),mean_wing_shift=float(np.linalg.norm(q-p,axis=1)[mask>.3].mean()),face_max_shift=float(np.linalg.norm(q-p,axis=1)[front_face>.9].max(initial=0)))

def main():
 a=argparse.ArgumentParser();a.add_argument('--source',required=True);a.add_argument('--outdir',required=True);opts=a.parse_args()
 src=Path(opts.source);h=hashlib.sha256(src.read_bytes()).hexdigest();assert h==SOURCE_SHA,(h,SOURCE_SHA)
 out=Path(opts.outdir);out.mkdir(exist_ok=True,parents=True)
 report={'run':'Run250','source_sha':h,'art_approved':False,'release':'NO_RELEASE','phone_gpu':'UNTESTED','variants':{}}
 for version in ('A','B'):
  s=trimesh.load(src,force='scene');core=s.geometry[CORE];fur=s.geometry[DOWN];v=core.vertices.copy();f=core.faces.copy()
  new,metrics=sculpt(v,f,version)
  ids=cKDTree(v).query(fur.vertices,k=1)[1]
  fur.vertices=fur.vertices+(new-v)[ids]
  core.vertices=new
  dst=out/f'run250_{version}_genuine_neural_wing_surface_inpaint_NO_RELEASE.glb'
  dst.write_bytes(s.export(file_type='glb',include_normals=True))
  re=trimesh.load(dst,force='scene')
  assert len(re.geometry)==9 and len(re.geometry[CORE].faces)==46856
  assert sum(len(g.faces) for g in re.geometry.values())==131835
  assert inverts(v,re.geometry[CORE].vertices,f)==0
  assert np.isfinite(re.geometry[CORE].vertices).all()
  metrics.update(bytes=dst.stat().st_size,sha256=hashlib.sha256(dst.read_bytes()).hexdigest(),triangles=sum(len(g.faces) for g in re.geometry.values()),meshes=len(re.geometry))
  report['variants'][version]=metrics
  print(metrics,flush=True)
 (out/'run250_geometry_report.json').write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':main()
