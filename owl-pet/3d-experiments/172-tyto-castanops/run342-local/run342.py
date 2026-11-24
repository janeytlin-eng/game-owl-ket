import numpy as np, trimesh, struct,json,hashlib,glob,sys
from pathlib import Path
from scipy.spatial import cKDTree
from PIL import Image,ImageDraw
import vtk
from vtk.util.numpy_support import vtk_to_numpy
p=Path(sys.argv[1]); out=Path(sys.argv[2]);out.mkdir(exist_ok=True)
raw=p.read_bytes(); assert hashlib.sha256(raw).hexdigest()=='e97a843849726e0e385797d44c53a7e584ce9aed6ba090d33b9da8e776333a52'
n=struct.unpack_from('<I',raw,12)[0];d=json.loads(raw[20:20+n]);buf=bytearray(raw[28+n:])
def acc(i):
 a=d['accessors'][i];v=d['bufferViews'][a['bufferView']];dt={5125:'<u4',5126:'<f4',5121:'u1'}[a['componentType']]; k={'SCALAR':1,'VEC2':2,'VEC3':3,'VEC4':4}[a['type']];return np.frombuffer(buf,dtype=dt,count=a['count']*k,offset=v.get('byteOffset',0)+a.get('byteOffset',0)).reshape(-1,k)
v=acc(1).copy(); f=acc(0).copy().reshape(-1,3); normals=acc(3).copy(); old=acc(5).copy();
# Use existing source atlas, prioritize low-coverage back and rear-side body, protect eyes/feet.
rng=np.random.default_rng(342); tri=v[f]; area=np.linalg.norm(np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]),axis=1);ids=rng.choice(len(f),size=15000,p=area/area.sum()); w=rng.random((len(ids),2)); w[w.sum(1)>1]=1-w[w.sum(1)>1]; w=np.c_[1-w.sum(1),w]; pts=(v[f[ids]]*w[:,:,None]).sum(1); ns=(normals[f[ids]]*w[:,:,None]).sum(1);ns/=np.linalg.norm(ns,axis=1)[:,None]; dist=cKDTree(old).query(pts)[0];mask=(pts[:,2]<0.02)&(pts[:,1]>-.52)&(ns[:,2]<.20)&(dist>.012);sel=np.where(mask)[0];sel=sel[np.argsort(-dist[sel])];# greedily distribute roots
chosen=[]
for i in sel:
 if not chosen or np.min(np.linalg.norm(pts[chosen]-pts[i],axis=1))>.045:chosen.append(i)
 if len(chosen)>=1300:break
roots=pts[chosen];nn=ns[chosen]; positions=[];uv=[];faces=[];nrm=[]
for q,norm in zip(roots,nn):
 t=np.array([0.,-1.,0.]);t-=norm*np.dot(t,norm)
 if np.linalg.norm(t)<.1:t=np.cross(norm,[1,0,0])
 t/=np.linalg.norm(t);side=np.cross(norm,t); L=rng.uniform(.045,.084);width=rng.uniform(.014,.026)
 for a in (0,np.pi/2):
  s=side*np.cos(a)+t*np.sin(a);base=len(positions)
  for j,u in enumerate((0,.45,1)):
   center=q+norm*(.004+L*u*(1-.23*u))+t*(L*.60*u*u);ww=width*(.40+.60*np.sin(np.pi*u))
   positions.extend([center-s*ww,center+s*ww]);uv.extend([[.21,u],[.79,u]]);nrm.extend([norm,norm])
  faces.extend([[base,base+1,base+2],[base+1,base+3,base+2],[base+2,base+3,base+4],[base+3,base+5,base+4]])
# Eye A/B color correction independently; no change to geometry of eyes.
acc(10)[:,:3]=[22,17,14];acc(14)[:,:3]=[12,10,9]
for ix in (10,14):
 d["accessors"][ix]["min"]=acc(ix).min(0).tolist();d["accessors"][ix]["max"]=acc(ix).max(0).tolist()
