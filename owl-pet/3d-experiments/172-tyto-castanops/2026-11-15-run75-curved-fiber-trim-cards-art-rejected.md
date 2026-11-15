# Run75 — #172 *Tyto castanops* v3: independent groomed down-card trim sheets (**ART_REJECTED**)

**Date:** 2026-11-15 Asia/Shanghai. **Zero additional spend. Not a finished or publishable electronic pet.** This is an isolated experimental failure audit, not a change to the existing 251-species production pipeline, concept art, manifests, prototype, or deployment.

## Preflight and prior-run ground truth

Read GitHub main `owl-pet/README.md`, `owl-pet/AGENTS.md`, `owl-pet/STATUS.md`, `owl-pet/prototype/index.html`, `owl-pet/research/species/172-tyto-castanops-v3.md`, `owl-pet/research/reviews/172-tyto-castanops-v3-review.md` and Run74 audit. (An initial lookup of **root** `AGENTS.md` returned 404; the actual `owl-pet/AGENTS.md` was subsequently successfully read.) Restored Run74 full 15,997,613-byte evidence ZIP from Google Drive file `1B0ZPVRH9brFFXUTkkktK9PQE038Yhmc3`, including real GLB, original owner's right-side cream mesoptile crop, multiview prior renders and code. The crop is one frontal concept view: neither its side nor back is independently verified.

## Executed technical work

Used the no-extra-cost, actually installed CPU tools **trimesh, NumPy, Pillow, VTK, Chromium, SwiftShader and Playwright**. Investigated an independent trim-sheet approach rather than again sculpting small bumps in an inadequate basic body. Wrote and executed `build_run75_groomcards.py`: painted a reusable 2×2 RGBA fiber trim atlas, then sampled a connected real body mesh and constructed surface-attached, tangent-directed **curved six-cross-section 3D clump cards** with alpha-mask texture. Front facial region was excluded from the fur. One batched additional mesh plus embedded atlas per asset.

The first geometry attachment was **wrong**: the legacy body uses a 90-degree node transform and the new fur was inadvertently left in world coordinates. Actual VTK front/side/back frames exposed a detached fur skirt at ground level. This was corrected by attaching the cards under the exact body node transform, and **both final exports were rebuilt and all rendering/tests repeated**. Wrong initial exports are not part of the release candidates.

Verified by GLB export and real re-import:

- 650-card variant: **22 geometries, 87,144 triangles, 5,319,720 bytes**, SHA256 `f86350c77d846c6ba9eb09daa045103fb3d357a0a9602e5fa27e3fe1f2acc74c`.
- 1600-card variant: **22 geometries, 96,644 triangles, 5,661,728 bytes**, SHA256 `8494b5dc72ac7a753dadf6ac995a811f577c9871a2e4a8832bdea0091ca4104f`.
- The source body remained **29,917 vertices** with unchanged base mesh, eye geometry and coarse original toes. New cards: 6,500 / 16,000 triangles respectively, one alpha-tested textured geometry. Two embedded PNG textures loaded in the WebGL smoke test.

Rendered **12 actual VTK glTF frames** (baseline/650/1600 × front/three-quarter/strict side/back) and comparative plates, then updated browser test to implement glTF alpha MASK cutoff and performed **16 actual Chromium WebGL2/SwiftShader draws** (two GLBs × four angles × 390×600 emulated portrait or 800×800 desktop). **0/16 WebGL errors, 0/16 JavaScript exceptions.** This is only a custom non-PBR raster smoke test; the browser clumps render noticeably darker than VTK, so even visual shader parity is **not** established. Simulated viewport is not a mobile phone hardware test.

## Actual art decision: **ART_REJECTED**

The 650-card coverage looks sparse and striped; 1600 cards become repetitive overlapping **shingles/scales, not soft natural cream mesoptile**. Crown outline is somewhat furrier but the silhouette and down texture are still inappropriate. Underlying body remains an unnaturally smooth bag/wedge, the heart-disc reads as a frontal photo projection, wing folds lack anatomical shape, back/side are not evidence-grounded, and feet are sharp low-grade geometry rather than down-buried juvenile toes with believable support. No verified actual-phone WebGL GPU, real PBR, animation or frame-rate criteria. **Neither asset is to be advertised or deployed as a successful sample.**

Software availability: no local Blender/bpy, PySide6, pybind11 or GPU/CUDA; container DNS cannot resolve GitHub or PyPI, so no executable professional external grooming stack was installed. Did not use paid services, paid model inference, or third-party reference photos as redistributed textures.

## Independently archived evidence

[Run75 full **53-file negative-evidence ZIP** in the independent ART_REJECTED Google Drive folder](https://drive.google.com/file/d/1kzaeEIOvWIvGMYghPliZXjiC0DTZ-f7S/view) — **19,415,632 bytes**, SHA256 **`4e9d3f05a4215d2137070e225753a6d96eb2bce9232a9bd1684066afa714a395`**. Contains original crop and previous baseline GLB, two *real* new GLBs, self-painted atlas, reproducible modeling/render/browser/QA source, 12 VTK views, 16 browser screenshots, side-by-side review sheets, errors/logs, signed-off ART_REJECTED quality JSON and SHA manifest. ZIP CRC and **52/52 internal SHA256** checks passed. Uploaded as a separate Google Drive file; then actually fetched **back** from remote and verified same complete 19,415,632-byte SHA256, ZIP CRC and 52 internal hashes. This link is **failed experiment evidence only**, not a demo link.

**Next direction:** no more density escalation or synthetic hair cards on the same sack. A genuinely new anatomically credible juvenile sculpture, real groom and independently established side/back references is prerequisite; after that, standard glTF PBR and physical-phone WebGL performance are separate gates. Keep production workflow isolated.
