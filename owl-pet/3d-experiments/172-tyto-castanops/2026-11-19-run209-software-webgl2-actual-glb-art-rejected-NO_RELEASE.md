# Run209 — actual software WebGL2 render of rejected native GLB: TECHNICAL_PASS / ART_REJECTED / NO_RELEASE

**2026-11-19 · #172 `Tyto castanops` v3 · rightmost age-unknown cream mesoptile.** This is research QA, not a new accepted model. Extra paid spend: **$0**.

## Repository and reference preflight

Read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/research/species/172-tyto-castanops-v3.md`, the existing cat-only `owl-pet/prototype/index.html` description, Run207–207b visual refusal and Run208–208b latest research audit. The mandatory visual target remains a fluffy **cream second-down age-unknown juvenile**, organically integrated heart-shaped disc, dark eyes, compact down-buried wings, concealed tail and full hollow-lip support. The real original 2D crop is **not locally accessible** in this run, so pixel-level match is not asserted. Main's 251-species production pipeline and pre-existing prototype must remain unchanged.

## Actual trial and negative-control provenance

Re-opened the attached **Run207–207b original evidence ZIP**, extracted the **unchanged Run207b GLB** and independently recomputed SHA256 `c6cead1a89aa9f620b630a2635d046398db86392178145182018f96344bc1812` (2,873,788 bytes). Reimport with Trimesh confirms 21 scene geometries and 100,922 triangles. **No new/modified mesh is claimed**. Run208b binary is not available locally and has **not** been tested; this is deliberately the older rejected Run207b for a reproducible browser feasibility experiment.

In the preceding Run208b, both HTTP loopback and a Chromium SwiftShader attempt failed. This run performed a **new actual Chromium runtime diagnosis** on Debian Mesa/Xvfb: navigation to `data:` and loopback URLs was blocked by administrator policy, while `page.set_content` succeeded. Tried four different Chromium GPU configurations in both headed and headless modes: ANGLE/SwiftShader and default WebGL flags returned a real `WebGL 2.0 (OpenGL ES 3.0 Chromium)` context; the desktop EGL mode did not. This identifies why treating blocked navigation as a model failure would be wrong.

Then implemented and **executed** a minimal native WebGL2 glTF 2.0 binary parser/renderer, not a screenshot impostor: parsed the **actual original GLB bytes** into glTF accessors/bufferViews, uploaded POSITION/COLOR_0/index buffers to actual WebGL2 vertex arrays, compiled GLSL ES 3.00 shaders and submitted indexed GPU draw calls with depth testing. Captured five independently positioned camera screenshots (front/back/left/right/quarter) from actual Chromium canvases; opened front and back visually. Runtime reported:
- GLB 2.0, 21 meshes, 41 accessors
- WebGL2 context created **true**, GLSL shaders compiled, 21 indexed draw calls, 100,922 triangles
- `gl.getError() == 0`, zero page exceptions
- Measurable non-background pixels at all five views: front 37,575; back 40,319; right 31,798; left 31,806; quarter 31,019
- Rendering: Chromium headless + Xvfb + ANGLE **software SwiftShader**. This is **not a hardware GPU performance benchmark**, **not an Android/iOS browser test**, and **not mobile acceptance**.

## Visual findings and gate

Actual browser front screenshot still shows stiff raised decorative heart applique, black toy-like bead eyes, straw/needle-like short fuzz and tubular unsupported tree-hollow rim. Browser back still shows generic fluffy egg anatomy and lacks authored feather tracts, wing anatomy and natural surface relief. The apparent continuous posterior mesh is not evidence of photorealistic down. Thus **WebGL2 technically draws the original rejected asset but art remains decisively unacceptable.** Tested version is Run207b, not Run208b; no v3 sample is approved, exported for publication or deployed.

**Decision: SOFTWARE_WEBGL2_TECH_PASS / ART_REJECTED / NO_MOBILE_HARDWARE_GATE / NO_RELEASE / NO_NOTIFICATION.** Do not promote the WebGL result to a high-quality 3D character claim.

## Source/asset exploration

Checked current public free model leads: a CC0 high-detail Great Horned Owl released 2026-09-28 (Grab3D) is an **adult tufted owl with 400k–800k triangles**, not a suitable juvenile face/down source; an ArtistFrog baby-owl sculpt (CGTrader, 2020) remains behind the previously verified HTTP 403 download blockage and has a commercial **"no AI"** license condition; the CC0 BlendSwap 2009 owl is an adult rigged asset with Blender Internal-era fur and is not an age-unknown cream mesoptile. None was downloaded or represented as a source-derived juvenile. No paid/free trial credits spent. Published sources:
- https://grab3d.com/models/animals/owl/
- https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt
- https://blendswap.com/blend/7951

## Evidence inventory and storage boundary

Local run ZIP: `owl172_run209_WEBGL2_software_evidence_ART_REJECTED_NO_RELEASE.zip`
- Length: **3,604,907 bytes**
- SHA256: **`7434b89efdf2d2796e037bb48eeb9312610659b416186417dc9ecee76e021cd0`**
- Payload: unchanged original GLB; Chromium probing script and 8 probe results; a runnable native WebGL2 glTF parser/render test; embedded original GLB HTML; five genuine native WebGL2 PNG views; a five-view contact sheet; JSON results; per-file reproducibility SHA256 manifest. Audited **12/12** payload hashes and byte counts by re-opening the ZIP (13 entries incl manifest).
- Not a GitHub Actions artifact and **not persisted in GitHub**; only this audit text is committed here. Actual attempted persistent Library `/Owl172-3D-Research/Run209` create and ZIP upload both returned `AccessDeny`. Do not claim durable off-session ZIP retention.

## Isolation and next priority

Research branch created from exact Run208 HEAD `fc1f1c4be6f8131293aecada7b046271c17d3aab`; mutation scoped to this single #172 audit file. No edits to `main`, the 251-species pipeline, owl-pet prototype, production assets, deployment or user-facing viewer. **Next high-value art step** is obtaining legitimate artist-grade young Tyto base anatomy plus groom/materials, or a true multi-view reconstruction source. This WebGL technical fix makes later GLB browser evaluation feasible, but cannot substitute for aesthetic quality or a real smartphone GPU check.
