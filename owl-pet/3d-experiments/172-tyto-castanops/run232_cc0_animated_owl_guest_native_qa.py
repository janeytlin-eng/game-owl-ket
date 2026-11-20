#!/usr/bin/env python3
"""Run232: public guest access to a free CC0 rigged owl; STRICT NO RELEASE.
Only follow publicly exposed download links; never pay or bypass accounts.
The claimed owl is a toy-style donor, not #172 Tyto castanops juvenile.
"""
import datetime,hashlib,json,re,struct,traceback,zipfile,math
from pathlib import Path
from urllib.parse import urljoin
import requests,numpy as np,trimesh
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw
import vtk
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
BASE=Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=BASE/"run232-evidence"; OUT.mkdir(parents=True,exist_ok=True)
SRC=Path("owl-pet/design/concepts/172-tyto-castanops-v3.png")
SHA="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
URL="https://vuena.itch.io/blocky-pets-free"
R={"run":232,"date_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
"candidate":"Vuena published FREE CC0 owl with 13 animations + mobile LOD; toy-style, not Tyto juvenile",
"target":"#172 Tyto castanops v3 RIGHTMOST CREAM MESOPTILE",
"art_approved":False,"released":False,"phone_webgl":"NOT_TESTED","extra_paid_usd":0,
"source_page":URL,"license_claim":"CC0 publicly advertised, not independently audited","status":"NOT_STARTED"}
S=requests.Session();S.headers["User-Agent"]="Owl172-public-free-asset-QA/1.0"
def digest(p):
 b=Path(p).read_bytes();return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def get(url,limit=18000000):
 if not url.startswith("https://"):raise ValueError("non-HTTPS source")
 with S.get(url,timeout=(20,95),stream=True,allow_redirects=True) as resp:
  if resp.status_code!=200:raise RuntimeError("HTTP_%s at %s"%(resp.status_code,url))
  if not resp.url.startswith("https://"):raise RuntimeError("unsafe redirect")
  raw=bytearray()
  for part in resp.iter_content(256*1024):
   raw+=part
   if len(raw)>limit:raise RuntimeError("download exceeded cap")
  return bytes(raw),{"http":resp.status_code,"url":resp.url,
    "content_type":resp.headers.get("Content-Type"),"bytes":len(raw)}
def fetch_free():
 records=[];links=[]
 for suffix in ("","/purchase","/download"):
  url=URL+suffix
  try:
   raw,meta=get(url,2000000);soup=BeautifulSoup(raw,"html.parser")
   text=soup.get_text(" ",strip=True)
   records.append({"url":url,"response":meta,
       "free_guest_text":bool(re.search("no thanks|take me to the downloads|CC0",text,re.I)),
       "title":soup.title.get_text(" ",strip=True)[:100] if soup.title else ""})
   for a in soup.select("a[href]"):
    href=urljoin(meta["url"],a.get("href",""));label=a.get_text(" ",strip=True)
    if (href.startswith("https://") and
        re.search("no thanks|downloads?|\\.zip\\b|\\.glb\\b|free",href+" "+label,re.I) and
        not re.search("checkout|login|purchase|subscribe|pay|account",href,re.I)):
      links.append({"href":href,"label":label[:90]})
  except Exception as e:records.append({"url":url,"error":repr(e)})
 R["public_pages"]=records;R["public_guest_links"]=links[:25]
 # Never guess API/file ID, send email, initiate checkout, or scrape paid files.
 for item in links[:25]:
  link=item["href"]
  if not re.search("/download|\\.zip(?:\\?|$)|\\.glb(?:\\?|$)",link,re.I):continue
  try:
   raw,meta=get(link)
   if raw[:4] not in (b"PK\x03\x04",b"glTF"):
    R.setdefault("attempts",[]).append({"link":link,"outcome":"public HTML or non-native response","meta":meta});continue
   ext=".zip" if raw[:4]==b"PK\x03\x04" else ".glb"
   dest=OUT/("run232_FREE_CC0_OWL_DONOR_NOT_ART_APPROVED"+ext)
   dest.write_bytes(raw)
   R["public_download"]={"link":link,"meta":meta,"sha":digest(dest)}
   return dest
  except Exception as e:R.setdefault("attempts",[]).append({"link":link,"error":repr(e)})
 # The official product offers a browser-only "No thanks" guest link. Try that UI transparently.
 return free_browser_guest()
