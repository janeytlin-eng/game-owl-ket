#!/usr/bin/env python3
"""Run200: test an untried, explicitly free image-to-3D provider with the real #172 crop.
No CAPTCHA bypass, no payment, no model substitutions, no art claims without actual GLB.
Also inspect artist-made free baby owl sculpt availability without circumventing marketplace login.
"""
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import urlparse,urljoin
import hashlib, json, re, time, traceback, struct, os
from playwright.sync_api import sync_playwright
R=Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run200-NEW-ANONYMOUS-IMAGE-TO-3D-NO_RELEASE"
O.mkdir(exist_ok=True,parents=True)
SOURCE=R/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
out={"run":200,"timestamp_utc":datetime.now(timezone.utc).isoformat(),"reference_sha256":hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 "provider":"https://3daistudio.pro/","secondary":"https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt",
 "new_glb":False,"no_release":True,"art_pass":False,"physical_mobile_gpu_pass":False,"no_extra_payment":True,
 "events":[],"errors":[],"network":[],"screenshots":[]}
assert out["reference_sha256"]==EXPECTED, "SOURCE_MISMATCH"
tmp=Path("/tmp/owl172-run200-target-native.glb")
def evt(v):out["events"].append({"t":round(time.monotonic()-t0,1),"event":str(v)[:350]});print(str(v)[:350],flush=True)
t0=time.monotonic()
def screenshot(p,tag):
 try:
  f=O/(tag+".png");p.screenshot(path=str(f),full_page=False,timeout=14000)
  out["screenshots"].append(f.name)
 except Exception as e:evt("SCREENSHOT_ERROR "+tag+" "+repr(e))
def controls(p):
 try:
  buttons=p.locator("button").all()
  return [{"text":(b.inner_text(timeout=1200) or "")[:130],"disabled":b.is_disabled()} for b in buttons[:75]]
 except Exception as e: return [{"error":str(e)[:180]}]
def capture_download(download):
 try:
  name=download.suggested_filename
  download.save_as(str(tmp))
  b=tmp.read_bytes()
  evt("DOWNLOAD_RECEIVED name="+str(name)+" bytes="+str(len(b))+" magic="+repr(b[:8]))
  if not(len(b)>5000 and b[:4]==b"glTF" and struct.unpack_from("<I",b,8)[0]==len(b)):
   tmp.unlink(missing_ok=True)
 except Exception as e:evt("DOWNLOAD_ERROR "+repr(e))
def access_obstacle(p):
 s=(p.locator("body").inner_text(timeout=2000) or "").lower()[:6000]
 return ("checking your browser" in s or "verify you are human" in s or
         "cloudflare ray id" in s or "human check" in s or
         p.locator("iframe[src*='challenges.cloudflare.com']").count()>0 or
         p.locator(".cf-turnstile").count()>0)
