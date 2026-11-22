#!/usr/bin/env python3
"""Research-only #172 Run298c correct glTF texture-row convention proven by real Chromium.
This operation modifies true native GLB PBR texture, not owl geometry or SVG.
"""
import sys, hashlib, json
from pathlib import Path
from PIL import ImageOps
import trimesh

if len(sys.argv)!=3: raise SystemExit('usage: patch.py input.glb output.glb')
src=Path(sys.argv[1]); dst=Path(sys.argv[2]); dst.parent.mkdir(parents=True,exist_ok=True)
scene=trimesh.load(src,force='scene')
assert len(scene.geometry)==2
assert sum(len(m.faces) for m in scene.geometry.values())==31000
fixed=0
for name,mesh in scene.geometry.items():
    if 'body' not in name: continue
    albedo=mesh.visual.material.baseColorTexture
    assert albedo is not None and albedo.size==(1536,1024)
    mesh.visual.material.baseColorTexture=ImageOps.flip(albedo)
    fixed+=1
assert fixed==1
scene.export(dst)
check=trimesh.load(dst,force='scene')
assert len(check.geometry)==2 and sum(len(m.faces) for m in check.geometry.values())==31000
rep={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
     'corrected_sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),
     'corrected_bytes':dst.stat().st_size,
     'triangles':31000,'real_glb':True,'texture_rows_flipped_for_chromium':True,
     'art_approved':False,'rights_cleared':False,'real_phone_tested':False,'release_allowed':False}
(dst.parent/'run298c_orientation_report.json').write_text(json.dumps(rep,indent=2),encoding='utf-8')
print(json.dumps(rep))
