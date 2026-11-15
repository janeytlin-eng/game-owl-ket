# Run97 — real 3D reference-informed silhouette warp / **ART_REJECTED**

**Date:** 2026-11-16, Asia/Shanghai. **Release decision: ART_REJECTED. Do not publicize or deploy these models.**

## Preflight, existing evidence and reference

Before making changes, re-read the current `owl-pet/AGENTS.md`, `README.md`, existing archived `prototype/index.html` (an unrelated cat viewer), `knowledge/OVERVIEW.md`, species `#172 Tyto castanops v3` context, previous Run92C and Run96/96B negative audits, original `design/concepts/172-tyto-castanops-v3.png`, and actual Run96B four-view Blender Cycles contact sheet. The original rightmost cream downy young owl is squat and plump with a real soft feathered heart-shaped face, tucked lateral wings and naturally planted toes on a wide woody tree hollow. Its source is only a concept illustration, not a proven all-azimuth anatomical scan.

Run96B already proved genuine GLB export/re-import/Blender and software WebGL smoke, but its 220,216-triangle geometry visibly looked like an upright toy egg with a bald smooth head, bead eyes, thin pasted facial rim, loose white cornflake shards, wing-arm bulges and artificial scalloped circular tree pedestal. Previous groom-density, texture projection, existing adult-bird asset transfers and TripoSR CPU work also failed the art gate.

## Actual independent Run97 physical 3D test

Created **two new real 3D nonlinear Blender mesh-vertex sculpture variations** (mild and broad) from the immutable Run96B GLB at source Git commit `fda09fdc455cd04871cc5e98d6974a8898457157` (original GLB SHA256 `9d70385786763ff7bdadd740299de6ddb563b2f0902eb6690b1a822b723d6e2f`). The transformation moves existing world-space 3D vertices with smooth spatial changes to breast/shoulder silhouette and depth. **No SVG, 2D impostor or new stacked ellipsoid/primitive geometry.** Both variants were exported as actual GLB and independently re-imported via Blender, and each was rendered in real Cycles from front, three-quarter, strict side and rear. A third identical-camera four-view baseline was rendered: **12 original Cycles PNGs total**, corresponding metrics, logs and a 3×4 contact sheet.

Execution: free `GitHub Actions`, Blender 4.0.2 CPU. First run [43775539027](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43775539027) failed on the Blender glTF importer missing `numpy`. Added `python3-numpy`; run [43775677350](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43775677350) completed technically but review revealed nearly no visual change, exposing a **coordinate-axis implementation error**: Blender's glTF import converts glTF Y-up to Blender Z-up. The sculpt had incorrectly used Y as height. Corrected to Blender Z-up, reran the experiment as [43775961923](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43775961923); all true 3D export, import, 12 Cycles renders, evidence archive, GitHub artifact upload and GitHub research-branch commit succeeded. This clearly separates a failed attempt, a false-flat technical run, and the actual successfully applied control.

| Data (latest correctly reoriented run) | Unchanged Run96B baseline | Run97 mild warp | Run97 broad warp |
| --- | ---: | ---: | ---: |
| GLB bytes | 4,483,508 | 23,384,304 | 23,407,476 |
| Meshes | 24 | 24 | 24 |
| Triangles | 220,216 | 220,216 | 220,216 |
| Warped vertices | 0 | 120,061 | 120,061 |
| Source / material state | pre-existing art-rejected | unchanged existing materials, 3D vertices moved | unchanged existing materials, 3D vertices moved |
| Blender re-import and 4 fixed-view Cycles renders | completed | completed | completed |
| Actual phone GPU / animation / touch | **not tested** | **not tested** | **not tested** |

Broad variant JSON SHA256 `d78121f0b1791963fa55e610ade2f6cc83b79e7e4f001cf7eebfaa8d274b72e8`; mild variant SHA256 `7c5b66e4d2831c60892cebaaa336fad1696b97b03aa797fe8f88442ad404d7dc`. Native Cycles broad-view recorded 3D bounding dimensions `[2.5302,1.5744,3.3706]`, compared with baseline `[2.071,1.5634,3.3706]`: changed real shoulder width, not a camera or image trick. The GLB grew ~5.2× during the Blender export, which is a new **mobile-delivery regression** despite triangle count being constant. This new GLB has **not** had an actual browser/WebGL2 smoke test or real mobile GPU FPS check, so do not infer phone readiness.

## Direct image inspection: reject all new models

**Actually opened** the original reference concept and previous Run96B contact, the current Run97 baseline and mild front frames, and all four original Cycles broad frames (front, 3/4, strict side, rear).

- Mild deformation is visually almost indistinguishable from the source’s tall, uneven toy egg.
- Broad deformation produces conspicuous **enlarged horizontal shoulder/arm balloons**; the front/rear now look even less like a downy naturally compact nestling. The actual strict side still appears thin and tall with an implausible pasted wing lump.
- Neither corrects the overly clean bald head, hard shallow heart edge, bead eyes, lack of anatomically layered juvenile shoulder/wing coverts, fragment-like down, dangling feet or flat scalloped puck standing in for a real hollow.
- The source concept’s rounded mass, subtle fuzzy face feathers, densely overlapping cream vellus, toe support and natural trunk geometry are not reproduced. An ordinary nonlinear proportional warp does not create anatomy, groom quality, or better material fidelity.

**ART_REJECTED** is final for Run97; passing export/import/render or numeric silhouette change does not count as a usable electronic pet. Avoid iterating more width tweaks over this flawed geometry. Meaningful next trials require licensed source-grade sculpt of a young Tyto, authored facial plumage and realistic juvenile feather tracts (or genuinely reliable multi-view sculpt reconstruction), then retopology and optimized/baked GLB and actual physical phone GPU/animation/gesture testing.

## Archive / safety / billing

GitHub isolated research branch `research/owl172-run97-reference-anchored-sculpt-warp`. Evidence directory `owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run97-SILHOUETTE-ABALATION-ART-REJECTED/` (historical spelling kept to match real committed path): the baseline GLB, mild & broad real GLBs, all 12 PNGs, 3×4 contact PNG, original Blender scripts, logs, per-model JSON metrics, SHA256SUMS and explicit release warning. Code and action at `tools/run97_nonlinear_anatomy_sculpt_warp.py`, `tools/run97_blender_4view.py`, `.github/workflows/owl-pet-172-run97-reference-anchored-sculpt.yml`. All research evidence has been committed by the successful Actions job, and the metrics/views were independently read back.

A GitHub compare of `main...research/owl172-run97-reference-anchored-sculpt-warp` after the previous run confirmed all 31 changed paths restricted to `owl-pet/3d-experiments/172-tyto-castanops/**` or `.github/workflows/owl-pet-172-*`; no changes to the 251-species pipeline, source reference image, original prototype, root game or deployment. No external credits or paid tools were used; a separate image-to-3D creative service required interactive approval and was not called. No release link or user-success notification is warranted.
