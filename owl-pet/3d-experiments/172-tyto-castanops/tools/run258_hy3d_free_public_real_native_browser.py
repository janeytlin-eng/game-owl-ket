#!/usr/bin/env python3
"""Run258: one honest, $0, browser-operated hy3d.dev image-to-GLB experiment.
Only the real #172 v3 RIGHTMOST cream-down juvenile is submitted.
Never click paid/sign-in/CAPTCHA or treat a screenshot/sample GLB as generation.
All artifacts quarantine-only; no 251-species workflow or production changes.
"""
import hashlib, json, pathlib, re, shutil, struct, sys, time, traceback
from PIL import Image

ROOT=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
SRC=ROOT/"research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/rightmost_baby_owl_512_rgba.png"
OUT=ROOT/"research-evidence-run258-HY3D-FREE-ACTUAL-BROWSER-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)
PIN="e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8"
KNOWN_BAD={"1e86303f2cf5879ced269e90f81969744cfc0b0d3c18b8c188beefdd67aaa09b"}
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(name,data):(OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2,default=str)+"\n")
def timez():return time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
def glb(p):
    b=p.read_bytes()
    if len(b)<1024 or b[:4]!=b"glTF" or struct.unpack_from("<I",b,8)[0]!=len(b):
        raise ValueError("Not a complete binary glTF")
    n,ty=struct.unpack_from("<I4s",b,12)
    if ty!=b"JSON":raise ValueError("Missing JSON chunk")
    d=json.loads(b[20:20+n].decode("utf8").strip(" \x00"))
    ts=sum((d["accessors"][t["indices"]]["count"] if "indices" in t else
      d["accessors"][t["attributes"]["POSITION"]]["count"])//3
      for m in d.get("meshes",[]) for t in m.get("primitives",[]) if t.get("mode",4)==4)
    info=dict(bytes=len(b),sha256=sha(b),real_triangles=ts,meshes=len(d.get("meshes",[])),
      images=len(d.get("images",[])),textures=len(d.get("textures",[])),
      materials=len(d.get("materials",[])),animations=len(d.get("animations",[])),
      prior_rejected_sha=sha(b) in KNOWN_BAD)
    if ts<1000:raise ValueError("Insufficient valid geometry")
    return info
