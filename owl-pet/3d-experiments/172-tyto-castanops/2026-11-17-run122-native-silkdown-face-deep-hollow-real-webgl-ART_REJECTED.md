# #172 Tyto castanops v3 rightmost downy chick — Run122 real native 3D sculpt, soft-filament and WebGL trial

**2026-11-17 Asia/Shanghai | FINAL ART_REJECTED | NO_RELEASE | No added payment | No production edits.**

## Read-before-experiment and actual biological / visual target

Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/research/species/172-tyto-castanops-v3.md`, the previous Run121 trial and original 1536×1024 `owl-pet/design/concepts/172-tyto-castanops-v3.png` Git blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`. The ONLY target is the **rightmost** age-unknown cream-white juvenile, not either adult. Art reference requires a gentle warm tan/cream **heart-shaped facial disc organically integrated into plumage**, two small dark recessed eyes, a very compact feather-coated head/body, dense soft cream down, short down-buried wing silhouette, thick fluffy shanks and broad feet physically supported by a realistic aged eucalypt hollow lip; 45°, strict side and back must hold up.

Run121's **actual** 2,827,088-byte source GLB, SHA256 `f04fd9b65371aecaa63c42f7245b30053a0156504096bbeae52107f451a64370`, was a real Blender loft/sculpt export, not a flat SVG. Its original four genuine reimported Cycles views nevertheless showed cartoon bead eyes, a wide flat facial patch, spherical/snowball body, excessive long sharp crown needles, bare spidery toes and a cookie/wreath-shaped support. Earlier Run119 native grooming and Run120 supposed-CC0 adult great-horned owl asset were rejected. Do not market yet another primitive-derived bird as professional sculpture.

## Actual execution, including two retained debugging failures

Branch `research/owl172-run122-heart-integrated-silkdown-sculpt-gate` created from Run121 SHA `82fff6d10213fbfe4eee2978bc00e423386a4ff0`; new isolated sculpt script `tools/run122_silkdown_anatomical_mesh_trial.py` and dedicated `.github/workflows/owl-pet-172-run122-heart-silkdown-qa.yml`.

The toolchain uses free Ubuntu runner Blender 4.0.2 (no separate paid 3D credits). It **imported the SHA-locked original Run121 GLB**, actually modified its existing continuous connected body shell with shallow heart brow/cheek/shoulder vertices rather than replacing the owl with disconnected spheroids, pulled eyes inward and reduced their scale, moved bill closer to head, warmed up down material, deleted original bristly ribbon hair, sampled a new set of **8,351 real tapered crossing 3D fiber shapes** rooted on the existing mesh, and replaced a flat lip with a deeper connected eucalypt hollow wall mesh. This is a technical test, not artist sculpt accreditation.

- First Actions run **43983301750** failed at GLB import due missing Debian `python3-numpy`; source validation and failure logs were saved, not hidden.
- Second run **43983553585** passed import and created 8,351 new 3D down-root objects but failed before GLB export: source script reused `root` for a Blender `Vector`, overwriting the output `pathlib.Path`. Failure logs preserved. Updated workflow installs NumPy; sculpt source now uses `fiber_root` explicitly.
- Third genuine end-to-end execution **43983720780** succeeded. Exported `research-evidence-run122-SILKDOWN-CONTINUOUS-SCULPT-NO_RELEASE/run122_continuous_sculpt_silkdown_organic_juvenile_ART_UNAPPROVED.glb` **6,039,668 bytes**, SHA256 **`2e6d6cbbad058e870618a5b4bc75153863bdfde46d0738511eece8b1532cc1d1`**. Blender re-imported exported GLB, measured **24 Blender mesh objects, 157,816 triangles**, and genuinely rendered **front, 45°, strict side, rear** at 520×520 in Cycles; 1040×1080 contact sheet archived. Scene/source asset has not been deployed.

## Browser and evidence integrity

