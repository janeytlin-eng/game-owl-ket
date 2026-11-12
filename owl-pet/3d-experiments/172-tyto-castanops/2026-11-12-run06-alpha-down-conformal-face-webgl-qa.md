# #172 棉棉 3D Run06 — alpha-down, skull-conformal facial disc & offline WebGL2 smoke (2026-11-12)

## Source gate (read before modeling)

- Re-read `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, Run03–Run05 prior experiments, and visually examined original full-resolution concept PNG via GitHub read.
- Sole design target: **the rightmost cream "AGE-UNKNOWN MESOPTILE"**, concept `owl-pet/design/concepts/172-tyto-castanops-v3.png`, Git blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`. Young's exact age/feather chronology and flight capability are unknown. The adults and any presumed nest interior are not used as juvenile references.
- Do not change the 251-species production manifest, concept images, numbering, existing prototype or workflows. All generation is an isolated failed experiment.

## Tooling and executed trials

- Used local **NumPy/SciPy/skimage marching cubes + trimesh GLB export/re-import + PIL generated RGBA feather atlas**; no Blender, unavailable pretrained image-to-3D weights, external GPU, fal credits or payment.
- Instead of Run05's >300k-triangle solid microfilament geometry, used real 3D **double-sided alpha feather cards** and an embedded 192×256 RGBA atlas exported as glTF `baseColorTexture` with `alphaMode=BLEND` and `metallicFactor=0`, `roughnessFactor=1`.
- **v17**: new SDF chick base, cream color variation, small down-buried wing masses, horn bill, black eyes, supported toes and talons; 3,093 alpha cards. Four real **software CPU raster** perspectives (front / 3⁄4 / strict side / back). The earlier VTK rendering attempt was unusable: even under Xvfb it yielded blank PNGs, so those blank images were *not* used as QA evidence.
- **v18**: revised head/body/neck blend into a squat chick rather than one elongated oval; denser soft atlas cards (9,279), shorter feather lengths, smoothed discontinuous face relief, reworked foot tubes. Four CPU raster views. 
- **v19**: **new curvature-following 3D heart disc mesh**, using cKDTree projection to the sculpted skull's front surface at each mask vertex (not a flat front billboard), graded chestnut-buff edge and pale center; 10,052 alpha down cards. Four CPU raster views. The disc is still a separate shell and is not a passable anatomical model.
- Built a standalone **dependency-free WebGL2 GLB-viewer HTML** capable of parsing glTF 2.0 accessors, indexed triangles, vertex colors, normals and embedded PNG alpha, with touch drag/yaw/pitch and viewport adaptation. The Chromium local HTTP test returned `net::ERR_BLOCKED_BY_ADMINISTRATOR`; an inline data-GLB fallback launched Chromium but returned **no WebGL2 context**. Therefore **no successful WebGL or mobile/device runtime is claimed**.
- CPU rasterizer is only for *static geometry QA* and is not evidence of browser shader fidelity, translucency order correctness or mobile GPU suitability.

| version | GLB bytes | actual meshes re-imported | triangles | alpha cards | SHA256 |
| --- | ---: | ---: | ---: | ---: | --- |
| v17 | 1,153,328 | 47 | 46,230 | 3,093 | `dad5d9519e8e9da9ee96c9240f1b2f65810a9cc188a362f35b3a8087a269b295` |
| v18 | 2,030,980 | 39 | 67,190 | 9,279 | `b5f58e8946c90c63c75c09eea8a6b1e481789eba6f1788f14f43f9897f618fc0` |
| v19 | 2,267,124 | 28 | 76,416 | 10,052 | `741d78e314240425ae352752dc63fd71f494f7bdbc0023eb512eb63cb4647e64` |

The GLBs were **exported, reloaded, and parsed** to confirm all positions, triangles and embedded RGBA atlas exist. The model is real 3D geometry, not SVG or a two-plane sprite. There is no rig, deformation, touch interaction with the bird, or actual mobile runtime pass.

## Visual review (based on opening the rendered 4-view contact sheets)

- v17: complete visual failure: tall potato silhouette with a very tiny, jagged, theatrical mask and robotic feet. Sparse fiber atlas has little perceptible fluff.
- v18: better head/neck/breast separation and visibly denser surface down; it still looks like a smooth fuzzy *snowman* with two eyes, not a premium owl chick. Facial heart is barely discernible, crown silhouette too geometric, feet too mechanical.
- v19: heart-shaped mask is finally clearly legible on a *curved three-dimensional head* in front, 3⁄4 and side views, but its dark grey/buff flat face reads as an **attached armored shield**, not continuous soft owl down. Side/back remain blunt, over-symmetrical generic masses; short wing barely registers. Alpha filaments are short glitter/surface scratches rather than plush second down. Toes don't look grounded on an actual lip, and the side/back face-disc transition is abrupt.
- Thus **FAIL / NOT USER-SHOWABLE**. No user-facing interactive sample exists. Do not promote any version to approved production or trigger user notification.

## Evidence and archive integrity

- Actual local experiment: `/mnt/data/mianmian_run06.py` generator, `/mnt/data/cpu_render_mianmian_run06.py` CPU raster renderer, `/mnt/data/mianmian_run06/viewer.html` GLB/WebGL2 offline test viewer, alpha PNG textures, 12 nonempty four-view CPU raster PNGs + 3 contact sheets, metrics JSON, v17/v18/v19 GLBs, browser smoke scripts/logs.
- Local zip: `/mnt/data/mianmian_172_run06_rejected_bundle.zip` — **4,792,756 bytes**, SHA256 `80746689282b1367ab3089aeb40a3373b3672cb1c373159d094b38b7dd69f011`, 35 entries. This is an ephemeral run-local artifact unless independently copied; do not call it a deployed asset.
- Explicit attempted upload to existing persistent Library folder `/猫头鹰电子宠物/mianmian_172_run06_rejected_bundle.zip` failed with `AccessDeny: FileDrive_7a934266b8748191824cde4d0af03f29`, matching older runs. Therefore **only this QA markdown is archived in GitHub**; binary GLBs/source/renders are not durably on GitHub or in Library. Do not cite this log as proof of a deployed model.
- No 251-species concept, research, manifest or workflow files edited.

## Next decision, based on repeated failure

Stop increasing procedural card density and stop treating smooth metaball silhouette as a high-quality bird. An actually image-conditioned multiview **skull/neck/wing sculpt and fur appearance** (Blender groom/hair with 3D artist direction, or legally available open model weights, or reviewed external image-to-3D when credits are available) is now needed. Preserve the new efficient alpha-atlas and GLB viewer as optional technical subcomponents; they do **not** repair the art. Only consider showing user when the front is actually reminiscent of the reference and all three other angles hold up, feet are grounded, and a real accessible WebGL runtime has been proven.
