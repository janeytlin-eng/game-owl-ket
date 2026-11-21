# #172 *Tyto castanops* v3 — Run268 postflight + Run269 native neural-mesh cleanup, ART_REJECTED / NO_RELEASE

**2026-11-21 (Asia/Shanghai).** Research-only, isolated from `main`, the 251-species production workflow, prior cat WebGL prototype and vocabulary game. No additional paid service was used. **Do NOT release any neural-derived sample: Tencent Hunyuan source has a noncommercial license, art is rejected, and no physical phone test exists.**

## Rechecked existing files and genuinely completed prior run

Read `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, prior Run267–268 record and existing #172 source/rejection rationale. On 2026-11-21 at 12:44:19Z, [Run268 Hunyuan3D-2mini CPU true mesh run](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44904352532) completed, not merely queued. [Original untouched artifact](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44904352532/artifacts/14707273954) ZIP 2,133,711 bytes, SHA256 `0c3cc3ee8f0ec506b81b4c907b9cdd813a59391149b0b9aa48715693e35a39f6`, was actually downloaded into an independent local container, CRC checked, and extracted. The standalone neural mesh `hunyuan_mini_cpu_native_UNREVIEWED_NO_RELEASE.glb` is a real native 2,944,900-byte GLB with SHA256 `b6004b868b8608bb3b1e9a489778de33e3fc1673a856b67824bb200ba5975b8b`, **74,597 vertices and 145,860 triangles**, six independently differing 3D VTK views; it is not watertight. Run268 logged 677.41 seconds to output real 3D. Its license is not production-cleared.

I actually opened the six spatial views: yes, a genuine sculpted heart-shaped facial disk, beak, wings and recognizable toes exist, but **eyes are blank white**, folded wings remain long and rigid; backside is a severe knobbly/crumbled shell, not cream-white down. No real tree-hole limb contact. Thus `ART_REJECTED`, independently of true mesh creation.

## New performed quantitative inspection: 862 connected components, NOT a single valid finished mesh

Using Trimesh on the actual Run268 source, computed **862 connected components**; the largest is a **watertight 133,268-triangle single body**. The other **861 isolated components account for 12,592 triangles**, including free-floating specks and larger disconnected patches, making visible debris. This is a concrete new diagnosis not evident from simple silhouette/triangle-count checks. Largest body's face, wing and feet remain organically continuous (not a few assembled primitives).

## Run269 actually executed locally: two genuine native-derived 3D variants and 12 real spatial images

Wrote and ran free, reproducible NumPy/Trimesh/VTK program to preserve only the one organic watertight component, then selectively apply VTK WindowedSinc smoothing (24 iterations, .08 passband) blended on rear **-Z** while leaving all front `z>=.12` vertices unchanged. **29,332 frontal vertices** are preserved exactly; **30,026** nonfrontal vertices moved more than .0005 units, maximum displacement `0.01589984`. Output smooth, source-faithful native GLB:

- `run269_island_pruned_back_smooth_TRUE3D_ART_UNREVIEWED_NO_RELEASE.glb`: **133,268 triangles, 2,665,764 bytes**, SHA256 `d7176ca11f6127a7b74390a714fae864dd24e404ed1ba63d45a0b751243199e1`.
- True VTK `vtkQuadricDecimation` .55 triangle reduction for a **technical-only mobile LOD**: **59,970 triangles, 29,950 vertices**, 1,199,852-byte GLB, SHA256 `0a4a8e72014cca087f6894f986eb0813d453de80f9ed5f8d7cc154ea4ea0a164`. Reduced LOD became **non-watertight**, another quality barrier; not claimed acceptable.

Rendered and actually visually checked six corrected 3D camera perspectives for *each* variant (frontal, 3/4, right, rear, left, top), with **12 distinct SHA256 image digests**; the previous Run268 side-view diagnostic used a misleading Z-up convention, whereas this pass uses actual **Y-up** orientation. All model variants are genuine independently reimportable 3D geometries, not planar photo projection or SVG. The cleaned model has less floating noise and a smaller reproducible GLB, but still has **white empty eyes, rigid unconvincing wing, clumpy hard rear surface, no dense layered cream-white down, no grounded feet/tree-hole**. Actual visual verdict: **ART_REJECTED / NO_RELEASE**.

A locally signed 21-member evidence ZIP with 18 SHA256-manifest files was created and independently CRC / per-file SHA256 verified: `owl172-run269-local-independent-evidence-NO_RELEASE.zip`, **6,569,889 bytes**, SHA256 `c5a7dcca33b16e0162a3f692a972a2d064d3519c2611d6f2ba34471ac2bd2fdb`. This is an **ephemeral local container artifact** and is not misrepresented as persistently stored in GitHub. The GitHub-run Run268 original is independently available as an actual Actions artifact.

## Independently dispatched GitHub Actions replication, actual remote obstacle

Created dedicated research branch `research/owl172-run269-hunyuan-island-prune-mobile-lod-NO_RELEASE` from Run268 experiment branch and committed the actual executable script at `tools/run269_back_surface_cleanup.py` (commit `e550a187215969aca37f954986c7424d8db4e1ac`). Committed an isolated artifact-generating workflow `.github/workflows/owl172-run269-hunyuan-native-clean-lod-NO_RELEASE.yml` (commit `ec7c09441949668170e5b803f3a648e3974f406e`); it reuses Run268's verified GLB, no new network generation, no payments and no production edits.

First actual [Run269 GitHub Actions](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44906090736) was triggered automatically but its real model step **failed** with `ImportError: no graph engines available!` (NetworkX missing). GitHub's top-level workflow conclusion `success` only meant the mandatory evidence-upload step succeeded; its 672-byte artifact had **no GLB**. Commit `7387c38feb657c169504ccdabd8073b8ddfb5da3` installed NetworkX, starting [second remote attempt](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44906234737), which still failed the geometry step because the Trimesh graph path also needed SciPy. Again, a nominal green workflow was **not** treated as model success. Commit `e6c91a0070505d0c81fb12119fecddc65fa762f6` installed SciPy 1.14.1.

**Actual final [Run269 successful remote native-geometry verification](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44906327130)** completed on the third attempt, with **both genuine 3D GLBs generated, 12 VTK physically different spatial images rendered, and independent GLB reimport/hash check passing**. Its raw [isolated GitHub Actions research artifact](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44906327130/artifacts/14708215783) contains 19 files, 4,509,605-byte ZIP, GitHub and independently recomputed SHA256 `5a2b83374c178948f47b63600b99b62bd0569b67b6983d243518846b2aa8ae1a`. Independent download, **19/19 CRC checks and 17/17 SHA256 manifest entries all passed**, and both original GLBs were reimported again in an unrelated environment.

Final remote machine-verified binary results differ slightly from the earlier local VTK 9.6 files due to different VTK 9.3 triangulation/smoothing algorithms; both variants are reported precisely rather than conflated:

| True 3D remote GLB | Tris | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| Pruned 861 free-floating components, rear-blended smoothing; original front intact | 133,268 | 2,665,764 | `161c21926b14226b245f045988019d620b0f3a0111d2ee4121bb75e1a13f1ef6` |
| Native quadric mobile-LOD reduction, still NOT watertight | 59,969 | 1,199,884 | `6feda6db1044f5f12e62c1015730a8c7f07ecd34df92021a8f209548413e1761` |

The CI VTK output has 29,332 unchanged frontal vertices, 30,900 rear vertices moved more than 0.0005 and max 0.022835 units displacement; remote VTK 9.3 is not byte-identical to the original local VTK 9.6 but reports the same actual 862-component/12,592-debris-triangle diagnosis. **Actually opened the final GitHub artifact's remote six front/side/back/top views for both models**. Both remain unambiguously **ART_REJECTED**: empty white eyes, long hard wings, heavy crusty unconvincing backside, no soft cream-white down or tree-hole support. Technical improvement must not be labeled artistic acceptance.

## Additional cheap independent local color-material negative-control (NOT REMOTELY ARCHIVED)

Also independently retrieved and SHA256-checked Run265b's original cleaned transparent rightmost chick reference (original evidence ZIP 3,743,794 bytes, digest `0e0125972a1bb1e1a9ac964469cf999860e5d3717bebd2122f7173332c7397c9`). On the **real Run269 continuous 133,268-triangle neural base**, performed actual UV-free 3D **directional reference-color sampling** into vertex colors, retaining organic 3D topology. Resulting genuine GLB 3,465,272 bytes, SHA256 `e19861586924918fb43f6152549e39879123a98a3e3c54c7938958d3f9be3bd0`, plus six additional local physical 3D VTK views actually generated and inspected. The eyes become brown/black, visibly closer to concept than blank white eyes, but the projection gives over-brown facial/chest color, over-rigid wings, awkward material transitions, and the entire rear retains an unconvincing spiky/crumbled surface. **ART_REJECTED / NO_RELEASE**. These six screenshots and experimental GLB remain in the ephemeral local workspace rather than falsely claiming a separate durable GitHub archive. No external paid generator was invoked.

## Quality and rights gates

- **True native 3D**: source Run268 true GLB confirmed, Run269 both locally exported and reimported.
- **Art**: explicitly rejected after real multiview side/back inspection. The current model is not a beautiful chick and should never be shown as the accepted pet.
- **Software WebGL2**: in this local Chromium/Playwright runtime, `canvas.getContext('webgl2')` returned null even with ANGLE SwiftShader flags. Thus Run269 **WEBGL2_UNTESTED / ENVIRONMENT_BLOCKED**, never transfer older model's software-WebGL checks.
- **Phone hardware**: neither Android nor iPhone physically tested, with no FPS/memory/heat/touch verification.
- **Rights**: Tencent Hunyuan non-commercial; no production rights established.
- **Branch isolation**: only #172 research code/CI/audit on new branch, no changes to `main`, 251-species pipeline, source reference, existing cat prototype or deployed site.

**Final acceptance: ART_REJECTED / WEBGL_UNTESTED / PHONE_UNTESTED / RIGHTS_UNCLEARED / NO_RELEASE.** Next research gate should use genuinely better juvenile facial/feather topology and artist-quality material, rather than claiming coarse surface smoothing will create down.