def free_browser_guest():
 from playwright.sync_api import sync_playwright
 events=[]
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,args=["--no-sandbox"])
  context=browser.new_context(accept_downloads=True)
  page=context.new_page()
  try:
   page.goto(URL+"/purchase",wait_until="domcontentloaded",timeout=35000)
   events.append({"step":"purchase_public","url":page.url,"title":page.title()})
   free=page.get_by_text("No thanks, just take me to the downloads")
   if not free.count():raise RuntimeError("PUBLIC_NO_THANKS_LINK_NOT_RENDERED")
   free.first.click(timeout=15000)
   page.wait_for_timeout(1500)
   events.append({"step":"free_guest_clicked","url":page.url,"title":page.title()})
   choices=[]
   for node in page.locator("a, button").all():
    label=node.inner_text(timeout=1000).strip()[:110]
    href=node.get_attribute("href") or ""
    if re.search("download|free sample|cute pets.*CC0|\\.zip\\b|\\.glb\\b",label+" "+href,re.I):
     if not re.search("starter|\\$4|\\$5|checkout|purchase|upgrade|pay|login",label+" "+href,re.I):
      choices.append((node,label,href))
   events.append({"step":"free_file_candidates","count":len(choices),
      "choices":[{"text":label,"href":href} for _,label,href in choices[:20]]})
   for node,label,href in choices[:12]:
    try:
     with page.expect_download(timeout=14000) as info: node.click(timeout=9000)
     downloaded=info.value
     dest=OUT/"run232_OFFICIAL_GUEST_FREE_SAMPLE_UNAPPROVED.zip"
     downloaded.save_as(str(dest))
     raw=dest.read_bytes()
     if raw[:4]==b"PK\\x03\\x04":
      R["browser_free_guest"]={"clicked":label,"suggested_filename":downloaded.suggested_filename,
          "file":digest(dest),"events":events}
      return dest
     if raw[:4]==b"glTF":
      other=dest.with_suffix(".glb");dest.rename(other)
      R["browser_free_guest"]={"clicked":label,"file":digest(other),"events":events}
      return other
     events.append({"step":"not_zip_or_glb","clicked":label,"bytes":len(raw)})
    except Exception as e:events.append({"step":"guest_download_attempt_failed","clicked":label,"error":repr(e)})
   raise RuntimeError("BROWSER_OFFICIAL_FREE_GUEST_NO_NATIVE_DOWNLOAD")
  finally:
   R["browser_guest_events"]=events
   browser.close()
def find_owl(pack):
 if pack.suffix==".glb":return pack
 with zipfile.ZipFile(pack) as z:
  files=[i for i in z.infolist() if not i.is_dir()]
  R["archive_members"]=[{"name":i.filename,"size":i.file_size} for i in files[:100]]
  owl=[i for i in files if "owl" in i.filename.lower() and i.filename.lower().endswith(".glb")]
  if not owl:raise RuntimeError("FREE_PACK_NO_OWL_GLB")
  owl.sort(key=lambda i:(int("lod0" in i.filename.lower()),i.file_size),reverse=True)
  picked=owl[0]
  if picked.file_size>80000000:raise RuntimeError("OWL_FILE_TOO_BIG")
  dest=OUT/"run232_NATIVE_OWL_FROM_PUBLIC_CC0_PACK_NOT_APPROVED.glb"
  dest.write_bytes(z.read(picked));R["selected_member"]=picked.filename
  return dest
def verify_model(path):
 b=path.read_bytes()
 if len(b)<20:raise ValueError("truncated GLB")
 magic,version,total,jslen,chunk=struct.unpack("<4sIIII",b[:20])
 if magic!=b"glTF" or version!=2 or total!=len(b) or chunk!=0x4e4f534a:
  raise ValueError("invalid native GLB")
 doc=json.loads(b[20:20+jslen])
 R["native"]={"sha":digest(path),"meshes":len(doc.get("meshes",[])),
 "skins":len(doc.get("skins",[])),"animation_count":len(doc.get("animations",[])),
 "animation_names":[a.get("name","") for a in doc.get("animations",[])],
 "materials":len(doc.get("materials",[])),"images":len(doc.get("images",[])),
 "extensions_required":doc.get("extensionsRequired",[])}
 if "KHR_draco_mesh_compression" in doc.get("extensionsRequired",[]):
  raise RuntimeError("DRACO_MUST_DECODE_BEFORE_GEOMETRY_QA")
 obj=trimesh.load(path,force="scene",process=False)
 meshes=[m for m in obj.dump() if isinstance(m,trimesh.Trimesh) and len(m.faces)]
 if not meshes:raise RuntimeError("NO_NONEMPTY_TRIANGLE_MESH")
 xyz=np.concatenate([m.vertices for m in meshes]);ext=np.ptp(xyz,axis=0)
 if not np.isfinite(xyz).all() or min(ext)<1e-5 or np.mean(np.max(abs(xyz),axis=1)<1e-8)>.9:
  raise RuntimeError("ZERO_POSITION_OR_INVALID_3D")
 R["geometry"]={"mesh_groups":len(meshes),"triangles":int(sum(len(m.faces) for m in meshes)),
  "vertices":int(len(xyz)),"extents":ext.tolist()}
 return meshes
