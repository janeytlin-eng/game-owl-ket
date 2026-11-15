# Run83 — #172 *Tyto castanops* v3: organic facial feather ruff, wing covert relief — **ART_REJECTED**

**Date:** 2026-11-15 Asia/Shanghai. **NOT a publishable or deployable 3D pet. No quality pass, no paid tool use.**

## Required repository and prior-art inspection

Re-read the current `main` owl-pet `AGENTS.md`, `README.md`, `STATUS.md`, `knowledge/ANATOMY_AND_POSTURE.md`, existing `prototype/index.html`, `research/species/172-tyto-castanops-v3.md`, v3 review, and Run79–Run82 rejection audits. The installed prototype is the old cat WebGL/SDF example, **not** a validated owl-pet model. The owner v3 visual is **one frontal concept of age-unknown cream mesoptile**: no scientifically validated exact age, no trustworthy right/rear three-dimensional anatomical reference. Run82's actual Blender GLB and original Cycles four-view archive were downloaded, unpacked and visually inspected, rather than relying on its written report alone.

The Run82 improvement to continuous head/torso removed a floating hard face plaque but turned the bird into a hanging egg/teardrop; the hallmark heart facial ruff was nearly invisible. Prior growing more needle/card down or sculpting hard face/wing ornament failed visual acceptance.

## Actual zero-cost Blender experiment

Created a **new independent branch only**, [`research/owl172-run83-organic-ruff-wingdown`](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run83-organic-ruff-wingdown), from `main`. Added separate [complete Blender 4.0.2 source](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run83-organic-ruff-wingdown/owl-pet/3d-experiments/172-tyto-castanops/tools/run83_blender_organic_ruff.py) and [dedicated workflow](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run83-organic-ruff-wingdown/.github/workflows/owl-pet-172-run83-organic-ruff.yml). Free Ubuntu GitHub Actions installed system Blender 4.0.2, actually constructed/exported/reimported a **real 3D GLB**, and rendered four original 640px Blender Cycles angles — frontal, three-quarter, strict side, back.

Changes against Run82's genuinely continuous loft skin: deeper **integrated** heart-face contour relief (not a separated rigid shield), alternate face/ruff materials, 240 pairs of real surface-conformal tapering facial fringe strips, seven rows of short wing-covert ridges on each lateral flank projected by mesh ray casting (not detached ellipsoid wings), and 11,400 curved cream-down polygon guides. No SVG or 2D-only mockup. A first workflow trigger was cancelled by concurrency during a filename correction; the final [GitHub Actions run **43712550676**](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43712550676) **completed successfully**. Workflows succeeding means the modeling tools ran, **not** that character art passed.

**Exact final GLB**: `owl172_run83_organic_integrated_face_ART_PENDING.glb`, **2,281,844 bytes**, SHA256 `08de41c64bcba2586fc38526a9d97c2fce7917eec2b084ea1f87cf69eeca756d`; independently reparsed as **44 GLB geometry primitives, 68,104 final triangles, 75,822 vertices**, no near-zero-area triangles at inspection tolerance. The earlier Blender-side 64,456 mesh polygons are **not** the exported final triangle count. Only one primitive was individually found watertight; **do not certify whole-body manifoldness or rigging**. Four original Cycles views and successful import/export build log are retained with the GLB.

## Actual browser draw, not physical mobile certification

Extracted original Run83 GitHub Actions ZIP, passed ZIP CRC, reopened the actual GLB in `trimesh`, and rendered its original transformed triangles/normals/material-color approximations in real desktop **Chromium WebGL2** on SwiftShader/Xvfb. First test navigation failed by local browser admin restriction; corrected by injecting the binary GLB-derived buffers into standalone page HTML rather than fetching localhost. Result: **eight actual successful WebGL2 draws**, four orientations at both 800×800 desktop and **390×600 simulated mobile** viewports, zero WebGL errors and zero page/JavaScript exceptions. This is **not** the reference-standard glTF PBR renderer, physical smartphone GPU/touch/thermal, measured on-device FPS, skeleton/animation or app acceptance.

## Four-view visual review — **REJECTED**

Against the original cream juvenile crop, Run82 baseline render and real Run83 Cycles/WebGL screenshots:

* The facial ruff is more legible frontally but individual geometric strips read as **a conspicuous repeated comb/tooth ring**, not a seamless, velvety heart-shaped Tyto feather transition. The attempted fix creates a **new severe decorative artifact**.
* Side wing covert strips read as hard repeated parallel scoring/streaks rather than a down-buried, anatomically credible juvenile wing. Side/back remains essentially rounded egg anatomy, still missing actual supported scapular/wing-fold geometry and concealed tail credible from multiple directions.
* Cream body down is spiky and mottled under software WebGL rather than dense soft second-down; eyes stay black toy-like discs, face lacks natural embedded brow/orbit and beak transitions; feet still appear inadequately attached/supported on a stylized flat ledge.
* Front is not sufficient to validate the anatomically unsupported side/back. No actual smartphone GPU, full PBR, animation, FPS or energy budget evidence.

**Decision: ART_REJECTED.** Do **not** publish, link as a successful sample, deploy, or mistake a free CI pass for art acceptance. Repeated hard geometry ornaments and ever more down polygons are a failed route; future work should focus on genuinely sculpted head-orbit volume and smooth feather-shader/groom transitions, properly licensed juvenile side/rear references and full mobile/WebGL QA.

## Artifact retention and exact limitations

The workflow **actually committed nine original negative proof files** — actual GLB, **four Blender Cycles PNGs**, original build/reimport log, metrics, GLB hash and explicit `NOT APPROVED` marker — into [the isolated branch's `uncertified-binary-run83` directory](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run83-organic-ruff-wingdown/owl-pet/3d-experiments/172-tyto-castanops/uncertified-binary-run83). GitHub contents were independently re-read: the GLB is 2,281,844 bytes; the four PNGs are 561,826, 553,473, 525,370 and 531,204 bytes. The branch-vs-main file comparison showed **only 11 isolated files**: standalone workflow, standalone model source and nine archive files. This is **durable remote negative evidence**, not visual release approval.

A fuller **27-file local evidence ZIP** includes the real model and Blender views, eight real browser screenshots, 2 contact sheets, original logs, independent QA scripts/reports and SHA256 manifest. ZIP: `owl172_run83_ART_REJECTED_full_evidence.zip`, **5,242,326 bytes**, SHA256 `a8c20c039051155f8d972c20089bd096076b46ec4a4551338826e1c7331cb480`. Local ZIP CRC and 26/26 per-file SHA256 checks passed. **This extra full ZIP/browser evidence has NOT been remotely archived:** Files Library folder creation and upload returned `AccessDeny`; attempted Google Drive connector handoff from the GitHub Actions artifact returned `BLOCKED_FILE_REFERENCE`. Only the original nine GitHub research-branch files are independently proven durable. Actions downloadable ZIP is subject to temporary retention, not a durable alternative.

**Isolation:** No extra paid credits, no modification to the 251-species production process, source concept plate, species manifests, existing cat WebGL prototype, root vocabulary game or live Sites deployment. The present standalone main-branch record is the only main change.