#!/usr/bin/env python3
"""Run261: one genuine $0 native image->3D attempt; reference crop/alpha-framing ablation.
Only far-right #172 v3 juvenile is used. Fail closed on auth/payment/challenges.
This experiment does not publish a character and cannot establish phone FPS or usage rights.
"""
import hashlib, json, pathlib, struct, shutil, traceback, re, time
from PIL import Image, ImageFilter, ImageOps
from playwright.sync_api import sync_playwright

ROOT=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
ORIGINAL=ROOT/"research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/rightmost_baby_owl_512_rgba.png"
OUT=ROOT/"research-evidence-run261-REAL-TRANSPARENT-ALPHA-FRAMING-NO_RELEASE"
PIN="e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8"
PRIOR_REJECTED={"d5811563a24061587d9fcf737d40f094cbe0bb58e77288ebed9e94ba43378065",
"4b74b8d045b50ad2075ccf262647824e06d1d51e440c7634c864651800a5541e"}
sha=lambda b:hashlib.sha256(b).hexdigest()
def record(name,obj):(OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False,default=str)+"\n")
def glb_info(blob):
    if len(blob)<1024 or blob[:4]!=b"glTF" or struct.unpack_from("<I",blob,8)[0]!=len(blob):
        raise ValueError("Not a complete binary glTF")
    n,tag=struct.unpack_from("<I4s",blob,12)
    if tag!=b"JSON" or n<30:raise ValueError("No valid JSON chunk")
    j=json.loads(blob[20:20+n].decode("utf-8").strip(" \x00"))
    tris=0
    for m in j.get("meshes",[]):
        for p in m.get("primitives",[]):
            if p.get("mode",4)!=4:continue
            idx=p.get("indices")
            a=j.get("accessors",[])
            if idx is not None:tris+=a[idx]["count"]//3
            elif "POSITION" in p.get("attributes",{}):tris+=a[p["attributes"]["POSITION"]]["count"]//3
    if tris<1000:raise ValueError("No sufficient native triangle geometry")
    return dict(sha256=sha(blob),bytes=len(blob),triangles=tris,mesh_count=len(j.get("meshes",[])),
                material_count=len(j.get("materials",[])),texture_count=len(j.get("textures",[])),
                image_count=len(j.get("images",[])),same_as_prior_rejected=sha(blob) in PRIOR_REJECTED)
