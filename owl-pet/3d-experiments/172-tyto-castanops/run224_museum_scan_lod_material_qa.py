#!/usr/bin/env python3
"""Run224: honest CC0 museum Tyto adult donor: inspect archive LODs, glTF PBR metadata,
render 3D multi-view and measure 2D silhouette retention. NOT the requested juvenile.
Do not put this donor in production; all results remain research negatives.
"""
import hashlib, json, pathlib, time, traceback, math, struct
import requests
import numpy as np
from PIL import Image, ImageDraw, ImageChops
import trimesh
import vtk
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray

BASE=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops/run224-evidence")
BASE.mkdir(parents=True,exist_ok=True)
PREFIX="0e65de5934db4f0eae02835ba7227dcc"
ROOT="https://zenodo.org/api/records/21379215/files/"
MODELS=[
 ("original",PREFIX+".glb",43225496),
 ("optimized",PREFIX+"_normalized_optimized.glb",5603344),
 ("optimized_025",PREFIX+"_normalized_optimized-0.250.glb",2185576),
 ("normalized_010",PREFIX+"_normalized-0.100.glb",1634244),
]
TARGET_SHA="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
R={"run":224,"date_utc":__import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
   "goal":"Compare archive-provided native museum scan LODs and glTF PBR integrity for eventual mobile donor study",
   "source_record":"https://zenodo.org/records/21379215",
   "source_license_claim":"Zenodo metadata cc-zero; provenance claim only; separate legal check before redistribution",
   "source_species":"adult Tyto alba taxidermy, NOT Tyto castanops mesoptile",
   "target":"#172 rightmost cream down age-unknown mesoptile; natural heart disc and 360 juvenile silhouette",
   "release":"NO_RELEASE","art":"ADULT_REFERENCE_REJECTED_FOR_JUVENILE",
   "real_phone_webgl":"NOT_TESTED","paid_usd":0,
   "main_production_modified":False,"models":{},"comparison":{},"files":{}}
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1<<20),b""):h.update(b)
 return {"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def download(name, filename, expected):
 p=BASE/("run224_"+name+"_ADULT_DONOR_NOT_APPROVED.glb")
 if p.exists() and p.stat().st_size==expected:return p,{"http":"LOCAL_CACHE","bytes":expected}
 url=ROOT+filename+"/content"
 rr=requests.get(url,headers={"User-Agent":"owl172-research-run224/1.0"},timeout=(25,130),stream=True)
 meta={"url":url,"http":rr.status_code,"content_type":rr.headers.get("content-type"),"redirect":rr.url}
 rr.raise_for_status()
 with p.open("wb") as f:
  n=0
  for block in rr.iter_content(1<<20):
   if block:
    n+=len(block)
    if n>55*1024*1024:raise ValueError("download cap exceeded")
    f.write(block)
 if p.stat().st_size!=expected:raise ValueError(f"unexpected asset size {p.stat().st_size} != {expected}")
 meta["integrity"]=sha(p)
 return p,meta
def glb_info(p):
 with p.open("rb") as f:
  header=f.read(20)
  if len(header)<20 or header[:4]!=b"glTF":raise ValueError("GLB magic/length invalid")
  magic,version,length,clen,typ=struct.unpack("<4sIIII",header)
  if length!=p.stat().st_size or typ!=0x4e4f534a:raise ValueError("GLB header/chunks inconsistent")
  doc=json.loads(f.read(clen).decode("utf-8"))
 images=doc.get("images",[])
 return {"version":version,"meshes":len(doc.get("meshes",[])),"nodes":len(doc.get("nodes",[])),
  "scenes":len(doc.get("scenes",[])),"materials":len(doc.get("materials",[])),
  "images":len(images),"texture_count":len(doc.get("textures",[])),
  "extensions_used":doc.get("extensionsUsed",[]),"extensions_required":doc.get("extensionsRequired",[]),
  "primitive_count":sum(len(m.get("primitives",[])) for m in doc.get("meshes",[])),
  "accessor_vertices":sum(int(a.get("count",0)) for a in doc.get("accessors",[]) if a.get("type")=="VEC3"),
  "pbr_basecolor_maps":sum(bool(m.get("pbrMetallicRoughness",{}).get("baseColorTexture")) for m in doc.get("materials",[])),
  "images_embedded":sum("bufferView" in a for a in images),
  "image_mime_types":[x.get("mimeType","external") for x in images][:25],
  "file_length_verified":True}
def render_views(name,p):
 sc=trimesh.load(str(p),force="scene",process=False)
 ms=sc.dump()
 if isinstance(ms,trimesh.Trimesh):ms=[ms]
 ms=[g for g in ms if isinstance(g,trimesh.Trimesh) and len(g.faces)]
 N=sum(len(g.faces) for g in ms); V=sum(len(g.vertices) for g in ms)
 if N<1000:raise ValueError("not useful 3D geometry")
 ren=vtk.vtkRenderer();win=vtk.vtkRenderWindow()
 win.SetOffScreenRendering(1);win.SetSize(420,420);win.AddRenderer(ren)
 ren.SetBackground(0.89,0.90,0.91)
 uv_textured=0;vertex_color=0
 for i,g in enumerate(ms):
  pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(np.asarray(g.vertices,dtype=np.float64),deep=True))
  poly=vtk.vtkPolyData();poly.SetPoints(pts)
  f=np.column_stack((np.full(len(g.faces),3,dtype=np.int64),np.asarray(g.faces,dtype=np.int64))).ravel()
  cells=vtk.vtkCellArray();cells.SetCells(len(g.faces),numpy_to_vtkIdTypeArray(f,deep=True));poly.SetPolys(cells)
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
  actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetInterpolationToPhong()
  uv=getattr(g.visual,"uv",None)
  material=getattr(g.visual,"material",None)
  tex_image=getattr(material,"baseColorTexture",None)
  if tex_image is None:tex_image=getattr(material,"image",None)
  if uv is not None and len(uv)==len(g.vertices) and tex_image is not None:
   try:
    texarr=np.asarray(tex_image.convert("RGB") if hasattr(tex_image,"convert") else tex_image)
    if texarr.ndim==3:
     uvfield=numpy_to_vtk(np.asarray(uv,dtype=np.float32),deep=True)
     uvfield.SetName("uv");poly.GetPointData().SetTCoords(uvfield)
     png=BASE/("run224_"+name+"_tex_"+str(i)+".png")
     Image.fromarray(texarr).convert("RGB").save(png)
     reader=vtk.vtkPNGReader();reader.SetFileName(str(png));reader.Update()
     texture=vtk.vtkTexture();texture.SetInputConnection(reader.GetOutputPort());texture.InterpolateOn()
     actor.SetTexture(texture);uv_textured+=1
   except Exception as e:R["models"][name].setdefault("texture_warnings",[]).append(str(e)[:200])
  else:
   try:
    colors=np.asarray(g.visual.to_color().vertex_colors)
    if len(colors)==len(g.vertices):
     arr=numpy_to_vtk(colors[:,:3].astype(np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
     arr.SetName("color");poly.GetPointData().SetScalars(arr);mapper.SetColorModeToDirectScalars()
     vertex_color+=1
   except Exception:pass
  ren.AddActor(actor)
 bounds=ren.ComputeVisiblePropBounds()
 center=np.array([(bounds[i*2]+bounds[i*2+1])/2 for i in range(3)])
 dims=np.array([bounds[2*i+1]-bounds[2*i] for i in range(3)])
 vertical=int(np.argmax(dims));hor=[i for i in range(3) if i!=vertical]
 d=float(dims.max());up=np.eye(3)[vertical]
 pngs=[]
 for j,deg in enumerate((0,90,180,270)):
  a=math.radians(deg);axis=np.zeros(3)
  axis[hor[0]]=math.cos(a);axis[hor[1]]=math.sin(a)
  cam=ren.GetActiveCamera();cam.ParallelProjectionOn()
  cam.SetFocalPoint(*center);cam.SetPosition(*(center+axis*2.8*d));cam.SetViewUp(*up)
  cam.SetParallelScale(.69*d);ren.ResetCameraClippingRange();win.Render()
  q=BASE/("run224_"+name+"_camera_"+str(deg)+".png")
  window=vtk.vtkWindowToImageFilter();window.SetInput(win);window.Update()
  writer=vtk.vtkPNGWriter();writer.SetFileName(str(q));writer.SetInputConnection(window.GetOutputPort());writer.Write()
  if q.stat().st_size<1000:raise ValueError("render blank "+str(deg))
  pngs.append(q)
 R["models"][name]["native_scene"]={"meshes":len(ms),"faces":N,"vertices":V,
  "bounds":np.round(sc.bounds,5).tolist(),"estimated_up_axis":vertical,
  "texture_actors_vtk":uv_textured,"vertex_color_actors":vertex_color,
  "rendering_warning":"VTK not a fully glTF PBR-authentic viewer; camera axes are NOT anatomical labels"}
 return pngs
def foreground(path):
 im=Image.open(path).convert("RGB")
 arr=np.asarray(im).astype(np.int16)
 bg=np.array([round(.89*255),round(.90*255),round(.91*255)])
 mask=(np.max(abs(arr-bg),axis=2)>23)
 return mask
def make_contacts(views):
 tile=Image.new("RGB",(4*420,4*460),(239,240,243));pen=ImageDraw.Draw(tile)
 for k,(name,files) in enumerate(views.items()):
  for j,q in enumerate(files):
   x=j*420;y=k*460
   tile.paste(Image.open(q).convert("RGB"),(x,y+28))
   pen.text((x+10,y+8),f"{name} true 3D azimuth {(0,90,180,270)[j]} deg",fill=(23,23,25))
 tile.save(BASE/"run224_four_LoDs_16view_ADULT_NOT_APPROVED.png")
 return tile
try:
 reference=pathlib.Path("owl-pet/design/concepts/172-tyto-castanops-v3.png")
 R["target_reference"] = sha(reference)
 if R["target_reference"]["sha256"]!=TARGET_SHA:raise ValueError("target v3 reference SHA changed")
 views={}
 for name,fname,size in MODELS:
  R["models"][name]={"source_filename":fname,"expected_bytes":size}
  try:
   p,meta=download(name,fname,size)
   R["models"][name]["source"]=meta
   R["models"][name]["gltf"]=glb_info(p)
   R["models"][name]["import"]="PENDING"
   views[name]=render_views(name,p)
   R["models"][name]["import"]="TRUE_3D_RENDERED"
   R["models"][name]["views"]=len(views[name])
  except Exception as e:
   R["models"][name]["error"]=repr(e)
   R["models"][name]["traceback"]=traceback.format_exc()[-1600:]
 if views:
  make_contacts(views)
 if "original" in views:
  for name,files in views.items():
   if name=="original":continue
   scores=[]
   for a,b in zip(views["original"],files):
    ma=foreground(a);mb=foreground(b)
    union=(ma|mb).sum();scores.append(float((ma&mb).sum()/union) if union else 0)
   R["comparison"][name]={"silhouette_iou_4views":[round(v,4) for v in scores],
    "mean_iou":round(float(np.mean(scores)),4),
    "relative_bytes":round(R["models"][name]["source"]["integrity"]["bytes"]/R["models"]["original"]["source"]["integrity"]["bytes"],4),
    "caveat":"crude camera-normalized silhouette proxy, NOT a 3D anatomy or texture-quality endorsement"}
 R["outcome"]="ADULT_DONOR_TECHNIQUE_ONLY_ART_REJECTED_NO_RELEASE"
except Exception as e:
 R["fatal_error"]=repr(e)
 R["fatal_traceback"]=traceback.format_exc()[-1800:]
 R["outcome"]="INCOMPLETE_DIAGNOSTICS_NO_RELEASE"
finally:
 for p in BASE.iterdir():
  if p.is_file():R["files"][p.name]=sha(p)
 (BASE/"run224_report.json").write_text(json.dumps(R,ensure_ascii=False,indent=2),encoding="utf-8")
 print(json.dumps({"outcome":R["outcome"],"model_summary":{k:{"import":v.get("import"),"error":v.get("error"),"native_scene":v.get("native_scene"),"gltf":v.get("gltf")} for k,v in R["models"].items()},"comparison":R["comparison"],"report":str(BASE/"run224_report.json")},ensure_ascii=False))
