#!/usr/bin/env python3
"""Run207: actual public no-charge image-conditioned Hunyuan browser trial.
Strictly nonrelease. No anti-bot bypass, payment, or proxy rotation.
"""
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import urlparse
import hashlib,json,time,traceback,os,platform
from PIL import Image,ImageDraw
import numpy as np

ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
E=ROOT/"research-evidence-run207-HY3D-PUBLIC-UI-NO_RELEASE"
SRC=ROOT/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
PREFLIGHT=[
"owl-pet/AGENTS.md","owl-pet/README.md","owl-pet/STATUS.md",
"owl-pet/prototype/index.html","owl-pet/research/species/172-tyto-castanops-v3.md",
str(ROOT/"known_rejected_asset_sha256_registry.json"),
str(ROOT/"2026-11-19-run206b-shortprompt-independent-original-artifact-NO_RELEASE.md")]
S={"run":207,"started_utc":datetime.now(timezone.utc).isoformat(),"method":"real source image via public https://hy3d.dev/ UI; never text-only",
   "vendor_page_claim":"no-signup, three free untextured mesh generations/day; not independently verified",
   "paid_spend":0,"art_approved":False,"real_phone_gpu_test":False,"published":False,"status":"NO_RELEASE"}
def digest(data):return hashlib.sha256(data).hexdigest()
def dump(p,o):
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(o,ensure_ascii=False,indent=2,default=str)+"\n")
def preflight():
 m={}
 for n in PREFLIGHT+[str(SRC)]:
  b=Path(n).read_bytes()
  if len(b)<30:raise RuntimeError("missing preflight "+n)
  m[n]={"bytes":len(b),"sha256":digest(b)}
 if m[str(SRC)]["sha256"]!=EXPECTED:raise RuntimeError("wrong source reference sha256")
 dump(E/"preflight.json",m)
 S["source_sha256_verified"]=EXPECTED
 S["runtime"]=platform.platform()

