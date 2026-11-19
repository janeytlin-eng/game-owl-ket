#!/usr/bin/env python3
"""Run223: actually qualify public CC0 museum scans and render real native 3D if legally available.
This is a donor-provenance study, NOT a juvenile Tyto pet release. No paid APIs.
"""
import datetime, hashlib, io, json, math, pathlib, re, traceback
import requests
OUT=pathlib.Path('owl-pet/3d-experiments/172-tyto-castanops/run223-evidence')
OUT.mkdir(parents=True,exist_ok=True)
EXPECTED='881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d'
REPO_BASE='https://github.com/janeytlin-eng/game-owl-ket'
R={'run':223,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'target':'#172 Tyto castanops v3 rightmost cream, age-unknown mesoptile',
   'goal':'Find an authentic existing CC0 photo-scanned Tyto base; test REAL GLB if licensed and accessible',
   'preceding_run':'Run222 rejected mechanical adult barn owl, 14 native views',
   'release':'NO_RELEASE','art':'NOT_APPROVED','phone_hardware':'NOT_TESTED',
   'additional_paid_usd':0,'main_modified':False,'production_modified':False,
   'sources':[],'checks':{},'files':{},'candidates':[]}
S=requests.Session(); S.headers.update({'User-Agent':'owl172-open-3d-research/1.0 (public CC0 attribution audit)'})
def sha(p):
 return {'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def request_json(url,params=None,timeout=30):
 res=S.get(url,params=params,timeout=(15,timeout))
 R['sources'].append({'url':res.url,'http':res.status_code,'bytes':len(res.content),
                      'content_type':res.headers.get('Content-Type','')})
 if not res.ok: R['sources'][-1]['error_body']=res.text[:500]
 res.raise_for_status()
 return res.json()
def zenodo_probe():
 found=[]
 for q in ('0e65de5934db4f0eae02835ba7227dcc','"Barn owl"','"Tyto alba"'):
  try:
   data=request_json('https://zenodo.org/api/records',params={'q':q,'size':20},timeout=40)
   items=data.get('hits',{}).get('hits',[])
   R['checks']['zenodo_'+q]={'returned':len(items),'total':data.get('hits',{}).get('total')}
   for item in items:
    m=item.get('metadata',{})
    title=str(m.get('title',''))
    desc=re.sub('<[^>]*>',' ',str(m.get('description','')))
    text=(title+' '+desc).lower()
    if not any(x in text for x in ('barn owl','tyto alba','0e65de5934db4f0eae02835ba7227dcc')):continue
    lid=m.get('license') or m.get('rights') or {}
    if isinstance(lid,list):license_name=' '.join(str(x.get('id',x) if isinstance(x,dict) else x) for x in lid)
    else:license_name=str(lid.get('id',lid) if isinstance(lid,dict) else lid)
    fs=[]
    entries=item.get('files',[])
    if isinstance(entries,dict):
     entries=entries.get('entries',{})
     entries=list(entries.values()) if isinstance(entries,dict) else entries
    for f in entries:
     if not isinstance(f,dict):continue
     name=str(f.get('key') or f.get('filename') or '')
     if name.lower().endswith('.glb'):
      url=f.get('links',{}).get('content') or f.get('links',{}).get('self') or f.get('links',{}).get('download')
      if url:fs.append({'name':name,'url':url,'size':f.get('size')})
    c={'source':'Zenodo Objaverse archival mirror','record_id':item.get('id'),
       'title':title,'license':license_name,'matched_uid':('0e65de5934db4f0eae02835ba7227dcc' in text),
       'museum':('wirtualne' in text or 'małopol' in text or 'malopol' in text),
       'glbs':fs,'url':item.get('links',{}).get('html')}
    found.append(c)
  except Exception as e:
   R['checks']['zenodo_'+q]={'error':repr(e)}
 R['candidates']=found[:35]
 # Zenodo calls Creative Commons Zero 'cc-zero', not 'cc0'. Both denote CC0.
 accepted=[c for c in found if c['glbs'] and
           any(x in c['license'].lower() for x in ('cc0','cc-zero'))]
 accepted.sort(key=lambda c:(c['title'].strip().lower()=='barn owl',
                              c['matched_uid'],c['museum'],len(c['glbs'])),reverse=True)
 for c in accepted:
  # Prefer the original full-resolution scan over derived decimations for anatomy QA.
  c['glbs'].sort(key=lambda g:(g['name'].lower()=='0e65de5934db4f0eae02835ba7227dcc.glb',
                                'normalized_optimized' in g['name'].lower()),reverse=True)
 return accepted
def smithsonian_probe():
 """Metadata scan. Never fetch 22GB full dataset; check scientific_name/title for Tyto."""
 try:
  import pandas as pd
  api='https://huggingface.co/api/datasets/MikeTrizna/smithsonian-open-access-3d/parquet/metadata/train'
  links=request_json(api,timeout=40)
  R['checks']['smithsonian_parquet_files']=len(links)
  if not isinstance(links,list) or not links:
   R['checks']['smithsonian']={'error':'no metadata Parquet files returned'};return
  total=0; matches=[]; total_bytes=0
  for url in links[:12]:
   rr=S.get(url,timeout=(20,80))
   total_bytes+=len(rr.content)
   if rr.status_code!=200:raise RuntimeError('HF parquet HTTP '+str(rr.status_code))
   if total_bytes>160000000:
    R['checks']['smithsonian_size_cap_reached']=total_bytes
    break
   df=pd.read_parquet(io.BytesIO(rr.content),columns=['title','package_title','scientific_name','object_type','topic','mesh_url','license','record_link']);total+=len(df)
   cols=[c for c in ('title','package_title','scientific_name','object_type','topic') if c in df.columns]
   for _,row in df.iterrows():
    val=' '.join(str(row[c]) for c in cols).lower()
    if re.search(r'\bowl\b|\btyto\b|strigiformes|barn[- ]owl',val):
     matches.append({'title':str(row.get('title',''))[:180],
       'scientific_name':str(row.get('scientific_name',''))[:160],
       'mesh_url':str(row.get('mesh_url',''))[:300],
       'license':str(row.get('license','')),
       'record_link':str(row.get('record_link',''))})
  R['checks']['smithsonian']={'rows_checked':total,'metadata_bytes':total_bytes,
       'owl_matches':len(matches),'matches':matches[:25],
       'scan_only':'Does not imply juvenile or body scan availability'}
  exact=[m for m in matches if ('tyto' in m['scientific_name'].lower() or 'barn owl' in m['title'].lower())
        and m['mesh_url'].startswith('https://') and 'cc0' in m['license'].lower()]
  R['checks']['smithsonian_exact_model_candidates']=exact[:10]
  if exact:
   R['smithsonian_candidate']={'source':'Smithsonian Open Access genuine CC0 3D scan',
     'title':exact[0]['title'],'license':'CC0 metadata',
     'glbs':[{'name':'smithsonian_3d_scan.glb','url':exact[0]['mesh_url']}],
     'url':exact[0]['record_link']}
 except Exception as e:
  R['checks']['smithsonian']={'error':repr(e)}
def download(c):
 g=c['glbs'][0]
 url=g['url']
 p=OUT/'run223_museum_CC0_candidate_ORIGINAL_NOT_APPROVED.glb'
 with S.get(url,timeout=(25,130),stream=True) as r:
  R['checks']['source_download_http']={'code':r.status_code,'mime':r.headers.get('Content-Type'),'url':r.url}
  r.raise_for_status()
  n=0
  with p.open('wb') as f:
   for chunk in r.iter_content(1024*1024):
    if chunk:
     n+=len(chunk)
     if n>65*1024*1024:raise RuntimeError('65 MiB safe limit reached')
     f.write(chunk)
 if p.read_bytes()[:4]!=b'glTF':raise ValueError('not a native GLB header')
 return p
def render(p):
 """Actual original native triangles from multiple 3D cameras, no synthetic 2D shift."""
 import numpy as np,trimesh,vtk
 from PIL import Image,ImageDraw
 from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
 sc=trimesh.load(str(p),force='scene',process=False)
 ms=sc.dump()
 if isinstance(ms,trimesh.Trimesh):ms=[ms]
 geometries=[x for x in ms if isinstance(x,trimesh.Trimesh) and len(x.faces)>0]
 tris=sum(len(g.faces) for g in geometries)
 R['checks']['native_GLTF_mesh']={'geometries':len(geometries),'faces':tris,
   'vertices':sum(len(g.vertices) for g in geometries),
   'original_bounds':np.asarray(sc.bounds).tolist()}
 if tris<3000:raise RuntimeError('not a usable native 3D donor, too few triangles')
 ren=vtk.vtkRenderer();win=vtk.vtkRenderWindow()
 win.SetOffScreenRendering(1);win.SetSize(420,420);win.AddRenderer(ren)
 tex_count=0
 for i,g in enumerate(geometries):
  pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(np.asarray(g.vertices,dtype=np.float64),deep=True))
  poly=vtk.vtkPolyData();poly.SetPoints(pts)
  ff=np.column_stack((np.full(len(g.faces),3,dtype=np.int64),np.asarray(g.faces,dtype=np.int64))).ravel()
  cells=vtk.vtkCellArray();cells.SetCells(len(g.faces),numpy_to_vtkIdTypeArray(ff,deep=True))
  poly.SetPolys(cells)
  tcoords=getattr(g.visual,'uv',None)
  if tcoords is not None and len(tcoords)==len(g.vertices):
   tc=numpy_to_vtk(np.asarray(tcoords,dtype=np.float32),deep=True)
   tc.SetName('uv');poly.GetPointData().SetTCoords(tc)
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
  actor=vtk.vtkActor();actor.SetMapper(mapper)
  actor.GetProperty().SetInterpolationToPhong()
  texture_img=getattr(getattr(g.visual,'material',None),'image',None)
  if texture_img is not None and tcoords is not None:
   try:
    texpath=OUT/('run223_texture_'+str(i)+'.png')
    Image.fromarray(np.asarray(texture_img)).convert('RGB').save(texpath)
    reader=vtk.vtkPNGReader();reader.SetFileName(str(texpath));reader.Update()
    texture=vtk.vtkTexture();texture.SetInputConnection(reader.GetOutputPort());texture.InterpolateOn()
    actor.SetTexture(texture);tex_count+=1
   except Exception as e:
    R['checks']['texture_error_'+str(i)]=repr(e)
  else:
   try:
    vcol=np.asarray(g.visual.to_color().vertex_colors)
    if len(vcol)==len(g.vertices):
     col=numpy_to_vtk(vcol[:,:3].astype(np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
     col.SetName('vertex_color');poly.GetPointData().SetScalars(col)
     mapper.SetColorModeToDirectScalars()
   except Exception:pass
  ren.AddActor(actor)
 R['checks']['native_renderer']={'triangles_submitted':tris,'image_textured_actors':tex_count,'actors':len(geometries),
  'warning':'VTK may not match original glTF PBR roughness/normal maps'}
 bounds=ren.ComputeVisiblePropBounds()
 center=np.array([(bounds[2*j]+bounds[2*j+1])/2 for j in range(3)])
 dims=np.array([bounds[2*j+1]-bounds[2*j] for j in range(3)])
 vaxis=int(np.argmax(dims));a,b=[x for x in (0,1,2) if x!=vaxis]
 diameter=float(dims.max())
 R['checks']['view_orientation']={'estimated_up_axis':vaxis,'dims':dims.tolist(),
   'not_a_verified_anatomical_front':True}
 tile=Image.new('RGB',(4*420,2*450),(237,238,240));draw=ImageDraw.Draw(tile)
 from vtk.util.numpy_support import vtk_to_numpy
 for j,angle in enumerate((0,50,100,150,200,250,300)):
  theta=math.radians(angle)
  vec=np.zeros(3);vec[a]=math.cos(theta);vec[b]=math.sin(theta)
  position=center+vec*2.7*diameter
  up=np.zeros(3);up[vaxis]=1
  cam=ren.GetActiveCamera()
  cam.SetFocalPoint(*center);cam.SetPosition(*position);cam.SetViewUp(*up)
  cam.ParallelProjectionOn();cam.SetParallelScale(.72*diameter)
  ren.SetBackground(.88,.90,.91);ren.ResetCameraClippingRange()
  win.Render()
  w=vtk.vtkWindowToImageFilter();w.SetInput(win);w.Update()
  writer=vtk.vtkPNGWriter()
  q=OUT/('run223_azimuth_'+str(angle)+'.png')
  writer.SetFileName(str(q));writer.SetInputConnection(w.GetOutputPort());writer.Write()
  if q.stat().st_size<1000:raise RuntimeError('3D screenshot failed '+str(angle))
  x=(j%4)*420;y=(j//4)*450
  tile.paste(Image.open(q).convert('RGB'),(x,y+30))
  draw.text((x+8,y+9),'REAL 3D camera azimuth '+str(angle)+' deg',fill=(25,27,30))
 tile.save(OUT/'run223_museum_7views_NOT_APPROVED.png')
 R['checks']['actual_views']=7
try:
 ref=pathlib.Path('owl-pet/design/concepts/172-tyto-castanops-v3.png')
 R['checks']['target_reference']=sha(ref)
 if R['checks']['target_reference']['sha256']!=EXPECTED:raise RuntimeError('reference SHA mismatch')
 R['checks']['preflight']={'README':'owl-pet/README.md','spec':'owl-pet/research/species/172-tyto-castanops-v3.md',
   'prev':'2026-11-20-run222...ART_REJECTED','main_production':'UNCHANGED (176/251 at main snapshot)'}
 matches=zenodo_probe()
 if matches:
  R['checks']['smithsonian']='Not scanned again: an exact legitimately CC0 museum Barn owl scan donor was already located; avoid unnecessary 180MB metadata transfer.'
 else:
  smithsonian_probe()
 if not matches and R.get('smithsonian_candidate'):
  matches=[R['smithsonian_candidate']]
 if matches:
  R['checks']['chosen_archival_candidate']=matches[0]
  p=download(matches[0])
  render(p)
  R['status']='REAL_NATIVE_CC0_3D_SCAN_RENDERED_ADULT_DONOR_ONLY_ART_UNAPPROVED_NO_RELEASE'
 else:
  if any('error' in R['checks'].get('zenodo_'+q,{}) for q in ('0e65de5934db4f0eae02835ba7227dcc','"Barn owl"','"Tyto alba"')) and 'error' in R['checks'].get('smithsonian',{}):
   R['status']='ARCHIVE_QUERIES_INCONCLUSIVE_NO_RELEASE'
  else:
   R['status']='NO_MATCHING_DOWNLOADABLE_CC0_TYTO_SCAN_FOUND_NO_RELEASE'
except Exception as exc:
 R['status']='FAILED_WITH_DIAGNOSTICS_NO_RELEASE'
 R['error']=repr(exc)
 R['traceback']=traceback.format_exc()[-3500:]
finally:
 for file in OUT.iterdir():
  if file.is_file() and file.name!='run223_report.json':R['files'][file.name]=sha(file)
 R['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 (OUT/'run223_report.json').write_text(json.dumps(R,ensure_ascii=False,indent=2,default=str)+'\n')
 print(json.dumps({'status':R['status'],'error':R.get('error'),
   'candidate_count':len(R['candidates']),'native_views':R['checks'].get('actual_views',0),
   'release':'NO_RELEASE'}),flush=True)
