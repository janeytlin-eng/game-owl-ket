#!/usr/bin/env python3
"""Run230 free public juvenile asset probe; NO LOGIN BYPASS / NO PAYMENT / NO RELEASE.
Source candidates are Meshy contributor-claimed CC0 community posts; not #172 v3.
Do not call a thumbnail, GLB magic, or machine render an approved 3D character.
"""
import hashlib, html, json, datetime, re, struct, traceback
from pathlib import Path
from urllib.parse import urlparse
import requests
import numpy as np
import trimesh

ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=ROOT/"run230-evidence"
OUT.mkdir(parents=True,exist_ok=True)
REPORT=OUT/"run230_machine_report.json"
SOURCES=[
 ("sunlit_owlet","https://www.meshy.ai/posts/Sunlit-Owlet-01a00f65-b940-70c9-817a-255fff4654d8"),
 ("heartshaped_barn_owl","https://www.meshy.ai/3d-models/HeartShaped-Barn-Owl-019ee9c5-915d-70bf-897b-1c0ce16030f4"),
]
R={"run":"230","utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
"intended":"#172 Tyto castanops v3 rightmost cream downy juvenile, naturally joined heart facial disc, small wings/concealed tail, hollow perch and credible 360 degrees",
"policy":"Only explicitly visible public GLB URLs from public page HTML; NEVER guess authenticated API endpoints, scrape logged-in content, bypass a download gate, or pay.",
"extra_paid_usd":0,"status":"NOT_RUN","release":"NO_RELEASE","art_approved":False,"phone_webgl":"NOT_TESTED","sources":[]}

def fingerprint(p):
 b=Path(p).read_bytes()
 return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}

def linked_glbs(s):
 t=html.unescape(s).replace("\\/","/").replace("\\u0026","&")
 candidates=re.findall(r'https://[^\s"\'<>\\]{1,1600}?\.glb(?:\?[^\s"\'<>\\]{0,1000})?',t,re.I)
 out=[]
 for u in candidates:
  pr=urlparse(u)
  if pr.hostname in ("cdn.meshy.ai","api.meshy.ai","www.meshy.ai","meshy.ai") and u not in out:out.append(u)
 return out[:6]

def native_model(path):
 b=path.read_bytes()
 if len(b)<20 or b[:4]!=b"glTF" or struct.unpack_from("<I",b,8)[0]!=len(b):
  raise ValueError("Not a genuine length-consistent binary glTF")
 sc=trimesh.load(str(path),force="scene",process=False)
 meshes=[m for m in sc.dump() if isinstance(m,trimesh.Trimesh) and len(m.faces)>0]
 if not meshes:raise ValueError("No genuine triangles")
 v=np.concatenate([m.vertices for m in meshes],axis=0)
 span=np.ptp(v,axis=0)
 if not np.isfinite(v).all() or np.any(span<=.00001):raise ValueError("Zero/spurious 3D bounds")
 out={"native_glb":fingerprint(path),"triangles":int(sum(len(m.faces) for m in meshes)),
      "meshes":len(meshes),"bounds":sc.bounds.tolist(),"real_xyz_spans":span.tolist()}
 if out["triangles"]>300000:
  out["seven_cameras"]="NOT_RENDERED_HIGH_POLYGON_NOT_MOBILE_READY"
  return out
 import vtk
 from PIL import Image, ImageDraw
 from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
 ren=vtk.vtkRenderer();ren.SetBackground(.89,.90,.91)
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(True);win.SetSize(380,380);win.AddRenderer(ren)
 for m in meshes:
  poly=vtk.vtkPolyData();pts=vtk.vtkPoints()
  pts.SetData(numpy_to_vtk(np.asarray(m.vertices,dtype=np.float64),deep=True));poly.SetPoints(pts)
  rows=np.column_stack([np.full(len(m.faces),3,dtype=np.int64),m.faces.astype(np.int64)]).ravel()
  cells=vtk.vtkCellArray();cells.SetCells(len(m.faces),numpy_to_vtkIdTypeArray(rows,deep=True));poly.SetPolys(cells)
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
  actor=vtk.vtkActor();actor.SetMapper(mapper);ren.AddActor(actor)
 b=np.asarray(ren.ComputeVisiblePropBounds()).reshape(3,2)
 center=b.mean(axis=1);size=float((b[:,1]-b[:,0]).max())
 cameras=[("front",[0,0,3],[0,1,0]),("left",[-3,0,0],[0,1,0]),
  ("back",[0,0,-3],[0,1,0]),("right",[3,0,0],[0,1,0]),
  ("oblique",[2,1,2],[0,1,0]),("top",[0,3,0],[0,0,-1]),("bottom",[0,-3,0],[0,0,1])]
 ims=[];out["camera_stats"]=[]
 for name,vec,up in cameras:
  cam=ren.GetActiveCamera();cam.ParallelProjectionOn()
  cam.SetPosition(*(center+size*np.asarray(vec)));cam.SetFocalPoint(*center)
  cam.SetViewUp(*up);cam.SetParallelScale(size*.8);ren.ResetCameraClippingRange()
  win.Render();w=vtk.vtkWindowToImageFilter();w.SetInput(win);w.Update()
  p=OUT/(path.stem+"_"+name+"_NOT_APPROVED.png")
  writer=vtk.vtkPNGWriter();writer.SetFileName(str(p));writer.SetInputConnection(w.GetOutputPort());writer.Write()
  arr=np.asarray(Image.open(p).convert("RGB"),dtype=np.int16)
  fg=int((np.abs(arr-np.array([227,230,232])).max(axis=2)>25).sum())
  if fg<250:raise ValueError("Blank supposed true 3D view "+name)
  ims.append((name,p));out["camera_stats"].append({"name":name,"foreground_px":fg,"sha":fingerprint(p)})
 win.Finalize()
 sheet=Image.new("RGB",(4*260,2*285),"#f3f5f7");d=ImageDraw.Draw(sheet)
 for i,(name,p) in enumerate(ims):
  x=i%4*260;y=i//4*285
  d.text((x+5,y+4),name,fill="#222222")
  sheet.paste(Image.open(p).convert("RGB").resize((250,250)),(x+5,y+28))
 dest=OUT/(path.stem+"_seven_views_ART_UNAPPROVED.png");sheet.save(dest)
 out["contact"]=fingerprint(dest);out["seven_cameras"]="TRUE_3D_RENDER_BUT_ART_UNAPPROVED"
 return out