with sync_playwright() as sp:
 browser=sp.chromium.launch(headless=True,args=["--disable-dev-shm-usage","--no-sandbox"])
 ctx=browser.new_context(accept_downloads=True,viewport={"width":1440,"height":900})
 ctx.set_default_timeout(6000)
 p=ctx.new_page()
 p.on("download",capture_download)
 def on_response(x):
  try:
   u=urlparse(x.url)
   if u.hostname and any(z in u.hostname for z in ("3daistudio.pro","cgtrader.com")) and len(out["network"])<150:
    out["network"].append({"host":u.hostname,"path":u.path[:120],"status":x.status,"type":x.headers.get("content-type","")[:65]})
  except: pass
 p.on("response",on_response)
 try:
  resp=p.goto("https://3daistudio.pro/",wait_until="domcontentloaded",timeout=42000)
  evt("STUDIO_GOTO_HTTP "+str(resp.status if resp else "none"))
  p.wait_for_timeout(3000)
  screenshot(p,"01_studio_initial")
  (O/"01_studio_controls.json").write_text(json.dumps(controls(p),ensure_ascii=False,indent=2))
  if access_obstacle(p):
   evt("STUDIO_HUMAN_CHECK_PRESENT_NO_BYPASS")
  else:
   try:
    tab=p.get_by_role("button",name=re.compile(r"image\s*to\s*3d",re.I))
    if tab.count():tab.first.click(timeout=4500);evt("CLICK_IMAGE_TO_3D_TAB")
    else: evt("NO_IMAGE_TAB_BUTTON")
   except Exception as e: evt("TAB_ERROR "+repr(e))
   p.wait_for_timeout(1300)
   screenshot(p,"02_image_tab")
   (O/"02_tab_controls.json").write_text(json.dumps(controls(p),ensure_ascii=False,indent=2))
   ins=p.locator("input[type='file']")
   if ins.count():
    try:
     ins.first.set_input_files(str(SOURCE.resolve()),timeout=6000)
     evt("UPLOADED_EXACT_REFERENCE_SHA256 "+EXPECTED)
    except Exception as e:evt("UPLOAD_ERROR "+repr(e))
   else:evt("NO_FILE_INPUT")
   p.wait_for_timeout(2000)
   screenshot(p,"03_after_upload")
   (O/"03_upload_controls.json").write_text(json.dumps(controls(p),ensure_ascii=False,indent=2))
   if access_obstacle(p):
    evt("HUMAN_CHECK_REQUIRED_AFTER_UPLOAD_NO_BYPASS")
   else:
    clicked=False
    for pattern in (r"generate.{0,25}(?:3d|model)",r"(?:create|build|convert).{0,20}3d",r"generate concept",r"generate"):
     buttons=p.get_by_role("button",name=re.compile(pattern,re.I))
     for i in range(min(buttons.count(),5)):
      b=buttons.nth(i)
      try:
       if not b.is_disabled() and b.is_visible():
        b.click(timeout=4000);evt("CLICKED_REAL_BUTTON "+pattern);clicked=True;break
      except Exception as e:evt("BUTTON_CLICK_ERROR "+repr(e))
     if clicked:break
    if not clicked:evt("NO_ENABLED_GENERATE_BUTTON")
    if clicked:
     deadline=time.monotonic()+250
     clicks=set()
     while time.monotonic()<deadline and not tmp.exists():
      p.wait_for_timeout(4500)
      tt=round(time.monotonic()-t0)
      if tt%25<6:screenshot(p,"04_poll_"+str(tt))
      if access_obstacle(p):
       evt("HUMAN_CHECK_INTERVENED_NO_BYPASS");break
      for pattern in (r"confirm.{0,25}(?:image|concept|model)",r"approve",r"make.{0,10}3d",r"start.{0,20}3d",r"download.{0,20}(?:glb|model|3d)"):
       try:
        b=p.get_by_role("button",name=re.compile(pattern,re.I))
        if b.count() and pattern not in clicks and b.first.is_visible() and not b.first.is_disabled():
         b.first.click(timeout=3000);clicks.add(pattern);evt("CLICKED_NEXT_STAGE "+pattern)
       except Exception as e:evt("NEXT_STAGE_CLICK_ERROR "+repr(e))
      # Only follow actual on-page first-party GLB hrefs (never fabricate endpoints).
      for a in p.locator("a[href]").all()[:100]:
       try:
        url=a.get_attribute("href") or ""
        if ".glb" not in url.lower(): continue
        absolute=urljoin(p.url,url)
        host=urlparse(absolute).hostname or ""
        if not (host.endswith("3daistudio.pro")):continue
        b=ctx.request.get(absolute,timeout=22000).body()
        if len(b)>5000 and b[:4]==b"glTF":tmp.write_bytes(b);evt("ACTUAL_FIRST_PARTY_GLB_HREF "+absolute[:150]);break
       except Exception as e:evt("ACTUAL_HREF_ERROR "+repr(e))
     evt("STUDIO_GENERATION_OBSERVATION_DONE")
   (O/"04_final_controls.json").write_text(json.dumps(controls(p),ensure_ascii=False,indent=2))
  screenshot(p,"05_studio_final")
 except Exception as e:
  out["errors"].append("STUDIO "+repr(e))
  (O/"studio_traceback.txt").write_text(traceback.format_exc())
 try:
  second=ctx.new_page()
  second.on("response",on_response)
  r=second.goto(out["secondary"],wait_until="domcontentloaded",timeout=38000)
  evt("ARTIST_SCULPT_HTTP "+str(r.status if r else "none"))
  second.wait_for_timeout(2000)
  screenshot(second,"06_artist_baby_owl_sculpt")
  page_text=second.locator("body").inner_text(timeout=6000)
  out["artist_sculpt_summary"]={"source":"ArtistFrog Free Baby Owl Sculpt (2020)","contains_free":"Free" in page_text,
    "contains_no_ai_licence":"no AI" in page_text,"needs_login_or_checkout":any(x.lower() in page_text.lower() for x in ("Log in","Sign in","Create an account","Add to cart")),
    "button_labels":controls(second),"preview_only_not_art_approved":True}
  evt("ARTIST_SCULPT_SOURCE_VISITED_NO_PAID_OR_LOGIN_BYPASS")
 except Exception as e:
  out["errors"].append("ARTIST "+repr(e))
  (O/"artist_traceback.txt").write_text(traceback.format_exc())
 browser.close()
