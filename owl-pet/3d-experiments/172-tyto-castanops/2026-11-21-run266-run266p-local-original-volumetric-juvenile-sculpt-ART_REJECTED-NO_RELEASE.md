# #172 Tyto castanops v3 — Run266 / 266p experimental original volumetric juvenile sculpt — ART_REJECTED / NO_RELEASE

**Date:** 2026-11-21 Asia/Shanghai. **Final:** TWO_TRUE_NATIVE_GLB_CREATED_LOCALLY / 12_REAL_VTK_SPATIAL_RENDERS / ART_REJECTED / CHROMIUM_WEBGL2_UNTESTED_FOR_THIS_MODEL / PHONE_UNTESTED / NO_RELEASE. This is a **negative-control research entry, not a usable or released Mianmian model**.

## Existing state checked first

Read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/STATUS.md`, and independently fetched the previous Run265b audit from commit `a6b62f2ff7b8c0eaf7adbfd77468688a5dd6b999`. Re-downloaded the actual previous [Run265b GitHub Actions artifact #14699737765](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44886196646/artifacts/14699737765), extracted its authentic rightmost v3 source image, masks, GLBs and actual camera images, and passed its existing `SHA256SUMS.txt` check. Opened the original photo-like juvenile reference and real five-angle TripoSR reconstruction. The prior mesh remains sideways / coarse-backed with bad feet and could not serve as a high-quality base.

## What was actually made, not planned

Performed an **independent, fully local, zero-paid-service** exploratory sculpt with NumPy, SciPy, scikit-image marching cubes, Trimesh, VTK and Pillow. Wrote and executed Python source code for a continuous infant head/body signed-distance surface (not reusing the failed TripoSR adult-like mesh), organically blended short wing lobes, a custom heart-shaped face surface with graduated relief, actual recessed eye/iris meshes, a tapered beak, curved three-digit foot structures and thousands of tapered down-fibre ribbon meshes. It is genuine 3D with spatially independent back/side surfaces: **not an SVG, flattened image, or 2D-rotation trick**. The body is a single watertight isosurface; detail still has primitive-looking anatomy and is not a professional organic production sculpt.

**Run266**: 5,324,632-byte binary GLB; SHA256 `4c5bfb04eea5ffcbab7e2bae3afd1670adb6a75038985adbe1b132749351fddd`; independently reimported: 23 meshes, 178,983 triangles; 23/23 glTF primitive meshes expose NORMAL and COLOR_0 attributes. Genuine VTK cameras rendered front, three-quarter, right, back, left and top (six distinct images).

Opened the six-view contact: conspicuously outward-projecting heart face, large button eyes, stiff pipe-like feet, stiff shards in the down, no anatomically believable folded wings or aged eucalyptus hollow. **ART_REJECTED**.

**Run266p** materially modified and *regenerated* the full 3D geometry: the facial relief and iris placement follow an analytically computed head/body front envelope, reducing detached face depth; iris/eyelid rings became smaller and warmer; outer ruff was softened; the feather coat was rebuilt from ~7,000 toward ~15,000 shorter and thinner attached fibres. Second native 6,571,052-byte binary GLB; SHA256 `75a3f0afabc2926dba094e5592d8720676baf1fce5a0cbf8ff9b76e1feccefa6`; 23 meshes, 200,229 actual triangles, 148,913 vertices; body watertight; all 23/23 glTF primitives contain normals and vertex colors. Rendered and **opened** six new real VTK spatial views; this is not just textual design work.

The second model is **still rejected**. Its front resembles a cartoon plush egg more than the cream-white natural juvenile in the reference. The eye/face relief is visibly imposed instead of naturally grown from the face disk; rear down remains a repetitive angular texture, with insufficient layered short wing detail. Foot tubes, perch contact and old eucalyptus hollow are unacceptable or missing. 200,229 triangles and 6.57MB without proper LOD and performance budgets cannot qualify as tested mobile WebGL.

## What was independently checked, and what failed to persist

Both GLB binaries were parsed as actual glTF v2, their raw header lengths and normal/vertex-color accessors checked, and reopened through Trimesh. Actual 12 spatial VTK camera PNGs were created, not reused still images. Produced Run266/266p reproducibility scripts, independent raw renders, contact sheets, machine reports, explicit `NO_RELEASE.flag`, SHA256SUMS and checksum verification. Packaged all into one 12MB local evidence ZIP:
`owl172_run266_run266p_REJECTED_NO_RELEASE_evidence.zip`
with **ZIP SHA256 `390439a747c7c4e1aa88cab4793a40b38c891c35c63f4a906b4dcd607c5bdbfc`**; `unzip -t` found no errors and SHA256 manifest check passed. This ZIP **exists only in this execution's container workspace**. An attempt to upload it and the audit to the persistent file Library returned `AccessDeny` for folder creation and both uploads. **Do not claim the GLB or ZIP are permanently archived in GitHub or Library**; this GitHub Markdown audit alone is durably saved, with exact checksums and scope.

**No physical iPhone/Android test and no Chromium Three.js test was performed on Run266/266p.** The software WebGL2 pass from previous Run265b is not transferable. No release, no demo, no replacement of any original art, no deployment. Actual original source art and all 251-species production files remain untouched. Free/offline experiment, incremental cost $0.

## Next gate

Need an actual professionally groomed, anatomically believable *juvenile-specific* organic mesh with natural integrated heart face, soft tapered short wings, eyes/eyelids and toes resting on a believable old eucalyptus tree hollow, followed by mobile-specific LOD, Chromium WebGL2 and real Android/iOS verification. Do not treat this procedural negative control as art acceptance.
