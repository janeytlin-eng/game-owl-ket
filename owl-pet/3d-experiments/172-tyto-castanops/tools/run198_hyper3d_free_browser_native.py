#!/usr/bin/env python3
"""Run198: one bona fide no-fee public image-to-3D UI attempt; no CAPTCHA bypass.
This script does not infer a 3D asset from images or previews.
"""
import asyncio, hashlib, json, os, re, struct, time, traceback
from pathlib import Path
from urllib.parse import urlparse
from playwright.async_api import async_playwright

ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
O=ROOT/"research-evidence-run198-HYPER3D-REAL-NATIVE-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
PHOTO=ROOT/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
URL="https://hyper3d.site/en"
RESULT={
 "run":198,"source":URL,"cost_paid_usd":0,"no_login":True,
 "challenge_bypass":False,"source_image_sha256":hashlib.sha256(PHOTO.read_bytes()).hexdigest(),
 "result":"UNSTARTED","upload":False,"submission":False,
 "new_valid_glb":False,"art_approved":False,"real_phone_gpu_approved":False,
 "no_release":True,"status_samples":[],"network_samples":[],"errors":[],
 "binary_candidates":[],"browser_screenshots":[]}
assert RESULT["source_image_sha256"]==EXPECTED

def save_json():
    (O/"run198_result.json").write_text(json.dumps(RESULT,indent=2,ensure_ascii=False)+"\n")
def record_status(s):
    if len(RESULT["status_samples"])<35:
        RESULT["status_samples"].append({"t":round(time.time(),3),"text":s[:900]})
def valid_glb(b):
    return len(b)>32 and b[:4]==b"glTF" and struct.unpack_from("<I",b,4)[0]==2 and struct.unpack_from("<I",b,8)[0]==len(b)
def store_candidate(data,url,kind):
    if len(data)>70_000_000: return
    sha=hashlib.sha256(data).hexdigest()
    rec={"sha256":sha,"bytes":len(data),"source_url":url[:400],"kind":kind,"valid_glb":valid_glb(data)}
    if not any(x["sha256"]==sha for x in RESULT["binary_candidates"]):
        RESULT["binary_candidates"].append(rec)
        if rec["valid_glb"]:
            known=ROOT/"known_rejected_asset_sha256_registry.json"
            registry=known.read_text(errors="replace") if known.exists() else ""
            if sha.lower() in registry.lower():
                rec["already_rejected_sha256"]=True
                (O/"run198_duplicate_rejected_source.glb").write_bytes(data)
            elif RESULT["upload"] and RESULT["submission"]:
                try:
                    import trimesh
                    mesh=trimesh.load(file_obj=__import__("io").BytesIO(data),file_type="glb",force="scene")
                    geometries=len(getattr(mesh,"geometry",{}))
                    rec["trimesh_geometry_count"]=geometries
                    if geometries>0:
                        (O/"run198_NEW_UNREVIEWED_NATIVE.glb").write_bytes(data)
                        RESULT["new_valid_glb"]=True
                    else: rec["geometry_error"]="No geometry"
                except Exception as ex: rec["geometry_error"]=repr(ex)
        return rec
async def screenshot(page,label):
    try:
        p=O/("run198_"+label+".png")
        await page.screenshot(path=str(p),full_page=True,timeout=16000)
        RESULT["browser_screenshots"].append(p.name)
    except Exception as ex: RESULT["errors"].append("screenshot "+label+": "+repr(ex))
async def snapshot(page,label):
    try:
        txt=(await page.locator("body").inner_text(timeout=15000))[:11000]
        (O/("run198_"+label+"_body.txt")).write_text(txt)
        record_status(label+": "+txt[:800])
    except Exception as ex: RESULT["errors"].append("body "+label+": "+repr(ex))
