#!/usr/bin/env python3
"""Run212: evaluate official Microsoft TRELLIS.2 public ZeroGPU Space, no paid API.
RESEARCH ONLY. Never mark 3D as accepted automatically.
"""
import json, hashlib, traceback, shutil, time, os
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image
import numpy as np
import cv2

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "owl-pet" / "3d-experiments" / "172-tyto-castanops" / "run212-evidence"
OUT.mkdir(parents=True, exist_ok=True)
SRC = ROOT / "owl-pet" / "design" / "concepts" / "172-tyto-castanops-v3.png"
SHA = "881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
report = {
 "experiment":"Run212 official Stability AI Stable Fast 3D one-stage ZeroGPU native GLB trial",
 "utc":datetime.now(timezone.utc).isoformat(),
 "status":"PREFLIGHT",
 "model":"stabilityai/stable-fast-3d",
 "source_file":str(SRC.relative_to(ROOT)),
 "expected_source_sha256":SHA,
 "claimed_paid_spend_usd":0,
 "only_one_public_free_zerogpu_trial":True,
 "art_gate":"NOT_PASSED", "mobile_hardware_gate":"NOT_TESTED",
 "release":"NO_RELEASE",
 "reference_crop_xyxy":[950,255,1440,850],
}

def sha(path):
 return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def make_input():
 assert SRC.is_file(), "Cannot locate official reference plate; do not use substitute image"
 report["actual_source_sha256"]=sha(SRC)
 assert report["actual_source_sha256"] == SHA, "Canonical source hash mismatch"
 plate=Image.open(SRC).convert("RGB")
 assert plate.size==(1536,1024), plate.size
 crop=plate.crop((950,255,1440,850))
 crop.save(OUT/"source_exact_rightmost_crop.png")
 # Data-derived soft background matte, NOT an invented back-view image.
 rgb=np.asarray(crop).copy()
 bgr=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR)
 h,w=bgr.shape[:2]
 m=np.zeros((h,w),dtype=np.uint8)
 rect=(round(w*.09),round(h*.035),round(w*.82),round(h*.89))
 bg=np.zeros((1,65),np.float64); fg=np.zeros((1,65),np.float64)
 cv2.grabCut(bgr,m,rect,bg,fg,7,cv2.GC_INIT_WITH_RECT)
 alpha=np.where((m==cv2.GC_FGD)|(m==cv2.GC_PR_FGD),255,0).astype(np.uint8)
 # Keep only connected foreground region containing face at central-upper crop.
 n, labels, stats, centers=cv2.connectedComponentsWithStats(alpha)
 if n>1:
  candidate=max(range(1,n),key=lambda i:stats[i,cv2.CC_STAT_AREA])
  alpha=(labels==candidate).astype(np.uint8)*255
 alpha=cv2.morphologyEx(alpha,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
 # Ensure output is not an almost empty / all-opaque segmentation.
 ratio=float(np.count_nonzero(alpha))/alpha.size
 report["input_matte_nonzero_ratio"]=ratio
 assert .15 < ratio < .94, f"GrabCut mask seems invalid: {ratio}"
 rgba=np.dstack((rgb,alpha))
 # Cropped image includes age-unknown youngster + hollow lip; provenance remains concept art.
 Image.fromarray(rgba,"RGBA").save(OUT/"source_rightmost_grabcut_rgba.png")
 report["input_image_sha256"]=sha(OUT/"source_rightmost_grabcut_rgba.png")
 return OUT/"source_rightmost_grabcut_rgba.png"

def render_glb(path):
 import trimesh
 import vtk
 sc=trimesh.load(path,force="scene")
 report["import_scene_meshes"]=len(sc.geometry)
 report["import_scene_triangles"]=int(sum(len(g.faces) for g in sc.geometry.values()))
 assert sc.geometry and report["import_scene_triangles"]>1000,"Invalid mesh; no output gate"
 importer=vtk.vtkGLTFImporter()
 importer.SetFileName(str(path))
 rr=vtk.vtkRenderer(); rr.SetBackground(.17,.19,.22)
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(640,640)
 win.AddRenderer(rr);importer.SetRenderWindow(win);importer.Update()
 bounds=rr.ComputeVisiblePropBounds()
 center=tuple((bounds[i]+bounds[i+1])/2 for i in (0,2,4))
 rad=max(bounds[1]-bounds[0],bounds[3]-bounds[2],bounds[5]-bounds[4])
 assert 0<rad<1e7,(bounds,rad)
 from PIL import ImageDraw
 positions=[("front",(0,-3,0)),("back",(0,3,0)),("left",(-3,0,0)),
            ("right",(3,0,0)),("quarter",(2,-2,1)),("top",(0,0,3)),("bottom",(0,-1,-3))]
 outimgs=[]
 for name,direction in positions:
  cam=rr.GetActiveCamera()
  cam.SetPosition(*(center[i]+direction[i]*rad for i in range(3)))
  cam.SetFocalPoint(*center)
  cam.SetViewUp(0,0,1 if name not in ("top","bottom") else 0.001)
  cam.ParallelProjectionOn();cam.SetParallelScale(rad*.78)
  rr.ResetCameraClippingRange();win.Render()
  filt=vtk.vtkWindowToImageFilter();filt.SetInput(win);filt.Update()
  dest=OUT/("native_"+name+".png")
  writer=vtk.vtkPNGWriter();writer.SetFileName(str(dest));writer.SetInputConnection(filt.GetOutputPort());writer.Write()
  assert dest.exists() and dest.stat().st_size>2000
  outimgs.append(dest)
 win.Finalize()
 contact=Image.new("RGB",(4*330,2*360),(234,231,225))
 draw=ImageDraw.Draw(contact)
 for i,p in enumerate(outimgs):
  im=Image.open(p).convert("RGB");im.thumbnail((325,325))
  x=(i%4)*330;y=(i//4)*360
  contact.paste(im,(x,y+25));draw.text((x+4,y+5),p.stem.replace("native_","").upper(),(30,30,30))
 contact.save(OUT/"sevenview_CONTACT_UNREVIEWED.png")
 report["native_sevenview_files"]=[p.name for p in outimgs]
 report["native_sevenview_status"]="RENDERED_UNREVIEWED_NOT_APPROVED"


def main():
 start=time.monotonic()
 try:
  imagepath=make_input()
  report["status"]="ATTEMPTING_OFFICIAL_SINGLE_STAGE_ZERO_GPU"
  report["public_api"]="stabilityai/stable-fast-3d"
  from gradio_client import Client, handle_file
  # Fresh GHA runner. Do not request a token, paid endpoint or credential.
  os.environ["HF_HOME"]="/tmp/owl172_run212_uncredentialed_hf_cache"
  cli=Client("stabilityai/stable-fast-3d", token=None, verbose=False)
  endpoints={str(k):str(v.api_name) for k,v in cli.endpoints.items()}
  report["endpoint_names"]=endpoints
  try:
   view=cli.view_api(return_format="dict")
   report["view_api_diagnostic"]=str(view)[:12000]
  except Exception as e: report["view_api_error"]=str(e)[:1000]
  generation_name=next((name for name in endpoints.values() if name and ("run_button" in name.lower() or name.endswith("/run"))),None)
  preprocess_name=next((name for name in endpoints.values() if name and "requires_bg_remove" in name.lower()),None)
  if not generation_name:
   raise RuntimeError("Public SF3D run_button endpoint unavailable: no free generation requested")
  # This CPU/Gradio state event should preserve the RGBA mask, not expend GPU quota.
  if preprocess_name:
   try:
    pre=cli.submit(handle_file(str(imagepath)),0.85,api_name=preprocess_name).result(timeout=60)
    report["preprocess_type"]=type(pre).__name__
    report["preprocess_summary"]=str(pre)[:2000]
   except Exception as e:
    report["preprocess_warning"]=str(e)[:1000]
  # Exactly one zero-cost GPU submission. The app's own run_button is a single-stage
  # mesh+UV/PBR GLB export; unlike TRELLIS.2 it needs no second GPU extraction.
  job=cli.submit("Run",handle_file(str(imagepath)),handle_file(str(imagepath)),0.85,"None",-1,1024,api_name=generation_name)
  report["submitted"]=True
  result=job.result(timeout=240)
  report["generation_return_type"]=type(result).__name__
  report["generation_result_excerpt"]=str(result)[:4000]
  candidates=[]
  def walk(o):
   if isinstance(o,str) and ".glb" in o.lower():
    candidates.append(o)
   elif isinstance(o,dict):
    for v in o.values():walk(v)
   elif isinstance(o,(list,tuple)):
    for v in o:walk(v)
  walk(result)
  report["candidate_count"]=len(candidates)
  if not candidates: raise RuntimeError("Single-stage official SF3D call returned no actual GLB file")
  # gradio_client automatically downloads File/Model3D outputs; distinguish file
  # from Gradio update dicts and refuse non-existent/model-thumbnail artifacts.
  import urllib.parse, urllib.request
  src=candidates[0]
  glb=OUT/"run212_sf3d_UNAPPROVED.glb"
  if src.startswith(("https://","http://")):
   urllib.request.urlretrieve(src,glb)
  else:
   shutil.copy2(src,glb)
  report["glb_bytes"]=glb.stat().st_size
  report["glb_sha256"]=sha(glb)
  assert glb.read_bytes()[:4]==b"glTF","Malformed GLB; generated 3D NOT proven"
  report["status"]="NATIVE_GLB_UNREVIEWED_NO_RELEASE"
  try: render_glb(glb)
  except Exception as e:
   report["render_error"]=str(e)
   report["render_traceback"]=traceback.format_exc()[-4000:]
   report["status"]="GLB_RENDER_FAILURE_NO_RELEASE"
 except Exception as e:
  report["error"]=str(e)
  report["traceback"]=traceback.format_exc()[-5000:]
  report["status"]="REMOTE_OR_GRADIO_FAILURE_NO_RELEASE"
 finally:
  report["runtime_seconds"]=round(time.monotonic()-start,2)
  report["evidence_files"]={p.name:{"bytes":p.stat().st_size,"sha256":sha(p)}
    for p in sorted(OUT.iterdir()) if p.is_file() and p.name not in ("run212_report.json","run212_report.md")}
  (OUT/"run212_report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False,default=str))
  summary=("# Run212 — Official Stable Fast 3D one-stage public GPU test: NO_RELEASE\\n\\n"
   "Isolated #172 Tyto castanops v3 research. Not accepted character.\\n\\n"
   "Status: **"+report["status"]+"**. Art and mobile hardware gates: NOT PASSED. Extra paid spend: $0.\\n\\n"
   "Input: exact SHA256-validated #172 v3 rightmost crop and transparent GrabCut mask.\\n\\n"
   "Source: Stability AI official Stable Fast 3D Gradio demo, uncredentialed public free GPU only.\\n\\n"
   "If native GLB is generated it must undergo independent seven-view aesthetics review before release.\\n\\n"
   "Reported error: "+str(report.get("error",report.get("render_error","none")))+"\\n")
  # Use real line breaks; keep JSON as primary machine-readable record.
  (OUT/"run212_report.md").write_text(summary.replace("\\n","\n"))
  print(json.dumps({k:v for k,v in report.items() if k not in ("traceback","render_traceback","view_api_diagnostic","preprocess_summary","generation_result_excerpt")},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
