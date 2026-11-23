#!/usr/bin/env python3
"""Run324: diagnose an ACTUAL free Hy3D result visible on Run323b page but no GLB URL.
One legitimate image upload and public Generate click. Capture only normal browser
responses and explicit public UI downloads or model-viewer blob src. No hidden
endpoint, no credential, CAPTCHA bypass, payment, or product art approval.
"""
from __future__ import annotations
from playwright.sync_api import sync_playwright
from pathlib import Path
from urllib.parse import urlsplit,urlunsplit
import time,json,hashlib,base64,re,traceback
import trimesh

SRC=Path("owl172-run295-evidence/young-REAL-PHOTO-PIXELS-transparent-input-NO_3D.png")
WHITE=Path("owl172-run295-evidence/young-isolated-white-background-input-NO_3D.png")
EXPECTED="6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77"
OUT=Path("owl172-run324-evidence");OUT.mkdir(exist_ok=True)
URL="https://hy3d.dev/"
R={"run":324,"service":URL,"target":"#172 rightmost original age-unknown cream Tyto castanops v3 chick",
  "source_white_sha256":EXPECTED,"extra_payment_usd":0,"bypassed_captcha":False,
  "real_native_glb":None,"art_approved":False,"rights_cleared":False,
  "phone_tested":False,"release":False,"status":"NOT_STARTED","checks":[]}
events=[];downloads=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def save(): (OUT/"actual_run324.json").write_text(json.dumps(R,ensure_ascii=False,indent=2)+"\n")
def safeurl(u):
 try:
  x=urlsplit(u)
  return urlunsplit((x.scheme,x.netloc,x.path,"",""))[:230]
 except Exception:return "invalid-url"
def shot(page,fn):
 try:page.screenshot(path=str(OUT/fn),full_page=False,timeout=15000);return fn
 except Exception as exc:return "snapshot-failed: "+str(exc)[:200]
def body(page):
 try:return page.locator("body").inner_text(timeout=4000)[:9000]
 except Exception:return ""
def inspect_dom(page):
 return page.evaluate("""() => {
  const items=[...document.querySelectorAll('model-viewer,canvas,iframe,a[href],button,[download],video,img')]
    .filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0;})
    .slice(0,125).map(e=>{
      const r=e.getBoundingClientRect();
      return {tag:e.tagName,src:(e.currentSrc||e.src||e.getAttribute('src')||'').slice(0,230),
       href:(e.href||e.getAttribute('href')||'').slice(0,230),
       text:(e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,90),
       w:Math.round(r.width),h:Math.round(r.height)}
    });
  return {items,canvases:document.querySelectorAll('canvas').length,
    modelViewers:document.querySelectorAll('model-viewer').length,
    visibleButtons:[...document.querySelectorAll('button')].filter(e=>e.getBoundingClientRect().width>0)
      .map(e=>({text:(e.innerText||'').trim().slice(0,95),enabled:!e.disabled})).slice(0,45)};
 }""")
def verify(blob,where):
 if not blob or len(blob)<2000 or len(blob)>80_000_000 or blob[:4]!=b"glTF":return False
 name="hy3d_native_actual_UNREVIEWED_NO_RELEASE.glb"
 out=OUT/name;out.write_bytes(blob)
 try:
  scene=trimesh.load(out,force="scene",process=False)
  tris=sum(len(g.faces) for g in scene.geometry.values())
  if tris<2000:raise RuntimeError("not substantial native 3D mesh")
  R["real_native_glb"]={"name":name,"bytes":len(blob),"sha256":sha(blob),
    "triangles":int(tris),"meshes":len(scene.geometry),"from_public_visible_ui":where}
  return True
 except Exception as exc:
  R.setdefault("native_errors",[]).append(repr(exc)[:300])
  out.unlink(missing_ok=True);return False