The exported GLB was loaded **from disk** by Three.js GLTFLoader on headless Chromium WebGL2 using **SwiftShader software rendering**, on a real 1280×720 desktop viewport and a **390×844 simulated mobile viewport**. Both reported `loaded:true`, 38 glTF render mesh primitives (material splits; not 38 authored bird anatomy parts), 157,816 triangles, rendered frames and successful orbit camera movement, in-frustum before and after, WebGL error 0, page errors 0, app errors 0. Both screenshots preserved and inspected. The reused Run118 QA script mistakenly labels the model as `Run122 TRELLIS GLB` in JSON; **this is a stale test harness string**. The actual SHA-verified source in Run122 is the original **Blender Run121 organic loft GLB**, and the Run122 output is an **edited native Blender sculpt**, NOT a new neural TRELLIS generation.

All 16 SHA256SUMS-listed files were independently reverified from the actual archived Actions ZIP (18 entries including manifest and its verification log); exported GLB hash independently matches. No SVG/screenshot substituted for the GLB. Browser sizes, software rasterizer and screenshots do not certify genuine iOS/Android GPU frame time, touch, memory/thermal limits or battery life; no interactive animation or physical-phone validation performed.

## Actual visual review of four directions AND mobile screenshot: ART_REJECTED

Opened original v3 reference and real Run121 baseline, Run122 full four-angle Cycles contact, and Run122 simulated mobile WebGL screenshot. There is a *limited* improvement: top crown looks less bristly; surface reads smoother with small dense fibers; eye size/front relief slightly better, and the bark now has real depth. However, these changes are **nowhere near** the artist-quality rightmost nestling:

- Warm facial disc is still an extremely wide **flat, posterized mask/rigid concentric white-and-beige face patch**, with geometric eye-ring outlines. It is not the integrated densely feathered little heart of the reference. Eyes still read as two shiny toy beads and the face lacks true curved skeletal anatomy.
- 45°/strict side clearly reveal **projecting eye/beak**, thin facial relief, a tall long egg/pear profile instead of the compact naturally rounded fledgling, and essentially **absent short wings/shoulder feather tract**.
- White body is a largely featureless smooth **white snowball**. The fur is microscopic flecks in Cycles and broken/glittering point specks in software WebGL, not convincingly distributed soft multi-layer cream-white down; the rear remains an undifferentiated round surface, without biologically credible feather flow or wing structure.
- Naked spidery toes, without stout fuzzy shanks, perch on a clearly **faceted polygonal cut timber stump**, not the broad weathered bark-lipped hollow around the original chick. It has thickness but not real bark anatomy.
- Browser screenshot further exposes flat shading, aliased down and the overall toy-like silhouette; therefore **no art approval** even though actual GLB loads and rotates. User explicitly prohibited low-quality assembled/procedural birds being passed off as finished.
  
**Verdict ART_REJECTED.** The technical GLB is saved solely as traceable experiment evidence, not a sample to be presented/linked as successful. No push to website, no user-visible release.

## Source / rights / isolation / next real blocker

No external paid generator used; an image-to-3D fal route with a hard **$0** budget requested noninteractive user input and was not invoked/charged. Researched no-charge Tyto source alternatives; currently verifiable free entries are primarily an adult or low-poly barn owl, while anatomically closer juvenile assets have login/download or reuse-rights barriers; source listing does not prove global commercial redistributability. This Run122 geometry was generated locally via original source and Run121 code, but professional origin/global production license audit still not approved.

The actual 3D model's entire shape is a variant of the failed Run121 toy-like geometry. This trial demonstrates **material/groom fixes cannot substitute for competent organic bird skull, anatomical wing tracts, young owl feet and bark support**, so avoid repeated procedural loft polishing. Priority is acquiring a truly appropriate sculpt base with author-confirmed redistribution rights and independent real multiview, then blending layered down professionally; only after passing human art checks should actual physical phone hardware, rig and perf be acceptance-tested.

Evidence path: `owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run122-SILKDOWN-CONTINUOUS-SCULPT-NO_RELEASE/`. Every new file and dedicated workflow is in `owl-pet/3d-experiments/172-tyto-castanops/**` or `.github/workflows/owl-pet-172-run122-heart-silkdown-qa.yml`. The 251-species pipeline, original v3 plate, manifests, main branch, existing cat/WebGL prototype and deployment untouched. Nothing purchased. **NO_RELEASE** remains hard gate.
