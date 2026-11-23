#!/usr/bin/env python3
"""Run317: real (not guessed) publicly served Stable Fast 3D GLB capture.
Only capture a GLB URL that was actually served to the browser's visible 3D model viewer.
No private API / login / payment. Artifact remains ART_NOT_APPROVED and NO_RELEASE.
"""
from pathlib import Path
import hashlib,json,time,traceback,re
from playwright.sync_api import sync_playwright
import trimesh

SOURCE=Path("owl172-run295-evidence/young-REAL-PHOTO-PIXELS-transparent-input-NO_3D.png")
WHITE=Path("owl172-run295-evidence/young-isolated-white-background-input-NO_3D.png")
EXPECTED="6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77"
OUT=Path("owl172-run317-evidence");OUT.mkdir(exist_ok=True)
URL="https://stabilityai-stable-fast-3d.hf.space/"
REPORT={"run":317,"target":"#172 Tyto castanops v3 rightmost cream age-unknown mesoptile",
        "service":URL,"status":"NOT_STARTED","genuine_glb":False,"glb":None,
        "art_approved":False,"rights_cleared":False,"phone_tested":False,
        "additional_payment_usd":0,"release":False}
network=[]
def sha(blob):return hashlib.sha256(blob).hexdigest()
def persist(): (OUT/"actual_run317.json").write_text(json.dumps(REPORT,indent=2,ensure_ascii=False)+"\n")
assert WHITE.is_file() and sha(WHITE.read_bytes())==EXPECTED
assert SOURCE.is_file()
REPORT["source_sha256"]=sha(SOURCE.read_bytes());persist()
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,args=["--no-sandbox","--disable-dev-shm-usage","--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
 page=b.new_page(viewport={"width":1280,"height":900},accept_downloads=True)
 def on_response(resp):
  try:
   u=resp.url
   if u.lower().split("?")[0].endswith(".glb"):
    network.append({"url":u,"status":resp.status,"mime":resp.headers.get("content-type","")})
  except Exception:pass
 page.on("response",on_response)
 try:
  resp=page.goto(URL,wait_until="domcontentloaded",timeout=75000)
  REPORT["http"]=resp.status if resp else None
  page.wait_for_timeout(4200)
  REPORT["first_screenshot"]="before_upload.png"
  page.screenshot(path=str(OUT/"before_upload.png"))
  if REPORT["http"]!=200: raise RuntimeError("HTTP_NOT_200")
  page.locator("input[type=file]").first.set_input_files(str(SOURCE.resolve()),timeout=12000)
  page.wait_for_timeout(7500)
  REPORT["upload_screenshot"]="upload.png"
  page.screenshot(path=str(OUT/"upload.png"))
  button=page.get_by_role("button",name=re.compile(r"^\s*Run\s*$",re.I))
  assert button.count() and button.first.is_enabled(), "NO_PUBLIC_RUN_BUTTON"
  button.first.click(timeout=10000)
  REPORT["run_clicked"]=True
  REPORT["run_at_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
  start=time.monotonic()
  while time.monotonic()-start<160:
   page.wait_for_timeout(6500)
   txt=page.locator("body").inner_text(timeout=5000)
   REPORT["last_text"]=txt[-1600:]
   if network and any(x["status"]==200 for x in network):break
  REPORT["observed_model_gets"]=network
  REPORT["scene_screenshot"]="actual_model_scene.png"
  page.screenshot(path=str(OUT/"actual_model_scene.png"))
  REPORT["public_DOM_model_sources"]=page.evaluate("""() => [...document.querySelectorAll('model-viewer,[src],[href]')]
     .map(e=>({tag:e.tagName,src:e.src||'',href:e.href||'',title:e.getAttribute('title')||'',aria:e.getAttribute('aria-label')||''}))
     .filter(x=>/\.glb(?:$|\?)/i.test(x.src+' '+x.href)).slice(0,15)""")
  # Public native GLB observed actually loaded by the visible 3D viewer.
  for seen in network:
   if seen["status"]!=200:continue
   try:
    response=page.request.get(seen["url"],timeout=60000)
    binary=response.body()
    REPORT.setdefault("download_checks",[]).append({"http":response.status,
             "bytes":len(binary),"content_type":response.headers.get("content-type","")})
    if response.status!=200 or binary[:4]!=b"glTF" or len(binary)<1000 or len(binary)>100_000_000:
     continue
    dest=OUT/"stability-SF3D-TyTo172-REAL_UNREVIEWED_NO_RELEASE.glb"
    dest.write_bytes(binary)
    scene=trimesh.load(dest,force="scene",process=False)
    tris=sum(len(g.faces) for g in scene.geometry.values())
    if tris<=1000:raise RuntimeError("INSUFFICIENT_GENUINE_NATIVE_TRIANGLES")
    REPORT["glb"]={"filename":dest.name,"bytes":len(binary),"sha256":sha(binary),
          "mesh_count":len(scene.geometry),"triangles":tris,"source":"PUBLIC_VISIBLE_BROWSER_MODEL_URL",
          "public_browser_source_url":seen["url"]}
    REPORT["genuine_glb"]=True;REPORT["status"]="NATIVE_GLB_ACQUIRED_UNREVIEWED";break
   except Exception as e:REPORT.setdefault("download_failures",[]).append(repr(e))
  if not REPORT["genuine_glb"]:REPORT["status"]="NO_NATIVE_GLB_FROM_BROWSER_DURING_CHECK"
  # Collect actual visible controls: useful if public 3D viewer uses a click-to-download.
  REPORT["visible_control_labels"]=page.evaluate("""() => [...document.querySelectorAll('button,a')]
     .filter(e=>e.offsetParent!==null).map(e=>({tag:e.tagName,text:(e.innerText||'').trim().slice(0,90),
       aria:e.getAttribute('aria-label'),title:e.getAttribute('title'),href:e.href||null})).slice(0,65)""")
 except Exception as e:
  REPORT["status"]="BROWSER_OR_MODEL_ERROR";REPORT["error"]=repr(e)
  REPORT["traceback"]=traceback.format_exc()[-1300:]
  try:page.screenshot(path=str(OUT/"failure.png"))
  except Exception:pass
 finally:
  REPORT["observed_model_gets"]=network
  (OUT/"observed_model_gets.json").write_text(json.dumps(network,indent=2)+"\n")
  persist();page.close();b.close()
(OUT/"NO_RELEASE.txt").write_text("Authentic native SF3D model may exist; visual art, short wing, natural face down, foot grip, rights, actual phone and softness NOT APPROVED. Do not deploy or market as finished pet.\n")
print(json.dumps(REPORT,indent=2,ensure_ascii=False))
