#!/usr/bin/env python3
"""Run207c: second/last permitted free browser generation focused on actual GLB export.
No paid credits; no captcha bypass; leave all output in expiring research artifact.
"""
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import urlparse
import os,sys,time,hashlib,json,traceback,base64,re
from PIL import Image
ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
E=ROOT/"research-evidence-run207c-HY3D-GLB-CAPTURE-NO_RELEASE"
SRC=ROOT/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
SHA="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
STATE={"run":"207c","utc_start":datetime.now(timezone.utc).isoformat(),
       "source_sha256":SHA,"paid_spend":0,"art_approved":False,"published":False,
       "physical_mobile_gpu_acceptance":False,"status":"NO_RELEASE"}
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,data):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2,default=str)+"\n")
def preflight():
 paths=["owl-pet/AGENTS.md","owl-pet/README.md","owl-pet/STATUS.md","owl-pet/prototype/index.html",
        "owl-pet/research/species/172-tyto-castanops-v3.md",
        str(ROOT/"known_rejected_asset_sha256_registry.json"),
        str(ROOT/"2026-11-19-run206b-shortprompt-independent-original-artifact-NO_RELEASE.md"),
        str(SRC)]
 proof={}
 for p in paths:
  raw=Path(p).read_bytes()
  if len(raw)<30:raise RuntimeError("missing "+p)
  proof[p]={"bytes":len(raw),"sha256":sha(raw)}
 if proof[str(SRC)]["sha256"]!=SHA:raise RuntimeError("source hash mismatch")
 dump(E/"preflight.json",proof)
def attempt():
 import requests
 from playwright.sync_api import sync_playwright
 responses=[];found=[];network_url=[]
 def save_glb(raw,origin):
  if raw[:4]!=b"glTF" or len(raw)<10000 or len(raw)>65_000_000:return False
  h=sha(raw)
  if any(q["sha256"]==h for q in found):return True
  f=E/("native_output_%d.glb"%len(found));f.write_bytes(raw)
  found.append({"file":str(f),"bytes":len(raw),"sha256":h,"origin":origin})
  return True
 def scan_obj(obj,origin,depth=0):
  if depth>6:return
  if isinstance(obj,dict):
   for k,v in obj.items():
    if isinstance(v,str):
     if v.startswith("data:model/gltf-binary;base64,"):
      try:save_glb(base64.b64decode(v.split(",",1)[1]),origin+"/"+k)
      except Exception:pass
     if len(v)>100000 and re.fullmatch(r'[A-Za-z0-9+/=]+',v[:1000]):
      try:save_glb(base64.b64decode(v),origin+"/"+k)
      except Exception:pass
     if v.startswith("http") and any(z in v.lower() for z in (".glb","/output/","/file/","/download")):
      network_url.append({"origin":origin,"field":k,"url":v})
    if isinstance(v,(dict,list)):scan_obj(v,origin+"/"+str(k),depth+1)
  if isinstance(obj,list):
   for i,v in enumerate(obj[:30]):scan_obj(v,origin+"/"+str(i),depth+1)
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,args=["--disable-dev-shm-usage","--use-angle=swiftshader"])
  page=browser.new_page(viewport={"width":1280,"height":900},accept_downloads=True)
  page.set_default_timeout(12000)
  def on_resp(resp):
   url=resp.url
   host=urlparse(url).hostname or ""
   if host.endswith("hy3d.dev") and "/api/hy3d/" in url:
    try:
     b=resp.body()
     record={"url":url.split("?")[0],"status":resp.status,
             "content_type":resp.headers.get("content-type"),"bytes":len(b),"sha256":sha(b)}
     if b[:4]==b"glTF":save_glb(b,"api_response_binary")
     try:
      obj=json.loads(b)
      record["json_keys"]=list(obj) if isinstance(obj,dict) else []
      record["small_json"]=obj if len(b)<20000 else "too_large"
      scan_obj(obj,url.split("?")[0])
     except Exception:record["body_excerpt"]=b[:250].decode("utf8","replace")
     responses.append(record)
    except Exception as ex:responses.append({"url":url[:170],"capture_error":repr(ex)})
   if (url.lower().split("?")[0].endswith(".glb") or resp.headers.get("content-type","").lower().startswith("model/gltf")) and resp.ok:
    try:save_glb(resp.body(),"browser_glb_response")
    except Exception:pass
  page.on("response",on_resp)
  top=page.goto("https://hy3d.dev/",wait_until="domcontentloaded",timeout=70000)
  STATE["page_http"]=top.status if top else None
  page.wait_for_timeout(2000)
  page.locator('input[type="file"]').first.set_input_files(str(SRC.resolve()))
  STATE["original_source_uploaded"]=True
  page.wait_for_timeout(2500)
  page.screenshot(path=str(E/"uploaded_source.png"))
  btn=page.get_by_role("button",name="Generate",exact=False)
  STATE["generate_buttons"]=btn.count()
  if btn.count()!=1:raise RuntimeError("ambiguous generate control")
  if not btn.is_enabled():raise RuntimeError("generate disabled")
  text=btn.inner_text().lower()
  if any(x in text for x in ("upgrade","buy","purchase","subscribe")):raise RuntimeError("payment forbidden")
  btn.click()
  STATE["submitted_one_free_ui_request"]=True
  for j in range(1,25):
   page.wait_for_timeout(7000)
   if j in (1,4,8,12,18,24):
    page.screenshot(path=str(E/("poll_%02d.png"%j)))
   if found:break
   # Never click again on Generate. UI output is rendered in a 3D viewer;
   # collect eligible DOM download controls, including icon-only buttons.
   dom=page.locator("button,a").evaluate_all("""(els) => els.map((x,i) => ({
      i,tag:x.tagName,txt:(x.innerText||'').trim().slice(0,80),
      title:x.getAttribute('title'),aria:x.getAttribute('aria-label'),
      href:(x.getAttribute('href')||'').slice(0,180),
      outer:x.outerHTML.slice(0,650)})).filter(x=>/down|export|\\.glb|save|model/i.test(
       [x.txt,x.title,x.aria,x.href,x.outer].join(' '))).slice(0,30)""")
   dump(E/"download_dom_live.json",dom)
   selectors=[
    'button[aria-label*="download" i]', 'button[title*="download" i]',
    'a[download]', 'button:has(svg.lucide-download)',
    'button:has(svg[data-lucide="download"])','a[href*=".glb"]',
    'button[aria-label*="export" i]','button[title*="export" i]'
   ]
   for sel in selectors:
    targets=page.locator(sel)
    for k in range(min(targets.count(),3)):
     t=targets.nth(k)
     if not t.is_visible() or not t.is_enabled():continue
     try:
      with page.expect_download(timeout=6000) as info:t.click(timeout=4000)
      dl=info.value; raw=(E/"download_candidate.bin")
      dl.save_as(str(raw))
      if save_glb(raw.read_bytes(),"download_event:"+sel):
       STATE["successful_download_selector"]=sel
       break
      raw.rename(E/"non_glb_download.bin")
     except Exception:pass
    if found:break
   if found:break
   # If an async job exposes an upstream storage URL, request only HTTPS model output.
   for item in network_url[-10:]:
    url=item["url"]; parsed=urlparse(url)
    if parsed.scheme!="https" or not parsed.hostname or parsed.hostname in ("127.0.0.1","localhost"):continue
    if not any(z in url.lower() for z in (".glb","/download","/output/")):continue
    try:
     rsp=requests.get(url,timeout=(10,35))
     STATE["url_download_http"]=rsp.status_code
     if rsp.ok and save_glb(rsp.content,"approved_response_url:"+item["field"]):break
    except Exception:pass
   if found:break
  page.screenshot(path=str(E/"final_screen.png"),full_page=False)
  (E/"final_visible_text.txt").write_text(page.locator("body").inner_text()[:9500])
  (E/"all_buttons_final.txt").write_text(str(page.locator("button").evaluate_all(
      "(els) => els.map(x => x.outerHTML.slice(0,800))"))[:22000])
  STATE["capture_attempts"]=j
  STATE["found_native_glb"]=found
  dump(E/"api_responses.json",responses)
  dump(E/"discovered_download_urls.json",network_url)
  browser.close()
 return found
