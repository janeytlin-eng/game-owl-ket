# #172 *Tyto castanops* v3 — Run243 neural 3D rear-wing anatomy study

**Date:** 2026-11-20 Asia/Shanghai  
**Decision:** `REAL_LOCAL_NEURAL_3D_CREATED / ART_REJECTED / PHONE_UNTESTED / NO_RELEASE`

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

A fresh **isolated research branch** has been created with the new reproducible [Run243 Python source](run243_genuine_neural_juvenile_rear_anatomy_ab.py) and dedicated GitHub Actions workflow `.github/workflows/owl172-run243-real-neural-rear-wing-webgl.yml`. It pins the original valid Run242 A SHA; produces two actual GLBs, attempts Chromium GLTFLoader/WebGL2 seven distinct cameras each, saves original GLBs and screenshots as a temporary research artifact, and commits small machine reports and contact sheet to the isolated branch. **The remote job is not yet certified as completed in this checkpoint**; do not claim remote browser, phone, or art success.

A first remote workflow commit used a wrong inherited artifact name; it was corrected by a second commit to the actual Run242 artifact name. The corrected workflow was then triggered by a new push. The research branch does not modify `main`, 251-species production, the existing cat UI or deployment. No paid service, subscriptions, or GPU purchases. Extra spend **USD 0**.

## Next experiment directions and gates

The specific negative result is that partial learned-surface y/z warping leaves adult flight-feather topology in the silhouette. Next viable step is a qualitatively new true-3D professional short folded-wing/resculpt or independently sourced legal juvenile asset, plus genuine multi-layer down groom and valid hollow eucalyptus mesh; then actual browser and *physical phone* render/interaction checks. No inferred physical GPU performance from native GLB validation or VTK. **NO_RELEASE**.
