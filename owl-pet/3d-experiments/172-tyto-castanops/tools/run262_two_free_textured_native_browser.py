#!/usr/bin/env python3
"""Run262: genuine source-bound zero-extra-cost textured image->3D experiments.
No automated CAPTCHA solving, signup, payment, credit top-up or fake 3D.
Only actual binary glTF model gets to the WebGL validation workflow.
"""
import hashlib, json, os, pathlib, re, struct, time, traceback
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
SOURCE=ROOT/"research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/rightmost_baby_owl_512_rgba.png"
OUT=ROOT/"research-evidence-run262-REAL-TEXTURED-FREE-BROWSER-NO_RELEASE"
PIN="e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8"
PROVIDERS=[
  {"id":"image_to_3d_app","url":"https://image-to-3d.app/","button":r"Generate 3D model|Generate 3D|Generate Model"},
  {"id":"supavoxel","url":"https://supavoxel.com/","button":r"Start Creating|Generate 3D Model|Generate 3D|Create 3D"},
]
REJECTED={"318a4c76986aca0f453fd1a07b60a103f0864656e0f60167b42c4995932e31df",
 "e3c33c70a8a1136a7548d22d2a272e9c5c254e773959b7705d5261ed0fec4535",
 "d5811563a24061587d9fcf737d40f094cbe0bb58e77288ebed9e94ba43378065"}
sha=lambda b:hashlib.sha256(b).hexdigest()
def dump(path,obj): path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str)+"\n")
def valid_glb(data):
    if len(data)<10000 or data[:4]!=b"glTF" or struct.unpack_from("<I",data,8)[0]!=len(data):
        raise ValueError("Not a complete native GLB")
    n,magic=struct.unpack_from("<I4s",data,12)
    if magic!=b"JSON" or n<30 or 20+n>len(data):raise ValueError("Missing glTF JSON")
    obj=json.loads(data[20:20+n].rstrip(b"\x00 ").decode())
    total=0
    for mesh in obj.get("meshes",[]):
        for prim in mesh.get("primitives",[]):
            if prim.get("mode",4)!=4:continue
            acc=obj["accessors"]
            index=prim.get("indices")
            total+=(acc[index]["count"] if index is not None else acc[prim["attributes"]["POSITION"]]["count"])//3
    if total<1000:raise ValueError("Not a useful 3D triangle mesh")
    return dict(sha256=sha(data),bytes=len(data),native_triangles=total,
      meshes=len(obj.get("meshes",[])),images=len(obj.get("images",[])),
      textures=len(obj.get("textures",[])),materials=len(obj.get("materials",[])),
      prior_rejected_same_bytes=sha(data) in REJECTED)
def safe_text(page):
    try:return page.locator("body").inner_text(timeout=7000)[:16000]
    except Exception:return ""
def redacted(url):
    return str(url).split("?")[0][:180]