def onresponse(response):
 try:
  url=response.url;ctype=response.headers.get("content-type","")
  if not any(k in (url+" "+ctype).lower() for k in (".glb","gltf","application/octet-stream","api/","generate","result","task","status")):return
  entry={"path":safeurl(url),"http":response.status,"mime":ctype[:120],
    "declared_size":response.headers.get("content-length","")[:24]}
  events.append(entry)
  if response.status==200 and (".glb" in url.lower() or "model/gltf" in ctype.lower()
      or "application/octet-stream" in ctype.lower()):
   try:
    b=response.body()
    entry["actual_bytes"]=len(b)
    if verify(b,"ACTUAL_VISIBLE_RESULT_BROWSER_NETWORK"):R["status"]="REAL_GLb_FROM_NETWORK"
   except Exception as e:entry["binary_capture_error"]=str(e)[:150]
  # A publicly received app response is allowed to be inspected; do not request unseen API endpoints.
  if response.status==200 and "application/json" in ctype.lower() and len(events)<45:
   try:
    data=response.json()
    if isinstance(data,dict):
     entry["json_keys"]=sorted(data.keys())[:45]
     # Never archive tokens or private request details. Only printable public asset fields.
     for k in ["download_url","glb_url","model_url","file_url","status","state","error","message"]:
      if k in data and (isinstance(data[k],str) or data[k] is None):
       entry[k]=(safeurl(data[k]) if k.endswith("url") and data[k] else str(data[k])[:200])
   except Exception:pass
 except Exception as exc:
  if len(events)<60:events.append({"handler_error":repr(exc)[:200]})
def model_dom_glb(page):
 """Only source referenced by actually rendered public 3D viewer, never a guessed API."""
 try:
  urls=page.evaluate("""() => [...document.querySelectorAll('model-viewer,[src]')]
    .map(e=>e.src||e.getAttribute('src')||'')
    .filter(v=>/^(blob:|data:|https?:)/.test(v) && (v.startsWith('blob:') || v.startsWith('data:') || /\.glb(?:$|[?#])/.test(v)))
    .slice(0,12)""")
 except Exception as exc:
  R.setdefault("dom_extract_errors",[]).append(str(exc)[:200]);return False
 R["public_model_viewer_sources"]=[x[:160] if not x.startswith("data:") else "data URL (size hidden)" for x in urls]
 for url in urls:
  try:
   if url.startswith("blob:") or url.startswith("data:"):
    result=page.evaluate("""async url => {
      const r=await fetch(url);const b=await r.arrayBuffer();
      if(b.byteLength>80000000||b.byteLength<1000)return {tooBigOrSmall:b.byteLength};
      let binary='';const x=new Uint8Array(b);
      for(let i=0;i<x.length;i+=4096) binary+=String.fromCharCode(...x.slice(i,i+4096));
      return {bytes:b.byteLength,b64:btoa(binary)};
    }""",url)
    if isinstance(result,dict) and "b64" in result:
     blob=base64.b64decode(result["b64"])
     if verify(blob,"VISIBLE_DOM_BLOB_OR_DATA_GLb"):return True
   elif url.startswith("https://") or url.startswith("http://"):
    rsp=page.request.get(url,timeout=20000)
    if rsp.status==200 and verify(rsp.body(),"VISIBLE_MODEL_VIEWER_SRC_HTTP"):return True
  except Exception as exc:R.setdefault("dom_extract_errors",[]).append(str(exc)[:250])
 return False

