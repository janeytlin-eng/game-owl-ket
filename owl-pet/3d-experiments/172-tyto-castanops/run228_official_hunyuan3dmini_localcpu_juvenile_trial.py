#!/usr/bin/env python3
"""Run228: test real official 0.6B Hunyuan3D-2mini shape reconstruction on CPU.
Isolated scientific/artistic feasibility only: NEVER release or deploy an unreviewed mesh.
No cloud inference, tokens, paid GPU, or production edits. Preserve all failure evidence.
"""
import os,sys,time,json,hashlib,traceback,importlib.util
from pathlib import Path
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"owl-pet/3d-experiments/172-tyto-castanops/run228-evidence"
OUT.mkdir(parents=True,exist_ok=True)
SRC=ROOT/"owl-pet/design/concepts/172-tyto-castanops-v3.png"
EXPECTED="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
R={"run":"Run228","timestamp_utc":datetime.now(timezone.utc).isoformat(),
 "intent":"Tyto castanops v3 rightmost cream mesoptile: investigate new official diffusion 3D base",
 "source":"https://github.com/Tencent-Hunyuan/Hunyuan3D-2",
 "weights":"tencent/Hunyuan3D-2mini","weights_license":"tencent-hunyuan-community",
 "inference":"local GitHub Actions CPU; no SaaS or external paid API",
 "model":"official 0.6B generative Hunyuan3D DiT, not TripoSR or synthetic primitives",
 "zero_additional_paid_usd":0,"status":"STARTED","release":"NO_RELEASE",
 "approved":False,"actual_phone_webgl_tested":False,
 "art_gate":"NOT_APPROVED_PENDING_REAL_7VIEW_VISUAL_QA","steps":{}}
