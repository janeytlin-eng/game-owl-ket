# #172 *Tyto castanops* v3 — Run293–295: real $0 native-3D service discovery, quota failure, and pixel-preserving chick isolation — NO RELEASE

**2026-11-22 Asia/Shanghai, independent GitHub research branches. Final gate: REAL_EXTERNAL_GENERATION_DEMO_OBSERVED / ACTUAL_TARGET_GLB_BLOCKED_BY_DAILY_QUOTA / SOURCE_CUTOUT_PASS / ART_UNTESTED_REJECTED_FOR_RELEASE / PHYSICAL_PHONE_UNTESTED / RIGHTS_HOLD / NO_RELEASE.**

## Checked before work

Read repo `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, `research/species/172-tyto-castanops-v3.md`, Run292 full research audit, existing cat prototype description, its six-view browser QA scripts, and earlier source/rights rejections. `main` and the separate 251-species concept production were left unchanged. The rightmost actual image is the **cream-white, dark-open-eyed, soft-down-covered, heart-faced, age-unknown mesoptile with down-buried short wing, hidden tail and two supported feet on a hollow lip**. It is not a specific-week biological claim.

No existing Run281–292 model passes juvenile anatomy and fine down. This test seeks an actual no-money 3D route, NOT a screenshot dressed up as an asset.

## Run293a: source physically opened; false navigation click discovered

Service https://trellis2.dev/ advertises free accountless image-to-3D. [Terms](https://trellis2.dev/terms-of-service) dated 2026-08-19 state output rights remain with content submitter but third-party HF model licenses may vary. [Privacy](https://trellis2.dev/privacy-policy) states images are processed by Hugging Face Spaces. Its independent branding is not proof Microsoft TRELLIS weights are used; upstream actual browser traffic later showed `hy3dlab-image-to-3d.hf.space`, with model identity/license still pending verification. Avoid product use until cleared.

Made synthetic **non-user** cartoon test image (not intended to resemble good owl art) using Pillow, launched headless actual Chromium at 390×780 and used Playwright normal UI. The first run clicked marketing CTA labelled "Generate 3D Free" rather than the actual form submit. This was a real QA false-positive, not a generated GLB. [Run293a](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45027706392), [artifact 14756402883](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45027706392/artifacts/14756402883) downloaded/verified: 152,362 ZIP bytes, SHA256 `13df1bcf1fb21952d4e96cf94dda389a3a881dc520ea36bfbf8929fdf8bbb6c0`, 7/7 CRC and 5/5 SHA entries correct.

## Run293b: actual no-money synthetic source generation rendered, but GLB wasn't captured

Fixed browser script to click the true visible enabled submit button `GENERATE / Fast & Private 3D in ~50s`. [Run293b](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45027990968) succeeded and the actual full-page screenshot showed a gray 3D two-lobed bird-like shape in the page's native orbit viewer, markedly inferior to target (as expected of a crude synthetic drawing).

More importantly, browser network telemetry observed an **HTTP 200 response** from `https://hy3dlab-image-to-3d.hf.space/static/45e649e3-dd11-4c39-898b-01d6c94e151b/white_mesh.glb`. The earlier script wrongly waited for a browser `download` event, whereas the model loader fetched the GLB as a network subresource. No actual GLB bytes were captured for binary/triangle inspection. Thus **real 3D browser generation observed / native binary not independently validated**; no model success claim.

Independently downloaded/verified [Run293b artifact 14755923198](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45027990968/artifacts/14755923198): ZIP 418,952 bytes, SHA256 `1a8bbedd757ec93aa88fdf49a85c25524172d73d142995eb3f0f4a0e8576a5d3`, 7/7 CRC and 5/5 internal SHA256 valid. The screenshot and JSON log are preserved; there is **no redistributable model** in this artifact.

## Run294: actual rightmost original concept submitted once, blocked by service limit

Created another isolated workflow to upload the **actual unmodified #172 v3 rightmost crop**, not an invented bird: source plate was exactly 1536×1024, crop 512×1024. The crop included excess dark eucalyptus bark and original plate title; it was recognized later as a poor image-to-3D conditioning input.

The updated Playwright script listens for genuine `.glb` network response bytes, with GLB2 binary signature/version/full-length, JSON chunk and POSITION-mesh validation and optional real Three.js SwiftShader three-angle test. A successful HTTP or a 3D-looking screenshot alone is never a pass.

