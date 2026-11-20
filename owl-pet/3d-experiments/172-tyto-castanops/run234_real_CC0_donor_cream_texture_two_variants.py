#!/usr/bin/env python3
"""Run234 real museum Tyto alba scan PBR cream texture A/B. NOT a juvenile character.
Source: Zenodo 21379215, adult scan, cc-zero metadata.
Do not release: adult flight feathers, tail, perch and poor down cannot pass v3 art gate.
"""
from pathlib import Path
import json,hashlib,traceback,datetime
import numpy as np,trimesh,vtk
from PIL import Image,ImageDraw
from skimage.color import rgb2lab,lab2rgb
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'run234-evidence';OUT.mkdir(parents=True,exist_ok=True)
SOURCE=OUT/'donor_uncompressed_adult.glb'
HASH='4865f48828adb93cef4f5ec07002adc1a61855a80adb286f781a227fca89430f'
R={'run':'234','date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'target':'#172 Tyto castanops v3 rightmost cream downy juvenile',
   'source':'https://zenodo.org/records/21379215','source_license':'Zenodo metadata cc-zero; legal provenance still needs review',
   'tested':'actual source scan texture transformation / true 3D GLB / seven cameras for each color',
   'extra_paid_usd':0,'release':'NO_RELEASE','art':'ART_REJECTED_BY_SCOPE',
   'phone_webgl':'NOT_TESTED','outputs':{}}
def stamp(p):
 p=Path(p);return {'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def render(sc,prefix):
 ren=vtk.vtkRenderer();ren.SetBackground(.89,.90,.91)
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(True);win.SetSize(440,440);win.SetMultiSamples(0);win.AddRenderer(ren)
 # CRITICAL: scene.dump() applies glTF node transform. Geometry alone is a rotated local coordinate frame.
 for i,m in enumerate(sc.dump()):
  if not isinstance(m,trimesh.Trimesh) or len(m.faces)==0:continue
  poly=vtk.vtkPolyData();p=vtk.vtkPoints();p.SetData(numpy_to_vtk(np.ascontiguousarray(m.vertices,dtype=np.float32),deep=True));poly.SetPoints(p)
  ff=np.column_stack([np.full(len(m.faces),3,dtype=np.int64),m.faces.astype(np.int64)]).ravel()
  cells=vtk.vtkCellArray();cells.SetCells(len(m.faces),numpy_to_vtkIdTypeArray(ff,deep=True));poly.SetPolys(cells)
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly);actor=vtk.vtkActor();actor.SetMapper(mapper)
  material=getattr(m.visual,'material',None)
  tex=getattr(material,'baseColorTexture',None)
  uv=getattr(m.visual,'uv',None)
  if tex is not None and uv is not None and len(uv)==len(m.vertices):
   png=OUT/f'{prefix}_PBR_atlas.png';Image.fromarray(np.array(tex)).convert('RGB').save(png)
   poly.GetPointData().SetTCoords(numpy_to_vtk(np.asarray(uv,dtype=np.float32),deep=True))
   reader=vtk.vtkPNGReader();reader.SetFileName(str(png));reader.Update()
   vt=vtk.vtkTexture();vt.SetInputConnection(reader.GetOutputPort());vt.InterpolateOn();actor.SetTexture(vt)
  ren.AddActor(actor)
 bounds=np.asarray(ren.ComputeVisiblePropBounds()).reshape(3,2);mid=bounds.mean(1);size=float(np.max(bounds[:,1]-bounds[:,0]))
 assert np.isfinite(bounds).all() and size>.1
 cams=[('left',(-3,0,0),(0,1,0)),('front',(0,0,3),(0,1,0)),('right',(3,0,0),(0,1,0)),
       ('back',(0,0,-3),(0,1,0)),('oblique',(2,1,2),(0,1,0)),('top',(0,3,0),(0,0,-1)),('bottom',(0,-3,0),(0,0,1))]
 ims=[];records=[]
 for name,pos,up in cams:
  cam=ren.GetActiveCamera();cam.ParallelProjectionOn();cam.SetPosition(*(mid+size*np.asarray(pos)));cam.SetFocalPoint(*mid)
  cam.SetViewUp(*up);cam.SetParallelScale(size*.70);ren.ResetCameraClippingRange();win.Render()
  fl=vtk.vtkWindowToImageFilter();fl.SetInput(win);fl.Update()
  pp=OUT/f'{prefix}_{name}_REAL_3D_ART_REJECTED.png'
  w=vtk.vtkPNGWriter();w.SetFileName(str(pp));w.SetInputConnection(fl.GetOutputPort());w.Write()
  a=np.asarray(Image.open(pp).convert('RGB')).astype(np.int16)
  fg=int((np.max(np.abs(a-np.array([227,230,232])),axis=2)>30).sum())
  uniq=int(np.unique(a.reshape(-1,3),axis=0).shape[0])
  assert fg>1000 and uniq>100,(name,fg,uniq)
  ims.append((name,pp));records.append({'camera':name,'foreground_pixels':fg,'rgb_colors':uniq,**stamp(pp)})
 win.Finalize()
 assert len(set(x['sha256'] for x in records))==7,'camera repetition'
 return ims,records
