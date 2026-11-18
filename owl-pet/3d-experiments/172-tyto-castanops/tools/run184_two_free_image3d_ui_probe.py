#!/usr/bin/env python3
"""Run184: actually use two advertised no-signup free image-conditioned 3D UIs.
Only source-bound, genuine downloaded GLB counts. All outcomes remain NO_RELEASE.
"""
import datetime, hashlib, json, pathlib, re, struct, time, traceback
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright

R = pathlib.Path(__file__).resolve().parent.parent
O = R / "research-evidence-run184-TWO-NEW-REAL-IMAGE3D-UI-NO_RELEASE"
O.mkdir(parents=True, exist_ok=True)
REF = R / "research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED = "5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
sha = lambda b: hashlib.sha256(b).hexdigest()
report = {"run":184, "timestamp":datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "verified_source_sha":None, "preflight":{}, "providers":{},
          "no_extra_spend":True, "physical_phone_gpu":"NOT_TESTED",
          "art_quality":"UNREVIEWED", "release":"NO_RELEASE"}
mandatory = [
  pathlib.Path("owl-pet/AGENTS.md"), pathlib.Path("owl-pet/README.md"),
  pathlib.Path("owl-pet/prototype/index.html"),
  pathlib.Path("owl-pet/research/species/172-tyto-castanops-v3.md"),
  R/"2026-11-18-run181-independent-sevenaxis-art-review-ART_REJECTED-NO_RELEASE.md",
  R/"2026-11-18-run182-new-highdetail-cc0-source-native-ART_REJECTED-NO_RELEASE.md",
  R/"2026-11-18-run183-real-free-juvenile-source-transport-NO_RELEASE.md",
  R/"known_rejected_asset_sha256_registry.json",REF]
report["preflight"]={p.name:p.exists() and p.stat().st_size>0 for p in mandatory}
if not all(report["preflight"].values()): raise RuntimeError("MISSING_PREFLIGHT "+str(report["preflight"]))
report["verified_source_sha"]=sha(REF.read_bytes())
assert report["verified_source_sha"]==EXPECTED, "Wrong reference image!"
rejects={item["sha256"] for item in json.loads((R/"known_rejected_asset_sha256_registry.json").read_text())["known_rejected_source_glbs"]}

def glb_metrics(b):
    if b[:4] != b"glTF" or len(b)<20: raise ValueError("NOT_NATIVE_GLB")
    magic,v,total=struct.unpack_from("<4sII",b)
    if v != 2 or total !=len(b):raise ValueError("BAD_GLB_HEADER")
    n,typ=struct.unpack_from("<II",b,12)
    if typ != 0x4e4f534a or n>len(b)-20:raise ValueError("BAD_JSON_CHUNK")
    d=json.loads(b[20:20+n])
    faces=0
    acc=d.get("accessors",[])
    for m in d.get("meshes",[]):
        for p in m.get("primitives",[]):
            if p.get("mode",4)!=4:continue
            idx=p.get("indices")
            if idx is not None: faces+=acc[idx]["count"]//3
            elif "POSITION" in p.get("attributes",{}):faces+=acc[p["attributes"]["POSITION"]]["count"]//3
    return {"meshes":len(d.get("meshes",[])),"triangles":faces,
      "images":len(d.get("images",[])), "textures":len(d.get("textures",[])),
      "materials":len(d.get("materials",[])),
      "animations":len(d.get("animations",[])),
      "rejected_source_sha":sha(b) in rejects}
def dump(label,data):
    (O/f"{label}_state.json").write_text(json.dumps(data,indent=2,ensure_ascii=False,default=str)+"\n")
def excerpt(page):
    try:
        s=page.locator("body").inner_text(timeout=3500)
        return s[-7000:]
    except Exception as e:return "TEXT_ERROR "+repr(e)
def screenshot(page,name):
    try:page.screenshot(path=str(O/name),full_page=False,timeout=10000)
    except Exception as e:print("SCREENSHOT_FAILURE",name,repr(e),flush=True)

