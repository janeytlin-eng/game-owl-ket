#!/usr/bin/env python3
"""Run224b: independently DECODE Khronos Draco glTF before 3D render.
Run224 erroneously displayed blank frames and zero bounds for three compressed GLBs.
Do not mistake a reported triangle count or a PNG > 1 kB for successful geometry.
Adult Barn Owl scientific scan only, NEVER an approved #172 juvenile pet.
"""
import pathlib,hashlib,json,struct,subprocess,traceback,math,datetime
import requests,numpy as np,trimesh,vtk
from PIL import Image,ImageDraw
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray

OUT=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops/run224b-evidence");OUT.mkdir(parents=True,exist_ok=True)
UID="0e65de5934db4f0eae02835ba7227dcc"
NAMES=[("optimized",UID+"_normalized_optimized.glb",5603344),("optimized_025",UID+"_normalized_optimized-0.250.glb",2185576),("normalized_010",UID+"_normalized-0.100.glb",1634244)]
R={"run":"224b","utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "correction_of":"Run224 native scene import appeared to succeed but Draco-required geometry had all-zero bounds. Blank screenshots != successful 3D rendering.",
 "source":"Zenodo museum CC0-claimed archived adult Tyto alba scan, record 21379215",
 "target":"#172 Tyto castanops age-unknown cream down mesoptile; archive adult is not a substitute",
 "no_extra_paid_usd":0,"main_production_modified":False,"release":"NO_RELEASE",
 "phone_webgl":"NOT_TESTED","cases":{},"files":{}}
