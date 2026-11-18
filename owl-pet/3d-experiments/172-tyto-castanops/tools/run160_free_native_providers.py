#!/usr/bin/env python3
"""Run160: actually operate new zero-extra-fee public image-to-3D browser UIs.

Explicitly no sign-up/paywall/Turnstile bypass, no undocumented API calls, no
download of hidden preview network responses, no conversion of demo models.
Do not confuse valid GLB with accepted baby-owl art.
"""
import datetime
import hashlib
import json
import pathlib
import re
import struct
import time
import traceback
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT = ROOT / "research-evidence-run160-THREE-ANONYMOUS-GENERATORS-NO_RELEASE"
OUT.mkdir(parents=True, exist_ok=True)
SOURCE = ROOT / "research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
SOURCE_SHA = "5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
SITES = [
    ("pic2mesh", "https://www.pic2mesh.com/"),
    ("img3d", "https://img3d.org/"),
    ("image_to_3d", "https://image-to-3d.app/"),
]

def digest(payload):
    return hashlib.sha256(payload).hexdigest()

def save(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str))

def txt(page):
    try:
        return page.locator("body").inner_text(timeout=7000)[-7000:]
    except Exception as exc:
        return "BODY_READ_ERROR: " + str(exc)[:240]

def snap(page, name, record):
    try:
        page.screenshot(path=str(OUT / (name + ".png")), full_page=False, timeout=12000)
    except Exception as exc:
        record.setdefault("screenshot_errors", []).append(name + ": " + repr(exc)[:200])

def glb_info(bits):
    output = {"bytes": len(bits), "sha256": digest(bits), "valid_glb_v2": False}
    if len(bits) < 28 or bits[:4] != b"glTF":
        return output
    _, ver, n = struct.unpack_from("<4sII", bits)
    output.update({"version": ver, "declared_bytes": n})
    if ver != 2 or n != len(bits):
        return output
    chunk_len, tag = struct.unpack_from("<II", bits, 12)
    if tag != 0x4E4F534A or 20 + chunk_len > len(bits):
        return output
    try:
        parsed = json.loads(bits[20:20 + chunk_len].decode("utf8").rstrip(" \x00"))
        output.update({
            "valid_glb_v2": bool(parsed.get("meshes")),
            "meshes": len(parsed.get("meshes", [])),
            "materials": len(parsed.get("materials", [])),
            "images": len(parsed.get("images", [])),
        })
    except Exception as exc:
        output["json_error"] = repr(exc)
    return output

def get_frames(page):
    return [page] + [fr for fr in page.frames if fr != page.main_frame]

def meaningful_controls(fr):
    try:
        return [v.strip()[:70] for v in fr.locator("button").all_inner_texts()[:45]]
    except Exception:
        return []

