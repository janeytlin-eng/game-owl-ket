# #172 Tyto castanops v3 rightmost downy mesoptile — Run120 independent no-charge source trial

**2026-11-17, Asia/Shanghai. Final: ART_REJECTED. Research evidence only. No approved sample, no deployment, no purchases.**

## Preflight
Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, the real existing cat/WebGL prototype (`owl-pet/prototype/index.html`), `owl-pet/research/species/172-tyto-castanops-v3.md` and Run119's actual failed 3D down-groom audit. Original target is the **rightmost** age-unknown young Tyto: **integrated wide heart-shaped facial disc, dark open eyes, dense cream-white second down, compact short-winged body, no remiges or visible tail, both feet and belly supported on a senescent eucalypt hollow lip**. Prior TRELLIS/Hunyuan/InstantMesh 3D seeds failed mainly on adult-like side/back, hard wing feathers and damaged facial geometry.

## What actually ran
Instead of yet another TRELLIS recolor, tested a **separate publicly downloadable 3D source** from the Innerscene parts library (listing: https://www.innerscene.com/tools/library/3d-parts/owl-d696472a). The vendor webpage **claims CC0** and calls it an original owl model, but upstream authorship and redistribution rights have not been independently established. Its public on-page **Download GLB** endpoint `https://www.innerscene.com/api/library/owl-d696472a/download` was used without login, purchases, credit bypass or secrets; HTTP **302 -> 200**, 20,671,040 bytes, GLB magic validated, SHA256 `c11c94db20065c6c6f252e768e8c748f22dc69ef9b4e7199110b96de0625c12e`. The exact HTTP response headers, source hash and source rights limitation are in the evidence archive.

Run120 `tools/run120_artist_owl_source_qa.py` was executed with **free Blender 4.0.2** in a real GitHub Actions Ubuntu runner: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43968068634 . Blender imported **129 actual mesh objects** totaling **62,592 triangles**, made four native Cycles views (front, 45°, strict side, back), and exported `run120_independent_CC0_claim_source_LOD_ART_UNAPPROVED.glb`. The exported mesh was genuinely re-imported and measured at 62,592 triangles. Size **20,674,588 bytes**, SHA256 `8374afe09f40d94785738dd4ef790da4ab3a2c2f34bd71beaba29ad4d4581253`. Geometry was under the 95k LOD threshold, **so no decimation occurred**: this is a technical export/reimport control, not an optimized mobile LOD nor new sculpt. Real source dimensions approx 0.408×0.212×0.513 meters per Blender (provided scale not independently validated). No browser/real-phone GPU claim.

All four native 480×480 PNGs, a four-view contact JPG, full Blender stdout, source download metadata, true exported GLB, metrics JSON, no-release flag and hashes have been committed to `research-evidence-run120-INDEPENDENT-CC0-CLAIM-SOURCE-ART_REJECTED/`. **16/16 manifest-listed files passed SHA256 verification.**

## Decisive source-structure rejection — NOT an organic juvenile sculpt
The actual Blender glTF import log, not speculation about the generic name of the asset, lists:
- `Great horned owl continuous thick body neck and facial volume`: expressly **a great horned owl**, not a Tyto.
- **129 named mesh primitives**, including **36 `Sphere.*` entries**, six `Paired owl feather tuft, not an anatomical ear` entries, and 30 parts with `wing` in the mesh name.
- Repeated `Layered wing covert`, `Cambered folded wing foundation`, `Bare raptor tarsus` and `Curved tapered bird claw` objects.

This directly conflicts with the user's explicit rule **not to substitute a simple geometric assembly**, and with the required age-unknown thick-down **Tyto** chick without exposed wing remiges. This is a genuine loadable 3D model but **not** the correct anatomical asset or a credible high-quality #172 pet prototype. The native four-view images were generated; independent full-resolution human visual acceptance was **not** obtained in this run and is NOT implied. The log-level taxonomic and assembly evidence already makes this an unconditional **ART_REJECTED**. No new acceptable model, no user-facing sample link.

The 129 separate meshes and 20.67 MB payload also make phone draw-call count and texture/memory budgets uncertain. No real Android/iOS GPU WebGL measurement, interaction/animation, short-wing and bark-contact QA, soft-down transparency, or worldwide model redistribution clearance. There is no basis for publication or notification.

## Scope
Isolated branch `research/owl172-run120-cc0-independent-tyto-source-qa` derived from Run119; only the new dedicated Run120 workflow, new Run120 QA source, this audit and Run120 evidence folder have been added. Relative to Run119, prior to this audit exactly 20 changed paths, all under `owl-pet/3d-experiments/172-tyto-castanops/` or the dedicated `.github/workflows/owl-pet-172-run120-independent-cc0-source-qa.yml`. No 251-species original image production, concept plate, old pet prototype, main branch or deployed site changes. No additional payment.

**Decision: no release, no user notification.** This trial usefully closes off another apparently promising "CC0 original owl" source because its actual GLB is a different species assembled from named primitives. Future candidates must meet anatomical source identity and mesh-organicity gate *before* costly fur, browser or animation work.