if tmp.exists():
 try:
  b=tmp.read_bytes()
  out["native_model_sha256"]=hashlib.sha256(b).hexdigest()
  out["native_model_bytes"]=len(b)
  out["native_glb_valid"]=len(b)>12 and b[:4]==b"glTF" and struct.unpack_from("<I",b,4)[0]==2 and struct.unpack_from("<I",b,8)[0]==len(b)
  if out["native_glb_valid"]:
   import trimesh
   s=trimesh.load(str(tmp),force="scene",process=False)
   meshes=[x for x in s.geometry.values() if isinstance(x,trimesh.Trimesh)]
   out["geometry"]={"meshes":len(meshes),"triangles":sum(len(x.faces) for x in meshes),"vertices":sum(len(x.vertices) for x in meshes)}
   registry=json.loads((R/"known_rejected_asset_sha256_registry.json").read_text())
   rejected=json.dumps(registry)
   out["already_rejected_sha"]=out["native_model_sha256"] in rejected
   out["new_glb"]=not out["already_rejected_sha"] and len(meshes)>0
   if out["new_glb"]:
    import vtk
    from PIL import Image,ImageDraw
    win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(500,500)
    importer=vtk.vtkGLTFImporter();importer.SetFileName(str(tmp));importer.SetRenderWindow(win);importer.Update()
    renderer=win.GetRenderers().GetFirstRenderer()
    bounds=renderer.ComputeVisiblePropBounds()
    center=[(bounds[i]+bounds[i+1])/2 for i in (0,2,4)]
    radius=max(bounds[1]-bounds[0],bounds[3]-bounds[2],bounds[5]-bounds[4],0.1)
    cameras={"front":(0,0,1),"right":(1,0,0),"back":(0,0,-1),"left":(-1,0,0),
             "top":(0,1,0),"bottom":(0,-1,0),"quarter":(.7,.4,.7)}
    pictures=[]
    for name,v in cameras.items():
     renderer.SetBackground(.16,.19,.23)
     cam=renderer.GetActiveCamera();cam.SetFocalPoint(*center)
     cam.SetPosition(*(center[i]+radius*3*v[i] for i in range(3)))
     cam.SetViewUp(0,0,-1) if name in ("top","bottom") else cam.SetViewUp(0,1,0)
     cam.ParallelProjectionOn();cam.SetParallelScale(radius*.85)
     renderer.ResetCameraClippingRange();win.Render()
     f=vtk.vtkWindowToImageFilter();f.SetInput(win);f.ReadFrontBufferOff();f.Update()
     path=O/("NATIVE_"+name+".png");w=vtk.vtkPNGWriter();w.SetInputConnection(f.GetOutputPort());w.SetFileName(str(path));w.Write()
     pictures.append(path)
    contact=Image.new("RGB",(1400,760),(27,30,34))
    draw=ImageDraw.Draw(contact)
    for i,path in enumerate(pictures):
     im=Image.open(path).convert("RGB");im.thumbnail((340,340))
     x=(i%4)*350;y=(i//4)*380;contact.paste(im,(x,y));draw.text((x+6,y+344),path.name,fill=(240,240,240))
    contact.save(O/"run200_NATIVE_7_VIEW_CONTACT.png")
    out["real_native_7view"]=True
 except Exception as e:
  out["errors"].append("GLB_VERIFY_OR_NATIVE_RENDER "+repr(e))
  (O/"native_qa_traceback.txt").write_text(traceback.format_exc())
 tmp.unlink(missing_ok=True)
out["final_status"]="NEW_NATIVE_UNREVIEWED_ART_NO_RELEASE" if out["new_glb"] else "NO_NEW_TARGET_GLTF_NO_RELEASE"
out["no_release"]=True
(O/"run200_results.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n")
(O/"NO_RELEASE.flag").write_text(out["final_status"]+"\nNo physical phone QA, no approved cream-down Tyto chick art, no payment.\n")
evt(out["final_status"])
