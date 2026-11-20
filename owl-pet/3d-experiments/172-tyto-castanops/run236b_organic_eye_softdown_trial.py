#!/usr/bin/env python3
"""Run236: research-only anatomically placed cornea and soft-down trial on genuine Run235 neural GLB.
Not a completed pet; no production edits, payments, publishing, or mobile claims.
"""
import hashlib,json,os
from pathlib import Path
import numpy as np,trimesh,vtk
from PIL import Image,ImageDraw
from scipy.spatial import cKDTree
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray

OUT=Path(os.environ.get('RUN236_OUT',str(Path(__file__).resolve().parent/'run236-evidence')))
OUT.mkdir(parents=True,exist_ok=True)
SOURCE=OUT/'run235_real_neural_cream_3d_microdown_ART_REJECTED_NO_RELEASE.glb'
EXPECTED='97a2df9235310bea850f2a61db15b7930e90e1b9404bc9170cc98706c181dea2'
assert SOURCE.read_bytes()[:4]==b'glTF'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED
root=trimesh.load(SOURCE,force='scene')
core=root.geometry['neural_base_lod_REAL_3D'].copy()
fur=root.geometry['neural_surface_second_down_ribbons'].copy()
rng=np.random.default_rng(236172)
v=np.asarray(core.vertices).copy();col=core.visual.vertex_colors[:,:3].astype(float).copy()
x,y,z=v.T
back=np.clip((.21-z)/1.10,0,1)**1.25
v[:,2]+=back*.14
flank=np.clip((.27-y)/.8,0,1)*np.clip((np.abs(x)-.40)/.3,0,1)
v[:,0]*=1-.053*flank
for cx,cy in [(-.167,.570),(.210,.570)]:
 r=np.sqrt(((v[:,0]-cx)/.125)**2+((v[:,1]-cy)/.144)**2)
 f=np.clip((v[:,2]-.60)/.13,0,1)
 hood=np.clip((1.16-r)/.30,0,1)*f
 col=col*(1-.65*hood[:,None])+np.array([188.,155.,122.])*.65*hood[:,None]
 iris=np.clip((.57-r)/.12,0,1)*f
 col=col*(1-.75*iris[:,None])+np.array([74.,50.,32.])*.75*iris[:,None]
 pupil=np.clip((.35-r)/.08,0,1)*f
 col=col*(1-.94*pupil[:,None])+np.array([24.,19.,16.])*.94*pupil[:,None]
 glare=np.exp(-(((v[:,0]-(cx-.025))/.016)**2+((v[:,1]-(cy+.027))/.02)**2)*2.2)*f
 col=col*(1-.65*glare[:,None])+np.array([228.,212.,190.])*.65*glare[:,None]
body=np.clip((.22-v[:,1])/.55,0,1)*np.clip((.70-v[:,2])/.65,0,1)
col=col*(1-.22*body[:,None])+np.array([230.,210.,190.])*.22*body[:,None]
core.vertices=v
core.visual.vertex_colors=np.column_stack((np.clip(col,0,255).astype(np.uint8),np.full(len(v),255,np.uint8)))
# All 7,200 curved down tufts are sourced from the genuine three-dimensional Run235 feather geometry.
fv=np.asarray(fur.vertices).reshape(-1,5,3)
assert len(fv)==12217
parts=fv[rng.choice(len(fv),size=7200,replace=False)].copy()
anchor=parts[:,:2,:].mean(axis=1)
parts=anchor[:,None,:]+(parts-anchor[:,None,:])*.53
for j in range(5):
 xx,yy,zz=parts[:,j,:].T
 parts[:,j,2]+=np.clip((.21-zz)/1.10,0,1)**1.25*.14
 wf=np.clip((.27-yy)/.8,0,1)*np.clip((np.abs(xx)-.40)/.3,0,1)
 parts[:,j,0]*=1-.053*wf
n=len(parts);seq=np.arange(n)*5
ff=np.stack((np.stack((seq,seq+1,seq+2),axis=1),np.stack((seq+1,seq+3,seq+2),axis=1),np.stack((seq+2,seq+3,seq+4),axis=1)),axis=1).reshape(-1,3)
soft=trimesh.Trimesh(vertices=parts.reshape(-1,3),faces=ff,process=False)
fc=np.repeat(np.array([[238,218,199]],np.uint8),len(soft.vertices),axis=0).astype(float)
fc+=rng.normal(0,1.7,len(soft.vertices))[:,None]*np.array([1,.8,.65]);fc[4::5]=[232,214,196]
soft.visual.vertex_colors=np.column_stack((np.clip(fc,0,255).astype(np.uint8),np.full(len(fc),255,np.uint8)))
# Two small 3D cornea patches are only anatomical details, not generic primitive replacement for the bird.
front=v[v[:,2]>.58];tree=cKDTree(front[:,:2]);eyes=[]
for cx,cy in [(-.167,.570),(.210,.570)]:
 verts=[];colors=[];nr=8;nt=40
 for ri in range(nr+1):
  rr=ri/nr
  for t in range(nt):
   a=2*np.pi*t/nt;xx=cx+rr*.073*np.cos(a);yy=cy+rr*.079*np.sin(a)
   _,ix=tree.query([xx,yy],k=12);zz=np.max(front[np.asarray(ix),2])+.003+.023*(1-rr*rr)
   verts.append([xx,yy,zz]);cc=([22,17,13] if rr<.43 else [59,43,30] if rr<.69 else [125,95,66] if rr<.84 else [173,142,111])
   if ((xx-(cx-.020))**2/(.014**2)+(yy-(cy+.024))**2/(.016**2))<1 and rr<.53:cc=[216,205,190]
   colors.append(cc)
 fs=[]
 for k in range(nr):
  for j in range(nt):
   a=k*nt+j;b=k*nt+(j+1)%nt;c=(k+1)*nt+j;d=(k+1)*nt+(j+1)%nt
   fs.extend(((a,c,b),(b,c,d)))
 eye=trimesh.Trimesh(vertices=np.array(verts),faces=np.array(fs),process=False)
 eye.visual.vertex_colors=np.column_stack((np.array(colors,np.uint8),np.full(len(colors),255,np.uint8)));eyes.append(eye)
