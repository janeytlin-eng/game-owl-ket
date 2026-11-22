# #172 *Tyto castanops* v3 RIGHTMOST juvenile — Run289 REAL adult native mesh LOD investigation and fail-closed image QA

**Date:** 2026-11-22 Asia/Shanghai. **Final: TRUE_NATIVE_ADULT_REFERENCE_GEOMETRIC_LOD_PASS / REAL_PBR_TEXTURE_BINARY_PRESERVED / 12_REAL_CAMERA_VIEWS_PASS / VISUAL_SOURCE_SIMILARITY_LIMITED / JUVENILE_ART_REJECTED / PHONE_WEBGL_UNTESTED / SOURCE_LICENSE_CHAIN_UNCLEARED / NO_RELEASE.**

## Protected scope and actual read-first

Re-read main's `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/STATUS.md`, actual `owl-pet/prototype/index.html` kitten WebGL prototype, and the Run288 independent no-release audit before coding. The target is the **rightmost cream-white fluffy juvenile in #172 Tyto castanops v3**, not an adult barn-owl specimen. Do not touch `main`, the original concept PNGs, the 251-species production system/manifests, the kitten prototype, or Sites deployment. All Run289 writes are restricted to this separate research branch, one standalone script, one standalone workflow, and this audit.

Technical donor input only: **adult** grey-brown taxidermy *Tyto alba* scanned by [Virtual Museums of Małopolska](https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc), original author page claims CC0. Actual binary read through a third-party mirror; mirror-to-original identity / downstream commercial provenance **NOT independently verified**, so research only. Source pinned SHA256 `6412ffd575360397bd90d391d3d4c23397f225945cdef3ec5727bfd91504cd44` at 43,225,496 bytes, 12 native meshes and 261,966 triangles. Run288 compacted bytes by 35% but barely touched triangles. New experiment tests true triangle-count reduction with actual textured geometry, not attempts to turn this wrong-age model into the target bird.

## Execution: genuine native 3D, independent reproducibility and failures

Use free Python / NumPy / Trimesh / VTK9.6 / Xvfb to read original GLB, preserve actual vertex positions, triangle indices, `TEXCOORD_0` and original PBR texture, and use actual VTK `QuadricDecimation` at 68% per mesh; re-export native GLB, re-import, check triangle counts and material, render **original and new GLB from six real 3D camera positions each** (12 images), enforce nonblank distinct screenshots and occupancy, log hashes. No 2D fake rotation, no SVG primitive assembly, no paid source.

The investigation caught **two genuine technical false positives**:

1. [Run289a Actions 45007124833](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45007124833) failed because strict UV validation rejected small legal negative UV coordinates near seams; corrected UV normalization to handle actual float UV tiling while still validating finiteness. Failure archived, not overwritten.
2. [Run289b Actions 45007268083](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45007268083) returned workflow success and 261,966 → 83,823 triangles but **human inspection of the six-angle PNG revealed a spiky explosion instead of an owl**. This is explicitly **false-positive QA, NOT a successful mesh**. Despite nonblank distinct renders and PBR attributes, geometry was corrupted, so the evidence remains a negative control. Independent ZIP verified; invalid output never promoted.
3. [Run289c Actions 45007592133](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45007592133) introduced spatial-bound and silhouette fail-closed guards and correctly failed: an invalid LOD bbox of `[[-1.062,-0.603,-1.083],[0.918,1.293,0.860]]` versus native source `[[-0.217,-0.001,-0.348],[0.215,0.563,0.112]]`. Pinning Python and VTK packages did not itself fix it. [Run289d 45007747412](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45007747412) copied VTK buffers explicitly, but still failed and established corruption was **already present before GLB export**, not a GLB export issue.
4. [Run289e 45007864832](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45007864832) added **per-submesh bounding-box protection** and preserved every original mesh when decimator output grew absurd spikes; the test correctly **failed** the ≥50% true triangle-removal gate because all 12 parts were initially corrupted. Fail-closed rather than announce success.
5. Root cause was reproduced **locally using the same pinned VTK9.6.2 / Trimesh4.11.1 / NumPy2.3.5 environment:** setting `t.SetName('UV0')` on the VTK texture-coordinate data array caused `vtkQuadricDecimation` to corrupt spatial vertices on every mesh, producing ~1-unit spikes. Running the otherwise identical code **without that custom name** preserved original mesh bounds in an independent local 12-mesh re-import; this was verified before the last remote retry. Unlike a file-extension or material fix, this explains why original glTF positions were correct but generated mesh geometry was nonsensical. Retained defensive bounding-box and occupancy gates in final code.
6. **[Final successful Run289f Actions 45007983178](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45007983178)** executed all steps including source SHA pin, 12-mesh genuine VTK decimation, post-export GLB readback, 12 camera renders, hash manifest and research archive. Zero outlier parts were retained; all parts genuinely decimated.

