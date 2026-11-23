# Run333 — shell fur mask A/B, local WebGL2 recovered — NO_RELEASE
2026-11-24 Asia/Shanghai. TWO_NATIVE_GLB_REIMPORTED / SIX_VTK_VIEWS / SIX_LOCAL_WEBGL2_VIEWS / ART_REJECTED / PHYSICAL_PHONE_UNTESTED / NO_RELEASE.

## Preflight
Read main owl-pet/AGENTS.md, README.md, STATUS.md, prototype/index.html (first 35 lines), and research/reviews/172-tyto-castanops-v3-review.md. Main STATUS latest visible entry 205/251, active batch, independent production. Read Run332 audit and actual source at 919d46e1334d681789fd1d17ef211abfb78dcf1f. Fetched and visually inspected original 1536x1024 #172 v3 concept (Git blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b). Rightmost chick: cream thick mesoptile, dark eyes, heart-shaped disc with warm narrow rim, buried short wings, hidden tail, supported feet, unknown precise age. Concept scientific verification=false. Blender/bpy unavailable. No paid tools or external assets invoked.

## Actual controlled local experiment
Instead of another crossed ribbon atlas, test continuous low-frequency cream backing and layered shell-mask fur on a 5cm-wide ellipsoidal curved swatch. A single opaque surface; B same surface plus five offset shells from 0.72mm to 3.28mm, progressively masked by seeded length noise, lighter outer cream. Not a bird sculpture; UV seam and poles are not welded. Both actual GLBs reimported with expected geometry counts. Binary GLB JSON checked: A one opaque material, B one opaque and five MASK materials (cutoff=.5), six embedded textures total, all doubleSided=false.
| Variant | Triangles | Bytes | SHA256 |
|---|---:|---:|---|
| A baked | 6912 | 227136 | 264d091532046851876f33eadba3d8ac8afffb771621ace1a3a1fb0d03838d5f |
| B shell | 41472 | 759176 | 019f9f6c52f064b62194e863d83935239cbed4684abb47cc9c53f37235849b25 |

Six actual 360x360 VTK renders reviewed. B has more continuous backing coverage than prior ribbon approaches and a fuzzy edge; however visible layered contour rings, cloth-like surface, pole distortion and missing distinct down clumps. A looks smooth, not feathers. B costs 6x triangles and 3.34x GLB bytes relative to A. Neither accepted.

## Local browser recovery and actual native GLB rendering
Unlike Run332, launching Chromium under xvfb-run with --no-sandbox --use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader successfully created WebGL 2.0 (OpenGL ES 3.0 Chromium); separate EGL configuration returned null. External Three.js CDN DNS failed. Implemented a narrow local GLB parser in Playwright page.evaluate, passing actual GLB bytes base64, parsing embedded position, UV, index, and texture buffers, drawing real indexed 3D triangles with depth test and shader discard at the GLB alpha cutoff. Rendered A/B at rotations 0, 1.1, 2.3 rad, 390x390 canvas inside 390x780 simulated mobile viewport. All six draws gl.getError()=0, A 6912 and B 41472 triangles each. No HTTP server or external library required. This is not a general GLTFLoader, no PBR, culling, scene transforms, animation, touch interaction, or phone performance benchmark. The simple shader uses radial lighting and linear filtering, not production shading.

Actually inspected full 1170x780 WebGL comparison. B has conspicuous dark pinhole/outline noise, not the softer VTK appearance; possible filtering of transparent pixels, mask threshold and depth interactions need isolation, not established cause. Neither visually meets soft fluffy down requirement. Shell overdraw and triangle cost are also unresolved. Crucial finding: real browser MASK evaluation is available locally again and must be used instead of relying on VTK blending. No full chick generated; no art-approved GLB; no physical phone test.

## Evidence / reproducibility
- [Executed shell.py](run333-local/shell.py), local SHA256 d0e75186e1ef64302806d52ddb296abd32b11ff41d45571267e3fe250f22bcf8; local git hash-object and remote readback match 10c9c4d7cd0d7698135dc06f41f13e5aaa6bfab1.
- [Executed webgl.py](run333-local/webgl.py), local SHA256 5cca95cfc7852521461dcb9d086375cd6a0615264f91e88aef93f922c1d2ace8; local git hash-object and remote readback match 068d2958afef0dcef3de1d7f3f4b5dd6dd2f663e.
- [Actual WebGL six-view thumbnail, base64 JPEG](run333-local/webgl-tiny.jpg.b64), remote encoded text read back exact; local decoded thumbnail 2248 bytes, SHA256 f2eed2ad71a14fcb58df6456f83fbb2e3331f3df33f1cd57f4fbe4f2ad0c39a8. Full WebGL montage SHA256 98ebe8e55072e7db4af5924c1b1d055c48cb4720c6a28a88e887fd3a429780bd; full VTK montage SHA256 317a7ef0ddc35709c5779cb3472f484ee0dd250aa9ae301ea6b18a43957c9d45. Full GLBs and full-size images generated locally only, not uploaded.
- Reproduce in isolated directory with NumPy, scipy, Pillow, Trimesh, VTK, Chromium and Playwright: xvfb-run -a python shell.py; xvfb-run -a python webgl.py.

Research branch only; no main, production, original concept, existing kitten prototype or deployment writes. Next experiment: diagnose dark alpha edges with constant RGB/alpha-bleed controlled A/B, reduce shell polygon budget, investigate actual down-clump normal/coverage shading. Do not expand swatch into pretend chick. Professional whole-chick anatomical sculpt still required. NO_RELEASE.
