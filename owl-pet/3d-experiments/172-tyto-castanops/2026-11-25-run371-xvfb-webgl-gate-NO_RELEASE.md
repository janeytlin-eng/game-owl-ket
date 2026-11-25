# Run371 — Xvfb SwiftShader native WebGL2 gate — ART_REJECTED / NO_RELEASE
2026-11-25; additional spend $0. Independent branch from Run370 f2459350e4184aa075720b9f34798141badc0214.

## Preflight
Re-read main AGENTS, README, STATUS (206/251, latest six revisions), #172 v3 review and Run370. Target cream thick mesoptile, developed heart mask, wings buried under down, concealed tail, age unknown; science=false. Run370 rejected two alternate foundations. No Blender, CUDA false; DNS errors persist for GitHub/raw/Hugging Face/Sketchfab in local container. Downloaded actual original SF3D artifact 14795923598 through GitHub connector, unzipped and verified exact GLB SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be. Source is 1,137,108 bytes, 16,971 vertices, 27,372 triangles, embedded base-color and normal JPEGs. No mesh changes this run.

## New result: restore actual browser rendering despite prior context failure
Used installed Chromium, Playwright and Xvfb display, headless=False, LIBGL_ALWAYS_SOFTWARE=1. X11 ANGLE GL and X11 ANGLE EGL both failed getContext('webgl2'). X11 ANGLE SwiftShader succeeded; real clear and readPixels [51,102,153,255], error 0, WebGL 2.0, max texture size 8192. Renderer ANGLE (Google, Vulkan 1.3.0 (SwiftShader Device (Subzero) (0x0000C0DE)), SwiftShader driver). This is software rendering, not real mobile hardware.

Repro command:
```sh
LIBGL_ALWAYS_SOFTWARE=1 xvfb-run -a -s '-screen 0 1024x1024x24' python webgl_qa.py
```
Browser args: --no-sandbox --disable-dev-shm-usage --use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ozone-platform=x11. Playwright new_page(viewport={'width':390,'height':844}, device_scale_factor=1,is_mobile=True,has_touch=True), mobile viewport meta, canvas 390x390. Native WebGL2 code parsed original GLB header, JSON and BIN, uploaded POSITION/NORMAL/UV and uint32 index buffer, decoded both JPEGs using createImageBitmap, generated mipmaps, compiled GLSL ES 3.0 vertex and fragment shaders, drew actual triangles with depth test and back-face culling. Directional approximation of texture+normal lighting, not full PBR. No external JS, no SVG, no procedural replacement geometry. Rotation in shader, four draws and readPixels with error checks. Front correctly negative Z. Core executed code excerpt:
```js
const n=dv.getUint32(12,true),j=JSON.parse(new TextDecoder().decode(bytes.slice(20,20+n))),start=28+n;
const view=i=>{const v=j.bufferViews[i];return bytes.slice(start+(v.byteOffset||0),start+(v.byteOffset||0)+v.byteLength)};
gl.enable(gl.DEPTH_TEST);gl.enable(gl.CULL_FACE);
gl.uniform1f(gl.getUniformLocation(program,'angle'),angle);
gl.drawElements(gl.TRIANGLES,a.count,gl.UNSIGNED_INT,a.byteOffset||0);gl.finish();
gl.readPixels(0,0,390,390,gl.RGBA,gl.UNSIGNED_BYTE,pix);
```

| View | degrees | foreground pixels | RGB FNV-like framebuffer hash | gl error | draw+readback wall ms |
|---|---:|---:|---|---:|---:|
| front |180|63345|9e28b8f5|0|153.75|
| quarter |135|59875|8a526db4|0|36.74|
| side |90|52224|b7ec6dc2|0|32.09|
| rear |0|63340|18042c98|0|30.63|

Actual pointer drag from x130 to x230 changed rotation 3.141592653589793 to 4.341592653589793 rad. No touch hardware test; mouse pointer injection only. Wall time includes readback and IPC and is not FPS benchmark. Actual four screenshots viewed in contact sheet: front mask recognizable, quarter and side reveal flattened feet and side seam; rear resembles an undifferentiated rounded mass, absent convincing shoulder wings and down volume. Dark edge atop head and baked texture remain; reject art. This solves current local software browser diagnostic blockage, NOT phone WebGL acceptance or a new art sample.

Actual source scripts hashes: webgl_qa.py 2550f05526ba8a534e79c3f4cbc047f4ba3c8b5c644c30f186dd8cd1fe24004b; probe.py 5230b46b388aee390b32ceaca3e83ff5aa25af1bff42489a064195ddf4614347. Report SHA256 f6b57bb8c715c07154052c626493e3777b4071874ccf2ae943e1bf88d480ee2f. Full 780x230 contact SHA256 68177250fa6ee0f8c9ea9a9c3042871be1fded8c07900322295709164bd18641. These full files exist locally in this run only. Actual tiny 176x52 JPEG evidence embedded below, 1508 bytes, SHA256 fee6e2b952095e93982fb6566cd74658317074848a0de6a169f094cef819a9b3. Decode base64; thumbnail is evidence only, not a visual release.

```base64
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
```

## New foundation search and source gate
Read pinned https://github.com/jaishakj/fauna-lab/blob/9d9b1515a823122efd51b97593c59b9e7ec28b82/data.js: links to Virtual Museums of Malopolska adult barn owl (same museum route already investigated in Run224/224b, not new base). Akimaylilll/owlrscon is an aerial reconstruction pipeline, not an owl scan; author labels WIP, not production-ready; no mesh asset in inspected tree. moizahmad418/3d-owl-character-configurator is actually product configurator, no qualified owl source. NVIDIAGameWorks/FleX search was bowl.obj false positive. External advertised CC0 adult Grab3D great horned owl and other known adult candidates do not meet juvenile morphology. No new downloaded third-party asset; no extra spend. No new mesh generated; no qualified sample. No changes to main, 251 species, original concepts or deployment. Continue independent foundation research; use new software WebGL path for screening only. Do not notify.
