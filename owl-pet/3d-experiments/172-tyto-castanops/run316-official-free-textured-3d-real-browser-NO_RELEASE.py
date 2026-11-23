#!/usr/bin/env python3
"""Run316: real official free GPU UI attempts for #172 v3 rightmost chick.
Use public anonymous browser forms only; no tokens, billing, bypass, or fake meshes.
Only a real native GLB with front/side/back art review can ever become a candidate.
"""
from __future__ import annotations
import hashlib, json, os, pathlib, re, time, traceback
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright, TimeoutError as BrowserTimeout

OUT=pathlib.Path("owl172-run316-evidence")
OUT.mkdir(exist_ok=True)
SRC=pathlib.Path("owl172-run295-evidence/young-REAL-PHOTO-PIXELS-transparent-input-NO_3D.png")
EXPECTED="6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77"
SERVICES=[
  dict(id="microsoft_TRELLIS2",url="https://microsoft-trellis-2.hf.space/",
       label="Microsoft TRELLIS.2 official ZeroGPU",family="MIT model/code; optional dependencies need review",
       generation_regex=r"^\s*Generate\s*$",extract_regex=r"Extract GLB",
       time_limit=220),
  dict(id="stability_stablefast3d",url="https://stabilityai-stable-fast-3d.hf.space/",
       label="Stability AI Stable Fast 3D official ZeroGPU",family="community license; rights unverified",
       generation_regex=r"Run|Generate|Convert",extract_regex=r"Download",
       time_limit=140),
]
report={
 "run":316, "utc_started":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
 "target":"#172 Tyto castanops v3 ORIGINAL RIGHTMOST age-unknown cream mesoptile",
 "rights_cleared":False, "physical_phone_tested":False, "art_approved":False,
 "webgl2_candidate_tested":False,"payment_usd":0,"release":False,
 "native_glb":[],"attempts":[],
 "allowed":"Public UI, no account registration or purchase, one request max per provider"}
