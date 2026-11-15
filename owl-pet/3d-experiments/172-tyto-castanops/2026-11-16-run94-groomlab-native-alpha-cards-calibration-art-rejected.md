# Run94 — native Blender glTF GroomLab PBR/alpha card calibration and true four-view negative art gate

**2026-11-16 (Shanghai local time); Verdict: ART_REJECTED. No public model, user demo, app changes, or production rollout.**

## Ground truth and previous failures checked

Re-read the repository's `owl-pet/AGENTS.md`, `README.md`, `research/species/172-tyto-castanops-v3.md` and Run92C audit. Directly opened the actual original `owl-pet/design/concepts/172-tyto-castanops-v3.png`: the target is **rightmost** cream downy juvenile, compact head and body, dark eyes framed in a **feathered** tan-edged heart disc, short down-buried wings, both substantial feet supported by a hollow lip. Original source plate is a front view; it does **not** establish exact side/back shape or age.

Directly opened Run93 GroomLab four-way `four_views.png`: it displayed an apparent coarse prickly spherical card system. Discovered a critical ambiguity: Run93 render code used **VTK**, whose opaque-looking cards did not establish how glTF alpha-masked, normal-mapped PBR would render in the target pipeline. Instead of calling that art failure certain based on the VTK picture, performed actual Blender/GLB tests.

## Actual no-fee execution and distinct engineering test

Independent research branch: `research/owl172-run94-groom-cards-alpha-calibration`; executable workflow `.github/workflows/owl-pet-172-run94-groom-alpha-calibration.yml`; experiment `tools/run94_groom_glb_alpha_multiview.py`. Reused **verified actual GLBs**, not a 2D owl or a new synthetic sphere:

- Source Run92C connected sculpt GLB SHA256 `6bc98227580d178e5750c6abd8903c31d956172b6afeacf20257dabf661d2d53`.
- Run93 genuine free GroomLab mesh-card GLB SHA256 `b1aa292c614ad93a819e1985005634433bf24beb02012398aa8f06f922442be6`.
- Removed the source's prior experimental soft-alpha-card mesh but preserved its real anatomy geometry; imported the GroomLab cards retaining glTF alpha `CLIP` material and texture nodes.
- Imported both GLBs in Blender, exported three new GLBs and **freshly re-imported each** for the native Cycles four-azimuth renders.
- Compared raw GroomLab card positions to two true mesh-component-scale reductions (`0.22` and `0.08`); registered card components against the real source body using a triangle-mesh BVH surface projection. This manipulates actual 3D hair-card vertex geometry; it does not substitute sprites, SVG or fake screenshots.
- Validated 12 Blender Cycles PNGs (3 variants × front, three-quarter, strict side and rear) and created a full 3×4 contact sheet. No physical Android/iOS GPU, standard mobile FPS, animation, rigging, touch, or thermal test.

First CI attempt [Run94 initial failure](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43759121914) imported/exported a raw GLB but aborted during render because Ubuntu's free Blender was built without OpenImageDenoiser. Modified the actual script to disable unsupported denoising. The second [Run94 successful Actions execution](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43759236174) completed all 12 Cycles renders and archived original binaries.

| Actual GLB | Bytes | True round-trip triangles | SHA256 | Verdict |
|---|---:|---:|---|---|
| Raw card alpha | 3,061,576 | 123,736 | `69091ede15696a6ccf7c5d3a53bccf72f656b814cf102ae28bf86ec50c02c40b` | Rejected |
| BVH-projected cards, 0.22 scale | 3,062,920 | 123,736 | `c9913e70dd42a41c0568443bf00cb0f9bdd8f72fdedbf3b4fc5d1968f75857cf` | Rejected |
| BVH-projected microcards, 0.08 scale | 3,068,920 | 123,736 | `d996375b71658444854d369aa7c1db0bcb25c2993fee92ac22fa578c4e679ddf` | Rejected |

The groom GLB had **3,168 triangles, 3,968 vertices and 400 connected card components**, larger than desired down fragments. The raw GroomLab cards' median centroid-to-body surface distance was **0.4984 model units**; the alpha-aware Blender render visibly showed an entirely **separate hair-card spherical cage underneath the owl**, not a usable plumage layer. This proves an alignment/registration failure in the Run93 GroomLab combination and explains the earlier VTK visual to a better degree than assuming the shader alone.

The BVH-registered shorter cards removed most of the detached cage: 0.22 reduced component maximal radius from about **0.170** to **0.0374 model units**, while 0.08 reduced it to **0.0136**. Yet both casts show **only grey speckling near the belly**, not the soft cream layered down of the target. This tests a genuine technical improvement in spatial registration and disproves that correction alone makes the sculpt artistically acceptable.

## Mandatory visual review of the actual original PNGs

Opened the actual contact sheet `run94_three_scales_four_azimuths_ART_REJECTED.png`, all 3 variants × 4 fixed views, and compared with the original #172 v3 rightmost chick.

- **Raw**: smooth white egg/penguin-like bird, two black protruding bead eyes, flat graphic heart, separate grey spherical card cage under its perch; grossly incorrect.
- **0.22**: separate cage no longer visibly hangs from perch, but the body remains a flat white egg with grey belly stipple, no true feathered heart rim, no plausible tucked-wing shape, feet not credible, and rear featureless.
- **0.08**: microcards largely disappear at review distance and add essentially no down softness; the same weak skull/neck/wing/foot anatomy persists. Strict side/back still fail.

**Art gate: ART_REJECTED.** Engineering GLB validity and native alpha PBR work do not establish a convincing *Tyto castanops* juvenile. The experiment eliminates a misleading rendering/registration failure mode but does not rescue the model. No user-facing demo or deployable model link should be offered.

## Archival, verifiability, safety and cost

The successful job permanently committed the source GLBs, three new unapproved GLBs, 12 native Blender Cycles PNGs, the 3×4 contact sheet, metrics JSON, logs, explicit rejection marker and 22 internal SHA256 rows to:

[Run94 quarantined actual research evidence](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run94-groom-cards-alpha-calibration/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run94-GROOM-ALPHA-CALIBRATION-ART-REJECTED).

Re-read the remote metrics, actual contact-sheet pixels and manifest: all three output SHA256 values in metrics match the archived SHA256 manifest, each model reports an actual re-import with 123,736 triangles, and all 12 view paths are present. Branch comparison with parent `research/owl172-run93-groomlab-free-groom-engine-probe` found changes confined to the Run94 workflow, Run94 script and Run94 quarantine evidence. **Main was not modified**; no 251-species production, taxonomy, plate, cat app, source animation or online deployment touched. No paid 3D API or model-generation credits used.

**Next technical obstruction:** a professional juvenile anatomically authored base mesh and physically convincing heart-shaped feather tracts. The current GroomLab approach can produce correctly located cards, but inherited toy-like shape plus sparse cards remains unsuitable. Do not iterate only on card length/density or call software alpha rendering a phone GPU pass.