## Final independently checked measurements

| Metric | Original adult museum study reference | Final Run289f actual textured adult 3D LOD |
|---|---:|---:|
| Native GLB bytes | 43,225,496 | **11,166,456** (**-74.17%**) |
| True triangles | 261,966 | **83,823** (**-68.0023%**) |
| Mesh objects on readback | 12 | **12** |
| Actual UV and embedded PBR source texture | Yes | **Yes, all 12 meshes** |
| Source/LOD native spatial bounds | `[[-.21721,-.00121,-.34815],[.21529,.56283,.11197]]` | **Matches to float32 roundoff**, zero spatial explosions |
| Real separate 3D camera views | 6 | **6 more** |
| Actual browser / iOS / Android load and performance | Not tested | **Not tested** |

Run289f model SHA256 **`1ba0df06ef23bf66e95198007c075bb878b3c3bb321069edefe1da4561bfcce7`**. The final model is a *real* 12-part adult owl native mesh with UV/PBR data and substantial actual geometric decimation; unlike Run288, it is not merely byte compacting. It is neither a juvenile sculpt nor an animated/phone-validated electronic pet. Source original removed from final archive to avoid duplicating 43MB pinned input.

## Independent archive verification + human visual gate

[Run289f research-only artifact 14748965963](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45007983178/artifacts/14748965963), GitHub Actions final SUCCESS, generated 2026-11-22, expected expiration **2026-12-13** (not permanent consumer hosting).

Downloaded ZIP **10,772,903 bytes**, ZIP SHA256 `be42a0d513ab19d239a62139be213d232e87d26b9ae548df76b65962f3c71ef0`, matching GitHub's artifact digest. Independently checked **20/20 ZIP CRC entries**, **18/18 internal SHA256 entries**, and reopened its GLB by Trimesh, independently validating 12 meshes, 83,823 triangles, 238,431 vertices, 12 UV/PBR textured meshes, original spatial envelope, correct `glTF` binary magic and GLB SHA. All six original and six LOD images have distinct hashes and measurable owl silhouette; front occupancy **10.816% original vs 10.379% LOD**, close after true decimation.

**Manually opened BOTH six-angle contact sheets** (not just workflow logs): original shows believable grey-brown taxidermy adult on a museum perch; new LOD now preserves major body/wing/branch silhouettes and no longer explodes. However, the VTK preview colors in the LOD are visibly speckled and noisy compared with original, and small feather/fringe and facial details degrade. Original source PBR texture is preserved in native GLB binary; **this does NOT demonstrate full real-time shader/UV texture-fidelity approval** because previews sample texture to vertex colors using software VTK. True GLTFLoader/WebGL2 shader material quality and mesh LOD error on a physical phone are still not verified.

**Final art gate remains unequivocally `ART_REJECTED / NO_RELEASE`.** This is an adult **grey-brown Tyto alba**, not the reference rightmost *Tyto castanops* cream-white baby. The model has mature long wings, a long tapering body and tail, no soft dimensional juvenile down, no baby-sized heart-shaped face/eyes and no eucalyptus hollow or convincing baby feet. The temporary GLB and screenshots are strictly technical reference evidence, **not** a good-looking baby to show users. A successful LOD is not a character success. Real Android/iPhone GPU, interactive animation, FPS, memory, touch and thermal testing unperformed. Primary-to-mirror provenance not fully proven. **External paid spend $0**; a zero-budget external 3D-generation catalog attempt required interactive input and was not charged, so it is not claimed to be a model generated by that system.

## Next research route

Stop using adult donor as an artistic base for the chick; it now provides a reproducible, legitimate **UV/texture-aware real mesh LOD technical path**, with corrected VTK texture-coordinate naming and fail-closed geometry checks. For the actual pet first obtain/create a professionally credible, license-cleared **young Tyto castanops** sculpt with physically plausible rear/side silhouette and short wings, then groom soft cream-white directional down with exportable alpha cards/hair mesh, reimport GLB and manually judge **front/right/back/top** before browser work. Test any candidate on software Chromium GLTFLoader mobile viewport and then actual Android/iPhone. Keep research isolated, no concept-production modifications, no release until all gates actually pass.