def inspect(m):
 import trimesh
 raw=Path(m["file"]).read_bytes()
 sc=trimesh.load(m["file"],force="scene",process=False)
 parts=[g for g in sc.geometry.values() if hasattr(g,"faces")]
 obj={"sha256":sha(raw),"bytes":len(raw),"mesh_count":len(parts),
      "triangles":sum(len(g.faces) for g in parts),
      "vertices":sum(len(g.vertices) for g in parts)}
 registry=json.loads((ROOT/"known_rejected_asset_sha256_registry.json").read_text())
 obj["previously_rejected_sha256"]=obj["sha256"] in json.dumps(registry)
 dump(E/"native_metrics.json",obj)
 return obj
def sevenview(path):
 # Reuse original world-axis VTK renderer in prior Run207; input name is isolated.
 import subprocess
 run207=ROOT/"run207_hy3d_public_browser_native_gate.py"
 # Do not execute script's main browser; dynamic import only exposes render.
 import importlib.util
 spec=importlib.util.spec_from_file_location("run207_render",run207)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 original=module.E
 module.E=E
 try:module.render(Path(path))
 finally:module.E=original
def finish():
 STATE["utc_end"]=datetime.now(timezone.utc).isoformat()
 dump(E/"status.json",STATE)
 inv={}
 for p in sorted(E.rglob("*")):
  if p.is_file() and p.name!="manifest.json":
   b=p.read_bytes();inv[str(p.relative_to(E))]={"bytes":len(b),"sha256":sha(b)}
 dump(E/"manifest.json",inv)
 print(json.dumps(STATE,ensure_ascii=False,indent=2,default=str))
def main():
 E.mkdir(parents=True,exist_ok=True)
 try:
  preflight()
  models=attempt()
  if models:
   STATE["native_mesh"]=inspect(models[0])
   if STATE["native_mesh"]["triangles"]>=1000 and not STATE["native_mesh"]["previously_rejected_sha256"]:
    try:sevenview(models[0]["file"]);STATE["status"]="REAL_GLB_NATIVE_SEVENVIEW_ART_UNREVIEWED_NO_RELEASE"
    except Exception as ex:
     STATE["status"]="REAL_GLB_RENDER_FAILURE_NO_RELEASE";STATE["render_error"]=repr(ex)
     (E/"render_trace.txt").write_text(traceback.format_exc())
   else:STATE["status"]="NATIVE_MESH_REJECTED_OR_INVALID_NO_RELEASE"
  else:STATE["status"]="BROWSER_3D_PREVIEW_VISIBLE_BUT_BINARY_NOT_CAPTURED_NO_RELEASE"
 except Exception as ex:
  STATE["status"]="ERROR_NO_RELEASE";STATE["exception"]=repr(ex)
  (E/"exception.txt").write_text(traceback.format_exc())
 finally:finish()
if __name__=="__main__":main()
