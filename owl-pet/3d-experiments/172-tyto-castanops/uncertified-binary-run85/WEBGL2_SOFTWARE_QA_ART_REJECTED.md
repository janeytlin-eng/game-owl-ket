# Run85 browser/visual QA — explicitly ART_REJECTED

Date: 2026-11-15 Asia/Shanghai. The GLB is an **experimental rejected artifact, not a released or qualified 3D owl-pet.**

## Provenance
- Free Blender 4.0.2 on Ubuntu GitHub Actions: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43715285987
- Actual repository archive in this directory contains 2,102,976-byte GLB (`53c89f426f212934f279ab3cc199e88af757bec998565cb566aea60e43507f27`) and four 640x640 Blender Cycles views. Round-trip Blender import: 26 mesh objects; independent trimesh GLB count **61,504 final triangles**. The source-side polygon total 57,856 is *not* the exported triangle total. 10,000 feather guides account for 30,000 triangles. GLB SHA and reimport values also verified by the corrected CI workflow after an initial failure involving stale Run84 filename references.
- Independently unpacked the successful Actions artifact ZIP, passed ZIP CRC, verified SHA256 against Run85 metrics. This does not itself prove art quality.

## Actually executed browser rendering
- Parsed the actual original GLB using trimesh; sent its positions/normals/material color approximation into a standalone custom WebGL2 shader.
- Ran Chromium on SwiftShader/Xvfb with actual `drawElements` calls for **4 views x 2 viewport sizes = 8 successful software WebGL2 draws** (800x800 desktop; simulated 390x600 mobile portrait). All frames returned `gl.getError() == 0`; no page JavaScript exceptions. No synthetic screenshot was counted as a render.
- Important: the renderer is a lightweight diagnostic shader, *not a standards-complete glTF PBR loader*. 390x600 emulates viewport size only; **not** physical phone GPU compatibility/thermal/touch/FPS. No animation or skinning validation. Browser screenshots and source were independently included in the 21-file **local-only** evidence archive; repeated Files Library folder/upload attempts returned AccessDeny. Never claim that extra archive is durable remotely. All four original Cycles images and the real GLB are durable on this isolated branch.

## Independent four-view art verdict
**ART_REJECTED** after inspecting actual Cycles PNG front, three-quarter, side and back. Compared to Run84, the pointed bottom is reduced and wide shelf contacts the belly, but the new analytic smooth-max skin now reads as two stacked full globes with an abrupt nape/shoulder constriction, not a biologically credible single mesoptile. The two front eyes are small glossy toy buttons, the heart mask is a cartoon/padded relief rather than soft Tyto facial feathers, side/back have virtually no believable folded, down-buried short wings, cream down is point-like speckled synthetic geometry, and long exposed forward toes do not have natural load bearing. The supporting shelf reads as a squared-off flat block rather than a convincing old eucalypt hollow lip. Material/perspective inconsistencies also persist.

**No approved sample, no model publication, no deployment or paid service.** No modification of 251-species production, original design plate/manifest, existing cat prototype, or Sites deployment. The narrow result is that making the belly rounder alone does not solve the sculptural and grooming defects; future work needs higher-quality juvenile morphology, physically plausible wing volume, fur groom and real phone/PBR tests.
