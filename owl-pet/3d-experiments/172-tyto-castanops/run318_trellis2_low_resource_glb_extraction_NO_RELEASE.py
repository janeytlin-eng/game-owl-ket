#!/usr/bin/env python3
"""Run318: one real anonymous Microsoft TRELLIS.2 UI generation and lower-cost GLB export.
NOT a finished pet. No use of private API, hidden file enumeration, paid credentials,
captcha bypass, guessed CDN paths or output fabricated from the original photo.
Hypothesis: Run316 Extract GLB failed with default 300k faces / 2048 texture /
1024 resolution; 512 generation / 100k face / 1024 texture might complete.
"""
from pathlib import Path
import hashlib, json, re, time, traceback
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

ROOT=Path("owl172-run318-evidence"); ROOT.mkdir(exist_ok=True)
SOURCE=Path("owl172-run295-evidence/young-REAL-PHOTO-PIXELS-transparent-input-NO_3D.png")
WHITE=Path("owl172-run295-evidence/young-isolated-white-background-input-NO_3D.png")
EXPECTED_WHITE="6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77"
TARGET_URL="https://microsoft-trellis-2.hf.space/"
def sha(b):return hashlib.sha256(b).hexdigest()
report={
 "experiment":"run318","target":"#172 Tyto castanops v3 concept rightmost unknown-age second-down chick",
 "hypothesis":"lower public UI model resolution 512 and export target 100000 faces/1024 texture may avoid Run316 GLB export error",
 "start_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
 "provider":TARGET_URL,"expected_input_white_sha256":EXPECTED_WHITE,
 "ui_generation_resolution":"512","ui_export_face_target":100000,"ui_export_texture_size":1024,
 "generation_clicked":False,"extraction_clicked":False,"valid_native_glb":False,
 "art_approved":False,"rights_cleared":False,"real_phone_tested":False,
 "payment_usd":0,"release":False,"status":"INITIAL","observations":[]
}
events=[]
def persist():
 (ROOT/"run318_result.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 (ROOT/"network_public_artifact_observations.json").write_text(json.dumps(events[-150:],ensure_ascii=False,indent=2)+"\n")
def snap(page,name):
 try:
  page.screenshot(path=str(ROOT/name),timeout=18000)
  return name
 except Exception as e:return "screenshot_failure: "+str(e)[:190]
def text(page):
 try:return page.locator("body").inner_text(timeout=4000)[-3500:]
 except Exception:return "BODY_NOT_READABLE"
def controls(page):
 return page.evaluate("""() => ({
  range:[...document.querySelectorAll('input[type=range]')].map((e,i)=>({index:i,value:e.value,min:e.min,max:e.max,step:e.step,near:e.parentElement?.parentElement?.textContent?.trim()?.slice(0,100)})),
  radios:[...document.querySelectorAll('input[type=radio]')].map(e=>({value:e.value,checked:e.checked,outer:e.outerHTML.slice(0,200)})),
  buttons:[...document.querySelectorAll('button')].filter(e=>e.offsetParent!==null).map(e=>({label:(e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,90),disabled:e.disabled})).slice(0,60)
 })""")
def set_range(page,lo,hi,value):
 vals=page.locator('input[type=range]')
 ix=[]
 for i in range(vals.count()):
  e=vals.nth(i)
  bounds=e.evaluate("(x)=>[Number(x.min),Number(x.max)]")
  if bounds==[lo,hi]:ix.append(i)
 if len(ix)!=1: raise RuntimeError("UNIQUE_RANGE_INPUT_NOT_FOUND "+str((lo,hi,ix)))
 vals.nth(ix[0]).evaluate("""(e,value)=>{
    const s=Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set;
    s.call(e,String(value));e.dispatchEvent(new Event('input',{bubbles:true}));
    e.dispatchEvent(new Event('change',{bubbles:true}));
 }""",value)
 page.wait_for_timeout(900)
 actual=vals.nth(ix[0]).input_value()
 if str(actual)!=str(value):raise RuntimeError("RANGE_SET_VERIFICATION_FAILED "+str((lo,hi,actual)))
 return ix[0]
def observed_source_urls(page):
 # Only DOM-visible download buttons or network-observed GLBs of this actual generation.
 try:
  return page.evaluate("""() => [...document.querySelectorAll('a[href],model-viewer[src],gradio-model3d')]
   .map(e=>({tag:e.tagName,url:e.href||e.src||'',visible:!!e.getClientRects().length,
              label:(e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,90)}))
   .filter(x=>x.url&&(x.url.includes('.glb')||x.url.includes('/file='))).slice(0,25)""")
 except Exception:return []
def try_actual_observed_glb(page):
 sources=[{"url":e["url"],"how":"browser_response","status":e["status"]} for e in events
           if e.get("url") and e.get("status")==200 and re.search(r'\.glb(?:\?|$)',e["url"],re.I)]
 sources+= [{"url":x["url"],"how":"DOM","status":None} for x in observed_source_urls(page)]
 seen=set()
 for item in sources:
  url=item["url"]
  if url in seen:continue
  seen.add(url)
  if not (url.startswith("https://") and urlparse(url).hostname in {"microsoft-trellis-2.hf.space","huggingface.co"}):continue
  try:
   rsp=page.request.get(url,timeout=40000)
   binary=rsp.body()
   if rsp.status!=200 or binary[:4]!=b"glTF" or not (2000<len(binary)<100_000_000):continue
   import trimesh
   model=ROOT/"trellis2-low-memory-UNREVIEWED-NO_RELEASE.glb"
   model.write_bytes(binary)
   scene=trimesh.load(str(model),force="scene",process=False)
   faces=sum(len(g.faces) for g in scene.geometry.values())
   if faces<1500:
    model.unlink(missing_ok=True);continue
   report["glb"]={"file":model.name,"sha256":sha(binary),"bytes":len(binary),
                  "geometry_count":len(scene.geometry),"faces":faces,"source":item["how"]}
   report["valid_native_glb"]=True;report["status"]="TRUE_NATIVE_GLB_ACQUIRED_UNREVIEWED"
   return True
  except Exception as e:report.setdefault("artifact_errors",[]).append(repr(e)[:220])
 return False
assert SOURCE.is_file() and WHITE.is_file()
assert sha(WHITE.read_bytes())==EXPECTED_WHITE
report["transparent_reference_sha256"]=sha(SOURCE.read_bytes())
persist()
try:
 with sync_playwright() as pw:
  browser=pw.chromium.launch(headless=True,args=["--no-sandbox","--disable-dev-shm-usage",
                         "--enable-unsafe-swiftshader","--use-gl=angle","--use-angle=swiftshader"])
  page=browser.new_page(viewport={"width":1320,"height":900},accept_downloads=True)
  def onresponse(r):
   try:
    u=r.url; t=r.headers.get("content-type","")
    if re.search(r'\.glb(?:\?|$)|/queue/|/file=|/upload',u,re.I):
     if len(events)<200:events.append({"url":u[:350],"status":r.status,"content_type":t[:100]})
   except Exception:pass
  page.on("response",onresponse)
  try:
   first=page.goto(TARGET_URL,wait_until="domcontentloaded",timeout=70000)
   report["first_http"]=first.status if first else None
   page.wait_for_timeout(4500)
   report["initial_screenshot"]=snap(page,"initial_ui.png")
   report["initial_controls"]=controls(page)
   if report["first_http"]!=200:raise RuntimeError("SITE_NOT_HTTP_200")
   if page.locator("input[type=file]").count()<1:raise RuntimeError("NO_PUBLIC_UPLOAD")
   # Set UI controls BEFORE uploading/clicking; never access provider backend directly.
   report["resolution_select_method"]="unselected"
   radio=page.get_by_role("radio",name=re.compile(r'^512$'))
   if radio.count():
    radio.first.check(force=True,timeout=6000);report["resolution_select_method"]="radio_check"
   else:
    page.get_by_text("512",exact=True).first.click(timeout=6000)
    report["resolution_select_method"]="visible_label_click"
   report["decimation_range_index"]=set_range(page,100000,500000,100000)
   report["texture_range_index"]=set_range(page,1024,4096,1024)
   report["configured_controls"]=controls(page)
   if report["configured_controls"]["range"][report["decimation_range_index"]]["value"]!="100000":
    raise RuntimeError("DECIMATION_UI_WAS_NOT_CONFIGURED")
   report["configured_screenshot"]=snap(page,"ui_512_100k_1024.png")
   page.locator("input[type=file]").first.set_input_files(str(SOURCE.resolve()),timeout=15000)
   page.wait_for_timeout(8000)
   report["upload_text"]=text(page)[-1300:]
   report["upload_screenshot"]=snap(page,"actual_upload.png")
   if re.search(r'sign in to upload|log in to upload|upload failed',report["upload_text"],re.I):
    raise RuntimeError("ACCOUNT_REQUIRED_TO_UPLOAD")
   btn=page.get_by_role("button",name=re.compile(r'^Generate$',re.I))
   if not btn.count() or not btn.first.is_enabled():raise RuntimeError("GENERATE_NOT_ENABLED")
   btn.first.click(timeout=15000);report["generation_clicked"]=True
   report["generation_started_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
   report["status"]="GENERATION_REQUESTED"
   started=time.monotonic()
   while time.monotonic()-started<245:
    page.wait_for_timeout(9000)
    preview_count=page.locator(".previewer-main-image").count()
    body=text(page)
    report["observations"].append({"seconds":round(time.monotonic()-started),
       "preview_images":preview_count,"text":re.sub(r'\s+',' ',body)[-600:]})
    if preview_count>=8:
     report["preview_images"]=preview_count
     report["preview_screenshot"]=snap(page,"real_multiview_preview.png")
     report["status"]="ACTUAL_NEURAL_PREVIEW_GENERATED"
     break
    if re.search(r'GPU quota|not enough gpu|out of memory|an error occurred|error while generating',body,re.I):
     report["status"]="GENERATION_ERROR_VISIBLE";break
   if report["status"]=="ACTUAL_NEURAL_PREVIEW_GENERATED":
    ext=page.get_by_role("button",name=re.compile("Extract GLB",re.I))
    if ext.count() and ext.first.is_enabled():
     ext.first.click(timeout=15000);report["extraction_clicked"]=True
     report["extract_started_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
     report["status"]="LOW_RESOURCE_EXTRACTION_CLICKED"
     start2=time.monotonic()
     while time.monotonic()-start2<165:
      page.wait_for_timeout(8500)
      if try_actual_observed_glb(page):break
      body=text(page)
      report["extract_samples"]=report.get("extract_samples",[])[-18:]+[
       {"seconds":round(time.monotonic()-start2),"text":re.sub(r'\s+',' ',body)[-700:],
        "observed_urls":len(observed_source_urls(page))}]
      if re.search(r'^Error$|error while|CUDA out of memory|quota exceeded',body,re.I):
       report["extract_error_visible"]=True
     if not report["valid_native_glb"]:
      report["status"]="LOW_RESOURCE_EXTRACTION_NO_GLB"
    else:report["status"]="GENERATED_PREVIEW_BUT_EXTRACT_BUTTON_DISABLED"
   report["final_dom_links"]=observed_source_urls(page)
   report["final_ui_text"]=text(page)[-2200:]
   report["final_screenshot"]=snap(page,"final_ui.png")
  finally:
   persist();page.close();browser.close()
except Exception as e:
 report["error"]=repr(e)
 report["traceback"]=traceback.format_exc()[-1900:]
 if report["status"] not in ("LOW_RESOURCE_EXTRACTION_NO_GLB",):
  report["status"]="BROWSER_OR_PUBLIC_UI_ERROR"
finally:
 report["finish_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
 (ROOT/"STRICT_NO_RELEASE.txt").write_text(
  "Run318 real official public UI low-resource extraction test. Do not release. "
  "No claim of art approval, true down feathers, correct feet, rights or physical phone QA.\n")
 persist()
 print(json.dumps({"status":report["status"],"generation_clicked":report["generation_clicked"],
  "extraction_clicked":report["extraction_clicked"],"glb":report.get("glb"),
  "error":report.get("error"),"observations":report["observations"][-3:]},ensure_ascii=False,indent=2))
