import glob,struct,json,hashlib
from pathlib import Path
import numpy as np,trimesh
from scipy.interpolate import PchipInterpolator
from PIL import Image,ImageDraw
import vtk
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
P=Path(__file__).parent
src=next(P.glob('run243-evidence/*variantC*'))
raw=src.read_bytes(); n=struct.unpack_from('<I',raw,12)[0]; orig=json.loads(raw[20:20+n]); binary=raw[28+n:]
def acc(d,b,i):
 a=d['accessors'][i]; v=d['bufferViews'][a['bufferView']]; dt={5126:'<f4',5125:'<u4',5123:'<u2',5121:'u1'}[a['componentType']]; k={'SCALAR':1,'VEC2':2,'VEC3':3,'VEC4':4}[a['type']]; return np.ndarray((a['count'],k),dtype=dt,buffer=b,offset=v.get('byteOffset',0)+a.get('byteOffset',0),strides=(v.get('byteStride',np.dtype(dt).itemsize*k),np.dtype(dt).itemsize))
def sm(a,b,x):
 t=np.clip((x-a)/(b-a),0,1);return t*t*(3-2*t)
# Juvenile posterior envelope, NOT observed side-view anatomy: a hypothesis.
yk=[-.82,-.72,-.58,-.40,-.20,0,.25,.48,.72,.99]; rear=[.05,-.12,-.32,-.43,-.46,-.43,-.36,-.28,-.20,.0]; width=[.27,.43,.55,.59,.60,.60,.56,.54,.45,.15]
r=PchipInterpolator(yk,rear);w=PchipInterpolator(yk,width)
def deform(v,strength):
 x,y,z=v.T; yc=np.clip(y,yk[0],yk[-1]); xc=np.clip(x/w(yc),-.999,.999); center=.19
 target=center-(center-r(yc))*np.sqrt(1-xc*xc)
 # only back half; front, beak, eyes and grounded toe region untouched.
 mask=(1-sm(-.10,.25,z))*sm(-.81,-.66,y)*(1-sm(.24,.65,y))
 # proportional posterior correction, rather than adding separate geometry
 q=v.copy();q[:,2]+=strength*mask*(target-z);return q

def pack(d,b):
 j=json.dumps(d,separators=(',',':')).encode();j+=b' '*(-len(j)%4);b=bytes(b);b+=b'\0'*(-len(b)%4);return struct.pack('<4sII',b'glTF',2,28+len(j)+len(b))+struct.pack('<I4s',len(j),b'JSON')+j+struct.pack('<I4s',len(b),b'BIN\0')+b

def make(label,strength):
 d=json.loads(json.dumps(orig));b=bytearray(binary); stats=[]
 for idx in [0,1]:
  p=d['meshes'][idx]['primitives'][0]; ai=p['attributes']['POSITION'];v=acc(d,b,ai);old=v.copy();norm=acc(d,b,p['attributes']['NORMAL']);oldn=norm.copy();q=deform(old,strength);v[:]=q
  # transform normals by inverse transpose of numerical deformation Jacobian
  eps=1e-4;J=np.stack([(deform(old+np.eye(3)[i]*eps,strength)-deform(old-np.eye(3)[i]*eps,strength))/(2*eps) for i in range(3)],axis=2)
  # singularity check before accepting geometry
  det=np.linalg.det(J); valid=abs(det)>1e-5; nn=oldn.copy(); nn[valid]=np.linalg.solve(J[valid].transpose(0,2,1),oldn[valid,:,None])[:,:,0];nn/=np.maximum(np.linalg.norm(nn,axis=1,keepdims=True),1e-8);norm[:]=nn
  d['accessors'][ai]['min']=q.min(0).tolist();d['accessors'][ai]['max']=q.max(0).tolist()
  stats.append({'mesh':idx,'max_displacement':float(np.linalg.norm(q-old,axis=1).max()),'nonpositive_jacobian':int((det<=0).sum())})
 out=P/f'run343_{label}_NO_RELEASE.glb';out.write_bytes(pack(d,b));s=trimesh.load(out,force='scene',process=False);return out,{'label':label,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'triangles':sum(len(g.faces) for g in s.geometry.values()),'deformation':stats}
def render(path):
 s=trimesh.load(path,force='scene',process=False);ren=vtk.vtkRenderer();ren.SetBackground(.89,.90,.92)
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(280,280);win.AddRenderer(ren)
 for idx,g in enumerate(s.geometry.values()):
  if idx==1:continue # geometry-only silhouette test; exclude alpha cards in all conditions
  points=vtk.vtkPoints();points.SetData(numpy_to_vtk(g.vertices,deep=True));cells=vtk.vtkCellArray();faces=np.column_stack([np.full(len(g.faces),3),g.faces]).astype(np.int64);cells.SetCells(len(g.faces),numpy_to_vtkIdTypeArray(faces.ravel(),deep=True));pd=vtk.vtkPolyData();pd.SetPoints(points);pd.SetPolys(cells)
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(pd);mapper.ScalarVisibilityOff();act=vtk.vtkActor();act.SetMapper(mapper);act.GetProperty().SetColor(*((.88,.79,.67) if idx==0 else (.14,.10,.07)));act.GetProperty().SetInterpolationToPhong();ren.AddActor(act)
 cam=ren.GetActiveCamera();cam.ParallelProjectionOn();cam.SetParallelScale(1.18);cam.SetFocalPoint(0,.08,.1);cam.SetViewUp(0,1,0)
 imgs=[]
 for pos in [(0,.08,4),(4,.08,.1),(0,.08,-4),(3,.08,-3)]:
  cam.SetPosition(*pos);ren.ResetCameraClippingRange();win.Render();f=vtk.vtkWindowToImageFilter();f.SetInput(win);f.Update();from vtk.util.numpy_support import vtk_to_numpy;im=vtk_to_numpy(f.GetOutput().GetPointData().GetScalars()).reshape(280,280,3)[::-1];imgs.append(Image.fromarray(im.copy()))
 win.Finalize();return imgs
if __name__=='__main__':
 results=[];cases=[('baseline',src)]
 for label,strength in [('A',.45),('B',.85)]:
  path,stats=make(label,strength);results.append(stats);cases.append((label,path))
 contact=Image.new('RGB',(1120,900),'white');draw=ImageDraw.Draw(contact)
 for j,(label,path) in enumerate(cases):
  for i,img in enumerate(render(path)):
   contact.paste(img,(i*280,j*300+20));draw.text((i*280+5,j*300+4),label+' '+['front','side','back','rear 3/4'][i],fill='black')
 contact.save(P/'run343_contact.jpg',quality=85);(P/'run343_report.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
