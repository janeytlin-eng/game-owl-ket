# #172 *Tyto castanops* v3 — Run246 Y-up coordinate correction, honest native-3D shelf A/B (NO RELEASE)

**2026-11-20 Shanghai · research-only · NOT ART APPROVED · PHONE GPU NOT TESTED · NO RELEASE.**

## Read-back before change

- Re-read `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, `research/species/172-tyto-castanops-v3.md`, Run245b's final audit and actual Run245/245b Python, machine reports and the actual Three.js browser viewer. Baseline browser supports real native GLBs and seven true views, but visually rejects the brown upright ring and adult-like long wing.
- Target remains the **far-right** concept bird: evidence-bounded age-unknown cream second-down juvenile, developed heart-shaped face, open dark eyes, genuinely short down-buried wing, no exposed tail, broad naturally weathered horizontal Tasmanian eucalypt hollow-lip with both feet supported. This is a concept/art prototype and does **not** represent verified age-specific juvenile morphology.

## Newly established cause, not another round of trivial body squeezing

The prior Run245b branch's viewer sets `camera.up=(0,1,0)`, `front=[0,0,1]`, `top=[0,1,0]`. Thus **Y is vertical** and Z is front/back. Yet Run245/245b's implicit hollow uses `zz` for the vertical `crown`, `floor` and truncation; the "low core vertices" proximity QA also selects `core.vertices[:,2]<-.40`. This is a **material coordinate-frame bug**, not merely a subjective silhouette preference. Its output appearing like a tall ring and obscuring the rear is consistent with this geometry-orientation error. Importantly, the previous reports' "458 low core vertices near bark" were measured in the wrong axis, so cannot establish foot support.

## Concrete new attempt

- Created isolated research branch `research/owl172-run246-correct-y-up-eucalypt-horizontal-shelf-neural-3d-no-release` from the latest Run245 branch, without touching main or the 251-species production line.
- Added `run246_yup_horizontal_organic_eucalypt_ledge_ab.py`: loads exactly the SHA256-pinned **actual learned Hunyuan 3D owl** `19274685ed19bb4c61b36a55b09048649a3db5c691aff2d75b1fe33831abf1ee` with eight original meshes and 86,867 triangles. Does not procedurally replace the owl. Derives the ground height and dimensions from *actual core Y coordinates* rather than hardcoded Z. Sculptures two independent watertight volumetric horizontal broken-bark ledge variations using 3D irregular noisy SDF, Gaussian smoothing and Marching Cubes; worn pale sapwood and weathered rough nonmetallic bark are vertex-colored. The high rear wall and upright ring are deliberately removed. Adds normals, then reloads each GLB and checks mesh preservation and proximity using **low Y** core vertices.
- Added dedicated free GitHub Actions push workflow `owl172-run246-yup-horizontal-eucalypt-ledges-native-webgl.yml`: retrieves SHA-pinned prior true-3D owl only from existing research artifact, actually executes geometry and native GLB export, and uses actual Chromium/Three.js WebGL2 for seven distinct cameras on **both** A/B models (14 images). Exports GLBs, per-image reports, combined QA contact; binary remains only in time-limited Actions evidence, while research reports/contact are committed solely to this branch.
- Job URL: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44743011827 . It was verified actually **in_progress** after the workflow commit at the time of this note; no mesh/render/art pass is claimed until its outputs are inspected. Extra external paid spend: $0.

## Release gate and open risks

The genuinely hard problem remains the **bird** (juvenile short wing, fluffy secondary down, natural face, consistent side/back), not just the support ledge. The support sculpt is an environmental experiment only; technical A/B outcomes cannot be described as a beautiful pet character. Device-specific Android/iPhone GPU FPS/VRAM/touch testing is absent. The shader/software driver alone cannot certify mobile production suitability.

**FINAL STATUS AT THIS POINT: PENDING_REMOTE_GLBS / PENDING_BROWSER_14VIEW / ART_UNAPPROVED / PHONE_UNTESTED / NO_RELEASE**.

Do not merge, publish, announce a sample, overwrite the existing kitten prototype or modify the 251-species production pipeline.