def web_try():
 from playwright.sync_api import sync_playwright,TimeoutError as PlaywrightTimeoutError
 web_events=[]
 api_models=[]
 started=time.monotonic()
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,args=["--disable-dev-shm-usage","--use-gl=angle","--use-angle=swiftshader"])
  page=browser.new_page(viewport={"width":1280,"height":950},accept_downloads=True)
  page.set_default_timeout(20000)
  page.on("pageerror",lambda e:web_events.append({"kind":"page_error","detail":str(e)[:400]}))
  def on_response(resp):
   try:
    url=resp.url
    host=urlparse(url).hostname or ""
    if host in ("hy3d.dev","www.hy3d.dev") or ("api/" in url and host.endswith(".hy3d.dev")):
     row={"code":resp.status,"url":url.split("?")[0][:200],
       "content_type":resp.headers.get("content-type","")[:80]}
     if len(web_events)<150:web_events.append(row)
     if resp.ok and ("model/gltf-binary" in row["content_type"] or url.lower().split("?")[0].endswith(".glb")):
      try:
       body=resp.body()
       if 10000<len(body)<55_000_000 and body[:4]==b"glTF":
        fn=E/("native_response_%02d.glb"%len(api_models))
        fn.write_bytes(body)
        api_models.append({"path":str(fn),"bytes":len(body),"sha256":digest(body)})
      except Exception as err:web_events.append({"kind":"glb_capture_error","detail":repr(err)})
   except Exception:pass
  page.on("response",on_response)
  resp=page.goto("https://hy3d.dev/",wait_until="domcontentloaded",timeout=65000)
  page.wait_for_timeout(5000)
  S["first_page_http"]=resp.status if resp else None
  S["title"]=page.title()
  S["url"]=page.url
  page.screenshot(path=str(E/"ui_initial.png"),full_page=True,animations="disabled",timeout=35000)
  page_text=page.locator("body").inner_text(timeout=10000)
  (E/"visible_page_text.txt").write_text(page_text[:8500])
  (E/"input_dom_excerpt.txt").write_text(page.locator("input").evaluate_all("(els) => els.map(x => ({type:x.type,accept:x.accept,outerHTML:x.outerHTML.slice(0,450)}))").__str__()[:5000])
  if S["first_page_http"]!=200 or "security verification" in page_text.lower() or "just a moment" in page_text.lower():
   S["status"]="BROWSER_HTTP_OR_SECURITY_CHALLENGE_NO_RELEASE"
  elif page.locator('input[type="file"]').count()==0:
   S["status"]="NO_ACCESSIBLE_FILE_INPUT_NO_RELEASE"
  else:
   inp=page.locator('input[type="file"]').first
   inp.set_input_files(str(SRC.resolve()))
   page.wait_for_timeout(2600)
   page.screenshot(path=str(E/"ui_after_file_upload.png"),full_page=True,animations="disabled",timeout=35000)
   S["uploaded_original_source_file"]=True
   S["uploaded_file_sha256"]=EXPECTED
   candidate=page.get_by_role("button",name="Generate",exact=False)
   if candidate.count()==0:candidate=page.locator("button").filter(has_text="GENERATE")
   S["generate_candidate_buttons"]=candidate.count()
   if candidate.count()==0:
    S["status"]="GENERATE_BUTTON_NOT_FOUND_NO_RELEASE"
   else:
    btn=None
    for i in range(candidate.count()):
     c=candidate.nth(i)
     if c.is_visible() and c.is_enabled():
      btn=c;break
    if btn is None:
     S["status"]="GENERATE_BUTTON_DISABLED_OR_HIDDEN_NO_RELEASE"
    else:
     s=btn.inner_text()[:180]
     if any(w in s.lower() for w in ("purchase","payment","buy credits","upgrade")):
      S["status"]="PAID_FLOW_NOT_AUTHORIZED"
     else:
      btn.click(timeout=12000)
      S["actual_generate_clicked"]=True
      S["clicked_button_label"]=s
      page.wait_for_timeout(2500)
      page.screenshot(path=str(E/"ui_after_submit.png"),full_page=True,animations="disabled",timeout=35000)
      for j in range(1,13):
       page.wait_for_timeout(11000)
       txt=page.locator("body").inner_text(timeout=10000)
       if j in (1,3,6,9,12):
        page.screenshot(path=str(E/("ui_poll_%02d.png"%j)),full_page=False,animations="disabled",timeout=20000)
       (E/"visible_after_submit.txt").write_text(txt[:9000])
       if any(w in txt.lower() for w in ("quota exceeded","daily limit","limit reached","need to sign in","payment required","not enough credits")):
        S["status"]="FREE_QUOTA_OR_PAYMENT_BLOCK_NO_RELEASE";break
       if api_models:break
       download_links=page.locator('a[download],a[href$=".glb"],button:has-text("Download")')
       if download_links.count()>0:
        for k in range(min(download_links.count(),4)):
         d=download_links.nth(k)
         if not d.is_visible() or not d.is_enabled():continue
         try:
          with page.expect_download(timeout=7000) as ev:d.click(timeout=7000)
          dl=ev.value; fn=E/"native_download.glb";dl.save_as(str(fn))
          if fn.read_bytes()[:4]==b"glTF":
           b=fn.read_bytes();api_models.append({"path":str(fn),"bytes":len(b),"sha256":digest(b)})
          else:fn.rename(E/"non_glb_download.bin")
          break
         except Exception as err:web_events.append({"kind":"download_not_ready","detail":repr(err)[:200]})
        if api_models:break
       if j==12:S["status"]="UI_POLL_EXHAUSTED_NO_GLB"
  S["elapsed_browser_seconds"]=round(time.monotonic()-started,2)
  S["captured_glb"]=api_models
  dump(E/"network_response_summary.json",web_events)
  browser.close()
 return api_models
def inspect_model(path):
 import trimesh
 raw=Path(path).read_bytes()
 if raw[:4]!=b"glTF":raise ValueError("NOT_GLB")
 sc=trimesh.load(path,force="scene",process=False)
 meshes=[m for m in sc.geometry.values() if hasattr(m,"faces")]
 n=sum(len(m.faces) for m in meshes)
 info={"bytes":len(raw),"sha256":digest(raw),"meshes":len(meshes),
      "triangles":n,"vertices":sum(len(m.vertices) for m in meshes)}
 registry=json.loads((ROOT/"known_rejected_asset_sha256_registry.json").read_text())
 info["already_rejected_sha256"]=info["sha256"] in json.dumps(registry)
 dump(E/"native_mesh_metrics.json",info)
 if n<1000:raise ValueError("INSUFFICIENT_NATIVE_TOPOLOGY")
 if info["already_rejected_sha256"]:return info
 try:render(Path(path))
 except Exception as err:
  (E/"render_error.txt").write_text(traceback.format_exc())
  S["render_error"]=repr(err)
 return info
