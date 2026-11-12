# 棉棉 #172 — Run 04: down grooming / continuous sculpture / mobile LOD (2026-11-12)

## Provenance and isolation
- Verified `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, `research/reviews/172-tyto-castanops-v3-review.md`, Run02 and Run03 GitHub records before any new mesh generation.
- The **only** visual design target remains the **right** cream AGE-UNKNOWN MESOPTILE in `owl-pet/design/concepts/172-tyto-castanops-v3.png` (Git blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`), not either adult. Concept is design-approved with limitations, *not a real anatomical scan*. Age, flight ability and exact down-feather progression **remain unknown**.
- Did not touch the 251-species manifest, concepts, production workflow, species IDs or canonical source images. This is a separate rejected 3D experiment only.

## Work actually executed
- Four new **actual 3D** revisions, v09–v12, were generated locally with NumPy/SciPy/scikit-image SDF+marching-cubes, trimesh and VTK. Each exported to GLB, reimported with trimesh, measured, and rendered at **front / 3⁄4 / strict 90° side / rear**. A separate low-density mobile candidate v12_mobile also exported and reimported.
- Sculpt includes one watertight, smoothly fused head–neck–chest surface, integrated short buried winglets, heart-disc-shaped 3D raised rim and shallow recessed face (not 2D sprite), brow/cheek structure, paired eye socket anatomy, small horn bill, down-covered tarsi, individual 3D toes and hooked talons. Geometric down is approximately 27,000 short, curved, rooted feather ribbon primitives; 8,000 in mobile LOD.
- v11–v12 add a separately named **broad old-eucalypt hollow-lip context mesh**. This is a stage prop only, not evidence for observed nest contents. No rigging/behavior is claimed.
- VTK initially segfaulted because the cell array was given invalid offsets; fixed offsets to 0,3,6,... and successfully rendered all subsequent cameras; debugging evidence exists in local bundle.
- Actual headless Chromium/Playwright execution tried a simple `data:text/html` smoke test and returned `ERR_BLOCKED_BY_ADMINISTRATOR`. **No phone/WebGL runtime success is claimed**.

| revision | bytes | GLB reimported parts | triangles | SHA256 |
| --- | ---: | ---: | ---: | --- |
| v09 | 6,382,264 | 35 | 207,736 | `c7ff7c91eab779713cf232135e40e0b25cb50b308b0c861002d3096599e39ab9` |
| v10 | 5,326,200 | 29 | 170,568 | `3e206b7b4c7a65fb57333906b227edce811f0bbac96ae73228be6ed79e9053d2` |
| v11 | 5,506,036 | 30 | 179,478 | `dd4cd8b14eb1861fb344b67ef2aca7e538419e18f26077970844302c3a221d04` |
| v12 | 5,506,040 | 30 | 179,478 | `0148839b0378b35caa3e7d7c3d24e9adac06e5f4c2e63a19ecf3c1e22552c7e4` |
| v12_mobile | 2,041,780 | 30 | 75,470 | `9fa404e2fc4ba38426138361369e6371bdf9ac40f1c04c7f7e6d900b61a98338` |

### Four-view findings (not inferred from filenames)
- **v09:** continuous 3D sculpt and a feather silhouette are visible, but high-contrast short strips look like prickly fur/surface scratches, head atop a tubular torso, bald side wing pads; bad foot support.
- **v10:** smooth integration of short wing bulges and fuzzy tarsi, proportionally fuller lower torso, more visibly recessed mask; still looks like a round toy owl/potato rather than the photographed-style #172 mesoptile, sharp hard-edged facial basin, awkward talons.
- **v11:** new broad textured perch permits independent support visualization, but deeper facial sculpt masks the bill. At side/rear angles shoulders and the compact chick form are not convincing. Perch is visually branch-like rather than a natural hollow lip.
- **v12:** bill repaired and face tint moderated, feet repositioned relative to prop, same genuine side/back geometry. **Still fails**: face reads as sculpted porcelain rather than soft radial down, body is overly symmetrical/round, contour too artificial, original reference's heart shape and deep feathers insufficient, feet/perch occlude each other, no pose deformation or true rig.
- **v12_mobile:** 75,470 tris, ~2 MB real GLB gives measurable LOD reduction but performance on an actual mobile GPU unverified; LOD does not fix quality concerns.

## Gate and disposition
**FAIL / NO USER NOTIFICATION.** Core geometric and rendering pipeline works, and mobile-lean export is real, but still no acceptable stylized-realistic 3D pet sample comparable to canonical premium #172 v3. Do **not** ask user to review; do **not** merge into approved concepts or standard 251-species generation. Need image-conditioned sculpt/texture, less CG-toy face, better down atlas/shader rather than dense metal-like strands, anatomically grounded body–wing intersection and actual mobile WebGL validation.

External tools: fal Hunyuan 3D Pro was previously credit-blocked; no retries, spending or unapproved credit additions. Blender/bpy and offline pretrained image-to-3D weights unavailable in this runtime. Anatomy skill is a technical isometric SVG tool, not animal modelling.

## Binary/source archive limitation
All five GLBs, four camera renders for four sculpting revisions, Python source, metrics and failed/diagnostic logs were bundled at `/mnt/data/mianmian_172_3d_run04_rejected_experiments.zip` locally (20,238,464 bytes; SHA256 `5431f0bc39f53fffd4c0c6946fece8134fa499aecc5b80793022a15c088e5437`). User library upload attempted again but both create_folder and upload returned `AccessDeny: FileDrive_7a934266b8748191824cde4d0af03f29`. **Only this GitHub text log is durable remotely; the binary zip is not remotely archived.** No claim of successful remote model deploy.

Next trial: reference-conditioned three-quarter silhouette comparison; anatomy-constrained body proportions and bill/eye depth; down-shell alpha atlas with material roughness variation rather than independent plastic-like strips; natural seated toes on a correctly constructed concave bark lip; test GLB and browser/WebGL on an allowed host before any user-facing milestone.
