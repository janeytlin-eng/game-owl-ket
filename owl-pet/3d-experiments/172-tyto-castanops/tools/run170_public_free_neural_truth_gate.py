#!/usr/bin/env python3
"""Run170: legitimate public browser image-to-native-GLB test, NO_RELEASE by default.
No hidden internal endpoints, no CAPTCHA bypass, no account, no payments.
Every output is quarantined as UNREVIEWED and needs independent art/mobile QA.
"""
import asyncio
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "research-evidence-run170-ANONYMOUS-NEURAL-NO_RELEASE"
OUT.mkdir(parents=True, exist_ok=True)
SOURCE = ROOT / "research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED_IMAGE = "5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
KNOWN = ROOT / "known_rejected_asset_sha256_registry.json"
PROVIDERS = [
    {"key": "3dai_dev", "url": "https://3dai.dev/en",
     "button": r"Generate textured 3D|Generate 3D|Generate geometry"},
    {"key": "image_to_3d_app", "url": "https://image-to-3d.app/",
     "button": r"Generate 3D model|Generate 3D"},
]
OUTCOME = {"run": 170, "utc_start": datetime.now(timezone.utc).isoformat(),
           "source_reference": str(SOURCE.relative_to(ROOT)), "providers": {},
           "new_valid_glb": [], "release": False,
           "physical_mobile_GPU_tested": False,
           "workflow_note": "No-release regardless of successful format. Art must be visually approved."}
assert SOURCE.is_file()
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == EXPECTED_IMAGE
OUTCOME["source_sha256"] = EXPECTED_IMAGE
OUTCOME["source_dimensions"] = list(Image.open(SOURCE).size)
assert KNOWN.is_file()
known_raw = KNOWN.read_text()
REJECTED_HASHES = set(re.findall(r"\b[a-fA-F0-9]{64}\b", known_raw))
assert REJECTED_HASHES

def log_result():
    (OUT / "run170_actual_results.json").write_text(json.dumps(OUTCOME, ensure_ascii=False, indent=2))

def is_interstitial(s):
    lower = s.lower()
    return any(v in lower for v in [
        "checking your browser", "verify you are human", "just a moment",
        "cloudflare attention required", "captcha challenge", "turnstile challenge",
    ])

def is_demo_url(s):
    lower = s.lower()
    return any(v in lower for v in ["/samples/", "/demo/", "toy-car", "sample.glb", "example.glb",
                                    "placeholder.glb", "sample-model", "model-viewer-assets"])

def verify_glb(path, provenance, url):
    import trimesh
    if is_demo_url(url) or not provenance:
        return {"valid": False, "reason": "static example or source-bound generation not demonstrated"}
    data = path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    info = {"bytes": len(data), "sha256": sha, "origin": url, "provenance": provenance}
    if sha in REJECTED_HASHES:
        return {**info, "valid": False, "reason": "known rejected file fingerprint"}
    if len(data) < 65000 or data[:4] != b"glTF":
        return {**info, "valid": False, "reason": "not a substantial GLB"}
    try:
        mesh = trimesh.load(path, force="scene", process=False)
        ntri = sum(len(m.faces) for m in mesh.geometry.values() if hasattr(m, "faces"))
        info.update(meshes=len(mesh.geometry), triangles=ntri)
        if ntri < 600 or not mesh.geometry:
            return {**info, "valid": False, "reason": "missing credible native geometry"}
    except Exception as e:
        return {**info, "valid": False, "reason": "reimport failed: " + repr(e)[:250]}
    return {**info, "valid": True, "art": "UNREVIEWED", "webgl": "NOT_TESTED"}

