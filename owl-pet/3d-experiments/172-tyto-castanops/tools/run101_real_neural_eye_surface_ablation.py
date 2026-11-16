#!/usr/bin/env python3
"""Run101 research-only REAL Hunyuan neural mesh face-depth and eye-color ablation.
Edits 80k-face 3D source vertices + glTF COLOR_0; no detached eye sphere,
flat card, SVG, fake 2D model, production overwrite or release.
Source license: Tencent Hunyuan3D-2 Community License, NOT CC0.
"""
import sys,json,hashlib,pathlib
import numpy as np
import trimesh
from PIL import Image,ImageFilter
if len(sys.argv)!=4: raise SystemExit("usage: python run101...py SOURCE.glb RIGHT_CROP.jpg EVIDENCE_DIR")
source,ref,out=map(pathlib.Path,sys.argv[1:])
out.mkdir(parents=True,exist_ok=True)
expected="60feb7a5e4f4c67a020e3457e7ffbfb52f6fbe3e75f115b970030c00b20cd35d"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert source.stat().st_size==1433708 and sha(source)==expected,"source GLB changed"
mesh=trimesh.load(str(source),force="mesh",process=False)
assert len(mesh.faces)==79988 and len(mesh.vertices)==39684
# glTF Y-up -> native Z-up for localized 3D face work. Reverse on export.
W=np.stack([mesh.vertices[:,0],-mesh.vertices[:,2],mesh.vertices[:,1]],axis=1)
x,y,z=W.T
front=np.clip((-y-.51)/.21,0,1)
front=front*front*(3-2*front)
eyes=[(-.1313,.3173),(.1087,.3116)] # ray-picked FROM physical GLB front, not arbitrary pixels
displacement=np.zeros(len(W))
pupil=np.zeros(len(W))
for cx,cz in eyes:
  d=((x-cx)/.048)**2+((z-cz)/.056)**2
  ridge=np.exp(-.5*((np.sqrt(d)-1.43)/.35)**2)
  displacement+=front*(.018*np.exp(-.95*d)-.012*ridge)
  pupil=np.maximum(pupil,np.exp(-1.25*d)*front)
W[:,1]+=displacement # +Y into actual forward-facing 3D surface
rgb=np.zeros((len(W),3),float)
rgb[:]=[236,220,195]
warm=np.clip((z+.7)/1.6,0,1)
rgb+=np.stack([8*warm]*3,axis=1)
radius=np.sqrt((x/.315)**2+((z-.26)/.265)**2)
face=np.clip((1.10-radius)/.26,0,1)*front
rgb=rgb*(1-face[:,None])+np.array([245,233,211])[None,:]*face[:,None]
dark=np.clip((pupil-.23)/.43,0,1)**1.2
rgb=rgb*(1-dark[:,None])+np.array([32,23,18])[None,:]*dark[:,None]
for cx,cz in eyes:
  d=((x-cx)/.06)**2+((z-cz)/.061)**2
  limbal=np.exp(-((np.sqrt(d)-.73)/.14)**2)*front*(1-dark*.85)*.32
  rgb=rgb*(1-limbal[:,None])+np.array([103,68,38])[None,:]*limbal[:,None]
  glint=np.exp(-1.5*(((x-cx+.013)/.011)**2+((z-cz-.019)/.012)**2))*front*.65
  rgb=rgb*(1-glint[:,None])+np.array([254,246,230])[None,:]*glint[:,None]
color_a=np.clip(rgb,0,255).astype(np.uint8)
photo=np.array(Image.open(ref).convert("RGB").filter(ImageFilter.GaussianBlur(.45)))
px=235+(x-eyes[0][0])*(92/(eyes[1][0]-eyes[0][0]))
py=244-(z-eyes[0][1])*395
u=np.clip(np.rint(px).astype(int),0,photo.shape[1]-1)
v=np.clip(np.rint(py).astype(int),0,photo.shape[0]-1)
projection=photo[v,u].astype(float)
weight=np.clip((1.04-radius)/.25,0,1)*front
weight*=np.clip((z-.035)/.09,0,1)*np.clip((.59-z)/.1,0,1)*np.clip((-.52-y)/.12,0,1)
color_b=np.clip(rgb*(1-weight[:,None])+projection*weight[:,None]*.96+rgb*weight[:,None]*.04,0,255).astype(np.uint8)
# Preserve true sculpt mesh topology, never proxy spheres/cylinders.
records=[]
for label,color in (("run101A_native_eye_recess_color_ART_UNAPPROVED",color_a),
                    ("run101B_orig_face_project_ART_UNAPPROVED",color_b)):
  m=mesh.copy()
  m.vertices=np.stack([W[:,0],W[:,2],-W[:,1]],axis=1)
  m.visual=trimesh.visual.ColorVisuals(mesh=m,
    vertex_colors=np.c_[color,np.full(len(color),255,dtype=np.uint8)])
  p=out/(label+".glb")
  m.export(str(p))
  check=trimesh.load(str(p),force="scene",process=False)
  assert len(check.geometry)==1
  roundmesh=list(check.geometry.values())[0]
  assert len(roundmesh.faces)==79988 and len(roundmesh.vertices)==39684
  assert roundmesh.visual.kind=="vertex"
  records.append(dict(glb=p.name,bytes=p.stat().st_size,sha256=sha(p),
                      triangles=len(roundmesh.faces),vertices=len(roundmesh.vertices),
                      glb_roundtrip=True,color0=True))
report=dict(source=source.name,source_sha256=sha(source),right_crop=ref.name,
            source_original_neural_geometry=True,eye_surface_raypicked=True,
            displaced_vertices=int(np.count_nonzero(abs(displacement)>.002)),
            displacement_max_normalized_units=float(displacement.max()),
            variants=records,pass_art_gate=False,phone_gpu_tested=False,
            cost_usd=0,licensing="Tencent Hunyuan3D-2 Community License: non-CC0 restricted")
(out/"run101_metrics.json").write_text(json.dumps(report,indent=2))
(out/"ART_GATE_NOT_PASSED.md").write_text(
 "# Run101 research only — ART_UNAPPROVED\n\n"
 "True 80k triangle neural-source mesh; genuine local eye-surface displacements and embedded per-vertex color.\n"
 "Facial experiment is not anatomically corrected grooming or completed electronic pet. "
 "Side/back, supported feet/tree hollow, soft layered down, actual-phone WebGL GPU and global license "
 "NOT approved. No deployment; do not merge into 251 species workflow.\n")
print(json.dumps(report,indent=2))