def generate_framed_reference():
    raw=ORIGINAL.read_bytes()
    assert sha(raw)==PIN, "Original far-right baby source mismatch"
    original=Image.open(ORIGINAL).convert("RGBA")
    assert original.size==(512,512)
    alpha=original.getchannel("A")
    bbox=alpha.point(lambda a:255 if a>=16 else 0).getbbox()
    assert bbox is not None
    # Preserve all visible animal/tree pixels. Only transparent canvas, alpha edge and
    # focal scale change. No invented side/back views, eyes or geometric primitives.
    margin=24
    box=(max(0,bbox[0]-margin),max(0,bbox[1]-margin),
         min(512,bbox[2]+margin),min(512,bbox[3]+margin))
    crop=original.crop(box)
    target_size=768
    scale=min(620/crop.width,620/crop.height)
    resized=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
    new=Image.new("RGBA",(target_size,target_size),(0,0,0,0))
    new.alpha_composite(resized,((target_size-resized.width)//2,(target_size-resized.height)//2))
    output=OUT/"run261_framed_real_rightmost_768_RGBA.png"
    new.save(output)
    original.save(OUT/"run261_original_source_512_RGBA.png")
    return output,dict(original_sha=PIN,original_bbox=bbox,original_crop=box,
                     source_size=list(original.size),framed_size=list(new.size),
                     generated_sha=sha(output.read_bytes()),resize_scale=scale,
                     framing_only=True,synthetic_geometry=False)

def execute():
    OUT.mkdir(parents=True,exist_ok=True)
    source,prep=generate_framed_reference()
    record("run261_reference_preprocess.json",prep)
    state=dict(run=261,started_utc=time.strftime("%FT%TZ",time.gmtime()),
      provider="https://hy3d.dev/",provider_claims_free=True,
      source_original_sha256=PIN,source_submitted_sha256=prep["generated_sha"],
      actual_provider_submit=False,provider_glb_received=False,real_glb_verified=False,
      software_webgl2=False,physical_phone_tested=False,
      art_approved=False,commercial_rights_cleared=False,additional_payment_usd=0,
      quota_or_captcha_bypass=False,release="NO_RELEASE",status="INIT",events=[])
    observed=[]
    try:
      with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,args=["--no-sandbox","--enable-webgl","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
        page=browser.new_page(viewport={"width":1440,"height":930},accept_downloads=True)
        capture_started=[False]
        def maybe(resp):
            if not capture_started[0]:return
            try:
                u=resp.url
                mime=resp.headers.get("content-type","").lower()
                if ".glb" not in u.lower() and "gltf-binary" not in mime and "application/octet-stream" not in mime:return
                if resp.status!=200:return
                b=resp.body()
                if b[:4]==b"glTF":
                    observed.append((u.split("?")[0],b))
                    state["events"].append({"type":"native-response","bytes":len(b),"mime":mime[:100]})
            except Exception as e:state["events"].append({"type":"binary-error","error":str(e)[:180]})
        page.on("response",maybe)
        def screenshot(n):
            page.screenshot(path=str(OUT/n),timeout=25000)
        try:
            resp=page.goto("https://hy3d.dev/",wait_until="domcontentloaded",timeout=80000)
            state["initial_http_status"]=resp.status if resp else None
            page.wait_for_timeout(3000)
            screenshot("run261_actual_browser_initial.png")
            text=page.locator("body").inner_text()
            (OUT/"run261_initial_visible.txt").write_text(text[:9000])
            state["browser_title"]=page.title()
            if (resp and resp.status>=400) or re.search(r"Just a moment|verify you are human|Cloudflare challenge",text,re.I):
                state["status"]="ACCESS_CHALLENGE_NO_BYPASS"
            elif re.search(r"sign in to generate|credit card required|subscription required|payment required",text,re.I):
                state["status"]="AUTH_OR_PAYMENT_GATE"
            elif page.locator("input[type=file]").count()==0:
                state["status"]="NO_VALID_FILE_UPLOAD"
            else:
                page.locator("input[type=file]").first.set_input_files(str(source.resolve()))
                page.wait_for_timeout(1600)
                screenshot("run261_actual_browser_reference_uploaded.png")
                state["reference_uploaded"]=True
                selected=None
                for label in ("Generate","Create 3D","Start"):
                    buttons=page.get_by_role("button",name=re.compile(label,re.I))
                    for i in range(min(6,buttons.count())):
                        b=buttons.nth(i)
                        if b.is_visible() and b.is_enabled() and not re.search(r"pay|upgrade|purchase",b.inner_text(),re.I):
                            selected=b;break
                    if selected is not None:break
                if selected is None:
                    state["status"]="NO_FREE_ENABLED_GENERATE"
                else:
                    capture_started[0]=True
                    state["actual_provider_submit"]=True
                    state["status"]="CLICKED_FREE_GENERATE"
                    state["selected_button"]=selected.inner_text()[:120]
                    selected.click(timeout=22000)
                    start=time.monotonic()
                    while time.monotonic()-start<330:
                        if observed:break
                        visible=page.locator("body").inner_text()
                        (OUT/"run261_actual_browser_progress.txt").write_text(visible[-9500:])
                        if re.search(r"rate limit|quota|daily limit|generation failed|failed to generate|try again later|GPU unavailable|no credits|payment required|sign in to",visible,re.I):
                            state["events"].append({"type":"provider-error-text","detail":visible[-800:]})
                            state["status"]="PROVIDER_QUOTA_OR_ERROR_NO_NATIVE";break
                        link=page.get_by_role("button",name=re.compile(r"download.*(GLB|model|3D)",re.I))
                        if not link.count():link=page.get_by_role("link",name=re.compile(r"download.*(GLB|model|3D)",re.I))
                        for i in range(min(2,link.count())):
                            if link.nth(i).is_visible() and link.nth(i).is_enabled():
                                try:
                                    with page.expect_download(timeout=9000) as download:
                                        link.nth(i).click(timeout=5000)
                                    d=download.value
                                    f=OUT/("run261_download_"+str(i)+pathlib.Path(d.suggested_filename).suffix)
                                    d.save_as(str(f))
                                    observed.append(("actual_browser_download",f.read_bytes()))
                                except Exception as e:state["events"].append({"type":"download-warning","error":str(e)[:170]})
                        if observed:break
                        page.wait_for_timeout(6500)
                    state["elapsed_generation_wait_sec"]=round(time.monotonic()-start,1)
                    if not observed and state["status"]=="CLICKED_FREE_GENERATE":state["status"]="NO_GLB_WITHIN_WAIT_WINDOW"
            screenshot("run261_actual_browser_final.png")
            (OUT/"run261_final_visible.txt").write_text(page.locator("body").inner_text()[:10000])
            for u,b in observed:
                try:
                    info=glb_info(b)
                    if info["same_as_prior_rejected"]:
                        state["events"].append({"type":"identical-prior-rejected-glb","sha256":info["sha256"]})
                    else:
                        dest=OUT/"run261_real_provider_NATIVE_ART_UNAPPROVED.glb"
                        dest.write_bytes(b)
                        state["provider_glb_received"]=True
                        state["real_glb_verified"]=True
                        state["status"]="REAL_NATIVE_GLB_REQUIRES_ART_REVIEW"
                        state["verified_glb"]=info
                        state["binary_response_origin"]=u[:180]
                        break
                except Exception as e:state["events"].append({"type":"rejected-binary","error":str(e)[:240]})
        finally:
            browser.close()
    except Exception as e:
        state["status"]="BROWSER_ERROR"
        (OUT/"run261_browser_error.log").write_text(traceback.format_exc(limit=8))
    state["completed_utc"]=time.strftime("%FT%TZ",time.gmtime())
    record("run261_machine_report.json",state)
    print("RUN261_EVIDENCE_ONLY",json.dumps(state,ensure_ascii=False))
if __name__=="__main__": execute()
