#!/usr/bin/env python3
"""Independent #172 owlet SDF / alpha-down geometry experiment. ART_REJECTED NO_RELEASE.
Anatomical SDF surface is a new true 3D sculpt, not an impostor or old neural mesh.
Rendering is a measurement only. No quality or phone acceptance.
"""
import sys, pathlib, hashlib, json, math, os
import numpy as np
from scipy.ndimage import gaussian_filter, map_coordinates
from scipy.spatial import cKDTree
from scipy.special import expit
from skimage.measure import marching_cubes
from PIL import Image
from matplotlib.path import Path
import trimesh
from trimesh.visual import ColorVisuals, TextureVisuals
from trimesh.visual.material import PBRMaterial

ref=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
sha=lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
assert sha(ref)=='8eee63bf0b8650c390d4c4bba6a07a0c2dd05dd7fc2e90e00a896ec3ab51c641'
rng=np.random.default_rng(172284)
N=169
xx=np.linspace(-.51,.51,N,dtype=np.float32)
yy=np.linspace(-.62,.58,N,dtype=np.float32)
zz=np.linspace(-.51,.54,N,dtype=np.float32)
X,Y,Z=np.meshgrid(xx,yy,zz,indexing='ij')
def ell(cx,cy,cz,rx,ry,rz):
 return (np.sqrt(((X-cx)/rx)**2+((Y-cy)/ry)**2+((Z-cz)/rz)**2)-1)*min(rx,ry,rz)
def blend(a,b,k):
 h=np.maximum(k-np.abs(a-b),0)/k
 return np.minimum(a,b)-h*h*k*.25
F=blend(ell(0,-.105,-.061,.340,.380,.285),ell(0,.226,-.005,.295,.264,.265),.080)
for side in [-1,1]:
 F=blend(F,ell(side*.284,-.105,-.073,.085,.212,.203),.051)
 F=blend(F,ell(side*.155,-.378,.015,.080,.087,.115),.033)
F+=.0027*np.sin(X*37+np.sin(Y*19)*1.8)*np.sin(Y*33-Z*19)+.0016*np.sin(Z*53+Y*22)
F=gaussian_filter(F,sigma=.58)
v,f,_,_=marching_cubes(-F,0,spacing=(xx[1]-xx[0],yy[1]-yy[0],zz[1]-zz[0]))
v+=np.array([xx[0],yy[0],zz[0]]);v[:,0]*=1.105;v[:,1]*=.955
body=trimesh.Trimesh(vertices=v,faces=f,process=False)
if body.volume<0:body.invert()
assert body.is_watertight and len(body.faces)>100000
T=np.linspace(0,2*np.pi,1500)
heart=np.column_stack([.245*1.105*(16*np.sin(T)**3)/17,.197*.955+.234*.955*(13*np.cos(T)-5*np.cos(2*T)-2*np.cos(3*T)-np.cos(4*T))/17])
isheart=Path(heart).contains_points(v[:,:2])
near=cKDTree(heart).query(v[:,:2],workers=1)[0]
sd=np.where(isheart,near,-near)
x,y,z=v.T;face=np.clip((z-.17)/.15,0,1)
rim=np.exp(-(sd/.016)**2)*face
heartmask=expit(sd/.012)*face*np.clip((y+.10)/.12,0,1)
body.vertices[:,2]+=(.012*heartmask+.011*rim+.008*np.exp(-(x/.039)**2-(y/.14-1.12)**2))*np.clip((z-.12)/.18,0,1)
x,y,z=body.vertices.T
rgb=np.asarray(Image.open(ref).convert('RGB'),dtype=float)
u=np.clip(256+x*398,0,511);w=np.clip(247-y*455,0,511)
photo=np.stack([map_coordinates(rgb[:,:,j],[w,u],order=1,mode='nearest') for j in range(3)],axis=1)
p=np.clip((np.linalg.norm(photo-128,axis=1)-7)/36,0,1)
light=np.clip((body.vertex_normals[:,2]+.02)/.85,0,1)*np.clip((z+.005)/.37,0,1)*p*.82
neutral=np.stack([241+6*y,222+10*y,202+11*y],axis=1)
color=neutral*(1-light[:,None])+photo*light[:,None]
color=color*(1-rim[:,None]*.12)+np.array([183,141,102])*rim[:,None]*.12
color*=1-.075*(np.exp(-((np.abs(x)-.33)/.04)**2)*np.exp(-((y+.12)/.2)**4))[:,None]
body.visual=ColorVisuals(mesh=body,vertex_colors=np.column_stack([np.clip(color,0,255).astype(np.uint8),np.full(len(v),255,dtype=np.uint8)]))
scene=trimesh.Scene();scene.add_geometry(body,geom_name='one_continuous_organic_owl_body')
def add(m,c,name):
 m.visual=ColorVisuals(mesh=m,vertex_colors=np.tile(np.array([*c,255],dtype=np.uint8),(len(m.vertices),1)))
 scene.add_geometry(m,geom_name=name)
