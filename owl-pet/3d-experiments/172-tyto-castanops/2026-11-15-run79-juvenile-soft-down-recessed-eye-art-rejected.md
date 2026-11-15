# Run79 — #172 *Tyto castanops* v3: free Blender short-down/recessed-eye/wingfold trial (**ART_REJECTED**)

**Date:** 2026-11-15 (Asia/Shanghai). **Research only — not a publishable or deployable 3D pet. Zero additional spend.**

## Preflight and owner reference

Read GitHub main owl-pet/AGENTS.md, README.md, current prototype and #172 material, and Run74–Run78 independent rejection audits. Recovered the exact Run78 successful GitHub Actions binary proof artifact (run 43694434557) and separately recovered/inspected the prior Drive 43-file verified rejected ZIP. Directly inspected the rightmost owner's source crop `owner_172_right_mesoptile_crop.jpg` against the real four-view Run78 Blender Cycles render. It depicts a cream-colored young barn-owl-like *Tyto castanops* concept with soft down and compact head, natural heart facial ruff and anatomically supported toes inside a tree hollow, but supplies **one front-facing image, not independently verified side/back anatomy or precise nestling age**.

## Actually executed zero-payment experiment

Created separate research branch [research/owl172-run79-juvenile-soft-groom](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run79-juvenile-soft-groom), based on GitHub main, adding only two files:
- [Run79 complete reproducible Blender source](https://github.com/janeytlin-eng/game-owl-ket/blob/0b6c6eaa2e4704bc4c6a975bb6c5d44e08ec2865/owl-pet/3d-experiments/172-tyto-castanops/tools/run79_blender_juvenile_softdown.py).
- [Isolated free Blender 4.0.2 GitHub Actions runner workflow](https://github.com/janeytlin-eng/game-owl-ket/blob/0b6c6eaa2e4704bc4c6a975bb6c5d44e08ec2865/.github/workflows/owl-pet-172-run79-softdown.yml).

[Actual workflow run 43698117928](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43698117928) completed successfully, research artifact ID **14155138804** (14-day CI retention; durable Drive ZIP below).

Compared with Run78, modified real sculpt body flank-wing relief, reduced facial rim thickness and made eye size/position more recessed, redesigned toes, switched irregular bark-support geometry, and shortened/raised distribution of true curved 3D mesh-filament down. This did not add ellipsoid wings or substitute an SVG, static illustration or a fake non-geometric 3D image. It **did not** use an external paid image-to-3D service or buy any credits.

Blender 4.0.2 produced, actually rendered four orthographic Cycles angles, exported a **3,583,256-byte GLB** (`SHA256:75d5c381698408f8843643e45843823b3b81da49b35aed4400eb3a5384324635`) and re-imported the GLB for inspection: **29 separate meshes / 104,852 final GLB triangles**. The earlier Blender source-side polygon count `101,556` is pre-export; **use final reimported count**, not the pre-export polygon count. The real groom is **19,500 short curved guides / 58,500 fur triangles**; the remaining triangles are anatomical body, face, feet and perch.

Independently loaded the exported Run79 GLB in local **Chromium 144 + SwiftShader WebGL2** using a binary glTF loader and simple shader, with actual static canvas renders across four views for both a **390×600 mobile-sized viewport** and an **800×800 desktop viewport**. All **8/8 actual software-browser draws** completed with `glError=0` and no JS exceptions. The first headless attempt reported WebGL2 unavailable; recovered by using a real Xvfb display with nonheadless Chromium. This is **viewport emulation on software rasterizer**, not a physical mobile GPU, not glTF reference-standard PBR, nor a measured frame rate or rigged-animation test.

## Art acceptance: **REJECTED**

Inspected all Run79 Blender four-view images and the eight WebGL static renders against the actual owner crop and Run78 contact. The results are somewhat softer than Run78 and eyes are less concentric, but they still fail the user's quality gates:

1. Face still resembles a flat ornamental heart shield. Natural orbital sculpt and cream-brown feather transition are absent; bill and eyes remain too simplified.
2. New short down reduces the Run78 needle/bristle look in Blender; WebGL instead shows tiny dot/sparkle-like surfaces. It is not coherent, soft layered down of the original concept.
3. Body remains a fused two-lobe pear/bag; side/back show no anatomically credible short wingfold or tail, and shoulder anatomy is not recognizable.
4. Toe bones still spring from two artificial spherical ankle mounds. Reworked bark perch has open tube ends, reads like hollow pipe rather than an old tree hollow.
5. No validated matching true side/back reference and no physical mobile WebGL GPU/performance/animation acceptance.

**No public sample, no deployment, do not represent GitHub Actions success as successful 3D character design.** The artifact's GLB is only retained as rejected negative research evidence.

## Independently archived, remote-read-verified evidence

[Run79 27-file full rejected evidence ZIP on Google Drive](https://drive.google.com/file/d/152g3MIID15AW5ZP-s0xEgiFQ1PGKYBkZ/view).

- ZIP exactly **9,466,495 bytes**, SHA256 **`ff005b8bd88cbedc9e9090e373b141d5c255a34effcb63bfcf0c90550daaf3a6`**.
- Contains real Run79 GLB, full CI log and re-import metrics, 4 Blender rendered views, 8 browser screenshots, browser QA source/logs, original owner crop, Run78 benchmark render, comparison contact sheets, signed off quality rejection, 26-file content SHA256 manifest and reproduction links to immutable source/workflow commits.
- Uploaded to separate Google Drive `Owl172_3D_research_ART_REJECTED` folder, re-fetched uploaded file from Drive, **9,466,495 bytes / same SHA256**, ZIP CRC test passed and **26/26 individual SHA256** rechecked. Remote result confirmed.

## Actual zero-cost tool research and remaining blocked capabilities

Further identified free [Daniel Bystedt Blender Hair cards from curves](https://www.cgchannel.com/2024/03/daniel-bystedts-free-blender-add-on-creates-hair-cards-from-curves/) (requires Blender 3.6+; not run), [GBH Tool open GitHub GPL-2.0-or-later test version](https://github.com/GixoXYZ/BlenderGBHTool) (newest line requires Blender 4.2; not run) and [GeoFeathers 1.2 pay-what-you-want](https://miauarts.gumroad.com/l/zrvcj) (`$0+`, license and export-to-GLB not yet cleared; not installed). No third-party weights or assets downloaded this run. The concrete next bottleneck is organic manual-quality young-owl sculpture and feasible hair-to-glTF PBR material pipeline; continuing trivial base-mesh deformations is unlikely to meet release criteria. Real mobile device tests remain pending.

No changes were made to the original concept image, 251-species production workflow, main prototype, vocabulary game, manifests, online deployment or paid services. Branch `main...research/owl172-run79-juvenile-soft-groom` was independently checked and contains exactly the two isolated files listed above. This markdown audit is the only additional main-branch change.