def run_one(browser, name, address, registry, result):
    record = {
        "public_url": address, "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "actions": [], "sampled_responses": [], "download_attempts": [], "screenshots": [],
    }
    result["providers"][name] = record
    ctx = browser.new_context(viewport={"width": 1390, "height": 900}, accept_downloads=True)
    page = ctx.new_page()
    page.set_default_timeout(10000)
    def on_response(resp):
        # Deliberately do not record signed links, cookies, request bodies or tokens.
        if len(record["sampled_responses"]) >= 40:
            return
        try:
            path = urlsplit(resp.url).path
            if re.search(r"generate|extract|\.glb|3d|predict|queue|gradio|api", path, re.I):
                record["sampled_responses"].append({
                    "host": urlsplit(resp.url).hostname, "path": path[:120],
                    "status": resp.status, "content_type": resp.headers.get("content-type", "")[:75],
                })
        except Exception:
            pass
    page.on("response", on_response)
    try:
        res = page.goto(address, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(9000 if name == "paint3d" else 3500)
        record["initial_http"] = res.status if res else None
        record["title"] = page.title()
        record["body_initial"] = txt(page)[:4500]
        snap(page, name + "_01_landing", record)
        if re.search(r"just a moment|performing security verification|verify you are human|cloudflare|turnstile.*(verify|challenge)", record["body_initial"], re.I):
            record["status"] = "ACCESS_CHALLENGE_NOT_BYPASSED"
            return
        # Embedded providers (e.g. public Gradio iframe) can expose their own
        # ordinary file input. Use only user-facing upload widgets.
        frame = None
        for pause in range(9):
            for fr in get_frames(page):
                try:
                    if fr.locator("input[type=file]").count() > 0:
                        frame = fr
                        break
                except Exception:
                    pass
            if frame is not None:
                break
            page.wait_for_timeout(3000)
        record["frame_count"] = len(page.frames)
        record["frames"] = [{"host": urlsplit(fr.url).hostname, "path": urlsplit(fr.url).path[:100]} for fr in page.frames[:15]]
        if frame is None:
            record["status"] = "NO_PUBLIC_FILE_INPUT"
            record["body_at_failure"] = txt(page)[-4000:]
            snap(page, name + "_02_no_upload_widget", record)
            return
        record["upload_frame"] = {"host": urlsplit(frame.url).hostname, "path": urlsplit(frame.url).path[:80]}
        frame.locator("input[type=file]").first.set_input_files(str(SOURCE))
        record["actions"].append("Uploaded checksum-confirmed rightmost cream chick using visible site's browser file input")
        page.wait_for_timeout(6500)
        snap(page, name + "_02_uploaded", record)
        record["body_after_upload"] = txt(page)[-3000:]
        record["controls_after_upload"] = meaningful_controls(frame)

        # Public "Generate" buttons only; never press login/buy/subscribe.
        button = None
        for pattern in [
            r"^generate shape$", r"^generate.*$",
            r"^create( 3d( model)?)?$", r"^convert( to 3d)?$", r"^run$", r"^submit$"
        ]:
            try:
                found = frame.get_by_role("button", name=re.compile(pattern, re.I))
                if found.count():
                    for j in range(min(found.count(), 4)):
                        if found.nth(j).is_enabled() and found.nth(j).is_visible():
                            button = found.nth(j)
                            break
                if button is not None:
                    break
            except Exception:
                pass
        if button is None:
            # Some public demos auto-submit on upload; watch rather than falsely
            # reporting failure. No private route or script injection.
            record["generation_control"] = "NO_CLICKABLE_SEPARATE_GENERATE_BUTTON"
        else:
            label = button.inner_text(timeout=3500)
            record["generation_control"] = label[:120]
            if re.search(r"sign|log.?in|pay|credit|subscribe|account", label, re.I):
                record["status"] = "ACCOUNT_OR_PAYMENT_GATE"
                return
            try:
                button.click(timeout=12000)
                record["actions"].append("Clicked public generation control: " + label[:75])
            except Exception as exc:
                record["generation_click_error"] = repr(exc)[:450]
        # First capture shortly after submit, then poll for up to ~132 s.
        for i in range(12):
            page.wait_for_timeout(11000)
            if i in (0, 3, 7, 11):
                snap(page, name + "_poll_" + str(i), record)
                record.setdefault("observations", []).append({
                    "poll": i, "main_body": txt(page)[-4000:],
                    "frame_body": txt(frame)[-2500:],
                    "frame_buttons": meaningful_controls(frame),
                })
        record["body_final"] = txt(page)[-5000:]
        record["frame_body_final"] = txt(frame)[-5000:]
        record["controls_final"] = meaningful_controls(frame)
        snap(page, name + "_03_final", record)

        # Only use clearly offered download/export UI; never intercept underlying
        # response bytes or fetch access-gated output directly.
        for fr in get_frames(page):
            for label in [r"extract glb", r"download glb", r"export glb",
                          r"download model", r"download 3d", r"download"]:
                for role in ["button", "link"]:
                    try:
                        widgets = fr.get_by_role(role, name=re.compile(label, re.I))
                        for j in range(min(widgets.count(), 2)):
                            ui = widgets.nth(j)
                            if not ui.is_visible() or not ui.is_enabled():
                                continue
                            caption = (ui.inner_text(timeout=3500) or label).strip()[:110]
                            if re.search(r"sign|log.?in|subscribe|credit|pay|upgrade", caption, re.I):
                                continue
                            try:
                                with page.expect_download(timeout=12000) as pending:
                                    ui.click(timeout=9000)
                                dl = pending.value
                                tmp = OUT / (name + "_quarantine_download.tmp")
                                dl.save_as(str(tmp))
                                bits = tmp.read_bytes()
                                tmp.unlink()
                                info = glb_info(bits)
                                info["suggested_name"] = dl.suggested_filename[:90]
                                info["known_rejected"] = info["sha256"] in registry
                                record["download_attempts"].append(info)
                                if info["valid_glb_v2"] and not info["known_rejected"]:
                                    file = OUT / (name + "_new_ui_generated_3d_UNREVIEWED.glb")
                                    file.write_bytes(bits)
                                    result["new_valid_glb"].append({"file": file.name, **info})
                                    record["status"] = "NEW_VALID_NATIVE_GLB_UNREVIEWED"
                                    return
                            except Exception as exc:
                                record["download_attempts"].append({"control": caption, "error": repr(exc)[:350]})
                    except Exception:
                        pass
        final = record.get("frame_body_final", "") + record.get("body_final", "")
        if re.search(r"sign.?in|register|create account|subscribe.*download|upgrade.*export", final, re.I):
            record["status"] = "DOWNLOAD_GATE_ACCOUNT_OR_SUBSCRIPTION"
        elif re.search(r"failed|error|quota|limit|unavailable|exhausted", final, re.I):
            record["status"] = "GENERATION_OR_PROVIDER_ERROR_NO_VALID_GLBS"
        else:
            record["status"] = "NO_PUBLIC_NATIVE_GLB_AFTER_GENERATION_ATTEMPT"
    except Exception as exc:
        record["status"] = "BROWSER_EXECUTION_ERROR"
        record["error"] = repr(exc)
        record["traceback"] = traceback.format_exc()[-2400:]
        snap(page, name + "_error", record)
    finally:
        record["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        save("run160_actual_results.json", result)
        ctx.close()

def main():
    for prerequisite in [
        "owl-pet/AGENTS.md", "owl-pet/README.md",
        "owl-pet/prototype/index.html",
        "owl-pet/research/species/172-tyto-castanops-v3.md",
        str(ROOT / "known_rejected_asset_sha256_registry.json"),
        str(ROOT / "2026-11-18-run157-sculptly-upload-state-native-preview-audit-NO_RELEASE.md"),
        str(ROOT / "2026-11-18-run159-two-corrected-generation-controls-actual-NO_RELEASE.md"),
    ]:
        if not pathlib.Path(prerequisite).is_file():
            raise RuntimeError("Missing prerequisite, do not proceed: " + prerequisite)
    if digest(SOURCE.read_bytes()) != SOURCE_SHA:
        raise RuntimeError("Exact rightmost input image SHA256 mismatch")
    rejected = (ROOT / "known_rejected_asset_sha256_registry.json").read_text()
    registry = set(re.findall(r"\b[a-f0-9]{64}\b", rejected.lower()))
    output = {
        "run": 160, "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "canonical_source_sha256": SOURCE_SHA, "source": str(SOURCE),
        "last_work": "Run159 corrected public controls: Paint 3D failed backend generation, Hy3D blocked behind account/payment; Run157 Sculptly generated a preview but art/export were rejected; Run147 image-to-3d.app screenshot timed out",
        "constraints": "Public visible UI only; no access bypass; no account; $0 additional payment",
        "new_valid_glb": [], "providers": {}, "art": "UNREVIEWED",
        "phone_webgl": "NOT_TESTED", "release": False,
    }
    save("run160_preflight.json", output)
    with sync_playwright() as pl:
        browser = pl.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        for name, address in SITES:
            run_one(browser, name, address, registry, output)
        browser.close()
    save("run160_actual_results.json", output)
    (OUT / "NO_RELEASE.flag").write_text(
        "Never release without actual non-demo GLB, lawful export, true native front/quarter/side/back art review and mobile WebGL validation.\n"
    )
    print("RUN160_REAL_BROWSER_PROBE", json.dumps({
        "providers": {k: v.get("status") for k, v in output["providers"].items()},
        "new_valid_glb_count": len(output["new_valid_glb"]),
        "additional_payment_usd": 0, "release": False
    }))

if __name__ == "__main__":
    try:
        main()
    except Exception:
        (OUT / "run160_fatal_error.txt").write_text(traceback.format_exc())
        raise