def front_z(px,py):
 depths=np.linspace(.54,.10,181); pts=np.array([(px-xx[0])/(xx[1]-xx[0]),(py-yy[0])/(yy[1]-yy[0]),(depths-zz[0])/(zz[1]-zz[0])])
 val=map_coordinates(F,pts,order=1,mode='nearest')
 idx=np.where(val<0)[0]
 return depths[idx[0]] if len(idx) else .32
for s in [-1,1]:
 cx=s*.118;cy=.210;cz=front_z(cx/1.105,cy/.955)+.009
 for name,r,d,c in [('eye',.026,-.009,[17,13,13]),('iris',.022,-.004,[27,20,15]),('spec',.0047,.018,[255,250,241])]:
  mesh=trimesh.creation.uv_sphere(radius=r,count=[32,24])
  mesh.apply_translation([cx,cy,cz+d]);add(mesh,c,name+str(s))
# physically curved, tapered beak loft
vertices=[];faces=[]
for i,t in enumerate(np.linspace(0,1,18)):
 center=np.array([0,.110-.122*t,.373+.029*t+.018*np.sin(np.pi*t*.9)])
 r=.021*(1-t)**.68+.001
 for a in np.linspace(0,2*np.pi,16,endpoint=False):
  vertices.append(center+[r*np.cos(a),r*np.sin(a),-.009*np.cos(a)+.003*np.sin(a)])
for i in range(17):
 for j in range(16):
  a=i*16+j;b=i*16+(j+1)%16;faces += [(a,b,a+16),(b,b+16,a+16)]
add(trimesh.Trimesh(vertices=vertices,faces=faces,process=False),[207,184,155],'curved_beak')
def tube(nodes,radii):
 nodes=np.array(nodes,float);v=[];f=[]
 for i,p in enumerate(nodes):
  t=nodes[min(i+1,len(nodes)-1)]-nodes[max(i-1,0)];t/=np.linalg.norm(t)
  side=np.cross(t,[0,1,0]);side/=np.linalg.norm(side)
  up=np.cross(t,side);up/=np.linalg.norm(up)
  for a in np.linspace(0,2*np.pi,10,endpoint=False):
   v.append(p+radii[i]*(side*np.cos(a)+up*np.sin(a)))
 for i in range(len(nodes)-1):
  for j in range(10):
   a=10*i+j;b=10*i+(j+1)%10;f.extend([(a,a+10,b),(b,a+10,b+10)])
 return trimesh.Trimesh(vertices=v,faces=f,process=False)
for side in [-1,1]:
 root=np.array([side*.16,-.40,.12])
 add(tube([root,root+[0,-.026,.05],root+[0,-.064,.14]],[.029,.027,.018]),[204,185,163],f'leg{side}')
 for j,offset in enumerate([-.075,-.035,.015,.052]):
  s=side*.155+offset
  pts=[[side*.16,-.435,.215],[s,-.45,.259],[s+offset*.5,-.447,.312],[s+offset*.55,-.478,.339]]
  add(tube(pts,[.019,.016,.011,.006]),[191,173,156],f'toe{side}_{j}')
  p=pts[-1]
  add(tube([p,[p[0]+offset*.09,p[1]-.012,p[2]+.023],[p[0]+offset*.13,p[1]-.043,p[2]+.034]],[.008,.005,.0008]),[110,94,77],f'claw{side}_{j}')
