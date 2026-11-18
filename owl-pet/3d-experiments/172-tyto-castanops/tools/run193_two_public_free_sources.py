#!/usr/bin/env python3
"""Run193 - source-bound free image-to-3D UI experiment, NO_RELEASE.

Try publicly advertised free Upsampler/Stable Fast 3D and 2d-to-3d vercel
(only if legal first-party controls allow proceeding without Turnstile).
Never bypass captcha, subscription, account, tokens, paid credits or rate limits.
Native binary from this specific photo only. No provider sample or faux mesh.
"""
from __future__ import annotations
import hashlib
import json
import pathlib
import re
import struct
import time
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

BASE = pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT = BASE / "research-evidence-run193-TWO-FREE-GENERATORS-NO_RELEASE"
OUT.mkdir(parents=True, exist_ok=True)
SOURCE = BASE / "research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED_SHA = "5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
REGISTRY = BASE / "known_rejected_asset_sha256_registry.json"
SITES = [
  {"name":"upsampler-free-sf3d", "url":"https://upsampler.com/free-image-to-3d-no-signup",
   "generate":r"^(Convert to 3D|Generate 3D Model|Generate 3D|Generate|Create 3D)(?:\b|$)"},
  {"name":"vercel-open-2d3d", "url":"https://2d-to-3d-model.vercel.app/",
   "generate":r"^(Generate 3D Model|Generate 3D|Generate|Convert|Create)(?:\b|$)"},
]
def utc():
    return datetime.now(timezone.utc).isoformat()
def sha(b):
    return hashlib.sha256(b).hexdigest()
def native_glb(b):
    if len(b) < 30 or b[:4] != b"glTF": return False, "not a GLB"
    version, length = struct.unpack_from("<II", b, 4)
    if version != 2 or length != len(b): return False, "invalid v2 length"
    jlen, kind = struct.unpack_from("<II", b, 12)
    if kind != 0x4e4f534a or jlen > len(b)-20: return False, "missing GLB JSON"
    try:
        j = json.loads(b[20:20+jlen])
        prim = sum(len(m.get("primitives", [])) for m in j.get("meshes", []))
        if not prim or not j.get("accessors"): return False, "no real mesh primitives"
        return True, {"meshes":len(j.get("meshes", [])), "primitives":prim,
          "textures":len(j.get("textures", [])), "materials":len(j.get("materials", [])),
          "nodes":len(j.get("nodes", []))}
    except Exception as e: return False, "GLB JSON invalid: " + repr(e)
assert SOURCE.exists(), "actual v3 rightmost owlet reference not found"
photo_hash = sha(SOURCE.read_bytes())
assert photo_hash == EXPECTED_SHA, f"Wrong species/source: {photo_hash}"
rejects = REGISTRY.read_text() if REGISTRY.exists() else ""
res = {"started_utc":utc(), "original_photo":str(SOURCE),
       "source_sha256":photo_hash, "existing_rejected_registry_present":REGISTRY.exists(),
       "sources":[],"quarantined_new_native_glb":0, "charge_usd":0,
       "art_accepted":False,"physical_mobile_gpu_tested":False,"release":False}
t0=time.monotonic()
def stamp(): return round(time.monotonic()-t0,1)
def save_glb(data, site, origin):
    ok, detail=native_glb(data)
    if not ok:return {"outcome":"invalid_format","diagnostic":detail}
    h=sha(data)
    if h in rejects:return {"outcome":"known_rejected","sha256":h}
    if len(data)>100*1024*1024:return {"outcome":"oversize_quarantined_not_saved","bytes":len(data)}
    file=OUT / f"run193_{site}_actual_new_source_QUARANTINED.glb"
    file.write_bytes(data)
    res["quarantined_new_native_glb"]+=1
    return {"outcome":"native_source_bound_unreviewed","sha256":h,
            "bytes":len(data),"origin":origin[:250], "mesh_manifest":detail}
def snapshot(page, tag):
    try:page.screenshot(path=str(OUT/f"{tag}.png"),full_page=True,timeout=13000)
    except Exception as e:print("screenshot error",tag,repr(e),flush=True)
