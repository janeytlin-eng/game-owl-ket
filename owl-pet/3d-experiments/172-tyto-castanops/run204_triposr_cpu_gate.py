#!/usr/bin/env python3
"""Run204 genuine CPU image-to-mesh attempt and negative-asset gate; no art approval."""
import hashlib,json,os,platform,subprocess,sys,time,traceback
from datetime import datetime,timezone
from pathlib import Path
R=Path("owl-pet/3d-experiments/172-tyto-castanops")
E=R/"research-evidence-run204-TRIPOSR-CPU-NATIVE-NO_RELEASE"
SRC=R/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
SOURCE_SHA="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
PREFLIGHT=["owl-pet/AGENTS.md","owl-pet/README.md","owl-pet/STATUS.md",
 "owl-pet/prototype/index.html","owl-pet/research/species/172-tyto-castanops-v3.md",
 str(R/"known_rejected_asset_sha256_registry.json"),
 str(R/"2026-11-19-run203d-independent-semantic-correction-NO_RELEASE.md")]
S={"run":204,"utc":datetime.now(timezone.utc).isoformat(),"model":"VAST-AI-Research/TripoSR",
 "device":"GitHub-hosted CPU","extra_payment":0,"new_native_glb":False,
 "sevenview_rendered":False,"art_approved":False,"physical_phone_gpu":False,"release":False}
def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,x):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+"\n")
def inspect():
 import numpy as np,trimesh,vtk
 from PIL import Image,ImageDraw
 target=E/"inference"/"0"/"mesh.glb"
 if not target.is_file() or target.stat().st_size<2048:
  S["gate"]="NO_NATIVE_GLB";return
 raw=target.read_bytes();fingerprint=sha(raw)
 sc=trimesh.load(target,force="scene",process=False)
 details={"sha256":fingerprint,"bytes":len(raw),"meshes":len(sc.geometry),
  "triangles":sum(len(x.faces) for x in sc.geometry.values() if hasattr(x,"faces"))}
 save(E/"native_mesh_inspection.json",details)
 rejected=json.loads((R/"known_rejected_asset_sha256_registry.json").read_text())
 known=set()
 for a in rejected["known_rejected_source_glbs"]:
  known.add(a["sha256"].lower())
  for b in a.get("derived_rejected_lods",[]):known.add(b["sha256"].lower())
 S["new_native_glb"]=fingerprint not in known and details["triangles"]>=100
 if not S["new_native_glb"]:
  S["gate"]="FINGERPRINT_DUPLICATE_OR_DEGENERATE";return
 vtk.vtkObject.GlobalWarningDisplayOff()
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(True);win.SetSize(480,480)
 imp=vtk.vtkGLTFImporter();imp.SetFileName(str(target));imp.SetRenderWindow(win);imp.Update()
 ren=win.GetRenderers().GetFirstRenderer()
 if ren is None:raise RuntimeError("VTK importer returned no renderer")
 ren.SetBackground(.87,.88,.85)
 bb=ren.ComputeVisiblePropBounds()
 c=np.array([(bb[0]+bb[1])/2,(bb[2]+bb[3])/2,(bb[4]+bb[5])/2])
 d=max(bb[1]-bb[0],bb[3]-bb[2],bb[5]-bb[4])
 if not np.isfinite(d) or d<=0:raise RuntimeError("Invalid render bounds")
 views={"front":([0,0,1],[0,1,0]),"back":([0,0,-1],[0,1,0]),
  "left":([-1,0,0],[0,1,0]),"right":([1,0,0],[0,1,0]),
  "top":([0,1,0],[0,0,-1]),"bottom":([0,-1,0],[0,0,1]),
  "quarter":([.65,.25,1],[0,1,0])}
 ims=[]
 for name,(v,up) in views.items():
  v=np.array(v,float);v/=np.linalg.norm(v)
  cam=ren.GetActiveCamera();cam.SetFocalPoint(*c);cam.SetPosition(*(c+2.5*d*v))
  cam.SetViewUp(*up);cam.ParallelProjectionOn();cam.SetParallelScale(.74*d)
  ren.ResetCameraClippingRange();win.Render()
  flt=vtk.vtkWindowToImageFilter();flt.SetInput(win);flt.ReadFrontBufferOff();flt.Update()
  p=E/("native_"+name+".png");writer=vtk.vtkPNGWriter()
  writer.SetFileName(str(p));writer.SetInputConnection(flt.GetOutputPort());writer.Write()
  if not p.exists() or p.stat().st_size<2000:raise RuntimeError("Missing real render "+name)
  ims.append((name,Image.open(p).convert("RGB").copy()))
 contact=Image.new("RGB",(1920,1050),(245,245,243));draw=ImageDraw.Draw(contact)
 for i,(name,im) in enumerate(ims):
  x=i%4*480;y=i//4*525;draw.text((x+12,y+8),name,fill=(0,0,0));contact.paste(im,(x,y+30))
 contact.save(E/"native_contact.png")
 S["sevenview_rendered"]=True;S["gate"]="NATIVE_GLTF_SEVENVIEW_UNREVIEWED"