# append rear-groom accessor payloads, no previous primitive changed besides eye colors

def add(a,typ,ct):
 a=np.ascontiguousarray(a);off=len(buf);buf.extend(a.tobytes());buf.extend(b'\x00'*((-len(buf))%4));vi=len(d['bufferViews']);d['bufferViews'].append({'buffer':0,'byteOffset':off,'byteLength':a.nbytes});i=len(d['accessors']);ar=a.reshape(len(a),-1);d['accessors'].append({'bufferView':vi,'componentType':ct,'count':len(a),'type':typ,'min':ar.min(0).tolist(),'max':ar.max(0).tolist()});return i
attrs={'POSITION':add(np.array(positions,dtype='<f4'),'VEC3',5126),'NORMAL':add(np.array(nrm,dtype='<f4'),'VEC3',5126),'TEXCOORD_0':add(np.array(uv,dtype='<f4'),'VEC2',5126)};ind=add(np.array(faces,dtype='<u4').ravel(),'SCALAR',5125);d['meshes'].append({'name':'rear_targeted_down_research','primitives':[{'attributes':attrs,'indices':ind,'material':0}]});d['nodes'].append({'name':'rear_targeted_down_research','mesh':8});d['nodes'][0]['children'].append(9);d['buffers'][0]['byteLength']=len(buf);j=json.dumps(d,separators=(',',':')).encode();j+=b' '*((-len(j))%4);new=struct.pack('<4sII',b'glTF',2,28+len(j)+len(buf))+struct.pack('<I4s',len(j),b'JSON')+j+struct.pack('<I4s',len(buf),b'BIN\x00')+buf;target=out/'run342_rear_down_NOT_APPROVED.glb';target.write_bytes(new);s=trimesh.load(target,force='scene'); print('meshes',len(s.geometry),'faces',sum(len(m.faces) for m in s.geometry.values()))
report={'source_sha256':hashlib.sha256(raw).hexdigest(),'candidate_sha256':hashlib.sha256(new).hexdigest(),'bytes':len(new),'triangles':sum(len(m.faces) for m in s.geometry.values()),'rear_roots':len(chosen),'added_triangles':len(faces),'rear_candidate_points':len(sel),'median_root_distance_to_old_groom':float(np.median(dist[chosen])),'no_release':True}
# Actual offscreen render of same geometry, exact camera poses. VTK importer may not reproduce glTF alpha and color accurately.
ims=[]
for label,model in [('source',p),('candidate',target)]:
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(330,380);imp=vtk.vtkGLTFImporter();imp.SetFileName(str(model));imp.SetRenderWindow(win);imp.Update();ren=imp.GetRenderer();ren.SetBackground(.85,.87,.9);cam=ren.GetActiveCamera();cam.ParallelProjectionOn();cam.SetParallelScale(1.12);cam.SetViewUp(0,1,0)
 for tag,vec in [('front',(0,0,5)),('side',(5,0,0)),('back',(0,0,-5)),('rear3q',(3,0,-4))]:
  cam.SetPosition(*vec);cam.SetFocalPoint(0,.09,.10);ren.ResetCameraClippingRange();win.Render();w=vtk.vtkWindowToImageFilter();w.SetInput(win);w.Update();ar=vtk_to_numpy(w.GetOutput().GetPointData().GetScalars()).reshape(380,330,-1)[::-1];im=Image.fromarray(ar[:,:,:3]);im.save(out/f'{label}_{tag}.png');ims.append((f'{label} {tag}',im))
 win.Finalize()
mont=Image.new('RGB',(4*330,2*408),'white');dr=ImageDraw.Draw(mont)
for i,(label,im) in enumerate(ims):x=i%4*330;y=i//4*408;mont.paste(im,(x,y+26));dr.text((x+7,y+6),label,fill='black')
mont.save(out/'montage.jpg',quality=90);(out/'report.json').write_text(json.dumps(report,indent=2));print(report)
