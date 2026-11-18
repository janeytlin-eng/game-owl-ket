#!/usr/bin/env python3
"""#172 Run156: actual no-login/no-payment browser generation tests.
Never defeat access verification, register, call undocumented provider APIs,
or mistake a site's preloaded sample viewer for the generated result.
"""
import hashlib, json, pathlib, struct, time, traceback, re, os
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

ROOT=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=ROOT/"research-evidence-run156-TWO-ANONYMOUS-3D-NO_RELEASE"
OUT.mkdir(parents=True, exist_ok=True)
SOURCE=ROOT/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
PROVIDERS=[
 ("sculptly_first_preview","https://sculptly3d.com/image-to-3d-model-free"),
 ("imagetod_retry","https://image-to-3d.app/")
]
def sha(bs): return hashlib.sha256(bs).hexdigest()
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False,default=str))
def glb(b):
    a={"bytes":len(b),"sha256":sha(b),"is_valid_glb":False}
    if len(b)<28 or b[:4]!=b"glTF":return a
    _,ver,size=struct.unpack_from("<4sII",b,0)
    a.update({"version":ver,"declared_bytes":size})
    if ver!=2 or size!=len(b):return a
    nchunk,kind=struct.unpack_from("<II",b,12)
    if kind!=0x4e4f534a or nchunk+20>len(b):return a
    try:
        j=json.loads(b[20:20+nchunk].decode("utf8").rstrip(" \x00"))
        a.update({"is_valid_glb":True,"meshes":len(j.get("meshes",[])),
          "images":len(j.get("images",[])),"materials":len(j.get("materials",[])),
          "animations":len(j.get("animations",[]))})
    except Exception as e:a["json_error"]=str(e)
    return a
def safe_txt(page):
    try: return page.locator("body").inner_text(timeout=10000)[-8000:]
    except Exception as e:return "BODY_ERROR "+repr(e)
def screenshot(page,name):
    try:page.screenshot(path=str(OUT/name),full_page=False,timeout=15000)
    except Exception as e:(OUT/(name+".error.txt")).write_text(str(e))
