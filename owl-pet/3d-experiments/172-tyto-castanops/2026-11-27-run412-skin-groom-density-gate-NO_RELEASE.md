# Run412 — native skin/groom attachment feasibility and source gate — NO_RELEASE

2026-11-27. Read main owl-pet AGENTS, README and STATUS (207/251), recursive tree, exact #172 v3 review and actual 512x1024 mesoptile crop, blob 2915b7c86316359ff2b8cbd26eb174bfa0280613. Original concept blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b unchanged. PASS_WITH_LIMITATIONS, science=false, age unknown. Target: soft continuous warm cream down, brown-edged heart disc, dark eyes, pale narrow beak, very short wings/tail concealed, supported feathered feet. Re-read previous Run411 commit 2accb33665ca66671adb8c647f9448ec995fca11 and actually viewed Run406 front/side/back before-after render; it remains rejected (featureless sockets, lumpy clay surface, exposed wing division, adult-like silhouette).

## Independent technical source examined

Read actual MIT source, not a generated asset:
- https://github.com/canopico-world/PhenoVoxel-Archive/blob/main/owl-feathers.js (blob bd0d29af60b3e27bcafe92e1b6d44741e942f393): area-weighted random triangle sampling, barycentric interpolation of atlas UV and inherited bone weights, top four weights normalized, four triangles per fine contour vane, unindexed vertex data, masked facial/leg regions.
- https://github.com/canopico-world/PhenoVoxel-Archive/blob/main/owl-rig.js (blob e6d3745d4e580d7a0ec74d76ddc480443413615a): 16-bone perched owl articulation, region-based weights and qualitative head/wing/foot movement. Source-specific coordinate thresholds are not transferable directly to castanops.
- License ledger https://github.com/canopico-world/PhenoVoxel-Archive/blob/main/ASSET-LICENSES.md credits Innovation Studio's Common Barn Owl scan https://sketchfab.com/3d-models/common-barn-owl-19c989a6681145bc999c332699eb852e as CC BY 4.0. This is an adult scan-derived exterior; authored rig and vane dimensions unvalidated. Repository recursive tree had no owl native model filename and GitHub releases returned empty; no independent mesh acquired. Do not confuse MIT implementation with scan license, or contour vanes with fine juvenile down.

## Actual native area-sampling diagnostic

Recovered complete 779740-byte Run406 GLB from immutable commit 16045db5e461b2b524b238c44aba742734c36b74, blob e3e50315d3b7d4669e6dc89d700ffa1bbf8f33fb using fetch_file base64. Decoded real positions and indices, 21622 vertices / 43240 indexed triangles, Y up/+Z front. POSITION and NORMAL only, no UV, JOINTS_0, WEIGHTS_0 or skeleton. Adapted the area-sampling idea solely as an in-memory feasibility diagnostic (not copied artwork). Each triangle area is half cross-product magnitude; cumulative area lookup for 14000 points using LCG seed 2019, recurrence (1664525*s+1013904223) mod 2^32, u=s/2^32. Sample barycentric weights 1-sqrt(r), sqrt(r)*(1-t), sqrt(r)*t. For each sample, mutually exclusive rough diagnostic masks: y<-.65 lower; else y>.23 and z>.30 upper front; else y>.23 upper crown/back; else body. These are model-coordinate masks only, not anatomical segmentation or measured down density.

| Region | Triangle area by centroid (model units squared) | Sampled points |
|---|---:|---:|
| Lower | 2.426530 | 3626 |
| Upper front | 0.871871 | 1305 |
| Upper crown/back | 1.698487 | 2538 |
| Body | 4.237948 | 6531 |
| Total | 9.234837 | 14000 |

Excluding lower and upper-front regions leaves 9069 actual candidate roots. At four triangles per vane, the hypothetical unindexed groom would add 36276 triangles and 108828 vertices; at 56 bytes/vertex (position 12 + normal 12 + UV 8 + four uint16 joints 8 + four float weights 16), approximately 6094368 bytes of attribute data before packaging, texture and runtime overhead. Combined hypothetical triangles 79516. These are calculated geometry budget estimates, not a produced groom, measured draw calls, frame rate or mobile benchmark. No UV/skin on rejected base means inherited color and deformation cannot actually be verified. Root sampling alone cannot repair its heart disc or body. Do not build a visually inferior vanity release from this result. Consider indexed/shared vertices, texture atlas and clustered cards only after a suitable juvenile sculpt exists; target fine soft fibers, not obvious adult vanes.

## New no-cost asset access attempts

- https://www.innerscene.com/tools/library/3d-parts/owl-d696472a lists a 19.7 MB CC0 owl GLB (added 2026-10-21). Actual viewer page opened https://www.innerscene.com/v/4jofHjnJFJFDgF4hD1zajx ; actual download request https://www.innerscene.com/api/library/owl-d696472a/download failed unsupported application/octet-stream. No visual or juvenile suitability claim, no bytes obtained.
- GitHub precise filenames barnowl.glb=0, barn_owl.glb=2 (one Git LFS pointer in series-ai/jam-ready-assets, one Godot import file), owlet.stl=0, owl_chick.obj=0, owlet.glb=0, owlet.obj=0. Other babyowl/baby_owl/owl_chick filename queries returned no matching model formats on returned pages. BarnOwl.obj in alvarocasadoc/3December actually fetched, 204533 chars, 879 positions/886 polygon faces, matches prior Run402 scale/count and source (do not count twice); no root LICENSE.
- Historical OHS side-view chick photograph https://digitalcollections.ohs.org/barn-owl-chick metadata dated 1904, original page open returned 403, no pixels retrieved. Not a 3D asset. Previously known Mint adult CC0 GLB and CGTrader baby sculpt are not new.
- Local probe github.com, raw.githubusercontent.com, huggingface.co, pypi.org all DNS errno -3. torch/trimesh/cv2/scipy/skimage/vtk available; no CUDA, Blender/bpy, pymeshlab, open3d, onnxruntime or transformers. No paid generation, no additional expense.

Decision ART_REJECTED / NO_RELEASE. No new GLB exported, no qualifying juvenile model, no mobile WebGL acceptance claimed. No modifications to main, original concept, 251-species workflow or deployment. Independent juvenile-grade native base remains the gate; retained new groom-source and actual budget evidence for future use.
