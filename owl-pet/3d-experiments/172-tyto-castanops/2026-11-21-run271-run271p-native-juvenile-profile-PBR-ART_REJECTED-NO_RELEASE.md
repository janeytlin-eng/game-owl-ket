# #172 *Tyto castanops* v3 — Run271/Run271p true native 3D juvenile profile sculpt, explicit PBR normal repair — ART_REJECTED / NO_RELEASE

**Date**: 2026-11-21 (Asia/Shanghai). **Scope**: isolated #172 rightmost cream-down juvenile electronic-pet research only. Upstream Hunyuan neural mesh is **NONCOMMERCIAL**; none of the resulting models may be promoted to production. No external credits purchased.

## Before producing anything: source, project and failure review

Read [owl-pet/AGENTS.md](../../AGENTS.md), [README](../../README.md), [STATUS](../../STATUS.md), existing cat WebGL prototype description, and the Run270 art rejection. Recovered the actual [Run270 source artifact](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44914000728/artifacts/14710478257), **2,452,679 bytes**, SHA256 **e113c72453bd57c2082f11b012d44aac06f678d6c7515f199e92c0590ab13670**, ZIP CRC good. Pinned the genuine single continuous Hunyuan GLB SHA256 **d90960a228b8de1f9479318200fa0b031a599bd3720103fbe2c51c05703721f2**, 66,596 vertices / 133,268 connected triangle faces, watertight. Independently re-opened all six original VTK views.

Recovered and opened actual [Run265b clean original source reference](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44886196646/artifacts/14699737765), specifically the 512px rightmost cream-white chick with dense soft down, rounded cheeks/chest, heart-shaped face, large dark eyes, very short folded wings and two feet. No reference substitution.

The prior Run270 face/eyes improved, but side/back remained an adult wedge with tapered tail, hard contiguous long wing and crusty rear surface. A surface-only change cannot guarantee artistic progress.

## Run271: actual A/B sculpt of the SAME native organic mesh

Implemented and **actually ran** [tools/run271_juvenile_back_proportion_ablation.py](tools/run271_juvenile_back_proportion_ablation.py) using free NumPy, SciPy, Trimesh, VTK and Pillow.

- Both variants begin from the **original continuously connected authentic neural mesh**, without adding spheres, patches, extrusion planes, SVG or separate shapes. The original 133,268 face connectivity and 66,596 vertex count remain. The front-most facial-eye vertices are protected by rear-localized deformation, not recreated with geometry.
- **gentle:** smooths coarse posterior micro-surface by a spatially smooth VTK WindowedSinc field; expands the upper rear slightly, compresses the low projecting rear, lifts its bottom portion and subtly broadens the thorax. 53,327 vertices moved over .001 model units in the local execution; max displacement .26279.
- **round:** more aggressive posterior smoothing and shorter lower-rear contour; 54,408 vertices moved over .001 locally; max displacement .40742. Anatomical front eye vertices moved less than .00003 model units in both cases.
- Independently exported and re-imported each actual glTF 2.0 GLB. Both are native genuine 3D connected watertight meshes. Rendered six **different, genuinely 3D camera positions each**, front, three-quarter, right, back, left and overhead, for **12 rendered images**. Prepared an actual source/gentle/round 3×4 contact sheet.

**Actual image inspection (local and remote) — ART_REJECTED:** Gentle has a shorter posterior wedge and a slightly rounder three-quarter body, but the low tail/wing still narrows sharply into a vertical spike. The stronger round variant creates a more obvious abrupt projection and a back horizontal crease; neither resembles the compact, feather-puffed reference's side silhouette. Both retain adult-length hard folded wings, smooth plastic-like chest texture instead of cream-white mesoptile down, rough/bumpy posterior, overlarge prominent feet and no credible old eucalyptus cavity/foot grip. The facial identity is retained but this is not a juvenile pet-worthy sculpt. The stronger sculpt is **not an art improvement**, and neither model is a new accepted baseline. No release.

## Run271p: actual glTF normals and mobile-style matte PBR correction

