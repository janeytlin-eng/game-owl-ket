# #172 *Tyto castanops* v3 — Run140 + Run140B: real textured 3D LOD / Chromium WebGL2 mobile emulation

**2026-11-17 18:48 (Asia/Shanghai), final ART_REJECTED / NO_RELEASE.** This is actual model work and empirical render evidence. **It is not an art-approved juvenile, not an openable user pet, and not a physical phone benchmark.**

## Preflight, authentic source and provenance
Read current owl-pet instructions, existing cat-only WebGL prototype, species v3 profile, Run137 failed grey shell and Run138/139 native PBR research (independent audit: [Run138/139](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run139-3dvalley-actual-free-trellis2/owl-pet/3d-experiments/172-tyto-castanops/2026-11-17-run138-run139-no-fee-native-pbr-ART_REJECTED-NO_RELEASE.md)). Pinned **real** rightmost v3 source PNG 512×512 SHA256 `e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8`.

**Input binary is exclusively the actual Run139 free 3DValley/TRELLIS.2 generated GLB from Actions artifact**, NOT a new primitive/low-poly imitation. Hard-checked original SHA256 `9a154c9e3aeebb34ebcd6f209760e1d9e21e2f544f2b690dae406d9c8bf878e8`, 9,983,448 bytes, 192,765 triangles, 2 textures, 1 material, 0 animations. Source art has already been rejected on genuine Blender front/quarter/side/back views: half-closed instead of open round eyes, hard face outline, adult-like wing feathers and long visible tail, dirty speckled back, exposed unsupported claws and no tree hollow.

## Run140 actual Blender textured mesh LOD experiment
[Successful genuine workflow 44067284027](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44067284027). Downloaded **same original binary** with GitHub Actions `download-artifact`, SHA256 verified, actual Blender 4.0.2 import and quadric DECIMATE applied to the real mesh, exported two genuinely new **textured GLB files**, leaving original intact:

| Model | Real triangles | File bytes | SHA256 |
|---|---:|---:|---|
| Run139 source | 192,765 | 9,983,448 | `9a154c9e3aeebb34ebcd6f209760e1d9e21e2f544f2b690dae406d9c8bf878e8` |
| Run140 LOD25 | 48,191 | 3,379,508 | `6a39340f48b0d83b31a6b1147f341121648430dd15537151bac72acbba48ee50` |
| Run140 LOD12 | 23,131 | 1,872,512 | `f9e5371e77a497a5e74458f97b0bad48a5592aa7919e079d602a26bd9966dc08` |

25% triangle variant reduces bytes ~66%, 12% reduces bytes ~81% (relative to source); **this is a native mesh/payload optimization**, not an artistic quality improvement, and no animation/rig added.

Installed actual Three.js and Playwright Chromium. Browser truly loaded each of these three GLBs on both 1280×720 desktop and **390×844 simulated touch/mobile viewport** with WebGL2 SwiftShader. Six actual JavaScript model loads and renders had >10 draws and 0 page errors, with screenshot/JSON evidence. **But inspection of actual mobile back-angle screenshots found a severe visual bug**: rotating the off-center imported root instead of a centered pivot pushed almost the entire owl off the right side of the mobile frame, despite green renderer counters. Accordingly, Run140 alone must **not** be interpreted as valid framed mobile viewing.

## Run140B actual corrective browser replay, no new inference or fee
[Successful genuine workflow 44067919279](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44067919279) replayed **identical source, LOD25 and LOD12 GLB binaries** from Run140 artifact, performed **no new neural inference**. Fixed Three.js scene hierarchy with a new centered parent pivot, rotating the pivot instead of offset mesh; computed portrait-oriented camera distance from camera FOV/aspect. Captured real front on desktop and back on phone-sized viewport, preserving no-release watermark.

All **six** genuine WebGL2 software emulation render tests (source, LOD25, LOD12 × desktop1280/mobile390) passed: no browser page errors, all full meshes loaded and drew, **all calculated projected model bounding boxes fit inside NDC viewport** (`frustum_bbox_fits=true`). I opened the genuine Run140B 390×844 backside screenshot: owl now really is centered and entirely visible, whereas Run140 was off-screen. Evidence is retained in `run140b_actual_browser_framing_qa.json`, six actual PNGs, browser logs and SHA256SUMS. **This proves software Chromium/Three.js openability and camera framing only**, not real phone GPU/frame-rate, touch gestures, thermal load, battery, iOS Safari/Android quality. Earlier SwiftShader p95 timings are *not* mobile hardware benchmarks.

## Real multi-angle art decision: remains FAIL
I personally inspected the Run139 source four-direction native Blender contact sheet and both Run140/140B actual software WebGL screenshots. New mesh is genuinely textured, recognizably an owl, with a heart face and some feather-like relief. However against the **rightmost cream mesoptile**, the eye apertures are wrong (narrow/squinting), face edges overly rigid, long adult-type primaries and tail exposed, feet not supported on an aged eucalyptus hollow lip, back texture darkly speckled/chipped and not convincing natural cream second-down. Even with geometric LOD optimization and centered mobile framing, it is still a **visually rejected** character. No release, user-facing view link, product integration, or publication.

Rights also remain unverified beyond the generating site's own public statement, and original output plus LOD derivatives are retained in short-lived **quarantined Actions artifacts** (Run140 artifact **14321855086**; Run140B artifact **14321542093**, 30-day retention), **not committed as redistributable repository GLBs**. No login bypass, provider quota bypass or added payment. Total extra spend zero.

## Evidence and isolation
- Run140 audit folder: `owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run140-PBR-LOD-SIMULATED-MOBILE-NO_RELEASE/`; contains source fingerprint, real Blender LOD report and log, six actual WebGL screenshots, JSON, SHA256 manifest and strict `NO_RELEASE.flag`.
- Run140B audit folder: `owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run140b-FRAMED-MOBILE-REPLAY-NO_RELEASE/`; original binary and 2 authentic LODs replayed, screenshots, camera viewport NDC checks, error traces, checksum manifest and strict `NO_RELEASE.flag`.
- Updated independent `known_rejected_asset_sha256_registry.json` with Run139 SHA and both actual derived LOD SHA to avoid future duplicate acceptance.
- Against fixed Run137C baseline `434da8d2f7e113ed4aa30d97c52e99e5a3570c3d`, Compare before this audit reported **14 commits ahead, 0 behind, 96 changed paths; zero outside** #172 independent experiment directory or dedicated new Run139/140/140B workflows. Did **not** modify main, 251-species original prototype pipeline, existing pet prototype, v3 concept art or deployment.

**Final: ART_REJECTED / NO_RELEASE.** The genuine 192k PBR GLB → optimized 48k/23k variants → actual software WebGL2 viewer is now technically reproducible, and the mobile-portrait camera bug is fixed. But technical progress does **not** waive 4-angle young-owl art fidelity, original source rights or true phone acceptance. No acceptable public character sample yet.