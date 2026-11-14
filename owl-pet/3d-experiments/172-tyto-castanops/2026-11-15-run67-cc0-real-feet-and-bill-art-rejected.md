# Run67 — #172 Tyto castanops v3 actual CC0 foot + bill surface transfer (ART_REJECTED)

Date: 2026-11-15 Asia/Shanghai. **No release, deployment, production change or paid service.**

## Mandatory preflight and baseline

Read `owl-pet/README.md`, `AGENTS.md`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, Run66 and the location of the current cat WebGL prototype. Recovered and unpacked the actual [Run65 failed-source ZIP](https://drive.google.com/file/d/1O0ORFCPipUQzJ9W-reaZvh_lkycQR70i/view) on local runtime (16,170,781 bytes). Used its #172 v3 right cream mesoptile crop, exact baseline Run63 P GLB (SHA256 `15f70a269602bfd9ecc1e6435a3714c2120db702ca008c70655162710dabb388`) and inspected 4-view renders. Independently recovered genuine Run10 GitHub Actions artifact [13965413613](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43266413692/artifacts/13965413613) with the UV-mapped Innerscene adult owl meshes (still downloadable as of this run, expires Nov 26). This is **adult great horned owl**, not a juvenile Tyto castanops.

## Actual new binary experiments

Wrote and ran independent `build_run67.py`, selecting 20 real 3D articulated original model toe, claw, tarsus and foot-pad meshes from a 129-mesh source with intact original UV/PBR material. Transformed their genuine sculpt surfaces into #172's existing nonparametric, photo-conditioned continuous body local coordinates, deleted only old crude experimental toe/shank/claw geometry. Compared two variants:
- Y = source-real-foot transplant + original pale bill: **23 meshes, 70,132 triangles, 3,825,412 bytes**, SHA256 `c3b79c038775946130732b34333d587334f00af988d0dc876aabdfea3faadda2`.
- Z = same source-real-foot transplant + source-real adult hooked bill: **23 meshes, 70,020 triangles, 3,826,320 bytes**, SHA256 `e8022eaf8eb6eb9386ce7f8a925a80bd69a2c8cc6fa2f4b0db09c85df06b7a75`.

Both were actually exported to GLB and *re-imported* with trimesh. Verified body topology and vertex coordinates **unchanged** at 59,520 source continuous-body triangles, 20 new CC0-source foot meshes in both, no original prototype changes. Original source CC0 license is claimed by publisher [Innerscene Owl](https://www.innerscene.com/tools/library/3d-parts/owl-d696472a); underlying creator and source propriety have not been independently verified; this use is a bounded anatomical feasibility experiment, not species validation.

Rendered 12 actual VTK glTF-importer images: base/Y/Z × front, three-quarter, strict side, back; valid actor counts. Ran 16 actual Chromium/ANGLE SwiftShader WebGL2 GLB draws: Y/Z × 390×600 and 800×800 × four angles. First browser test failed because no X server; headless launch then produced no WebGL2. Fixed by using **xvfb-run headed Chromium**; reran all final 16 screenshots and got **0 WebGL errors and no page JS exceptions**. 390px viewport is NOT a phone hardware test; custom GLB viewer is not standard PBR or animation.

## Art review = ART_REJECTED

Checked actual renders against the original juvenile right-bird crop. Adult transfer feet are too thin/dark/small, mostly occluded by belly, and not large supported juvenile feet on a tree hollow lip. Z's source hooked bill is overly dark and reads as a tiny black hook, worse than the original pale bill. Inherited body still looks like smooth pear; heart face is a frontal photo projection, not sculpted feather layers; back has poor juvenile wing morphology, side/rear identity is absent. VTK shows large side/rear dark rendering anomalies absent from simplified browser raster. No genuine soft multilayer cream down. No mobile hardware, FPS, animation, touch or real PBR evidence.

The free fal image-to-3D catalog was actually attempted but **requires interactive user input** in this noninteractive execution; it did not execute or charge anything. No new free hosted generative route available in this run.

## Evidence, integrity, persistence

Local independent QA ZIP `Owl172_Run67_CC0_REAL_ANATOMY_TRANSFER_ART_REJECTED_QA.zip`:
- 50 files (49 data/code/source/checks plus JSON SHA256 manifest), **18,645,889 bytes**.
- ZIP SHA256 `d03049caf6fc100662a9fe85d2f522c8a650b6b6307b286ce8f6dbed710a1eb5`.
- Verified ZIP CRC and all 49 included payload SHA256 hashes locally.
- Contains Y/Z real GLBs, real source/Run63 baseline compact GLBs, original reference crop, build/render/browser scripts, 12 VTK images, 16 WebGL screenshots, QA JSON, and logs.
- **Remote ZIP not archived:** an actual upload to a new Library experiment folder and subsequent upload both returned `AccessDeny`. Do not represent this local ZIP as a persistent public link. Text report here is independently persisted. The GitHub runner's Run10 parent artifact is available only until 2026-11-26, not permanent.

Nothing was paid or deployed, and no original `251`-species production files, manifests, original concept art, or existing cat prototype were touched. **Next**: acquire a real age-specific professionally sculpted three-view #172 chick and accurate soft groom; adult owl-foot/body transfer and extra geometry are not adequate; then actual handset PBR/animation tests before release.