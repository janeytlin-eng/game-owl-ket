# Run80 — #172 *Tyto castanops* v3: corrected lateral wing mask, recessed face, hollow shelf (**ART_REJECTED**)

**Date:** 2026-11-15 Asia/Shanghai. **No acceptable 3D pet, do not release.** No paid model or tool inference.

## Re-read before execution

Re-read main `owl-pet/AGENTS.md`, `README.md`, `prototype/index.html`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, and Run77, Run78, Run79 audits. Recovered Run79 GitHub Actions binary artifact and its prior verified Google Drive 27-file archive. Directly inspected original rightmost cream mesoptile crop against four-view real Run79 Blender renders. Its single frontal image does **not** validate hidden side/back anatomy, exact age or smartphone rendering.

## Actually executed — isolated, zero-extra-cost Blender 4.0.2

Created independent research branch [research/owl172-run80-structural-eye-wing-bark](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run80-structural-eye-wing-bark). On this branch only, committed reproducible [Run80 Blender model source](https://github.com/janeytlin-eng/game-owl-ket/blob/d1e0ee35e50f029c342cd337a20af8694fc09a6e/owl-pet/3d-experiments/172-tyto-castanops/tools/run80_blender_anatomy_correction.py) and [isolated CI workflow](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run80-structural-eye-wing-bark/.github/workflows/owl-pet-172-run80-anatomy.yml) plus its trigger. GitHub Actions [run 43703078665](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43703078665) **completed successfully** using stock Ubuntu Blender 4.0.2.

Real mesh changes vs Run79: repaired the actual anatomical modeling bug where the fold-mask excluded the visible -Y/front half of the bird; widened/chiseled a bilateral relief inside the remeshed **continuous body surface** without adding ellipsoid wings; reduced eye and orbit radii, made the beak shorter, hid spherical tarsal stumps under the belly, redesigned forward-projecting toes, replaced open-ended cylindrical perch with an actually meshed broad irregular hollow floor, and changed cream groom distributions to **15,500 curved guides / 46,500 fur triangles**. Two external paid tools were not called.

Blender completed four orthographic Cycles views (front, threequarter, strict side, back) and exported a **real 3,124,696-byte GLB**, SHA256 `a26b3e8d13136f4229d2e07963104bdf0eee9841f813a7333571ae5eac284c3e`. Blender export/reimport retained **31 geometry meshes / 97,180 final triangles**; script's earlier **92,860 polygons** are Blender pre-export and must not be confused with final GLB triangulation. Separate local trimesh parse also reported 31 geometries / 97,180 triangles. [CI artifact 14157133710](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43703078665/artifacts/14157133710) retains the real GLB, four actual renders, build/reimport logs and metrics, subject to default **14-day expiration**.

Also executed standalone Chromium WebGL2 SwiftShader rendering of the **actual exported GLB** in 390×600 simulated mobile viewport and 800×800 desktop viewport, four angles each: **8/8 real GL draws, glError 0, JS errors 0**, 31 meshes and 97,180 triangles. This is a custom light shader and **not** a standard glTF PBR viewer, physical phone GPU, rigging, motion, thermals or FPS acceptance.

## Visual quality gate — rejected

Compared all four real Cycles views and WebGL threequarter view with original owner crop and Run79 contact:
- Front and shoulder sculpt improve anatomical visibility but **look like jagged/crumpled shoulder pads**, not genuine short, down-buried young owl wings; the backside still resembles a two-lobe sphere with no convincing folded feather structure.
- Smaller eyes are less oversized, but remain artificial near-perfect circular black dots; heart facial ruff still appears as a detached hard plaque, especially at true profile; bill is too simplified.
- The feather material remains needles, hard flakes and sparkling strips rather than voluminous warm cream second-down. Browser rendering accentuates the failures.
- Hidden ankle-balls and broader ledge are minor improvements, but feet remain unnaturally short/unclear, and the shelf is a smooth slab rather than old eucalypt hollow. Side/back juvenile mass distribution is not evidenced by owner's one front view.
- Independent trimesh analysis revealed **inconsistent winding in the new experimental hollow-ledge mesh** even though the GLB rendered. Cannot claim release-grade geometry.
- Real phone GPU / physically correct glTF PBR materials / animation have not been tested.

**ART_REJECTED**. Neither the free Blender CI pass nor static browser pass is art acceptance. No character sample or deployment. Do not present as a visually adequate pet.

## Evidence and retention limitation

Prepared local complete **26-file** rejected-evidence ZIP containing 1 exported GLB, 4 Blender originals, Run79 comparison contact, owner crop, 8 browser screenshots, real QA source and reports, build log, strict quality decision and SHA256 manifest. ZIP size **6,755,814 bytes**, SHA256 `731f709a7b2b568bf6c9a15053e49439899cffe1b5e46e22b7180f500e425db5`; local CRC and **25/25 file SHA256** tests passed.

**Remote full ZIP retention is blocked this run:** an attempted Files Library create-folder and upload returned `AccessDeny`; Drive connector upload could not egress this locally generated ZIP or the downloaded GitHub artifact (`BLOCKED_FILE_REFERENCE`). Do **not** imply it was archived to Drive or indefinitely durable. The GitHub Actions proof artifact is actually remote but temporary (14 days); the fully reproducible Blender source, workflow, research history and this audit are durable GitHub files. Re-attempt a permitted remote archive in a later run, but do not overwrite user-owned or original production content.

Scope: only independent research branch and this GitHub main markdown audit changed. No changes to 251-species production, original concept plate, manifes​ts, existing cat WebGL prototype, vocabulary game, Sites deployment or paid services.