scene=trimesh.Scene()
for name,geo in [('neural_true3D_contiguous_core',core),('true3D_rooted_soft_down',soft),('left_anatomical_cornea_patch',eyes[0]),('right_anatomical_cornea_patch',eyes[1])]:scene.add_geometry(geo,geom_name=name)
output=OUT/'run236b_true3D_eyes_down_ART_REJECTED_NO_RELEASE.glb';scene.export(output)
re=trimesh.load(output,force='scene')
assert output.read_bytes()[:4]==b'glTF' and len(re.geometry)==4
assert all(np.isfinite(g.vertices).all() and (np.ptp(g.vertices,axis=0)>.01).all() for g in re.geometry.values())
def poly(g):
 d=vtk.vtkPolyData();p=vtk.vtkPoints();p.SetData(numpy_to_vtk(np.asarray(g.vertices,np.float32),deep=True));d.SetPoints(p)
 a=np.column_stack((np.full(len(g.faces),3,np.int64),g.faces.astype(np.int64))).ravel();cells=vtk.vtkCellArray();cells.SetCells(len(g.faces),numpy_to_vtkIdTypeArray(a,deep=True));d.SetPolys(cells)
 c=numpy_to_vtk(np.ascontiguousarray(g.visual.vertex_colors[:,:3]),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR);c.SetName('RGB');c.SetNumberOfComponents(3);d.GetPointData().SetScalars(c);return d
ren=vtk.vtkRenderer();ren.SetBackground(.91,.92,.94)
for g in (core,soft,*eyes):
 norm=vtk.vtkPolyDataNormals();norm.SetInputData(poly(g));norm.SplittingOff();mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norm.GetOutputPort());mapper.SetScalarModeToUsePointData();mapper.SetColorModeToDirectScalars()
 actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetInterpolationToPhong();actor.GetProperty().SetAmbient(.28);actor.GetProperty().SetSpecular(.28 if g in eyes else .06);ren.AddActor(actor)
window=vtk.vtkRenderWindow();window.SetOffScreenRendering(True);window.SetMultiSamples(0);window.SetSize(560,560);window.AddRenderer(ren)
b=np.array(ren.ComputeVisiblePropBounds());center=(b[::2]+b[1::2])/2;extent=max(b[1::2]-b[::2]);photos=[]
sheet=Image.new('RGB',(4*420,2*465),(244,245,247));draw=ImageDraw.Draw(sheet)
for i,(name,xyz) in enumerate([('front',(0,0,3)),('left',(-3,0,0)),('threequarter',(2,0,2)),('right',(3,0,0)),('back',(0,0,-3)),('top',(0,3,0)),('bottom',(0,-3,0))]):
 cam=ren.GetActiveCamera();cam.ParallelProjectionOn();cam.SetPosition(*(center+extent*np.array(xyz,float)));cam.SetFocalPoint(*center);cam.SetViewUp(*(0,1,0) if name not in ('top','bottom') else (0,0,1));cam.SetParallelScale(extent*.76);ren.ResetCameraClippingRange();window.Render()
 f=vtk.vtkWindowToImageFilter();f.SetInput(window);f.Update();path=OUT/f'run236b_{name}_real3D_ART_REJECTED.png';wr=vtk.vtkPNGWriter();wr.SetFileName(str(path));wr.SetInputConnection(f.GetOutputPort());wr.Write()
 im=Image.open(path).convert('RGB');sheet.paste(im.resize((416,416)),((i%4)*420,(i//4)*465+26));draw.text(((i%4)*420+5,(i//4)*465+5),name,fill='#222')
 a=np.asarray(im,dtype=np.int16);fg=int((np.max(abs(a-np.array([232,235,240])),axis=2)>38).sum());assert fg>10000
 photos.append({'view':name,'foreground_pixels':fg,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
window.Finalize();assert len({p['sha256'] for p in photos})==7
contact=OUT/'run236b_seven_real3D_views_ART_REJECTED_NO_RELEASE.png';sheet.save(contact)
report={'run':'236b','source_run235_sha256':EXPECTED,'native_glb_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'glb_bytes':output.stat().st_size,'neural_core_faces':len(core.faces),'down_faces':len(soft.faces),'ocular_detail_faces':sum(len(g.faces) for g in eyes),'eyes_natural_quality':'UNAPPROVED','fur_natural_quality':'UNAPPROVED','anatomy':'UNAPPROVED_ADULT_LIKE_WING','tree_hollow':'MISSING','phone_webgl':'UNTESTED','paid_cost_usd':0,'status':'TRUE_3D_TECH_PASS_ART_REJECTED_NO_RELEASE','views':photos,'contact_sha256':hashlib.sha256(contact.read_bytes()).hexdigest()}
(OUT/'run236b_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='views'},ensure_ascii=False))
