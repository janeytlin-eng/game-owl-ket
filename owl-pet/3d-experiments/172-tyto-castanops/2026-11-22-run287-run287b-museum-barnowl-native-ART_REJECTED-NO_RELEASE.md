# #172 Tyto castanops v3 rightmost cream-white downy fledgling — Run287 / Run287b museum barn-owl anatomy baseline

**2026-11-22 (Asia/Shanghai). Final gate: REAL_TEXTURED_NATIVE_3D_PASS / SIX_CORRECTED_REAL_VIEWS_PASS / ART_REJECTED / MOBILE_WEBGL_UNTESTED / PHONE_UNTESTED / SOURCE_RIGHTS_NOT_CERTIFIED / NO_RELEASE.**  
**Research only. No consumer sample or production asset was released.**

## Read-first / protected scope

Before starting, read `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, the prior kitten `prototype/index.html`, and Run286's audit; independently downloaded and examined prior Run281 TripoSR original, Run284 procedural sculpt, and Run286 adult-donor evidence including the #172 v3 **rightmost** cream-white fluffy chick cropped reference. Earlier bases are visibly wrong: rock-textured single-view neural mesh, oversimplified toy, and a 399,999-triangle adult ear-tufted owl. No modification to `main`, its 251-species concept workflow or manifests, source #172 art, kitten prototype or deployed site. Separate experimental research branch only.

## Actual new no-extra-fee native 3D source

Instead of more adult-to-chick primitive shape warps, located a real-species-specific publicly available **barn owl museum taxidermy scan**, the Virtual Museums of Małopolska “Barn owl” (adult, not *Tyto castanops* chick), originally published as [Sketchfab model 0e65de5934db4f0eae02835ba7227dcc](https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc) with a publisher **CC0 claim**. Found corresponding same-model-ID native GLB via publicly readable [model gallery](https://doc.ayootech.com/galeri) at `https://doc.ayootech.com/galeri/model/0e65de5934db4f0eae02835ba7227dcc.glb`. **License provenance is not independently certified**; the gallery is a third-party mirror. Do not assume this verifies the original rights chain. No login bypass, account purchase or additional payment.

Actual independent GitHub Actions download HTTP 200 / `glTF` magic. **43,225,496-byte native GLB**, SHA256 `6412ffd575360397bd90d391d3d4c23397f225945cdef3ec5727bfd91504cd44`. Trimesh imported **12 real mesh parts, 261,966 triangles, 756,317 vertices**, actual nontrivial embedded 1024×1024 textures. The model includes the adult perched on a branch and round timber base, with genuine 3D side and back feather shapes, but adult proportions/long developed wing/tail and mature coarse feather pattern.

## Run287: acquisition PASS, initial rendering FAIL despite nominal job success

[Run287 GitHub Actions 44997966088](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44997966088) completed successfully; [research artifact 14744925898](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44997966088/artifacts/14744925898), independently downloaded. ZIP **23,497,408 bytes**, SHA256 `1e6e77af5a5675b0ff6e24d3da0782c1b2a72519473e6be32c7342dfd01f6bd5`, same as GitHub digest, **13/13 entries passed ZIP CRC**. Source GLB and geometry are genuine.

**Critical false-success caught by actual image inspection**: the workflow used VTK `vtkGLTFImporter` which silently failed to create any renderable actors (`Error loading model metadata`); all six named PNG shots were near-blank beige squares, each just 1,554 bytes. Thus the **Run287 six-view QA claim is invalid** although the workflow status was green. Do not cite Run287 as proof of art or rendered geometry. This was identified by opening the actual exported contact sheet, not inferred from logs.

## Run287b: corrected real texture / transform six-camera pipeline PASS

Replaced the broken loader for the render QA with native GLB import in Trimesh, applied each mesh's actual scene transform via `scene.dump(concatenate=False)`, built VTK actors from the original true triangle vertices, UV-sampled the native material's 1024px PBR base textures into per-vertex colors, and set up two actual lights. Set **six distinct 3D camera positions**, not 2D transforms. Added fail-closed checks that the foreground occupies >0.8% of each frame and six PNG SHA256 digests differ. This is independent textured 3D space inspection, **not real-time browser WebGL**. It creates no new juvenile art and cannot be described as a native VTK glTF import.

[Run287b GitHub Actions 44998202292](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44998202292) completed successfully. Independently downloaded [corrected research artifact 14744309028](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44998202292/artifacts/14744309028): **24,110,732-byte ZIP**, SHA256 `8bca1ee3ea90bce2abe0d0bc40c377b2a857f4e508f890a890d0cc78547ecfb1`; same digest as GitHub; **11/11 ZIP entries pass CRC and 9/9 embedded SHA256 file checks pass**. Original source GLB SHA256 still exactly pinned. All 12 actual GLB meshes carry 1024×1024 embedded base textures. Real full-space camera views: front, oblique, right, back, left, top, each at 480×480px; all six have unique SHA256. Foreground occupancy fractions: **11.14%, 7.75%, 10.17%, 9.62%, 9.65%, 8.98%**, proving nonblank views. Opened the actual 1440×1002 contact sheet and independently reviewed all six: realistic 3D true side/back silhouette and perched foot grip, not 2D image rotations. Job self-validation and independent archived-hash verification both succeeded. Evidence artifact expires around **2026-12-06**; not permanent release hosting.

## Art gate and mobile gate — explicitly REJECTED

The real six-camera contact sheet shows a **grey-brown adult barn owl taxidermy** with a rigid long-flight-feather silhouette, mature legs/talons, slender upright body and branch-on-wood-display base. It does possess a species-typical facial disk but **not** the correct rightmost concept's soft cream-white down, rounded infant proportions, shortened folds, dark-eyed youthful face expression, naturally layered baby fluff or actual old-eucalyptus nest-hollow grasp. It is also **Tyto alba**, a different species from the target **Tyto castanops**. Do not recolor or relabel this adult specimen into a product. No animation, proper topological rig, juvenile mesh, remesh LOD, tactile interactions or interactive electronic pet was made. **ART_REJECTED / NO_RELEASE** without exception.

The GLB includes 261,966 triangles and large textures, with branch and mount unnecessary for a mobile pet. No Chromium WebGL2 load, physical Android/iPhone GPU frame rate, device memory/thermal tests, or touch QA was run. Do not call it phone-ready. The original publisher claims CC0 but secondary mirror identity and full rights chain remain unverified. $0 additional external spend; fal paid/cloud generation not initiated, and a zero-budget tooling lookup required interaction unavailable in this automated run.

## Follow-on, bounded goal

**Positive research outcome:** a genuinely adult barn-owl anatomy/feather direction reference and a fail-closed true textured 3D six-camera QA path, with a concrete silent-renderer bug fixed. **Negative product outcome:** high-quality adult reference still cannot stand in for juvenile sculpt and real groom; no release.

For next attempts prioritize an independently licensed high-quality **young Tyto** artist-sculpted base or actual reference-multi-angle juvenile, and GLB-compatible real groom / art quality before mobile QA; do not exhaust resources with more primitive patching, grey noise feathers, or mere tech-success reports. All newly created workflow and audit files remain within isolated #172 research work. No consumer-facing 3D owl is available.