async def main():
    responses=[]
    saved_downloads=[]
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,args=["--disable-dev-shm-usage"])
        context=await browser.new_context(viewport={"width":1280,"height":900},
                                          accept_downloads=True,locale="en-US")
        page=await context.new_page()
        page.on("pageerror",lambda e:RESULT["errors"].append("pageerror "+str(e)[:300]))
        def on_response(response):
            try:
                ct=response.headers.get("content-type","")
                url=response.url
                if len(RESULT["network_samples"])<120 and (
                  "api" in url or "model" in url or "generate" in url or
                  "glb" in url or response.status>=400):
                    RESULT["network_samples"].append({
                        "status":response.status,"url":url[:250],"content_type":ct[:100]})
                if response.status==200 and (
                  ".glb" in urlparse(url).path.lower() or "model/gltf-binary" in ct.lower()):
                    responses.append(response)
            except Exception as ex:RESULT["errors"].append("network "+repr(ex))
        page.on("response",on_response)
        def on_download(d):
            saved_downloads.append(d)
        page.on("download",on_download)
        try:
            response=await page.goto(URL,wait_until="domcontentloaded",timeout=45000)
            RESULT["initial_http_status"]=response.status if response else None
            await page.wait_for_timeout(6500)
            RESULT["title"]=await page.title()
            await screenshot(page,"start")
            await snapshot(page,"start")
            html=(await page.content()).lower()
            (O/"run198_initial_dom_excerpt.txt").write_text(html[:30000])
            if RESULT["initial_http_status"] in (403,429,503,530) or "just a moment" in RESULT["title"].lower():
                RESULT["result"]="BLOCKED_HTTP_OR_SECURITY_CHALLENGE";return
            challenge=await page.locator("iframe[src*='challenges.cloudflare.com'],iframe[src*='turnstile']").count()
            if challenge:
                await page.wait_for_timeout(8000)
                challenge=await page.locator("iframe[src*='challenges.cloudflare.com'],iframe[src*='turnstile']").count()
                RESULT["turnstile_iframe_count"]=challenge
                if challenge:
                    RESULT["result"]="TURNSTILE_PRESENT_UNSOLVED_NO_BYPASS";return
            inputs=page.locator("input[type='file']")
            RESULT["file_input_count"]=await inputs.count()
            if not RESULT["file_input_count"]:
                RESULT["result"]="NO_ACTUAL_FILE_INPUT";return
            await inputs.first.set_input_files(str(PHOTO))
            RESULT["upload"]=True
            await page.wait_for_timeout(2500)
            await screenshot(page,"after_upload")
            await snapshot(page,"after_upload")
            txt=(await page.locator("body").inner_text()).lower()
            if "buy credit" in txt or "payment required" in txt or "upgrade to generate" in txt:
                RESULT["result"]="PAID_WALL_NO_CHARGE";return
            # Explicitly click the true in-workbench Generate control, not homepage CTA.
            buttons=page.get_by_role("button",name=re.compile(r"(generate\s*(3d\s*)?(model)?|create\s*3d)",re.I))
            names=[]
            for idx in range(min(await buttons.count(),15)):
                b=buttons.nth(idx)
                names.append({"name":(await b.inner_text())[:150],"enabled":await b.is_enabled(),
                              "visible":await b.is_visible()})
            RESULT["generate_buttons"]=names
            picked=None
            for idx in range(min(await buttons.count(),15)):
                b=buttons.nth(idx)
                if await b.is_visible() and await b.is_enabled():
                    picked=b
                    break
            if picked is None:
                RESULT["result"]="NO_ENABLED_GENERATE_CONTROL";return
            await picked.click(timeout=15000)
            RESULT["submission"]=True
            RESULT["submit_epoch_seconds"]=round(time.time(),3)
            await snapshot(page,"after_click")
            await screenshot(page,"after_click")
            for i in range(26):
                await page.wait_for_timeout(5800)
                if i in (3,10,20,25):
                    await snapshot(page,"poll_"+str(i))
                    await screenshot(page,"poll_"+str(i))
                body=(await page.locator("body").inner_text(timeout=15000)).lower()
                if any(x in body for x in ["upgrade your plan","payment details required","purchase credits"]):
                    RESULT["result"]="PAID_WALL_AFTER_SUBMISSION_NO_CHARGE";break
                if not RESULT["new_valid_glb"]:
                    for d in list(saved_downloads):
                        try:
                            path=await d.path()
                            if path and Path(path).is_file():
                                data=Path(path).read_bytes()
                                store_candidate(data,d.url,"download-event")
                                saved_downloads.remove(d)
                        except Exception as ex:RESULT["errors"].append("download "+repr(ex))
                    for response in list(responses):
                        try:
                            data=await response.body()
                            store_candidate(data,response.url,"network-response")
                            responses.remove(response)
                        except Exception as ex:RESULT["errors"].append("responsebody "+repr(ex))
                if RESULT["new_valid_glb"]:break
                # Only fetch links added after actual submission.
                if i in (7,17,24):
                    anchors=await page.locator("a[href*='.glb']").all()
                    for a in anchors[:6]:
                        try:
                            href=await a.get_attribute("href")
                            if href and href.startswith("http"):
                                res=await context.request.get(href,timeout=14000)
                                if res.ok:store_candidate(await res.body(),href,"post-submit-link")
                        except Exception as ex:RESULT["errors"].append("link "+repr(ex))
            if RESULT["new_valid_glb"]:
                RESULT["result"]="NEW_NATIVE_GLB_UNREVIEWED_NO_RELEASE"
            elif RESULT["result"]=="UNSTARTED":
                RESULT["result"]="NO_NEW_DOWNLOADABLE_NATIVE_GLB_AFTER_ACTUAL_UI_SUBMISSION"
            await snapshot(page,"final")
            await screenshot(page,"final")
        except Exception as ex:
            RESULT["result"]="BROWSER_EXCEPTION"
            RESULT["errors"].append(repr(ex))
            (O/"run198_traceback.txt").write_text(traceback.format_exc())
        finally:
            save_json()
            await browser.close()
try:
    asyncio.run(main())
finally:
    save_json()
print(json.dumps({"result":RESULT["result"],"uploaded":RESULT["upload"],
                  "submitted":RESULT["submission"],"new_valid_glb":RESULT["new_valid_glb"],
                  "candidates":RESULT["binary_candidates"],"errors":RESULT["errors"][:4]},
                  ensure_ascii=False),flush=True)
