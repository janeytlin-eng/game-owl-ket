# Run354 — native EGL ES3 software draw + new engine/source audit — NO_RELEASE
2026-11-25 Asia/Shanghai. ART_REJECTED / NO_RELEASE. No new model generated.

## Preflight
Read main AGENTS, README, STATUS (206/251), DESIGN_WORKFLOW, prototype/index.html, #172 v3 species record and review; reread Run353 at 73ae88b218bf2b37d8b715554c4f86381c5e8f8c and earlier Runs87B,95,99B. Target remains rightmost cream age-unknown mesoptile. Single original view does not prove the actual rear anatomy. Recovered historical artifact 14733006902, ZIP test passed, actual reference crop opened. Source GLB SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117, unchanged historical neural donor, not a new inference.

## Alternative source / engine exploration
- Actual fal library 3D lookup, history search and recommendation with US$0 ceiling each returned "User input required but current turn is running in a non-interactive mode." No job submitted, no money spent.
- [Modly](https://github.com/lightningpixel/modly) is locally GPU-oriented; [Image To 3D](https://github.com/neko-legends/image-to-3D) explicitly does not support CPU inference. [Modelado](https://huggingface.co/alegauss/modelado-models) has CPU ONNX weights but is still TripoSR, not new reconstruction. [Image to Mesh Web](https://github.com/tomosud/Image_to_Mesh_web) uses MoGe-2 with WASM fallback but predicts single-view depth and cannot establish a complete anatomically plausible rear; not acceptable as whole-body reconstruction.
- [Innerscene](https://www.innerscene.com/tools/library/3d-parts/owl-d696472a) direct binary download failed in current container. Run87B already establishes this exact donor is an adult horned owl, rejected. [Grab3D](https://grab3d.com/models/animals/owl/) also explicitly adult horned owl; [museum barn owl](https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc) is not verified juvenile; [CGTrader sculpt](https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt) listed no-AI license, not taken as generative input. No suitably licensed complete juvenile source verified.
- Actual local runtime: CUDA false, bpy absent, onnxruntime absent; github.com, huggingface.co, pypi.org hostname resolution returned no results. But Mesa libEGL and software DRI are present.

## Actual new technical experiment
Instead of another rejected mesh modification, tested a native surfaceless EGL 1.5 pbuffer with OpenGL ES 3.2 and real GLSL ES 300 shaders, using Mesa llvmpipe (LLVM 19.1.7, 256 bits), loading the real historical GLB through Trimesh and sending its largest connected component (50,205 vertices, 100,534 triangles) with position, normal and vertex color through indexed GPU-style draw calls. 390x500 viewport, 4 actual draw calls, glFinish, glReadPixels, saved four PNGs and full contact. Not a browser/WebGL test; this proves native software rasterization in the current environment, which is a distinct route from previous Chromium context failures. Shader is basic diffuse vertex color, not PBR.

| Azimuth | Draw+finish ms (single measurement) | Non-background pixels | GL error |
|---|---:|---:|---:|
|0|180.007539|90139|0|
|45|12.586483|70090|0|
|90|11.685753|64733|0|
|180|12.037815|90139|0|

First draw includes possible initialization/compilation overhead; remaining values are not a benchmark, no repeat distribution, no phone FPS or thermals. Actual pixel contact sheet opened: frontal heart disc discernible but eyes remain recessed, side profile too flat and the back is dark, lumpy, and clay-like. Still rejected. No new model, no validated mobile WebGL, no release.

## Evidence
Executed source egl_probe.py 5553 bytes SHA256 b4a0c1a25dcd9c29918aea7881f5aa67a25adefa5e480a92b4281ce95feb9455.
Actual metrics JSON 1053 bytes SHA256 66be62beae964cc28c396f51b3cbaeda62c9e1104054c153d50d78cfe5eba526.
Actual full contact 780x1000 JPEG 65076 bytes SHA256 c942649bce04be585c16a20ec891ac40450d89ce7e808486ff658a394b569f07.
Actual reduced contact 156x200 JPEG 2541 bytes SHA256 172206a931ff3996a6a28a40e9c03fca71e1e3f97b0fb94f34f11126dd22bbbe.
Full source and full renders local to this execution unless independently committed; no claims of remote binary completeness. Historical original donor remains artifact 14733006902.
No changes to main, species pipeline, source art, prototype or live site; no paid jobs. Next: new genuinely organic juvenile sculpt/engine; native EGL can be used for offscreen shader QA but does not waive browser and real-phone requirements.
