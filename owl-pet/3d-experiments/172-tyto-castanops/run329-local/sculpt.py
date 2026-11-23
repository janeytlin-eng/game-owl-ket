import numpy as np, trimesh, json, hashlib
from skimage.measure import marching_cubes
from scipy.ndimage import gaussian_filter
from pathlib import Path
P=Path(__file__).parent
rng=np.random.default_rng(172329)
# +Y forward, +Z up. normalized sculpt units, not measured biology.
step=.014
xs=np.arange(-.82,.83,step); ys=np.arange(-.73,.76,step); zs=np.arange(-.12,1.66,step)
x,y,z=np.meshgrid(xs,ys,zs,indexing='ij',sparse=True)
def ell(cx,cy,cz,a,b,c): return (np.sqrt(((x-cx)/a)**2+((y-cy)/b)**2+((z-cz)/c)**2)-1)*min(a,b,c)
def blend(a,b,k):
 h=np.maximum(k-np.abs(a-b),0)/k
 return np.minimum(a,b)-h*h*k*.25
f=ell(0,-.045,.69,.55,.43,.60)
f=blend(f,ell(0,.035,1.19,.445,.365,.405),.21)
for s in [-1,1]:
 f=blend(f,ell(s*.35,-.12,.70,.245,.29,.415),.15)
 f=blend(f,ell(s*.23,.055,.24,.19,.21,.26),.10)
# two bands of irregular sculpted volume, not hair planes
n=gaussian_filter(rng.normal(size=f.shape).astype('float32'),1.25); n/=n.std()
n2=gaussian_filter(rng.normal(size=f.shape).astype('float32'),3.8); n2/=n2.std()
f=f+.0035*n+.005*n2
v,fa,_,_=marching_cubes(f.astype('float32'),0,spacing=(step,step,step)); v+=np.array([xs[0],ys[0],zs[0]])
body=trimesh.Trimesh(v,fa,process=True); trimesh.repair.fix_normals(body)
shade=np.clip(.6+.10*rng.normal(size=len(v)),0,1)
base=np.array([222,202,174]); rgb=np.clip(base+shade[:,None]*np.array([24,30,37]),0,255)
body.visual.vertex_colors=np.column_stack((rgb,np.full(len(v),255))).astype('uint8')
# Facial surface is a hand-authored heart boundary with radial feather relief and orbital hollows.
# Catmull-Rom closed loop around the exact heart, top centre notch to right lobe and bottom point.
outline=np.array([[0,1.42],[.115,1.48],[.255,1.46],[.345,1.36],[.355,1.23],[.30,1.105],[.17,.995],[0,.925],[-.17,.995],[-.30,1.105],[-.355,1.23],[-.345,1.36],[-.255,1.46],[-.115,1.48]])
def loop(points,sub=12):
 a=[]
 for i in range(len(points)):
  p0,p1,p2,p3=[points[j%len(points)] for j in [i-1,i,i+1,i+2]]
  for t in np.arange(sub)/sub: a.append(.5*((2*p1)+(-p0+p2)*t+(2*p0-5*p1+4*p2-p3)*t*t+(-p0+3*p1-3*p2+p3)*t**3))
 return np.array(a)
edge=loop(outline); N=len(edge); R=30; center=np.array([0,1.23]); fv=[]; fc=[]
for i in range(R+1):
 r=max(.001,i/R); p=center+(edge-center)*r; X,Z=p.T
 # convex, continuous face surface; depress around dark eyes, ridge down central beak
 orbit=np.exp(-((np.abs(X)-.145)/.088)**2-((Z-1.285)/.088)**2)
 Y=.446-.105*r**1.7-.038*orbit+.028*np.exp(-(X/.062)**2)*np.exp(-((Z-1.21)/.17)**2)
 t=np.arange(N)*2*np.pi/N
 Y+=.0012*np.sin(t*47+r*13)*r+.006*np.exp(-((r-.94)/.035)**2)
 fv.extend(np.column_stack((X,Y,Z)))
 rim=np.exp(-((r-.93)/.058)**2); streak=(np.sin(t*47+r*13)+1)*.5
 col=np.array([233,218,192])[None,:]-rim*np.array([69,76,73])[None,:]-orbit[:,None]*np.array([58,63,62])+streak[:,None]*np.array([13,13,11])
 fc.extend(np.column_stack((np.clip(col,0,255),np.full(N,255))))