def main():
 assert SOURCE.is_file() and stamp(SOURCE)['sha256']==HASH
 scene=trimesh.load(SOURCE,force='scene',process=False)
 assert len(scene.geometry)==1
 m=next(iter(scene.geometry.values()))
 f=np.asarray(m.faces);v=np.asarray(m.vertices)
 edges=np.vstack([f[:,[0,1]],f[:,[1,2]],f[:,[2,0]]])
 conn=coo_matrix((np.ones(len(edges),np.int8),(edges[:,0],edges[:,1])),shape=(len(v),len(v))).tocsr()
 components,_=connected_components(conn,directed=False)
 R['source_mesh']={'glb':stamp(SOURCE),'faces':int(len(f)),'verts':int(len(v)),
                   'connected_components':int(components),'watertight':bool(m.is_watertight),
                   'scene_bounds':np.asarray(scene.bounds).round(6).tolist()}
 assert components>100
 img=np.asarray(m.visual.material.baseColorTexture.convert('RGB'))
 lab=rgb2lab(img/255.0)
 sets=[]
 for key,l_target,b_tint in [('warm_cream',89.0,12.0),('cool_ivory',92.0,5.0)]:
  lab2=lab.copy()
  lab2[:,:,0]=np.clip(l_target+(lab[:,:,0]-np.mean(lab[:,:,0]))*.26,68,99)
  lab2[:,:,1]=np.clip((lab[:,:,1]-np.mean(lab[:,:,1]))*.14+1.2,-4,6)
  lab2[:,:,2]=np.clip((lab[:,:,2]-np.mean(lab[:,:,2]))*.14+b_tint,0,20)
  tex=np.uint8(np.round(np.clip(lab2rgb(lab2),0,1)*255))
  obj=scene.copy();mm=next(iter(obj.geometry.values()));mm.visual.material.baseColorTexture=Image.fromarray(tex)
  mm.visual.material.roughnessFactor=.94;mm.visual.material.metallicFactor=0.
  dest=OUT/f'run234_{key}_real_photogrammetry_ADULT_NOT_JUVENILE.glb';obj.export(dest)
  assert dest.read_bytes()[:4]==b'glTF'
  imp=trimesh.load(dest,force='scene',process=False)
  meshes=[x for x in imp.geometry.values() if isinstance(x,trimesh.Trimesh)]
  assert len(meshes)==1 and len(meshes[0].faces)==len(f)
  assert np.isfinite(meshes[0].vertices).all() and (np.ptp(meshes[0].vertices,axis=0)>.1).all()
  ims,stats=render(imp,'run234_'+key)
  R['outputs'][key]={'GLB':stamp(dest),'triangles':int(len(f)),'seven_true_3d_views':stats}
  sets.append((key,ims))
 contact=Image.new('RGB',(7*240,2*260),(247,247,246));pen=ImageDraw.Draw(contact)
 for row,(key,ims) in enumerate(sets):
  for col,(name,pp) in enumerate(ims):
   x=col*240;y=row*260;pen.text((x+5,y+4),key+' '+name,fill=(30,30,30))
   contact.paste(Image.open(pp).convert('RGB').resize((234,234)),(x+3,y+23))
 sheet=OUT/'run234_14_TRUE_3D_VIEWS_TWO_MATERIALS_ART_REJECTED.png';contact.save(sheet)
 R['contact_sheet']=stamp(sheet)
 R['status']='TWO_TRUE_NATIVE_GLB_14_REAL_3D_CAMERAS_MATERIAL_TEST_ART_REJECTED_NO_RELEASE'
try:main()
except BaseException as e:
 R['status']='FAILED_NO_RELEASE';R['error']=repr(e);R['traceback']=traceback.format_exc()[-8000:]
finally:
 (OUT/'run234_machine_report.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'status':R['status'],'source':R.get('source_mesh'),'contact_sheet':R.get('contact_sheet'),'error':R.get('error')},ensure_ascii=False),flush=True)
