# #172 *Tyto castanops* v3 — Run268 independent neural baseline and Hunyuan3D-2mini CPU attempt

**Date:** 2026-11-21 (Asia/Shanghai). **Release gate: NO_RELEASE.** This is a research-only run; do not equate a technical GLB with accepted, art-directed fluffy juvenile owl.

## Existing work checked BEFORE executing Run268

Re-read `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, Run267–267p audit, and preceding Run265b artifact metadata. Restored the actual [Run265b independently generated evidence](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44886196646/artifacts/14699737765) to the working container (3,743,794-byte ZIP, recorded SHA256 `0e0125972a1bb1e1a9ac964469cf999860e5d3717bebd2122f7173332c7397c9`). Visually opened original transparent rightmost juvenile image and genuine Run265b five-view TripoSR renders; image confirms cream down, heart face, distinct dark eyes, young round proportions and visible natural toes. Neural Run265b is physically three-dimensional but badly rotated/deformed with elongated coarse dark backside; not an acceptable artistic foundation.

## New ACTUAL quantitative geometry check of prior real model (local CPU + VTK)

Ran a newly executed VTK orthographic projection comparison using the exact original Run265b cleaned RGBA reference (SHA256 `9413b2b017001462f330fead80dd261100235975878b937c952d25984aba4540`) and Run265b native GLB (SHA256 `4ea732feea7f75c8ee348b68b7ef3f942250e7f2b9db2e406d326228e9d5cca0`). Tested six **real** 3D axial camera projections, normalizing the actual alpha silhouettes and scanning quarter-turns and mirrors for alignment to the reference mask; mesh has **37,028 triangles** and is **not watertight**. Scores below are **silhouette IoU only**:

| Projection | Best IoU |
| --- | ---: |
| +Z | 0.818009 |
| -Z | 0.817661 |
| +X | 0.814949 |
| -X | 0.814787 |
| -Y | 0.747031 |
| +Y | 0.746991 |

Reference silhouette bounding width-to-height ratio is **0.774713**. This newly measured result exposes a specific **false-positive problem**: several radically different axes achieve IoU ≈0.81 because a coarse oval volume matches an owl silhouette without resolving anatomy. It does **not** validate 3D orientation, iris, folded wings, feet, layered down, asymmetric face detail, or the side and back. **Do not use silhouette IoU as an acceptance gate by itself.**

## New distinct 3D generation route actually dispatched

Created an isolated branch with an executable Python runner `tools/run268_hunyuan2mini_cpu_native.py` and independent GitHub Actions workflow `.github/workflows/owl172-run268-hunyuan-mini-cpu-NO_RELEASE.yml`. Pinned the original source SHA, obtained the existing Run265b image without image regeneration, and launched **[Run268 genuine CPU inference workflow](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44904352532)**. It clones the upstream official Tencent Hunyuan3D-2 source, records upstream revision, installs a free local CPU inference stack, attempts `tencent/Hunyuan3D-2mini` `hunyuan3d-dit-v2-mini-turbo` (five diffusion steps, 128³ marching-cubes geometry) and, **only if a real mesh exists**, exports and reimports native GLB and renders six real VTK camera images. It signs its raw outputs with SHA256 and uploads an Actions artifact, whether inference succeeds or fails. At the time of this initial audit the workflow has been genuinely queued and is running its dependency stage; **do not claim that a Run268 GLB or art pass exists until its artifact is retrieved and visually checked**.

This is a genuine **new neural foundation engine**, not another round of additive geometric eyes, spikes, fake fluff, projected planar image rotations or an unexecuted plan. Model load and CPU inference may still fail due to memory/dependencies/weights; the Actions outcome and logs are authoritative. No third-party paid endpoint was called.

## Rights, device, isolation and next gate

Tencent Hunyuan source explicitly declares a non-commercial license. Therefore **even a visually excellent experimental output is NOT authorized for production release** without appropriate clearance. No actual Android/iPhone GPU, FPS, heat, memory or touchscreen test has been performed. Existing WebGL2 software checks from older runs do not transfer automatically to a new model; **Run268 WebGL remains UNTESTED**.

Only #172-specific research Python, isolated workflow and this audit have been changed on a research branch. No change to `main`, 251-species production, source concept images, vocabulary game, existing cat WebGL prototype or deployment. **ART_UNREVIEWED / WEBGL_UNTESTED / PHONE_UNTESTED / RIGHTS_UNCLEARED / NO_RELEASE.**