ff=[]
for i in range(R):
 for j in range(N):
  a=i*N+j;b=i*N+(j+1)%N;c=b+N;d=a+N;ff.extend([[a,b,c],[a,c,d]])
face=trimesh.Trimesh(fv,ff,process=False);face.visual.vertex_colors=np.array(fc,dtype='uint8');face.fix_normals()
if face.face_normals[:,1].mean()<0:face.invert()
# tapered, cupped 3D down barbs with feather flow, no billboards. Exclude facial area.
pts,ids=trimesh.sample.sample_surface(body,10500,seed=172329); ns=body.face_normals[ids]
keep=~((pts[:,1]>.18)&(pts[:,2]>.92)&(np.abs(pts[:,0])<.385))
pts,ns=pts[keep],ns[keep]; tangent=np.tile([0.,-.15,-1.],(len(pts),1));tangent-=ns*(tangent*ns).sum(1)[:,None];tangent/=np.maximum(np.linalg.norm(tangent,axis=1)[:,None],1e-6)
side=np.cross(ns,tangent); L=rng.uniform(.027,.088,len(pts)); W=rng.uniform(.0012,.004,len(pts)); tip=pts+ns*L[:,None]*.68+tangent*L[:,None]*.75
mid=pts+ns*L[:,None]*.55+tangent*L[:,None]*.2
vv=np.stack([pts-ns*.004,mid+side*W[:,None],mid+ns*W[:,None],mid-side*W[:,None],tip],axis=1).reshape(-1,3)
ff=np.array([[0,1,2],[0,2,3],[0,3,1],[1,4,2],[2,4,3],[3,4,1]])[None,:,:]+5*np.arange(len(pts))[:,None,None]
down=trimesh.Trimesh(vv,ff.reshape(-1,3),process=False); cols=np.clip(np.array([235,219,193])+rng.normal(0,7,(len(pts),1)),0,255).astype('uint8'); down.visual.vertex_colors=np.repeat(np.column_stack([cols,np.full(len(cols),255)]),5,axis=0)
def colored(m,c):m.visual.vertex_colors=np.tile(np.array([*c,255],dtype='uint8'),(len(m.vertices),1));return m
def egg(c,s,col):
 m=trimesh.creation.icosphere(subdivisions=3);m.vertices=m.vertices*np.array(s)+c;return colored(m,col)
parts={'body':body,'face':face,'down':down}
for s in [-1,1]:
 parts[f'eye{s}']=egg([s*.145,.427,1.285],[.055,.036,.059],[31,23,17]);parts[f'iris{s}']=egg([s*.145,.452,1.285],[.040,.012,.043],[14,12,10]);parts[f'glint{s}']=egg([s*.145-.015,.463,1.303],[.008,.004,.009],[225,222,207])
# Beak loft: tapered hook with real cross-sections (not cone). Feet intentionally not resolved in this experiment.
def loft(name,sections,color):
 verts=[];faces=[];K=24
 for cx,cy,cz,rx,ry in sections:
  t=np.arange(K)*2*np.pi/K;verts.extend(np.column_stack([cx+rx*np.cos(t),cy+ry*np.sin(t),np.full(K,cz)]))
 for i in range(len(sections)-1):
  for j in range(K):
   a=i*K+j;b=i*K+(j+1)%K;faces.extend([[a,b,b+K],[a,b+K,a+K]])
 m=trimesh.Trimesh(verts,faces,process=True);m.fix_normals();parts[name]=colored(m,color)
loft('beak',[(0,.435,1.245,.043,.022),(0,.467,1.205,.039,.047),(0,.492,1.152,.025,.033),(0,.48,1.105,.010,.015),(0,.457,1.082,.001,.001)],[187,155,111])
scene=trimesh.Scene(parts); path=P/'sculpt-NO_RELEASE.glb';path.write_bytes(scene.export(file_type='glb'));loaded=trimesh.load(path,force='scene')
report={'seed':172329,'geometry':{k:{'vertices':len(m.vertices),'triangles':len(m.faces)} for k,m in parts.items()},'triangles':sum(len(m.faces) for m in loaded.geometry.values()),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'body_watertight':bool(body.is_watertight),'down_barbs':len(pts),'loaded_geometries':len(loaded.geometry),'release':False,'foot_support':'unresolved'}
(P/'diagnostic.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))