After inspecting the actual Run270 GLB JSON, discovered its only primitive had POSITION+COLOR_0 and **no NORMAL**, and lacked an explicit PBR material. This can lead to device-dependent default metallic/lighting appearance. First Run271 CI made similarly incomplete GLBs. **Run271p actually repaired the exporter**, without changing the vertex geometry: exported genuine normals with trimesh glTF exporter \`include_normals=True\`, and inserted a nonmetallic opaque matte PBR material via GLB JSON tree_postprocessor:
\`metallicFactor: 0.0\`, \`roughnessFactor: 1.0\`, \`baseColorFactor: [1,1,1,1]\`, with actual COLOR_0 vertex colors and NORMAL attributes.

Local and final remote binary postflight independently confirmed **66,596 finite unit normals (norm range ~0.99999994–1.0), 66,596 vertex colors, 133,268 native triangles, a single native mesh, watertight**, explicit matte material, no image-plane substitute. This is **valid material/normal metadata**, not proof of hardware GPU performance or acceptable fur art.

## Remote actual execution, independent binary and image evidence

First [Run271 action 44918227824](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44918227824) produced two true native GLBs, 12 spatial views and comparison evidence, but lacked explicit GLB NORMAL/PBR attributes. The corrected [Run271p actual action 44918354692](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44918354692) completed the source retrieval, free-tool install, native mesh sculpt, dual GLB export, 12 distinct renders, fresh independent binary reopen/verification, visual comparison creation and evidence upload successfully.

The final [Run271p research artifact (NOT a released pet)](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44918354692/artifacts/14712826229) was **actually downloaded** and independently audited:

- Original ZIP: **7,158,669 bytes**, SHA256 **568f85a5f02a2eb977537a24b266740dcd36dcfb6b208366e3a290907fb1269b**, matches GitHub digest. **21/21 ZIP CRC files valid; 19/19 signed file hashes match**.
- **gentle GLB**: 3,465,408 bytes; SHA256 **da21a63c0ec7dbdb8da920896599eb7cafd62fcf94de2e25bae016dd218724ea**; native 66,596 vertices / 133,268 triangles, watertight, NORMAL + COLOR_0 + explicit matte PBR all rechecked.
- **round GLB**: 3,465,404 bytes; SHA256 **5af3b4b6d3f67f33fade3f3de6c5b810c4b22518778e0b63bcf6b4dbdae2f36e**; same genuine native 3D topology, material and numeric normal checks.
- Actual six spatial renders for each variant have distinct SHA256. 974,842-byte \`ACTUAL_12_IMAGE_SIDE_BY_SIDE_QA.png\` shows original and both variants side by side; image was opened and inspected, with art refusal confirmed independently.
- A separate local 20-file experiment ZIP was also CRC/SHA256 checked, but local workspace is ephemeral, so the **GitHub Actions research artifact**, not the local backup, is the verified durable temporary evidence (expires around 2026-12-21).

## Real barriers and disposition

**TRUE_NATIVE_CONNECTED_3D_PASS / FINITE_NORMALS_AND_NONMETALLIC_MATTE_GLTF_PASS / SIX_VIEWS_PER_VARIANT_PASS / ART_REJECTED / SOFTWARE_WEBGL2_NOT_TESTED_FOR_RUN271P / PHYSICAL_PHONE_NOT_TESTED / HUNYUAN_NONCOMMERCIAL / NO_RELEASE**.

Local Chromium was actually attempted with default, ANGLE SwiftShader and native SwiftShader switches at 390×780; every \`canvas.getContext('webgl2')\` returned null. Do NOT extrapolate prior software WebGL2 successes to this new GLB. No Android/iOS hardware FPS, GPU memory, touch, or thermals tested. No third-party paid credits used.

**Next technical/art decision:** repeated smooth warp of an adult-like base does not produce the reference's dense layered mesoptile down, truly juvenile short folded wing or organic rear silhouette. Do not continue stacking primitives or endlessly pushing tail geometry. Future useful work requires a specifically juvenile sculpt/groom source with proper multi-angle anatomy, baked down material, a credible old eucalyptus tree-cavity support and independent 390×780 hardware WebGL tests. Never promote a software-valid GLB to a release without passing all artistic, licensing and mobile gates.

This entire Run271 branch is isolated: only a #172 research script, dedicated research Actions workflow, and this audit; **main, all 251-species concept-production workflows, original references, the cat WebGL prototype and deployment are unchanged**. Strict **NO_RELEASE**.
