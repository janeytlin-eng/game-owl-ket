#!/usr/bin/env python3
"""Run189: two independent, original-photo-bound, genuine free image-to-GLB UI tests.
Any output is QUARANTINED until independent native views, art rights and physical mobile QA.
No captcha bypass, no account creation, no purchase/paid credits, no marketing/demo exports.
"""
import hashlib
import json
import pathlib
import re
import struct
import time
import traceback
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

BASE=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=BASE/"research-evidence-run189-TWO-ORIGINAL-IMAGE-FREE-GLB-STRICT-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)
PHOTO=BASE/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
SITES=[
 {"name":"image-to-3d-app","url":"https://image-to-3d.app/","match":r"Generate 3D model|Generate 3D|Create 3D"},
 {"name":"triple3d-ai","url":"https://triple3d.ai/image-to-3d","match":r"Generate 3D Model|Generate 3D"}
]
result={"started_utc":datetime.now(timezone.utc).isoformat(),"photo":str(PHOTO),
        "photo_sha256":hashlib.sha256(PHOTO.read_bytes()).hexdigest() if PHOTO.exists() else "MISSING",
        "expected_sha256":EXPECTED,"sites":[],"release":False,"charge_usd":0,
        "physical_mobile_gpu_tested":False,"art_approved":False,"new_native_glb_count":0}
