#!/usr/bin/env python3
"""Run211: evaluate official Microsoft TRELLIS.2 public ZeroGPU Space, no paid API.
RESEARCH ONLY. Never mark 3D as accepted automatically.
"""
import json, hashlib, traceback, shutil, time, os
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image
import numpy as np
import cv2

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "owl-pet" / "3d-experiments" / "172-tyto-castanops" / "run211-evidence"
OUT.mkdir(parents=True, exist_ok=True)
SRC = ROOT / "owl-pet" / "design" / "concepts" / "172-tyto-castanops-v3.png"
SHA = "881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
report = {
 "experiment":"Run211 official Microsoft TRELLIS.2 public ZeroGPU image-to-real-3D trial",
 "utc":datetime.now(timezone.utc).isoformat(),
 "status":"PREFLIGHT",
 "model":"microsoft/TRELLIS.2",
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
  report["status"]="ATTEMPTING_FREE_PUBLIC_ZERO_GPU"
  from gradio_client import Client, handle_file
  # This is a public free Space; no authentication, paid tokens or API keys.
  cli=Client("microsoft/TRELLIS.2",verbose=False)
  endpoints={str(k):str(v.api_name) for k,v in cli.endpoints.items()}
  report["endpoint_names"]=endpoints
  generate_name=next((name for name in endpoints.values() if name.endswith("image_to_3d")),None)
  extract_name=next((name for name in endpoints.values() if name.endswith("extract_glb")),None)
  if not generate_name or not extract_name: raise RuntimeError("Public endpoint names unavailable, no paid fallback")
  # Exactly one submission, deliberately small 512 grid and default sampler parameters.
  args=[handle_file(str(imagepath)),172211,"512",7.5,0.7,12,5.,7.5,0.5,12,3.,1.,0.,12,3.]
  job=cli.submit(*args,api_name=generate_name)
  report["submitted"]=True
  result=job.result(timeout=260)
  report["generation_return_type"]=type(result).__name__
  assert isinstance(result,(tuple,list)) and len(result)>=2,"unexpected Gradio output"
  report["preview_image_count"]=len(result[1]) if isinstance(result[1],list) else None
  # A generation preview is NOT a 3D file; require the second GLB extraction step.
  second=cli.submit(result[0],60000,1024,api_name=extract_name)
  extracted=second.result(timeout=260)
  candidates=[]
  def walk(o):
   if isinstance(o,str) and o.lower().endswith(".glb"):candidates.append(o)
   elif isinstance(o,dict):
    for v in o.values():walk(v)
   elif isinstance(o,(list,tuple)):
    for v in o:walk(v)
  walk(extracted)
  assert candidates,"No GLB returned by second stage; do not claim success"
  from urllib.parse import urlparse
  from urllib.request import urlretrieve
  p=candidates[0]
  if p.startswith("http://") or p.startswith("https://"):
   urlretrieve(p,OUT/"run211_unapproved.glb")
  else: shutil.copy2(p,OUT/"run211_unapproved.glb")
  glb=OUT/"run211_unapproved.glb"
  report["glb_bytes"]=glb.stat().st_size
  report["glb_sha256"]=sha(glb)
  assert glb.read_bytes()[:4]==b"glTF","Invalid GLB magic"
  report["status"]="NEW_NATIVE_GLB_UNREVIEWED"
  try: render_glb(glb)
  except Exception as e:
   report["render_error"]=str(e)
   report["render_traceback"]=traceback.format_exc()[-4000:]
   report["status"]="GLB_RENDER_FAILED_NO_RELEASE"
 except Exception as e:
  report["error"]=str(e)
  report["traceback"]=traceback.format_exc()[-5000:]
  report["status"]="REMOTE_OR_INPUT_FAILURE_NO_RELEASE"
 finally:
  report["runtime_seconds"]=round(time.monotonic()-start,2)
  report["evidence_files"]={p.name:{"bytes":p.stat().st_size,"sha256":sha(p)} for p in sorted(OUT.iterdir()) if p.is_file() and p.name not in ("run211_report.json","run211_report.md")}
  (OUT/"run211_report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False,default=str))
  summary=("# Run211 — Public ZeroGPU TRELLIS.2 single real trial, NO_RELEASE\n\n"
           "This is a detached #172 research trial, not a production or accepted 3D sample.\n\n"
           "Status: **"+report["status"]+"**. Art gate: **NOT PASSED**; mobile GPU: **NOT TESTED**; paid spend: **USD 0**.\n\n"
           "Source: fixed SHA256 of owl-pet design plate, exact rightmost crop and documented GrabCut matte.\n\n"
           "Model: official public microsoft/TRELLIS.2 on Hugging Face ZeroGPU, no token, max one free submission.\n\n"
           "Raw report: [run211_report.json](run211_report.json). The unapproved model, if generated, is held only in an Actions evidence artifact and is never published as an accepted pet.\n\n"
           "Service/error: "+str(report.get("error",report.get("render_error","none reported")))+"\n")
  (OUT/"run211_report.md").write_text(summary)
  print(json.dumps({k:v for k,v in report.items() if k!="traceback" and k!="render_traceback"},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
