# #172 Tyto castanops v3 — Run234 / Run234b / Run234c real adult museum scan, texture and native glTF experiments — ART REJECTED, NO RELEASE

**UTC date:** 2026-11-20. **Target:** canonical rightmost creamy fluffy `AGE-UNKNOWN MESOPTILE` from `owl-pet/design/concepts/172-tyto-castanops-v3.png` (737,545 bytes, SHA256 `881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d`). **Do not release:** all experiments are genuine 3D *adult* donor models, not a passing nestling pet. **Mobile WebGL:** NOT TESTED. **Incremental spending:** $0.

## Canonical repository and prior state checked

Re-read `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, and the previous Run229–233 failure/art audits. The only existing interactive prototype is a *cat*. Original #172 plate passes **2D concept only**. Its juvenile should have a developed heart facial disc, eyes and bill, full cream second-down, compact crouch, short down-buried wings, invisible tail, belly and both feet on an old wide eucalyptus hollow lip. No precise developmental age or invented nest contents. **251-species production is separate.**

[Run233 official Hunyuan mini-Turbo five-step local CPU neural inference](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44668960253) was still executing at this audit's first inspection, so **no result or GLB is presumed**; previous standard 20-step CPU run timed out. No paid provider or quota bypass used.

## Actual experimental source — true photography-derived 3D, not primitives

Reobtained original adult barn owl museum asset from [Zenodo record 21379215](https://zenodo.org/records/21379215), labelled **cc-zero** in its repository metadata (not a legal clearance opinion). The originally compressed 5,603,344-byte file SHA256 is `3fff5130cfad17cc1fcf312819019bad75782f4f01708d18696e100d643691cb`. Correctly Draco-decoded native glTF GLB: **6,380,156 bytes**, SHA256 `4865f48828adb93cef4f5ec07002adc1a61855a80adb286f781a227fca89430f`. Independently parsed **30,412 real photo-scanned triangles / 24,036 vertices**, 3 textured PBR maps, genuine vertex NORMALs and UVs. It has **1,282 disconnected geometry components** and is not watertight, so it is not automatically a clean organic sculpt basis. This is a brown **adult** Tyto scan with mature remiges, tail, visible legs and artificial wooden perch.

## Run234: two real GLBs, 14 actual spatial camera renders, remote reproducibility CONFIRMED

Recolored source PBR photo atlases through CIELAB transformation to two distinct variants (**warm cream** and **cool ivory**), while preserving the source's real photogrammetry mesh, UV and PBR channel semantics as far as Trimesh re-export allowed. Corrected an important prior camera orientation bug: **apply glTF scene node transforms via `scene.dump()` before rendering**. Then exported/reimported two genuine native GLB files and rendered true front/back/left/right/oblique/top/bottom cameras each using VTK/Xvfb: **14 valid distinct nonblack views**.

On the dedicated [Run234 GitHub Actions](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44670343314), the full workflow **completed successfully** and independently produced:
- warm cream native GLB **12,611,988 bytes**, SHA256 `4c03ded6b51641d32af96b18d7c2edfee0e7e6b6442e5c3d400c88f4f8df09a1`
- cool ivory native GLB **12,640,276 bytes**, SHA256 `d4c4818c1d95bf76527f64f0cb4d7f086c61f9b16db322dd8bd127bba248dd1c`
- 14 true 3D camera PNGs and contact sheet (269,321 bytes, SHA256 `e44c961f715ac22a18e1c8f74f3cdd7b2b1539c611a13faa3909a7d0578f9198`).
- Remote zipped machine evidence: **43,599,008 bytes**, SHA256 `4532d6760710744ddf3830e8b1474f55434f557bc0cbe99c6e69509e2a174964`, **23 entries**, archive integrity checked, downloaded and opened locally; artifact [14599229579](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44670343314/artifacts/14599229579) temporary (expires 2026-12-20).

I actually opened and visually examined the remote **14-view** contact sheet. Both are still unmistakably adults; the plumage looks bleached and sculpturally stiff, with long flight feathers and perched adult legs, no fuzzy baby anatomy, no compact body or broad tree-hollow support. **ART REJECTED**.

## Run234b: actual rough mobile-size experiments, 14 further real views, ART REJECTED

Resized Trimesh-transcoded baseColor PBR images of the valid **12,611,788-byte local** warm variant from 2048 to 1024 and 512 and re-exported/reimported two original polygonal 3D meshes. 1024 atlas yielded **10,474,644 bytes**, SHA256 `8a6b5d2314be5dabcba22635e7438f9b6176778589b773a76ee3b01b8981f78f` (16.95% smaller); 512 atlas **9,724,696 bytes**, SHA256 `4ce3d2857dc3964a2bc8d587408857863716a1568b2698f2d0862652be09140f` (22.89% smaller). Both produced seven independent 3D VTK viewpoints (14 total), image sheet SHA256 `7a653e4ea4775eaca112eadda11b7ce113fba3f3c37fa7a86bba1ad6e82cbda7`. This is a size-only proxy, **not** a phone GPU/browser FPS test. These intermediate binaries currently exist only in the local sandbox, NOT the remote GitHub archive.

## Crucial new negative finding and corrective Run234c

Independent inspection of the GLB JSON/buffer revealed why Run234 re-exports were abnormally large: **Trimesh duplicated 3rd/4th PBR map entries, emitted 4 PNG images instead of original 3, and dropped the `NORMAL` vertex attribute**, inflating source from 6.38MB to 12.61MB. Simply shrinking the diffuse baseColor atlas in that flawed export barely reduced total mobile payload and silently degraded normal-vector metadata.

As a distinct, executed experiment, created a native GLB binary-chunk editor that directly transforms the original **JPEG baseColor** using CIELAB without changing original triangle/indices/UV/**NORMAL**/normal map/AO-roughness maps or image references. Exactly 3 source image slots are retained; no duplicated atlas; all outputs were re-imported and spatially validated:
- 2048 diffuse: **6,011,276 bytes** SHA256 `19b280a1319343811147c220526620d4f5a785124e547dbfa9228473688da08d` (5.8% smaller than 6.38MB source)
- 1024 diffuse: **5,720,596 bytes** SHA256 `fd80599f86e06c1d9afccbbcabfed519fbb9123de362a3cab0b1e097f2c10a61` (10.3% smaller)
- 512 diffuse: **5,610,504 bytes** SHA256 `f33572873d86fe86af2bb454337a104a8dee742be21d8c7f5b601682115202d2` (12.1% smaller).

Using the corrected actual scene-transform camera system, performed **seven native 3D camera renders on the 2048 version and seven more on the 512 version** (14), reopened the two-resolution comparison contact sheet and confirmed the adult's shape remains consistent but emphatically **not a juvenile**. Local SHA of 14-view contact PNG `run234c_14_REAL_3D_VIEWS_PBR_NORMALS_PRESERVED_ART_REJECTED.png` is available from Run234c machine report. Source mesh is real, not SVG or primitive substitutes. The corrected standalone source is now committed as `run234c_native_gltf_PBR_mesh_normals_preserving.py`, and [Run234c remote reproducibility workflow](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run234-museum-cream-material-real-3d-qa-no-release/.github/workflows/owl172-run234c-native-gltf-preserve-normals-qa.yml) has been triggered. **Remote completion and full remote hashes must be read back before claiming remote Run234c validation**.

## Strict gate, isolation and next technical bottleneck

**ART_REJECTED / NO_RELEASE / PHONE_WEBGL_UNTESTED.** Real photo-derived adult geometry, CIELAB recoloring, normal preservation and correct GLB export do not create genuine baby 360° anatomy or fluffy second-down. A professional, true juvenile heart-disc/short-wing/concealed-tail/hollow-footed sculpt plus believable groom is still the gating need. Further adult-mesh color tweaks have diminishing returns. Mobile target performance must be checked on actual phone WebGL only after the art passes.

All work is confined to independent `research/owl172-run234-museum-cream-material-real-3d-qa-no-release` branch: standalone experiment scripts and dedicated GitHub Actions; no changes to `main`, 251-species pipeline, existing WebGL cat prototype or deployment. No paid generation, subscription or unauthorized private asset access.


## Run234c remote execution / independent ZIP readback — VERIFIED after initial audit

**Live [GitHub Actions Run234c](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44671103661) completed SUCCESS**, all checks including actual source checksum, real native GLB generation, 14 independent VTK cameras and artifact upload passed. **Green CI means technical geometry and archive only, NOT art acceptance.**

Downloaded the actual 20,332,592-byte GitHub Actions artifact ZIP and independently checked its complete SHA256 `a9b31afc84fe2b815d28ac2aef52e984d7f79fc84a1f9fb9730440ff921f75ad`, ZIP integrity (22 entries, no CRC corruption), machine JSON, and real binary contents of all three remotely generated GLBs. Separate temporary artifact [14601030123](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44671103661/artifacts/14601030123), 30-day research retention.

Exact REMOTE results, different binary SHA from the independent local experiment because metadata serialization varies:
- 2048-px diffuse: **6,011,308 bytes**; SHA256 `f471a37bc171699e002cbbfaac08898889a3d4489444cc26977148c871f3e037`.
- 1024-px diffuse: **5,720,608 bytes**; SHA256 `a590d7357b850cd92c725d3eb4c5eccb755d6705e1085174032e89856c45c84e`.
- 512-px diffuse: **5,610,516 bytes**; SHA256 `398c7dc6d654b54aea7cbaefc7937d9cc054ab7a838b2270ecfc433e96943d19`.
- Remote fourteen-view contact sheet 257,918 bytes, SHA256 `da8a495209e52fd3c734b3453b296a21908cbecfa5544bef29e5d95fe1912c43`.

A second independent, programmatic GLB v2 inspection on the **downloaded remote bytes**, not merely the CI report, confirmed for all three models: **30,412 triangles, 24,036 POSITION vertices, 24,036 NORMAL vertices, valid finite 3D vertex normals, valid UV, exactly 3 retained PBR textures and 5 glTF buffer views**. Real GLB magic and byte length matched and Trimesh scene import succeeded. I then actually opened the 14-view sheet: still whitewashed adult owl with long adult flight wings/tail, hard surface, exposed legs/perch, NO downy nestling, NO natural hollow lip. Unambiguously **ART REJECTED / NO RELEASE / PHONE WEBGL UNTESTED**.

Run233 official diffusion CPU experiment remains separately in progress at this final audit, with no independently verified generated GLB yet; its later status must be checked independently and should never be inferred from these adult donor successes.