def render(mesh):
 import vtk
 vtk.vtkObject.GlobalWarningDisplayOff()
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(True);win.SetSize(420,420)
 imp=vtk.vtkGLTFImporter();imp.SetFileName(str(mesh.resolve()));imp.SetRenderWindow(win);imp.Update()
 ren=win.GetRenderers().GetFirstRenderer()
 if ren is None:raise RuntimeError("no VTK renderer")
 ren.SetBackground(.93,.93,.91)
 bb=ren.ComputeVisiblePropBounds()
 mid=np.array([(bb[0]+bb[1])/2,(bb[2]+bb[3])/2,(bb[4]+bb[5])/2])
 span=max(bb[1]-bb[0],bb[3]-bb[2],bb[5]-bb[4])
 if not np.isfinite(span) or span<=0:raise RuntimeError("bad bounds")
 cams={"world_zplus":([0,0,1],[0,1,0]),"world_zminus":([0,0,-1],[0,1,0]),
       "world_xplus":([1,0,0],[0,1,0]),"world_xminus":([-1,0,0],[0,1,0]),
       "world_yplus":([0,1,0],[0,0,-1]),"world_yminus":([0,-1,0],[0,0,1]),
       "world_quarter":([.7,.3,1],[0,1,0])}
 sheet=Image.new("RGB",(1680,900),(246,246,243));draw=ImageDraw.Draw(sheet)
 for i,(name,(vec,up)) in enumerate(cams.items()):
  v=np.array(vec,dtype=float);v/=np.linalg.norm(v)
  cam=ren.GetActiveCamera();cam.SetFocalPoint(*mid);cam.SetPosition(*(mid+2.7*span*v))
  cam.SetViewUp(*up);cam.ParallelProjectionOn();cam.SetParallelScale(.78*span)
  ren.ResetCameraClippingRange();win.Render()
  cap=vtk.vtkWindowToImageFilter();cap.SetInput(win);cap.ReadFrontBufferOff();cap.Update()
  fp=E/("native_"+name+".png");w=vtk.vtkPNGWriter();w.SetFileName(str(fp))
  w.SetInputConnection(cap.GetOutputPort());w.Write()
  img=Image.open(fp).convert("RGB")
  x=(i%4)*420;y=(i//4)*450
  sheet.paste(img,(x,y+24));draw.text((x+12,y+5),name,fill=(0,0,0))
 sheet.save(E/"native_seven_view_world_axes.png")
 S["native_world_camera_views"]=7
 S["real_phone_gpu_test"]=False
def finish():
 S["completed_utc"]=datetime.now(timezone.utc).isoformat()
 dump(E/"status.json",S)
 manifest={}
 for path in sorted(E.rglob("*")):
  if path.is_file() and path.name!="manifest.json":
   b=path.read_bytes();manifest[str(path.relative_to(E))]={"bytes":len(b),"sha256":digest(b)}
 dump(E/"manifest.json",manifest)
 (ROOT/"2026-11-19-run207-public-hunyuan-image-conditioned-browser-NO_RELEASE.md").write_text(
  "# Run207 actual public free image-to-3D browser test — nonrelease\n\n"
  "Source: #172 v3 rightmost crop, locally SHA256 verified; source upload is marked only if Playwright succeeded.\n"
  "Original 3D files, browser screenshots, traffic summaries and seven native world-axis views, if any, are isolated in the expiring CI artifact.\n"
  "Status: **"+S.get("status","NO_RELEASE")+"**; native GLB: "+str(S.get("native_mesh",{}))+"\n"
  "No paid credits, Cloudflare bypass, password, main, prototype, 251-species workflow or deployment changes.\n"
  "Native mesh/WebGL technical checks cannot substitute for an anatomical/down quality review. No smartphone GPU claim. **NO_RELEASE**.\n")
 print(json.dumps(S,ensure_ascii=False,indent=2))
def main():
 E.mkdir(parents=True,exist_ok=True)
 try:
  preflight()
  models=web_try()
  for m in models:
   try:
    S["native_mesh"]=inspect_model(m["path"])
    S["status"]="NATIVE_GLB_RENDERED_ART_UNREVIEWED_NO_RELEASE"
   except Exception as ex:
    S["status"]="NATIVE_GLB_VALIDATION_FAILED_NO_RELEASE"
    S["native_error"]=repr(ex)
    (E/"model_exception.txt").write_text(traceback.format_exc())
   break
 except Exception as e:
  S["exception"]=repr(e);S["status"]="BROWSER_OR_PREFLIGHT_EXCEPTION_NO_RELEASE"
  (E/"exception_trace.txt").write_text(traceback.format_exc())
 finally:finish()
if __name__=="__main__":main()
