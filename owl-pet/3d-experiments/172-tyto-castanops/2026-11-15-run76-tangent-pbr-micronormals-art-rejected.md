# Run76 — #172 *Tyto castanops* v3: game-oriented tangent-space down micro-normal GLB (**ART_REJECTED**)

**Date:** 2026-11-15 (Asia/Shanghai). **Zero extra spend, not publishable.** Isolated research under `owl-pet/3d-experiments/172-tyto-castanops/`; no changes to original concept plate, 251-species production, manifest, existing prototype or deployment.

## Preflight

Re-read GitHub `main` `owl-pet/AGENTS.md`, `README.md`, `prototype/index.html`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, and Run75 failure audit; checked latest commit was Run75 (`8891ee8eeca0fc52039a9152e82d4777fb5766fd`). Recovered the complete Run75 evidence ZIP from Google Drive (19,415,632 bytes), verified original SHA256 `4e9d3f05a4215d2137070e225753a6d96eb2bce9232a9bd1684066afa714a395`, and inspected its original rightmost owl crop, real baseline GLB, last modeling source and actual four-view renders. The concept crop is a **single frontal view**; side/back are not independent reference evidence. This is the age-unknown mesoptile, not a verified 5-week nestling.

## Actual executed independent experiment

Tried a **mobile-friendly glTF 2.0 PBR tangent-space normal-map route**, unlike the Run75 alpha-card groom. Built `build_run76_micronormals.py` with Pillow/NumPy/trimesh. Painted two independent curved-filament micro-height/normal textures, preserved the front heart-disc area using a UV mask, retained the original reference-derived body texture, and set glTF PBR `normalTexture`, `roughnessFactor=1.0`, `metallicFactor=0.0` on the continuous body mesh.

1. `velvet`: 35,000 short filaments; `owl172_run76_velvet_normalmap_ART_PENDING.glb`, **4,541,628 bytes**, SHA256 `65069fdebb6719de4515cf2edd8f04a7a357ca6790b93ba0e0af7561173a81fb`.
2. `coarse`: 15,500 longer filaments; `owl172_run76_coarse_normalmap_ART_PENDING.glb`, **4,231,412 bytes**, SHA256 `2a22a0e39fde4387a819e1e1cf3cfdfb45844cdd78b8684e255b12ad3354a8e4`.

Both **real GLBs exported and re-imported**. Each retains 21 geometries, **80,644 triangles** and 29,917 original connected-body vertices exactly unchanged; each re-import proves an embedded normalTexture exists, with original body topology intact.

Rendered **12 actual VTK four-view frames** (baseline and both variants × front / 3⁄4 / side / back), then created and actually executed a new normal-aware derivative-tangent GLSL raster test (`browser_qa_viewer_run76.js`), with full GLB binary parser and glTF texture extraction. **16 Chromium WebGL2 SwiftShader drawings and screenshots** across 2 variants × 4 angles × 2 viewports (390×600 portrait, 800×800 desktop); each loaded 2 textures, one normal-mapped body mesh, and no WebGL or JavaScript errors. This renderer is a **custom approximation**, **NOT a reference-standard glTF PBR renderer**, real mobile GPU or animation/performance test.

VTK per-frame RGB mean absolute change from the base was only **0.43–0.57 / 255**, too small for a meaningful art improvement.

## Visual art gate: **ART_REJECTED**

The tiny normal variation can perturb lighting but **cannot grow the plush cream mesoptile volume, repair silhouette, or make the side/back anatomical**. Actual rendered body still looks cylindrical, smooth, too wedge-shaped and missing believable folded short wings and buried tail. The heart disc still reads as a front-projected image, coarse feet are too exposed and angular, and a dark crown spot appears in the actual WebGL raster. Neither version resembles a professionally sculpted, age-unknown cream-down masked owl. The single front concept plate cannot substantiate the invented side/back anatomy.

No real-phone GPU test, authentic standard PBR material verification, animation or frame-rate measurements, so **neither model may be promoted to a playable pet sample**.

## No-extra-cost tool exploration and blockages

- Found current [SculptForge](https://github.com/islandmed/SculptForge) release **v0.13.2** (2026-11-14 UTC), which documents a headless CLI, glTF support, and open-source sculpting pipeline. The current container has no SculptForge binary, Blender/bpy, CUDA or GPU. Container-side DNS fails for direct GitHub and PyPI downloads, so actual SculptForge execution could not be verified. This is a **candidate, not a used tool**.
- Corrected earlier GroomLab speculation: the [official GroomLab download page](https://www.getgroomlab.com/) says **Maya 2022+ on Windows 64-bit** is required, not a standalone Linux Blender alternative. Do not build future Linux plan around it.
- Attempted a no-cost/zero-budget connected 3D-model recommendation read; it returned **interactive authorization required** in non-interactive context. No inference job, credits or purchase were attempted.

## Independent immutable failure evidence

[Run76 52-file full **ART_REJECTED** ZIP in dedicated Drive folder](https://drive.google.com/file/d/1Eaag_cEbNwjVgLZarJxX-3N3MethLurb/view) — **15,931,832 bytes**, SHA256 **`fc6b3dd1189ea3c2925d0cacf1667c689c813ba09f94a588ea87ce71aa08f669`**. Includes the source concept crop (owned reference), previous baseline GLB, both true newly exported GLBs and their embedded maps, reproducible Python, normal-aware GLSL browser test, 12 VTK renders, 16 actual browser screenshots, four review plates, logs, art rejection JSON, and SHA256 manifest. Uploaded separately; **materialized back from Google Drive** and verified byte-for-byte original equality, ZIP CRC and **51/51** internal SHA256 hashes.

**Next experiment direction:** stop treating geometry-free normal/roughness polish as a substitute for an anatomical sculpture. Acquire independently verified orthogonal views of the same age stage or gain access to genuinely professional sculpt/groom tooling; only after achieving anatomy, true fluffy silhouette, face depth and visible juvenile feet does mobile WebGL performance become a useful release gate. The GitHub artifact here is **research evidence**, not an interactive demo.

