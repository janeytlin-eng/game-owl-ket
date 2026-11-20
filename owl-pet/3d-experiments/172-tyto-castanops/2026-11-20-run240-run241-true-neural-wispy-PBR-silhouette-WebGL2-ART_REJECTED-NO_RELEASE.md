# #172 *Tyto castanops* v3 | Runs 240–241 | authentic neural 3D down/ocular PBR and juvenile sculpt A/B

**Date:** 2026-11-20, Shanghai time. **Final verdict:** `TRUE_NATIVE_3D_TECH_PASS / SOFTWARE_WEBGL2_PASS / ART_REJECTED / PHYSICAL_PHONE_UNTESTED / NO_RELEASE`.

## Research and source audit

Re-read the owl-pet README and status, and the current design/science boundary in `owl-pet/research/species/172-tyto-castanops-v3.md` and review. The current interaction prototype is a cat and is **not** a release-ready owl. The #172 right-hand source is **AGE-UNKNOWN MESOPTILE**, not an evidenced exact age: an unusually thick cream second-down coat, developed dark-eyed heart mask, round compact crouch, tiny down-buried folded wings, concealed tail, both feet and belly securely resting on a wide old eucalypt hollow lip. The concept `owl-pet/design/concepts/172-tyto-castanops-v3.png` was actually opened and reviewed. Main and the 251-species owl prototype production workflow were not edited.

The verified Run239 B native Hunyuan model was used as a **real learned 3D source**, sha256 `84348c034e39287fe9a7a9d4054c46951d7543f06f1a304d63a623057de9beee`. It already contained learned core geometry, truly surface-following down, eye elements, UVs and PBR materials, and was previously rejected on art. Run240 then became the pinned source for Run241, GLB sha256 `71cc6ad479479008d79f7eaa0dd375aedd46d691ae1c493d949f9fcb5a9bb121`. No SVG, 2D spin, hollow primitive owl assembly, licensed paywall circumvention or chargeable external service was involved.

## Run240 — actual four-cell featherlets and ocular PBR test

Source: [native atlas and ocular study script](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run240-neural-softdown-fourcell-ocular-pbr-no-release/owl-pet/3d-experiments/172-tyto-castanops/run240_native_organic_down_ocular_pbr_ab.py). [Actual public CPU GitHub Actions execution](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44702808105).

Two new original binary GLBs were actually exported, re-imported with Trimesh and independently checked for all eight original real geometry groups, **86,867 real triangles** and **12,217 preexisting three-dimensional surface-following feather tufts**, with unchanged native neural positions, triangle indices, normals and vertex colors. The native GLB PNG was replaced by a four-cell tapered filament atlas, with UV retargeting, plus independent eye iris, pupil and reflection roughness. This is a material and feather-pattern study, not evidence of a newly sculpted body.

- A: 3,749,284 bytes; GLB SHA256 `9e0c096be65310444d69ec46de7ab03e3c4c346aa549547f07223bdd4a0dee78`; alpha cutoff 0.13.
- B: 3,754,384 bytes; GLB SHA256 `71cc6ad479479008d79f7eaa0dd375aedd46d691ae1c493d949f9fcb5a9bb121`; alpha cutoff 0.10.

Both were **really loaded by Chromium Three.js GLTFLoader** through WebGL2 and independently rendered in seven different spatial camera positions each. The native binary SHA, mesh topology, normal, non-metallic PBR, alpha-test material and nonblank nonduplicate camera gates all passed for both. Actual renderer = ANGLE Vulkan **SwiftShader software**, **NOT** a phone GPU or evidence of actual mobile frame rate. The actual 14-view [WebGL screenshot contact](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run240-neural-softdown-fourcell-ocular-pbr-no-release/owl-pet/3d-experiments/172-tyto-castanops/run240-evidence/run240_real_neural_14trueWEBGL_views_ART_REJECTED_NO_RELEASE.png) was opened for visual judgment.

Texture-program warning observed in the actual runner: `RuntimeWarning: invalid value encountered in power` and `invalid value encountered in cast` at `sin(pi*t)**fractional_power` near an atlas boundary. The models and browser images were nonblank and valid, but this must be clamped with `maximum(sin(pi*t),0)` in a later experiment; do not call the atlas mathematically clean. The resulting thin down still reads as repetitive hairlines at the QA scale.

Run240 ephemeral raw artifacts: [GitHub Actions artifact 14614076050](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44702808105/artifacts/14614076050), 5,843,729-byte reported ZIP, GitHub digest `sha256:dd1555a518cfe2f588340ef614a46fa64d6ca6130e67c6d47ac524e50e77c657`. Machine JSON and contact were durably committed to its isolated research branch; raw GLB is subject to the artifact retention window, **not permanent deployment**.

