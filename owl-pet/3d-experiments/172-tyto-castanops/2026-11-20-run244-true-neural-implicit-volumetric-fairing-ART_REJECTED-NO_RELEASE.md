# #172 *Tyto castanops* v3 — Run244 TRUE neural 3D volumetric wing-fairing study

**2026-11-20 Asia/Shanghai · Result: ART_REJECTED / NO_RELEASE · physical phone not tested**

## Rechecked before new work

- Read `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, the species-specific `owl-pet/research/species/172-tyto-castanops-v3.md`, and full Run243 rejection with its real WebGL2 14-view contact.
- Opened the real `design/concepts/172-tyto-castanops-v3.png` and compared the **far-right** juvenile at full resolution. Age is not precisely established. Its required cream second down, natural heart face, squat body, buried very short wings, hidden tail, supported feet and broad weathered eucalyptus hollow lip remain distinct acceptance criteria.
- Verified the previous Run242 authentic source Actions ZIP by SHA256 before extracting. Original ZIP **6,186,461 bytes**, SHA256 `72d59b3135983fa9a4712486e52526cc90c023a9fcd0b0e6669dfd4d9864d2db`; source native Hunyuan GLB **3,831,092 bytes**, SHA256 `ef60639bbba95a0e876ac427b277fa500063b9ce05d9b9c8bae5811a5c0518d1`. This source is a real 3D learned sculpt, not a visual stand-in. `main` continues to hold the old cat interaction prototype and 251-species production is separate.

## What was actually computed locally

This is a **different geometry representation** from Run239–243's repeated direct spatial displacements. Using free Python Trimesh, SciPy, scikit-image and VTK, Run244 voxelized the existing actual continuous neural-body triangle mesh at pitch 0.025 scene units, computed its full volumetric occupancy, performed volumetric morphological closing and 3D Gaussian fairing, reconstructed an organic isosurface with marching cubes, and transferred the implicit surface displacement back to the original learned neural 3D body surface in a localized side/rear mask. Its real feather cards were retargeted using a nearest-3 weighted 3D displacement interpolation. Original facial region, original colours/UVs, six real eye components, body triangle connectivity and all native fur alpha texture were preserved. No SVG or ellipsoid/primitive owl was assembled.

Two 3D variants were actually exported and **re-imported** locally, each with eight native meshes and 86,867 actual triangles, and both passed finite vertex and input SHA checks:

| Trial | Implicit filter | Actual new GLB bytes | Local SHA256 | True core vertices displaced >0.01 | Max true 3D movement |
| --- | --- | ---: | --- | ---: | ---: |
| E | sigma 3.25 cells, isovalue .52 | 3,831,092 | `b09de76bfb72c96b9018d9288a25390b9b0817a4aef83cdc3970755f988c5b19` | 2,818 | 0.04422 |
| F | sigma 4.75 cells, isovalue .55 | 3,831,092 | `671798ec285ab9593d243982b0758d3f04ef37c6aa38475c4aa6a589b129ae92` | 4,865 | 0.07611 |

The 3D implicit fields genuinely contained 15,930 (E) and 14,498 (F) vertices before target-to-original learned-mesh retargeting. This is not a 2D cutout or spin-render.

## Actual local visual QA — both REJECTED

Used **VTK GLTFImporter with true 3D front, left, back and oblique cameras** on source/E/F (12 actual raster frames), and opened the full 1,200×970 image contact, then compared with the original right-side concept. This VTK view is an exploratory native-raster *silhouette* check and its muted material is **not** a correct final PBR screenshot.

Result: E/F marginally smooth some back/wing grooves and change the rump outline, but the long, clearly adult-style down-sweeping wing and protruding rear tail remain strongly visible at left and oblique perspectives. The neural scaffold is still too upright rather than a compact, broad, soft chick, the existing down cards barely register as convincing thick mesoptile, and no broad physical tree-hollow ledge is present. The original eye mask is still sculptural/hard. The subtle volumetric surface transfer is insufficient; F is not a new approved base.

This distinct failed route is useful: local volumetric fairing with preservation of old topology **cannot reconstruct missing juvenile wing anatomy or thick layered down**. Further tiny local parameter changes are not the next priority. A **true artist-driven juvenile mesh/retopology and layered down groom** is needed; credible hollow support and actual handheld WebGL GPU/controls verification are still separate gates.

## Remote reproducibility and safeguards

- Original 3D code and [dedicated GitHub Actions workflow](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run244-neural-implicit-surface-wing-fairing-art-reject-no-release/.github/workflows/owl172-run244-neural-implicit-mesh-webgl.yml) were created on **isolated research branch** `research/owl172-run244-neural-implicit-surface-wing-fairing-art-reject-no-release`; no main production/deployment changes.
- [Run244 Actions execution](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44724537054) was actually triggered. It re-fetches the SHA-pinned prior source, recomputes native E/F GLBs, reimports them, attempts **seven genuinely separate Chromium WebGL2 spatial screenshots per model** using the existing Run237 GLTFLoader QA, hashes PNGs, and uploads originals as a 30-day *research* artifact (not a permanent pet release). Success or failure must be checked before claiming remote results.
- Free tooling only; external paid USD 0. No physical Android/iPhone GPU has been used. Neither VTK nor software Chromium is phone certification.
- **Release: NO_RELEASE. Art approval: FALSE.** Source is research-only and neither model should be promoted to the game or linked as a finished pet.

### Final remote verification

Pending the current actual GitHub Actions job and original artifact readback. Do not mark remote WebGL pass or original artifact verified based on workflow creation alone.
