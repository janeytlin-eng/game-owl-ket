# Run334 — controlled browser alpha decode diagnosis — NO_RELEASE
2026-11-24 Asia/Shanghai. NATIVE_GLB_REIMPORTED / NINE_LOCAL_WEBGL2_VIEWS / ALPHA_DECODE_ARTIFACT_ISOLATED / ART_REJECTED / PHYSICAL_PHONE_UNTESTED / NO_RELEASE.

Preflight: read main owl-pet/AGENTS.md, README, STATUS (latest visible 205/251, separate production), existing kitten prototype first 30 lines and #172 v3 review (PASS_WITH_LIMITATIONS, science=false), and Run333 audit plus actual shell.py/webgl.py at e7ead811ab91f545ebf772620719e67c8d6fa089. Original concept not reopened this round; target grounded in repository review: cream thick mesoptile, developed heart-shaped mask, dark eyes, short wing buried in down, tail hidden, supported feet, precise age unknown. No full bird claimed.

## Executed experiment
Generate same 5cm shell swatch type as Run333 with 25x37 grid, 128px seeded binary masks, six layers, constant cream RGB (242,226,201) even where alpha zero. Native GLB reimported: 10,368 triangles, 110,100 bytes, SHA256 f639ff33c28b5f9ff3a878f59e255515228b7ff9fcb4cf769b54ea2437f3883e. One quarter of Run333 B triangle count, not a quality-equivalent comparison. First local attempt failed Pillow int64 alpha array; fixed explicit uint8 and reran successfully.

Same GLB and same camera for three rendering conditions: 0 default createImageBitmap; 1 explicit premultiplyAlpha:none AND colorSpaceConversion:none; 2 default bitmap plus shader constant RGB (reference, same sampled alpha). Chromium via xvfb and ANGLE SwiftShader, 390x780 simulated mobile viewport, 390px canvas; angles 0,1.1,2.3 radians. Nine renders all gl.getError=0 and 10,368 indexed triangles. No general GLTF loader or PBR benchmark.

Actual pixel comparison (foreground ref red >100), absolute RGB error in 8bit levels, proportion with any channel error >10:
| Angle | FG pixels | Default mean error | Default >10 | Explicit mean error | Explicit >10 |
|---|---:|---:|---:|---:|---:|
|0|58107|16.88894|33.52952%|0|0%|
|1.1|46683|17.11487|33.73605%|0.00001428|0%|
|2.3|50386|16.97049|33.67007%|0.00000662|0%|

Actual full 1170x1170 montage inspected: default top row dark contour labyrinth reproduces Run333 problem; explicit middle row visually matches constant RGB bottom row. This isolates a bitmap-decode/texture RGB handling artifact in the custom renderer; the two options changed jointly so cannot independently attribute to premultiplication vs color space. Does not prove all Run333 artifacts fixed in production loaders. Important: removing false dark edges exposes smooth egg-like cream swatch with stepped outline, not natural down. All variants ART_REJECTED. No full chick, no physical phone test.

Evidence: executed [experiment.py](run334-local/experiment.py) remote exact source readback git blob 4ea878129a80742813bcf05f2f33ca0d9961e81b matches local git hash-object; local SHA256 55e22da45abc8ff636bbdf86bea748d408ec6042c1ae646e84f5275f8461f49b. Reproduce isolated with NumPy/SciPy/Pillow/Trimesh/Playwright/Chromium: xvfb-run -a python experiment.py. Full montage SHA256 ca5409b42f5cf7fb8b05009d91bdaaecfd8a460773e8cfee57030657ac61087a; [120px JPEG thumbnail encoded base64](run334-local/montage-tiny.jpg.b64) 1829 decoded bytes SHA256 b792fccea59823eeac2c0348d87ef7d74bdd23dceca8347949076a5e35f7ccf3. Full GLB and full-size renders local only. Next: split the two bitmap options in a controlled test, implement directional clump normal/coverage shading and validate actual loader behavior, independent of whole-chick sculpt. No main/production/original concept/prototype/deployment write, no paid calls. NO_RELEASE.
