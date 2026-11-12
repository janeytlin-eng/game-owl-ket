# #172 棉棉 3D Run10 — actual CC0 asset import, compact GLB, rejected juvenile mesh transfer (2026-11-13 +0800)

## Source boundary rechecked

- Read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, Run08/Run09 reports and the exact original concept blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`.
- The target remains the **rightmost cream, age-unknown mesoptile**, not an adult: thick soft down, warm-buff heart face, dark eyes, invisible full-length wing/tail, lower round crouch and two feet supported on an old eucalypt hollow edge. Developmental age and precise taxonomic plumage remain unverified.
- Previous Run09 GitHub Actions: its **third** attempt `43263153618` succeeded with an independent adult base and 4 rendered views; first and second failed (numpy dependency, distro Blender denoiser). The actual artifact was downloaded for this run, reopened locally and visually inspected. Adult reference is plainly a **great horned owl** with ear tufts, golden irises, long rectrices and adult wing feathers; thus **not a usable juvenile Tyto image**.

## Actual local 3D work in this run

- Extracted Run09 verified Actions artifact `13964263321`, a real Blender import and render, and inspected the four-camera sheet as *meshes*, not 2D flips.
- Implemented actual binary glTF image-bufferView repacking (`tools/optimize_glb_textures.py`), maintaining all scene node/mesh/material/UV bindings and replacing 2048px textures with 512px images; tiny genuinely flat maps become 32px. Opaque base-colours JPEG, normal maps PNG. Ran on the actual downloaded CC0 adult model: **20,670,700 → 2,718,708 bytes locally**; 129 meshes/62,592 triangle scene re-import check preserved. Isolated pipeline run produced a reproducible 2,719,036-byte variant.
- Implemented and ran true mesh transfer (`tools/refit_owl_juvenile_anatomy_experiment.py`), removing the source species' ear tufts and exposed tail and deforming its actual skinned-looking body topology to a round lower crouch; shrank retained real wing feather geometry. **v24** 115 mesh nodes, 59,736 triangles, 2,643,920-byte runner GLB. Note that the mesh does **not** have a skeletal skin/animation merely because its physical geometry was moved; don't mislabel this as rigged. Rendered independently by local VTK and by actual GitHub-hosted **Blender 4.0.2** from four real cameras.
- Executed a further **v25 A/B** locally to shift the genuine owl texture and wing coloration toward cream, darken irises and lighten bill (`tools/recolor_reference_trial.py`). GLB exported and VTK 3-angle raster check was inspected; local v25 ~2.2MB. This recolour makes the body paler but reduces plume definition, and **is visually worse than the required natural soft down**. v25 is not included in the runner artifact; only its source is permanently archived.
- New separate and constrained CI file `.github/workflows/owl-pet-172-run10-transfer.yml` was run via independent trigger `run10-trigger.txt`: [actual GitHub Actions run 43266413692](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43266413692), **completed successfully**. Runner downloaded real licensed-source adult GLB, ran scripts, static auditor, Blender four-view render and artifact upload. This proves the free toolchain and file exchange, **not** juvenile art acceptance.
- Run10 evidence artifact `13965413613`: [download the NOT APPROVED QA archive](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43266413692/artifacts/13965413613) (expires **2026-11-26T17:12:04Z**; 14-day retention). Contains original CC0 GLB, 2.7MB optimized adult, 2.6MB v24 experiment, real four renders, import stats, static mobile audit, hashes and Blender log. Artifact ZIP digest `sha256:69e37f527f43c77185c284b5a83abd68e7578815c77d2166455dca520a1d0a37`.
- Independent hash evidence, CI: external original `c11c94db20065c6c6f252e768e8c748f22dc69ef9b4e7199110b96de0625c12e`; optimized adult `b898b84ca67535a8627c465533557f001fcd3ac67558768dd53fc7684dbc1e45`; v24 `694a930687b22b16f5fbc09e06f7020b58e92b33e74332f047ad5b906af7a705`.

## Actual independent quality gate

- **Art FAIL** after viewing Blender's actual front/threequarter/side/rear renders of v24. The face is generic round/eye-shaped without a Tyto heart outline; eyes remain yellow, the huge cream fluff is replaced by close-woven adult body texture, silhouette is a smooth egg/pear, short wing looks like a scratch, feet/tarsus remain adult-stiff with no believable support on a hollow lip. V25 cream mapping likewise still lacks depth, natural down fibres and correct eye/face anatomy.
- **Technical preflight WARN_OR_FAIL:** v24 59,736 triangles and ~2.64MB fit rough budgets, but independent `audit_glb_mobile.py` detects **448 near-zero-area/degenerate triangles** using its declared 1e-18 cross-norm-squared cutoff; source optimized adult had 64. V24 has 0 animations, 0 skins, 0 morph-target meshes. 13 images decoded, ~6.32MB RGBA texture memory before mipmaps. This is a *static* approximation only. The workflow's subsequent Blender export is 3,565,996 bytes, without artistic approval.
- **Phone/WebGL NOT TESTED.** A passing Linux Blender import and static glTF parser is not an actual phone GPU, animation, fps, shader, memory or touch test.
- External legal provenance: [Innerscene Owl](https://www.innerscene.com/tools/library/3d-parts/owl-d696472a) presents its original asset as CC0. This is an adult anatomy/texture source only; not evidence that horned-owl morphology represents *Tyto castanops* mesoptile.

## Persistence and isolation

- Permanently on GitHub main, **only dedicated experimental tooling/workflow/marker/report**:
  - `tools/optimize_glb_textures.py`
  - `tools/refit_owl_juvenile_anatomy_experiment.py`
  - `tools/recolor_reference_trial.py`
  - `.github/workflows/owl-pet-172-run10-transfer.yml`
  - `run10-trigger.txt` plus this document.
- The validated binary GLB and rendered PNGs are retained in a time-limited **Actions artifact**, not in the permanent main branch. No claim of permanent binary archiving; this toolchain can rebuild while source is available, but remote publication and real-phone verification remain undone.
- Did not modify #172 concept, research reviews, 251-species manifest/production, existing prototype or original production workflows. No paid model generator, no charges.

**Decision:** **do not display/ship** any v24/v25 sample. This finds a functioning no-fee Blender + real CC0-geometry + compact glTF pipeline but proves that repurposing an adult horned owl cannot substitute for a reference-conditioned Tyto chick sculpt. Next meaningful step is truly sculpting an anatomically correct warm heart face, age-appropriate eye/bill/feet, and organic fluffy down groom and then testing a real phone runtime. No more cosmetic ellipse or colour-only variants.
