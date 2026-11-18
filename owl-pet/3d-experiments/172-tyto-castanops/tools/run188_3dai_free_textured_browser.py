#!/usr/bin/env python3
"""Run188: one UI-bound no-fee image-to-textured-GLB attempt, no art release.
Not bulk scraping; never use payable plans, demos or off-source model urls.
"""
import hashlib
import json
import pathlib
import re
import struct
import time
from datetime import datetime,timezone
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run188-3DAI-TEXTURED-REAL-UI-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
SOURCE=R/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
d={"utc":datetime.now(timezone.utc).isoformat(),"site":"https://3dai.dev/en","source":str(SOURCE),
   "source_sha256":hashlib.sha256(SOURCE.read_bytes()).hexdigest() if SOURCE.exists() else "MISSING",
   "expected_sha256":EXPECTED,"upload_success":False,"generate_clicked":False,"glb_count":0,
   "no_paid_tools":True,"release":False,"mobile_gpu_tested":False,"events":[],"http":[]}
if d["source_sha256"] != EXPECTED:
    d["fatal"]="SOURCE_HASH_FAIL"
    (O/"run188_results.json").write_text(json.dumps(d,indent=2))
    raise SystemExit("Refuse non-target source")
def event(name,**detail):
    info={"sec":round(time.monotonic()-start,2),"name":name,**detail}
    d["events"].append(info)
    print(json.dumps(info,ensure_ascii=False),flush=True)
def validate_glb(data):
    if len(data)<20 or data[:4]!=b"glTF":
        return False
    ver, length=struct.unpack_from("<II",data,4)
    return ver==2 and len(data)==length
start=time.monotonic()
browser=None
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,args=["--no-sandbox","--disable-dev-shm-usage"])
        ctx=browser.new_context(viewport={"width":1365,"height":900},accept_downloads=True)
        page=ctx.new_page()
        def response(resp):
            if len(d["http"])>=100:
                return
            u=resp.url
            if re.search(r"3dai\.dev|huggingface|gradio|\/api\/",u,re.I):
                d["http"].append({"status":resp.status,"method":resp.request.method,"url":u.split("?")[0][:220],
                                  "kind":resp.request.resource_type})
        page.on("response",response)
        page.goto("https://3dai.dev/en",wait_until="domcontentloaded",timeout=45000)
        page.wait_for_timeout(2500)
        (O/"run188_page_title.txt").write_text(page.title()+"\n"+page.url+"\n")
        page.screenshot(path=str(O/"run188_01_initial.png"),full_page=True,timeout=15000)
        ins=page.locator('input[type="file"]')
        n=ins.count()
        event("file_inputs_detected",n=n)
        (O/"run188_inputs.txt").write_text("\n".join(ins.nth(i).evaluate("(el)=>el.outerHTML.slice(0,1000)") for i in range(n)))
        if not n:
            event("no_upload_input")
        else:
            f=ins.first
            f.set_input_files(str(SOURCE),timeout=12000)
            page.wait_for_timeout(3500)
            d["upload_success"]=True
            event("actual_reference_file_selected",sha256=EXPECTED)
            page.screenshot(path=str(O/"run188_02_uploaded.png"),full_page=True,timeout=15000)
            bs=page.locator("button")
            bstate=[]
            for i in range(min(bs.count(),35)):
                b=bs.nth(i)
                bstate.append({"text":(b.inner_text(timeout=1500) or "").strip()[:90],
                               "enabled":b.is_enabled(),"visible":b.is_visible()})
            (O/"run188_button_state.json").write_text(json.dumps(bstate,indent=2))
            candidates=page.get_by_role("button",name=re.compile(r"Generate\s+(?:textured\s+)?3D",re.I))
            event("generation_button_candidates",n=candidates.count())
            clicked=False
            for i in range(candidates.count()):
                b=candidates.nth(i)
                if b.is_visible() and b.is_enabled() and "textured" in b.inner_text().lower():
                    b.click(timeout=12000)
                    clicked=True
                    break
            if not clicked:
                event("textured_submit_unavailable")
            else:
                d["generate_clicked"]=True
                event("actual_textured_submit_clicked")
                page.wait_for_timeout(1500)
                page.screenshot(path=str(O/"run188_03_after_submit.png"),full_page=True,timeout=15000)
                for step in range(24):
                    page.wait_for_timeout(10000)
                    txt=page.locator("body").inner_text(timeout=8000)
                    # Store only progress snippets, never infer completion from marketing text.
                    excerpt=" ".join(txt[-900:].split())
                    event("live_poll",step=step+1,excerpt=excerpt[-430:])
                    if step in (2,10,23):
                        page.screenshot(path=str(O/f"run188_poll_{step+1:02d}.png"),full_page=True,timeout=15000)
                    has_error=bool(re.search(r"Generation failed|Try another image|Out of credits|Pay to|Sign in to download",txt,re.I))
                    if has_error:
                        event("possible_visible_error_or_paywall")
                        break
                    # Download only after click with source proven and from this live session.
                    links=page.locator("a[href$='.glb'],a[download$='.glb']")
                    if links.count()>0:
                        event("native_glb_links_found",count=links.count())
                        for j in range(min(links.count(),2)):
                            href=links.nth(j).get_attribute("href") or ""
                            if href.startswith("http") and re.match(r"https://",href):
                                rsp=ctx.request.get(href,timeout=30000)
                                bb=rsp.body()
                                if rsp.ok and validate_glb(bb):
                                    sha=hashlib.sha256(bb).hexdigest()
                                    (O/f"run188_source_bound_native_{j+1:02d}_UNREVIEWED.glb").write_bytes(bb)
                                    d["glb_count"]+=1
                                    d["native_glb"]={"url":href,"bytes":len(bb),"sha256":sha}
                                    event("actual_native_glb_downloaded",sha256=sha,bytes=len(bb))
                                    break
                    if not d["glb_count"]:
                        btns=page.get_by_role("button",name=re.compile(r"Download.*GLB|GLB.*Download",re.I))
                        if btns.count()>0 and btns.first.is_visible() and btns.first.is_enabled():
                            try:
                                with page.expect_download(timeout=5000) as dl:
                                    btns.first.click()
                                downloaded=dl.value
                                dest=O/"run188_source_bound_native_button_UNREVIEWED.glb"
                                downloaded.save_as(str(dest))
                                bb=dest.read_bytes()
                                if validate_glb(bb):
                                    sha=hashlib.sha256(bb).hexdigest()
                                    d["glb_count"]+=1
                                    d["native_glb"]={"bytes":len(bb),"sha256":sha,"from":"browser download"}
                                    event("actual_button_glb_downloaded",sha256=sha,bytes=len(bb))
                                else:
                                    dest.unlink()
                                    event("invalid_download_not_glb")
                            except PlaywrightTimeout:
                                event("download_button_no_real_file")
                    if d["glb_count"]:
                        break
                try:
                    page.screenshot(path=str(O/"run188_04_final.png"),full_page=True,timeout=15000)
                except Exception as e:
                    event("final_screenshot_error",error=repr(e)[:160])
        ctx.close()
        browser.close()
except Exception as exc:
    d["exception"]=repr(exc)
    print("RUN188_EXCEPTION",repr(exc),flush=True)
finally:
    (O/"run188_results.json").write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n")
    (O/"NO_RELEASE.flag").write_text("Run188: no accepted art or physical mobile test; source-conditioned native outputs are UNREVIEWED.\n")
    print("RUN188_FINAL",json.dumps({"uploaded":d["upload_success"],"clicked":d["generate_clicked"],
          "real_glbs":d["glb_count"],"release":False}),flush=True)
