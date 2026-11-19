#!/usr/bin/env python3
"""Run229: a genuinely executed non-rigid sculpt *negative experiment* on a real adult Tyto scan.
NOT an accepted juvenile; no simple assembled fake, no model release, no main/prototype changes.
Source: Zenodo museum record 21379215, metadata cc-zero; specimen is adult Tyto alba.
Input: native GLB correctly decoded from Khronos Draco by glTF-Transform, verified SHA.
"""
import json, hashlib, traceback, datetime, math
from pathlib import Path
import numpy as np, trimesh, vtk
from PIL import Image, ImageDraw
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray

ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=ROOT/"run229-evidence"
OUT.mkdir(parents=True,exist_ok=True)
SOURCE=OUT/"donor_uncompressed_adult.glb"
SHA="4865f48828adb93cef4f5ec07002adc1a61855a80adb286f781a227fca89430f"
R={"run":"229","utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
   "donor":"adult CC0-claimed museum Tyto alba, NOT juvenile castanops",
   "intended":"#172 v3 rightmost mesoptile; cream true down, heart face, squat, concealed wings/tail, supported hollow",
   "no_extra_paid_usd":0,"mobile_webgl":"NOT_TESTED","release":"NO_RELEASE",
   "art_status":"UNREVIEWED_PENDING_HUMAN_VISUAL_QA_NOT_APPROVED"}

def digest(p):
 b=Path(p).read_bytes()
 return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}

def warp(vertices):
 # Native glTF mesh Z-negative is UP; scene transform maps it to world Y-up.
 # Retain scanned organic topology/material UVs and alter body/head continuously.
 # Still not a real juvenile anatomy sculpt: if the final shape fails, reject.
 v=np.asarray(vertices).copy()
 x,y,z=v[:,0],v[:,1],v[:,2]
 head=np.clip((-z-.37)/.16,0,1)
 head=head*head*(3-2*head)
 torso=np.exp(-((z+.36)/.09)**2)
 v[:,0]=.025+(x-.025)*(1.09+.27*head+.17*torso)
 v[:,1]=-.055+.17*np.tanh((y+.055)/.17)
 v[:,2]=z+.033*head+.018*torso
 return v

def geometry(scene):
 return [m for m in scene.dump() if isinstance(m,trimesh.Trimesh) and len(m.faces)>100]

def render(geos,name):
 ren=vtk.vtkRenderer()
 ren.SetBackground(.89,.90,.91)
 win=vtk.vtkRenderWindow()
 win.SetOffScreenRendering(True)
 win.SetSize(440,440)
 win.AddRenderer(ren)
 tex_handles=[]
 for i,m in enumerate(geos):
  poly=vtk.vtkPolyData()
  pts=vtk.vtkPoints()
  pts.SetData(numpy_to_vtk(np.ascontiguousarray(m.vertices,dtype=np.float64),deep=True))
  poly.SetPoints(pts)
  rows=np.column_stack([np.full(len(m.faces),3,dtype=np.int64),m.faces.astype(np.int64)]).ravel()
  cells=vtk.vtkCellArray()
  cells.SetCells(len(m.faces),numpy_to_vtkIdTypeArray(rows,deep=True))
  poly.SetPolys(cells)
  mapper=vtk.vtkPolyDataMapper()
  mapper.SetInputData(poly)
  actor=vtk.vtkActor()
  actor.SetMapper(mapper)
  material=getattr(m.visual,"material",None)
  tex=getattr(material,"baseColorTexture",None)
  if tex is None:tex=getattr(material,"image",None)
  uv=getattr(m.visual,"uv",None)
  if tex is not None and uv is not None and len(uv)==len(m.vertices):
   img=Image.fromarray(np.asarray(tex)).convert("RGB")
   texpath=OUT/("run229_"+name+"_texture_"+str(i)+".png")
   img.save(texpath)
   tc=numpy_to_vtk(np.asarray(uv,dtype=np.float32),deep=True)
   tc.SetName("UV")
   poly.GetPointData().SetTCoords(tc)
   reader=vtk.vtkPNGReader()
   reader.SetFileName(str(texpath))
   reader.Update()
   texture=vtk.vtkTexture()
   texture.SetInputConnection(reader.GetOutputPort())
   texture.InterpolateOn()
   actor.SetTexture(texture)
   tex_handles.append(texture)
  ren.AddActor(actor)
 b=np.array(ren.ComputeVisiblePropBounds()).reshape((3,2))
 assert np.isfinite(b).all() and (b[:,1]>b[:,0]).all()
 mid=b.mean(axis=1)
 size=float(np.max(b[:,1]-b[:,0]))
 # Seven REAL cameras; glTF scene transform makes WORLD Y UP and Z horizontal.
 cams=[("left",[-3,0,0],[0,1,0]),
       ("front",[0,0,3],[0,1,0]),
       ("right",[3,0,0],[0,1,0]),
       ("back",[0,0,-3],[0,1,0]),
       ("oblique",[2,1,2],[0,1,0]),
       ("top",[0,3,0],[0,0,-1]),
       ("bottom",[0,-3,0],[0,0,1])]
 ims,records=[],[]
 for label,vec,up in cams:
  camera=ren.GetActiveCamera()
  camera.ParallelProjectionOn()
  camera.SetPosition(*(mid+size*np.array(vec,dtype=float)))
  camera.SetFocalPoint(*mid)
  camera.SetViewUp(*up)
  camera.SetParallelScale(size*.72)
  ren.ResetCameraClippingRange()
  win.Render()
  p=OUT/("run229_"+name+"_"+label+"_REAL3D_ART_UNAPPROVED.png")
  w=vtk.vtkWindowToImageFilter()
  w.SetInput(win);w.Update()
  writer=vtk.vtkPNGWriter()
  writer.SetFileName(str(p))
  writer.SetInputConnection(w.GetOutputPort());writer.Write()
  im=np.asarray(Image.open(p).convert("RGB"),dtype=np.int16)
  fg=int((np.max(np.abs(im-np.array([227,230,232])),axis=2)>25).sum())
  assert fg>1000,("EMPTY CAMERA",label,fg)
  ims.append((label,p))
  records.append({"camera":label,"foreground_pixels":fg,"file":p.name,"file_integrity":digest(p)})
 win.Finalize()
 return ims,records

