# #172 *Tyto castanops* v3 — Run129 real CC0 source geometry and native 4-view art QA

**Date: 2026-11-17. FINAL: ART_REJECTED / NO_RELEASE. Actual no-cost 3D acquisition and Blender inspection. No premium chick model approved, no user preview, no physical-phone claim.**

## Preflight / source of truth

Read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/prototype/index.html`, `owl-pet/research/species/172-tyto-castanops-v3.md`, original concept path `owl-pet/design/concepts/172-tyto-castanops-v3.png`, and existing Runs123–128 source/sculpt reviews. Do not confuse old kitten WebGL prototype, a flat reference image or a cartoon bird with a satisfactory sculpt. #172 remains the **rightmost cream downy age-unknown mesoptile** with integrated heart facial disc, small dark eyes, short down-buried wings, concealed tail, supported feathered feet and old eucalypt hollow. Never claim an exact juvenile age.

## Real public-source experiment and actual binary mesh

New isolated research branch `research/owl172-run129-open-cc0-source-actual-geometry-gate`; code `tools/run129_no_fee_cc0_geometry_source.py`; dedicated GitHub workflow `.github/workflows/owl-pet-172-run129-free-cc0-source-native-qa.yml`.

On [successful final actual Actions Run129](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44020376814), Python made real unauthenticated requests and read response bytes:
- [Gobkit official free catalogue](https://gobkit.com/api/free) **HTTP 200, 587,631 bytes, JSON**, 397 listed models over 37 packs in the live response. Its licence field asserts **CC0-1.0**; publisher's [free assets page](https://gobkit.com/freebies) describes no account, no payment, commercial reuse, and hand-authored low-poly style. A catalogue licence is creator/publisher's declaration, not independent warranty of upstream rights.
- Official catalogue's entry `id=owl` yielded the exact public file URL `https://gobkit.com/freebies/animalB/Owl.glb` (not a guessed or protected download token). Actual **HTTP 200 `model/gltf-binary`, 156,676-byte GLB**, SHA256 **`339a2eafd291fe1c2352d93d0755ca10a1c34d0b83b560a91cdca73053db3685`**. glTF v2.0 header/file size valid, true source mesh **310 indexed triangles**, one skin, one material, one texture, and **four animation names** (`idle`, `attack`, `dead`, `walk`). Internal glTF metadata also declares CC0. This was **real third-party geometry** but expressly low-poly game asset, not a professional chick sculpt; never promote it as the target.
- [Gobkit community catalogue](https://gobkit.com/api/community) **HTTP 200**, 24 returned items for this request; no source was downloaded from that endpoint.
- [Gaitkit eaglet](https://gaitkit.com/asset/eaglet) listing HTTP 200 exposed a **Pro** download indicator, and is a different bird; **no paid asset was downloaded**. Pixabay yellow chick listing returned **HTTP 403**, and is an unrelated species even if accessible. Additional external spend **$0**.

**Data-extractor caveat:** `catalog_summary.owl_matches=[]` in recorded JSON is a defect of the exploratory regex filter despite the separately extracted and validated `candidate[0].catalog_id=owl`. It must not be misrepresented as zero owl entries; source candidate/file evidence is authoritative for this run. No claim of exhausting all 397 visually.

## Actual four-orbit native Blender QA and visible art judgment

Execution used Ubuntu runner **Blender 4.0.2**, genuine `bpy.ops.import_scene.gltf` on the downloaded GLB, unmodified imported mesh, Cycles CPU **18 samples**, and actual **540×540** PNG renders at nominal front/45°/90°/180°. Native inspection reports object `Owl`: 670 Blender vertices / **310 faces**, plus importer-created `Icosphere`: 42 vertices / **80 faces**, for 390 Blender faces total. This imported helper is **not** extra artist-quality down on the bird. Three lighting-area objects and an orthographic camera were used for observation, not to synthesize an owl. All four source renders and JSON metrics are in `research-evidence-run129-REAL-PUBLIC-CC0-GLB-ART_UNREVIEWED-NO_RELEASE/`.

I actually opened the four archived image files in the session. The bird is a **hard-edged orange-brown geometric toy**: angular horn-like ear tufts, two huge circular white eye rings with black disks, a sharp yellow projecting beak, plain faceted spherical/rounded torso, broad planar adult wings, plainly visible rear tail and long bare stalk-like legs. The side and back are coherent **as a toy**, not as any downy *Tyto castanops* juvenile. There is **no organically integrated heart-shaped facial disc, no cream-white fine down, no tucked juvenile wing morphology, no correct supported feathered feet, and no eucalypt hollow**. This is far below the premium target and fails the user's explicit no-primitives/no-toy acceptance gate.

**Final ART_REJECTED**, not just source listing unreveiwed. No WebGL browser or physical phone GPU tests were run for this art-rejected candidate: lightweight 310-triangle geometry is not evidence of a usable high-quality *Tyto* pet, and no good reason exists to ship it. Its four animation clips remain a potential **engineering-only** reference, inferior in aesthetic relevance to the earlier rejected Run126–127 10k-triangle rig.

## Real failure repair / preserved negative evidence

Three honest workflow executions, none mislabeled as art success:
1. [Run129 initial](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44020092258): valid GLB retrieved, Blender glTF import failed because Ubuntu Blender lacked NumPy. Source and failure log archived.
2. [Run129 NumPy repaired](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44020239785): GLB imported but scene initially had no world datablock (`NoneType.color`), so no four view until fixed. Failure log was archived.
3. [Run129 final fixed](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44020376814): installed `python3-numpy`, initialized neutral Blender world, disabled absent denoiser, **actual four renders all saved**, evidence archived, uploader completed, scoped evidence committed. All final `run129_steps.txt` values are `success`.

The final SHA256 manifest `SHA256SUMS.txt` lists the four PNG images, all execution logs and source/four-view metrics; `sha_checked.log` contains independent `sha256sum -c` check results. Rejected raw source binary was **not committed, uploaded as artifact or shipped**, even though publisher declares CC0; its exact official download URL and SHA256 preserve provenance and repeatability. The four 3D **rendered** angles are not an interactive model.

## Isolation and next useful standard

Research changes only under `owl-pet/3d-experiments/172-tyto-castanops/**` plus the **single Run129 dedicated workflow**. Against Run128 base `8db87c689fe043e93ece1a9cf6ac87dffc1f83bc`, GitHub compare showed no edits to `main`, root vocabulary game, `owl-pet/prototype`, 251-species production/manifest, user v3 original concept PNG or deployed site. No unauthorized payment.

This experiment confirms that open, no-login CC0 **technical rigs** can be fetched and genuinely rendered, but their toy geometry cannot solve the professional high-quality juvenile sculpt bottleneck. Next trials must prioritize a legally obtained anatomically juvenile *Tyto*-like continuous sculpt, real cream down / integrated face / hidden wings / natural feet / tree hollow, independently inspected in 360° **before** technical mobile WebGL and physical-phone GPU acceptance. **No qualifying new sample; NO_RELEASE.**
