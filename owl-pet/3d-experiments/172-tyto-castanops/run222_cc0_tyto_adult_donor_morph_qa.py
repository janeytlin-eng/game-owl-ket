#!/usr/bin/env python3
"""Run222: independently download real CC0 Tyto owl donor, native morph GLB and 7-view QA; NO_RELEASE."""
import os,json,hashlib,pathlib,datetime,traceback
import requests,numpy as np,trimesh
from PIL import Image,ImageDraw
OUT=pathlib.Path('owl-pet/3d-experiments/172-tyto-castanops/run222-evidence')
OUT.mkdir(exist_ok=True,parents=True)
SRC='https://3dassets.dev/api/v1/packs/birds-and-reptiles-hd'
EXPECTED='881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d'
REPORT={'run':222,'target':'#172 Tyto castanops v3 rightmost cream mesoptile',
  'source_pack':SRC,'source_license_claim':'CC0 1.0, 3DAssets.dev',
  'material':'Adult barn owl anatomical donor, NOT accepted juvenile',
  'additional_paid_usd':0,'release':'NO_RELEASE','art':'NOT_ACCEPTED',
  'mobile_hardware':'NOT_TESTED','main_changed':False,'production_changed':False,
  'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':{},'files':{}}
def digest(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return {'bytes':p.stat().st_size,'sha256':h.hexdigest()}
def walk(x):
 if isinstance(x,dict):
  yield x
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
def candidate(data):
 found=[]
 for d in walk(data):
  label=' '.join(str(d.get(k,'')) for k in ('name','title','slug','displayName','display_name')).strip().lower()
  if not ('barn owl' in label or 'barn-owl' in label):continue
  urls=[]
  for sub in walk(d):
   for k,v in sub.items():
    if isinstance(v,str) and v.startswith('https://') and ('.glb' in v.lower() or k.lower() in ('cdnurl','modelurl','downloadurl','glb_url','file_url','url') and '.glb' in v.lower()):urls.append(v)
  if urls:found.append((label,urls[0]))
 return found
def download(url,path):
 with requests.get(url,timeout=(20,120),stream=True) as r:
  REPORT['checks']['download_http']={'code':r.status_code,'type':r.headers.get('Content-Type'),'final_url':r.url}
  r.raise_for_status()
  n=0
  with path.open('wb') as f:
   for b in r.iter_content(1048576):
    if b:
     n+=len(b)
     if n>80_000_000:raise RuntimeError('size cap exceeded')
     f.write(b)
 if path.stat().st_size<1000 or path.open('rb').read(4)!=b'glTF':raise RuntimeError('GLB magic failed')
def stats(sc):
 return {'mesh_count':len(sc.geometry),'triangles':int(sum(len(g.faces) for g in sc.geometry.values())),
  'vertices':int(sum(len(g.vertices) for g in sc.geometry.values())),
  'bounds':np.array(sc.bounds).round(4).tolist()}
def morph(sc):
 """A deliberately limited adult anatomical donor morph, NOT authentic juvenile sculpture."""
 parts=sc.dump()
 if isinstance(parts,trimesh.Trimesh):parts=[parts]
 a=np.vstack([x.vertices for x in parts if isinstance(x,trimesh.Trimesh)])
 lo,hi=a.min(axis=0),a.max(axis=0)
 if hi[1]-lo[1]<1e-6:raise RuntimeError('no upright y extent')
 xmid,zmid=(lo[0]+hi[0])/2,(lo[2]+hi[2])/2
 out=trimesh.Scene()
 for i,g in enumerate(parts):
  if not isinstance(g,trimesh.Trimesh):continue
  g=g.copy();v=g.vertices.copy();t=np.clip(((v[:,1]-lo[1])/(hi[1]-lo[1])-.50)/.37,0,1)
  t=t*t*(3-2*t)
  v[:,0]=xmid+(v[:,0]-xmid)*(1+.13*t)
  v[:,2]=zmid+(v[:,2]-zmid)*(1+.08*t)
  v[:,1]=lo[1]+.86*(v[:,1]-lo[1])
  g.vertices=v;out.add_geometry(g,geom_name='adult_anatomy_morph_'+str(i))
 return out
def render(file,prefix):
 import vtk
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(480,480)
 imp=vtk.vtkGLTFImporter();imp.SetFileName(str(file));imp.SetRenderWindow(win);imp.Update()
 ren=win.GetRenderers().GetFirstRenderer()
 if ren is None or ren.GetActors().GetNumberOfItems()==0:raise RuntimeError('VTK no actors')
 b=ren.ComputeVisiblePropBounds()
 center=np.array([(b[2*i]+b[2*i+1])/2 for i in range(3)])
 sz=max(b[2*i+1]-b[2*i] for i in range(3))
 views={'front':(0,0,1,0,1,0),'back':(0,0,-1,0,1,0),'left':(-1,0,0,0,1,0),
  'right':(1,0,0,0,1,0),'quarter':(.7,.2,.7,0,1,0),
  'top':(0,1,0,0,0,-1),'bottom':(0,-1,0,0,0,1)}
 for name,vec in views.items():
  cam=ren.GetActiveCamera()
  cam.SetPosition(*(center+np.array(vec[:3])*2.7*sz));cam.SetFocalPoint(*center)
  cam.SetViewUp(*vec[3:]);cam.ParallelProjectionOn();cam.SetParallelScale(.72*sz)
  ren.SetBackground(.91,.91,.92);ren.ResetCameraClippingRange();win.Render()
  fl=vtk.vtkWindowToImageFilter();fl.SetInput(win);fl.Update()
  p=OUT/(prefix+'_'+name+'.png')
  writer=vtk.vtkPNGWriter();writer.SetFileName(str(p));writer.SetInputConnection(fl.GetOutputPort());writer.Write()
  if p.stat().st_size<500:raise RuntimeError('empty view '+name)
 return len(views)
def sheet():
 names=['front','quarter','right','back','left','top','bottom']
 im=Image.new('RGB',(4*480,4*520),(234,235,236));draw=ImageDraw.Draw(im)
 for row,pref in enumerate(('donor','morph')):
  for j,name in enumerate(names):
   x=(j%4)*480;y=(row*2+j//4)*520
   im.paste(Image.open(OUT/(pref+'_'+name+'.png')).convert('RGB'),(x,y+30))
   draw.text((x+10,y+10),pref+' '+name,fill=(30,30,30))
 im.save(OUT/'run222_actual_14view_comparison_NOT_APPROVED.png')
try:
 ref=pathlib.Path('owl-pet/design/concepts/172-tyto-castanops-v3.png')
 REPORT['checks']['reference']=digest(ref)
 if REPORT['checks']['reference']['sha256']!=EXPECTED:raise ValueError('reference mismatch')
 Image.open(ref).convert('RGB').crop((950,255,1440,850)).save(OUT/'official_v3_rightmost_reference.png')
 r=requests.get(SRC,timeout=(20,60));REPORT['checks']['manifest_status']=r.status_code;r.raise_for_status()
 manifest=r.json();(OUT/'run222_source_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
 options=candidate(manifest);REPORT['checks']['candidate_options']=options[:8]
 if not options:raise RuntimeError('no named barn owl GLB in manifest')
 url=options[0][1];REPORT['checks']['donor_url']=url
 original=OUT/'CC0_barn_owl_ADULT_original.glb';download(url,original)
 scene=trimesh.load(original,force='scene',process=False);REPORT['checks']['donor_stats']=stats(scene)
 if REPORT['checks']['donor_stats']['triangles']<3000:raise RuntimeError('not enough 3D geometry')
 edited=OUT/'run222_real3d_adult_donor_morph_UNAPPROVED.glb'
 edited.write_bytes(morph(scene).export(file_type='glb'))
 reopened=trimesh.load(edited,force='scene',process=False);REPORT['checks']['morph_stats']=stats(reopened)
 REPORT['checks']['donor_7view']=render(original,'donor')
 REPORT['checks']['morph_7view']=render(edited,'morph')
 sheet()
 REPORT['status']='ACTUAL_NATIVE_TYTO_DONOR_MORPH_14VIEWS_TECH_ONLY_ART_UNAPPROVED'
except Exception as e:
 REPORT['status']='FAILED_NO_RELEASE';REPORT['error']=repr(e);REPORT['traceback']=traceback.format_exc()[-5000:]
finally:
 for p in OUT.iterdir():
  if p.is_file() and p.name!='run222_report.json':REPORT['files'][p.name]=digest(p)
 REPORT['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 (OUT/'run222_report.json').write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'status':REPORT['status'],'error':REPORT.get('error'),'files':list(REPORT['files']),'release':'NO_RELEASE'}),flush=True)