def run_one(browser,cfg):
    sid=cfg["id"]; root=OUT/sid;root.mkdir(parents=True,exist_ok=True)
    state=dict(run=262,provider=sid,url=cfg["url"],source_sha256=PIN,
      upload_success=False,provider_submit=False,GLB_received=False,
      usage_rights_cleared=False,free_service_claim_unverified=True,
      no_payment=True,challenge_bypass=False,phone_gpu_tested=False,release="NO_RELEASE",
      status="INIT",events=[],actual_glbs=[])
    page=browser.new_page(viewport={"width":1440,"height":950},accept_downloads=True)
    incoming=[]; downloads=[]; clicked=[False]
    def capture_response(resp):
        if not clicked[0] or resp.status!=200:return
        try:
            mime=resp.headers.get("content-type","").lower()
            if ".glb" not in resp.url.lower() and "gltf-binary" not in mime and "application/octet-stream" not in mime:return
            body=resp.body()
            if body[:4]==b"glTF":
                incoming.append((redacted(resp.url),body))
                state["events"].append({"type":"actual-native-response","size":len(body),"mime":mime[:100]})
        except Exception as e:
            state["events"].append({"type":"capture_exception","message":str(e)[:140]})
    def capture_download(dl):
        try:
            p=root/("browser_download_"+str(len(downloads))+".bin")
            dl.save_as(str(p))
            b=p.read_bytes()
            if b[:4]==b"glTF":downloads.append((redacted(dl.url),b))
            else:state["events"].append({"type":"non_glb_download","bytes":len(b)})
        except Exception as e:state["events"].append({"type":"download_exception","message":str(e)[:160]})
    page.on("response",capture_response)
    page.on("download",capture_download)
    try:
        response=page.goto(cfg["url"],wait_until="domcontentloaded",timeout=85000)
        state["http"]=response.status if response else None
        page.wait_for_timeout(4000)
        page.screenshot(path=str(root/"initial_actual_browser.png"),timeout=24000)
        t=safe_text(page);(root/"initial_visible.txt").write_text(t)
        state["browser_title"]=page.title()
        if (response and response.status>=400) or re.search(r"Just a moment|Checking your browser|Cloudflare challenge|verify you are human|captcha",t,re.I):
            state["status"]="ACCESS_CHALLENGE_NO_BYPASS"
        elif not page.locator("input[type=file]").count():
            state["status"]="NO_REAL_UPLOAD_CONTROL"
        else:
            all_inputs=page.locator("input[type=file]")
            selected=all_inputs.first
            for k in range(min(5,all_inputs.count())):
                x=all_inputs.nth(k)
                if re.search("image|png|jpg|webp",x.get_attribute("accept") or "",re.I):
                    selected=x;break
            selected.set_input_files(str(SOURCE.resolve()),timeout=30000)
            page.wait_for_timeout(3500)
            state["upload_success"]=True
            page.screenshot(path=str(root/"source_uploaded_actual_browser.png"),timeout=24000)
            t=safe_text(page);(root/"after_upload_visible.txt").write_text(t)
            if re.search(r"verify you are human|Cloudflare challenge|complete (the )?captcha|authentication required|subscription required|payment required|card required",t,re.I):
                state["status"]="POST_UPLOAD_ACCESS_GATE"
            else:
                button=None
                candidates=page.get_by_role("button",name=re.compile(cfg["button"],re.I))
                for k in range(min(12,candidates.count())):
                    b=candidates.nth(k)
                    if b.is_visible() and b.is_enabled():
                        name=b.inner_text(timeout=2500)
                        if not re.search(r"subscribe|buy|purchase|upgrade|pay\b|credit card",name,re.I):
                            button=b;break
                if button is None:
                    state["status"]="NO_FREE_ENABLED_GENERATE_CONTROL"
                else:
                    state["selected_visible_button"]=button.inner_text(timeout=3000)[:150]
                    state["provider_submit"]=True
                    clicked[0]=True
                    button.click(timeout=20000)
                    state["status"]="FREE_GENERATE_CLICKED"
                    start=time.monotonic()
                    for i in range(40):
                        if incoming or downloads:break
                        page.wait_for_timeout(6500)
                        t=safe_text(page)
                        if i%3==0:
                            (root/"progress_actual_visible.txt").write_text(t)
                            page.screenshot(path=str(root/"progress_actual_browser.png"),timeout=22000)
                        if re.search(r"out of credits|insufficient credits|payment required|subscribe to download|sign in to continue|daily limit|quota exceeded|rate limit|generation failed|generation error|server error|upgrade to",t,re.I):
                            state["status"]="FREE_QUOTA_OR_PAYMENT_OR_GENERATION_ERROR";break
                        # Download buttons are still real-site controls, not an invented GLB.
                        possible=page.get_by_role("button",name=re.compile(r"download.*(glb|3d|model)",re.I))
                        if possible.count()==0:possible=page.get_by_role("link",name=re.compile(r"download.*(glb|3d|model)",re.I))
                        for k in range(min(3,possible.count())):
                            b=possible.nth(k)
                            if b.is_visible() and b.is_enabled():
                                try:
                                    with page.expect_download(timeout=7000) as event:
                                        b.click(timeout=3500)
                                    obj=event.value
                                    dst=root/("direct_download_"+str(k)+".bin")
                                    obj.save_as(str(dst))
                                    val=dst.read_bytes()
                                    if val[:4]==b"glTF":downloads.append(("actual-browser-download",val))
                                except Exception as e:state["events"].append({"type":"download_control_warning","details":str(e)[:200]})
                        if incoming or downloads:break
                    state["generation_wait_seconds"]=round(time.monotonic()-start,1)
                    if state["status"]=="FREE_GENERATE_CLICKED" and not incoming and not downloads:
                        state["status"]="NO_NATIVE_GLB_WITHIN_BOUNDED_WINDOW"
        page.screenshot(path=str(root/"final_actual_browser.png"),timeout=25000)
        (root/"final_visible.txt").write_text(safe_text(page))
        for idx,(url,b) in enumerate(incoming+downloads):
            try:
                info=valid_glb(b)
                info["response_source"]=url
                if info["prior_rejected_same_bytes"]:continue
                path=root/("run262_"+sid+"_"+str(idx)+"_NATIVE_ART_UNAPPROVED.glb")
                path.write_bytes(b)
                state["GLB_received"]=True
                state["actual_glbs"].append(dict(info,path=str(path)))
            except Exception as e:state["events"].append({"type":"rejected_payload","why":str(e)[:180]})
        if state["GLB_received"]:state["status"]="NEW_REAL_NATIVE_GLB_AWAITING_MULTIVIEW_ART_REVIEW"
    except Exception as e:
        state["status"]="BROWSER_EXCEPTION_NO_RELEASE"
        state["error"]=str(e)[:400]
        (root/"exception.log").write_text(traceback.format_exc(limit=7))
    finally:
        dump(root/"machine_report.json",state)
        page.close()
    return state
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    data=SOURCE.read_bytes()
    assert sha(data)==PIN, "Wrong #172 v3 rightmost infant source"
    im=Image.open(SOURCE).convert("RGBA")
    assert im.size==(512,512)
    report={"source_sha256":PIN,"source_dimensions":list(im.size),
      "source_role":"actual v3 RIGHTMOST cream juvenile and eucalyptus hollow only",
      "additional_external_payment_usd":0,"provider_trials":[],"release":"NO_RELEASE"}
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,args=["--no-sandbox","--enable-webgl","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
        for cfg in PROVIDERS:
            try:report["provider_trials"].append(run_one(browser,cfg))
            except Exception as e:report["provider_trials"].append({"provider":cfg["id"],"error":str(e)[:300]})
        browser.close()
    dump(OUT/"run262_aggregate_report.json",report)
    print("RUN262_TRUE_UI_SOURCE_BOUND",json.dumps({p.get("provider"):p.get("status") for p in report["provider_trials"]},ensure_ascii=False))
if __name__=="__main__":main()
