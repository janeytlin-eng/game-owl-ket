#!/usr/bin/env python3
"""Run195: actual no-charge CC0 owl animation donor probe; NEVER publishes a character."""
import hashlib, json, os, re, struct, time, traceback, zipfile
from pathlib import Path
from urllib.parse import urlparse
import requests
ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=ROOT/"research-evidence-run195-CC0-RIGGED-DONOR-ART_UNAPPROVED-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)
SOURCE="https://vuena.itch.io/blocky-pets-free"
BLENDSWAP="https://blendswap.com/blend/7951"
TARGET="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
result={"run":195,"source":SOURCE,"second_source":BLENDSWAP,"price_paid_usd":0,
        "reference_sha256_expected":TARGET,"accepted_as_character":False,
        "mobile_physical_gpu_test":False,"status":"NOT_STARTED",
        "source_claim":"CC0 sample owl, rigged, toy-style, NOT a Tasmanian masked owl nestling"}
(OUT/"NO_RELEASE.flag").write_text("NOT a target-qualified juvenile owl; NEVER integrate or publish.\n")
def record(name, data):
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2,default=str)+"\n")
def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for c in iter(lambda:f.read(1<<20),b""): h.update(c)
    return h.hexdigest()
def info(p):return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p)}
def glb_manifest(p):
    b=p.read_bytes()
    assert len(b)>=20 and b[:4]==b"glTF" and int.from_bytes(b[4:8],"little")==2
    assert int.from_bytes(b[8:12],"little")==len(b)
    n=int.from_bytes(b[12:16],"little")
    assert b[16:20]==b"JSON" and n < len(b)
    g=json.loads(b[20:20+n].decode("utf-8"))
    out={"bytes":len(b),"sha256":sha(p),"mesh_count":len(g.get("meshes",[])),
         "node_count":len(g.get("nodes",[])),"material_count":len(g.get("materials",[])),
         "texture_count":len(g.get("textures",[])),"animation_count":len(g.get("animations",[])),
         "animation_names":[x.get("name","unnamed") for x in g.get("animations",[])],
         "skin_count":len(g.get("skins",[])),
         "triangle_indices_or_unindexed_primitives":len([p for m in g.get("meshes",[]) for p in m.get("primitives",[])])}
    try:
        import trimesh
        scene=trimesh.load(str(p),force="scene",process=False)
        meshes=list(scene.geometry.values())
        out["loaded_meshes"]=len(meshes)
        out["triangles"]=sum(len(m.faces) for m in meshes)
        out["vertices"]=sum(len(m.vertices) for m in meshes)
        out["bounds"]=scene.bounds.tolist() if scene.bounds is not None else None
    except Exception as e: out["trimesh_error"]=str(e)
    return out
