# Run419 — direct EGL alpha reference gate — ART_REJECTED / NO_RELEASE

2026-11-27. Re-read main owl-pet AGENTS, README and STATUS (207/251); queried actual design tree: v3 reference is concepts/172-tyto-castanops-v3.png, blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b, 737545 bytes. No new visual inspection of source image claimed. Reference remains the right juvenile, cream-white down, heart-shaped facial disc and compact body. Re-read complete Run418 report at 3791d5ab6021f50dd87ae0bf458286e9e98afce9, which found VTK glTF importer MASK and BLEND pixel-identical. Preserve prior artifacts and do not repeat rejected base mesh modifications.

## Actual executed direct-renderer test
Bypassed the VTK glTF importer using Python ctypes, EGL surfaceless pbuffer (256x256, RGBA8), Mesa llvmpipe OpenGL 4.5 compatibility profile (Mesa 25.0.7-2, LLVM 19.1.7, 256 bits). Compiled GLSL 330 vertex and fragment shaders, uploaded procedural 256x256 RGBA feather alpha texture, drew a fullscreen triangle and read back RGBA pixels. This is a shader test fixture, NOT a character or actual glTF loader. Actual rendered three PNGs and comparison viewed. Results:

| Mode | Unique RGB | Background pixels | SHA256 raw top-down RGBA |
|---|---:|---:|---|
| OPAQUE | 1 | 0 | 478eef47e2bd388f18c4045413495325e570f9dcc3406af770b457a778177095 |
| MASK (.4) | 2 | 47100 | b3889cf71bef654d5fdcbac52dfd0f5a5c6b3252a1efad85f0d7065b98e412fc |
| BLEND | 251 | 31830 | 2cd3f0fe2e01eecd57f205ccf8f65da6b028dee3d4af389168e7a1cea8b4622b |

MASK and BLEND differ at 33,724 of 65,536 pixels. Background threshold <=1 per RGB channel relative to [26,36,46]. All three draws returned GL_NO_ERROR. Actual visual inspection: opaque flat cream square; mask crisp, binary striped feather silhouette; blend graded translucency showing individual semi-transparent barb stripes. This proves the direct EGL pipeline can separate these alpha semantics and is a useful independent reference for groom materials; it does not certify multi-layer transparency, full glTF correctness, real owl appearance or mobile performance. The test texture is deliberately artificial.

Core executed shader and atlas formula (source excerpts, not complete runnable script):
```glsl
#version 330 core
in vec2 uv;out vec4 color;uniform sampler2D atlas;uniform int mode;
void main(){vec4 c=texture(atlas,uv);if(mode==1&&c.a<0.4)discard;color=vec4(c.rgb,mode==2?c.a:1.0);}
```
```python
y,x=np.mgrid[0:256,0:256]/255.
width=.37*np.sin(np.pi*y)**.8+.008
edge=np.clip((width-abs(x-.5))*80,0,1)
barbs=.35+.65*(.5+.5*np.cos((y-abs(x-.5)*.55)*190))**2
opacity=edge*barbs*np.sin(np.pi*y)**.4
a=np.zeros((256,256,4),np.uint8)
a[:,:,:3]=[249,233,207]
a[:,:,3]=(opacity*255).astype(np.uint8)
```
GL_NEAREST min/mag filter, clear RGB (.10,.14,.18), blend enabled only for BLEND with GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA. EGL platform surfaceless 0x31DD, OpenGL API 0x30A2. Pixel readback via glReadPixels GL_RGBA/GL_UNSIGNED_BYTE, vertical flip before hash. Actual PNGs and full Python script were generated in runtime only; this record archives measured evidence and excerpts, not a remote binary archive.

## Browser gate — actual four launch attempts
Playwright Chromium HeadlessChrome/144.0.0.0, page.set_content with canvas (no local HTTP/file navigation). Tried default, ANGLE swiftshader, ANGLE swiftshader-webgl, EGL + disable-gpu-sandbox; all with no-sandbox and disable-dev-shm-usage. Both webgl2 and webgl context creation returned null in all four configurations, event message "BindToCurrentSequence failed", vendor/device 0xffff; EGL path reported disabled GL vendor/renderer. Thus the issue is not only local page URL access; browser GPU context creation is also blocked here. Separate 390x844 mobile-emulated viewport attempt also returned null. No physical phone tested.

## New no-fee sculpt routes screened
- https://github.com/Chethan-ULTIMAX/VIEWFORGE — local six-view silhouette visual-hull reconstruction. Author explicitly notes missing concavity and texture recovery. Single v3 juvenile view is insufficient; a hull alone would not satisfy the facial disc/eyes quality gate. No model downloaded or run.
- https://github.com/Hasasasaki/photo-to-mesh — local Hunyuan3D multiview plus experimental VGGT/2DGS reconstruction; requires open weights and GPU per author, not a new proven CPU-only route. No model executed.
- https://www.embossify.com/models/owl — free standard 4196-triangle CC0 model according to publisher; description says ear tufts and mathematically generated design; reject for wrong morphology and simplistic geometry before download. No new asset visual claim.
- Prior adult Mint and Innerscene candidates reappeared in results; not counted as new assets.

Decision: ART_REJECTED / NO_RELEASE. No accepted sculpt, no mobile WebGL sign-off, no paid service submission or additional external cost. No main changes, original concept modifications, species workflow or deployment edits. Direct EGL reference is a rendering diagnostic only; the core missing deliverable is still a high-quality new juvenile sculpt.