async def probe(browser, provider):
    key, url = provider["key"], provider["url"]
    p = {"url": url, "state": "STARTED", "source_uploaded": False, "clicked_generate": False,
         "network_3d": [], "observations": [], "downloads": []}
    OUTCOME["providers"][key] = p
    context = await browser.new_context(accept_downloads=True, viewport={"width": 1340, "height": 950})
    page = await context.new_page()
    clicked_at = [0.0]
    candidate_responses = []

    async def response_listener(resp):
        if not clicked_at[0] or time.monotonic() < clicked_at[0]:
            return
        u = resp.url
        headers = resp.headers
        ctype = headers.get("content-type", "").lower()
        if (".glb" in u.lower() or "model/gltf-binary" in ctype or
            "application/octet-stream" in ctype):
            if len(p["network_3d"]) < 20:
                p["network_3d"].append({
                    "status": resp.status, "url_domain": urlparse(u).netloc,
                    "url_path_truncated": urlparse(u).path[:180], "content_type": ctype[:80]})
            if not is_demo_url(u) and resp.ok and (".glb" in u.lower() or "model/gltf-binary" in ctype):
                candidate_responses.append(resp)

    page.on("response", response_listener)
    try:
        response = await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        p["http_status"] = response.status if response else None
        await page.wait_for_timeout(4500)
        p["page_title"] = (await page.title())[:160]
        text = (await page.locator("body").inner_text(timeout=10000))[:4500]
        p["body_excerpt"] = text[:2500]
        p["form_controls"] = await page.locator("input, button, select").evaluate_all(
            "(els) => els.slice(0,75).map(e=>({tag:e.tagName,type:e.type||null,text:(e.innerText||e.ariaLabel||'').slice(0,90),disabled:e.disabled}))")
        await page.screenshot(path=str(OUT / (key + "_01_initial.png")), full_page=False)
        if p["http_status"] in [401, 402, 403, 429] or is_interstitial(text):
            p["state"] = "BLOCKED_OR_HUMAN_CHECK"
            return
        inputs = page.locator("input[type='file']")
        if await inputs.count() == 0:
            p["state"] = "NO_PUBLIC_UPLOAD_INPUT"
            return
        await inputs.first.set_input_files(str(SOURCE))
        p["source_uploaded"] = True
        await page.wait_for_timeout(6000)
        await page.screenshot(path=str(OUT / (key + "_02_uploaded.png")), full_page=False)
        txt = (await page.locator("body").inner_text(timeout=10000))[:5000]
        if is_interstitial(txt):
            p["state"] = "HUMAN_CHECK_AFTER_UPLOAD"
            return
        buttons = page.get_by_role("button", name=re.compile(provider["button"], re.I))
        if await buttons.count() == 0:
            p["state"] = "NO_PUBLIC_GENERATE_BUTTON"
            p["postupload_excerpt"] = txt[:2000]
            return
        button = buttons.first
        for _ in range(8):
            if await button.is_enabled():
                break
            await page.wait_for_timeout(1500)
        if not await button.is_enabled():
            p["state"] = "GENERATE_BUTTON_DISABLED"
            p["postupload_excerpt"] = txt[:1800]
            return
        if "pay" in (await button.inner_text()).lower():
            p["state"] = "PAYMENT_BUTTON_NOT_CLICKED"
            return
        # This is the visible public free generate action, not a bypassed API request.
        clicked_at[0] = time.monotonic()
        await button.click(timeout=15000)
        p["clicked_generate"] = True
        p["state"] = "GENERATING"
        await page.wait_for_timeout(5000)
        await page.screenshot(path=str(OUT / (key + "_03_submitted.png")), full_page=False)
        already_saved = False
        for tick in range(1, 37):
            await page.wait_for_timeout(10000)
            if tick in (6, 18, 35):
                await page.screenshot(path=str(OUT / (key + "_progress_" + str(tick) + ".png")), full_page=False)
            body = (await page.locator("body").inner_text(timeout=15000))[:10000]
            if tick in (1, 6, 18, 35):
                p["observations"].append({"after_seconds": tick * 10,
                                         "text_tail": body[-1800:]})
            if is_interstitial(body):
                p["state"] = "HUMAN_CHECK_DURING_GENERATION"
                break
            # Only attempt visible native GLB export; not paid, login or private links.
            downloadable = page.get_by_role("button", name=re.compile(r"download.*GLB|export.*GLB|download 3D|download model", re.I))
            links = page.get_by_role("link", name=re.compile(r"download.*GLB|export.*GLB|download model", re.I))
            locator = downloadable.first if await downloadable.count() else (links.first if await links.count() else None)
            if locator is not None and await locator.is_visible() and await locator.is_enabled():
                try:
                    async with page.expect_download(timeout=20000) as dlinfo:
                        await locator.click(timeout=15000)
                    download = await dlinfo.value
                    suggested = download.suggested_filename
                    if is_demo_url(suggested):
                        p["downloads"].append({"suggested": suggested, "rejected": "static-demo filename"})
                    else:
                        file = OUT / (key + "_user_generated_UNREVIEWED.glb")
                        await download.save_as(str(file))
                        check = verify_glb(file, True, page.url)
                        p["downloads"].append({"suggested": suggested, **check})
                        if check["valid"]:
                            OUTCOME["new_valid_glb"].append({"file": file.name, "provider": key, **check,
                                "source_reference_sha256": EXPECTED_IMAGE, "is_static_demo": False})
                            already_saved = True
                        else:
                            file.unlink(missing_ok=True)
                    p["state"] = "NATIVE_EXPORT_VALIDATED" if already_saved else "DOWNLOAD_REJECTED"
                    break
                except (PlaywrightTimeout, Exception) as e:
                    p["observations"].append({"download_error": repr(e)[:240]})
            # Some sites return a native GLB directly over a public generated request after clicking.
            if candidate_responses and not already_saved:
                for resp in list(candidate_responses)[:4]:
                    if is_demo_url(resp.url):
                        continue
                    try:
                        blob = await resp.body()
                    except Exception:
                        continue
                    if len(blob) < 65000 or blob[:4] != b"glTF":
                        continue
                    file = OUT / (key + "_generation_response_UNREVIEWED.glb")
                    file.write_bytes(blob)
                    check = verify_glb(file, True, resp.url)
                    p["downloads"].append(check)
                    if check["valid"]:
                        OUTCOME["new_valid_glb"].append({"file": file.name, "provider": key, **check,
                            "source_reference_sha256": EXPECTED_IMAGE, "is_static_demo": False})
                        p["state"] = "NATIVE_GENERATION_RESPONSE_VALIDATED"
                        already_saved = True
                        break
                    file.unlink(missing_ok=True)
                if already_saved:
                    break
            if re.search(r"sign in to download|login to download|purchase to download|buy credits|not enough credits", body, re.I):
                p["state"] = "EXPORT_LOGIN_OR_CREDIT_GATED"
                break
            if re.search(r"(generation|job|task) failed|error generating|no available GPU", body, re.I):
                p["state"] = "PUBLIC_GENERATION_ERROR"
                break
        if not already_saved and p["state"] == "GENERATING":
            p["state"] = "NO_NATIVE_EXPORT_IN_OBSERVATION_WINDOW"
        await page.screenshot(path=str(OUT / (key + "_04_final.png")), full_page=False)
        p["final_excerpt"] = (await page.locator("body").inner_text(timeout=10000))[-2500:]
    except Exception as e:
        p["state"] = "BROWSER_ERROR"
        p["error"] = repr(e)[:1200]
    finally:
        log_result()
        await context.close()

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        try:
            for provider in PROVIDERS:
                await probe(browser, provider)
        finally:
            await browser.close()
    OUTCOME["utc_end"] = datetime.now(timezone.utc).isoformat()
    log_result()
    print("RUN170_DONE", json.dumps({k: v["state"] for k,v in OUTCOME["providers"].items()}),
          "FRESH_VALID_GLB", len(OUTCOME["new_valid_glb"]))
if __name__ == "__main__":
    asyncio.run(main())
