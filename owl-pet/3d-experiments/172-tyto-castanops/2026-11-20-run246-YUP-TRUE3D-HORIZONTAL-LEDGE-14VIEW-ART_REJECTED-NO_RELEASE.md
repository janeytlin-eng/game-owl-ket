# #172 *Tyto castanops* v3 — Run246 true 3D coordinate correction, 14-view proof and ART REJECTION

**2026-11-20 Shanghai — TRUE_NATIVE_3D_PASS / SOFTWARE_WEBGL2_PASS / ART_REJECTED / PHONE_UNTESTED / NO_RELEASE.**

## Checked first, and the independently verified problem corrected

Read `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, `research/species/172-tyto-castanops-v3.md`, original far-right three-owl v3 reference (Git blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`), Run245b source, final audit and actual seven-view browser screenshot. Original target = cream, short-winged, puffy age-unknown Tyto chick with real heart face, dark eyes, concealed tail and credible supported feet at a wide old eucalypt hollow-lip.

A serious previous **axis mismatch** was independently found: `run237_browser_viewer_RESEARCH_ONLY.html` defines **Y up** (front = +Z; top = +Y), while Run245/245b's SDF height, crown/floor truncations and "low-vertex" support metric were incorrectly based on **Z**. This explains why its apparently organic hollow rendered as an upright scalloped ring obscuring the rear body. Run246 uses exactly X lateral, **Y vertical** and Z front/back, with actual Hunyuan model bounds instead of wrongly oriented hardcoded elevations.

## Actual experiment and independently checked native outputs

A fully isolated branch was created: `research/owl172-run246-correct-y-up-eucalypt-horizontal-shelf-neural-3d-no-release`. A dedicated free GitHub Actions run **[44743011827](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44743011827)** completed **success**. It SHA-verified and loaded the original REAL Hunyuan learned 3-D bird GLB with SHA256 `19274685ed19bb4c61b36a55b09048649a3db5c691aff2d75b1fe33831abf1ee`, left all its eight bird/eye/down meshes unchanged, and modeled a separate organic horizontal broken eucalyptus ledge using a true 3D SDF/noise field and marching cubes, with explicit normals, vertex-colored worn sapwood, nonmetallic rough bark.

Two differently sized and sculpted ledge A/B variants were really exported and **re-imported**:
- **Run246 A**: native GLB **4,945,972 bytes**, SHA256 `7864afc8a220c7edfa069f4d5bf2498db0fe0810c7e917a0451fc8201f22312b`; 9 native meshes and **131,835 triangles** (support: 44,968 triangles, watertight). Support Y top = **-0.7245**; real core Y bounds **-0.8103 to +0.9873**, so support top is only about **4.77% of core height** above its minimum and cannot form another body-height rear wall. Reported fraction of lowest-Y core sample within 0.1 three-dimensional units of ledge is 1.0, but this proximity number is **not** a biomechanics/contact stability certification.
- **Run246 B**: native GLB **5,136,712 bytes**, SHA256 `91492e695f03c54eb5339886c47793d930c1cc5d7a514e7d60ce6c1644ac9747`; 9 native meshes and **139,171 triangles** (support: 52,304 watertight triangles); support Y top = **-0.7229**, approximately **4.86% of core height** above minimum. Low-Y proximity fraction = 0.98224; same physical-contact caveat.

**Real Chromium + Three.js GLTFLoader + WebGL2** executed for seven distinct actual spatial cameras per variant (14 browser screenshots); all ten software quality gates per variant passed: native GLB SHA, WebGL2, mesh and triangle threshold, vertex NORMALs, nonmetallic PBR, down alpha, distinct frames, nonblank colors, and no fatal browser error. Actual driver was **ANGLE SwiftShader software rendering**, NOT an Android or iOS phone GPU. Performance counters are not mobile FPS.

Downloaded original [Run246 GitHub Actions evidence artifact](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44743011827/artifacts/14632605036): the **7,372,003-byte ZIP** has SHA256 `efb59307bf2e90ec586cfa64de7534b317bf30ce168a3f797fcae4370e487827`, exactly matching the GitHub artifact digest. Independently opened all **22** ZIP entries and verified CRC with no failures. Both native GLB bytes independently matched their separate expected SHA256s, and direct glTF/Trimesh reload confirmed all 9 meshes, real triangle totals, watertight environmental ledge, all mesh normals, bark metalness=0, and two versions' core bounds. All **14 screenshot hashes** matched the browser's own machine reports. The contact image is permanently saved at [Run246 14-view research-only comparison](run246-evidence/run246_AB_fourteen_actual_WebGL2_views_ART_UNAPPROVED.png), SHA256 `a647364655e7b650c957ff0d8462b16b4013efb9edfbb031a194ad2ea4a15a2e`.

## Actual opened visual verdict — still ART_REJECTED

The axis correction **succeeded visibly**: previous upright back-blocking bark ring is gone; a roughly horizontal, Y-up base visibly supports the bird, and the owl's rear is visible from a genuine back camera. But both newly modeled environmental ledges look like small beige scalloped stone/cookie plinths rather than a long, irregular, genuinely weathered mature eucalypt hollow edge with aged bark. B is broader but not more convincing. Both variants retained the same rejected bird: front heart-shaped disc is recognizable, but round eye structures are hollow-looking and too bright, cream down is coarse/sparse, body too upright, long remex-like adult wings clearly visible from side, tail/rear elongated, and back mostly featureless white. The reference chick is much rounder and fluffier, its wings short/buried and tail concealed. Surface support is plausible by view, but actual dual-foot physical contact, animations, phone WebGL FPS, memory, temperature and touch were not tested.

**The correct verdict is a verified technical scene-axis/mesh fix, NOT a usable beautiful juvenile owl pet. No art sign-off, no merge, no public preview, no deployment.**

## Isolation, spend, next nontrivial work

Branch delta from Run245 contains only a dedicated Run246 Python research file, dedicated Actions workflow, notes and generated machine reports/14-view contact. No modifications to `main`, root vocabulary game, production manifests, 251-species pipeline, existing kitten WebGL prototype or live deployment. Binary GLB and all individual browser screenshot originals remain in the separate 30-day Actions artifact (expected retention until **2026-12-20**). No external paid APIs, GPU accounts or purchases; extra paid amount **$0**.

The most productive next attempt is **professional anatomy and groom reconstruction of a true short down-buried juvenile wing**, full backside down layering, and a real weathered wood material, not another slight generic warp of the adult wing or another smooth "hollow" pedestal. **FINAL STATUS: ART_REJECTED / NO_RELEASE**.
