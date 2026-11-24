# Run339 — facial disc relief A/B — NO_RELEASE
2026-11-24. TWO_NATIVE_GLB_REIMPORTED / SIX_VTK_VIEWS / ART_REJECTED / WEBGL_UNTESTED / NO_RELEASE.

Read main owl-pet/AGENTS.md, README.md, STATUS.md, prototype/index.html, #172 v3 review, and Run338 record/source at 1666cf9cc1f5b86b85be2d91f87ca3b928193bca. GitHub connector retrieved the actual v3 PNG (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b) and displayed it for visual inspection. Raw host DNS failed in local container; connector worked. Reference right bird has a soft rounded crown, tan-edged developed heart mask, dark glossy eyes with dark feathered sockets, narrow pale bill, cream mesoptile, short wings buried in down. Exact age and side/back anatomy not established.

## Actual local experiment
Following Run338 rigid facial rim and artificial eye seating, isolated a curved facial-disc study, not a complete juvenile and not a release candidate. Local free Python, NumPy, SciPy, Trimesh, VTK, Pillow. Blender executable and bpy unavailable; no paid calls. Periodic spline outline from visually estimated front proportions; continuous surface with paired orbital depressions and narrow midline ridge. A has raised 6 mm rim; B reduces rim relief to 1.8 mm, adds nonperiodic eye-centered angular feather-like relief (0.45 mm amplitude coefficient), warmer/darker orbital shading and rim pigment. Same sampling and topology; simultaneous changes, not causal isolation. Open perimeter and no bill/head integration by design. Eyeballs/pupils separate and only placeholders.

Two actual native GLBs exported and reimported with Trimesh; six offscreen VTK renderings at 420x420, 0/35/70 degrees; visually inspected full 1260x840 montage. Both 133760 triangles.
A 2594300 bytes SHA256 b8f52bdce9ff406401e7c909ea0c4c822fc76c16437fa60d18aabef4883a3134.
B 2594296 bytes SHA256 0df80acc1cad3d8b4e4124902aaba85c0639f95009936dfa809604694c9046aa.
Full montage SHA256 2c02b789a8d6fee480d1c2731de3dfd1a9544a6d86121be52997148a735012e6.

A resembles a smooth molded mask with a rigid rim. B does soften rim, introduces discernible surface direction at oblique views, but appearance still embossed plastic/stone rather than fine facial feathers; eyes look like flat buttons, color/lighting too pale, outline too symmetric, incomplete bill/cheeks and no skull integration. Both ART_REJECTED. Excessive 133k triangles for just face; no GLB material/performance or phone validation. Do not infer complete side/back anatomy or consider this a usable pet.

## Evidence
- [Executed A/B source](run339-local/face.py.gz.b64), commit 7173d824506deb33ff6a6f67488f41edb767ed67, exact readback; git blob be93c528fd1cd181c4550ac9febdf530924a71af matches local encoded file (3260 chars). Decode base64 then gunzip. Uncompressed script SHA256 12f5c5ddb05d6ee88590337c227af41e4d8ae26d5af4de57940c257e942cf40e.
- [Actual render audit thumbnail](run339-local/audit.jpg.b64), commit 8cba0e13af51b31f1d7ac1cbf93e8b4fdfae876f; exact readback, git blob 405808b5439ebf5846f5bca453da0d034bd54ba1 matches local encoded bytes. Decode base64; 150x100 grayscale JPEG SHA256 8e56591103f9c87fbf413417d5dde0f7e4dfceafa1df284e2e48e22232ddec45. A top, B bottom. Full-size renders and GLBs generated locally but not uploaded.
- Next avoid further high-poly procedural relief mask; prefer integrated skull/face topology, recessed continuous glossy eye surface with realistic eyelid geometry, bill and facial feather direction in textures/normal maps, and stronger reference-matched lighting. A real artist-quality base sculpt remains bottleneck.

Zero extra spend. Independent research branch from Run338. No edits to main, species production, source concept, existing prototype or deployment. No release.
