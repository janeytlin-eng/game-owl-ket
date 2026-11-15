# Run71 — #172 *Tyto castanops* v3: juvenile anatomy relief + translucent 3D down ribbons (**ART_REJECTED**)

**Date:** 2026-11-15 (Asia/Shanghai). Independent experiment only, **not releasable art**. $0 spent. No changes to existing owl-pet prototype, original species assets, 251-species production pipeline, other manifests, or deployment.

## Preflight / source provenance
Actually re-read `owl-pet/README.md`, `owl-pet/AGENTS.md`, `owl-pet/STATUS.md`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, and Run69 / Run70 independent failed experiment records from GitHub main. Recovered [Run70 real 53-entry evidence archive](https://drive.google.com/file/d/16T__VtwC1Cp1Ej84WczJ7xsmftKoxfcy/view), verified archive CRC, extracted the user-owned rightmost cream mesoptile crop, baseline **real GLB** and scripts, and rendered baseline four angles. Baseline M GLB SHA256 `2a4baef490800a0bc28e08b762d06a8201ae1bbd2dfbfe158f10a224bac7be6c`. Original concept is frontal art; age is UNKNOWN, no validated side/back photographic reconstruction.

## Actual new 3D work
Wrote, executed, corrected, re-executed and archived `build_run71.py`. Unlike prior repeatedly assembled primitive wing pads, this trial **deformed the existing closed nonparametric continuous surface**: differentiated round head from softer neck and lower belly and sculpted bilateral shallow diagonal folded-wing masses and trailing fold grooves directly into the surface. Retained true UV-coordinate duplicates while welding coincident 3D positions.

Second variant sampled the *actual 3D triangle surface by area* and built 10,000 distinct curved translucent ribbon strands with texture-conditioned cream/tawny vertex colours and tip-alpha gradients. Explicitly patched glTF hair primitive material to `alphaMode=BLEND`, `doubleSided=true`, nonmetallic roughness 1. This is actual volumetric 3D geometry; not a front billboard, SVG or 2D-only drawing. First glTF material patch attempt raised KeyError because the exported colour mesh omitted a material index; fixed to create an explicit compatible PBR material and re-exported.

Reimported and mechanically checked both GLB candidates:
- **A_sculpt:** 17 meshes, 69,764 triangles, 3,706,296 bytes, SHA256 `2972221e4fbb2d3c0a4febddd93310cadfcbcf0525177b7bc2b03f3f694aaf29`.
- **B_fur:** 18 meshes, 99,764 triangles, 5,226,644 bytes, 10,000 actual 3D down strands + 30,000 triangles, SHA256 `e909e0fabf99443232a3590d454b7f1269f24fc146e171cd6a82a6c8aeb229c7`.
- Both have consistent, closed body topology after geometric UV seam welding, positive volume about 0.50367, max body vertex displacement 0.03833 model units vs Run70 M.

## Real render / browser QA
Executed **12 VTK glTF2 balanced studio renders**: baseline/A/B × front/three-quarter/strict side/back; generated comparison views. For B, RGB absolute render delta versus baseline on identical camera/light was front 3.311/255, 3/4 3.089/255, side 2.345/255 and back 2.655/255. Actual renderer actors loaded (17/18 for candidates). Executed **16 Chromium WebGL2 actual drawing and screenshot tests**: A/B × simulated phone 390×600 and desktop 800×800 × four angles; all 16 had `glError=0`, 1 embedded image loaded, no browser exceptions. The simple browser test was improved to respect vertex alpha, glTF BLEND and depth-mask semantics.

These use desktop software ANGLE/SwiftShader and a small hand-written glTF renderer; **do not constitute physical-phone GPU, performance/FPS, standards-complete PBR, feather depth sorting under all lighting, rig or animation acceptance**.

## Human visual assessment: **ART_REJECTED**
Reviewed actual VTK four-view sheets and browser three-quarter screenshot. The continuous wing geometry reads as a lateral shoulder bulge, not convincing down-buried juvenile wings. Semitranslucent ribbons form peripheral stubble and small surface speckles, not voluminous cream down. Face continues to look largely like a front photograph stamped on a bag-like body, oversized stylized pale feet/toes fail age-appropriate anatomy, and side/back are not independently grounded. **Neither openable GLB meets art/phone gate, so do NOT announce, promote, deploy or substitute it for the electronic pet.**

## Independent immutable negative-evidence archive
[**Run71 55-entry research-only ZIP on Google Drive**](https://drive.google.com/file/d/1PPCF89vg6lgO2pWWPkxvzTDLgbBRt59z/view) contains A and B real GLBs plus Run70 baseline, full reproducible modeling and QA source, owner rightmost crop, 12 VTK rendered PNGs, 16 browser screenshots, side-by-side visual comparisons, machine QA JSON and SHA256 manifest. **14,715,496 bytes; ZIP SHA256 `6692f4b7c41331b4635fb6a7c26a3f8bf17a8742dd2ff3b1cf8c79a024a0946c`**. New upload saved independently in existing `Owl172_3D_research_ART_REJECTED` folder; remote Google Drive fetch returned exactly 14,715,496 bytes, and re-materialized archive checksum, ZIP CRC and all **54/54 internal SHA256 checks passed**.

## $0 alternatives and limitations
Actual local imports confirmed `trimesh`, `vtk`, `scipy`, `numpy`, `PIL`, `Playwright/Chromium`; `bpy/Blender` and CUDA GPU absent. HTTPS attempts from container to GitHub/PyPI/Blender/Grab3D failed at DNS. Read external owl chick visual context on web without inserting third-party photo into model; explored free candidate assets but adult species and unclear rights cannot be claimed as the target mesh. Attempted fal image-to-3D catalog discovery; connector responded `User input required but current turn is running in a non-interactive mode`; **no inference and no paid charges**.

**Meaningful next threshold:** stop surface-level tuning of the poor bag-like baseline; obtain legitimately licensed, artist-quality chick multi-angle anatomical sculpture and natural strand-groom, then optimize GLB with true device-based WebGL/PBR frame timing. Continuing to turn triangular fluff stubble into a “success” would misrepresent the art gate.