def stamp(p):
 p=Path(p);return {"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def measure(name,fn):
 t=time.monotonic()
 try:
  out=fn()
  R["steps"][name]={"ok":True,"seconds":round(time.monotonic()-t,2)}
  return out
 except BaseException as e:
  R["steps"][name]={"ok":False,"seconds":round(time.monotonic()-t,2),"error":repr(e)}
  raise

def source_image():
 from PIL import Image
 assert SRC.exists() and stamp(SRC)["sha256"]==EXPECTED,"immutable concept SHA mismatch"
 R["canonical_original"]=stamp(SRC)
 # Reuse actually validated Run225 segmentation & restored two pupil holes.
 path=ROOT/"owl-pet/3d-experiments/172-tyto-castanops/run225_hunyuan2_official_zerogpu_juvenile_qa.py"
 spec=importlib.util.spec_from_file_location("run225_preprocess",path)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 p=Path(mod.prep());img=Image.open(p).convert("RGBA")
 bb=img.getchannel("A").getbbox()
 assert bb,"empty rightmost owl segmentation"
 img=img.crop(bb);img.thumbnail((480,480),Image.Resampling.LANCZOS)
 canvas=Image.new("RGBA",(512,512),(0,0,0,0))
 canvas.alpha_composite(img,((512-img.width)//2,(512-img.height)//2))
 p=OUT/"run228_owl_pupils_restored_2D_input_only.png"
 canvas.save(p)
 R["source_crop"]=dict(stamp(p),bbox=bb,pupil_holes=mod.R.get("restored_eye_holes"))
 return canvas

def infer(img):
 import torch,numpy as np,trimesh
 torch.set_num_threads(3)
 os.environ["OMP_NUM_THREADS"]="3"
 os.environ["MKL_NUM_THREADS"]="3"
 # No texture stage: geometry must pass seven-view artistic anatomy first.
 repo=Path(os.environ.get("RUN228_HY3D_ROOT","/tmp/Hunyuan3D-2"))
 sys.path.insert(0,str(repo))
 from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline
 def make():
  pipe=Hunyuan3DDiTFlowMatchingPipeline.from_pretrained(
   "tencent/Hunyuan3D-2mini",subfolder="hunyuan3d-dit-v2-mini",
   use_safetensors=True,device="cpu",dtype=torch.bfloat16,variant="fp16")
  R["model_loaded"]=True
  R["weights_format"]="official model.fp16.safetensors, CPU bfloat16 attempted for memory ceiling"
  # 20 diffusion steps at CPU, intermediate geometry; never silently approve this.
  with torch.no_grad():
   model_out=pipe(image=img,num_inference_steps=20,
       octree_resolution=192,num_chunks=1500,
       generator=torch.Generator(device="cpu").manual_seed(228172),
       output_type="trimesh")
  m=model_out[0]
  assert isinstance(m,trimesh.Trimesh) and len(m.faces)>1000
  assert np.isfinite(m.vertices).all()
  span=np.ptp(m.vertices,axis=0)
  assert np.min(span)>0.02,span.tolist()
  p=OUT/"run228_real_official_Hunyuan3Dmini_CPU_SHAPE_ART_NOT_APPROVED.glb"
  m.export(str(p))
  assert p.read_bytes()[:4]==b"glTF"
  imported=trimesh.load(str(p),force="scene")
  meshes=[x for x in imported.geometry.values() if isinstance(x,trimesh.Trimesh) and len(x.faces)>0]
  assert meshes
  v=np.vstack([x.vertices for x in meshes])
  assert (np.ptp(v,axis=0)>0.02).all() and np.isfinite(v).all()
  R["native_mesh"]={"GLB":stamp(p),"triangle_count":int(sum(len(x.faces) for x in meshes)),
          "vertex_count":int(sum(len(x.vertices) for x in meshes)),
          "XYZ_nonzero_spans":np.ptp(v,axis=0).round(5).tolist(),
          "texturing":"not attempted, reject geometry before paint"}
  return p
 return measure("OFFICIAL_0_6B_MODEL_CPU_SHAPE_INFERENCE",make)

def render_views(p):
 import vtk,numpy as np,trimesh
 from PIL import Image,ImageDraw
 from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
 sc=trimesh.load(str(p),force="scene")
 ren=vtk.vtkRenderer();ren.SetBackground(.91,.92,.94)
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(True);win.SetSize(440,440);win.AddRenderer(ren)
 for m in sc.geometry.values():
  if not isinstance(m,trimesh.Trimesh) or not len(m.faces):continue
  d=vtk.vtkPolyData();pts=vtk.vtkPoints()
  pts.SetData(numpy_to_vtk(np.asarray(m.vertices,dtype=np.float32),deep=True));d.SetPoints(pts)
  rows=np.column_stack((np.full(len(m.faces),3,dtype=np.int64),m.faces.astype(np.int64))).ravel()
  cells=vtk.vtkCellArray();cells.SetCells(len(m.faces),numpy_to_vtkIdTypeArray(rows,deep=True));d.SetPolys(cells)
  normal=vtk.vtkPolyDataNormals();normal.SetInputData(d);normal.SplittingOff()
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(normal.GetOutputPort())
  a=vtk.vtkActor();a.SetMapper(mapper);a.GetProperty().SetColor(.95,.90,.81)
  a.GetProperty().SetInterpolationToPhong();ren.AddActor(a)
 bounds=np.array(ren.ComputeVisiblePropBounds(),float)
 assert np.isfinite(bounds).all() and (bounds[1::2]>bounds[::2]).all()
 center=(bounds[::2]+bounds[1::2])/2;size=max(bounds[1::2]-bounds[::2])
 # Axial views not claimed as semantic FRONT until inferred coordinate axes verified.
 cameras=[("minusX",(-3,0,0)),("plusX",(3,0,0)),("minusY",(0,-3,0)),
    ("plusY",(0,3,0)),("plusZ",(0,0,3)),("minusZ",(0,0,-3)),
    ("oblique",(2,-2,1))]
 contact=Image.new("RGB",(4*330,2*365),(243,244,246))
 dr=ImageDraw.Draw(contact)
 records=[]
 for i,(name,v) in enumerate(cameras):
  cam=ren.GetActiveCamera();cam.ParallelProjectionOn()
  cam.SetPosition(*(center+size*np.array(v,dtype=float)))
  cam.SetFocalPoint(*center)
  cam.SetViewUp(*( (0,1,0) if name.endswith("Z") else (0,0,1) ))
  cam.SetParallelScale(size*.77);ren.ResetCameraClippingRange();win.Render()
  wti=vtk.vtkWindowToImageFilter();wti.SetInput(win);wti.Update()
  q=OUT/("run228_REAL_MESH_"+name+"_ART_UNAPPROVED.png")
  w=vtk.vtkPNGWriter();w.SetFileName(str(q));w.SetInputConnection(wti.GetOutputPort());w.Write()
  im=Image.open(q).convert("RGB");a=np.asarray(im,dtype=np.int16)
  fg=int((np.max(abs(a-np.array([232,235,240])),axis=2)>38).sum())
  assert fg>700, "empty 3D camera "+name
  contact.paste(im.resize((322,322)),(i%4*330,i//4*365+27))
  dr.text((i%4*330+6,i//4*365+5),name,fill=(28,31,38))
  records.append({"axis_camera":name,"foreground_pixels":fg,"file":q.name})
 contact_path=OUT/"run228_OFFICIAL_REAL_7AXIAL_MESH_QA_NOT_APPROVED.png"
 contact.save(contact_path)
 R["seven_spatial_camera_views"]=records
 R["contact_sheet"]=stamp(contact_path)
 win.Finalize()

def main():
 t=time.monotonic()
 try:
  img=measure("VERIFY_V3_AND_RESTORE_EYES",source_image)
  mesh=infer(img)
  measure("RENDER_SEVEN_REAL_SPATIAL_MESH_VIEWS",lambda:render_views(mesh))
  R["status"]="ACTUAL_NATIVE_GLB_AND_SEVEN_MESH_VIEWS_CREATED_ART_UNREVIEWED_NO_RELEASE"
 except BaseException as e:
  R["error"]=repr(e);R["traceback"]=traceback.format_exc()[-12000:]
  R["status"]="FAILED_OR_PARTIAL_NO_APPROVED_GLB_NO_RELEASE"
 finally:
  R["runtime_seconds"]=round(time.monotonic()-t,2)
  R["files"]={p.name:stamp(p) for p in sorted(OUT.iterdir()) if p.is_file() and not p.name.endswith("report.json")}
  (OUT/"run228_report.json").write_text(json.dumps(R,ensure_ascii=False,indent=2,default=str)+"\n")
  (OUT/"run228_status.md").write_text("# #172 Run228 official Hunyuan3D-2mini CPU feasibility — NO RELEASE\n\n"
   +"status: "+R["status"]+"\nerror: "+str(R.get("error","none"))+"\n"
   +"Never present raw bare mesh or green CI as an approved downy owl; no real mobile WebGL proof.\n")
  print(json.dumps({k:v for k,v in R.items() if k not in ("traceback","files")},ensure_ascii=False,default=str),flush=True)
if __name__=="__main__":main()
