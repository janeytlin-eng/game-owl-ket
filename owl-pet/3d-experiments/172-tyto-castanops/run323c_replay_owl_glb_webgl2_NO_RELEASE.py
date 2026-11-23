#!/usr/bin/env python3
"""Repeat the actual OWL mobile-viewport WebGL2 test from the immutable free CC0 source artifact.
This deliberately does NOT retry an unauthenticated download or invent an asset. NO_RELEASE."""
from __future__ import annotations
import importlib.util,json,pathlib,hashlib,shutil
from playwright.sync_api import sync_playwright

source_module = pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops/run323_native_chick_rig_access_NO_RELEASE.py")
spec=importlib.util.spec_from_file_location("run323_source_audit", source_module)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
archive_owl=pathlib.Path("run323-input/source_animal_owl.glb")
assert archive_owl.exists(), "Original Run323 artifact did not contain owl GLB"
expected="12b0d7ff039b60b58ea4dd0ebcf07242c5f2c3d1ba0dc0935b94aa5a954a8bbc"
assert mod.sha256(archive_owl)==expected, "Reused owl is not byte-identical to original source"
dst=mod.OUT/archive_owl.name
shutil.copy2(archive_owl,dst)
mod.REPORT["experiment"]="Run323c immutable native CC0 rig baseline owl-specific real Chromium WebGL2"
mod.REPORT["replay_original_artifact"]={
    "source_run_id":45180513360, "source_artifact_id":14821411655,
    "owl_glb_sha256":expected, "owl_glb_bytes":archive_owl.stat().st_size,
    "license":"CC0 Popyca free sample, verified LICENSE.txt inside archived source",
    "art_rejected":True
}
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--enable-unsafe-swiftshader","--use-gl=angle","--use-angle=swiftshader","--enable-webgl"])
    mod.browser_webgl(b,[dst])
    b.close()
mod.REPORT["conclusion"]="Genuine animated/rigged owl native GLB has been viewed, but designer-toy with no heart face or down: ART_REJECTED, NO_RELEASE; physical phone not tested"
mod.REPORT["quality_gate"]="ART_REJECTED"
mod.dump()
if not (mod.REPORT.get("webgl2",{}).get("captures") and all(x.get("status")=="loaded" and x.get("webgl2") and x.get("glError")==0 for x in mod.REPORT["webgl2"]["captures"])):
    raise SystemExit("WebGL2 owl captures failed; inspect real evidence and mark technology failure, never art approval")