try:
 ref=Path("owl-pet/design/concepts/172-tyto-castanops-v3.png")
 assert fingerprint(ref)["sha256"]=="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
 R["reference"]=fingerprint(ref)
 sess=requests.Session()
 sess.headers["User-Agent"]="owl172-public-asset-research/1.0"
 for name,url in SOURCES:
  s={"name":name,"url":url,"license_claim":"CC0 (publisher claimed; not independently cleared)"}
  R["sources"].append(s)
  try:
   resp=sess.get(url,timeout=(12,45))
   s.update({"page_http":resp.status_code,"page_bytes":len(resp.content),
        "page_sha256":hashlib.sha256(resp.content).hexdigest(),
        "claims_cc0":"CC0" in resp.text})
   if resp.status_code in (401,402,403,429):
    s["status"]="AUTH_OR_LIMIT_REQUIRED_STOP";continue
   resp.raise_for_status()
   urls=linked_glbs(resp.text)
   s["public_native_glb_links_in_html"]=len(urls)
   if not urls:s["status"]="NO_PUBLIC_GLB_LINK_IN_PAGE_HTML";continue
   s["link_hosts"]=sorted({urlparse(u).hostname for u in urls})
   for i,u in enumerate(urls[:2]):
    req=sess.get(u,stream=True,timeout=(15,75))
    if req.status_code in (401,402,403,429):
     s["status"]="ASSET_AUTH_OR_LIMIT_REQUIRED_STOP";continue
    if req.status_code!=200:
     s["asset_http"]=req.status_code;continue
    p=OUT/(name+"_PUBLIC_NATIVE_CANDIDATE.glb")
    size=0
    with p.open("wb") as f:
     for part in req.iter_content(262144):
      size+=len(part)
      if size>50*1024*1024:break
      f.write(part)
    if size>50*1024*1024:
     p.unlink(missing_ok=True);s["status"]="OVER_50MIB_CAP";break
    s["geometry"]=native_model(p)
    s["status"]="TRUE_NATIVE_GLB_QUARANTINED_ART_UNAPPROVED"
    break
   if "status" not in s:s["status"]="NO_VALID_PUBLIC_BINARY_GLB"
  except Exception as e:
   s["status"]="FAILED_OR_NOT_VALID_GLB";s["error"]=repr(e)[:500]
 R["status"]="NATIVE_GLB_CANDIDATE_FOR_MANUAL_REVIEW" if any("geometry" in s for s in R["sources"]) else "NO_NEW_NATIVE_GLB"
except BaseException as e:
 R["status"]="INCOMPLETE";R["error"]=repr(e);R["traceback"]=traceback.format_exc()[-4000:]
finally:
 R["files"]={p.name:fingerprint(p) for p in OUT.iterdir() if p.is_file() and p!=REPORT}
 REPORT.write_text(json.dumps(R,indent=2,ensure_ascii=False)+"\n")
 print(json.dumps({"status":R["status"],"sources":[{"name":s["name"],"http":s.get("page_http"),"status":s.get("status"),"public_glb_links":s.get("public_native_glb_links_in_html"),"error":s.get("error")} for s in R["sources"]]},ensure_ascii=False),flush=True)