def probe(browser,slug,url):
    record={"url":url, "states":[], "network":[], "download":None,
            "output":"NOT_OBTAINED","source_bound":False}
    ctx=browser.new_context(viewport={"width":1365,"height":850},accept_downloads=True,
      locale="en-US",device_scale_factor=1)
    page=ctx.new_page()
    started=time.monotonic()
    def observed_response(response):
        if len(record["network"])>=140:return
        u=urlsplit(response.url)
        if u.hostname and (u.hostname.endswith("trellis2.dev") or u.hostname.endswith("3dai.dev") or response.status>=400):
            record["network"].append({"host":u.hostname,"path":u.path[:200],"status":response.status,
              "content_type":response.headers.get("content-type","")[:100]})
    page.on("response",observed_response)
    try:
        page.goto(url,wait_until="domcontentloaded",timeout=45000)
        page.wait_for_timeout(3500)
        screenshot(page,slug+"_00_initial.png")
        record["states"].append({"t":round(time.monotonic()-started,1),"phase":"initial",
             "title":page.title(),"url":page.url,"body":excerpt(page)})
        file_loc=page.locator('input[type="file"]')
        record["file_input_count"]=file_loc.count()
        if file_loc.count()==0:
            record["output"]="NO_PUBLIC_IMAGE_FILE_INPUT";return record
        file_loc.first.set_input_files(str(REF))
        record["source_bound"]=True
        page.wait_for_timeout(4500)
        screenshot(page,slug+"_01_real_reference_uploaded.png")
        record["states"].append({"t":round(time.monotonic()-started,1),"phase":"uploaded",
              "body":excerpt(page)})
        if slug=="trellis2":
            candidates=page.get_by_role("button",name=re.compile(r"generate",re.I))
        else:
            candidates=page.get_by_role("button",name=re.compile(r"generate",re.I))
        record["generate_buttons"]=[]
        for i in range(min(candidates.count(),12)):
            b=candidates.nth(i)
            record["generate_buttons"].append({"text":(b.inner_text(timeout=3000) or "")[:200],
                 "enabled":b.is_enabled(),"visible":b.is_visible()})
        clicked=False
        for i in range(min(candidates.count(),12)):
            b=candidates.nth(i)
            if b.is_visible() and b.is_enabled():
                b.click(timeout=12000);clicked=True;break
        record["generate_clicked"]=clicked
        if not clicked:
            record["output"]="GENERATE_CONTROL_NOT_ENABLED";return record
        screenshot(page,slug+"_02_after_generation_click.png")
        record["states"].append({"t":round(time.monotonic()-started,1),"phase":"clicked",
             "body":excerpt(page)})
        # Actual asynchronous inference, never use preloaded sample models.
        # Wait up to 175s per provider and inspect the user's generated output UI.
        downloaded=False
        for tick in range(12):
            page.wait_for_timeout(15000)
            body=excerpt(page)
            snapshot={"t":round(time.monotonic()-started,1),"phase":"generation_poll",
                "tick":tick+1,"body":body[-3500:]}
            record["states"].append(snapshot)
            if tick in (1,3,7,11):screenshot(page,slug+f"_03_poll_{tick+1:02d}.png")
            choices=page.get_by_role("button",name=re.compile(r"download|export|save.*glb",re.I))
            links=page.locator('a[download], a[href$=".glb"], a[href*=".glb?"]')
            targets=[choices.nth(i) for i in range(min(choices.count(),10))]+[links.nth(i) for i in range(min(links.count(),10))]
            if targets:
                record["download_controls"]=[]
                for el in targets:
                    try:record["download_controls"].append({"text":el.inner_text(timeout=2000)[:160],
                        "enabled":el.is_enabled(),"visible":el.is_visible()})
                    except Exception:pass
                for el in targets:
                    if not el.is_visible() or not el.is_enabled():continue
                    try:
                        with page.expect_download(timeout=9500) as result:el.click(timeout=9000)
                        download=result.value
                        dest=O/(slug+"_new_UI_generated_UNREVIEWED.glb")
                        download.save_as(str(dest))
                        b=dest.read_bytes()
                        record["download"]={"name":download.suggested_filename,"size":len(b),"sha256":sha(b)}
                        try:
                            record["download"]["gltf"]=glb_metrics(b)
                            record["output"]="VALID_NATIVE_GLB_NEEDS_INDEPENDENT_ART_QA"
                        except Exception as ex:
                            record["download"]["parse_error"]=repr(ex)
                            record["output"]="DOWNLOADED_NON_GLB_OR_BAD_FORMAT"
                        downloaded=True
                        break
                    except Exception as e:
                        record.setdefault("download_attempt_errors",[]).append(repr(e)[:500])
                if downloaded:break
            if re.search(r"quota exceeded|not available|out of credits|sign in to download|server error|generation failed|unavailable",body,re.I):
                record["server_error_observed"]=True
        if not downloaded and record["output"]=="NOT_OBTAINED":record["output"]="NO_GLB_AFTER_FULL_WAIT"
        screenshot(page,slug+"_04_final_ui.png")
        return record
    except Exception as e:
        record["output"]="BROWSER_ERROR"
        record["exception"]=repr(e)
        record["traceback"]=traceback.format_exc()[-3500:]
        screenshot(page,slug+"_error.png")
        return record
    finally:
        record["elapsed_s"]=round(time.monotonic()-started,2)
        (O/(slug+"_final_visible_text.txt")).write_text(excerpt(page))
        try:ctx.close()
        except Exception:pass
        dump(slug,record)

with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,args=["--no-sandbox","--use-gl=angle","--use-angle=swiftshader"])
    try:
        for slug,url in [
          ("trellis2","https://trellis2.dev/"),
          ("3dai","https://3dai.dev/en")
        ]:
            report["providers"][slug]=probe(browser,slug,url)
            print("RUN184_LIVE_PROVIDER",slug,
                  report["providers"][slug].get("output"),flush=True)
    finally:browser.close()
report["valid_glb_count"]=sum(x.get("output")=="VALID_NATIVE_GLB_NEEDS_INDEPENDENT_ART_QA" for x in report["providers"].values())
(O/"run184_results.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
(O/"NO_RELEASE.flag").write_text("Run184: No art or physical mobile acceptance; new GLB if any isolated for QA; zero purchases.\n")
print("RUN184_FINAL",report["valid_glb_count"],"NEW_SOURCE_BOUND_NATIVE_GLBS_NOT_YET_ART_PASSED",flush=True)
