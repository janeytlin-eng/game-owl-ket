# #172 棉棉 3D Run07 — continuous organic sculpt / reference audit / CC0 alternative scout (2026-11-12)

## Mandatory rereads and boundaries

- Read `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, and archived Run04–Run06 reports before modeling.
- Independently loaded and **visually viewed the complete original 1536×1024 PNG** via GitHub repository read (base64-decoded image display). Exact source: `owl-pet/design/concepts/172-tyto-castanops-v3.png`, Git blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`. The **rightmost** bird is cream, broad-bodied, crouching, with small warm brown heart disc, dark eyes, cream bill, short down-buried wings and both feet resting on the exterior hollow lip. Left/central adult birds are **not** the geometry reference. Exact young age/flight ability unknown.
- All work isolated from 251-species manifests, prototype, design concepts and scheduled production.

## This run actually executed

- Checked current Python 3D stack: trimesh 4.11.1, vtk 9.6.2, NumPy 2.3.5, SciPy 1.17.0, scikit-image and PIL available. Blender/bpy absent. Python package installation failed due DNS. Existing fal credit block not retried.
- Verified actual **VTK software offscreen rendering works under Xvfb** with a small rendered test sphere; previous no-output VTK experience was not universally applicable. Chromium `--headless` with software SwiftShader flags **timed out**, with no successful WebGL2 test, so mobile/WebGL is still **unverified**.
- Built `v20` using marching cubes of a **single continuous smoothed skull–neck–body–wing volume**, not a separate head + torso toy construction; sampled a manually positioned heart outline and vertex-painted a subtle continuous facial-disc color/rim directly on the skull surface. Separate actual 3D horn bill, small eyes, two downy leg segments, articulated toe/talon tubes and 7,100 short curved down-fiber ribbons. Exported GLB, reopened and counted actual triangles. Four actual VTK renders + contact sheet visually checked.
- Built `v21` by substantially reducing sculpt micro-noise and down-ribbon dimensions, softening eye socket and brown heart rim, reducing visible eye size, shortening toes and reducing leg pom-poms; added subtle short-wing coloration. Exported GLB, reopened and rendered all four views.
- **v20 visual failure:** severe parallel quilt/knit-like ripples, hard-mask effect, bead eyes, overly mechanical egg-shaped leg pads and unsupported feet, large featureless capsule from side and behind.
- **v21 visual failure after review of the contact sheet:** smoother but nearly bald toy/potato, heart outline still reads as painted logo rather than feather anatomy, nose is a simplistic extrusion, down still reads as sparse surface specks, feet remain unsupported and disproportionate; strict side and back show a single featureless upright oval with almost no anatomical wing/shoulder/neck transition. The original reference has broad soft down, organic color/contour shading and a much richer developed face. **FAIL / NOT USER-SHOWABLE / NOT PROMOTED.**
- Crucial result: **one-piece SDF + more/fewer geometric fibers is not enough**. Continuing this line will not bridge the gap to premium reference-conditioned animal sculpt without improved base geometry and actual groomed/alpha hair materials. Use the v20/v21 renders as negative QA evidence, not a model showcase.

| revision | GLB bytes | triangles, after re-import | meshes | SHA256 |
| --- | ---: | ---: | ---: | --- |
| v20 | 6,367,044 | 241,116 | 23 | `ed014f728a96b510731f6031c9184a5c4c1b5c866f2243ffc736bfd065aadaec` |
| v21 | 5,748,500 | 219,372 | 23 | `04cc178c3c4bf73f98bb96a7bf0e399cc074636d287f0ed9da2679ccafb0432a` |

## Concrete no-cost alternative leads identified, not yet adopted

- **CC0 digitized adult barn owl museum specimen**, Virtual Museums of Małopolska, Sketchfab `0e65de5934db4f0eae02835ba7227dcc`, ~262k triangles: https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc . Potentially useful anatomical topology & wing/foot reference, **not** a juvenile mesoptile mesh or evidence for age; requires actual permission/asset verification at download stage.
- **CC0 Innerscene owl GLB**, ~19.7 MB, claimed freely licensed and available at https://www.innerscene.com/tools/library/3d-parts/owl-d696472a . A download click resolved to `https://files.innerscene.com/library/owl-d696472a/8ecea479b865c7141318/owl.glb`, but container tool download and direct page fetch did **not** yield bytes; do not claim model inspected or imported.
- **CC0 rigged game-pet owl** in a free sample pack, https://vuena.itch.io/blocky-pets-free , has a mobile LOD and animations; the listed design is a *designer toy* so unlikely to meet species-realistic art gate. Not yet downloaded.
- The license and downloadability of any external asset must be checked and recorded before modifying and re-distributing it. None is incorporated into v20/v21.

## Actual files, QA evidence and archive status

- Local sources: `/mnt/data/mianmian_run07.py`, `/mnt/data/mianmian_run07_v21.py`, plus reproducible VTK camera renderer scripts and logs.
- Outputs: two reimported real GLBs, 8 individual VTK PNGs, 2 contact sheets, JSON metrics.
- Verified local zip archive: `/mnt/data/mianmian_172_run07_rejected_bundle.zip`; **11,997,888 bytes**, 22 files, ZIP integrity pass, SHA256 `d313ddf97201075dc81ab107ff0ebbef681479dc3f9af0d56d8ef6edc4b2a816`.
- Explicit persistent Library upload to `/Owl Pet 3D Experiments/mianmian_172_run07_rejected_bundle.zip` failed with **AccessDeny FileDrive_7a934266b8748191824cde4d0af03f29**. Thus only this Markdown report is durable in GitHub; the local bundle is *not* remotely archived. No deployment or user-visible playable sample exists.
- The original #172 v3 PNG, 251-species production manifest, pipeline and preexisting prototype were not edited. No external credits or payments used.

## Decision for next work

Do **not** simply continue SDF tweaking or pushing card density; seek a real, inspectable CC0 anatomical base and transform to a compact down-covered chick with genuinely modeled shoulders, asymmetric tucked wings, heart-disc transition, feather shader/groom and grounded toes. If possible use actual Blender sculpt and a multiview alignment gate. Obtain real browser WebGL validation and durable binary archive before quality approval. **Hold user notification until there is an actually good, accessible sample.**
