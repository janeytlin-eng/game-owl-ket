# #172 Tyto castanops v3 — Runs125/125B: real free baby-owl model source checks

**2026-11-17, ART_UNREVIEWED / NO_RELEASE. No new 3D model approved, no new payment, no 251-species production changes.**

## Input / safeguards
Independently re-read existing owl-pet README and AGENTS, #172 target and Runs 122–124E, starting from prior evidence commit `b5da5ee59f0b4053aafcde0e192aa7d1d58b76ee`. The target is the **rightmost cream-white downy juvenile** with a coherent heart-shaped facial disc, small dark eyes, short underdeveloped wings, correct side/back morphology, natural tree-hollow support, true soft fur and mobile WebGL performance. The rejected previous sphere-like or adult feathered meshes cannot be relabeled as complete.

## Run125 — real remote tool-assisted source catalogue examination
Actual zero-dollar network and metadata probe executed in [GitHub Actions run 44001279234](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44001279234). Code: `tools/run125_independent_chick_source_access.py`.

Eight requests and byte-magic classification:
- BlenderKit public API: **3 baby-owl** results (`baby owl`) and **10 barn-owl** results (`barn owl`), zero `owlet`. Thirteen query-matched response rows all explicitly return `isFree=false` under their royalty-free BlenderKit terms; some are duplicates across queries. In particular `Baby Owl Animated`, `Baby Owl Animated Black` and `Owl Baby Animated` are on-target title candidates but **not free**, and **not tested 3D**. Did not attempt billed download.
- BlendSwap `Baby Owl Character`, by **drothenbucher**: [public listing](https://blendswap.com/blend/11643) HTTP 200 HTML, publicly listed **CC BY**. No geometry at the metadata URL. This was a new artist-chick route worthy of an official download test.
- Other targets: BlendSwap owl catalogue HTTP 200; OpenGameArt public query HTML 200; Poly Haven metadata API HTTP 200 but matches for `owl` were only false-positive `wooden_bowl` names; Printables barn owl listing HTTP 403 in runner (a separate public listing indicates CC BY-NC-ND, incompatible with derivatives).
- **0/8 endpoints returned GLB, BLEND, or ZIP model bytes.** All source requests, headers, redirect destinations, SHA256 and parsed model metadata are archived, not interpreted as assets.

## Run125B — actual artist-provided free-download link, not fabricated CDN URL
Actual artist-page inspection executed in [GitHub Actions run 44001515197](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44001515197) via `tools/run125b_blendswap_public_artifact_probe.py`.

The official [Baby Owl Character listing](https://blendswap.com/blend/11643) returned HTTP 200, exposing **93 HTML anchors**. Parsed the exact official **Download** anchor, `/blend/11643/download`, then made a real unauthenticated GET to [the official download action](https://blendswap.com/blend/11643/download). Result: **HTTP 403, 5,606 bytes, HTML**, not a Blender file. Did not guess a signing URL, bypass authentication or purchase. The child has not been visually or geometrically reviewed; the publicly displayed CC BY does not establish its suitability for this particular Tasmanian masked owl.

## Strict scope, evidence and decision
The two independent `research-evidence-run125*` directories include actual execution logs, machine-readable source observations, failed access classifications, NO_RELEASE flags and **passing SHA256 manifests**. The GitHub job logs returned `probe_step=success` and `access_step=success`: **successful probes, not successful modeling**. No GLB/BLEND acquired in either experiment; accordingly **Blender reimport, native four-angle render, mobile Three.js or physical phone GPU tests were NOT performed**. No image or HTML preview is claimed to be real 3D. There is no deliverable to show.

Research branch: `research/owl172-run125-juvenile-artist-source-blenderkit-blendswap`. Changes relative to Run124 baseline remain exclusively in dedicated `.github/workflows/owl-pet-172-run125*.yml` and `owl-pet/3d-experiments/172-tyto-castanops/**`. Original v3 PNG, 251-species production flow, owl-pet prototype, main branch and deployed app all remain untouched. Cost $0.

**Next meaningful gate**: obtain a genuinely accessible independently sculpted juvenile Tyto-like mesh under clearly reusable license; only then proceed to native four-view Blender dissection/sculpt, controlled mobile GLB LOD and actual phone GPU checks. Avoid repeating edits to adult horned-owl sources or snowball/flat-mask proxy meshes.