## Run241 — actual sculpt of the native learned juvenile body

Source: [reproducible neural sculpt/wing attenuation script](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run241-neural-juvenile-body-sculpt-and-wing-attenuation-no-release/owl-pet/3d-experiments/172-tyto-castanops/run241_native_juvenile_sculpt_3d_ab.py). [Actual public CPU GitHub Actions execution](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44703755992).

Starting with the exact binary Run240 B GLB (download SHA verification passed), two variants altered the actual native learned mesh `POSITION` and `NORMAL` attributes nonrigidly, compacting lower-body height, broadening the torso, shortening the rear silhouette and applying local mesh-neighborhood smoothing to residual adult-wing ridges. No ellipsoid replacement or new fake owl primitive was added. Source triangles, eyes, atlas PNG and fur UV attributes were retained. Source and results each have eight real mesh groups and **86,867 triangles**.

- A: 3,754,380 bytes; sha256 `2a7b5ada2d51537dec26462365523ecd0f63c1a053c2d7af2d6687789b6c43d8`; greatest actual core warp 0.13897 model units.
- B: 3,754,380 bytes; sha256 `480b69f0ad296cc91ee6fac521d688cb60510065e9b16d005a629878473c1981`; greatest actual core warp 0.23312 model units.

Both native GLBs re-imported with unmodified original triangles. Both again passed actual Chromium WebGL2 software smoke gates and seven **distinct, nonblank** views each. Actual [14-camera WebGL A/B contact](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run241-neural-juvenile-body-sculpt-and-wing-attenuation-no-release/owl-pet/3d-experiments/172-tyto-castanops/run241-evidence/run241_neural_juvenile_AB_14_real_WEBGL_ART_REJECTED_NO_RELEASE.png) was opened and compared with the original right-hand v3 concept; the B variant is palpably a little shorter and plumper but not yet anatomically or visually acceptable.

Run241 raw evidence: [Actions artifact 14614455807](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44703755992/artifacts/14614455807), reported 5,790,138-byte ZIP, GitHub digest `sha256:376573d76ccd5b76a799d6fb8e83f8e1ffe60d7643d7cb8b824be45ab7c105a2`. Reproducible script, workflow, screenshot contact and machine reports were committed on this independent research branch. Artifact is temporary; original binary files have not been permanently published.

## Independent visual gate: FAILED

I opened the original right-hand juvenile design image and the actual Run240 and Run241 WebGL contacts. **The white object is a true 3D owl study, but not the requested electronic pet**:

- **Heart face:** recognizable and two dark eyes present; glossy simple eyes and molded rigid forehead remain visibly artificial.
- **Cream mesoptile:** colour approximately pale enough, but featherlets lack the dense uneven soft halo and natural fibre layering of the source.
- **Proportions:** Run241 B is shorter/plumper than A, but still has a visibly long, ridged, folded **adult-style wing** and elongated side profile. B also looks somewhat over-compressed. Both fail short, down-buried wing and naturally compact juvenile requirements.
- **Back and side:** genuine geometry and camera consistency pass; texture and feather anatomy are weak, especially a bland rear silhouette and a folded adult-wing ridge.
- **Support/environment:** NO high-fidelity broad old-eucalypt hollow lip; underside and feet remain unsupported as a pet scene.
- **Mobile:** actual WebGL2 SwiftShader desktop headless pass only; real Android/iPhone WebGL GPU, memory, touch, thermal stability and frame-rate acceptance **not tested**. Synthetic software timing cannot be converted to phone FPS.

**Strict final gate: ART_REJECTED / PHONE_WEBGL_UNTESTED / NO_RELEASE**. A green workflow or valid native GLB is never product approval. No updates to deployed prototype, main, species production assets or user-facing pet. Additional paid cost: USD 0.

## Reproducibility and next obstacles

Run240 isolated branch changed only its dedicated study script, workflow and committed QA evidence. Run241 isolated branch added only its own script, workflow and QA evidence on top. Do not merge into main or rewrite the 251-species production workflow.

Next work should prioritize a **proper artistically supervised continuous juvenile sculpt** (bulk and short buried wing, face disc and down-laden back), real high-fidelity down grooming that reads at close and mobile views, and a genuinely sculpted / properly sourced old-eucalypt cavity lip. Fix the atlas `sin` fractional-power boundary warning; it has no excuse in a release-quality pipeline. Only after an external visual quality gate passes should a real physical phone WebGL test and product demo be considered. Until then, retain `NO_RELEASE`.
