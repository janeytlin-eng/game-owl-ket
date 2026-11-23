#!/usr/bin/env python3
"""Run325: actual public free textured image-to-native-3D tests, no pay / no CAPTCHA bypass.
Provenance gates require a successful intended #172 chick form submission, a NEW
post-submit GLB, real substantial mesh, and embedded texture/UV evidence.
Not a release or scientific validation. Never confuse site demo assets with results.
"""
from pathlib import Path
import base64, hashlib, json, re, time, traceback
from urllib.parse import urlsplit, urlunsplit
import trimesh
from playwright.sync_api import sync_playwright

INPUT=Path("owl172-run295-evidence/young-REAL-PHOTO-PIXELS-transparent-input-NO_3D.png")
WHITE=Path("owl172-run295-evidence/young-isolated-white-background-input-NO_3D.png")
CHECK="6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77"
OUT=Path("owl172-run325-evidence"); OUT.mkdir(exist_ok=True)
SITES=[
 ("hi3d_pro_pbr","https://hi3d.pro/en",r"Generate|Create 3D",130),
 ("hunyuan3d_dev_textured","https://hunyuan3d.dev/en",r"Generate|Create 3D",130),
]
R={"run":325,"target":"#172 v3 rightmost cream downy age-unknown mesoptile",
  "providers":[],"real_generated_models":[],"paid_usd":0,"account_created":False,
  "captcha_bypassed":False,"art_approved":False,"phone_tested":False,
  "rights_cleared":False,"release":False,"status":"IN_PROGRESS"}
def sha(b):return hashlib.sha256(b).hexdigest()
def persist():
 (OUT/"actual_run325.json").write_text(json.dumps(R,indent=2,ensure_ascii=False)+"\n")
def cleanurl(u):
 try:
  x=urlsplit(u);return urlunsplit((x.scheme,x.netloc,x.path,"",""))[:210]
 except Exception:return "bad-url"
def shot(page,fn):
 try:page.screenshot(path=str(OUT/fn),full_page=False,timeout=16000);return fn
 except Exception as e:return "screenshot_error:"+str(e)[:100]
def txt(page):
 try:return page.locator("body").inner_text(timeout=4500)[:6500]
 except Exception:return ""
def blocked(page,t):
 return bool(re.search(r"insufficient credits|out of credits|no credits|payment required|buy credits|subscribe to generate|sign in required|please log in|verification required|verify you are human|checking your browser|access denied",t,re.I)) or page.locator('iframe[src*="challenges.cloudflare.com"]').count()>0
def actual_glb(data,p,origin):
 if len(data)<5000 or len(data)>80_000_000 or data[:4]!=b"glTF":return False
 try:
  tmp=OUT/(p["site"]+"_actual_target_candidate_NO_RELEASE.glb");tmp.write_bytes(data)
  sc=trimesh.load(tmp,force="scene",process=False)
  triangles=int(sum(len(g.faces) for g in sc.geometry.values()))
  if triangles<2500:raise RuntimeError("insufficient native triangles")
  meshes=len(sc.geometry)
  # GLB header and JSON chunk; inspect embedded images without inventing texture success.
  chunklen=int.from_bytes(data[12:16],"little")
  gltf=json.loads(data[20:20+chunklen])
  nimg=len(gltf.get("images",[]));ntex=len(gltf.get("textures",[]))
  nmats=len(gltf.get("materials",[]))
  model={"bytes":len(data),"sha256":sha(data),"file":tmp.name,"triangles":triangles,
         "meshes":meshes,"image_count":nimg,"texture_count":ntex,"materials":nmats,
         "origin":origin,"source":"rightmost #172 target submitted from original"}
  p["native"]=model;R["real_generated_models"].append(model)
  return True
 except Exception as e:
  p.setdefault("rejected_binary",[]).append(str(e)[:230]);return False
def page_refs(page):
 try:return page.evaluate("""()=>[...document.querySelectorAll('model-viewer[src],a[href],source[src]')]
  .map(e=>({url:e.src||e.href||"",label:(e.innerText||e.getAttribute('download')||"").slice(0,90)}))
  .filter(e=>/^(blob:|data:|https?:)/.test(e.url) && (/\\.glb(?:[?#]|$)|blob:|gltf-binary|download/i.test(e.url+e.label)))
  .slice(0,30)""")
 except Exception:return []
