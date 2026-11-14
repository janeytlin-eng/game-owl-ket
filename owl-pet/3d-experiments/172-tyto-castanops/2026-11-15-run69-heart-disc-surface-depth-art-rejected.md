# Run69 — #172 Tyto castanops v3: actual volumetric heart-disc sculpt (ART_REJECTED)

Date: 2026-11-15 Asia/Shanghai. **Independent experiment, NOT a release.** No deployment, payments, production modifications or changes to the 251-species flow.

## Mandatory preflight
Read current `owl-pet/README.md`, `AGENTS.md`, `STATUS.md`, `research/species/172-tyto-castanops-v3.md`, and `research/reviews/172-tyto-castanops-v3-review.md`. Recovered and verified previous [Run68 real evidence ZIP](https://drive.google.com/file/d/1v-h9pQVI65gWa6O9l2g1tkKRs8I4mA4W/view) (25,633,509 B, SHA256 `5721cdc680a7bf63d2b2de3621755154352180cf3d9e3a5d62d924047b00140c`); checked its real GLB, original #172 rightmost cream young reference, UV texture, light-calibrated four-angle renderings and browser QA. Also recovered Run65 source/build evidence and re-read the latest [Run68 rejection record](https://github.com/janeytlin-eng/game-owl-ket/blob/main/owl-pet/3d-experiments/172-tyto-castanops/2026-11-15-run68-pbr-lighting-uv-seam-art-rejected.md).

The approved source is an age-unknown thick-cream-mesoptile concept with a developed heart mask, down-buried short wings, concealed tail and supported feet. It is not a photogrammetric scan or an independently known side/back anatomy.

## Actually executed new 3D modeling experiment
Wrote and executed a distinct reproducible `build_run69.py` sculpt that changes vertex positions on the **existing continuous true 3D body**, not a front-facing image card. A closed, approximately heart-shaped 3D spline and normal-oriented surface influence create shallow raised disc borders, cheek volume, depressed eye sockets and fine local relief. Changes deliberately isolate frontal face depth; source back, feet, wings and UV atlas are not retouched.

Two independently exported and **re-imported GLB** candidates:
- A_subtle: 19 meshes, 82,756 triangles, 4,312,580 B, 4,181 changed body vertices, peak displacement 0.02181 source-model units, SHA256 `d0bf97dad5d50b10a373ee29fcef82a7892e6311116e930f5262d49c15eb8d1a`.
- B_deep: 19 meshes, 82,756 triangles, 4,312,580 B, 4,466 changed body vertices, peak displacement 0.04362 units, SHA256 `4ef130bdf5c32ad04edfb27665334a73d0e741d773208322bbab655b7c506ac2`.
Baseline Run68 seam32 GLB SHA256 `5a8b307f0c9d434ca5466311a14001c3e717f07f58a9a9e2df0c7c67fe794aa4`.

A naive trimesh watertight query falsely reported open body due to intentional coincident *UV seam duplicates* with different texture coordinates. Geometric seam welding while ignoring UV/normals confirmed watertight and consistently-wound bodies with **positive signed volumes** (A about 0.5856; B about 0.5864). The released-binary candidates retain proper UV vertex duplicates: no physical gap was identified.

Ran **12 actual VTK glTF2 import + balanced studio four-view renders** (baseline/A/B × front, three-quarter, strict side, back), four comparison images and three four-view sheets. Quantified mean absolute front rendered RGB difference versus identical-scene baseline: A 0.248/255, B 0.482/255, back image bit-identical. Executed **16 Chromium ANGLE SwiftShader WebGL2 actual GLB draws** (A/B × simulated 390×600 mobile view / 800×800 desktop × four viewpoints), saved 16 screenshots; all 16 glError=0 and no page JS exceptions. These results DO NOT imply real mobile hardware GPU, 3D animation/FPS or standards-complete PBR success.

## Art acceptance
**ART_REJECTED for both A and B.** The true-surface facial relief makes only marginal local shadow change. The character still looks like a pear-shaped smooth body with a front-projected photo face, sticker-like oval wings, implausible juvenile feet, weak side/back anatomical identity and no convincingly fluffy creamy down. The render difference is too small to fix the fundamental anatomy/groom deficiencies. No publishable/openable *good-quality* character exists in this experiment, so **do not publish these GLBs or notify as a demo**.

## Free route constraints
Explored existing free [Blender procedural feather geometry nodes](https://blendatlas.com/products/procedural-feathers-with-geometry-nodes-blender-project) and an [MIT procedural-animal repository](https://github.com/majidmanzarpour/threejs-procedural-animals) as leads, not as integrated models. Current sandbox had no Blender/bpy, CUDA GPU, model weights, or binary-asset outbound DNS; available tools include trimesh, scipy, VTK and Chromium/Xvfb. Attempted fal image-to-3D discovery with strict **$0 budget**; connector required interactive user input, so **no inference was submitted and no credits charged**. Third-party reference photos were not inserted into model textures.

## Independent evidence, integrity, persistence
[**Run69 complete real-3D failed research ZIP on Google Drive**](https://drive.google.com/file/d/1kdGebnTyJ6-ZcRfEuWJXiXeyLtta_9R7/view) — 14,981,889 B, **56 ZIP entries**, both actual GLBs plus baseline GLB, owner concept crop, build and QA source code, 12 VTK frames, 16 browser WebGL screenshots, comparison sheets, machine QA JSON and SHA256 manifest. ZIP SHA256 **`02b17f0977e6823689fe41b079621ecdcd8009dd1d9dfb9eeb1e0f5e1c798bd4`**. Uploaded as a new independent file to existing `Owl172_3D_research_ART_REJECTED` Drive folder. Re-materialized the **remote** ZIP; byte hash identical to local copy, CRC clean and **55/55 internal SHA256** checked. This is reproducibility/negative evidence, not a player-ready 3D character.

No changes to original concepts, prototype, production manifests, species ledger, root game, or hosted Sites. **Next meaningful quality threshold:** professional infant-owl sculpt/skin/feather groom with trustworthy side/back references, followed by actual phone WebGL2/PBR performance and multi-angle QA. Avoid more primitive layer/UV-only cosmetic changes being presented as progress.