events=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def persist():
 (OUT/"run316_actual_results.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 (OUT/"observed_network.json").write_text(json.dumps(events[-150:],ensure_ascii=False,indent=2)+"\n")
def catch(response, service):
 try:
  u=response.url
  if len(events)>200:return
  if (".glb" in u.lower() or "queue" in u or "upload" in u or "api/" in u):
   events.append({"provider":service,"status":response.status,"url":u[:260],
       "mime":response.headers.get("content-type","")[:80]})
 except Exception:pass
def ui(page):
 try:
  return page.locator("body").inner_text(timeout=3500)[:6500]
 except Exception as e:return "body unavailable: "+str(e)[:300]
def screenshot(page,name):
 try:page.screenshot(path=str(OUT/name),full_page=False,timeout=12000)
 except Exception as e:return str(e)[:180]
 return name
def get_real_glb_from_visible_public_links(page,service_id,at):
 """Only current-page publicly exposed download URLs. Never private endpoints."""
 links=page.evaluate("""() => [...document.querySelectorAll('a')].map(a => ({
     text:(a.innerText || a.getAttribute('aria-label') || '').trim().slice(0,90),
     url:a.href || ''})).filter(x => /(?:\.glb(?:\?|$)|Download GLB)/i.test(x.url+' '+x.text)).slice(0,20)""")
 at["visible_public_links"]=links
 for link in links:
  u=link["url"]
  if not u.startswith("https://") or "blob:" in u or "javascript:" in u:continue
  # Explicit link to an ordinary public generated GLB. Keep same browser session.
  if ".glb" not in u.lower() and "/file=" not in u.lower():continue
  try:
   rsp=page.request.get(u,timeout=35000)
   if rsp.status!=200:continue
   b=rsp.body()
   if b[:4]!=b"glTF" or len(b)>75_000_000:continue
   dest=OUT/(service_id+"_unreviewed_native.glb"); dest.write_bytes(b)
   at["public_download_real_glb"]={"filename":dest.name,"size":len(b),"sha256":sha(b)}
   report["native_glb"].append(at["public_download_real_glb"])
   return True
  except Exception as e:at.setdefault("download_errors",[]).append(repr(e)[:250])
 return False
def attempt(page,spec):
 at={"id":spec["id"],"url":spec["url"],"label":spec["label"],
     "status":"INITIAL","made_generation_click":False,"native_glb":False,
     "real_phone":False,"paid_usd":0,"release":False}
 report["attempts"].append(at);persist()
 page.on("response",lambda resp: catch(resp,spec["id"]))
 try:
  rsp=page.goto(spec["url"],wait_until="domcontentloaded",timeout=65000)
  at["initial_http"]=rsp.status if rsp else None
  page.wait_for_timeout(4000)
  at["initial_url"]=page.url;at["initial_title"]=page.title()
  at["initial_text"]=ui(page)[:2400]
  at["initial_screenshot"]=screenshot(page,spec["id"]+"_initial.png")
  at["file_inputs"]=page.locator("input[type=file]").count()
  if at["initial_http"] not in (200,304):
   at["status"]="HTTP_NOT_OK";return
  if at["file_inputs"]<1:
   at["status"]="NO_USABLE_IMAGE_UPLOAD_UI";return
  page.locator("input[type=file]").first.set_input_files(str(SRC.resolve()),timeout=10000)
  page.wait_for_timeout(8500)
  at["after_select_text"]=ui(page)[:2800]
  at["after_upload_screenshot"]=screenshot(page,spec["id"]+"_after_upload.png")
  at["visible_file_input_count"]=page.locator("input[type=file]").count()
  # Gradio replaces native input after upload; this is NOT a lost upload by itself.
  if re.search(r"(sign\s*in\s*to\s*upload|log\s*in\s*to\s*upload|upload\s*failed|please\s*sign\s*in)",at["after_select_text"],re.I):
   at["status"]="UPLOAD_REQUIRES_ACCOUNT";return
  buttons=page.get_by_role("button")
  labels=[]
  for i in range(min(buttons.count(),65)):
   try:
    b=buttons.nth(i)
    if not b.is_visible(timeout=250):continue
    label=(b.inner_text(timeout=600) or b.get_attribute("aria-label") or "").strip()
    if label:labels.append({"index":i,"label":label[:85],"enabled":b.is_enabled(timeout=600)})
   except Exception:pass
  at["buttons"]=labels
  choices=[x for x in labels if re.search(spec["generation_regex"],x["label"],re.I)
           and x["enabled"]]
  if not choices:
   at["status"]="NO_ENABLED_PUBLIC_GENERATE_BUTTON";return
  button=buttons.nth(choices[0]["index"])
  at["generation_button"]=choices[0]
  button.click(timeout=9000)
  at["made_generation_click"]=True;at["click_at_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
  at["status"]="GENERATE_CLICK_CONFIRMED"
  page.wait_for_timeout(7000)
  at["during_screenshot"]=screenshot(page,spec["id"]+"_generation_start.png")
  max_t=spec["time_limit"]
  started=time.monotonic(); observed=[]
  while time.monotonic()-started<max_t:
   page.wait_for_timeout(9000)
   txt=ui(page)
   lower=txt.lower()
   observed.append({"seconds":int(time.monotonic()-started),
       "snippet":re.sub(r"\s+"," ",txt[:780])})
   if any(s in lower for s in ["you have exceeded your gpu quota",
       "zerogpu quota","sign in to use","not enough gpu time","you have reached your limit",
       "error while generating","cuda out of memory","an error occurred"]):
    at["status"]="GPU_QUOTA_OR_SERVER_ERROR";break
   # Click a public extract button ONLY after preview evidence, not while idle.
   preview=any(s in lower for s in ["extract glb","3d asset preview","extracted glb"])
   if spec["id"]=="microsoft_TRELLIS2" and preview:
    ext=page.get_by_role("button",name=re.compile("Extract GLB",re.I))
    try:
     if ext.count() and ext.first.is_enabled(timeout=500):
      at["extract_control_seen"]=True
      # Generation states are reflected by a rich multi-angle preview, not a bare button label.
      htmls=page.locator(".previewer-main-image")
      at["preview_multiview_image_count"]=htmls.count()
      if htmls.count()>=8:
       screenshot(page,spec["id"]+"_preview_before_extract.png")
       ext.first.click(timeout=12000)
       at["extract_clicked"]=True
       at["status"]="EXTRACT_CLICK_CONFIRMED"
       page.wait_for_timeout(30000)
       if get_real_glb_from_visible_public_links(page,spec["id"],at):break
    except Exception as e:
     at["extract_attempt_error"]=repr(e)[:450]
   # Standard Gradio browser download interface
   if get_real_glb_from_visible_public_links(page,spec["id"],at):break
   if at.get("public_download_real_glb"):
    at["status"]="NATIVE_GLB_ACQUIRED";break
   # Avoid indefinitely retrying extraction
   if at.get("extract_clicked") and time.monotonic()-started>170:break
  at["poll_samples"]=observed[-25:]
  at["after_generation_text"]=ui(page)[:4000]
  at["after_generation_screenshot"]=screenshot(page,spec["id"]+"_after_generation.png")
  if at.get("public_download_real_glb"):
   at["status"]="NATIVE_GLB_ACQUIRED_UNREVIEWED";at["native_glb"]=True
  elif at["status"] in ("GENERATE_CLICK_CONFIRMED","EXTRACT_CLICK_CONFIRMED"):
   at["status"]="GENERATE_NO_DOWNLOAD_WITHIN_OBSERVED_WINDOW"
 except Exception as e:
  at["status"]="BROWSER_EXECUTION_ERROR"
  at["exception"]=repr(e)[:900]
  at["traceback"]=traceback.format_exc()[-1300:]
  screenshot(page,spec["id"]+"_error.png")
 finally:persist()
if __name__=="__main__":
 if not SRC.is_file():raise FileNotFoundError("Original chick crop script must run first")
 original=pathlib.Path("owl172-run295-evidence/young-isolated-white-background-input-NO_3D.png")
 assert sha(original.read_bytes())==EXPECTED, "Original #172 cutout unexpectedly changed"
 report["reference_transparent_sha256"]=sha(SRC.read_bytes())
 report["reference_white_sha256"]=sha(original.read_bytes())
 persist()
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,args=["--no-sandbox","--use-gl=angle",
      "--use-angle=swiftshader","--enable-unsafe-swiftshader","--disable-dev-shm-usage"])
  for s in SERVICES:
   page=browser.new_page(viewport={"width":1280,"height":900},device_scale_factor=1,accept_downloads=True)
   attempt(page,s)
   page.close()
   if report["native_glb"]:break
  browser.close()
 import trimesh
 for item in report["native_glb"]:
  model=OUT/item["filename"]
  try:
   scene=trimesh.load(str(model),force="scene",process=False)
   item["geometry_count"]=len(scene.geometry)
   item["genuine_triangles"]=sum(len(x.faces) for x in scene.geometry.values())
   item["geometry_valid"]=item["genuine_triangles"]>1000
  except Exception as e:item["parse_error"]=str(e)
 report["utc_finished"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
 report["art_approved"]=False;report["rights_cleared"]=False;report["release"]=False
 (OUT/"STRICT_NO_RELEASE.txt").write_text(
   "Official public free GPU demos tested without accounts, tokens or payment.\n"
   "#172 rightmost chick target. Only native GLB geometry + multi-angle expert art + rights + phone QA qualifies.\n"
   "No public link or demo is an approved owl-pet product. Do not deploy. NO_RELEASE.\n")
 persist()
 print(json.dumps(report,indent=2,ensure_ascii=False))