def inspect_form(page):
 return page.evaluate("""()=>({
   buttons:[...document.querySelectorAll('button')].filter(e=>e.getBoundingClientRect().width>0).slice(0,65)
     .map(e=>({name:(e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,100),
                enabled:!e.disabled})),
   uploads:[...document.querySelectorAll('input[type=file]')].map(e=>({
     files:e.files?.length||0,accept:e.accept||'',hidden:e.getBoundingClientRect().width===0})),
   canvases:document.querySelectorAll('canvas').length,
   viewerSources:[...document.querySelectorAll('model-viewer[src]')].map(e=>e.src).slice(0,10),
   challengeIframes:document.querySelectorAll('iframe[src*="challenges.cloudflare.com"]').length
 })""")
def probe(browser,name,url,button,limit):
 p={"site":name,"url":url,"started_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
    "status":"NOT_STARTED","native":None,"generation_clicked":False,
    "samples":[],"requests":[],"received_glb_urls":[],"spent_usd":0}
 R["providers"].append(p);persist()
 page=browser.new_page(viewport={"width":1280,"height":900},accept_downloads=True)
 baseline=set();seen=set();downloads=[]
 def response(resp):
  try:
   u=resp.url;typ=resp.headers.get("content-type","").lower()
   is_glb=bool(re.search(r"\.glb(?:[?#]|$)",u,re.I) or "model/gltf" in typ)
   if not (is_glb or "generate" in u.lower() or "api/" in u.lower()):return
   if len(p["requests"])<55:
    p["requests"].append({"url":cleanurl(u),"http":resp.status,"mime":typ[:100]})
   if is_glb and resp.status==200 and p["generation_clicked"] and not p["native"]:
    if u not in baseline and not re.search(r"demo|sample|robotexpressive",u,re.I):
     p["received_glb_urls"].append(cleanurl(u))
     try:actual_glb(resp.body(),p,"post-submit browser GLB response")
     except Exception as e:p.setdefault("response_read_errors",[]).append(str(e)[:150])
  except Exception:pass
 def download(d):
  if not p["generation_clicked"]:return
  try:
   f=OUT/(name+"_actual_download_NO_RELEASE.glb")
   d.save_as(f);downloads.append({"suggested_filename":d.suggested_filename,"bytes":f.stat().st_size})
   actual_glb(f.read_bytes(),p,"visible browser download following generation")
  except Exception as e:downloads.append({"error":str(e)[:200]})
 page.on("response",response);page.on("download",download)
 try:
  start=page.goto(url,wait_until="domcontentloaded",timeout=62000)
  p["initial_http"]=start.status if start else None
  page.wait_for_timeout(4000)
  p["initial_text"]=txt(page)[:2200]
  p["initial_screenshot"]=shot(page,name+"_01_home.png")
  if p["initial_http"]!=200:
   p["status"]="HTTP_ERROR_NO_GENERATION";return
  if blocked(page,p["initial_text"]):
   p["status"]="PUBLIC_VERIFICATION_OR_LOGIN_GATE_NO_BYPASS";return
  initial=page_refs(page)
  baseline={x["url"] for x in initial}
  p["initial_demo_refs"]=[cleanurl(x["url"]) for x in initial[:8]]
  inputs=page.locator("input[type=file]")
  if not inputs.count():
   p["status"]="NO_REAL_IMAGE_UPLOAD_CONTROL";return
  # Browser's actual upload control, not an undocumented API endpoint.
  inputs.first.set_input_files(str(INPUT.resolve()),timeout=12000)
  page.wait_for_timeout(4500)
  p["upload_form"]=inspect_form(page)
  p["after_upload_screenshot"]=shot(page,name+"_02_upload.png")
  p["after_upload_text"]=txt(page)[:1800]
  if blocked(page,p["after_upload_text"]):
   p["status"]="UPLOAD_LOGIN_OR_CAPTCHA_GATE";return
  # Reject spurious hidden input mutation with no accepted form preview.
  state=p["upload_form"]
  has_new_preview=any(x["url"] not in baseline and x["url"].startswith("blob:") for x in page_refs(page))
  if not has_new_preview and not re.search(r"uploaded|remove image|change image|image selected|preview|\\.png",p["after_upload_text"],re.I):
   p["upload_preview_evidence"]="INCONCLUSIVE; file input set but no visible acceptance proof"
  else:p["upload_preview_evidence"]="VISIBLE_PREVIEW_OR_TEXT_POSSIBLE"
  buttons=page.get_by_role("button")
  selected=None
  for i in range(min(buttons.count(),90)):
   b=buttons.nth(i)
   try:
    if not b.is_visible(timeout=400) or not b.is_enabled(timeout=400):continue
    label=(b.inner_text(timeout=500) or b.get_attribute("aria-label") or "").strip()
    if re.search(button,label,re.I) and not re.search(r"premium|subscribe|pay|upgrade|credit pack|buy now",label,re.I):
     selected=b;p["generation_button"]=label[:100];break
   except Exception:continue
  if selected is None:p["status"]="NO_FREE_ENABLED_GENERATION_CONTROL";return
  selected.click(timeout=12000)
  p["generation_clicked"]=True;p["status"]="GENERATE_CLICKED";persist()
  shot(page,name+"_03_start.png")
  t=time.monotonic()
  while time.monotonic()-t<limit and not p["native"]:
   page.wait_for_timeout(5500)
   body=txt(page)
   elapsed=round(time.monotonic()-t,1)
   if len(p["samples"])<27:
    p["samples"].append({"elapsed_s":elapsed,"body":re.sub(r"\s+"," ",body)[:380]})
   if blocked(page,body):
    p["status"]="QUOTA_LOGIN_OR_CAPTCHA_BLOCK_NO_BYPASS";break
   if re.search(r"generation failed|unexpected error|server error|GPU unavailable",body,re.I):
    p["status"]="REMOTE_GENERATION_FAILED";break
   for q in page_refs(page):
    u=q["url"]
    if u in seen or u in baseline or re.search(r"demo|sample|robotexpressive",u,re.I):continue
    seen.add(u)
    if not (u.startswith("blob:") or u.startswith("data:") or re.search(r"\.glb(?:[?#]|$)",u,re.I)):continue
    try:
     if u.startswith("blob:") or u.startswith("data:"):
      result=page.evaluate("""async u=>{
        const x=await (await fetch(u)).arrayBuffer();if(x.byteLength>80000000)return null;
        let s='';const b=new Uint8Array(x);
        for(let i=0;i<b.length;i+=4096)s+=String.fromCharCode(...b.subarray(i,i+4096));
        return btoa(s);
      }""",u)
      if result:actual_glb(base64.b64decode(result),p,"new visible model-viewer/blob")
     elif u.startswith("https://") or u.startswith("http://"):
      resp=page.request.get(u,timeout=18000)
      if resp.status==200:actual_glb(resp.body(),p,"new public visible GLB link")
    except Exception as e:p.setdefault("public_asset_errors",[]).append(str(e)[:140])
   # User-visible download only; do not click upsell/trial/purchase.
   if re.search(r"download|ready|complete",body,re.I):
    dl=page.get_by_role("button",name=re.compile("Download (GLB|model|3D)",re.I))
    if dl.count() and not p.get("download_click"):
     try:dl.first.click(timeout=2800);p["download_click"]=True
     except Exception:pass
  p["final_screenshot"]=shot(page,name+"_04_result.png")
  p["final_text"]=txt(page)[-2500:]
  p["final_dom"]=inspect_form(page)
  if p["native"]:
   p["status"]="REAL_NATIVE_GLb_OBTAINED_UNREVIEWED"
  elif p["status"]=="GENERATE_CLICKED":
   p["status"]="NO_NEW_MODEL_IN_OBSERVED_FREE_WINDOW"
 except Exception as e:
  p["error"]=str(e)[:600]
  p["traceback"]=traceback.format_exc()[-1300:]
  p["status"]="BROWSER_OR_UI_EXCEPTION_NO_RELEASE"
  shot(page,name+"_error.png")
 finally:
  p["downloads"]=downloads
  p["finished_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
  page.close();persist()

if __name__=="__main__":
 assert INPUT.exists() and WHITE.exists(),"Run295 source crop missing"
 assert sha(WHITE.read_bytes())==CHECK,"RIGHT chick reference SHA mismatch"
 R["source_transparent_sha"]=sha(INPUT.read_bytes())
 R["source_white_sha"]=sha(WHITE.read_bytes())
 persist()
 with sync_playwright() as pl:
  browser=pl.chromium.launch(headless=True,args=["--no-sandbox","--disable-dev-shm-usage",
    "--enable-webgl","--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
  try:
   for site in SITES:
    probe(browser,*site)
    if R["real_generated_models"]:break
  finally:browser.close()
 R["status"]="NATIVE_UNREVIEWED_ART_GATE_REQUIRED" if R["real_generated_models"] else "NO_PROVEN_NEW_NATIVE_MODEL_NO_RELEASE"
 (OUT/"STRICT_NO_RELEASE.txt").write_text("Actual Run325 free UI experiment only. No art approval, no commercial rights, no real phone QA, no main/251 edits. NO_RELEASE.\n")
 persist()
 print(json.dumps({"status":R["status"],"providers":[{"site":p["site"],"status":p["status"],"model":p["native"]} for p in R["providers"]]},indent=2))
