# Run178 — human visual review of real browser-rendered GLB

**ART_REJECTED / NO_RELEASE.** Do not present as a finished #172 Tyto castanops v3 age-unknown mesoptile owl or launch into mobile production.

## Original input and provenance

- Original v3 rightmost cream-down juvenile crop: `research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png`; SHA256 `5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9`.
- Genuinely image-conditioned free three.ws MCP `mesh_forge` GLB generated in Run175, recovered in Run176; actual GLB SHA256 `c56c1a1c0159e11a140f587f12ad4c84b49fdb38b9b3142078f3de9d75f46e99`, 10,840,896 bytes, 90,618 triangles, 1 mesh, 1 material/texture.
- Run178 reopened precisely those bytes through Three.js/GLTFLoader in headless Chromium ANGLE SwiftShader (software WebGL2), 390x844 simulated phone viewport (390px canvas, 2x pixel ratio). 7 genuine axis screenshots, 90,618 triangles/frame, no lost context and no browser page errors. This is **not** a real phone GPU or frame-rate acceptance.

## Real visual verdict

Reviewed `research-evidence-run178-REAL-WEBGL-SOFTWARE-NO_RELEASE/run178_real_software_webgl_sevenview_UNREVIEWED.png` visually, against the original reference.

- **Partial positive**: a coherent recognizable Tyto heart-shaped facial-mask contour exists in one forward-facing direction; model really has depth across multiple camera axes, not a 2D cutout. It renders as an actual textured GLB in WebGL.
- **Major fail: down and colour**: the entire crown, torso, wing, and back are hard, encrusted, pointed plate-like grey/brown surfaces, not lush fine cream-white second-down/mesoptile fluff. Surface reads like weathered stone or layered scales.
- **Major fail: juvenile anatomy**: both strict side views show disproportionately large rigid adult-style folded wing layers, with trailing pointed tips/tail; not short wings buried inside down or concealed tail.
- **Major fail: full 3D continuity**: underside camera shows a near-black open shell / broken hollow inner surface instead of continuous belly and supported feet. Back is overly textured hard plates rather than rounded down-filled silhouette.
- **Major fail: face quality**: dark eyes read narrow/half-closed and severe; the facial disc projects unnaturally away from the skull in strict side profile compared with the source's softly integrated face.
- **Major fail: support**: feet/talons are fully exposed without the required broad old eucalypt hollow-lip support.

Therefore browser format/geometry feasibility does not imply art quality. **No acceptance, no deployment, no customer-facing sample, no paid tools.** Avoid reusing this SHA as a starting point for cosmetic retexturing; replace the anatomical base with a source that is actually round, down-covered, and complete in all directions.

## Independent evidence

- [Run178 actual CI execution](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44285363504)
- [Actual browser 7-axis screenshot sheet](research-evidence-run178-REAL-WEBGL-SOFTWARE-NO_RELEASE/run178_real_software_webgl_sevenview_UNREVIEWED.png)
- [Runtime metrics and GPU identity](research-evidence-run178-REAL-WEBGL-SOFTWARE-NO_RELEASE/run178_metrics.json)
- [Evidence SHA256 manifest](research-evidence-run178-REAL-WEBGL-SOFTWARE-NO_RELEASE/run178_sha256_manifest.json)
- Original GLB retained only in isolated GitHub Actions artifact, not in git history. All changes confined to #172 research and dedicated workflow; `main`, 251-species production, original prototype and deployment untouched.