def run():
    for file in ["owl-pet/AGENTS.md","owl-pet/README.md","owl-pet/prototype/index.html",
       "owl-pet/research/species/172-tyto-castanops-v3.md",
       str(ROOT/"known_rejected_asset_sha256_registry.json"),
       str(ROOT/"2026-11-18-run155-actual-free-cc0-juvenile-model-source-probe-NO_RELEASE.md")]:
        if not pathlib.Path(file).is_file():raise RuntimeError("missing preflight "+file)
    if sha(SOURCE.read_bytes())!=EXPECTED:raise RuntimeError("canonical source checksum mismatch")
    rejected=(ROOT/"known_rejected_asset_sha256_registry.json").read_text()
    data={"run":156,"tested_utc":datetime.now(timezone.utc).isoformat(),
       "canonical_image":str(SOURCE),"source_sha256":EXPECTED,
       "policy":"public UI only, zero added fee, no account, no verification bypass",
       "last_run":"Run155 blocked 403 public Meshy; Run154 sculpt/groom art rejected",
       "providers":{},"real_new_valid_glb":[],"payment_usd":0,"final":"NO_RELEASE"}
    save("run156_preflight.json",data)
    with sync_playwright() as play:
        browser=play.chromium.launch(headless=True,args=["--no-sandbox","--disable-dev-shm-usage"])
        for key,url in PROVIDERS:
            record={"public_url":url,"actions":[],"network":[],"downloads":[],"start_utc":datetime.now(timezone.utc).isoformat()}
            data["providers"][key]=record
            ctx=browser.new_context(viewport={"width":1330,"height":875},accept_downloads=True,ignore_https_errors=False)
            page=ctx.new_page()
            page.set_default_timeout(12000)
            def on_resp(response):
                if len(record["network"])>=60:return
                try:
                    u=response.url
                    if re.search(r"\.glb(\?|$)|/generate|/api/(job|generation|3d)|/result",u,re.I):
                        record["network"].append({"status":response.status,"url":u[:180],
                          "content_type":response.headers.get("content-type")})
                except Exception:pass
            page.on("response",on_resp)
            try:
                response=page.goto(url,wait_until="domcontentloaded",timeout=50000)
                page.wait_for_timeout(3500)
                record.update({"initial_http":response.status if response else None,
                     "initial_url":page.url,"title":page.title(),
                     "body_initial":safe_txt(page)[:4500]})
                screenshot(page,key+"_initial.png")
                content=record["body_initial"].lower()
                if "just a moment" in content or "performing security verification" in content:
                    record["status"]="ACCESS_VERIFICATION_NOT_BYPASSED"
                    continue
                file_input=page.locator("input[type=file]")
                record["file_input_count"]=file_input.count()
                if not file_input.count():
                    record["status"]="NO_VISIBLE_FILE_INPUT"
                    continue
                file_input.first.set_input_files(str(SOURCE))
                record["actions"].append("uploaded actual sha256-locked canonical source via public file input")
                page.wait_for_timeout(1800)
                screenshot(page,key+"_uploaded.png")
                record["body_post_upload"]=safe_txt(page)[:3800]
                # Select only an explicitly labelled public generation action, never sign in/pay.
                labels=["Generate 3D model","Generate textured 3D","Generate model","Create model","Generate","Create 3D"]
                button=None
                for label in labels:
                    for role in ("button","link"):
                        loc=page.get_by_role(role,name=label,exact=True)
                        if loc.count():
                            button=loc.first; break
                    if button is not None:break
                if button is None:
                    record["status"]="UPLOAD_ACCEPTED_NO_PUBLIC_GENERATE_CONTROL"
                    continue
                label=button.inner_text(timeout=5000).strip()
                if re.search("sign|log.?in|subscribe|buy|pay|credit card",label,re.I):
                    record["status"]="GENERATION_REQUIRES_ACCOUNT_OR_PAYMENT"
                    continue
                record["generation_control"]=label
                try:
                    button.click(timeout=10000)
                    record["actions"].append("clicked public "+label)
                except Exception as e:
                    record["generation_click_error"]=repr(e)
                    record["status"]="PUBLIC_GENERATION_CLICK_FAILED"
                    continue
                # Observe actual generation on live provider for bounded time, with screenshots.
                for i in range(12):
                    page.wait_for_timeout(9500)
                    txt=safe_txt(page)
                    if i in (0,3,7,11):
                        record["observations_"+str(i)]={"url":page.url,"body_tail":txt[-4000:]}
                        screenshot(page,key+"_after_"+str(i)+".png")
                    if re.search(r"sign in to download|signup to download|unlock.*download|payment required|you.ve used",txt,re.I):
                        record["possible_download_gate"]=txt[-1500:]
                    if re.search(r"generation failed|something went wrong|server error|failed to generate",txt,re.I):
                        record["possible_failure"]=txt[-1500:]
                record["body_final"]=safe_txt(page)[-8000:]
                record["url_final"]=page.url
                # Only provider's visible UI link/button may supply GLB, not preloaded site demo.
                dl_controls=page.get_by_role("button",name=re.compile("download.*(glb|model)|export.*glb",re.I))
                if not dl_controls.count():
                    dl_controls=page.get_by_role("link",name=re.compile("download.*(glb|model)|export.*glb",re.I))
                record["visible_download_controls"]=dl_controls.count()
                if dl_controls.count() and not re.search("sign.?in|checkout|purchase|subscribe",page.url,re.I):
                    try:
                        with page.expect_download(timeout=10000) as ed:
                            dl_controls.first.click(timeout=8000)
                        d=ed.value
                        dest=OUT/(key+"_quarantine.tmp")
                        d.save_as(dest)
                        bits=dest.read_bytes();dest.unlink()
                        info=glb(bits);info["filename"]=d.suggested_filename
                        info["previously_rejected"]=info["sha256"] in rejected
                        record["downloads"].append(info)
                        if info["is_valid_glb"] and not info["previously_rejected"]:
                            name=key+"_new_ui_generated_3d_UNREVIEWED.glb"
                            (OUT/name).write_bytes(bits)
                            data["real_new_valid_glb"].append({"filename":name,**info})
                    except Exception as e:record["download_failure"]=repr(e)
                record["status"]="NEW_VALID_GLBS_RECEIVED" if any(x["is_valid_glb"] and not x["previously_rejected"] for x in record["downloads"]) else "NO_NEW_VALID_DOWNLOAD_NOT_ART_PASSED"
            except Exception as e:
                record["status"]="BROWSER_EXECUTION_ERROR"
                record["error"]=repr(e);record["traceback"]=traceback.format_exc()[-3500:]
                screenshot(page,key+"_error.png")
            finally:
                record["end_utc"]=datetime.now(timezone.utc).isoformat()
                save("run156_actual_results.json",data)
                ctx.close()
        browser.close()
    (OUT/"NO_RELEASE.flag").write_text(
        "ART_UNREVIEWED/NO_RELEASE. Never release without genuine GLB, rights, true 4-angle art review and physical phone WebGL gate.\n")
    save("run156_actual_results.json",data)
    print("RUN156_ACTUAL_RESULT",json.dumps({"providers":{k:r.get("status") for k,r in data["providers"].items()},
         "valid_new_glb_count":len(data["real_new_valid_glb"]),"payment_usd":0}))
if __name__=="__main__":
    try:run()
    except Exception:
        (OUT/"run156_fatal_error.txt").write_text(traceback.format_exc())
        raise
