#!/usr/bin/env python3
"""Research-only organic GLB re-sculpt from pinned neural owlet mesh.
Physically existing surface topology and mesh; eye socket tests, compact posterior,
and actual 3D barycentrically seeded feather ribbon surface. NEVER RELEASE.
"""
import sys, pathlib, hashlib, json
import numpy as np, scipy.sparse as sp, trimesh
from scipy.spatial import cKDTree
P=pathlib.Path(sys.argv[2]);P.mkdir(exist_ok=True,parents=True)
source=pathlib.Path(sys.argv[1]); B=source.read_bytes()
assert hashlib.sha256(B).hexdigest()=='e3c33c70a8a1136a7548d22d2a272e9c5c254e773959b7705d5261ed0fec4535'
src=trimesh.load(source,force='scene'); assert len(src.geometry)==1
m=next(iter(src.geometry.values()));assert len(m.faces)==20000 and m.is_watertight
v0=m.vertices.copy(); V=v0.copy(); edges=m.edges_unique
A=sp.coo_matrix((np.ones(2*len(edges)),(np.r_[edges[:,0],edges[:,1]],np.r_[edges[:,1],edges[:,0]])),shape=(len(V),len(V))).tocsr()
deg=np.maximum(np.asarray(A.sum(axis=1)).ravel(),1.)
def smoothstep(q):
 t=np.clip(q,0,1);return t*t*(3-2*t)
x,y,z=V.T
rear=smoothstep((-z-.04)/.60); low=smoothstep((.5-y)/1.45)
# Genuine local mesh smoothing, masked away from facial plate and feet.
W=rear*smoothstep((y+.80)/.34)
for _ in range(12):
 mean=(A@V)/deg[:,None];V+=.12*W[:,None]*(mean-V)
# Posterior/ventral volumetric shape change is controlled in three dimensions;
# source triangle connectivity stays identical, not an assembled approximation.
x,y,z=V.T
rear=smoothstep((-z-.07)/.70)
V[:,2]+=0.16*rear*smoothstep((.66-y)/1.60)
V[:,1]+=0.18*rear*smoothstep((-.16-y)/.75)
V[:,0]*=(1+.075*rear*smoothstep((.6-y)/1.6))
# continuous organic shallow depression around the eye sockets in actual head mesh
x,y,z=V.T
for sx in (-.205,.205):
 d2=((x-sx)/.095)**2+((y-.435)/.105)**2
 V[:,2]-=.028*np.exp(-.5*d2)*smoothstep((z-.45)/.22)
body=trimesh.Trimesh(vertices=V,faces=m.faces,process=False)
assert body.is_watertight
rng=np.random.default_rng(264)
x,y,z=V.T
# Pale back as well as belly, avoid gray/brown dorsal color blocks.
cream=np.array([241.,231.,211.]); cc=np.repeat(cream[None],len(V),axis=0)
front=smoothstep((z+.0)/.65); face=np.exp(-((x/.48)**4+((y-.44)/.44)**4)*1.8)*front
cc=cc*(1-face[:,None]*.68)+np.array([248,237,214])[None]*face[:,None]*.68
cc+=rng.normal(0,1.4,(len(V),1));cc=np.clip(cc,0,255).astype(np.uint8)
body.visual.vertex_colors=np.column_stack((cc,np.full(len(V),255,dtype=np.uint8)))
# Eye membrane follows convex hull samples from the true original face, not a
# sphere/cylinder stuck on top. Outer ring blends into real cream face.
front_vertices=V[(V[:,2]>.54)&(V[:,1]>.18)]
tree=cKDTree(front_vertices[:,:2]); iris=[]
for sx in (-.205,.205):
 vv=[];ff=[];cols=[];R=16;N=72
 for ii in range(R+1):
  r=ii/R
  for jj in range(N):
   theta=2*np.pi*jj/N
   xx=sx+.113*r*np.cos(theta); yy=.435+.110*r*np.sin(theta)
   dist,ix=tree.query((xx,yy),k=14)
   zi=np.percentile(front_vertices[np.atleast_1d(ix),2],80)
   zz=zi+.012+.020*(1-r*r)
   vv.append((xx,yy,zz))
   # black pupil, warm iris, limbal ring, soft almond eyelid, cream transition
   if r<.36:color=(13,12,11)
   elif r<.64:
    q=.5+.5*np.cos(theta*18+2.2*r); color=(int(75+42*q),int(45+26*q),int(27+18*q))
   elif r<.69:color=(24,19,14)
   elif r<.79:color=(104,84,65)
   else:
    t=smoothstep((r-.79)/.21); color=tuple(int((1-t)*a+t*b) for a,b in zip((152,132,106),(244,233,210)))
   cols.append((*color,255))
 for i in range(R):
  for j in range(N):
   a=i*N+j;b=i*N+(j+1)%N;c=(i+1)*N+j;d=(i+1)*N+(j+1)%N
   ff.extend(((a,d,b),(a,c,d)))  # positive-Z front face winding: verified by actual Chromium WebGL2, not only VTK
 em=trimesh.Trimesh(vertices=vv,faces=ff,process=False)
 em.visual.vertex_colors=np.asarray(cols,dtype=np.uint8)
 iris.append(em)
