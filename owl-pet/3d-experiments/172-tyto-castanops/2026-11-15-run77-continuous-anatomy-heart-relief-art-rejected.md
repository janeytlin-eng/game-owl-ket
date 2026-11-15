# Run77 — #172 *Tyto castanops* v3 independent continuous anatomy and face-rim ablation (**ART_REJECTED**)

**Date:** 2026-11-15 (Asia/Shanghai). **Not a publishable 3D pet. Zero additional spend.** This file is an isolated research audit only; the 251-species production workflow, original source artwork, manifests, existing cat prototype and live deployment remain unchanged.

## Preflight and input provenance

Read GitHub `main` `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, the existing `prototype/index.html` (currently a separate, non-owl cat WebGL prototype), the #172 `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, and Run74–Run76 failed QA audits. The latest prior GitHub commit was `400e87854236316e8377a6b5b51c8fefe0dec233`.

Recovered the complete Run76 **15,931,832-byte** ART_REJECTED ZIP from Google Drive and verified its previously recorded SHA256. Examined the real GLB, rightmost owner's cream mesoptile crop and multiview renders. The crop is a **single frontal illustration**. There are no independent orthogonal young-owl anatomical references; exact nestling age remains unknown. The art reference is not proof of the biological side and back.

## Actual experiment: four exportable 3D candidates, not primitives/SVG

Using locally available free `trimesh`, `NumPy`, `SciPy` KDTree, Pillow, VTK, Chromium and Playwright, implemented `build_run77.py`. Started from the real UV-mapped, connected Run74 body (59,520 body triangles); modified the existing **29,917-vertex 3D skin** directly to test tapered neck/head/chest, non-uniform rear crown/scapular surfaces, carved bilateral short-wing root folds and continuous heart-disc 3D depth. No additional separate sphere/ellipsoid 'wings' and no fake 2D model. The front skin/UV remains tied to the previous owner-reference-conditioned texture.

Actually built, exported and re-imported four GLBs:
- `gentle` — 3,845,524 bytes, SHA256 `cb664e95da1fd1702f8fa6a295061e361352b94a78a5dfa0dbac53a6c99252a6`.
- `pronounced` — 3,845,524 bytes, SHA256 `484a6214b7ee960b794377df6c5a8c5dbb2c053de7b4a1af121251a9593b005c`.
- `lowrim` — 3,845,524 bytes, SHA256 `f56581a7e32e173d416db119e9ffe65345cc208d7e6d18be2cd3c64eeff39115`.
- `silhouette` — 3,845,520 bytes, SHA256 `a4a9a0e2f29fe22111327dcb32b9f4160d5b771f11a30e655be77dc702a8ee91`.

All four have **21 geometries and 80,644 triangles**, keep original body topology and pass a *welded-at-UV-seam* body watertightness, consistent-winding and positive-volume check. This confirms technical mesh validity only, not correct owl anatomy or art.

## Actual QA

Rendered **20 actual VTK views** (baseline + four candidates × frontal, three-quarter, strict side, rear), plus four same-camera comparison plates; inspected all four candidate four-view contact sheets. Against the baseline, average VTK pixel differences were modest: `gentle` 1.88–2.72, `pronounced` 2.67–3.90, `lowrim` 2.05–2.35 and `silhouette` 2.39–2.77 RGB levels out of 255. These are changes, **not** reference fidelity measurements.

The initial `gentle` and `pronounced` physically sculpted heart rim generated conspicuous dark striped tearing along the face, especially the upper right of the mask. Revised `lowrim` (13% face strength) and `silhouette` (0% face sculpt) reduced these defects but did **not** deliver true three-dimensional mask sculpt or natural face/eye anatomy. All variants retain over-smooth, somewhat bag-like bodies, crude visible adult-like feet, no convincing natural cream fluff silhouette, and fake/unsupported-looking wings in side/rear. This is a **clear art rejection**.

Additionally loaded the two revised GLBs in an actually executed local Chromium WebGL2 GLB viewer using software SwiftShader, generating **16 actual browser canvas screenshots** (two variants × four angles × 390×600 mobile-emulated and 800×800 desktop viewports) with **0 WebGL errors and 0 JS errors**. The custom shader is **not reference-standard glTF PBR**, the 390px viewport is **not a real phone**, and no phone GPU, 3D animation, frame time or battery/performance measurements exist. No claim of mobile shipping readiness.

## Explicit release gate: **ART_REJECTED**

Even the best candidate fails core art gates: dense cream down, authentic heart-face sculpt, accurate short down-buried juvenile wings, credible multiangle skeleton/proportions and visible supported juvenile toes. There is no evidence-based rear/side anatomy from the one source view. **Do not use, present or link to these candidates as acceptable electronic pet samples.**

## Independently archived negative evidence — remote verified

[Run77 rejected 66-file full ZIP archive (research failure only)](https://drive.google.com/file/d/1yDm7VbiGAROn8gl66zN5ufnyw1dcxyIf/view?usp=drivesdk)

- Exact **21,003,928 bytes**, SHA256 **`357e7f1c6e4feedfae4ebfd428d0089912b65c71e608a4a8544f6da0d540d6d5`**.
- Original one-view crop, prior real baseline GLB, 4 actual new GLBs, all source scripts and logs, 20 VTK camera screenshots, four comparatives, 16 Chromium WebGL screenshots, build statistics, quality decision JSON and all-file hashes.
- Verified locally ZIP CRC and **65/65** internal SHA256 hashes; uploaded to the existing dedicated Google Drive `Owl172_3D_research_ART_REJECTED` folder, **materialized the saved file back** and verified identical SHA256, byte-for-byte equality, ZIP CRC and **65/65** internal hashes again. Never deployed.

## Updated direction

This test narrows the failure cause: surface-coordinate facial relief distorts the photo-conditioned UV mask without improving natural mesoptile anatomy. Further micro-warping the inherited body is unlikely to meet the quality threshold. Seek a genuinely new child-owl anatomically credible multisided sculpt and real feather/down grooming from a usable **zero-additional-cost** professional modeling stack; only then test against an actual mobile GPU with an ordinary glTF PBR renderer. No paid service accessed, authorized, or charged.