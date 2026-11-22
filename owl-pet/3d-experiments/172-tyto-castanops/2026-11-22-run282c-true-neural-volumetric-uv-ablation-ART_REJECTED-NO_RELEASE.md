# #172 *Tyto castanops* v3 — Run282c authenticated neural volumetric retopology / ART_REJECTED / NO RELEASE

Date: 2026-11-22 Asia/Shanghai. This is a **research experiment only**. No sample is approved for display, release, commercialization, or physical-phone use.

## Upstream checks and original target

Before implementation re-read `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, the retained kitten/WebGL description, and the [Run281 MIT TripoSR real 3D / Run281b art-rejected record](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run281-open-triposr-cpu-young-owl-NO_RELEASE/owl-pet/3d-experiments/172-tyto-castanops/2026-11-22-run281-MIT-TripoSR-rightmost-juvenile-CPU-NO_RELEASE.md). Reopened the **actual rightmost** 512×512 reference photo (SHA256 `8eee63bf0b8650c390d4c4bba6a07a0c2dd05dd7fc2e90e00a896ec3ab51c641`) and the Run281b genuine 3D GLB (SHA256 `46f22943806075ec749d96f1bafa630fee256a02e6048839c428101fc9c12e12`) from their separate GitHub Actions evidence archives.

Target is cream-white dense fluffy down, heart-shaped facial disc, dark small eyes, round fledgling/owlet body, short folded wings, coherent side/back anatomy, natural supported feet on an old eucalyptus hollow, realistic mobile WebGL behavior. None of these quality gates may be inferred from one front photo or successful file import.

## Actual new native 3D experiment and baseline

**Distinct technique:** Rather than reattach geometry spines, paint bump maps, or deform the older adult donor, attempt to repair the rocklike, noisy MIT TripoSR mesh via **volumetric level-set retopology derived from actual 3D reconstruction**. Authenticated source has **51,795 real vertices, 103,084 triangles**, but is non-watertight with 110 disconnected components. The largest authentic connected shell has **100,534 triangles**; removing 2,550 micro-fragment triangles is not a cartoon primitive replacement. Voxelize the real mesh at pitch **0.007**, fill interior, binary close / fill holes, apply two independent **3D Gaussian field** sigma values **1.5** and **3.0**, extract the 0.47 iso-surface using actual marching cubes, fix winding where needed, and reimport glTF output.

Both outputs retain a genuinely three-dimensional continuous reconstructed body, built from the neural surface rather than a sphere/ellipsoid/2D billboard. Pixel-based UV material is independently bound to the actual spatial geometry: front pixels come from the exact reference and rear is a neutral subtle cream texture. This **is not legitimate evidence of hidden-side appearance**. The normal-based front/rear UV atlas transition was explicitly expected to cause side-color seams. In local testing the original default SimpleMaterial inadvertently darkened texture by a `baseColorFactor` of `[.4,.4,.4,1]`; this was identified through direct glTF JSON inspection and corrected to nonmetallic PBR with white baseColor before final tested exports.

## Actual local execution, quantitative evidence and manual visual review

Executed using free Python NumPy, SciPy, scikit-image, Trimesh, PIL, VTK with a real offscreen renderer; both native GLBs were independently reimported and rendered from six different spatial axes (+Z, +X, -Z, -X, +Y, -Y) for **12 true 3D camera frames**, not composited rotations of a flat photograph.

| Output | Real mesh vertices | Real triangles | GLB bytes | SHA256 | Watertight |
|---|---:|---:|---:|---|---|
| sigma 1.5 | 67,944 | 135,884 | 4,083,424 | `00997ef58d115b21d067173e1ab3c1898d8cde01a2c277d848d73cfd8dd31c50` | yes |
| sigma 3.0 | 64,614 | 129,224 | 3,896,944 | `a31b2b6ec21713dde992ad944b2398ab285258839dc6d30349d5bfcf20ec6b70` | yes |

Local independently generated evidence ZIP: **5,753,463 bytes**, SHA256 `05fa3f47e2c129c9586bf0305ae4e3a95a807a33387b0473228c471a6fefb2a2`, **22 entries**, ZIP CRC passed and **21/21** SHA256 member hashes matched. Contains both actual GLBs, source-backed texture, both six-view sets, QA JSON, and standalone manual visual-review note. The GitHub Actions re-execution may have different GLB hashes if package/library versions differ; do **not** equate local and remote files without checking.

**Visual art verdict: ART_REJECTED for both variants.** Opened actual six-view montage and individual reference. Sigma 3.0 does indeed eliminate much of the initial hard rock/cauliflower-like surface, and the extracted surface is now closed; but the result looks like a **smooth stone/rubber shell** with severe brown/gray UV seams. The heart-shaped face is flattened/dark, folded wings/wing layering are absent, side profile is wedge-like and incoherent, rear is featureless without soft down, and feet look like malformed artifacts. Sigma 1.5 retains extra surface ridges. The original reference's fine fluffy cream down does not survive this reconstruction method. No eucalyptus hollow contact and no believable real-world pet anatomy.

This is a measured **engineering cleanup**, not even a preliminary art pass. A front photograph projected on true 3D is not proof of satisfactory hidden geometry, and a watertight mesh is not a successful electronic pet. Further smoothing alone would erase anatomy faster than it restores it.

## Independent GitHub reproduction

New, isolated research branch: `research/owl172-run282c-genuine-neural-voxel-reto-gltf-NO_RELEASE`. Submitted only:
- `owl-pet/3d-experiments/172-tyto-castanops/run282c_neural_volumetric_3d_ablation_NO_RELEASE.py` — provenance-checked *actual neural mesh* retopology, two whole GLB outputs, six native views each and reimport.
- `.github/workflows/owl172-run282c-real-neural-voxel-texture-NO_RELEASE.yml` — free CPU reproduce/QA/sha256/archive, failures explicitly fail closed.
- This audit. No changes to main, 251 species production pipeline, original concept/manifests, kitten prototype or deployment.

Triggered a real independent [GitHub Actions Run282c](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44975310956) from the branch commit. Source evidence is fetched from previous verified GitHub Actions artifact IDs **14733361023** (genuine upright GLB) and **14733006902** (rightmost concept 512px); hashes are checked before any modeling work. The final remote success and evidence are recorded separately only after independent inspection; a workflow being launched does not imply success.

## Explicit remaining blockers and next direction

**ART_REJECTED / MOBILE_GPU_UNTESTED / RIGHTS_NOT_CLEARED / NO_RELEASE**. Neither iPhone nor Android GPU, memory, frame rate, overheating, touch or animation has been tested. TripoSR's MIT code/weights alone do not establish independent rights to the concept's source imagery. No external paid credits or paid services used.

Future work must solve actual juvenile three-dimensional sculpture, heart-shaped raised disc, real folded-wing silhouette and back feather tracts **before** surface fur/UV polish; a professionally sculpted young owl with groomable down or reliable additional side/back references is needed. Do not promote this archive, its attractive front projection, or any technical GLB pass to a product demo.

## Run282c remote GitHub Actions fully completed and independently reverified

**Actual independent execution:** [GitHub Actions #44975310956](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44975310956), original successful run at `b6cd836ec9434c5f24e273b1263d116aaef4c18f`, all workflow steps completed successfully including source download, provenance SHA check, free CPU native modeling, twelve VTK spatial views, artifact upload and fail-closed gate.

**Evidence artifact:** [Run282c #14735970352](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44975310956/artifacts/14735970352), repository metadata size **5,796,105 bytes**, SHA256 `287d31b956ea738a7a1c2ee487dea9923470fae1d56a9e6f358e35600e827348`, expires **2026-12-06 02:17:23 UTC**. This is a temporary research archive, not a released/approved sample.

Downloaded the actual GitHub artifact back into an independent analysis environment. **26/26 ZIP members CRC-passed; 24/24 individual archived SHA256 sums matched**; original execution status states `mesh=success`, `image=success`, `generation=success`. Both native GLBs were **independently reimported from the downloaded remote archive**, confirming true mesh topology, watertightness and embedded texture. The remote versions differ modestly from local builds because of different numerical/package-version behavior; never imply byte identity.

| Independently generated GitHub GLB | Vertices | Triangles | Bytes | SHA256 |
|---|---:|---:|---:|---|
| level-set sigma=1.5 | 67,924 | 135,844 | 4,082,276 | `d1088daa89cdc0c8e085600283c69103688c6fd7562a3a7d82f74a07f0fc083f` |
| level-set sigma=3.0 | 64,586 | 129,168 | 3,895,344 | `5eb3064d07495bfdc120ee6a420671c0bce07c118bdad31123c88d5113e10e88` |

**Actual opened remote six-view image and independent art decision:** both remain severely below the original rightmost cream-down owlet design. The sigma 3.0 shape is smoother and technically valid but resembles an artificial pebble or molded shell, loses natural feather layers, retains front/rear paint seams, has distorted wings/feet and no realistic owl side/back anatomy. **ART_REJECTED / NO_RELEASE**, irrespective of machine assertions. No real phone GPU test.

This audit and the original code are retained on a strictly segregated research branch. The GitHub Actions artifact has independent model bytes and view frames as a short-term audit trail, not a permanent model asset.
