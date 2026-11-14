# Run65 — #172 Tyto castanops v3, conformal closed wing shells + contour down

**Date:** 2026-11-15 (Asia/Shanghai). **Final quality gate: ART_REJECTED. No release or user-facing 3D preview.**

## Live preflight and origin
Read main `owl-pet/README.md`, `owl-pet/AGENTS.md`, STATUS, existing `owl-pet/prototype/index.html` (a prior raymarched cat, not an owl), and Run64 independent rejection record. Extracted original slide 172 of the owner's 185-slide `Owl_Prototype_Gallery.pptx`, inspecting the **rightmost light cream fluffy young owl** as the front target. Exact age and side/back remain unverified. Run64 binary ZIP showed up in connected Drive folder but returned 404 on raw download; recovered, extracted and inspected **Run63 binary evidence ZIP** instead, using variant P as the isolated 3D baseline. Baseline P SHA256 `15f70a269602bfd9ecc1e6435a3714c2120db702ca008c70655162710dabb388`.

## Actual model production, QA and repair
- Wrote and executed an independent procedural **volumetric 3D** conforming closed-wing shell generator, not an SVG/alpha-card mesh. Two curved folded juvenile-wing shells; each **3,250 vertices, 6,496 triangles**, watertight positive volume and consistent winding. Initially found inverted wing normals; corrected and rebuilt, then re-imported real GLBs using trimesh.
- **U**: continuous 3D baseline body plus two solid wings and a 768-pixel original down/feather diffuse texture; **19 meshes, 82,756 triangles, 4,310,348 bytes**; SHA256 `d4f8738850661e9a9f0eaed141185e5ea3e7137a055a44f508566faf315431a1`.
- **V**: U plus **950 curved tapering true 3D down tubes** following crown, sides and back; **20 meshes, 111,256 triangles, 5,315,992 bytes**; SHA256 `a37ad821056674c3af2c9db94e5b9a9f9505fbe86f227bec61376998dd2de43f`. Body source vertex positions unchanged in both.
- Generated **8 actual VTK glTF2 imported front/three-quarter/strict-side/back images** and two composite view sheets; 16 real Chromium/ANGLE SwiftShader WebGL2 GLB rasterizations (U/V x four views x 390x600 emulated mobile viewport or 800x800 desktop). All **16/16 WebGL2 draws** returned glError 0 with no JS errors, both images loaded. Repaired custom browser QA fixture so that it samples each primitive's actual material-specific baseColorTexture rather than erroneously sharing image zero. This is a **desktop simulated viewport**, not real phone GPU/PBR performance, touch or animation validation.

## Visual gate: BOTH ART_REJECTED
U's closed wings appear **glued-on oval patches** rather than organic folded juvenile wings. V's 950 solid strands resemble **white needles/scratches**, not soft densely layered cream down. Both still have smooth pear-shaped bodies, front-projected photographic heart-shaped face, poorly structured side/back and unnatural claws/feet. VTK shading also shows unacceptable dark self-occlusion patches. Passing mesh winding checks and glError=0 **does not** make a presentable digital pet. No physical phone or standards-compliant PBR/animation validation.

## Free tooling and blocks
Blender/bpy unavailable locally; VTK/trimesh/Chromium available. Shell DNS blocked external CC0 owl/model assets; available listings unsuitable as verified juvenile mesh. Invoked fal image-to-3D discovery **with USD 0 inference budget**; service required interactive authorization, so no generation or paid request was sent. No purchases.

## Independently archived rejected research
- Full **44-entry** ZIP (43 internal SHA256 file checks + CRC), **16,170,781 bytes**; SHA256 **`dc5855c8bec00880be991a3229f8cd8e6aa20e8470f3875d96ac83700b3b0b02`**.
- [Run65 rejected binary GLB/source/reference/multiview/actual WebGL QA ZIP](https://drive.google.com/file/d/1O0ORFCPipUQzJ9W-reaZvh_lkycQR70i/view) was uploaded to the **independent** Google Drive `Owl172_3D_research_ART_REJECTED` folder, then **rematerialized from Drive** and verified byte-for-byte, ZIP CRC and internal hashes.
- [Run65 text QA and obstacles](https://drive.google.com/file/d/1_r9m9vENb4dkAStGn4-N70l5m1LrsH2Z/view) uploaded separately.
- **Not a successful sample**; links are *failed experiment audit artifacts*, not a usable pet or showcase.
- No changes to 251 species production code, root vocabulary game, concept art, manifests, owl-pet prototype, Sites or deployment.

Next hard gate: manually sculpted/anatomically integrated juvenile wings and layered soft down, credible three-dimensional face, feet, strict side/back design and **actual physical mobile WebGL/PBR performance**.