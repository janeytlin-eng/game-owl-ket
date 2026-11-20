# #172 Tyto castanops v3 — Run255: native Hunyuan 3D / PBR microdown & ocular study

**2026-11-21 (Asia/Shanghai) / RESEARCH ONLY / ART_REJECTED / PHONE_UNTESTED / NO_RELEASE**

## Preflight / immutable input

Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, the existing kitten WebGL prototype description, original rightmost #172 v3 chick concept, and the Run251–254 native-3D scripts/QA/audits. Independently downloaded the 22-entry original [Run251 evidence](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44798375236/artifacts/14658854894) and the 23-entry [Run254 evidence](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44828726630/artifacts/14675936663), extracting actual GLBs and browser screenshots. Run254 front has moderately widened torso but side retains elongated adult-like wing/tail; eye/disk and tree support remain off-target. Further affine/surface-cut sculpt repetition was deprioritized.

Used original **Run251 A** true learned Hunyuan GLB (eye PBR repaired): 4,035,000 bytes; immutable SHA256 `cd1513ac0822eef25bb56f9f8d08d244cac64d209ea8c92333693d287c926eb6`. Contains nine authentic meshes, 85,009 total triangles, 34,000-triangle continuous closed neural core, 36,651-groom triangles, six ocular components and real 3D bark mesh. There is no image billboard or primitive approximation.

## Actual independent local experiment

Instead of more implausible adult-to-chick geometry warps, implemented and **executed** a separate free NumPy/Pillow/Trimesh 3D PBR material pipeline:
- Native 17,002-vertex learned core receives generated continuous azimuth/height UVs, a warm creamy RGBA-derived 1024² surface-albedo texture and anisotropic, gentle microdown tangent-space normal texture, both embedded into the actual GLB; 14,000 or 24,000 fine fiber strokes are painted **onto the 3D mesh UV texture**, never presented as a substitute for 3D geometry.
- Preserves all original natural learned geometry/topology and the original source 3D groom. Probes real mesh-space 1.16× and 1.25× enlargement of both sets of brown iris, black pupil and eye highlight geometry.
- Re-import verified nine 3D meshes, 85,009 triangles, closed/positive learned core, preserved groom, all UVs and actual embedded PBR baseColor/normal textures. No geometry added, no bare geometric assemblies. Outputs **two genuine native GLBs**.

**Local reproducible results** (the native 3D files and source are separately retained for review, not approved character assets):
- A: 4,896,680 bytes; GLB SHA256 `3b4d1449dcf11524ae581f250af06a1b484fa1a379af34dc137d72b27fadbf1d`; 14,000 painted source-following microstrands; 1.16× actual 3D eyes.
- B: 5,272,728 bytes; GLB SHA256 `9ff81650376b790e8880f3a8fc8bab6998289aacf36f91e16621182a813c4636`; 24,000 painted source-following microstrands; 1.25× actual 3D eyes.

Both independently rendered in VTK with actual 3D front, threequarter, left, back cameras (8 images), visually opened and reviewed. More natural warm PBR fiber colour and enlarged pupils alone **do not** yield acceptable juvenile anatomy. The VTK result still exhibits elongated rear wing/tail, over-firm face disk, dark speckled/spiky existing groom (also VTK renderer interpretation), excessive seam-like chest artifacts, smooth flat dorsal silhouette and a cookie-like wood pedestal rather than an old hollow. No immediate art improvement over the baseline; A and B **both ART_REJECTED**. Future work must prioritize an infant-specific artistic/learned 3D source and true anatomical short folded wings; adding any more cosmetic fur strands is not recommended.

## Remote browser replication / archive

Dedicated experiment branch `research/owl172-run255-native-neural-pbr-microdown-eye-material-no-release`, new isolated exporter `run255_anisotropic_juvenile_down_material.py` and dedicated [Run255 GitHub Actions workflow](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run255-native-neural-pbr-microdown-eye-material-no-release/.github/workflows/owl172-run255-genuine-neural-cream-down-ocular-material-no-release.yml) source SHA-pinned Run251 original under the GitHub-provided token. The workflow performs true Chromium/Three.js GLTFLoader seven-camera WebGL2 per variant, checks screenshot hashes and archives raw GLB, albedo and normal texture images, browser evidence, machine reports and original exporter in one research-only 30-day artifact. Technical WebGL2 passing is **not art acceptance**. [Run255 workflow attempt](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44832813118).

**Remote status pending until independently verified**. Do not claim browser result or publish until runner completion + downloaded raw binary audit.

No change to `main`, 251-species concept manufacturing, existing kitty prototype, root vocabulary game, deployment or online Sites. Zero external fees. No release; actual Android/iPhone hardware WebGL memory, framerate, touch and thermal state UNTESTED.
