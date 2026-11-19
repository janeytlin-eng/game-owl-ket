#!/usr/bin/env python3
"""Actual CC0 candidate GLB fetch/7-view QA. Never automatically accepts or publishes source."""
import hashlib,json,math,pathlib,traceback
from datetime import datetime,timezone
import requests,numpy as np,trimesh
from PIL import Image,ImageDraw
ROOT=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=pathlib.Path("/tmp/owl172-run210-evidence");OUT.mkdir(parents=True,exist_ok=True)
MODEL=OUT/"innerscene_owl_original_unmodified_CC0.glb"
SRC="https://www.innerscene.com/api/library/owl-d696472a/download"
PAGE="https://www.innerscene.com/tools/library/3d-parts/owl-d696472a"
s={"run":210,"art_gate":"UNASSESSED_NO_RELEASE","hardware_mobile_gate":"NOT_RUN",
   "source_page":PAGE,"src":SRC,"paid_usd":0,"reference_image_available":False,
   "timestamp_utc":datetime.now(timezone.utc).isoformat()}
def digest(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for x in iter(lambda:f.read(1024*1024),b""):h.update(x)
 return h.hexdigest()
try:
 with requests.get(SRC,stream=True,timeout=(25,150),headers={"User-Agent":"Mozilla/5.0 (model provenance research)"}) as r:
  s["http"]=r.status_code;s["resolved_url"]=r.url;s["type"]=r.headers.get("Content-Type","");r.raise_for_status()
  with MODEL.open("wb") as f:
   for b in r.iter_content(chunk_size=1048576):
    if b:f.write(b)
 raw=MODEL.read_bytes()
 s["bytes"]=len(raw);s["sha256"]=digest(MODEL);s["glb_magic"]=repr(raw[:4])
 if raw[:4]!=b"glTF":raise ValueError("NOT A NATIVE GLB; response perhaps HTML")
 scene=trimesh.load(MODEL,force="scene",process=False)
 s["meshes"]=len(scene.geometry)
 s["triangles"]=int(sum(len(g.faces) for g in scene.geometry.values()))
 s["vertices"]=int(sum(len(g.vertices) for g in scene.geometry.values()))
 s["bounds"]=np.asarray(scene.bounds).tolist()
 s["visual_kinds"]=[str(getattr(g.visual,"kind",None)) for g in scene.geometry.values()]
 s["native_glb_loaded"]=True
 try:
  import vtk
  rw=vtk.vtkRenderWindow();rw.SetOffScreenRendering(1);rw.SetSize(600,600)
  imp=vtk.vtkGLTFImporter();imp.SetFileName(str(MODEL));imp.SetRenderWindow(rw);imp.Update()
  ren=rw.GetRenderers().GetFirstRenderer()
  if ren is None or ren.GetActors().GetNumberOfItems()==0:raise RuntimeError("no VTK actors")
  s["vtk_actors"]=ren.GetActors().GetNumberOfItems()
  b=ren.ComputeVisiblePropBounds()
  if not all(math.isfinite(t) for t in b):raise RuntimeError("bad bounds")
  center=[(b[2*i]+b[2*i+1])/2 for i in range(3)];scale=max(b[2*i+1]-b[2*i] for i in range(3))
  axes={"pos_z":(0,0,1,0,1,0),"neg_z":(0,0,-1,0,1,0),
        "pos_x":(1,0,0,0,1,0),"neg_x":(-1,0,0,0,1,0),
        "pos_y":(0,1,0,0,0,-1),"neg_y":(0,-1,0,0,0,1),
        "quarter":(.7,.2,.7,0,1,0)}
  contact=Image.new("RGB",(600*4,635*2),(232,233,234));draw=ImageDraw.Draw(contact)
  for i,(name,vec) in enumerate(axes.items()):
   ax=np.array(vec[:3]);cam=ren.GetActiveCamera()
   cam.SetFocalPoint(*center);cam.SetPosition(*(np.array(center)+2.7*scale*ax))
   cam.SetViewUp(*vec[3:]);cam.ParallelProjectionOn();cam.SetParallelScale(scale*.78)
   ren.SetBackground(.91,.91,.92);ren.ResetCameraClippingRange();rw.Render()
   w=vtk.vtkWindowToImageFilter();w.SetInput(rw);w.Update()
   p=OUT/("native_"+name+".png");writer=vtk.vtkPNGWriter()
   writer.SetFileName(str(p));writer.SetInputConnection(w.GetOutputPort());writer.Write()
   x=(i%4)*600;y=(i//4)*635;contact.paste(Image.open(p).convert("RGB"),(x,y+35))
   draw.text((x+15,y+12),name,fill=(32,32,32))
  contact.save(OUT/"run210_sevenview_contact.png")
  s["vtk_views"]=len(axes);s["native_render_completed"]=True
 except Exception:
  s["native_render_completed"]=False;s["render_error"]=traceback.format_exc()[-4000:]
except Exception:
 s["native_glb_loaded"]=False;s["source_error"]=traceback.format_exc()[-6000:]
s["art_decision"]="NOT ACCEPTED: strict mesoptile morphology, true quality, side/back and mobile still need independent human inspection"
(OUT/"run210_metrics.json").write_text(json.dumps(s,indent=2,ensure_ascii=False))
manifest={p.name:{"bytes":p.stat().st_size,"sha256":digest(p)} for p in OUT.iterdir() if p.is_file()}
(OUT/"run210_manifest.json").write_text(json.dumps(manifest,indent=2))
(ROOT/"2026-11-19-run210-new-cc0-source-native-probe-UNREVIEWED-NO_RELEASE.md").write_text(
 "# Run210 — free CC0 3D asset source probe: NO_RELEASE\n\n"
 "Only a source trial, not an accepted young Tyto castanops. Web source: "+PAGE+
 " (claims CC0; 2026-10-21); test endpoint "+SRC+".\n\n"
 "Actual result JSON:\n\n"+json.dumps(s,indent=2,ensure_ascii=False)+
 "\n\nRaw source binary, seven native camera images when successful, and hashes are in short-retention "
 "workflow artifacts, NOT production. The rightmost original plate crop was not accessible here; "
 "source style/morphology cannot be deemed conformant by automated GLB structure. "
 "No smartphone/GPU acceptance, no extra paid service, no production changes.\n")
print(json.dumps(s,indent=2,ensure_ascii=False),flush=True)
