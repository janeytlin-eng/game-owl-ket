# Run406 — native posture diagnostic — NO_RELEASE

2026-11-27. Read main AGENTS, README, STATUS, recursive tree and Run405 (b021f75b111eba82907fc94408de2bd1582f5717). The requested v3 original remains blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b. Recovered and actually viewed the full 512×1024 v3 mesoptile crop, blob 2915b7c86316359ff2b8cbd26eb174bfa0280613: cream wispy down, brown-edged heart disc, small dark eyes, pale bill, substantial feathered feet, compact silhouette, no obvious long tail. Left edge crops part of body; no true side/back reference or known age. Do not silently substitute later v6.

## Actual experiment

Recovered complete 779,732-byte native GLB via connector from historical Run100, commit 7757abbe42f206ed05ac74766f91ef6de8fcb315, path `owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run100-REAL-NEURAL-TOPOLOGY-ART_UNAPPROVED/run100_voxel_55k_ART_UNAPPROVED.glb`, blob ab38e9ac13d06fc03608a15460c08c2296a0966c. Already rejected neural-derived voxel mesh, not an independent new sculpt. 21,622 vertices and 43,240 indexed triangles (actual index count 129,720, not filename's nominal 55k). Y-up, front +Z. One cream rough nonmetal material; no eyes/texture/rig in this diagnostic source.

Tested an explicit lateral posture deformation on the actual vertices, preserving x/y and triangle connectivity:
`z2 = z - .32 * max(0,y) + .48 * max(0,-z) * clamp((.65-y)/1.4,0,1)`.
Recomputed vertex normals as normalized sums of incident face cross products. Updated POSITION accessor bounds and GLB JSON/BIN length fields. Output 779,740 bytes, header length and JSON parse checked. No assertion of external renderer import or mobile QA. Native output blob e3e50315d3b7d4669e6dc89d700ffa1bbf8f33fb.

Actual indexed-triangle software rasterization with orthographic views at 0/90/180 degrees around Y, common 70 px/unit, depth buffer and interpolated vertex-normal diffuse lighting. 480×320 comparison PNG, top baseline, bottom deformation, columns front/side/back. Actual visual inspection: baseline has a long sloped body and rear projection; test shortens rear volume but produces abrupt sloping rump and disproportionately protruding beak. Front retains clay-like featureless eye sockets, stiff facial disc, segmented side wings, rough body/feet. Rear remains lumpy and adult-feather-like. No fluffy down, no lifelike eyes, no adequate juvenile identity. NOT an art pass. No product release.

- Original Z extent: -0.9818594 to 0.9586429; deformed -0.6118954 to 0.9237584 (about 21% shorter depth). X/Y extents unchanged.
- Original front/side/back covered pixels: 10675/11279/10675; deformed 10675/9547/10675. Side area decreased, not evidence of scientific accuracy or better identity.
- Actual six-view PNG blob 5312717e40b08c8a836b40d0f4ef4d05efcb3f31. Binary assets committed together at d8cd9d949cbfefa04444788338213c4c19ee7775.
- [Comparison](before-after-front-side-back.png), [diagnostic GLB](native-posture-diagnostic-NO_RELEASE.glb). These are internal rejected test assets only.

## Alternatives and blockers

Fresh GitHub searches: owlet filename:owl.obj 0; barnowl extension:stl 0; barn_owl extension:obj 0; owlet extension:dae 0; owl filename:owl.ply 8 (Plymouth and bowl false positives); owl chick extension:obj 140 (top results MUD text). Search counts are not proof of absence. Reviewed newer source listings: https://mint.gg/free-3d-models/barn-owl (CC0, 19,966 triangles, adult plumage, known Run402 lead); https://grab3d.com/models/animals/owl/ (CC0, great horned owl adult, exclude); https://gaitkit.com/asset/eaglet (5,384 triangles, animated low-poly eagle chick, wrong species/form; license not established here). No external binary obtained or claimed. Local DNS failure errno -3 for github.com, api.github.com, huggingface.co; local torch, trimesh, vtk, skimage present, Blender/bpy, transformers, diffusers absent. No paid submission or additional expense.

Decision: ART_REJECTED / NO_RELEASE. The recoverable small historical neural mesh lets us diagnose posture without extra spending, but silhouette compression is insufficient. Prioritize an independent juvenile-grade base, not more edits to this rejected source. No changes to main, v3 original, 251-species workflow, or deployment.