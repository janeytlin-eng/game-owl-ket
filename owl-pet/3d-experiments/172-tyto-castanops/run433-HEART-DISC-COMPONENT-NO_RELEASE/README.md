# Run433 — continuous heart-disc surface component — ART_REJECTED / NO_RELEASE

2026-11-28. Read main owl-pet AGENTS (b9ebde6dc406354b77d4297089a6f8f928f3b878), README and STATUS (207/251 in latest entries), research/species/172-tyto-castanops-v3.md (5c754f9daf8433ba608107e389659b0271b1480a), original concept v3 (5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b, image displayed), prior Run432 (5f28029a260b1c52eb0fda3209b024846b764495). Target remains rightmost age-unknown mesoptile: warm-rimmed heart disc, dark eyes, pale bill, compact down-covered body, concealed tail and short wing, supported feet. No new scientific age assertion.

## Actual no-cost experiment

Rather than another adult mesh rescaling or unlicensed asset, tested a single continuous, manually traced heart-disc surface component with curved depth, depressed orbital regions, raised medial bridge and rim and radial microrelief. This is an original procedural *component* only, not a full character or a neural reconstruction, and intentionally not offered as a sample. The boundary was hand approximated visually from the original, not extracted by a segmentation model. Actual color PLY and three-view depth-buffered rendering created and archived; exact executable JS in experiment.js. Geometry: 5761 vertices, 11400 triangles, 0 degenerate, finite coordinates, 120 open boundary edges (intentional patch), 0 edges with incidence >2. Depth extent 0.3060 arbitrary units; 0/45/90 degree foreground coverage 22814/16271/3068 pixels. PLY 417751 ASCII bytes; PNG 435918 bytes. The three panels are actual views of the same mesh; not independent illustrations. Vertex shading only, no physical feather BSDF or strands.

## Visual gate

Viewed original and output at all three angles, and viewed the remote PNG readback. Heart outline and warm rim are recognizable but overly uniform and shell-like. Radial polar-grid convergence produces a conspicuous center artifact and artificial broad spokes, rather than natural separately directed down around the eyes and bill. Eye regions lack actual globes, eyelids and realistic anatomy, no beak, no body/head integration, no rear/head or wing structure. Side view exposes the thin open patch. No mobile WebGL qualification. Reject as character; do not promote to full pet or simply attach this disc to an ellipsoid. For next attempt, avoid a global polar grooming origin, investigate two orbital feather flow fields, preserve actual ocular and beak anatomy on a continuous complete mesh, and evaluate on a rights-clear juvenile base. A smooth ring alone is insufficient.

## Runtime and provenance

Actual local checks: github.com, raw.githubusercontent.com, media.githubusercontent.com and huggingface.co DNS resolution each failed with temporary error -3. trimesh, VTK, torch, skimage, cv2, playwright present; bpy and pymeshlab absent, Blender executable not found; home cache only fontconfig. The actual component experiment instead ran via CPU JS, no network-dependent inference. No paid service used. No externally sourced mesh redistributed.

Artifacts committed at 3e763bee2ff400b7f9edf58f781c3f390155d285; immutable readback SHA for PLY 5b5abcaf7e04506fa5b907255999eea415126fa6, PNG 940914994ee3c0f746bc2854d1fe431e0e7c81b2, JS 304cc9bdecf631ec47c75806ef0ea2a61e297913, metrics 7c10a31e1c6c61a36a718375e3678d479c52c174. PNG displayed from remote readback; PLY text readback length 417751. No claim of full byte hash computed independently.

Decision: ART_REJECTED / NO_RELEASE. No qualified sample. Zero extra spend. Only independent experiment branch changed; no main, original concept, 251-species workflow or deployed game changes.
