# #172 Tyto castanops v3 — Run181 independent source-bound GLB visual rejection

**2026-11-18. ART_REJECTED / NO_RELEASE.** No user-facing character demo, no product adoption, no main-branch change, no paid tools.

## Preflight and real original-source chain

Read owl-pet README and AGENTS, original v3 mesoptile design record, Run178 rejection, Run179 failure and Run180 recovery. The reference is the **rightmost** age-unknown mesoptile from original v3, not an adult Tyto. Original extracted crop verified SHA256: `5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9`. Run180 cleaned only connected exterior dark background; that **new** input was independently verified in CI as SHA256 `8f47899ba4fced01ffe92b3b8b6615884a62f4880528219aff57aef9b3622145`, so this evaluation genuinely addresses the new image-conditioned Run180 output, not the art-rejected Run175/178 asset.

The new official free three.ws MCP mesh_forge GLB was fetched directly from `https://three.ws/cdn/forge/anon/2b5c60a2-4b7a-4f70-af17-ba3b95d23341.glb` with HTTP **200** and checked byte-for-byte against SHA256 `809e2110faec1301072c99f08a3caf440e9fd30692c7dd8c5e80bf109b9f8c48`. This is a genuine GLB with 470,660 bytes, one model mesh, **26,016 triangles**; not an SVG, a toy mesh substitution, the rejected Run175 GLB, or a screenshot masquerading as 3D. The exact binary is retained in the isolated Actions artifact, **not** committed to git.

## Executed WebGL and visual art review

[Run181 verified GitHub Actions execution](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44289277183) actually loaded the GLB in Three.js/GLTFLoader through Chromium at a **390 × 844 simulated phone viewport, deviceScaleFactor 2**. The renderer used ANGLE SwiftShader software WebGL2; all seven axis/oblique views drew 26,016 triangles and 1 draw call without context loss, with no page errors. Seven real raster captures, stitched contact sheet, actual GLTF measurements, SHA256 manifest and logs are [archived in Run181's isolated research directory](research-evidence-run181-CLEAN-NATIVE-WEBGL-NO_RELEASE/). This demonstrates format/draw compatibility on desktop software WebGL, **not** actual iPhone/Android hardware, frame rate, GPU memory or battery acceptance.

I visually opened the actual **[seven-view WebGL raster sheet](research-evidence-run181-CLEAN-NATIVE-WEBGL-NO_RELEASE/run181_real_software_webgl_sevenview_UNREVIEWED.png)** at full canvas size and compared it with the original cleaned concept. The following mismatches are decisive:

- **EYES/COLOUR FAIL:** the entire model is pale flat clay-white; both intended dark open eyes are reduced to vague shallow sockets; the bill and face have almost no contrasting colour. Runtime reports **0 texture maps**, exactly matching the provider's `look_at_model` no-texture warning.
- **DOWN FAIL:** despite a lighter surface than rejected Run178, crown and back contain sharp nubs, rigid overlapping plate/splinter ridges and carved adult feather structures. Nothing resembles thick fine airy cream mesoptile down in true side/back views.
- **JUVENILE ANATOMY FAIL:** the side silhouettes are too long, slim, rear-tapering and clearly show large layered wing feathers with a protruding pointed posterior, not a compact round hatchling with down-buried wings and concealed tail.
- **UNDERSIDE/FEET FAIL:** bottom view is a deeply open, ribbed, shell-like cavity, not a finished continuous soft belly. Feet project beneath the character with no eucalypt hollow/lip physical support.
- **FACE/SIDE COHERENCE FAIL:** a broad Tyto facial outline is detectable head-on, but the mask becomes a long flat protruding beaklike form in oblique/strict profile and loses its naturally integrated fluffy shape.

The geometrical structure and non-textured surface are both **art-unacceptable**. 26K triangles and successful simulated WebGL render do not meet the release threshold; cosmetic recolouring would hide neither the hollow underside nor wrong adult-like wing and tail anatomy. No artificial improvements/edits to the rejected GLB should be called a completed pet.

## Evidence and repository boundary

[Raw machine evidence](research-evidence-run181-CLEAN-NATIVE-WEBGL-NO_RELEASE/run181_metrics.json) includes source SHA, clean-input SHA, GLB SHA, renderer, triangle count and all seven draw results; the [SHA256 manifest](research-evidence-run181-CLEAN-NATIVE-WEBGL-NO_RELEASE/run181_sha256_manifest.json) includes the GLB, source logs and original PNGs. Original GLB binary retained only in the 30-day [isolated workflow artifact](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44289277183), not released or added to git. Unaccepted model SHA now registered in the negative-only rejection registry so it cannot be silently reused.

No other owl species, 251-species concept production, repository main, existing pet prototype or deployment was changed. Extra purchased credits/fees: **$0**.

**Final gate: ART_REJECTED / NO_RELEASE.** Future candidates need a genuinely different full-volume juvenile anatomical base with high-quality down, dark open eyes, fully closed underside, supported feet and proper true multi-axis appearance. Physical mobile WebGL remains untested until an actual art-passing GLB exists.
