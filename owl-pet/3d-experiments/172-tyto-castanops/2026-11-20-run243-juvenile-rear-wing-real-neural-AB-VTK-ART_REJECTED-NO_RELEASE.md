# #172 *Tyto castanops* v3 — Run243 neural 3D rear-wing anatomy study

**Date:** 2026-11-20 Asia/Shanghai  
**Decision:** `TRUE_NATIVE_NEURAL_GLBS / REAL_SOFTWARE_WEBGL2_PASS / ART_REJECTED / PHYSICAL_PHONE_UNTESTED / NO_RELEASE`

## Baseline recheck

Re-read owl-pet/AGENTS.md, README, STATUS, and the Run242 original audit and original 14-view evidence. The right-most concept remains a **cream-white downy young Tyto**, with a soft natural heart face, compact squat body, down-buried short folded wings, short hidden tail, two supported feet and an aged broad hollow eucalyptus ledge. Its exact age is not established. Main remains untouched; the deployed interaction prototype is still a cat, never confused with the desired bird.

The original Run242 ZIP was physically downloaded and decompressed, passed the ZIP CRC audit, and matched the **6,186,461-byte** official artifact SHA256 `72d59b3135983fa9a4712486e52526cc90c023a9fcd0b0e6669dfd4d9864d2db`. The pinned **real Hunyuan neural 3D** source GLB was independently re-imported: 3,831,092 bytes, SHA256 `ef60639bbba95a0e876ac427b277fa500063b9ce05d9b9c8bae5811a5c0518d1`, 8 meshes and 86,867 real triangles (46,856 continuous learned body triangles + 36,651 surface-following down triangles + six separate 3D eye elements).

## What was actually attempted

Instead of repeating the previously failed global width contraction, Run243 works in localized y/z directions on the original continuous learned body. It moves the far rear/low tail volume upward and forward, reduces lower side wing projection, preserves original eye/pupil/catchlight meshes and original full triangle topology, and applies constrained Taubin smoothing to side ridges. No sphere/ellipsoid owl assembly, SVG, or 2D rotating photograph. Two reproducible variants were tested locally:

- **C:** 0.18 upward tail, 0.20 rear-forward, moderate folding and surface smoothing. Output: native GLB **3,831,092 bytes**, SHA256 `2d8aa37a28c02577664db34706e5509dab44c174ae2d606e6bd38c097a8cef20`. Learned-body maximum local displacement 0.23749 scene units. 8 original meshes / 86,867 original triangles preserved.
- **D:** 0.31 upward tail, 0.28 rear-forward, stronger folding. Output: native GLB **3,831,096 bytes**, SHA256 `f9e4cc8c067795bb5670f5af574f34d3f678d14548abc18a092fd6d2b5851935`. Learned-body maximum local displacement 0.36761 scene units. 8 original meshes / 86,867 original triangles preserved.

The local Python implementation, native re-import reports, source-integrity gate, three-dimensional vertex bounds and 21-view comparison were actually executed. Real 3D raster screenshots were generated with **VTK offscreen GLTFImporter** from source A, candidate C and candidate D, using seven distinct spatial cameras per model. VTK output is an exploratory *software raster review*, **not** a genuine-browser/WebGL gate. It lacked the proper final lit cream material in the VTK view, so its color is not representative; geometry silhouette comparison remains meaningful.

## Independent visual result — REJECT

The 21-view comparison shows C partially lifting/foreshortening the trailing lower silhouette while retaining the adult-like engraved wing ridge. D creates a more artificial pinched/notched rear wing-to-tail transition. Both remain visibly adult-wing-shaped at profile and do not acquire the original downy owl chick's soft natural geometry, especially at sides/back. True juvenile layered second-down is still missing at browser framing, face mask remains hard/ring-like, and there is no realistic wide tree hollow ledge. C/D are **not** a release baseline. Repeated 3D deformation cannot substitute artist sculpt/retopology.

## Remote reproducibility and integrity

