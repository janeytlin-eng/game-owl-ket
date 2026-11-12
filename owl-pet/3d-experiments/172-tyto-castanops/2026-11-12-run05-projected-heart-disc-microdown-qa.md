# #172 棉棉 Run05 — projected heart-disc / microdown / mobile LOD (2026-11-12)

## Source and boundaries
- Before sculpting, directly re-read `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md` and Run02–Run04 failed 3D experiments.
- Reference independently fetched from GitHub main through repository connector as complete PNG; **rightmost cream "AGE-UNKNOWN MESOPTILE"** in `design/concepts/172-tyto-castanops-v3.png`, Git blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`. Reference has three birds; left/centre adults were not used to derive young proportions.
- Preserve scientific unknowns (exact age, flight capability, feather chronology). No alterations to 251-species manifest, concepts, workflows or canonical source imagery.
- Previous records establish v03–v12 had real GLBs but toy facial disc / needle down and unverified mobile runtime; this run makes **new v13–v16+mobile**, not reinterpretation of old renders.

## Real work performed
- Directly generated 5 **true polyhedral 3D GLBs** using Python NumPy/SciPy/skimage marching cubes, trimesh and VTK offscreen render; each exported and **reimported** successfully. No image plane / SVG used as finished character.
- v13: asymmetric fused skull / neck / breast / short buried wings from volumetric SDF; independently sculpted heart contour and face basin; tessellated eyes, small horn bill, curled toes/talons; anisotropic feather-cluster cards; eucalyptus branch context. Four camera renders.
- v14: compressed height to better match chick's crouching proportions, shortened spiky feather clusters, reduced protruding eyes, added more down; four camera renders.
- v15: **new contribution**: cKDTree-project heart-mask vertices to the *actual curved body/skull surface* (mask depth conforms to skull instead of a front-plane plaque), reproject fluffy rim, and sample an additional ~11k radial 3D fine facial down tufts. Eye sockets moved into this surface instead of floating in front. Four camera renders.
- v16: reduced artificial periodic geometry striations, softened lighting/color contrast, removed separate white ankle pom-poms and smoothed/reshaped support wood. Four camera renders.
- v16_mobile: separate genuine low-poly GLB (lower grid and fewer feather ribbons), re-imported successfully. Mobile file alone does **not** prove phone WebGL runtime, and its VTK preview render was interrupted by execution timeout.
- Source `/mnt/data/mianmian_run05.py` is the final v16/v16_mobile generator, NOT a precise reconstruction of earlier v13–v15 scripts, whose edits are preserved as output GLBs and renders in the bundle.

| Model | GLB bytes | Reimported meshes | Triangles | SHA256 |
| --- | ---: | ---: | ---: | --- |
| v13 | 6030380 | 32 | 228657 | `2306981ebd54a6768ebb02795c9a74a6d109043d2e597518d144acbb18647988` |
| v14 | 6114012 | 32 | 256518 | `1962fad12f2750d6a1ecfa831920fb0713223c1cb3d56e316f840f36753ec1da` |
| v15 | 6872872 | 33 | 276123 | `2e93218737daae3391ab33d573d55166fb98f7d627a54d8d3419e5c894265ba8` |
| v16 | 8006408 | 31 | 307132 | `505bbcb86fa7f5bc175c315f7a6adcd6970519187d1fffc5ead3f28e3d5bce2d` |
| v16_mobile | 2850716 | 31 | 128571 | `3387deea800fbea8bbab6e2485b29f72a129f6c05bd59a42c71729268ddf8f8c` |

## Independent visual review
- v13 is an unacceptable hedgehog-like thin owl: overly long sharp white strokes, bulging doll eyes and cylindrical trunk.
- v14 has somewhat improved crouch and a softer silhouette but remains a symmetrically oval artificial animal; the rimmed face and ankle pom-poms are conspicuously toy-like.
- v15 integrates the face curvature and makes 3D facial microdown clearly visible, with smaller embedded eyes, but its face still reads like a geometric theatrical mask, the body is too plain, and individual down shards give a **salt-and-pepper styrofoam** texture, not dense soft cream mesoptile.
- v16 color/lighting are calmer and bark support more naturally rounded. **Still FAIL**: stiff circular baby proportions, 2D-looking eye arrangements despite 3D geometry, not enough believable shoulder/wing transitions, feet/ledge awkward; profile/back resemble one fuzzy oval, not species-grade anatomy. Mobile tris 128k and size 2.85MB, but real device frame rate, overdraw, double-sided card rendering and GLB shader appearance all unverified.
- No anatomical animation/rig: would need a proper connected head/neck structure. No actual mobile browser / WebGL success; Chromium smoke run failed/timed out.
- Therefore **REJECT / DO NOT NOTIFY USER / NOT A QUALITY-PASSED SAMPLE**. Reference v3 and canonical production assets unchanged.

## Artifacts and archive honesty
- Full local rejected-experiment bundle: `/mnt/data/mianmian_172_run05_rejected_experiments.zip` (23,490,511 bytes, SHA256 `920c69429b7d5e59b75f924d189475dafeb9258d8d6064ad577ae18a81f35c36`); includes all 5 GLBs, 4-view VTK renders of v13–v16, contact sheets, final generator source, and validation metrics.
- Persistent File Library upload was **attempted** at `/Owl Pet 3D Experiments/mianmian_172_run05_rejected_experiments.zip`; again rejected as `AccessDeny: FileDrive_7a934266b8748191824cde4d0af03f29`. **Only this markdown record is durably GitHub archived, binaries remain local to this run and are not remotely guaranteed.** Do not call this a deployed sample.
- No fal usage, payment or credit retries; no Blender was available. Anatomy Skill is not a 3D animal modeling tool.

## Next test direction
Stop scaling procedural cards indefinitely; prioritize real feather texture atlas with alpha/roughness, image-conditioned multiview geometry with legally accessible offline weights, and organic continuous skull/cheek/breast transition. Create a strict face-disc depth and grounded toes landmark QA set. Then obtain a genuine mobile WebGL test before approval. Hold user notification until premium visual gate is passed.
