# 棉棉 #172 — independent 3D sculpting Run 03 (2026-11-12)

## Boundaries / repository reconfirmation
- Re-read `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, previous Run01 and Run02 quality gates.
- Canonical reference: `owl-pet/design/concepts/172-tyto-castanops-v3.png`, immutable Git blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`. The **right-hand, cream, age-unknown mesoptile** only; no assertions about exact age, flight, adult remiges or tail.
- Read original 1536×1024 reference image through GitHub; previous accepted *concept* is not a finished 3D model.
- This experiment is independent: **do not modify 251-species manifest, standard concept plates, production workflow or prototype**.

## Real experiments executed in this run
Environment: Python NumPy + SciPy + scikit-image + trimesh + VTK offscreen rendering + Pillow. Blender/bpy absent; no additional paid model calls. Three fresh 3D meshes were produced, exported as GLB, **re-imported**, and physically rendered at FRONT / 35° / 90° SIDE / REAR.

| revision | GLB bytes | GLB reloaded parts | triangles | SHA256 |
| --- | ---: | ---: | ---: | --- |
| v06 | 5,360,020 | 39 | 277,440 | `560f8aed537d7e734097687a51d97262e15537016530261122bfd08f6b5cc016` |
| v07 | 5,528,512 | 26 | 252,532 | `b3fe07ec89e99394f3acb38a0d90ec0cdc0850665a8fb5c181f05c0109be449b` |
| v08 | 5,501,152 | 26 | 251,772 | `8388b2da3b9e8dd14eb46af715b5dea1d8e82a2be210b4a9fc2cb13ac193419f` |

- **v06:** continuous SDF head/torso, separate heart relief, black eyes, ivory bill, wings, claws and tens of thousands of down triangles; **failed**: applied mask/card effect at profile, cheek bead artifacts, large oval paddle wings and tall legs.
- **v07:** removed standalone heart plate; assigned a signed-distance anatomical heart region directly to the 3D skull, deformed the physical face, embedded smaller wings, removed cheek beads, reduced and densified down ribbons; **failed**: disc still too planar in strict profile, coarse toy expression, plastic/scratched fur.
- **v08:** sculpted curved 3D mask around skull from front to sides, relocated eyes/beak, groomed fringe around deformed surface; **failed**: visual continuity improved but still lacks realistic fluffy feather depth, natural Tyto cheek volumes, proper crouched support and aesthetically convincing side/back anatomy.

Each revision produced four real VTK renders, a contact sheet, metrics JSON, Python source and full GLB. Local archive: `/mnt/data/mianmian_172_3d_run03_rejected_experiments.zip`, 14MB compressed, SHA256 `b1359043ec7d6e3eb82b643249898ee2fa83fc2a949c7ded801b3b3792f8ef2f`. This is a **rejected exploration bundle**, not a production asset.

## Actual QA gate: FAIL — do not notify
Reviewed front, three-quarter, side, rear render. v08 is less obviously composed of pasted parts than v06, but it still resembles a textured 3D oval with simplified facial geometry, not the lush cream mesoptile of v3. Rear shape and short wing not anatomically persuasive, front eye/beak relations too stylized, foot pose and perch support not resolved. Feather triangles read as surface scratches rather than soft second down. Not enough artistic quality. No mobile browser WebGL success verification; not rigged. Triangle count / feather overdraw also require mobile LOD/atlas solution.

## Archival limitation and next experiment
Tried to upload the actual zip into persistent File Library under `/Owl Pet 3D Experiments/`; both folder creation and zip upload returned `AccessDeny`, matching Run02. Therefore **only this text record is GitHub-archived; the binaries are locally available but not remotely deposited**. Do not claim remote binary or mobile runtime validation. Propose next approach: textured down atlas on feather cards, more distinct rounded skull and cheek shapes, less uniform oval torso, crouched supported feet and a separate neck rig. If an image-conditioned free model with actual accessible weights becomes available, compare it with the procedural route. Fal account had no balance before, no retry and no paid generation.

Status: **FAIL / user review held**, canonical owl-pet production files untouched.
