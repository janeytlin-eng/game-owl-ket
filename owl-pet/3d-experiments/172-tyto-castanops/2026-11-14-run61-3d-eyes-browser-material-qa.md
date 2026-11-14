# Run61 — #172 *Tyto castanops* v3 rightmost mesoptile — 3D eye-depth ablation (2026-11-14)

**Status: ART_REJECTED. Research only. NOT a deployable/showable owl pet.**

## Live preflight / input
Re-read `owl-pet/README.md` (f25561f5a25383ec03406e78262f45b21b703cae), `owl-pet/AGENTS.md` (b9ebde6dc406354b77d4297089a6f8f928f3b878), `research/species/172-tyto-castanops-v3.md` (5c754f9daf8433ba608107e389659b0271b1480a), and `research/reviews/172-tyto-castanops-v3-review.md` (50ab5259987180a6a46a428317440f2436bfce56), plus Run10/Run11-12 historical experiments. Retrieved and inspected the owner’s Run58 and latest Run60 Drive ZIPs and Run60 QA; visually compared the original right-hand cream bird concept and Run60 J model's front/three-quarter/true side/back renders. This is a one-view artistic reference, not a measured 3D anatomical scan; age and side/back morphology remain uncertain.

## Actual run
Using free local trimesh, VTK, Chromium, Playwright and Xvfb, loaded Run60 J (actual 3D GLB), created and reimported **two new real GLB variants A/B**: add a pair of separate 3D eye-globe corneas, subtly contoured elliptical 3D eyelid rings and specular glints. Changes are limited to eyes, not a new complete juvenile anatomy. Each variant: **23 meshes, 83,204 triangles, 3,872,168 bytes**. Body remains watertight/winding-consistent after UV-seam welding. SHA256:
- A `b22e057c3045ae31c84103435b03309d56a0ecbb68832138bc06499c0ca5e2fb`.
- B `ee9fb4f57ea258902bde764492f7b351dedd0017f16dc5c04f2223096ba1f084`.

Performed **8 real VTK renders** (front / oblique / strict side / rear × A/B). Independently ran **16 Chromium WebGL2 draws** with corrected glTF material parsing (A/B × 390×600 emulated mobile viewport and 800×800 desktop × four angles); all 16 `gl.getError()=0`, 23 meshes, one embedded texture, no JS exceptions. Not physical mobile hardware or true Three.js GLTFLoader/PBR. Browser test initially had a MATERIAL BUG: prior custom viewer erroneously used `p.material !== undefined` as a synonym for `baseColorTexture`, applying the bird's texture to the new dark corneas (white eyes). Isolated QA viewer fixed to test `pbrMetallicRoughness.baseColorTexture` and to use `baseColorFactor`; reran all screenshots. Corrected browser screenshots show dark corneas.

## Artistic verdict
**A and B ART_REJECTED**: the glossy globes look like artificial button eyes, and B still has hard synthetic eyelid rings. Major unchanged blockers: smooth pear-shaped trunk, no soft cream mesoptile down, frontal photo-mapped face, anatomically implausible feet/wing/scapula, and rear and side inferred from a front-only reference. No reliable professional-model, PBR or real-phone pass. No user sample notification.

## Independent local evidence and archival status
Created 47-file `Owl172_Run61_3D_EYE_ANATOMY_ART_REJECTED_QA.zip` containing both GLBs, Run60 J base GLB, reference crop, full scripts, corrected browser fixture, eight VTK images, sixteen corrected Chromium screenshots, QA audit, structural/browser JSON, SHA256 manifest and logs. ZIP integrity and its 46 internal file hashes verified. ZIP size **16,123,949 bytes**, SHA256 **56bdd4dfc654a0185958fb387c292fe7a18327ec03dc4e3f38555129cfa4c655**. Local runtime path `/mnt/data/Owl172_Run61_3D_EYE_ANATOMY_ART_REJECTED_QA.zip`; **remote binary upload FAILED** with `AccessDeny` (twice, for ZIP and text): do not report a remote binary QA archive. This markdown is the permanent source of failure analysis, not binary evidence. No paid tools, no approved image edits, no changes to 251-species pipeline, existing pet prototype or game's root code.

Next: do not simply accumulate eye parts or down feathers. Obtain genuinely professional multilayer juvenile sculpt/groom and vetted side/rear morphology before a real-phone glTF PBR, animation, frame-time and touch gate.

## New no-fee source scouting (post-build)
A focused public image/source search found two **photographer-documented juvenile Tasmanian Masked Owl** observation sets (these were **not** used as model textures and **not** downloaded into the GLB):
- Luke O'Brien, 2016-01-27, [Tasmanian Masked Owl at the Raptor Refuge](https://www.lukeobrien.com.au/tasmanian-masked-owl-raptor-refuge), showing a captive/rescued juvenile “Montgomery”, identified in the article as about two months old, with photos of residual juvenile fluff, feet, climbing/hopping postures and wing emergence. This is **not** evidence for the exact unknown-age cream mesoptile in the concept; use only as taxon-relative gross physical anatomy and posture comparison.
- Luke O'Brien, 2018-01-28, [Young Masked Owl at the Raptor Refuge](https://www.lukeobrien.com.au/young-masked-owl-raptor-refuge), showing fluffy juvenile “Bentley” and close-up relationships between head disc, body and supported feet. The webpage does not establish a mesoptile age standard or precise 3D scan.
- Comparative only: [Australian Wildlife Conservancy Northern Masked Owl branchling](https://www.australianwildlife.org/news-and-resources/news/uncovering-the-secrets-of-the-northern-masked-owl), different taxon (`T. novaehollandiae kimberli`), not species-evidence for `castanops`.
All photo copyright and reuse permissions must be independently checked; **view as anatomy reference only, never copy/project into a commercial/released GLB without license**. Existing owner-concept remains canonical art target and `science=false`. This may help human sculptor(s) resolve why current front texture projection, shoulders and claw support are anatomically wrong.
