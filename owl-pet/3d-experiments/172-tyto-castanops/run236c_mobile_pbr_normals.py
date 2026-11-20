#!/usr/bin/env python3
"""Run236c: native glTF2 normals + explicit PBR materials for real Run236b neural mesh.
This is a format/material experiment, NOT phone WebGL validation or art approval.
"""
import os,struct,json,hashlib
from pathlib import Path
import numpy as np,trimesh
outdir=Path(os.environ.get('RUN236C_OUT',str(Path(__file__).resolve().parent/'run236c-evidence')))
outdir.mkdir(parents=True,exist_ok=True)
src=outdir/'run236b_true3D_eyes_down_ART_REJECTED_NO_RELEASE.glb'
expected='1b6181759f6ab995b9744f8d2310301e613290fe47c430b1baa56135ad074366'
assert src.read_bytes()[:4]==b'glTF'
assert hashlib.sha256(src.read_bytes()).hexdigest()==expected
scene=trimesh.load(src,force='scene');assert len(scene.geometry)==4
for name,g in scene.geometry.items():
 normals=g.vertex_normals
 assert np.isfinite(normals).all() and normals.shape==g.vertices.shape
b=scene.export(file_type='glb',include_normals=True)
magic,version,tot=struct.unpack_from('<4sII',b,0)
assert magic==b'glTF' and version==2 and tot==len(b)
jl,jt=struct.unpack_from('<II',b,12)
data=json.loads(b[20:20+jl]);assert jt==0x4e4f534a
assert len(data['meshes'])==4
assert all(all(k in prim['attributes'] for k in ('NORMAL','COLOR_0','POSITION')) for m in data['meshes'] for prim in m['primitives'])
materials=[
 {'name':'cream_matte_second_down_base','pbrMetallicRoughness':{'baseColorFactor':[1,1,1,1],'metallicFactor':0.0,'roughnessFactor':0.94},'doubleSided':False},
 {'name':'cream_micro_down_cards_double_sided','pbrMetallicRoughness':{'baseColorFactor':[1,1,1,1],'metallicFactor':0.0,'roughnessFactor':0.98},'doubleSided':True},
 {'name':'dark_living_cornea_low_roughness','pbrMetallicRoughness':{'baseColorFactor':[1,1,1,1],'metallicFactor':0.0,'roughnessFactor':0.21},'doubleSided':True},
 {'name':'dark_living_cornea_low_roughness_right','pbrMetallicRoughness':{'baseColorFactor':[1,1,1,1],'metallicFactor':0.0,'roughnessFactor':0.21},'doubleSided':True},
]
for mesh in data['meshes']:
 name=mesh.get('name','')
 mid=1 if 'soft_down' in name else (2 if 'left' in name else 3) if 'cornea' in name else 0
 for prim in mesh['primitives']:prim['material']=mid
data['materials']=materials
jsonbytes=json.dumps(data,separators=(',',':'),ensure_ascii=False).encode('utf8')
jsonbytes+=b' ' * ((-len(jsonbytes))%4)
other=b[20+jl:]
new=b'glTF'+struct.pack('<II',2,12+8+len(jsonbytes)+len(other))+struct.pack('<II',len(jsonbytes),0x4e4f534a)+jsonbytes+other
assert len(new)==struct.unpack_from('<I',new,8)[0]
target=outdir/'run236c_true3D_mobilePBR_normals_ART_REJECTED_NO_RELEASE.glb'
target.write_bytes(new)
loaded=trimesh.load(target,force='scene')
assert len(loaded.geometry)==4
assert all(np.isfinite(g.vertices).all() and np.ptp(g.vertices,axis=0).min()>.01 for g in loaded.geometry.values())
report={
 'run':'Run236c','source_run236b_sha256':expected,
 'native_glb_sha256':hashlib.sha256(new).hexdigest(),'glb_bytes':len(new),
 'mesh_parts':len(loaded.geometry),'true_3d_triangles':sum(len(g.faces) for g in loaded.geometry.values()),
 'normal_accessors':sum('NORMAL' in p['attributes'] for m in data['meshes'] for p in m['primitives']),
 'pbr_materials':len(materials),'phone_webgl':'UNTESTED','art_approval':False,
 'status':'TRUE_3D_TECH_PASS_ART_REJECTED_NO_RELEASE','additional_paid_usd':0}
(outdir/'run236c_native_PBR_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
