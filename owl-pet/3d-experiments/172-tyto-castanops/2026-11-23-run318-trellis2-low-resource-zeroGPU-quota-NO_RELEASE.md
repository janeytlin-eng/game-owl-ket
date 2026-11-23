# #172 *Tyto castanops* v3 rightmost downy chick — Run318 actual official TRELLIS.2 low-resource GLB test

**Date:** 2026-11-23 (Asia/Shanghai). **Final:** `REAL_PUBLIC_UI_CLICKED / ZEROGPU_QUOTA_0_SECONDS / NO_NEW_NATIVE_GLB / NO_NEW_WEBGL_QA / ART_NOT_APPROVED / RIGHTS_HOLD / NO_RELEASE`.

## Scope and checked starting point

- Re-read `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, #172 v3 species record and review, existing kitten WebGL prototype context, and [Run316–317b audit](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run317-stability-public-GLB-real-WebGL2-NO_RELEASE/owl-pet/3d-experiments/172-tyto-castanops/2026-11-23-run316-to-run317b-official-GLB-WebGL2-ART_REJECTED-NO_RELEASE.md).
- Exact user target remains original v3 plate's **rightmost cream second-down, age-unknown mesoptile**, with organic heart-shaped disc, two dark eyes, natural short down-buried wings, concealed tail, believable feet on old eucalypt hollow, true soft down, coherent sides/back. Not the two adults; not an interchangeable Barn Owl.
- Rebuilt the original rightmost transparent reference and verified reference white-background SHA256 `6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77` and transparent cutout SHA256 `37e2b3c96da31c558f511ee172b43bec4c721186a074327ec6cb791c9d2c5ed8`. Did not change concept bytes.
- Run317 genuine Stable Fast 3D 27,372-triangle textured GLB was **art-rejected**, especially real sides/back. Its three-view screenshots were independently downloaded/opened as a starting quality comparison, not treated as a finished asset.

## New hypothesis actually tested

Microsoft's current [TRELLIS.2 public Gradio source](https://huggingface.co/spaces/microsoft/TRELLIS.2/blob/main/app.py) exposes generation resolution choices 512/1024/1536, GLB decimation 100k–500k (default 300k), and texture size 1024–4096 (default 2048). The official [extract_glb implementation](https://huggingface.co/spaces/microsoft/TRELLIS.2/blob/main/app.py) separately decodes latents then calls GPU-intensive geometry remeshing/texture baking. Prior Run316 successfully generated multiview preview but failed its default Extract GLB. New bounded experiment: real **512 resolution + 100,000-face decimation + 1024 texture** via public UI; only one generation and (if it becomes possible) one extraction; no API endpoints, account creation, hidden file access or payment.

Actual reproducible files:
- `run318_trellis2_low_resource_glb_extraction_NO_RELEASE.py`: real Playwright page upload / controls / Generate / conditional Extract GLB, native glTF header + Trimesh import gate, screenshots, JSON and public network logs.
- `.github/workflows/owl172-run318-trellis2-low-memory-export-NO_RELEASE.yml`: independent sparse checkout / original-reference hash / actual Chromium / conditional real browser WebGL QA / evidence integrity.

## Execution, observed outcome and independent validation

- [Actual successful **research** GitHub Actions run 45139414699](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45139414699) completed 2026-11-23 08:33:53Z. **Workflow success means research completed, NOT that a model was generated.**
- HTTP 200 official site. Actual browser screenshots confirm correct original chick uploaded, UI radio **512** selected, **Decimation Target 100000**, **Texture Size 1024** visibly set and persisted. Actual `Generate` button click recorded `generation_clicked=true`.
- After the click, Gradio displayed **`You have exceeded your ZeroGPU quota (120s requested vs. 0s left). Try again in 0:00:00. Authenticate with a Hugging Face token for more quota`**. This occurred before any meaningful 3D preview (preview image count = 0); thus `Extract GLB` was **not** clicked. This is a no-quota generation refusal; **it does not test the proposed lower-cost export hypothesis**.
- No newly produced GLB. No new native 3D, multi-angle art evaluation, WebGL2 browser model load or physical-phone measurement. No financial charge, no token supplied, no account registered, no validation bypass.
- [Research-only original evidence artifact #14801770964](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45139414699/artifacts/14801770964) was independently downloaded and inspected: ZIP **2,137,205 bytes**, SHA256 `35208f01e29db9b6839bd09bbd87f5c7262c927a580c29648dd0ed14a3e33d69`; **16/16 ZIP CRC** valid, **13/13 internal file hashes** valid. It holds actual source reference, screenshots including the quota error, Gradio DOM/controls, network observations, runner report and `STRICT_NO_RELEASE` flag. Artifact scheduled to expire **2026-12-07 08:33:50Z**; this audit and reproducible code remain in the research branch.

## Rights and quality boundary

- The model weights are publicly labelled MIT, but this does not establish that all model/data/third-party runtime dependencies or resulting product rights are cleared. Commercial-use questions about TRELLIS.2's NVIDIA dependencies/hosted output remain open in [upstream discussion #22](https://github.com/microsoft/TRELLIS.2/issues/22); independently verify before product use. Never read a community model page as a complete license chain.
- Hard quality gates remain: real native volumetric 3D with credible cream down **in geometry/structure**, non-cartoon natural facial disc, short wings/shoulders, coherent rear silhouette, two realistic supporting feet, acceptable light/non-metallic PBR, 390×780 browser WebGL2 and a genuine phone touch/performance test. None passed anew.
- Next time: do not keep hammering a server announcing ZeroGPU quota 0s. Try the public UI again only if the displayed quota genuinely changes, or pursue genuinely different free lawful high-quality sculpt/asset pipeline. It is a **transient provider quota**, not a permanent project blocker.

All files and actual evidence isolated to `research/owl172-run318-official-trellis2-low-memory-extract-NO_RELEASE`. **Main, 251-species imagery workflow, v3/v4 plates, original kitten prototype and deployment remain untouched.**

**Final gate: NO_RELEASE — no approved viewable character; no user-facing sample should be published.**