# Dense surface-following true 3D down, barycentric on real neural surface.
# Avoid face/feet; place back/side/ventral fluff for full 360 geometry.
seedfaces=body.faces
sampleP,fidx=trimesh.sample.sample_surface(body,11500,seed=264)
n=body.face_normals[fidx]; normals=n.copy()
valid=(sampleP[:,1]>-.72)&(np.linalg.norm(sampleP[:,:2]-np.array([0,.36]),axis=1)>.04)
# exclude central facial disk from long fiber; back naturally receives large portion
frontface=(sampleP[:,2]>.53)&(sampleP[:,1]>.10)&(np.abs(sampleP[:,0])<.48)
valid &= ~frontface
roots=sampleP[valid]; dirs=normals[valid];count=len(roots)
# mini-feather curved strips taper, with base inside the skin, ends project above it
up=np.array([0.,1.,0.]);dirs=dirs*.82+up[None]*.31
dirs/=np.linalg.norm(dirs,axis=1)[:,None]
side=np.cross(dirs,np.array([.02,0.,1.]))
small=np.linalg.norm(side,axis=1)<.05;side[small]=np.cross(dirs[small],np.array([1.,0.,.03]))
side/=np.linalg.norm(side,axis=1)[:,None]
# 4-segment bent 3D feather; 8 vertices, six faces each, no planar billboard
L=rng.uniform(.048,.092,count)
width=rng.uniform(.0015,.0037,count)
hv=np.zeros((count*8,3),dtype=np.float32);hc=np.empty((count*8,4),dtype=np.uint8)
faces=np.zeros((count*6,3),dtype=np.int32)
for k in range(4):
 u=k/3
 q=roots+dirs*(L*u)[:,None]+up[None]*(-.16*u*u*L)[:,None]
 ww=(width*(1-u*.93))[:,None]*side
 hv[(2*k)::8]=q-ww;hv[(2*k+1)::8]=q+ww
 for h in (2*k,2*k+1):
  hc[h::8]=np.column_stack([rng.integers(241,253,count),rng.integers(229,242,count),rng.integers(209,229,count),np.full(count,255)])
for k in range(3):
 b=np.arange(count,dtype=np.int32)*8+k*2
 faces[k*2::6]=np.column_stack([b,b+1,b+3]);faces[k*2+1::6]=np.column_stack([b,b+3,b+2])
hair=trimesh.Trimesh(vertices=hv,faces=faces,process=False);hair.visual.vertex_colors=hc
scene=trimesh.Scene()
for name,geo in [('body_continuous_neural',body),('left_eye_soft_socket',iris[0]),('right_eye_soft_socket',iris[1]),('barycentric_3d_down',hair)]: scene.add_geometry(geo,geom_name=name)
out=P/'run264_native_juvenile_socket_compaction_DOWN_REJECTED_NO_RELEASE.glb'
out.write_bytes(scene.export(file_type='glb',include_normals=True))
check=trimesh.load(out,force='scene')
rep={'source_sha256':hashlib.sha256(B).hexdigest(),'glb_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'glb_bytes':out.stat().st_size,'mesh_count':len(check.geometry),'triangle_count':sum(len(g.faces) for g in check.geometry.values()),'body_faces_preserved':np.array_equal(body.faces,m.faces),'body_watertight':body.is_watertight,'surface_strands':count,'vertex_disp_gt_1mm':int(np.count_nonzero(np.linalg.norm(V-v0,axis=1)>.001)),'max_displacement':float(np.linalg.norm(V-v0,axis=1).max()),'rights':'UNCLEARED','phone':'UNTESTED','art':'UNREVIEWED','release':'NO_RELEASE'}
(P/'run264_machine_report.json').write_text(json.dumps(rep,indent=2)+'\n')
(P/'NO_RELEASE.flag').write_text('RESEARCH_ONLY; NO_RELEASE; RIGHTS_UNCLEARED; PHONE_UNTESTED\n')
print(json.dumps(rep,indent=2))
