#!/usr/bin/env python3
"""#172 Run323: ordinary public no-payment browser UI tests of new image-to-native-GLB sites.
Research only. No scraping hidden APIs, no accounts, no price/credit purchase,
no CAPTCHA bypass. A successful download is not an art approval or product release.
"""
from __future__ import annotations
import hashlib, json, pathlib, re, time, traceback
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright
import trimesh

P = pathlib.Path("owl172-run295-evidence/young-REAL-PHOTO-PIXELS-transparent-input-NO_3D.png")
WHITE = pathlib.Path("owl172-run295-evidence/young-isolated-white-background-input-NO_3D.png")
O = pathlib.Path("owl172-run323-evidence"); O.mkdir(exist_ok=True)
EXPECTED_WHITE_SHA="6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77"
SITES=[
 {"id":"3dai_dev_geometry","url":"https://3dai.dev/en","button":r"Generate white 3D mesh","max_seconds":165,
  "intent":"Service shows texture unavailable; attempt genuinely enabled free white native mesh, not a finished owl"},
 {"id":"trellis2_dev","url":"https://trellis2.dev/","button":r"GENERATE","max_seconds":160,
  "intent":"Independent public no-signup Trellis2 textured GLB generator; not the earlier ZeroGPU official quota"},
 {"id":"hy3d_dev","url":"https://hy3d.dev/","button":r"GENERATE","max_seconds":150,
  "intent":"Independent no-login Hunyuan3D geometry-only GLB fallback, not a complete textured product"},
]
report={"run":"323b","started_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
 "goal":"#172 Tyto castanops v3 rightmost cream-white age-unknown mesoptile chick",
 "source_original":"owl-pet/design/concepts/172-tyto-castanops-v3.png",
 "paid_usd":0,"accounts_created":False,"captcha_bypassed":False,
 "art_approved":False,"rights_cleared":False,"real_phone_tested":False,
 "release":False,"native_glb":None,"providers":[]}