try:
    # Verify exact previously approved reference and own repository restrictions.
    src=ROOT/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED"/"rightmost_mesoptile_input.png"
    assert src.exists() and sha(src)==TARGET, "Original #172 v3 reference mismatch"
    result["reference"]=info(src)
    for path in ["owl-pet/README.md","owl-pet/AGENTS.md","owl-pet/prototype/index.html",
                 "owl-pet/research/species/172-tyto-castanops-v3.md",
                 str(ROOT/"known_rejected_asset_sha256_registry.json"),
                 str(ROOT/"2026-11-19-run194-inerscene-exact-known-reject-dedup-NO_RELEASE.md")]:
        assert Path(path).is_file(),path
    registry=json.loads((ROOT/"known_rejected_asset_sha256_registry.json").read_text())
    prior=json.dumps(registry)
    assert SOURCE not in prior, "Refuse repeated known source"
    result["source_preflight_checked"]=True

    # The old feather-groom Blender source is *only* checked for legitimate anonymous access.
    try:
        resp=requests.get(BLENDSWAP,timeout=18,headers={"User-Agent":"Mozilla/5.0"},allow_redirects=True)
        (OUT/"blendswap_response_excerpt.txt").write_text(resp.text[:9000] if "text" in resp.headers.get("Content-Type","") else "non-text")
        result["blendswap_http"]={"status":resp.status_code,
            "content_type":resp.headers.get("Content-Type",""),"final_host":urlparse(resp.url).hostname,
            "bytes":len(resp.content),"public_download_proven":False}
    except Exception as e: result["blendswap_error"]=str(e)

    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,args=["--disable-dev-shm-usage","--no-sandbox"])
        page=browser.new_page(accept_downloads=True,viewport={"width":1280,"height":850},locale="en-US")
        diag={"stages":[],"downloads":[],"page_titles":[]}
        def snap(tag):
            try:
                page.screenshot(path=str(OUT/(tag+".png")),full_page=True,timeout=10000)
                (OUT/(tag+".html")).write_text(page.content()[:150000])
                diag["stages"].append({"tag":tag,"url_host":urlparse(page.url).hostname,"title":page.title(),
                          "body_excerpt":page.locator("body").inner_text(timeout=5000)[:4500]})
            except Exception as e: diag["stages"].append({"tag":tag,"error":str(e)})
        try:
            page.goto(SOURCE,wait_until="domcontentloaded",timeout=45000)
            page.wait_for_timeout(1700); snap("run195_source")
            result["license_text_seen"]="cc0" in page.locator("body").inner_text().lower()
            if not result["license_text_seen"]: raise RuntimeError("Publisher CC0 notice absent; no download permitted")
            # This is a free sample only. Avoid the paid full pack, voluntary payment, login, and paywall.
            btn=page.get_by_text("Download Now",exact=False).first
            if btn.count(): btn.click(timeout=12000)
            else:
                sel=page.locator("a[href*='download']").first
                if sel.count():sel.click(timeout=12000)
            page.wait_for_timeout(1800);snap("run195_after_download_now")
            for label in ["No thanks, just take me to the downloads","No thanks, just take me to downloads",
                          "No thanks, just take me to the downloads page"]:
                button=page.get_by_text(label,exact=False).first
                if button.count() and button.is_visible():
                    button.click(timeout=12000);page.wait_for_timeout(1300)
                    diag["clicked_zero_price_link"]=label
                    break
            snap("run195_free_download_page")
            content=page.locator("body").inner_text()
            result["page_has_free_zip_name"]="Cute-Pets-Wildlife-FREE-Sample-CC0" in content
            # Prefer ZIP link in row naming the explicitly free CC0 sample, reject paid pack.
            cand=page.locator("a:has-text('Download')")
            result["candidate_download_links"]=cand.count()
            extracted=None
            for j in range(min(cand.count(),16)):
                a=cand.nth(j)
                if not a.is_visible():continue
                parent=a.locator("xpath=..")
                parent_text=parent.inner_text(timeout=4000).lower()
                if any(t in parent_text for t in ["full pack","starter","$4.99","buy now"]): continue
                if page.locator("body").get_by_text("Cute-Pets-Wildlife-FREE-Sample",exact=False).count():
                    # Click the zero-price download; never submit any form or checkout.
                    try:
                        with page.expect_download(timeout=18000) as dl:
                            a.click(timeout=7000)
                        download=dl.value
                        fn=download.suggested_filename
                        if not fn.lower().endswith(".zip"):raise RuntimeError("Expected ZIP, got "+fn)
                        dest=OUT/"run195_actual_free_cc0_sample.zip"
                        download.save_as(str(dest))
                        extracted=dest;diag["downloads"].append(info(dest));break
                    except Exception as e:
                        diag["downloads"].append({"attempt":j,"error":str(e)[:250]})
            if not extracted:
                # Explicitly try the visible text 'Download' near a free ZIP entry, still no payment.
                rows=page.locator("text=/Cute-Pets-Wildlife-FREE-Sample-CC0/i")
                diag["free_sample_rows"]=rows.count()
                for j in range(min(rows.count(),4)):
                    anchor=rows.nth(j).locator("xpath=ancestor::*[self::div or self::li][1]").get_by_text("Download",exact=True)
                    if anchor.count():
                        try:
                            with page.expect_download(timeout=15000) as dl:
                                anchor.first.click(timeout=6500)
                            dest=OUT/"run195_actual_free_cc0_sample.zip"
                            dl.value.save_as(str(dest));extracted=dest;diag["downloads"].append(info(dest));break
                        except Exception as e:diag["downloads"].append({"row":j,"error":str(e)[:200]})
            snap("run195_final_browser")
            record("run195_browser_actions.json",diag)
            result["free_zip_acquired"]=bool(extracted)
            if not extracted:result["status"]="SOURCE_ACCESS_OR_UI_BLOCKED"
            else:
                assert zipfile.is_zipfile(extracted)
                with zipfile.ZipFile(extracted) as z:
                    names=z.namelist()
                    record("run195_zip_inventory.json",{"zip":info(extracted),"entries":names[:250]})
                    owls=[n for n in names if n.lower().endswith(".glb") and "owl" in n.lower() and not n.startswith("__MACOSX/")]
                    if not owls:
                        result["status"]="NO_OWL_GLB_IN_VERIFIED_FREE_ZIP"
                    else:
                        manifest=[]
                        known={x.get("sha256") for x in registry.get("known_rejected_source_glbs",[])}
                        for n in owls[:3]:
                            data=z.read(n)
                            if len(data)>30_000_000:continue
                            dest=OUT/("run195_OWL_"+str(len(manifest))+".glb")
                            dest.write_bytes(data)
                            v=glb_manifest(dest)
                            v["zip_entry"]=n
                            v["prior_rejected_binary"]=v["sha256"] in known
                            manifest.append(v)
                        record("run195_native_glb_metrics.json",manifest)
                        result["native_glb"]=manifest
                        result["status"]="REAL_NATIVE_OWL_DONOR_ACQUIRED_ART_REJECTED" if manifest else "NO_VALID_NATIVE_GLB"
        finally: browser.close()
    result["art_verdict"]="ART_REJECTED: source explicitly describes stylized low-poly designer toy owl, not cream down Tyto castanops mesoptile; no true feather sculpt, mask or backed anatomy qualification"
    result["mobile_verdict"]="UNTESTED on physical phone; LOD existence alone not GPU verification"
except Exception as exc:
    result["status"]="EXECUTION_OR_SOURCE_ERROR"
    result["error"]=repr(exc)
    (OUT/"run195_traceback.txt").write_text(traceback.format_exc())
finally:
    record("run195_final_source_and_quality_audit.json",result)
    manifest={p.name:info(p) for p in OUT.iterdir() if p.is_file() and p.name!="run195_sha256_manifest.json"}
    record("run195_sha256_manifest.json",manifest)
    assert all(sha(OUT/n)==v["sha256"] for n,v in manifest.items())
    print(json.dumps({"status":result["status"],"free_zip_acquired":result.get("free_zip_acquired"),
        "owl_glbs":len(result.get("native_glb",[])),
        "no_release":True,"evidence_files":len(manifest)},ensure_ascii=False))