def launch():
    from playwright.sync_api import sync_playwright
    src=SRC.read_bytes()
    assert sha(src)==PIN,"Original RIGHTMOST source identity mismatch"
    im=Image.open(SRC)
    assert im.size==(512,512) and im.mode=="RGBA","Source must be 512 RGBA baby"
    shutil.copy2(SRC,OUT/"run258_RIGHTMOST_source_512_RGBA.png")
    s=dict(run="258",source=str(SRC),source_sha256=PIN,provider="https://hy3d.dev/",
        actual_browser_interaction=False,provider_glb_received=False,
        independent_new_model_verified=False,real_native_views=False,
        browser_webgl2_tested=False,physical_phone_tested=False,
        art_approved=False,rights_cleared=False,additional_payment_usd=0,
        no_account_or_captcha_bypass=True,release="NO_RELEASE",status="PREFLIGHT",
        start=timez(),screens=[],events=[],rejections=[])
    dump("run258_status.json",s)
    try:
      with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,args=[
           "--no-sandbox","--enable-webgl","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
        page=browser.new_page(viewport={"width":1440,"height":930},accept_downloads=True,locale="en-US")
        captured=[]
        submit_started=[False]
        def capture_response(resp):
          if not submit_started[0]:return
          try:
            u=resp.url.lower();mime=resp.headers.get("content-type","").lower()
            if ".glb" not in u and "model/gltf-binary" not in mime and "application/octet-stream" not in mime:
              return
            s["events"].append(dict(event="binary-response",http=resp.status,mime=mime[:90],url=u.split("?")[0][:210]))
            if resp.status!=200 or len(captured)>=4:return
            b=resp.body()
            if len(b)>1024 and b[:4]==b"glTF":
              p=OUT/("run258_generated_response_%d_RESEARCH_ONLY.glb"%len(captured))
              p.write_bytes(b);captured.append(p)
          except Exception as ex:s["events"].append(dict(event="binary-response-exception",error=str(ex)[:190]))
        page.on("response",capture_response)
        def screenshot(name):
          p=OUT/name;page.screenshot(path=str(p),timeout=25000);s["screens"].append(name)
        def visible(name):
          t=page.locator("body").inner_text(timeout=12000)
          (OUT/name).write_text(t[:20000]);return t
        try:
          page.goto("https://hy3d.dev/",wait_until="domcontentloaded",timeout=85000)
          page.wait_for_timeout(3000)
          screenshot("run258_initial_actual_browser.png")
          t=visible("run258_initial_visible.txt")
          s["title"]=page.title()
          s["upload_inputs"]=page.locator("input[type=file]").count()
          if re.search(r"(sign in|log in).*(required|to generate)|subscription required|payment required|generation paused",t,re.I):
            s["status"]="LOGIN_OR_PAYMENT_REQUIRED_NO_CALL"
          elif page.locator("iframe[src*='turnstile'],iframe[src*='captcha'],input[name*='captcha']").count():
            s["status"]="PROTECTED_CHALLENGE_NO_BYPASS"
          elif not s["upload_inputs"]:
            s["status"]="NO_PUBLIC_IMAGE_FILE_INPUT"
          else:
            page.locator("input[type=file]").first.set_input_files(str(SRC.resolve()))
            page.wait_for_timeout(1800)
            s["actual_browser_interaction"]=True
            screenshot("run258_uploaded_actual_reference.png")
            t=visible("run258_after_upload_visible.txt")
            submit=None
            for label in ("Generate", "Create 3D", "Start"):
              b=page.get_by_role("button",name=re.compile(label,re.I))
              for i in range(min(b.count(),8)):
                if b.nth(i).is_visible() and b.nth(i).is_enabled() and not re.search(r"buy|purchase|pay|upgrade",b.nth(i).inner_text(),re.I):
                  submit=b.nth(i);s["chosen_generate_label"]=b.nth(i).inner_text()[:140];break
              if submit:break
            if not submit:
              s["status"]="NO_ENABLED_PUBLIC_FREE_GENERATE_CONTROL"
            else:
              s["status"]="ACTUAL_GENERATION_REQUEST_SUBMITTED"
              submit_started[0]=True
              s["submitted_at"]=timez()
              submit.click(timeout=20000)
              started=time.monotonic()
              while time.monotonic()-started<390:
                if captured:break
                t=visible("run258_progress_visible.txt")
                if re.search(r"(quota|rate limit|daily limit|generation failed|failed to generate|GPU unavailable|internal server error|try again later)",t,re.I):
                  s["events"].append(dict(event="provider-error-visible",text=t[-800:]))
                  s["status"]="PROVIDER_ERROR_NO_MODEL";break
                if re.search(r"sign in to|log in to|buy credits|upgrade to|purchase",t,re.I):
                  s["status"]="ACCOUNT_OR_PAYMENT_GATE_STOP";break
                d=page.get_by_role("button",name=re.compile(r"download.*(GLB|model|3D)|export.*GLB",re.I))
                if not d.count():d=page.get_by_role("link",name=re.compile(r"download.*(GLB|model|3D)|export.*GLB",re.I))
                for i in range(min(d.count(),3)):
                  if d.nth(i).is_visible() and d.nth(i).is_enabled():
                    try:
                      with page.expect_download(timeout=10000) as ev:d.nth(i).click(timeout=5000)
                      dl=ev.value
                      p=OUT/("run258_download_%d"%len(captured)+pathlib.Path(dl.suggested_filename).suffix)
                      dl.save_as(str(p));captured.append(p)
                      s["events"].append(dict(event="actual-download",name=p.name,bytes=p.stat().st_size))
                      break
                    except Exception as ex:
                      s["events"].append(dict(event="download-control-not-ready",detail=str(ex)[:150]))
                if captured:break
                page.wait_for_timeout(7000)
              s["elapsed_wait_sec"]=round(time.monotonic()-started,1)
              if s["status"]=="ACTUAL_GENERATION_REQUEST_SUBMITTED":
                s["status"]="REQUEST_COMPLETED_OR_TIMED_OUT_NO_VERIFIED_GLB"
          for p in captured:
            try:
              info=glb(p)
              s.setdefault("candidate_binaries",[]).append(dict(name=p.name,**info))
              if not info["prior_rejected_sha"]:
                shutil.copyfile(p,OUT/"run258_original_NATIVE_PROVIDER_RESEARCH_ONLY.glb")
                s["verified_glb"]=info;s["provider_glb_received"]=True
                s["independent_new_model_verified"]=True
                s["status"]="NEW_REAL_NATIVE_GLB_ART_UNREVIEWED_NO_RELEASE"
            except Exception as ex:s["rejections"].append(dict(file=p.name,reason=str(ex)[:300]))
        except Exception:
          s["status"]="ACTUAL_BROWSER_ERROR"
          (OUT/"run258_browser_exception.txt").write_text(traceback.format_exc(limit=8))
        finally:
          try:screenshot("run258_final_actual_browser.png")
          except Exception as ex:s["events"].append(dict(event="final-screenshot-fail",error=str(ex)[:150]))
          try:visible("run258_final_visible.txt")
          except Exception:pass
          s["finished"]=timez()
          dump("run258_status.json",s)
          browser.close()
    except Exception:
      s["status"]="BROWSER_SETUP_ERROR"
      (OUT/"run258_setup_exception.txt").write_text(traceback.format_exc(limit=8))
      dump("run258_status.json",s)
    print("RUN258_ACTUAL_FINAL",json.dumps(s,ensure_ascii=False,default=str))
if __name__=="__main__":
    if sys.argv[-1]=="browse":launch()
    else:raise SystemExit("Only browse. Blender QA uses known separate renderer if real GLB.")