# masked feather geometry; cutout texture has real RGBA and UV, not painted pseudo-hair
n=128; arr=np.zeros((n,n,4),dtype=np.uint8)
for row in range(n):
 t=row/(n-1)
 for col in range(n):
  u=col/(n-1)-.5; width=.43*(1-t)**.58*(.65+.35*np.sin(np.pi*t))
  edge=abs(u)/(width+1e-4)
  noise=.5+.5*np.sin(107*u+10*t)*np.sin(47*u-27*t)
  alpha=255*max(0,1-edge)**.65*(.65+.35*noise)
  if t<.045:alpha*=t/.045
  if t>.975:alpha*=max(0,(1-t)/.025)
  arr[row,col]=[255,int(246-10*t),int(230-14*t),int(alpha)]
tex=Image.fromarray(arr,'RGBA');tex.save(out/'alpha_down_128.png')
samples,fi=trimesh.sample.sample_surface(body,19000,seed=172284)
norms=body.face_normals[fi]
mask=(samples[:,1]>-.43)&(samples[:,1]<.47)&(samples[:,2]>-.35)&(samples[:,2]<.46)
mask &= ~(Path(heart).contains_points(samples[:,:2])&(samples[:,2]>.16))
mask &= ~((samples[:,1]>.07)&(samples[:,2]>.18)&(np.abs(samples[:,0])<.26))
choices=np.flatnonzero(mask);fv=[];ft=[];ff=[]
for i in rng.choice(choices,size=3600,replace=len(choices)<3600):
 p=samples[i];nor=norms[i];nor=nor/np.linalg.norm(nor)
 t=np.array([rng.normal(0,.29),-1.,rng.normal(0,.3)]);t-=np.dot(t,nor)*nor
 if np.linalg.norm(t)<.05:continue
 t/=np.linalg.norm(t)
 s=np.cross(nor,t);s/=np.linalg.norm(s)
 length=rng.uniform(.031,.061);width=rng.uniform(.009,.020);phase=rng.uniform(-.5,.5)
 for a in range(2):
  side=np.cos(a*np.pi*.5+phase)*s+np.sin(a*np.pi*.5+phase)*np.cross(nor,s)
  side/=np.linalg.norm(side);start=len(fv)
  for zeta,shape in [(0,.55),(.3,1.),(.67,.78),(1,.02)]:
   c=p+nor*(.003+.007*zeta)+zeta*t*length+nor*.006*np.sin(np.pi*zeta)
   c[1]-=length*.19*zeta*zeta
   for sign in [-1,1]:
    fv.append(c+sign*side*width*shape);ft.append([0 if sign<0 else 1,zeta])
  for j in range(3):
   q=start+j*2;ff.extend([(q,q+1,q+2),(q+1,q+3,q+2)])
fur=trimesh.Trimesh(vertices=np.array(fv),faces=np.array(ff),process=False)
fur.visual=TextureVisuals(uv=np.array(ft),material=PBRMaterial(name='alpha_mask_real_down',baseColorTexture=tex,baseColorFactor=[255,255,255,255],emissiveFactor=[.22,.19,.16],metallicFactor=0,roughnessFactor=1,alphaMode='MASK',alphaCutoff=.3,doubleSided=True))
base=scene.copy()
scene.add_geometry(fur,geom_name='real_uv_alpha_mask_feathers')
result={}
for name,s in [('organic_base',base),('organic_alpha',scene)]:
 path=out/f'run284_{name}_RESEARCH_NO_RELEASE.glb'
 path.write_bytes(trimesh.exchange.gltf.export_glb(s,include_normals=True))
 chk=trimesh.load(path,force='scene')
 tri=sum(len(g.faces) for g in chk.geometry.values())
 result[name]={'bytes':path.stat().st_size,'sha256':sha(path),'real_triangles':tri,'mesh_count':len(chk.geometry),'root_count':3600 if name=='organic_alpha' else 0,'art':'UNAPPROVED_NO_RELEASE'}
 assert tri>100000
(out/'run284_machine_report.json').write_text(json.dumps({'reference_sha256':sha(ref),'versions':result,'art':'REQUIRES_MANUAL_REJECTION_REVIEW','real_phone':'UNTESTED','rights':'UNCLEARED','release':False},indent=2))
print(json.dumps(result,indent=2))