def sha(data):return hashlib.sha256(data).hexdigest()
def save(): (O/"actual_report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
def shot(page,tag,suffix):
 name=f"{tag}_{suffix}.png"
 try:page.screenshot(path=str(O/name),full_page=False,timeout=15000)
 except Exception as exc:return "screenshot failed: "+str(exc)[:180]
 return name
def textbody(page):
 try:return page.locator("body").inner_text(timeout=5000)[:4500]
 except Exception as exc:return f"body_read_error={exc}"
def verify_native_bytes(blob,filename,origin,record):
 if len(blob)<1000 or len(blob)>80_000_000 or blob[:4]!=b"glTF":return False
 dest=O/filename
 dest.write_bytes(blob)
 try:
  sc=trimesh.load(str(dest),force="scene",process=False)
  triangles=sum(len(g.faces) for g in sc.geometry.values())
  meshes=len(sc.geometry)
  bounds=sc.bounds.tolist() if sc.bounds is not None else None
  if triangles<1000: raise ValueError("not substantial native 3D geometry")
  record["native_glb"]={"name":filename,"size":len(blob),"sha256":sha(blob),
   "triangle_count":int(triangles),"geometry_count":meshes,"bounds":bounds,"origin":origin}
  report["native_glb"]=record["native_glb"]
  return True
 except Exception as exc:
  dest.unlink(missing_ok=True)
  record.setdefault("invalid_native",[]).append(str(exc)[:250])
  return False
def public_refs(page):
 try:
  return page.evaluate("""() => Array.from(document.querySelectorAll('a[href],model-viewer[src],[src$=".glb"]'))
    .map(e=>({url:e.href||e.src||'',label:(e.innerText||e.getAttribute('title')||'').trim().slice(0,80)}))
    .filter(e=>/\.glb(?:[?#]|$)|\/file=|download.*glb/i.test(e.url))
    .slice(0,12)""")
 except Exception:return []
def probe_site(browser,sp):
 r={"provider":sp["id"],"source_url":sp["url"],"intent":sp["intent"],
    "status":"NOT_STARTED","payment_usd":0,"webgl_unverified":True}
 report["providers"].append(r);save()
 page=browser.new_page(viewport={"width":1280,"height":900},accept_downloads=True)
 network=[]; dl=[]
 def on_response(response):
  try:
   url=response.url
   if re.search(r"\.glb(?:[?#]|$)",url,re.I):
    network.append({"url":url,"http":response.status,"mime":response.headers.get("content-type","")})
  except Exception:pass
 def on_download(download):
  try:
   target=O/(sp["id"]+"__download.glb")
   download.save_as(str(target))
   dl.append({"path":target.name,"suggested_name":download.suggested_filename,
     "size":target.stat().st_size})
  except Exception as exc:dl.append({"error":str(exc)[:200]})
 page.on("response",on_response);page.on("download",on_download)
 try:
  initial=page.goto(sp["url"],wait_until="domcontentloaded",timeout=65000)
  r["http_initial"]=initial.status if initial else None
  page.wait_for_timeout(4000)
  r["title"]=page.title()
  r["initial_text"]=textbody(page)[:2200]
  r["initial_screenshot"]=shot(page,sp["id"],"open")
  if r["http_initial"]!=200:
   r["status"]="HTTP_NOT_200";return
  if re.search(r"cloudflare|performing security verification|turnstile|captcha|verify you are human",r["initial_text"],re.I):
   r["status"]="ANTI_BOT_CHALLENGE_NOT_BYPASSED";return
  inputs=page.locator("input[type=file]")
  r["actual_file_inputs"]=inputs.count()
  if not inputs.count():
   r["status"]="NO_UPLOAD_CONTROL";return
  inputs.first.set_input_files(str(P.resolve()),timeout=15000)
  page.wait_for_timeout(6000)
  r["after_upload_text"]=textbody(page)[:2600]
  r["after_upload_screenshot"]=shot(page,sp["id"],"upload")
  if re.search(r"sign in required|log in to upload|upload failed|please sign in",r["after_upload_text"],re.I):
   r["status"]="LOGIN_REQUIRED";return
  buttons=page.get_by_role("button")
  labels=[]
  for i in range(min(buttons.count(),90)):
   try:
    b=buttons.nth(i)
    if b.is_visible(timeout=500):
     label=(b.inner_text(timeout=500) or b.get_attribute("aria-label") or "").strip()
     if label:labels.append({"i":i,"name":label[:100],"enabled":b.is_enabled(timeout=500)})
   except Exception:pass
  r["actual_buttons"]=labels
  matches=[b for b in labels if re.search(sp["button"],b["name"],re.I) and b["enabled"]]
  if not matches:
   r["status"]="NO_ENABLED_FREE_GENERATE_CONTROL";return
  button=buttons.nth(matches[0]["i"])
  r["generation_button"]=matches[0]["name"]
  button.click(timeout=15000)
  r["clicked_generation"]=True
  r["status"]="GENERATE_CLICKED"
  r["generation_started_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
  shot(page,sp["id"],"start")
  t=time.monotonic();samples=[]
  while time.monotonic()-t < sp["max_seconds"]:
   page.wait_for_timeout(6500)
   txt=textbody(page);small=re.sub(r"\s+"," ",txt)[:550]
   if len(samples)<30:samples.append({"elapsed":round(time.monotonic()-t,1),"text":small})
   if re.search(r"out of (?:free )?credits|quota exceeded|free quota|not enough credits|payment required|subscribe to|purchase credits|upgrade your plan|log in to continue",txt,re.I):
    r["status"]="QUOTA_OR_PAYMENT_BLOCKED_NO_SPEND";break
   if re.search(r"server error|internal server error|job failed|generation failed|GPU is busy|try again later",txt,re.I):
    r["status"]="SERVER_OR_MODEL_FAILURE";break
   # Accept only actually loaded native .glb response URL or visible public link.
   urls=[x["url"] for x in network if x["http"]==200]
   urls += [x["url"] for x in public_refs(page)]
   seen=set()
   for url in urls:
    if url in seen or not url.startswith("https://") and not url.startswith("http://"):continue
    seen.add(url)
    try:
     response=page.request.get(url,timeout=20000)
     if response.status==200 and verify_native_bytes(response.body(),sp["id"]+"__UNREVIEWED_NO_RELEASE.glb",url,r):
      r["status"]="ACTUAL_NATIVE_GLB_ACQUIRED_UNREVIEWED"
      break
    except Exception as exc:r.setdefault("public_download_errors",[]).append(str(exc)[:160])
   if report["native_glb"]:break
   # If a genuinely downloaded result exists, verify it; no forced click for a paywall.
   for item in dl:
    candidate=O/item.get("path","not-a-file")
    if candidate.is_file() and verify_native_bytes(candidate.read_bytes(),
        sp["id"]+"__UNREVIEWED_NO_RELEASE.glb","VISIBLE_BROWSER_DOWNLOAD",r):
     r["status"]="ACTUAL_NATIVE_GLB_ACQUIRED_UNREVIEWED";break
   if report["native_glb"]:break
   # Click a visible explicit free download GLB button only if result is already marked finished.
   if re.search(r"(3d model is ready|model is ready|generation complete|download glb)",txt,re.I):
    dl_buttons=page.get_by_role("button",name=re.compile("download (?:GLB|3D model)",re.I))
    if dl_buttons.count():
     try:dl_buttons.first.click(timeout=2000)
     except Exception:pass
  r["samples"]=samples[-24:]
  if r["status"]=="GENERATE_CLICKED":r["status"]="NO_NATIVE_GLB_IN_OBSERVED_WINDOW"
  r["final_text"]=textbody(page)[-2700:]
  r["after_generation_screenshot"]=shot(page,sp["id"],"after")
 except Exception as exc:
  r["status"]="BROWSER_EXCEPTION"
  r["error"]=repr(exc)[:850];r["traceback"]=traceback.format_exc()[-1400:]
  shot(page,sp["id"],"exception")
 finally:
  r["observed_glb_responses"]=network[:20]
  r["browser_downloads"]=dl[:20]
  r["final_public_model_links"]=public_refs(page)
  page.close();save()
if __name__=="__main__":
 if not P.is_file() or not WHITE.is_file():raise RuntimeError("Run295 original reference preprocessing must complete first")
 if sha(WHITE.read_bytes())!=EXPECTED_WHITE_SHA:raise RuntimeError("Original chick white reference SHA mismatch; abort")
 report["reference_png_sha256"]=sha(P.read_bytes())
 report["reference_white_sha256"]=sha(WHITE.read_bytes())
 save()
 with sync_playwright() as playwright:
  browser=playwright.chromium.launch(headless=True,args=[
   "--no-sandbox","--disable-dev-shm-usage","--enable-webgl","--use-gl=angle",
   "--use-angle=swiftshader","--enable-unsafe-swiftshader"])
  try:
   for s in SITES:
    probe_site(browser,s)
    if report["native_glb"]:break
  finally:browser.close()
 report["finished_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
 (O/"STRICT_NO_RELEASE.txt").write_text(
  "#172 3D public service generation experiments. Genuine native GLB is NOT product art approval.\n"
  "No paid requests or CAPTCHA bypass. Real side/back/fluffy down, licensing and physical phone are unverified.\n"
  "NEVER deploy, merge, represent to the user as an accepted owl or count toward 251-species art.\n")
 save()
 print(json.dumps(report,indent=2,ensure_ascii=False))