def archive():
 save(E/"status.json",S)
 lines=["# Run204 — official MIT TripoSR CPU image-to-native-GLB trial / NO_RELEASE","",
  "Original pinned rightmost #172 v3 mesoptile source sha256: "+SOURCE_SHA+".",
  "Preflight: README, AGENTS, STATUS, old cat WebGL prototype, v3 design, Run203d and rejection registry.",
  "Actual official pretrained image-to-3D inference attempted on no-charge GitHub-hosted CPU.",
  "Recorded gate: "+str(S.get("gate"))+"; native GLB: "+str(S["new_native_glb"])+
  "; independent native seven-view rendered: "+str(S["sevenview_rendered"])+".",
  "Exit code: "+str(S.get("exit_code","not reached"))+"; see separate raw log and checksum manifest.",
  "Marching-cubes CPU mesh is NOT an artistic pass. Heart-shaped disc, cream down, chick anatomy,",
  "concealed tail/short wings, coherent sides/back and hollow support remain unapproved.",
  "No real phone GPU test. No production, main, existing prototype or deployment changes.",
  "Quarantined original 3D GLB and renders in Actions artifact only; no model release, no extra payment.",
  "**NO_RELEASE / NO_NOTIFICATION.**"]
 (R/"2026-11-19-run204-triposr-cpu-sourcebound-NO_RELEASE.md").write_text("\n".join(lines)+"\n")
 inventory={}
 for p in sorted(E.rglob("*")):
  if p.is_file() and p.name!="manifest.json":
   b=p.read_bytes();inventory[str(p.relative_to(E))]={"bytes":len(b),"sha256":sha(b)}
 save(E/"manifest.json",inventory)
def main():
 E.mkdir(parents=True,exist_ok=True)
 try:
  evidence={}
  for path in PREFLIGHT:
   b=Path(path).read_bytes()
   if len(b)<50:raise RuntimeError("Empty preflight "+path)
   evidence[path]={"bytes":len(b),"sha256":sha(b)}
  b=SRC.read_bytes()
  if sha(b)!=SOURCE_SHA:raise RuntimeError("Rightmost v3 reference SHA mismatch")
  evidence[str(SRC)]={"bytes":len(b),"sha256":sha(b)}
  evidence["runtime"]={"python":sys.version,"platform":platform.platform(),"cpus":os.cpu_count()}
  save(E/"preflight.json",evidence)
  cmd=[sys.executable,"/tmp/TripoSR/run.py",str(SRC.resolve()),"--device","cpu",
   "--mc-resolution","128","--chunk-size","1024","--model-save-format","glb",
   "--output-dir",str((E/"inference").resolve())]
  S["command"]=cmd
  start=time.monotonic()
  with (E/"inference_console.log").open("w") as log:
   p=subprocess.run(cmd,cwd="/tmp/TripoSR",stdout=log,stderr=subprocess.STDOUT,timeout=2100,
    env={**os.environ,"OMP_NUM_THREADS":"2","MKL_NUM_THREADS":"2","TOKENIZERS_PARALLELISM":"false"})
  S["exit_code"]=p.returncode;S["inference_seconds"]=round(time.monotonic()-start,2)
  if p.returncode==0:inspect()
  else:S["gate"]="INFERENCE_ERROR_SEE_RAW_LOG"
 except Exception as err:
  S["gate"]="SETUP_OR_RUNTIME_ERROR";S["error"]=repr(err)
  (E/"exception_trace.txt").write_text(traceback.format_exc())
 finally:
  archive()
  print(json.dumps({k:S.get(k) for k in ["gate","exit_code","error","new_native_glb","sevenview_rendered","release"]},indent=2))
if __name__=="__main__": main()
