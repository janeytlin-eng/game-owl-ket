"""Mobile LOD experiment on external *adult great horned owl*, not #172 approved juvenile."""
import sys,json,hashlib,pathlib
import trimesh
from PIL import Image
import numpy as np
src=pathlib.Path(sys.argv[1]);dst=pathlib.Path(sys.argv[2]);maxtex=int(sys.argv[3]) if len(sys.argv)>3 else 512;
assert 32 <= maxtex <= 2048
scene=trimesh.load(src,force='scene',process=False)
seen={};changes=[]
for name,mesh in scene.geometry.items():
 m=getattr(mesh.visual,'material',None)
 if m is None: continue
 ident=id(m)
 if ident in seen:continue
 seen[ident]=True
 for slot in ('baseColorTexture','normalTexture','metallicRoughnessTexture','occlusionTexture','emissiveTexture'):
  im=getattr(m,slot,None)
  if im is not None:
   a=im.copy();w,h=a.size
   if max(w,h)>maxtex:
    ratio=maxtex/max(w,h);a=a.resize((max(1,int(w*ratio)),max(1,int(h*ratio))),Image.Resampling.LANCZOS)
    setattr(m,slot,a)
   changes.append({'material_name':m.name,'slot':slot,'old_image':[w,h],'new_image':list(getattr(m,slot).size)})

scene.export(dst)
re=trimesh.load(dst,force='scene',process=False)
info={'source':str(src),'output':str(dst),'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'glb_bytes':dst.stat().st_size,
 'geometry_before':len(scene.geometry),'geometry_after':len(re.geometry),
 'triangles_before':sum(len(g.faces) for g in scene.geometry.values()),
 'triangles_after':sum(len(g.faces) for g in re.geometry.values()),
 'max_texture_dim':maxtex,'materials_reduced':changes,'stage':'EXTERNAL_ADULT_REFERENCE_ONLY; NOT_A_JUVENILE; NOT_USER_APPROVED'}
(dst.with_suffix('.json')).write_text(json.dumps(info,indent=2));print(json.dumps({k:v for k,v in info.items() if k!='materials_reduced'},indent=2))
