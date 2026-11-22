#!/usr/bin/env python3
"""Run308 genuine native Tyto-alba (adult) CC0 asset test, NOT 172 juvenile.
Fetch only the exact free immutable CDN objects, independently inspect mesh, materials
and license claims; make no claim that the source geometry matches Tyto castanops chicks.
"""
import json,hashlib,urllib.request,traceback
from pathlib import Path
from datetime import datetime,timezone
out=Path('owl172-run308-evidence');out.mkdir(exist_ok=True)
pack='https://3dassets.dev/api/v1/packs/birds-and-reptiles-hd'
ids={'barn-owl':'28079','tree-stump-with-hollow':'28115'}
report={'run':308,'utc':datetime.now(timezone.utc).isoformat(),
  'purpose':'Genuine licensed adult barn-owl Tyto morphology and hollow prop; NOT juvenile artwork',
  'pack_manifest':pack,'source_taxon':'Tyto alba, adult; NOT Tyto castanops, young',
  'rights_claim_verified_by_provider':False,'rights_independently_cleared':False,
  'webgl2_real_browser':False,'physical_mobile_tested':False,
  'art_approved':False,'release_allowed':False,'paid_usd':0,'models':[],'errors':[]}

def get(url,cap):
 req=urllib.request.Request(url,headers={'User-Agent':'OpenOwl172Research/1.0'})
 with urllib.request.urlopen(req,timeout=100) as res:
  b=res.read(cap+1)
  if len(b)>cap:raise ValueError('File too large')
  return b,res.headers.get('Content-Type','')
try:
 b,ct=get(pack,5_000_000);manifest=json.loads(b)
 (out/'provider-pack-manifest.json').write_bytes(b)
 entries=manifest.get('data',{}).get('assets',[])
 assert len(entries)>=30, 'Provider manifest unexpectedly missing pack contents'
 for slug,asset_id in ids.items():
  info={'slug':slug,'id':asset_id,'download_ok':False,'trimesh_import_ok':False}
  report['models'].append(info)
  item=next((a for a in entries if str(a.get('id'))==asset_id),None)
  if not item: info['error']='Asset id missing from published source pack';continue
  for k in ('slug','title','url','cdnUrl','aiGenerated','aiModel','license','stats'):
   info[k]=item.get(k)
  lic=(item.get('license') or {}).get('slug')
  assert lic=='cc0-1.0', 'Provider does not label this asset CC0'
  assert item.get('cdnUrl')==f'https://cdn.3dassets.dev/assets/{asset_id}/v1/model.glb'
  info['provider_license_claim_cc0']=True
  data,mime=get(item['cdnUrl'],3_500_000)
  assert len(data)>5000 and data[:4]==b'glTF' and int.from_bytes(data[8:12],'little')==len(data), 'No native complete GLB'
  p=out/(slug+'-ORIGINAL_CC0_NOT_172_JUVENILE.glb');p.write_bytes(data)
  info.update(download_ok=True,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),mime=mime,
    declared_size_matches=len(data)==item.get('stats',{}).get('fileSize'))
  jlen=int.from_bytes(data[12:16],'little');info['glb_json']=json.loads(data[20:20+jlen].decode('utf-8'))
  gj=info.pop('glb_json')
  info.update(gltf_version=gj.get('asset',{}).get('version'),gltf_meshes=len(gj.get('meshes',[])),
    gltf_materials=len(gj.get('materials',[])),gltf_textures=len(gj.get('textures',[])),
    gltf_images=len(gj.get('images',[])),gltf_extensions=gj.get('extensionsUsed',[]))
  try:
   import trimesh
   scene=trimesh.load(p,force='scene')
   geos=list(scene.geometry.values())
   info['trimesh_import_ok']=True
   info['trimesh_triangles']=sum(len(g.faces) for g in geos)
   info['trimesh_geometry_count']=len(geos)
   info['trimesh_bounds']=scene.bounds.tolist()
  except Exception as ex:info['trimesh_error']=repr(ex)[:700]
 report['rights_claim_verified_by_provider']=all(x.get('provider_license_claim_cc0') for x in report['models'])
except Exception as ex:
 report['errors'].append(type(ex).__name__+': '+str(ex))
 report['traceback_tail']=traceback.format_exc()[-1700:]
finally:
 report['reason_not_product']=[
  'This is mature adult Tyto alba, not cream-down age-unknown mesoptile Tyto castanops.',
  'Adult remiges/long legs/tail are not compatible with short down-buried wings and concealed tail.',
  'Source lacks groomed juvenile cream down and guaranteed side/back for target chick.',
  'Tree stump asset is habitat prop, not proof of genuine older Tasmanian eucalypt hollow.',
  'Provider advertises CC0; contributor-reported generative origin does not independently clear upstream rights.',
  'Static adult WebGL loading is a technical gate only; physical iPhone/Android not checked.'
 ]
 (out/'raw-asset-validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
 print(json.dumps({k:v for k,v in report.items() if k in ('models','errors','release_allowed','art_approved')},indent=2,ensure_ascii=False)[:12000])