def blocked(text):
    return bool(re.search(r"cloudflare|turnstile|hcaptcha|recaptcha|verify you are human|security challenge|captcha",text,re.I))
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox","--disable-dev-shm-usage"])
    for site in SITES:
        name=site["name"]
        item={"name":name,"url":site["url"],"started":utc(),
              "phase":"initial","frames":[],"events":[],"http":[],"submitted":False,
              "source_uploaded":False,"verified_new_glb":[],"issues":[]}
        res["sources"].append(item)
        ctx=browser.new_context(viewport={"width":1366,"height":900},
                                accept_downloads=True,service_workers="block")
        page=ctx.new_page()
        def record(event,**kw):
            item["events"].append({"t_sec":stamp(),"event":event,**kw})
            print(name,event,json.dumps(kw,ensure_ascii=False)[:450],flush=True)
        def response(resp):
            try:
                if len(item["http"]) < 130:
                    url=resp.url.split("?")[0]
                    if re.search(r"3d|api|model|generate|queue|upload|glb|gpu",url,re.I):
                        item["http"].append({"url":url[:220],"status":resp.status,
                          "method":resp.request.method, "resource":resp.request.resource_type})
                if item["submitted"] and (resp.url.split("?")[0].lower().endswith(".glb") or
                   "model/gltf-binary" in (resp.headers.get("content-type","").lower())):
                    try:
                        b=resp.body()
                        v=save_glb(b,name,resp.url.split("?")[0])
                        item["verified_new_glb"].append(v)
                        record("actual_native_response",**v)
                    except Exception as e:record("native_response_error",error=repr(e)[:280])
            except Exception:pass
        page.on("response",response)
        try:
            page.goto(site["url"],wait_until="domcontentloaded",timeout=44000)
            page.wait_for_timeout(5500) # allow lazy browser widgets to load
            record("loaded",url=page.url,title=page.title())
            snapshot(page,name+"_01_initial")
            body=page.locator("body").inner_text(timeout=12000)
            (OUT/f"{name}_initial_body.txt").write_text(body[:15000])
            if blocked(body):
                item["phase"]="captcha_security_block_no_bypass"
                record("security_challenge_stop")
                continue
            # A remote generator can be embedded in an iframe; inspect real frames.
            frame_list=list(page.frames)
            for frame in frame_list:
                try:
                    item["frames"].append({"url":frame.url[:350],
                      "file_inputs":frame.locator("input[type=file]").count(),
                      "buttons":frame.locator("button").count(),
                      "text":frame.locator("body").inner_text(timeout=3000)[:600]})
                except Exception as e:item["issues"].append("frame-inspection "+repr(e)[:100])
            (OUT/f"{name}_frames.json").write_text(json.dumps(item["frames"],indent=2,ensure_ascii=False))
            # Choose a genuine source-image file input, not provider demo link.
            candidates=[]
            for frame in frame_list:
                try:
                    inputs=frame.locator("input[type=file]")
                    for idx in range(min(inputs.count(),5)):
                        inp=inputs.nth(idx)
                        accept=(inp.get_attribute("accept") or "").lower()
                        if not accept or any(x in accept for x in ("image","png","jpg","jpeg","webp")):
                            candidates.append((frame,inp))
                except Exception:pass
            record("image_file_inputs",count=len(candidates))
            if not candidates:
                item["phase"]="generator_unavailable_no_image_uploader"
                continue
            frame, inp = candidates[-1]
            try:inp.set_input_files(str(SOURCE),timeout=18000)
            except Exception as e:
                item["phase"]="source_upload_failed";record("upload_failed",err=repr(e)[:300])
                continue
            item["source_uploaded"]=True
            record("uploaded_exact_owned_v3_rightmost",sha256=photo_hash,frame=frame.url[:180])
            page.wait_for_timeout(3500)
            snapshot(page,name+"_02_after_upload")
            buttons=[]
            for f in list(page.frames):
                try:
                    for i in range(min(65,f.locator("button").count())):
                        b=f.locator("button").nth(i)
                        buttons.append({"frame":f.url[:200],"text":(b.inner_text(timeout=2000) or "").strip()[:160],
                                        "visible":b.is_visible(),"enabled":b.is_enabled()})
                except Exception:pass
            (OUT/f"{name}_buttons.json").write_text(json.dumps(buttons,indent=2,ensure_ascii=False))
            if blocked(" ".join(x["text"] for x in buttons)+page.locator("body").inner_text()):
                item["phase"]="security_challenge_after_upload_no_bypass";record("challenge_stop")
                continue
            good=[]
            for f in list(page.frames):
                try:
                    matches=f.get_by_role("button",name=re.compile(site["generate"],re.I))
                    for i in range(min(10,matches.count())):
                        b=matches.nth(i)
                        if b.is_visible() and b.is_enabled():good.append((f,b))
                except Exception:pass
            record("real_generate_controls",count=len(good))
            if not good:
                item["phase"]="no_enabled_generation_control"
                continue
            chosen_frame,btn=good[-1]
            label=btn.inner_text(timeout=3000).strip()
            if re.search(r"buy|purchase|pay|subscribe|credit|upgrade",label,re.I):
                item["phase"]="paid_only_no_purchase";record("paid_control_stop",label=label)
                continue
            record("clicking_actual_free_generate",text=label,frame=chosen_frame.url[:160])
            btn.click(timeout=20000)
            item["submitted"]=True
            item["phase"]="submitted_free"
            snapshot(page,name+"_03_submitted")
            # Observe status with bounded wait and only source-bound post-submit downloads.
            for tick in range(19):
                page.wait_for_timeout(7500)
                frame_texts=[]
                for f in list(page.frames):
                    try:frame_texts.append(f.locator("body").inner_text(timeout=2400))
                    except Exception:pass
                whole=" ".join(frame_texts)
                record("poll",step=tick+1,tail=" ".join(whole[-400:].split()))
                if tick in (3,10,18):snapshot(page,name+f"_poll_{tick+1:02d}")
                if re.search(r"insufficient credits|out of credits|pay to|upgrade to|subscribe|rate limit|too many requests",whole,re.I):
                    item["phase"]="auth_quota_or_payment_stop";break
                if blocked(whole):
                    item["phase"]="security_challenge_stop";break
                if re.search(r"generation failed|gpu unavailable|internal server error|upstream error",whole,re.I):
                    item["phase"]="upstream_failed";break
                for f in list(page.frames):
                    try:
                        links=f.locator("a[href*='.glb'],a[download*='.glb']")
                        for j in range(min(3,links.count())):
                            a=links.nth(j)
                            href=a.get_attribute("href") or ""
                            if href.startswith("http"):
                                rr=ctx.request.get(href,timeout=25000)
                                if rr.ok:
                                    v=save_glb(rr.body(),name,href)
                                    item["verified_new_glb"].append(v);record("download_link_checked",**v)
                    except Exception as e:record("link_check_error",error=repr(e)[:220])
                    try:
                        dl=f.get_by_role("button",name=re.compile(r"Download.*GLB|Extract GLB|GLB.*Download",re.I))
                        for j in range(min(2,dl.count())):
                            b=dl.nth(j)
                            if b.is_visible() and b.is_enabled():
                                with page.expect_download(timeout=6500) as D:b.click()
                                temp=OUT/f"{name}_browser_download.tmp"
                                D.value.save_as(str(temp))
                                v=save_glb(temp.read_bytes(),name,"real browser post-submit export")
                                item["verified_new_glb"].append(v);record("browser_download_checked",**v)
                                temp.unlink(missing_ok=True)
                    except PWTimeout:record("download_button_no_file")
                    except Exception as e:record("download_button_error",error=repr(e)[:180])
                # Evaluate both independent sources even when the first returns an unapproved candidate.
            snapshot(page,name+"_04_final")
            if item["phase"]=="submitted_free" and not res["quarantined_new_native_glb"]:
                item["phase"]="submitted_but_no_new_native_export"
        except Exception as e:
            item["phase"]="browser_exception";item["issues"].append(repr(e))
            record("browser_exception",msg=repr(e)[:500])
        finally:
            item["ended"]=utc()
            (OUT/f"{name}_audit.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n")
            ctx.close()
        # Evaluate both independent sources even when the first returns an unapproved candidate.
    browser.close()
res["ended_utc"]=utc()
(OUT/"run193_results.json").write_text(json.dumps(res,ensure_ascii=False,indent=2)+"\n")
(OUT/"NO_RELEASE.flag").write_text("No hero-quality character has been approved. No commercial rights verified. No physical mobile WebGL GPU test. Never ship generated or simple geometry stand-ins.\n")
print("RUN193_RESULT",json.dumps({"sites":[{"name":x["name"],"phase":x["phase"],"submitted":x["submitted"],"source_uploaded":x["source_uploaded"]} for x in res["sources"]],"new_real_glb":res["quarantined_new_native_glb"],"NO_RELEASE":True}),flush=True)