if __name__=="__main__":
 assert SRC.exists() and WHITE.exists() and sha(WHITE.read_bytes())==EXPECTED,"Original #172 reference mismatch"
 R["source_transparent_sha256"]=sha(SRC.read_bytes());save()
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,args=["--no-sandbox","--disable-dev-shm-usage",
   "--enable-webgl","--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
  page=browser.new_page(viewport={"width":1280,"height":900},accept_downloads=True)
  page.on("response",onresponse)
  def downloaded(download):
   try:
    path=OUT/"actual_public_button_download_UNREVIEWED.glb"
    download.save_as(str(path));downloads.append({"name":download.suggested_filename,
      "bytes":path.stat().st_size})
    if verify(path.read_bytes(),"VISIBLE_DOWNLOAD_GLb_BUTTON"):R["status"]="REAL_GLB_FROM_BUTTON"
   except Exception as exc:downloads.append({"error":str(exc)[:200]})
  page.on("download",downloaded)
  try:
   resp=page.goto(URL,wait_until="domcontentloaded",timeout=65000)
   R["initial_http"]=resp.status if resp else None
   page.wait_for_timeout(4000)
   R["first_screenshot"]=shot(page,"hy3d_initial.png")
   if R["initial_http"]!=200:raise RuntimeError("PUBLIC_SITE_NOT_HTTP200")
   if re.search(r"cloudflare|performing security verification|captcha",body(page),re.I):
    R["status"]="VERIFICATION_NOT_BYPASSED"
   else:
    inp=page.locator("input[type=file]")
    if not inp.count():raise RuntimeError("NO_ACTUAL_UPLOAD_INPUT")
    inp.first.set_input_files(str(SRC.resolve()),timeout=13000)
    page.wait_for_timeout(6500)
    R["after_upload"]=shot(page,"hy3d_upload.png")
    btn=page.get_by_role("button",name=re.compile("GENERATE",re.I))
    if not btn.count() or not btn.first.is_enabled():raise RuntimeError("NO_ENABLED_GENERATE")
    btn.first.click(timeout=13000)
    R["generate_clicked"]=True;R["status"]="PUBLIC_GENERATION_CLICKED";save()
    watch=time.monotonic()
    while time.monotonic()-watch<155 and not R["real_native_glb"]:
     page.wait_for_timeout(6500)
     elapsed=round(time.monotonic()-watch,1)
     txt=body(page)
     if len(R["checks"])<27:
      R["checks"].append({"elapsed_s":elapsed,"slice":re.sub(r"\s+"," ",txt[:1000])[:530]})
     if elapsed>20 and elapsed%35<7:
      R["preview_screenshot"]=shot(page,"hy3d_during_preview.png")
     if model_dom_glb(page):break
     try:
      # User-visible model Download action only; do not touch any buy/upgrade/credit buttons.
      dl=page.get_by_role("button",name=re.compile(r"download\s*(GLB|3D model|model)",re.I))
      if dl.count() and dl.first.is_enabled(timeout=500):
       R["visible_download_button"]=True
       if not R.get("download_clicked"):
        dl.first.click(timeout=3000)
        R["download_clicked"]=True
        page.wait_for_timeout(2000)
     except Exception as exc:R.setdefault("download_click_error",[]).append(str(exc)[:150])
     if re.search(r"you have exceeded|no credits|quota exceeded|please pay|payment required|security verification",txt,re.I):
      R["status"]="QUOTA_OR_VERIFICATION_BLOCK";break
    R["final_text"]=body(page)[:8000]
    R["final_dom"]=inspect_dom(page)
    R["final_screenshot"]=shot(page,"hy3d_actual_final_result.png")
    if R["real_native_glb"]:R["status"]="REAL_NATIVE_GLb_OBTAINED_UNREVIEWED"
    elif R["status"]=="PUBLIC_GENERATION_CLICKED":R["status"]="VISIBLE_PREVIEW_BUT_NO_EXPORTED_NATIVE_GLb"
  except Exception as exc:
   R["error"]=repr(exc)[:900]
   R["traceback"]=traceback.format_exc()[-1200:]
   if R["status"] not in ("QUOTA_OR_VERIFICATION_BLOCK",):R["status"]="EXPERIMENT_OR_REMOTE_ERROR"
   R["error_screenshot"]=shot(page,"hy3d_error.png")
  finally:
   R["downloads"]=downloads
   (OUT/"actual_ui_network_metadata.json").write_text(json.dumps(events,indent=2))
   R["network_relevant_events"]=len(events)
   save();page.close();browser.close()
 (OUT/"STRICT_NO_RELEASE.txt").write_text(
   "Run324 research only. Real GLB download is not juvenile-quality art approval.\n"
   "No payment or CAPTCHA bypass. Rights and physical-phone/WebGL still untested. NO_RELEASE.\n")
 print(json.dumps(R,ensure_ascii=False,indent=2))