def sha(p):
 return {"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def inspect_glb(p):
 with p.open("rb") as f:
  a=f.read(20)
  magic,version,total,jlength,typ=struct.unpack("<4sIIII",a)
  if magic!=b"glTF" or total!=p.stat().st_size or typ!=0x4e4f534a:raise ValueError("invalid GLB header")
  d=json.loads(f.read(jlength).decode("utf8"))
 return {"extensions_required":d.get("extensionsRequired",[]),
  "faces_accessor":sum(a.get("count",0)//3 for a in d.get("accessors",[]) if a.get("type")=="SCALAR"),
  "materials":len(d.get("materials",[])),"meshes":len(d.get("meshes",[]))}
def native_valid(sc):
 geos=[g for g in sc.dump() if isinstance(g,trimesh.Trimesh) and len(g.faces)]
 if not geos:raise ValueError("No actual triangle geometry")
 xyz=np.concatenate([g.vertices for g in geos],axis=0)
 dim=np.ptp(xyz,axis=0)
 degenerate=float(np.mean(np.linalg.norm(xyz,axis=1)<1e-10))
 if not np.isfinite(xyz).all() or np.max(dim)<1e-3 or np.sum(dim>1e-5)<2:
  raise ValueError("DEGENERATE_3D: raw geometry bounds "+repr(dim.tolist()))
 if degenerate>0.99:raise ValueError("DEGENERATE_3D: 99% zero vertices")
 return geos,{"num_meshes":len(geos),"faces":sum(len(g.faces) for g in geos),
  "vertices":len(xyz),"bbox_dimensions":np.round(dim,5).tolist(),"zero_vertex_fraction":round(degenerate,5)}
def render(name,geos):
 ren=vtk.vtkRenderer();win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1)
 win.SetSize(420,420);win.AddRenderer(ren);ren.SetBackground(.89,.90,.91)
 count=0
 for i,g in enumerate(geos):
  poly=vtk.vtkPolyData();points=vtk.vtkPoints()
  points.SetData(numpy_to_vtk(np.asarray(g.vertices,dtype=np.float64),deep=True));poly.SetPoints(points)
  f=np.column_stack((np.full(len(g.faces),3,dtype=np.int64),np.asarray(g.faces,dtype=np.int64))).ravel()
  cells=vtk.vtkCellArray();cells.SetCells(len(g.faces),numpy_to_vtkIdTypeArray(f,deep=True));poly.SetPolys(cells)
  m=vtk.vtkPolyDataMapper();m.SetInputData(poly);act=vtk.vtkActor();act.SetMapper(m)
  mat=getattr(g.visual,"material",None)
  tex=getattr(mat,"baseColorTexture",None)
  if tex is None:tex=getattr(mat,"image",None)
  uv=getattr(g.visual,"uv",None)
  if tex is not None and uv is not None and len(uv)==len(g.vertices):
   try:
    img=Image.fromarray(np.asarray(tex)).convert("RGB")
    p=OUT/("run224b_"+name+"_texture_"+str(i)+".png");img.save(p)
    tc=numpy_to_vtk(np.asarray(uv,dtype=np.float32),deep=True);tc.SetName("uv")
    poly.GetPointData().SetTCoords(tc)
    reader=vtk.vtkPNGReader();reader.SetFileName(str(p));reader.Update()
    tx=vtk.vtkTexture();tx.SetInputConnection(reader.GetOutputPort());tx.InterpolateOn()
    act.SetTexture(tx);count+=1
   except Exception as e:R["cases"][name].setdefault("texture_warnings",[]).append(repr(e))
  ren.AddActor(act)
 bounds=ren.ComputeVisiblePropBounds()
 mid=np.array([(bounds[2*i]+bounds[2*i+1])/2 for i in range(3)])
 span=np.array([bounds[2*i+1]-bounds[2*i] for i in range(3)])
 upidx=int(np.argmax(span));axes=[i for i in range(3) if i!=upidx];width=float(max(span))
 if width<.001:raise ValueError("renderer 3D bounds degenerate")
 ims=[]
 for deg in (0,90,180,270):
  theta=math.radians(deg);direction=np.zeros(3)
  direction[axes[0]]=math.cos(theta);direction[axes[1]]=math.sin(theta)
  cam=ren.GetActiveCamera();cam.ParallelProjectionOn()
  cam.SetFocalPoint(*mid);cam.SetPosition(*(mid+direction*3*width))
  cam.SetViewUp(*np.eye(3)[upidx]);cam.SetParallelScale(.7*width)
  ren.ResetCameraClippingRange();win.Render()
  q=OUT/("run224b_"+name+"_deg"+str(deg)+".png")
  filt=vtk.vtkWindowToImageFilter();filt.SetInput(win);filt.Update()
  writer=vtk.vtkPNGWriter();writer.SetFileName(str(q));writer.SetInputConnection(filt.GetOutputPort());writer.Write()
  img=np.asarray(Image.open(q).convert("RGB")).astype(np.int16)
  bg=np.array([227,230,232])
  non_bg=int((np.max(abs(img-bg),axis=2)>25).sum())
  if non_bg<500:raise ValueError(f"EMPTY_RENDER {name} {deg}, foreground={non_bg}")
  ims.append(q)
 R["cases"][name]["render"]={"views":len(ims),"native_texture_actors":count,"orientation_verified":False,
   "note":"VTK still approximates PBR; this is adult archive material not juvenile"}
 return ims
def contact(views):
 im=Image.new("RGB",(1680,3*454),(240,242,244));pen=ImageDraw.Draw(im)
 for k,(name,imgs) in enumerate(views.items()):
  for i,p in enumerate(imgs):
   x=i*420;y=k*454;im.paste(Image.open(p).convert("RGB"),(x,y+25))
   pen.text((x+12,y+5),name+" actual decoded Draco 3D azimuth "+str(i*90),fill=(30,30,30))
 im.save(OUT/"run224b_draco_decoded_12views_ADULT_NOT_APPROVED.png")
try:
 views={}
 ref=pathlib.Path("owl-pet/design/concepts/172-tyto-castanops-v3.png")
 R["reference"]=sha(ref)
 if R["reference"]["sha256"]!="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d":raise ValueError("design reference changed")
 for name,file,expected in NAMES:
  d=R["cases"][name]={"archive_filename":file,"expected_bytes":expected}
  try:
   url="https://zenodo.org/api/records/21379215/files/"+file+"/content"
   r=requests.get(url,timeout=(25,120));d["http"]=r.status_code;r.raise_for_status()
   source=OUT/("run224b_"+name+"_draco_ARCHIVE_ADULT_ONLY.glb");source.write_bytes(r.content)
   d["source"]=sha(source)
   if d["source"]["bytes"]!=expected:raise ValueError("archive byte count mismatch")
   d["source_glb"]=inspect_glb(source)
   dest=OUT/("run224b_"+name+"_decoded_REAL_UNCOMPRESSED_ADULT_ONLY.glb")
   cmd=["gltf-transform","copy",str(source),str(dest)]
   proc=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=180)
   d["decode_cli"]={"return_code":proc.returncode,"output_tail":proc.stdout[-2000:]}
   if proc.returncode!=0:raise RuntimeError("gltf-transform copy failed")
   d["decoded"]=sha(dest);d["decoded_glb"]=inspect_glb(dest)
   if "KHR_draco_mesh_compression" in d["decoded_glb"]["extensions_required"]:
    raise ValueError("still Draco-required after copy, decode not independent")
   sc=trimesh.load(str(dest),force="scene",process=False)
   geos,d["valid_nonzero_geometry"]=native_valid(sc)
   views[name]=render(name,geos)
   d["state"]="VALID_NONZERO_NATIVE_TRIANGLES_RENDERED"
  except Exception as e:d["state"]="UNVERIFIED_OR_FAILED";d["error"]=repr(e);d["traceback"]=traceback.format_exc()[-1500:]
 if views:contact(views)
 R["result"]="DRACO_DECODE_AND_NONZERO_GEOMETRY_QUALIFICATION_COMPLETE_ART_REJECTED_NO_RELEASE"
except Exception as e:
 R["fatal"]=repr(e);R["result"]="INCOMPLETE_NO_RELEASE"
finally:
 for p in OUT.iterdir():
  if p.is_file():R["files"][p.name]=sha(p)
 (OUT/"run224b_report.json").write_text(json.dumps(R,ensure_ascii=False,indent=2))
 print(json.dumps({"result":R["result"],"cases":{k:{"state":v.get("state"),"error":v.get("error"),"valid_geometry":v.get("valid_nonzero_geometry"),"decoded_glb":v.get("decoded_glb")} for k,v in R["cases"].items()}},ensure_ascii=False))
