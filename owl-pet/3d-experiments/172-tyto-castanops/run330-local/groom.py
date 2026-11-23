import numpy as np, trimesh as tm, vtk, json, hashlib
from pathlib import Path
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray
from PIL import Image
O=Path(__file__).parent
# Curved 5 cm-scale chest swatch, deliberately NOT a complete bird.
rng=np.random.default_rng(172330)
N=44; X,Y=np.meshgrid(np.linspace(-.025,.025,N),np.linspace(-.025,.025,N)); Z=.008-5*(X*X+Y*Y)
base=tm.Trimesh(np.c_[X.ravel(),Y.ravel(),Z.ravel()],np.array([[i*N+j,i*N+j+1,(i+1)*N+j+1] for i in range(N-1) for j in range(N-1)]+[[i*N+j,(i+1)*N+j+1,(i+1)*N+j] for i in range(N-1) for j in range(N-1)]),process=False)
base.visual.vertex_colors=[212,190,159,255]
roots=rng.uniform(-.024,.024,(650,2)); seed=330

def groom(mode):
 r=np.random.default_rng(seed); V=[]; F=[]; C=[]
 def tube(p,rad,col):
  p=np.array(p); n=len(p); i=len(V); d=np.gradient(p,axis=0); d/=np.linalg.norm(d,axis=1)[:,None]; a=np.cross(d,[0,1,0]); a/=np.maximum(np.linalg.norm(a,axis=1)[:,None],1e-9); b=np.cross(d,a)
  for j in range(n):
   for k in range(3):
    theta=2*np.pi*k/3; V.append(p[j]+rad[j]*(a[j]*np.cos(theta)+b[j]*np.sin(theta))); C.append(col)
  for j in range(n-1):
   for k in range(3):
    q=i+j*3+k; w=i+j*3+(k+1)%3; F.extend([[q,w,w+3],[q,w+3,q+3]])
 if mode=='C':
  g=np.linspace(-.023,.023,26); xx,yy=np.meshgrid(g,g); rr=np.c_[xx.ravel(),yy.ravel()]+r.uniform(-.0008,.0008,(676,2))
 else: rr=roots
 for x,y in rr:
  z=.008-5*(x*x+y*y); origin=np.array([x,y,z-.00025]); length=r.uniform(.003,.006); shade=r.uniform(-12,9); col=np.clip(np.array([238,223,194,255])+np.array([shade,shade,shade,0]),0,255).astype(int)
  if mode=='A':
   for k in range(8):
    a=r.uniform(0,2*np.pi); delta=np.array([np.cos(a)*length*.55,np.sin(a)*length*.55,length*.8]); tube([origin,origin+delta*.5,origin+delta],[.000095,.000063,.000009],col)
  else:
   # Each down tuft has a shared curved stalk and flexible, spreading barbs;
   # C adds a second shallow undercoat. Fully spatial tubes, no billboards.
   lean=np.array([r.uniform(-.001,.001),-r.uniform(.001,.0028),length]); tip=origin+lean
   tube([origin,origin+lean*.5,tip],[.00009,.000055,.000008],col)
   for k in range(7):
    a=k*2.39996+r.uniform(-.3,.3); t=r.uniform(.12,.65); p=origin+lean*t; span=r.uniform(.0018,.0038); q=np.array([np.cos(a)*span,np.sin(a)*span-.0007,r.uniform(.0005,.0022)]); tube([p,p+q*.45+np.array([0,0,.0007]),p+q],[.00007,.000048,.000007],col)
   if mode=='C':
    for k in range(4):
     a=r.uniform(0,2*np.pi); q=np.array([np.cos(a)*.0018,np.sin(a)*.0018,r.uniform(.0008,.0018)]); tube([origin,origin+q*.5,origin+q],[.00013,.00010,.000014],[225,207,179,255])
 m=tm.Trimesh(V,F,vertex_colors=C,process=False); s=tm.Scene([base,m]); path=O/f'{mode}.glb'; path.write_bytes(s.export(file_type='glb')); re=tm.load(path,force='scene'); return s,{'triangles':sum(len(g.faces) for g in re.geometry.values()),'geometries':len(re.geometry),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

def render(s,mode):
 ren=vtk.vtkRenderer(); ren.SetBackground(.17,.19,.22); win=vtk.vtkRenderWindow(); win.SetOffScreenRendering(1); win.AddRenderer(ren); win.SetSize(480,480)
 for m in s.geometry.values():
  p=vtk.vtkPoints(); p.SetData(numpy_to_vtk(np.array(m.vertices),deep=True)); cells=vtk.vtkCellArray(); cells.SetCells(len(m.faces),numpy_to_vtkIdTypeArray(np.c_[np.full(len(m.faces),3),m.faces].astype(np.int64).ravel(),deep=True)); poly=vtk.vtkPolyData(); poly.SetPoints(p); poly.SetPolys(cells); colors=numpy_to_vtk(np.array(m.visual.vertex_colors,dtype=np.uint8),deep=True); colors.SetName('RGBA'); poly.GetPointData().SetScalars(colors); mapper=vtk.vtkPolyDataMapper(); mapper.SetInputData(poly); mapper.SetColorModeToDirectScalars(); actor=vtk.vtkActor(); actor.SetMapper(mapper); actor.GetProperty().SetAmbient(.28); actor.GetProperty().SetDiffuse(.72); ren.AddActor(actor)
 for j,pos in enumerate([(0,0,.13),(.085,-.07,.065),(0,-.12,.026)]):
  cam=ren.GetActiveCamera(); cam.SetPosition(*pos); cam.SetFocalPoint(0,0,.006); cam.SetViewUp(0,1,0 if j==0 else .1); cam.ParallelProjectionOn(); cam.SetParallelScale(.038); ren.ResetCameraClippingRange(); win.Render(); w=vtk.vtkWindowToImageFilter(); w.SetInput(win); w.Update(); writer=vtk.vtkPNGWriter(); writer.SetFileName(str(O/f'{mode}-{j}.png')); writer.SetInputConnection(w.GetOutputPort()); writer.Write()
 win.Finalize()
report={}
for mode in 'ABC':
 s,report[mode]=groom(mode); render(s,mode)
montage=Image.new('RGB',(1440,1440))
for i,mode in enumerate('ABC'):
 for j in range(3): montage.paste(Image.open(O/f'{mode}-{j}.png'),(j*480,i*480))
montage.save(O/'comparison.jpg',quality=92); montage.resize((240,240)).save(O/'evidence.jpg',quality=70)
(O/'report.json').write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2))