def views(meshhes):
 ren=vtk.vtkRenderer();ren.SetBackground(.89,.90,.91);ren.SetUseFXAA(False)
 win=vtk.vtkRenderWindow();win.AddRenderer(ren);win.SetOffScreenRendering(True);win.SetSize(420,420)
 for m in meshhes:
  poly=vtk.vtkPolyData();points=vtk.vtkPoints()
  points.SetData(numpy_to_vtk(np.ascontiguousarray(m.vertices,dtype=np.float64),deep=True));poly.SetPoints(points)
  faces=np.column_stack([np.full(len(m.faces),3,dtype=np.int64),np.asarray(m.faces,dtype=np.int64)]).ravel()
  cells=vtk.vtkCellArray();cells.SetCells(len(m.faces),numpy_to_vtkIdTypeArray(faces,deep=True));poly.SetPolys(cells)
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
  actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetColor(.83,.80,.70);ren.AddActor(actor)
 bounds=np.array(ren.ComputeVisiblePropBounds()).reshape(3,2)
 if not np.isfinite(bounds).all():raise RuntimeError("NO_3D_ACTORS")
 center=bounds.mean(axis=1);ext=bounds[:,1]-bounds[:,0];axis=np.eye(3)
 up=int(np.argmax(ext));plane=[a for a in range(3) if a!=up];scale=float(max(ext))
 poses=[]
 for d in [0,90,180,270]:
  direct=math.cos(math.radians(d))*axis[plane[0]]+math.sin(math.radians(d))*axis[plane[1]]
  poses.append(("azimuth_%03d"%d,direct,axis[up]))
 poses += [("oblique",(axis[plane[0]]+axis[plane[1]]+axis[up])/math.sqrt(3),axis[up]),
           ("top",axis[up],axis[plane[0]]),("bottom",-axis[up],axis[plane[0]])]
 shots=[];data=[];bg=np.array([227,230,232],dtype=np.int16)
 for name,dir,upvec in poses:
  cam=ren.GetActiveCamera();cam.ParallelProjectionOn()
  cam.SetPosition(*(center+dir*3.5*scale));cam.SetFocalPoint(*center)
  cam.SetViewUp(*upvec);cam.SetParallelScale(scale*.71);ren.ResetCameraClippingRange();win.Render()
  filt=vtk.vtkWindowToImageFilter();filt.SetInput(win);filt.Update()
  p=OUT/("run232_TRUE3D_%s_NOT_APPROVED.png"%name)
  writer=vtk.vtkPNGWriter();writer.SetFileName(str(p));writer.SetInputConnection(filt.GetOutputPort());writer.Write()
  px=np.asarray(Image.open(p).convert("RGB"),dtype=np.int16)
  fg=int(np.max(np.abs(px-bg),axis=2).astype(np.int16).clip(0,255).__gt__(26).sum())
  unique=int(len(np.unique(px.reshape(-1,3),axis=0)))
  if fg<700 or fg>158760 or unique<64:raise RuntimeError("BLANK_CAMERA_"+name)
  shots.append(p);data.append({"view":name,"foreground":fg,"unique_colors":unique,"file":digest(p)})
 if len(set(digest(p)["sha256"] for p in shots))<5:raise RuntimeError("DUPLICATE_CAMERA_HASHES")
 sheet=Image.new("RGB",(1120,640),(243,243,243));pen=ImageDraw.Draw(sheet)
 for i,p in enumerate(shots):
  x=i%4*280;y=i//4*320;pen.text((x+5,y+5),p.stem[-33:],fill=(30,30,30))
  sheet.paste(Image.open(p).convert("RGB").resize((268,268)),(x+5,y+28))
 dst=OUT/"run232_NATIVE_SEVEN_VIEWS_ART_UNAPPROVED.png";sheet.save(dst)
 R["views"]=data;R["contact_sheet"]=digest(dst);win.Finalize()
try:
 R["reference"]=digest(SRC)
 if R["reference"]["sha256"]!=SHA:raise RuntimeError("V3_REF_SHA_MISMATCH")
 native=find_owl(fetch_free());meshes=verify_model(native);views(meshes)
 R["status"]="TRUE_3D_NATIVE_WITH_7_VIEW_TECH_PASS_ART_UNREVIEWED_NO_RELEASE"
except BaseException as ex:
 R["status"]="NO_NEW_QUALIFIED_NATIVE_OWL_NO_RELEASE"
 R["error"]=repr(ex);R["traceback"]=traceback.format_exc()[-4000:]
finally:
 R["files"]={p.name:digest(p) for p in OUT.iterdir() if p.is_file() and p.name!="run232_machine_report.json"}
 (OUT/"run232_machine_report.json").write_text(json.dumps(R,ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({"status":R["status"],"error":R.get("error"),
   "native":R.get("native"),"geometry":R.get("geometry"),"views":len(R.get("views",[]))},
   ensure_ascii=False),flush=True)
