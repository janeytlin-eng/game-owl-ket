# Run85 — rounded supported mesoptile with integrated folded-wing relief (**ART_REJECTED**)

**Date:** 2026-11-15 Asia/Shanghai. **Not approved, not a usable high-quality 3D pet, not published or deployed.** No external paid tools.

## Pre-flight: actual project and previous work examined

Re-read `owl-pet/AGENTS.md`, `README.md`, the exact `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, `knowledge/ANATOMY_AND_POSTURE.md`, Run81–82 rejection audit, Run83 and Run84 research branch assets, and checked the existing `prototype/index.html` boundary. The prototype is a separate old cat WebGL interaction, **not** an acceptable owl character. The owner's #172 v3 concept is one frontal crop from a scientific-limited design plate: age-unknown cream mesoptile, developed heart disc, short fully down-buried wing, no visible tail, and natural belly/two-foot support on a broad eucalypt hollow lip. Never infer exact castanops age or verified lateral/back anatomy from the front plate.

Read [Run84 source and its raw evidence](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run84-smooth-vertex-ruff/owl-pet/3d-experiments/172-tyto-castanops/uncertified-binary-run84) as immediate baseline; downloaded its actual artifact and inspected the four Blender Cycles views. Run84 had a hanging pointed teardrop/bag body, very slight folded wing relief, discontinuous facial impression and brittle speckled down. Do not claim it was approved.

## Actually modeled and corrected via no-extra-payment Blender

Used the successful free GitHub Actions Ubuntu 24.04 Blender 4.0.2 workflow route to run a new independent `run85_blender_gradient_disc.py` sculpt, forked from a Run84 baseline but **newly reconstructed in the actual 3D continuous loft**:
- Replaced the pointed egg profile with a rounded broad lower body and separate smoothly interpolated cranial transverse radii. Tried to reduce unsupported dangling belly while preserving a compact juvenile. This intentionally changes real front, profile and back mesh surface, not an SVG or front image.
- Added a lateral, short wing-like deformation *in the body surface* that is buried under down rather than importing an adult layered flight feather; softened the heart-disc colour transition and reduced toy eyes, beak thickness, and fibre lengths/contrast.
- Kept a game-exportable 3D GLB with **10,000 actual curved microdown guides** and exported 4 original 640px Cycles views. No claim of premium groom realism.
- One workflow attempt [43715003013](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43715003013) correctly failed CI: original copied script showed valid completed export/import but a stale Run84 filename in its four-view check stopped durable archival. Corrected the file checks to `sculpt85_`, added independent binary SHA256 and import-metrics assertions, reran the actual free workflow [43715285987](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43715285987) with **all jobs success**.

## Independently verified durable research evidence

Actual GLB **2,102,976 bytes**, **SHA256 `53c89f426f212934f279ab3cc199e88af757bec998565cb566aea60e43507f27`**, format magic `glTF`; 26 Blender re-import mesh objects. Model-side Blender polygon count 57,856 is *not* final export triangle count; independent trimesh GLB parse counted **61,504 final triangles**, including 30,000 in 10,000 feather guides. Original Cycles images: front, three-quarter, strict side, back. Successfully downloaded the final Actions evidence ZIP, passed its CRC check, independently matched the GLB SHA to the remote `metrics.json`.

**Durable rejected binary and four native renders** (with exact log, checksum and metrics):
[Run85 research branch archive](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run85-supported-rounded-mesoptile/owl-pet/3d-experiments/172-tyto-castanops/uncertified-binary-run85).
[Independent browser and visual QA audit](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run85-supported-rounded-mesoptile/owl-pet/3d-experiments/172-tyto-castanops/uncertified-binary-run85/WEBGL2_SOFTWARE_QA_ART_REJECTED.md).
Branch archive commit initially `ffac03fa9f32ba0fa9698024343c835ffef346ed` (the follow-up browser QA text is an independent later research-only commit).

Independently loaded the same original GLB into actual Chromium SwiftShader software WebGL2, drawing from parsed original triangles/normals on **8 actual frames**: four views × 800×800 desktop and simulated 390×600 phone portrait. Observed `gl.getError()=0` for all eight, no JavaScript exceptions. This was a **custom lightweight shader** not a standard glTF 2.0 PBR viewer. No physical phone GPU/thermal/touch, real FPS, animation, standard PBR material parity or artistic acceptance was established. Never equate browser screenshot/viewpoint with a working pet.

## Four-view art rejection after actual PNG inspection

The formerly pointed drooping belly was reduced and now visually contacts the ledge, but the body has become a **snowman-like pair of stacked globes with a narrowed neck**; not a believable juvenile owl cranium/neck/trunk continuum. The Tyto heart area reads as a soft padded cartoon mask with circular black toy eyes, rather than dense facial feathers. The side silhouette has no convincing folded short wing; the back is essentially featureless and symmetrical; the cream down reads as brittle sparkly grain rather than dense second-down. Front/side show elongated exposed toes and artificial support; the flat rectangular eucalypt ledge is also not anatomically/contextually credible. These are decisive art failures, not small texture bugs.

**Verdict: ART_REJECTED, no quality-approved GLB or sample URL.** Do not showcase as a pet, assign acceptance, or deploy. Need credible overall juvenile organic sculpt, feather field, short-wing geometry, facial ruff and grounded perch before full phone/PBR/animation validation. More procedural globe tweaking is not likely to meet the quality bar.

## Retention and noninterference

The successful free workflow pushed only 9 binary/log/QA source files into a dedicated research branch `research/owl172-run85-supported-rounded-mesoptile`, plus this later independent QA note; main branch only receives this textual negative audit. `main...research/owl172-run85-supported-rounded-mesoptile` compare showed only the specific experiment workflow, new Blender script and dedicated rejected binary archive changed. **No** 251-species production workflow, root word-game, original concept/manifest, existing owl-pet prototype or online Sites deployment touched; **zero** external paid inference/purchases.

For additional browser screenshot retention, a **21-file local-only ZIP** `owl172-run85-independent-art-rejected-evidence.zip` of 4,379,997 bytes, SHA256 `47804e40eb39fa4b4f90d438784c49898b8a7ae58acc5434a61428f7131ac956`, passed ZIP CRC and SHA manifest. Google Drive connector file-ref upload failed validation; explicit Files Library folder creation and upload both returned `AccessDeny`. **Do not claim this supplementary ZIP is remotely archived.** The actual GLB, four Blender renders, metrics, checksum, logs and QA note **are durably archived in GitHub research branch** as linked above.
