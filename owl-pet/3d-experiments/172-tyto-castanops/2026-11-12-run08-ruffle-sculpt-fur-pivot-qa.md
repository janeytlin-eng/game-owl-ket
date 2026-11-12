# #172 棉棉3D Run08 — volumetric cranial rim, feather profile A/B, actual raster QA (2026-11-12)

## Scope / canonical assets checked

- Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, and Run01, Run06 and Run07 experiment records. Existing verified concept: `owl-pet/design/concepts/172-tyto-castanops-v3.png` (Git blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`), **rightmost** cream age-unknown mesoptile; not the adult birds. The exact developmental age, wing state and inner nest remain unknown; source science=false.
- No 251-species manifests, concept image, review, existing prototype, or ongoing production workflows were changed.

## Actual local experiments and independent inspection

- Confirmed no installed Blender/bpy, no CUDA, and no usable container internet DNS for external assets. Python `trimesh`, `scikit-image`, `SciPy`, `VTK`, `PIL`, `xvfb-run` are available.
- Built **v22**, a real polygonal 3D GLB with a single integrated smooth-min organic cranial/body volume, an **implicit geometric heart-region rim** instead of a planar sign on the front, vertex-pigmented facial tissue, tapered 3-D curved down clumps, short integrated wings, independent curved bill/eyes, toes and a separate eucalyptus outer hollow lip. Actual GLB write and `trimesh` re-import succeeded; VTK/Xvfb rendered four genuine camera viewpoints (front / three-quarter / strict-side / rear). Source: ephemeral `mianmian_run08/organic_owl_v22.py`.
- **v22 QA FAIL:** broad egg silhouette and shield-like face despite integrated geometry, synthetic lawn-mowed/card-edge down, expressionless bead eyes, visually unsupported feet, side/back still lack anatomically convincing shoulders. This is materially inferior to the approved *illustration* and is not fit to present as a 3D pet.
- Built **v23** as an actual A/B revision, reducing the solid-face ridge and dark rim, lowering/widening the crouching torso, increasing 3D fiber extent, adjusting directional grooming and cream coloration. Export/reload and the same independent four-angle VTK/Xvfb QA completed. Source: ephemeral `mianmian_run08/organic_owl_v23.py`.
- **v23 QA FAIL:** surface coating becomes slightly more downy but looks like stiff straw, and the crown makes an unnatural flat-topped tuft. Facial mask remains toy-hard; body remains a pear-like lump. Not approved for user display or promotion.
- Independent on-machine QA view: complete `four_views.png` sheets were actually opened and visually examined, not inferred from mesh validity or triangle count.

| Version | Reimported triangles | Meshes | GLB bytes | SHA256 | User gate |
|---|---:|---:|---:|---|---|
| v22 | 176,075 | 18 | 4,004,872 | `e90ce42d77979cb3dae28bec83b84f5d32649bbd15ec3b49517f5aaad7a0a2f8` | FAIL |
| v23 | 195,800 | 18 | 4,704,632 | `b74b3cd68f6d2ccf65c7ce005728e26018f5139dd23d6b348d69ad642506998b` | FAIL |

## Free alternative asset and tool research actually performed

- Re-checked **CC0 digitized adult barn owl** (museum scan): https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc . Still not downloaded, and not a mesoptile or evidence for its exact shape.
- New stronger **professionally feathered, rigged CC0 Blender owl** candidate, 31.7MB (Blender 2.6x) by gholm and collaborators: https://blendswap.com/blend/7951 . Public listing says feathers/groom/rig/animation; download endpoint https://blendswap.com/blend/7951/download explicitly requires **sign-in**. Discussion reports possible incompatibility in Blender 2.9, so not yet an importable reference. License CC0 per listing, but no asset bytes obtained.
- Examined a concrete public GitHub GLB binary without guessing using the connector: `Inefy/project-rat/assets/models/barn_owl.glb`, 440,888 actual bytes, glTF 2.0 header and JSON parsed, 1 mesh/3 primitives, material names NIGHTMARE_Paint, NIGHTMARE_Skin, NIGHTMARE_Eye; project MIT license and original authored meshes per its `ASSETS.md`. Its deliberately MS-Paint/horror visual design has human-style features, so **REJECT as a reference-conditioned realistic juvenile base**. Confirming a GLB can be inspected via the GitHub connector does **not** mean it was downloaded into the Python runtime or adopted. Source: https://github.com/Inefy/project-rat/blob/main/assets/models/barn_owl.glb .
- Innerscene CC0 owl https://www.innerscene.com/tools/library/3d-parts/owl-d696472a remains unavailable as local bytes; cannot claim converted.
- No fal/paid generation, payment, or unauthorized asset redistribution.

## Browser/mobile test & archive caveats

- Attempted actual Chromium/Playwright WebGL2 smoke under 3 software SwiftShader configurations with file:// URL; all returned `net::ERR_BLOCKED_BY_ADMINISTRATOR`. A separate data: test also returned `net::ERR_BLOCKED_BY_ADMINISTRATOR`. These are environment-policy blocks, not tests showing model compatibility. **Real mobile WebGL behavior unverified.**
- Local bundle `/mnt/data/mianmian_172_run08_rejected_bundle.zip` contains v22/v23 GLBs, exact executed sources, metrics, 8 individual VTK PNG renders, 2 four-view contact sheets and browser tests: **20 entries**, 9,053,629 bytes, ZIP integrity pass, SHA256 `1b62e6cf3e9748713cc0ba54c4e4c191bdec96423b0774b725d1e1e19e04c5b1`.
- An explicit attempt to upload the bundle to Library root using the file upload action failed again with `AccessDeny: id=FileDrive_7a934266b8748191824cde4d0af03f29`. The local bundle is ephemeral and **not remotely archived**; do not claim this Markdown is a complete assets archive. This GitHub report is the only persistent evidence for Run08 unless binaries are uploaded later.

## Decision

Do **not** iterate the same organic SDF/geometry fur path indefinitely: 23 attempts spanning 8 runs have confirmed a hard visual-quality ceiling without image-conditioned zoological anatomy and physically plausible groom. The successful novelty this run is a structured A/B of integrated heart rim and feather profile, with objective reimport + actual four-angle rejection. Next run should focus on acquiring and actually opening a license-cleared real sculpt/feathered owl, ideally transferring to contemporary Blender; then remodel it towards an age-unknown Tyto nestling and run authentic mobile WebGL. If tool access remains blocked, do *not* present a broken model as a cute pet. Only notify user with a real openable, visually credible sample.
