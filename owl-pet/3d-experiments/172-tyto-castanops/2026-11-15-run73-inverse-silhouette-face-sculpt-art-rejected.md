# Run73 — #172 *Tyto castanops* v3: inverse-silhouette continuous-body sculpt and smooth heart-disc ablation (**ART_REJECTED**)

**Execution:** 2026-11-15 Asia/Shanghai. Isolated zero-spend research, not an approved character. No modification of the 251-species production process, image manifests, owner concept images, existing WebGL pet prototype, game root or deployment.

## Current main / provenance
Re-read the GitHub main owl-pet README, AGENTS, STATUS, prototype code, the #172 v3 species science/design boundary, and earlier Run70–Run72 failed audit records. The owner reference is a **frontal age-unknown cream mesoptile**, not validated side/back photos. Recovered Run72 actual ZIP from the dedicated research folder and checked 19,457,865 bytes / SHA256 `d20c8b4a2c798e107e425b820169ee5b084e535af0a17a0eaef4e9d2594b2aec`. Used its actual rightmost cream chick reference crop and source **Run72 E** continuous-mesh GLB SHA256 `24e9fae8c34a3e57de1c6ee476cd77dc1d73249eec1e73438c27acd3b58c6881`.

## Three true 3D variants actually made
Wrote and executed a new `build_run73.py`, then corrected it in `build_run73_R.py`. Measured source mesh width at actual Z slices; applied a shape-profile deformation to the genuine UV-mapped, closed 59,520-triangle nonparametric body, synchronizing UV-seam duplicates and repositioning inset eye corneas. The profile is an **artist-estimated** interpretation of the concept's frontal silhouette, not hidden-angle scientific ground truth. No 2D/SVG substitute was generated.

- P: 70% frontal silhouette redistribution, softer shoulders/crown, fuller low torso.
- Q: 100% redistribution with physical heart-face relief, recessed orbital pads, nasal bridge and tiny continuous-surface microdown. Visual inspection found jagged stepped/creased face rim.
- R: actually corrected Q using smooth logistic implicit heart mask, reducing overly sharp ridges and microdisplacement. Face edge is less harsh but still not professional art.

All three were exported and **reimported as actual GLB files**. P/Q/R: **21 meshes and 80,644 triangles each**, **3,845,524 bytes each** (includes baseline bark staging, prior toes and corneas). All three underlying body meshes pass geometric-UV-welded closedness, winding consistency, and positive volume: 0.506903 / 0.518992 / 0.515992 units³; maximum body vertex changes from parent 0.03370 / 0.05676 / 0.04247 units. GLB SHA256:
- P `7e28f29b97079657f4c42e989bdaf7227763d9cb4b44c5fb8b60fa612977b3e5`
- Q `e1ce1db3e34a7e447b7f1856e089456419ddff97f3fea7ec85a191c9d2000b6c`
- R `597457e8ef9bce199b27c5b026ba6bbec4eb6afa19399bad4f4eefb343201758`

## Actual rendering + browser QA
Rendered **16 VTK glTF importer frames** (Run72 E baseline + P/Q/R, each front/three-quarter/strict side/back), all 21 actor meshes loaded, with multi-view sheets and comparison images. Relative to baseline in the fixed frontal view, mean absolute RGB difference was P **3.9308/255**, Q **5.6888/255**, R **5.4150/255**; 512px image silhouette width at row 180 changed from 241px baseline to 258/266/266px. These prove the mesh was altered, not visual similarity to the real bird.

Executed **24 actual Chromium WebGL2 draws**: P/Q/R × simulated 390×600 portrait and 800×800 desktop × four angles. All 24 loaded one embedded texture and returned WebGL error 0 / no page exception. Rendering was under **desktop SwiftShader/Xvfb**, not a smartphone or full glTF PBR animation/FPS/touch/power validation.

## Final art gate — **ART_REJECTED**
Actual front, 3/4, side, back, and a browser portrait frame were inspected. P changes the silhouette a little; Q adds harsh physical face-border artifacts; R softens that artifact. **All remain a smooth, bag-shaped volume bearing a frontal photographic heart-mask texture**, not a cream-white fluffy young *Tyto*. Juvenile rounded head-neck anatomy and down-buried wings, properly formed and supported feet, feather volume, and independently plausible side/back remain inadequate. Neither the rendering smoke test nor numeric silhouette changes satisfy the user's quality threshold. **Do not publish, demo, deploy, or send a success notification.**

## Separate durable failed-evidence archive
[Run73 79-entry full research ZIP (Google Drive)](https://drive.google.com/file/d/1LSoZQNC2j3DX7tKHCLucRcdLxcNRQgaX/view), **18,504,924 bytes**, ZIP SHA256 `0b6b9a0b5d92a83498619886970426849fa1f0697fcb02242e0db184dd6e443f`. Contains three independently openable true GLBs, Run72 parent GLB, owner concept crop, both build programs, VTK scripts, WebGL test source, 16 VTK frames, 24 Chromium screenshots, JSON QA, render logs, four-view sheets and an internal SHA256 manifest. After upload into the existing `Owl172_3D_research_ART_REJECTED` Google Drive folder, a **fresh remote file was materialized and compared byte-by-byte**. Exact length/hash matched, ZIP CRC passed, and **78/78 internal SHA256 hashes** passed. This proves provenance/reproducibility, **not acceptable art**.

## $0 tool exploration / decision
Real local available tools: `trimesh`, SciPy/Numpy, VTK and Chromium SwiftShader. No local `bpy`/Blender or CUDA GPU; third-party premium generation inference wasn't invoked or paid. Inspected public alternative assets (CC0 adult Great Horned Owl and classic rigged adult owl) and real juvenile *T. castanops* anatomical context; these are not equivalent to the requested infant character and were not imported. Scientific caveat: the actual photo of a younger chick has a less developed face disc than the owner age-unknown mesoptile design. Free professionally groomed *juvenile* multi-angle sculpt/rig and real mobile runtime remain the core unsatisfied prerequisites. Further tiny local warps are not a route to premium quality.

**Status:** research archived; **ART_REJECTED**; zero charges; original prototype and 251-species production pipeline untouched.
