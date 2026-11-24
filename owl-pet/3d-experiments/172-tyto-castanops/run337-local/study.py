import numpy as np, trimesh as t, vtk, hashlib, json
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray
from PIL import Image,ImageDraw
from pathlib import Path
out=Path(__file__).parent;rng=np.random.default_rng(337)
# Shared volumetric base; world-space, no UV singularities.
m=t.creation.icosphere(subdivisions=5);u=m.vertices.copy();f=m.faces.copy();scale=np.array([.64,.75,.49]);q=rng.normal(size=(16,3));q/=np.linalg.norm(q,axis=1)[:,None];q*=rng.uniform(35,90,(16,1));n=np.sin(u@q.T+rng.uniform(0,6.28,16)).mean(1)
p=u*(1+.018*n[:,None])*scale;c=np.clip(np.array([239,223,194])+n[:,None]*25,0,255).astype('uint8');base=t.Trimesh(p,f,vertex_colors=c,process=False)
# Sparse tapered, curved, physical microfilament tubes with branchlets; no alpha cards.
N=1900;roots=rng.normal(size=(N,3));roots/=np.linalg.norm(roots,axis=1)[:,None];v=[];faces=[];cols=[]
def tube(path,rad,color):
 k=len(v); axis=path[-1]-path[0];axis/=np.linalg.norm(axis);a=np.cross(axis,[0,1,0]);a/=max(np.linalg.norm(a),1e-9);b=np.cross(axis,a)
 for i,pt in enumerate(path):
  for j in range(3):
   ang=j*2*np.pi/3;v.append(pt+rad[i]*(np.cos(ang)*a+np.sin(ang)*b));cols.append(color)
 for i in range(len(path)-1):
  for j in range(3):
   x=k+i*3+j;y=k+i*3+(j+1)%3;faces.extend([[x,y,y+3],[x,y+3,x+3]])
for u0 in roots:
 normal=u0/scale;normal/=np.linalg.norm(normal);r=u0*scale*.992;tang=rng.normal(size=3);tang-=normal*np.dot(tang,normal);tang/=np.linalg.norm(tang);L=rng.uniform(.024,.056);s=np.linspace(0,1,4);path=r+s[:,None]*L*normal+s[:,None]**2*L*.8*tang;col=np.clip(np.array([245,232,209])+rng.normal(0,5),0,255).astype('uint8');tube(path,np.array([.0018,.0014,.0008,.00015]),col)
 for h,sign in [(1,1),(2,-1)]:
  side=np.cross(normal,tang)*sign;start=path[h];tube(np.array([start,start+L*.21*normal+L*.12*side,start+L*.37*normal+L*.27*side]),np.array([.001,.0006,.00012]),col)
groom=t.Trimesh(np.array(v),np.array(faces),vertex_colors=np.array(cols),process=False)
report={};imgs=[]
for name,scene in [('A_base',t.Scene(base)),('B_hybrid',t.Scene([base,groom]))]:
 path=out/(name+'.glb');scene.export(path);loaded=t.load(path,force='scene');mesh=loaded.to_geometry();report[name]={'triangles':len(mesh.faces),'vertices':len(mesh.vertices),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'meshes':len(loaded.geometry)}
 ren=vtk.vtkRenderer();ren.SetBackground(.15,.14,.13);win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(390,390);win.AddRenderer(ren);win.SetMultiSamples(4)
 for part in loaded.geometry.values():
  pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(part.vertices,deep=True));cells=vtk.vtkCellArray();cells.SetCells(len(part.faces),numpy_to_vtkIdTypeArray(np.column_stack([np.full(len(part.faces),3),part.faces]).astype('int64').ravel(),deep=True));pd=vtk.vtkPolyData();pd.SetPoints(pts);pd.SetPolys(cells);pd.GetPointData().SetScalars(numpy_to_vtk(part.visual.vertex_colors[:,:3].copy(),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR));norm=vtk.vtkPolyDataNormals();norm.SetInputData(pd);norm.SplittingOff();norm.Update();mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norm.GetOutputPort());mapper.SetColorModeToDirectScalars();actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetAmbient(.58);actor.GetProperty().SetDiffuse(.42);actor.GetProperty().SetSpecular(.005);ren.AddActor(actor)
 for i,a in enumerate([0,1.1,2.5]):
  cam=ren.GetActiveCamera();cam.SetPosition(2.8*np.sin(a),.35,2.8*np.cos(a));cam.SetFocalPoint(0,0,0);cam.SetViewUp(0,1,0);cam.ParallelProjectionOn();cam.SetParallelScale(.89);ren.ResetCameraClippingRange();win.Render();cap=vtk.vtkWindowToImageFilter();cap.SetInput(win);cap.Update();wr=vtk.vtkPNGWriter();wr.SetInputConnection(cap.GetOutputPort());p=out/f'{name}_{i}.png';wr.SetFileName(str(p));wr.Write();imgs.append(p)
 win.Finalize()
mont=Image.new('RGB',(1170,826),'white');d=ImageDraw.Draw(mont)
for i,p in enumerate(imgs):
 x=i%3*390;y=i//3*413;d.text((x+10,y+4),p.stem,fill='black');mont.paste(Image.open(p),(x,y+23))
mont.save(out/'montage.jpg',quality=88);mont.resize((234,165)).save(out/'tiny.jpg',quality=55);(out/'report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
