#!/usr/bin/env python3
"""Run297b UV atlas diagnostic of original photo on genuine owl mesh. NO RELEASE."""
import json, hashlib,sys
from pathlib import Path
import numpy as np
from PIL import Image,ImageFilter
import trimesh
from trimesh.visual.texture import TextureVisuals
from trimesh.visual.material import PBRMaterial
src=Path(sys.argv[1]);photo=Path(sys.argv[2]);dest=Path(sys.argv[3]);dest.mkdir(parents=True,exist_ok=True)
scene=trimesh.load(src,force='scene')
body=scene.geometry['smoothed-original-native-owl'].copy()
fur=scene.geometry['down-feather-triangle-ribbons'].copy()
V=body.vertices;N=body.vertex_normals;lo=V.min(axis=0);hi=V.max(axis=0)
x=np.clip((V[:,0]-lo[0])/(hi[0]-lo[0]),0,1);y=np.clip((V[:,1]-lo[1])/(hi[1]-lo[1]),0,1)
photoim=Image.open(photo).convert('RGB')
atlas=Image.new('RGB',(2048,1024),(223,211,192))
atlas.paste(photoim.resize((1024,1024),Image.Resampling.LANCZOS),(0,0))
rg=np.random.default_rng(172297)
noise=rg.normal(0,7,(1024,1024,1)).astype(np.float32)
mat=np.clip(np.array([225,210,188],dtype=np.float32)+noise,0,255).astype(np.uint8)
mat=Image.fromarray(mat).filter(ImageFilter.GaussianBlur(.45))
atlas.paste(mat,(1024,0));atlas.save(dest/'run297b-UV-bake-ATLAS.png')
front=(N[:,2]>.12)&(V[:,2]>-.02)
u=np.where(front,x*.498+.001,.502+x*.496)
uv=np.column_stack([u,y*.995+.002])
body.visual=TextureVisuals(uv=uv,material=PBRMaterial(
    baseColorTexture=atlas,metallicFactor=0,roughnessFactor=0.97,doubleSided=True))
out=trimesh.Scene()
out.add_geometry(body,geom_name='actual-native-mesh-photo-bake')
out.add_geometry(fur,geom_name='real-mesh-bound-cream-down-ribbons')
fp=dest/'run297b-real-owl-UV-fur-UNAPPROVED.glb';out.export(fp)
s=trimesh.load(fp,force='scene')
info={'variant':'Run297b','bytes':fp.stat().st_size,'sha256':hashlib.sha256(fp.read_bytes()).hexdigest(),
 'mesh_triangles':{k:len(g.faces) for k,g in s.geometry.items()},
 'UV_texture_baked':True,'source_atlas_from_project_original':True,
 'art_approved':False,'rights_cleared':False,'no_release':True}
(dest/'run297b-QA.json').write_text(json.dumps(info,indent=2));print(info)