[Run294](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45028464551) completed the **experiment**; the website itself returned **"Processing limit reached / Come back tomorrow / Resets in about 2 hours"**, and generated **zero actual target GLB**. No payment/account/rate-limit circumvention attempted. In fact no WebGL model was tested because no GLB existed. Its workflow success only means transparent evidence capture, NOT successful generation. [Run294 artifact 14756751931](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45028464551/artifacts/14756751931) was independently downloaded: **831,805 ZIP bytes, SHA256 `de698e66b8a7b8a45ae2942770ffa49a847b4039fd697bf07bc42a95c1c5f654`**, 9/9 CRC plus 8/8 file SHA256 verification. `NO_NATIVE_GLB.flag` and `run294_report.json` unequivocally state the block. A temporary rate limit is **not** permanent tooling unavailability; a later ordinary scheduled run can re-evaluate after the source's own displayed reset.

## Run295: actual source image intelligently isolated from bark (input only, not model)

Instead of spending another blocked generation, used **free OpenCV GrabCut** with explicit seed mask around the actual original young (rather than fake geometric owl modeling), retained original RGB texture and fine cream down, generated a soft-alpha foreground and a white-background input. This directly addresses the unnecessary old tree hollow/title occupying the former target conditioning crop.

New isolated 392×580 transparent PNG, white-background source, gray quality-control preview and unchanged original source crop generated and reopened. Actual quality review: **preserves facial mask, eyes, soft down outline and full feet clearly**; tiny gray/brown substrate patch survives under the toes and the alpha hairline is imperfect. This is a meaningful better **2D input** for a future real image-to-native-3D tool, **not itself a 3D asset**, and it does not resolve unknown side/back geometry.

[Run295](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45028925453) succeeded. Independently downloaded [Run295 artifact 14757395174](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45028925453/artifacts/14757395174), **1,113,523 ZIP bytes; SHA256 `3197c82ae51eac4cb9903628439f6d3a353639d4cccc07e53fba989c02cf9c3d`**. 8/8 ZIP CRC and 6/6 internal SHA256 passed. Source original 1536×1024 SHA256 `881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d`, output subject 392×580, 162,079 nontransparent matte pixels, 10,891 antialiased boundary pixels. Full program [run295_real_reference_cutout_preprocess_ONLY_NO_RELEASE.py](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run295-neural-matte-isolate-actual-owl-concept-NO_RELEASE/owl-pet/3d-experiments/172-tyto-castanops/run295_real_reference_cutout_preprocess_ONLY_NO_RELEASE.py) regenerates output from the immutable original.

## Additional independent anatomy reference research (do not confuse with species facts)

Oregon Historical Society 1904 William L. Finley *Tyto alba* downy barn-owl chick photo catalog: [side A0562](https://digitalcollections.ohs.org/barn-owl-chick), [back A0564](https://digitalcollections.ohs.org/barn-owl-chick-2), [second side A0565](https://digitalcollections.ohs.org/barn-owl-chick-3), [front group A0567](https://digitalcollections.ohs.org/barn-owl-chicks). Catalog metadata indicates no U.S. copyright on some images; global rights unverified. These are **not** verified multi-camera images of the same individual and cannot establish *T. castanops* exact age or specific juvenile plumage. Only source URLs indexed; photos not copied.

## Current quality verdict and isolation

**NO_RELEASE.** The actual target still has **no produced native GLB** from this source after quota was hit; **no truthful multi-angle native 3D art acceptance** and **no Android/iPhone physical WebGL GPU/FPS/memory/thermal validation**. The single synthetically generated gray blob is not a suitable child model. The pixel-preserving alpha cutout is useful legitimate new pre-processing evidence but **must never be called 3D**. Upstream third-party model rights also remain unresolved. No extra external paid services: **$0**.

Isolated research artifacts and scripts only on `research/owl172-run295-neural-matte-isolate-actual-owl-concept-NO_RELEASE`, inherited from isolated Run294 branch; no edits to `main`, 251 species production, concept manifests, original image or cat demo/deployment. All artifact links are **temporary research evidence**, expire roughly **2026-12-06**, not product links.

**Correct next experiment:** after displayed free quota resets, feed the Run295 isolated white/alpha original-pixel image rather than the bark-dominated triptych crop; capture true GLB bytes; independently open and judge front/right/back/top and materially correct cream down and anatomically fused face/wing/feet. Without basic three-dimensional juvenile side/back and groom, art remains rejected regardless of algorithm/triangle count. Do not assume output rights are cleared merely because the site's general terms claim user retention.
