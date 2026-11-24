# Run340 — integrated skull/eye seating A/B — NO_RELEASE
2026-11-24. TWO_NATIVE_GLB_REIMPORTED / SIX_VTK_VIEWS / ART_REJECTED / WEBGL_UNTESTED / NO_RELEASE.

Read main owl-pet/AGENTS.md, README, STATUS, prototype/index.html, #172 v3 review and Run339 record at fab844892bde978963c3c556bcc2f2e67ab028ea. Retrieved and visually inspected actual v3 PNG (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b). Right bird has cream down, dark recessed glossy eyes, warm feathered heart rim, small ivory beak, buried short wings and supported robust feet. Exact age and posterior details unverified.

Actual free local experiment: Python, NumPy, Trimesh, VTK, Pillow. Blender executable/bpy absent, Chromium available. Following Run339 high polygon relief, test a continuous closed deformed icosphere skull with integrated orbital depressions and subtle rim on a 20,480-triangle surface. A uses protruding globes; B translates each globe 8 mm inward and adds organic variable-thickness eyelid ring; two changes together, not a single-factor causal test. No beak, torso, down or finished feather texture; limited eye seating study only, not a complete pet. Exported and reimported two native GLBs:
- A 442608 bytes, 23040 triangles, SHA256 1b9f89eda5350551d81ce59b6e9e20fd8ed210581c38cdd9b95a1392caa63528.
- B 503664 bytes, 27648 triangles, SHA256 abb91bf0cd471b97a28bbc4aebfc9343f9bef746db34ea9fd8cdafad1536885d.
- Six actual 400x400 VTK views (front, 35, 70 degrees each), full montage 1200x800 SHA256 988238832f8b7f8981b79baa2c271d9d16ba0854e0707bce298b9141475eb9ce. VTK used manual specular settings for eyes rather than standard glTF PBR shader, hence no PBR validation.

Visual inspection: B reduces obviously protruding eyes in oblique view; lids remain detached, asymmetric looking, ring-like rather than naturally feathered, eyes too dark and lacking convincing reflections. Skull is smooth egg-like, heart disc vague and lacks feather structure, unlike reference. Both ART_REJECTED. Reduced triangle count alone is not equivalent visual quality. No whole bird, posterior anatomy, WebGL or physical phone validation. Stop repeating primitive head/rim sculpt as a candidate; need source artist-quality continuous topology or better surface reconstruction, then realistic eye socket feather transition. Do not release.

Evidence:
- [Executed source](run340-local/head.py.gz.b64), commit b9ec9aff6b525662018d6aab4d386fb34d6f96f8, exact readback, blob ab439de0fbc76e96301a4cc3ece758f7cf667434 equals local encoded source. Base64 decode then gunzip; raw script SHA256 9fa558033b64a1a33bbf872102b41ac32cb8d0f465b81b109b3559247c649ca9.
- [Actual audit thumbnail](run340-local/audit.jpg.b64), commit 3051682d2608a6c5cfb29dbf1bd61dd6a581eb16, exact readback, blob 708043584e5cc534c8374942aad2c80dd6001207; base64 decode, 120x80 grayscale JPEG, local SHA256 7963d3d57d7288c770a387a7888d42fdf33e9a0a4afc048c355c2100a762479d. A top, B bottom. Full GLBs and full-size renderings generated locally only, not uploaded.
Zero extra spend. Independent branch from Run339 commit. No edits to main, existing prototype, species pipeline, source concept or deployment.
