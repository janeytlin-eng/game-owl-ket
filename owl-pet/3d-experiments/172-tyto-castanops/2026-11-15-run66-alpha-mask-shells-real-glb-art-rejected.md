# Run66 — #172 Tyto castanops v3 independent alpha-mask down shell experiment (ART_REJECTED)

Date: 2026-11-15 Asia/Shanghai. **No release, no deploy, no production changes.**

## Preflight / recovered source
Read current `owl-pet/README.md`, `AGENTS.md`, present prototype boundaries, #172 v3 visual target and Run65 independent rejection report. Recovered and actually unpacked the **Run65 44-file binary ZIP** from the independent research Drive archive at https://drive.google.com/file/d/1O0ORFCPipUQzJ9W-reaZvh_lkycQR70i/view; archive SHA256 `dc5855c8bec00880be991a3229f8cd8e6aa20e8470f3875d96ac83700b3b0b02`. Inspected the owner Gallery slide 172 **rightmost cream downy young owl**, source GLBs and prior 4-view QA. Baseline for new W/X was Run63 P recovered inside Run65: GLB SHA256 `15f70a269602bfd9ecc1e6435a3714c2120db702ca008c70655162710dabb388`.

## Executed tests and unexpected bug fix
Implemented an independent real 3D **4-vs-6 alpha-MASK spatial lofted fur-shell** experiment. Source owl body is a continuous 155x193 parametric grid with preserved 3D face, not SVG/billboards. New fur shells are curved offset surfaces with separately stochastic 1024x1024 RGBA maps, omitting the heart disc/eyes. This is a distinct alternative to the rejected pin-like 3D feather strands. Generated, exported and **re-imported** two new GLBs:
- W: 4 shell layers, 48,106 new fur-shell triangles, 117,870 total triangles, 7,137,668 bytes, SHA256 `cf43b9cb6b90bfd166edfdcdd2ee13feef3ecd92d8517ac6abb548344c42b5b3`.
- X: 6 shell layers, 72,024 new triangles, 141,788 total triangles, 8,617,632 bytes, SHA256 `ffb6d86cbee5ed4e371d4337cdf8876378c02ea1639e0937157a4915a94cee47`.

Found a major geometry defect during rendering: **all initial shell triangles pointed inward** (face-normal dot with source outward normals < 0 in 100% of sampled triangles). Reversed topology, rebuilt both GLBs and recomputed actual per-face outward-normal fraction = **1.000** on each round-tripped fur mesh. Verified all glTF fur materials retained `alphaMode=MASK` and per-layer base-color alpha textures. The browser test fixture was corrected to actually honor `alphaMode`/`alphaCutoff`, rather than quietly treating alpha textures as opaque.

8 rendered multiview VTK images (front/three-quarter/strict side/back), 2 contact sheets, and **16 genuine Chromium/ANGLE SwiftShader WebGL2 GLB draws** at 390×600 simulated-mobile or 800×800 desktop viewport; all 16 glError=0, no page JS exceptions, 5 and 7 embedded images loaded. This is **not** a standards-complete PBR loader or physical mobile test; no fps/animation/touch claim.

## Final art gate: ART_REJECTED (W and X)
Alpha-masked shells exhibit **speckled broken-paint/noisy foil** appearance rather than realistic creamy neonatal down; 6-layer X visually less flecked than 4-layer W but still unacceptable. Body remains pear-shaped with front-projected heart face, side/back lacking credible folded juvenile wings, claws and visual identity. Strong dark VTK side patches remain even after verified outward shell normals. Fur-only uncompressed RGBA memory ~16 MiB W / 24 MiB X plus source body texture and overdraw: not proven reasonable for mobile.

Explored zero-cost mesh alternatives: local trimesh/VTK/Chromium available but Blender, CUDA and local model weights absent. Located a CC0 adult great horned owl at https://grab3d.com/models/animals/owl/ and a CC0 museum barn-owl scan at https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc ; attempted downloading Grab3D's 13 MB light GLB in the sandbox, but the actual download failed. Neither is a verified anatomical/maturity match for the target. No money spent; no paid inference.

## Evidence and archive status
Created locally `Owl172_Run66_ALPHA_SHELL_ART_REJECTED_EVIDENCE.zip`, **23,924,740 bytes**, SHA256 **`c86eccb2b493edfca24d20f9b55df020ed8b8570fe1683925c045e8e6ab4bc23`**. Contains both new real GLBs, 44 other listed files/sha entries (45 ZIP entries total, 44 SHA256 checks), model-building/render/browser QA source, front reference, 8 VTK frames, 16 browser screenshots, VTK composites and 3-way comparison. Verified ZIP CRC and all 44 inner hashes. **Remote binary archive NOT COMPLETE:** persistent File Library create/upload returned AccessDeny; Drive connector rejected locally created file egress. Do not claim the binaries were saved to Drive or linked as public artifacts.

Only this independent text failure record is being saved on GitHub. Do not touch original 251-species production, manifests, original image, existing prototype or Sites. Next step: stop increasing shell layers, switch to professional juvenile sculpt and groom assets and real handset WebGL/PBR QA if a free accessible route becomes available.