A fresh **isolated research branch** has been created with the new reproducible [Run243 Python source](run243_genuine_neural_juvenile_rear_anatomy_ab.py) and dedicated GitHub Actions workflow `.github/workflows/owl172-run243-real-neural-rear-wing-webgl.yml`. It pins the original valid Run242 A SHA; produces two actual GLBs, attempts Chromium GLTFLoader/WebGL2 seven distinct cameras each, saves original GLBs and screenshots as a temporary research artifact, and commits small machine reports and contact sheet to the isolated branch. **This earlier pending checkpoint is superseded by final verified remote results below.**

A first remote workflow commit used a wrong inherited artifact name; it was corrected by a second commit to the actual Run242 artifact name. The corrected workflow was then triggered by a new push. The research branch does not modify `main`, 251-species production, the existing cat UI or deployment. No paid service, subscriptions, or GPU purchases. Extra spend **USD 0**.

## Next experiment directions and gates

The specific negative result is that partial learned-surface y/z warping leaves adult flight-feather topology in the silhouette. Next viable step is a qualitatively new true-3D professional short folded-wing/resculpt or independently sourced legal juvenile asset, plus genuine multi-layer down groom and valid hollow eucalyptus mesh; then actual browser and *physical phone* render/interaction checks. No inferred physical GPU performance from native GLB validation or VTK. **NO_RELEASE**.

## Final verified remote result and binary evidence (supersedes pending checkpoint)

[Corrected Run243 Actions 44714815561](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44714815561) finished successfully with pinned true-3D source SHA, two neural continuous-mesh edits, native GLB reimport, **14 genuine Chromium Three.js WebGL2 spatial-view screenshots**, strict nonblank/distinct-camera, normals, material/alpha and image SHA tests, and isolated research evidence commit. An initial [wrong inherited artifact-name run](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44714172429) failed. The [first corrected successful compute run](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44714203753) then hit a **non-fast-forward evidence commit push conflict** after this audit was added. The workflow was fixed to rebase before pushing, and final run succeeded; these failures were not disguised as model success.

Remote native C: **3,831,092 bytes**, SHA256 `e97a843849726e0e385797d44c53a7e584ce9aed6ba090d33b9da8e776333a52`. Remote native D: **3,831,096 bytes**, SHA256 `3c3fb6fe37c3841c911f056d35dedb2f385d1ab1578ffb8be701b420b0fd8190`. Both independently reimported as **8 real meshes and 86,867 triangles**, with original eye components and UVs intact. Local exploratory hashes from the independent local script are *not* the remote binary hashes; do not conflate them.

The [actual permanent 14-view browser contact](run243-evidence/run243_CD_14_ACTUAL_WEBGL2_VIEWS_ART_UNAPPROVED_NO_RELEASE.png) is **300,885 bytes**, SHA256 `259ef14eb9e5105bd67ddd65b80d1401ad07c02cf0ba9be7636d51111bac3dc4`. [Machine report](run243-evidence/run243_machine_report.json) and [browser report](run243-evidence/run243_webgl_report.json) are also now committed in the research branch. Both passed actual Chromium WebGL2 on **ANGLE SwiftShader software renderer**; no physical Android/iPhone GPU testing took place.

The [original complete remote evidence ZIP](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44714815561/artifacts/14619221675) was downloaded and independently re-opened: **6,094,132 bytes**, SHA256 `18c04ecd76a1571d9326a2e51b7c3f3c651629d0da92a7255156cd4888952f2c`. All **22 ZIP entries** passed CRC, both true-GLB sizes and SHA256 matched the machine report, all **14 original screenshot SHA256 claims** matched their bytes, and the permanent contact hash was verified. The ZIP is temporary and expires on **2026-12-20**, not a permanent or approved model release.

**Final independent artistic verdict: REJECT.** Real browser profiles show both variants still have the adult-style long carved folded wing/tail; D produces an artificial notch in the rear, while rear down and cheeks remain insufficiently juvenile. The face/eyes are too hard/ring-like, the visible feathering too sparse to resemble thick cream mesoptile, and a wide realistic eucalyptus hollow support is absent. These are true 3D tests, but not aesthetically acceptable electronic-pet characters.

This branch differs from Run242 only by Run243 research Python, workflow, audit, machine JSONs and authentic browser contact. No main/251-species production/deployed cat code modified, no external paid spend. **NO_RELEASE.**