assert result["photo_sha256"]==EXPECTED,"source mismatch: never substitute another owlet"
REG=BASE/"known_rejected_asset_sha256_registry.json"
reject_text=REG.read_text() if REG.exists() else ""
def hashfile(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def validate_glb(data):
    if len(data)<28 or data[:4]!=b"glTF": return False,"not glTF"
    version,length=struct.unpack_from("<II",data,4)
    if version!=2 or length!=len(data):return False,"bad GLB v2 length"
    chunk_len,chunk_type=struct.unpack_from("<II",data,12)
    if chunk_type!=0x4E4F534A or chunk_len<=0 or chunk_len>len(data)-20:return False,"no JSON chunk"
    try:
        doc=json.loads(data[20:20+chunk_len])
        m=doc.get("meshes",[])
        primitives=sum(len(x.get("primitives",[])) for x in m)
        if not primitives or not doc.get("accessors"):return False,"no actual mesh primitives"
        return True, {"nodes":len(doc.get("nodes",[])),"meshes":len(m),
                      "primitives":primitives,"materials":len(doc.get("materials",[])),
                      "textures":len(doc.get("textures",[]))}
    except Exception as e:return False,"GLB JSON invalid: "+repr(e)
def capture_glb(body,site,index,origin):
    if len(body)>100*1024*1024:return {"status":"too_large"}
    ok,desc=validate_glb(body)
    if not ok:return {"status":"invalid_not_mesh","reason":desc}
    sha=hashlib.sha256(body).hexdigest()
    if sha in reject_text:return {"status":"known_rejected_hash","sha256":sha}
    dest=OUT/f"run189_{site}_new_native_{index:02d}_QUARANTINED_UNREVIEWED.glb"
    dest.write_bytes(body)
    result["new_native_glb_count"]+=1
    return {"status":"new_native_quarantined","sha256":sha,"bytes":len(body),
            "native_structure":desc,"origin":origin}
start=time.monotonic()
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,args=["--no-sandbox","--disable-dev-shm-usage"])
    for spec in SITES:
        site=spec["name"]
        d={"name":site,"url":spec["url"],"phase":"start","submitted":False,
           "upload_success":False,"events":[],"http":[],"new_glb":[],"free_only":True}
        result["sites"].append(d)
        def ev(name,**k):
            record={"at_sec":round(time.monotonic()-start,1),"event":name,**k}
            d["events"].append(record)
            print(site, json.dumps(record,ensure_ascii=False),flush=True)
        ctx=browser.new_context(viewport={"width":1340,"height":900},accept_downloads=True)
        page=ctx.new_page()
        def onresponse(response):
            try:
                u=response.url.split("?")[0]
                if len(d["http"]) < 100 and (re.search(r"3d|model|api|task|upload|queue|generate",u,re.I)):
                    d["http"].append({"url":u[:230],"status":response.status,
                                      "method":response.request.method,"kind":response.request.resource_type})
            except Exception: pass
        page.on("response",onresponse)
        try:
            page.goto(spec["url"],wait_until="domcontentloaded",timeout=45000)
            page.wait_for_timeout(3500)
            (OUT/f"{site}_initial_url.txt").write_text(page.url+"\n"+page.title()+"\n")
            page.screenshot(path=str(OUT/f"{site}_01_initial.png"),full_page=True,timeout=18000)
            doc=page.locator("body").inner_text(timeout=10000)
            (OUT/f"{site}_initial_text.txt").write_text(doc[:9000],encoding="utf-8")
            if re.search(r"security check|cloudflare|verify you are human|captcha|turnstile",doc,re.I):
                ev("captcha_or_antibot_visible_stop_no_bypass")
                d["phase"]="captcha_or_security"
                continue
            files=page.locator('input[type="file"]')
            ev("file_input_count",count=files.count())
            (OUT/f"{site}_inputs.json").write_text(json.dumps([
                files.nth(i).evaluate("(e)=>({html:e.outerHTML.slice(0,1200),accept:e.accept})")
                for i in range(min(files.count(),8))],ensure_ascii=False,indent=2))
            if not files.count():
                ev("no_actual_photo_upload_available")
                d["phase"]="no_uploader"
                continue
            # Select original reference, not a provider sample or promotional model.
            files.first.set_input_files(str(PHOTO),timeout=12000)
            page.wait_for_timeout(2500)
            d["upload_success"]=True
            ev("target_photo_uploaded",sha256=EXPECTED)
            page.screenshot(path=str(OUT/f"{site}_02_uploaded.png"),full_page=True,timeout=18000)
            buttons=page.locator("button")
            stats=[]
            for j in range(min(buttons.count(),65)):
                b=buttons.nth(j)
                try:stats.append({"text":(b.inner_text(timeout=1500) or "").strip()[:110],
                                  "visible":b.is_visible(),"enabled":b.is_enabled()})
                except Exception:pass
            (OUT/f"{site}_button_states.json").write_text(json.dumps(stats,ensure_ascii=False,indent=2))
            ev("button_state_captured",count=len(stats))
            # Do not spend if actual submit exposes payment or non-free credits.
            visible=" ".join((x["text"] or "") for x in stats if x["visible"] and x["enabled"])
            if re.search(r"buy credits|purchase credits|checkout|subscribe to generate",visible,re.I):
                ev("payment_gate_no_purchase")
                d["phase"]="paywall"
                continue
            matched=page.get_by_role("button",name=re.compile(spec["match"],re.I))
            candidates=[]
            for j in range(min(matched.count(),12)):
                b=matched.nth(j)
                try:
                    if b.is_visible() and b.is_enabled(): candidates.append(b)
                except Exception:pass
            ev("live_generation_candidates",count=len(candidates))
            if not candidates:
                d["phase"]="generation_control_unavailable"
                continue
            # Prefer the actual widget submit, not navigation to another site's marketing page.
            b=candidates[-1]
            label=b.inner_text(timeout=3000).strip()
            if re.search(r"buy|purchase|subscribe|upgrade|pay",label,re.I):
                ev("submit_requests_payment_stop",label=label)
                d["phase"]="paywall"
                continue
            ev("submitting_free_target_image",button=label)
            b.click(timeout=15000)
            d["submitted"]=True
            d["phase"]="submitted"
            page.wait_for_timeout(2500)
            page.screenshot(path=str(OUT/f"{site}_03_submitted.png"),full_page=True,timeout=18000)
            # Poll up to 3 minutes each site. Source-bound generated links only.
            for tick in range(18):
                page.wait_for_timeout(10000)
                body=page.locator("body").inner_text(timeout=10000)
                ev("poll",step=tick+1,text=" ".join(body[-600:].split())[-380:])
                if tick in (3,10,17):page.screenshot(path=str(OUT/f"{site}_poll_{tick+1:02d}.png"),full_page=True,timeout=18000)
                if re.search(r"out of credits|purchase credits|pay to download|subscribe to|verification required|too many requests",body,re.I):
                    ev("quota_auth_or_payment_block_stop")
                    d["phase"]="quota_or_auth_block"
                    break
                if re.search(r"Generation failed|Internal Server Error|Something went wrong|GPU unavailable",body,re.I):
                    ev("visible_upstream_generation_error")
                    d["phase"]="upstream_error"
                    break
                # Real generated GLB download link must emerge after submitted.
                anchors=page.locator("a[href*='.glb'],a[download*='.glb']")
                for j in range(min(anchors.count(),3)):
                    anchor=anchors.nth(j)
                    href=anchor.get_attribute("href") or ""
                    if href.startswith("https://"):
                        try:
                            rr=ctx.request.get(href,timeout=22000)
                            if rr.ok:
                                verdict=capture_glb(rr.body(),site,j+1,href.split("?")[0][:260])
                                d["new_glb"].append(verdict)
                                ev("native_link_checked",**verdict)
                                if verdict.get("status")=="new_native_quarantined":break
                        except Exception as e:ev("native_get_error",error=repr(e)[:200])
                if result["new_native_glb_count"]:break
                download_buttons=page.get_by_role("button",name=re.compile(r"Download.*GLB|GLB.*Download",re.I))
                for j in range(min(download_buttons.count(),2)):
                    b=download_buttons.nth(j)
                    if b.is_visible() and b.is_enabled():
                        try:
                            with page.expect_download(timeout=5000) as event:b.click()
                            path=OUT/f"{site}_clicked_download.tmp"
                            event.value.save_as(str(path))
                            verdict=capture_glb(path.read_bytes(),site,j+5,"real browser download after original upload")
                            d["new_glb"].append(verdict)
                            path.unlink(missing_ok=True)
                            ev("native_button_checked",**verdict)
                        except PWTimeout:ev("download_click_produced_no_file")
                        except Exception as e:ev("download_error",error=repr(e)[:200])
                if result["new_native_glb_count"]:break
            try:page.screenshot(path=str(OUT/f"{site}_04_final.png"),full_page=True,timeout=18000)
            except Exception as e:ev("final_screenshot_failed",error=repr(e)[:200])
        except Exception as exc:
            d["phase"]="exception"
            d["exception"]=repr(exc)
            ev("exception",error=repr(exc)[:450])
        finally:
            (OUT/f"{site}_evidence.json").write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n")
            ctx.close()
        if result["new_native_glb_count"]:
            break
    browser.close()
result["ended_utc"]=datetime.now(timezone.utc).isoformat()
(OUT/"run189_results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
(OUT/"NO_RELEASE.flag").write_text("Run189: original-image-bound native 3D must pass six independent views, art review, licence and physical mobile GPU before release; no substitutes.\n")
print("RUN189_FINAL",json.dumps({"new_native_glb_count":result["new_native_glb_count"],
    "sites":[{"name":s["name"],"phase":s["phase"],"upload":s["upload_success"],
              "submitted":s["submitted"]} for s in result["sites"]],"NO_RELEASE":True}),flush=True)
