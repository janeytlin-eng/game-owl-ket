# #172 *Tyto castanops* v3 — Run321 native anatomical-relief sculpt A/B / ART REJECTED / NO RELEASE

Date: **2026-11-23 (Asia/Shanghai)**. **REAL NATIVE GLB A/B GENERATED / ACTUAL 12-VIEW VTK AND 6-VIEW WEBGL2 / TECH PASS / ART REJECTED / RIGHTS HOLD / PHYSICAL PHONE UNTESTED / STRICT NO RELEASE**.

## Scope, scientific and process baseline

Re-read [owl-pet/AGENTS.md](../../AGENTS.md), [README](../../README.md), [STATUS](../../STATUS.md), [#172 v3 visual review](../../research/reviews/172-tyto-castanops-v3-review.md) and [Run320](2026-11-23-run320-real-native-microgroom-AB-ART_REJECTED-NO_RELEASE.md). The canonical source is [#172 v3 original three-bird concept](../../design/concepts/172-tyto-castanops-v3.png), **RIGHTMOST** age-unknown chick. Required: broad organic heart-shaped face, dark eyes, cream thick mesoptile, rounded juvenile form, almost hidden short wings, hidden tail, correct side/back, strong feet on old eucalyptus hollow. Scientific age is not established. Run320 failed because fiber scratches do not fix the base wing/shoulder/egg-back sculpture. Production of 251 species is separate and ongoing.

## New actual modeling experiment (not another surface-particle or color trial)

- Obtained the exact real native original **Run317 Stable Fast 3D textured GLB**, SHA256 `c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be`, 1,137,108 bytes, 27,372 triangles. It is not a billboard/SVG or a primitive assembly.
- Tested a different idea: reshape the **existing contiguous UV-textured 3D mesh itself**. Deform its real vertices on bilateral lateral/upper-dorsal shoulder regions with continuous falloffs and three shallow scapular relief tracks, preserving face, claws and original texture. No spheres, cards, additional simple meshes, new inference or paid tool.
- **Variant A**: strength 0.55, maximum individual vertex displacement **0.035249 m**; 95th percentile **0.023598 m**. **Variant B**: strength 1.0, maximum **0.063549 m**; 95th percentile **0.042788 m**. Source and both variants all contain **27,372 triangles**, one real UV-textured mesh. Both round-tripped through independent Trimesh GLB import with matching vertex locations.
- Produced and actually opened **12 native 3D VTK spatial renders** (untouched baseline, A, B × front, right, 135° rear oblique, back); compared a real 3×4 montage. Then regenerated on GitHub Actions, loaded both output GLBs in true Chromium / Three.js GLTFLoader / SwiftShader WebGL2 at **390×780 emulated smartphone viewport** and actually opened their six front/right/back screenshots. This is **not a physical iPhone or Android trial**.

### Exact final remote native files

| Asset | Bytes | SHA256 |
|---|---:|---|
| A | 2,556,852 | `b6e7afe8ede07d941576fcade79c639871d1306e8fb19916b8e5d45eec9efb6e` |
| B | 2,556,856 | `6a81d66c5d6f5ab8ed0f594687ee8cb20df29d8ae26a922df97871ee8c4f863b` |

Both **WebGL2 pass**: one mesh, 27,372 triangles, valid UV and single material, three genuine different angles each, model loaded. A logged one non-blocking 404 resource request; B logged no browser console error. No camera-orientation mistake from previous experiments. Three.js r170 / Chromium SwiftShader CPU GPU; hardware frame times, device temperature, interaction responsiveness, memory and WebGL on real phones **unverified**.

## Repeatable silhouette diagnostic (NOT an art approval metric)

An independent, committed [diagnostic script](run321_silhouette_diagnostic_NO_APPROVAL.py) compares four true 3D VTK render angles using the unchanged native model; background fixed by corner sampling; silhouette = max RGB deviation >25; no learned or arbitrary aesthetic score. Ran on the **independently downloaded remote artifact**.

- **B vs original, right-side silhouette IoU = 0.997652**: only **217 / 92,427 union-mask pixels (0.235%)** change.
- **B vs original, back silhouette IoU = 0.954090**: **5,155 / 112,284 (4.591%)** change.
- **A vs original, right IoU = 0.999047**; back = **0.976581**. Even 6.35 cm peak displacement fails to carve a recognizable tucked wing silhouette on the visible side.

These figures objectively bound what this deformation accomplishes; IoU does **not** measure feather aesthetics and must never grant automatic release.

## Actual visual art verdict — both REJECTED

I opened the 3×4 true 3D comparison and all six real Chromium screenshots. A and B both still look like an elongated textured **egg / upright oval** on the back and right side. B's slightly reshaped back surface is not separate or naturally nested short wings, scapular and contour-feather masses, fluffy volume or a credible bird shoulder. Natural heart disc remains an inherited texture/geometry feature, not newly sculpted feather architecture. Both retain inappropriate isolated source-bottom/feet instead of anatomically supported eucalyptus-hollow contact, and a smooth rear despite inherited fine texture. No improvement near the professional art bar; **ART_REJECTED / NO_RELEASE**. Do not show user as a preview, publish, merge, deploy or count as a completed species/model.

**Consequence:** This A/B falsifies the hypothesis that continuous whole-mesh vertex relief alone repairs the image-to-3D egg-back. Together with Run320, do **not** repeat more numeric displacement, feather density, or trivial surface material tweaks. Next necessary new path is an artist-authored juvenile multiview base sculpt or a demonstrably higher-quality native juvenile 3D source with explicit rights, built-in heart-face/wing/shoulder structures and truly volumetric mesoptile before real phone QA. Existing source is governed by [Stability AI SF3D community licensing](https://huggingface.co/stabilityai/stable-fast-3d/blob/main/README.md); product rights/commercial conditions have **not** been approved. Zero extra paid credits.

## Independent reproducibility and remote evidence

- [Isolated Run321 source](run321_anatomical_surface_relief_NO_RELEASE.py)
- [Repeatable silhouette diagnostic](run321_silhouette_diagnostic_NO_APPROVAL.py)
- [Isolated workflow](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run321-integrated-sculpt-relief-AB-ART_REJECTED-NO_RELEASE/.github/workflows/owl172-run321-integrated-sculpt-AB-NO_RELEASE.yml)
- [Actual successful remote GitHub Actions run #45157783073](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45157783073)
- [Raw remote 30-file research artifact #14809088127](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45157783073/artifacts/14809088127), scheduled expiry **2026-12-07 10:39 UTC**.

Downloaded the raw artifact ZIP from GitHub and independently verified **7,533,869 bytes**, SHA256 **`e21c9ae4fb99240401dd7b89ac0df7e2fc58d789f42e20b3a976aa173391a650`**, **30/30 ZIP CRC entries passed**, **27/27 internal-file SHA256+byte checks passed**. Images actually decoded and opened; data was not merely inferred from workflow success. Includes original native GLB, two distinct sculpted real GLBs, 12 distinct original VTK views, six actual Chromium screenshots, model/source manifest, logger and NO_RELEASE file. Diagnostic computed independently on downloaded remote raster evidence, not claimed to be part of the original ZIP. Persistent branch commits contain code and review; binary artifact has an expiration and is **not** claimed to be permanently in Library.

### Isolation

All source, evidence and audit belong to **research/owl172-run321-integrated-sculpt-relief-AB-ART_REJECTED-NO_RELEASE**, derived from previous isolated Run320 research branch. **No writes to main**, no concept PNG overwrite, no 251-species manifests/production status modification, no root word game changes, no existing kitten prototype or Sites deployment modifications. Strict **NO_RELEASE**.