try:
 assert SOURCE.exists() and digest(SOURCE)["sha256"]==SHA
 ref=Path("owl-pet/design/concepts/172-tyto-castanops-v3.png")
 assert digest(ref)["sha256"]=="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
 R["original_v3_concept"]=digest(ref)
 scene=trimesh.load(str(SOURCE),force="scene",process=False)
 scanned=geometry(scene)
 assert scanned
 morph=scene.copy()
 for m in morph.geometry.values():m.vertices=warp(m.vertices)
 p=OUT/"run229_REAL_PHOTOGRAMMETRY_NONRIGID_MORPH_EXPERIMENT_NOT_APPROVED.glb"
 morph.export(str(p))
 imported=trimesh.load(str(p),force="scene",process=False)
 geos=geometry(imported)
 xyz=np.vstack([m.vertices for m in geos])
 spans=np.ptp(xyz,axis=0)
 assert np.isfinite(xyz).all() and np.all(spans>1e-4)
 R["native_model"]={"source":digest(SOURCE),"morph":digest(p),
     "triangles":int(sum(len(m.faces) for m in geos)),
     "bounds":imported.bounds.tolist(),"nonzero_spans":spans.tolist(),
     "visual_kind":[m.visual.kind for m in geos]}
 original,original_stats=render(scanned,"source_adult")
 mutated,mutated_stats=render(geos,"nonrigid_study")
 contact=Image.new("RGB",(7*250,2*288),(245,247,249))
 pen=ImageDraw.Draw(contact)
 for row,ims in enumerate((original,mutated)):
  for col,(label,fn) in enumerate(ims):
   x,y=col*250,row*288
   pen.text((x+5,y+5),("ADULT " if row==0 else "MORPH ")+label,fill=(35,35,35))
   contact.paste(Image.open(fn).convert("RGB").resize((242,242)),(x+4,y+32))
 sheet=OUT/"run229_14_ACTUAL_MESH_CAMERAS_ART_UNAPPROVED.png"
 contact.save(sheet)
 R["contact"]=digest(sheet)
 R["source_views"]=original_stats
 R["morph_views"]=mutated_stats
 R["status"]="TRUE_NATIVE_GLB_AND_14_RENDERED_VIEWS_EXIST_BUT_ART_NOT_ACCEPTED"
except BaseException as e:
 R["status"]="INCOMPLETE_ART_UNAPPROVED"
 R["error"]=repr(e)
 R["traceback"]=traceback.format_exc()[-6000:]
finally:
 R["files"]={p.name:digest(p) for p in OUT.iterdir() if p.is_file() and p.name!="run229_machine_report.json"}
 (OUT/"run229_machine_report.json").write_text(json.dumps(R,ensure_ascii=False,indent=2,default=str)+"\n")
 print(json.dumps({"status":R["status"],"model":R.get("native_model"),
                   "contact":R.get("contact"),"error":R.get("error")},ensure_ascii=False),flush=True)
