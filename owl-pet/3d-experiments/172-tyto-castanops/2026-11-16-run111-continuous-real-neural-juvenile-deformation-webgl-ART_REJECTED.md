# #172 *Tyto castanops* v3 — Run111: real neural juvenile silhouette deformation + live browser GLB QA — ART_REJECTED

**Executed:** 2026-11-16 (Asia/Shanghai, 22:58–23:04). **Strict status:** ART_REJECTED / NO PET SAMPLE / NO PRODUCTION CHANGE / NO EXTRA PAID TOOL.

## Preflight: repo, target and previous attempt reviewed

Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/STATUS.md`, the authoritative `owl-pet/research/species/172-tyto-castanops-v3.md`, Run110's complete audit, its native four-angle rendered contact sheet, previous Run92C sculpt failure, and Run102B's software WebGL harness. Repo's `prototype/index.html` is still the old unapproved *cat* prototype; the 251-species concept pipeline must not be touched.

The target is specifically the right-hand **age-unknown cream second-down mesoptile** in `owl-pet/design/concepts/172-tyto-castanops-v3.png`, not an adult owl. Its design contract is a wide heart-shaped disc, fully open dark eyes, small bill, squat and down-soft body, extremely short down-veiled wing, no visible tail, and belly and both feet on a wide senescent eucalypt hollow lip. The reference cannot scientifically determine exact side/rear morphology or age. Run110 improved eye openness but produced narrow face relative to body, a long horizontal wedge in profile, scaly coarse feathers, and bare unsupported toes.

**Actual prior GLB input:** Run110's `run110_eyes_plus_softdown_ART_UNAPPROVED.glb` (3,292,496 bytes, SHA256 `604217f513c6e04f8f7d29ba17a418836a33fafe6d6e8fe3b5571b21da09a7c6`), itself derived from the real Run99 Hunyuan neural reconstruction, NOT a procedural sphere/egg or 2D image. This experiment must **not** erase source rights constraints.

## Actual one-run experiment and corrected technical failure

- Dedicated branch: `research/owl172-run111-juvenile-silhouette-warp-webgl-qa` from Run110 branch, not `main`. Reproducible native Blender implementation: `tools/run111_true_neural_juvenile_deformation.py`; live Three.js GLTFLoader viewer `tools/run111_viewer.mjs`; Playwright Chromium runner `tools/run111_software_webgl_qa.mjs`; exact isolated workflow `.github/workflows/owl-pet-172-run111-real-juvenile-warp-webgl.yml`.
- First real [Actions attempt](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43891498920) **failed at Blender glTF import**, because the GitHub runner's Blender 4.0.2 system Python lacked `numpy`. This is preserved in that job log, `actual_blender_run111.log`, and the first failure archive. The overall workflow is marked success **only because failure-archive steps deliberately ran under `if: always()`**. It is **NOT** evidence of a generated model.
- Fixed dependency with `python3-numpy`, then **actually reran** on free Ubuntu Actions: [second run 43891772698](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43891772698). Blender generation, 8 Cycles rendered views, explicit GLB fresh reimports, browser, checksums, and restricted evidence commit all ran successfully.
- Input 8 mesh parts / 127,262 real triangles. Applied continuous nonrigid vertex deformation to **every original 3D mesh vertex** including existing eye parts and 2,500 surface-sampled feather tufts: shortened lower trunk, widened upper head at two strengths (+20% / +34% Gaussian envelope), gently reduced elongated profile and added small front-geometry cheek relief. Preserved input polygon topology and material indices; never swapped in an invented primitive, 2D card portrait or flat face sticker. This is an **ablation**, not a new anatomically crafted owl.
- The two variants both independently exported **real binary glTF** and passed a brand-new Blender 4.0.2 import with exactly **8 meshes / 127,262 polygons**:

| Actual artifact | Bytes | SHA256 | Body bounds (x/y/z, imported coordinate units) |
| --- | ---: | --- | --- |
| `run111_juvenile_compact_20_ART_UNAPPROVED.glb` | 3,508,148 | `3b7b426f8cc1037f24948e9c0945e8b55877bc0ee5f95c55555b56fb9c5a529b` | 1.677 / 1.777 / 1.757 |
| `run111_juvenile_broadface_34_ART_UNAPPROVED.glb` | 3,508,232 | `c755adfdea0d54e8de5588d72593009162d799ec2a97dec2026cc1efe613a886` | 1.733 / 1.777 / 1.757 |

Input body bounds were 1.540 / 1.948 / 1.898; values describe actual imported meshes rather than biological measurements. Eight native Blender Cycles renders: front, quarter, strict side and back for **each** independent variant. Two 880×880 genuine four-angle contact JPEGs made from the eight renders.

- Chromium loaded the **actual new broadface GLB** using Three.js `GLTFLoader`, not a fake preview or static PNG. Software WebGL2 (Chromium SwiftShader) at 1280×720 desktop **and simulated 390×844 phone viewport** loaded 8 meshes / 127,262 triangles with zero GL/page/app errors. Rendered 104 and 120 frames respectively; both viewport boxes stayed inside after a real orbit-drag interaction, and camera coordinates changed. Browser screenshots in `browser/` were actually opened and visually reviewed. **This is not a physical Android/iOS device or GPU FPS, touch, battery, shader-parity or thermal benchmark**.
- Research-only evidence directory: `research-evidence-run111-JUVENILE-NONRIGID-MORPH-ART_UNAPPROVED/`. It contains both GLBs, eight native PNGs, two contact JPEGs, desktop/simulated-phone screenshots, browser metrics, full run logs, measured dimensions, source SHA, checksum manifest, checksum validation, and explicit rejection flag. Every one of the **21** tracked evidence payloads returned `OK` in SHA256 validation. Exact original files are committed (not merely artifact pointers). See [successful action](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43891772698).

## Independent visual QA of actual renders — **reject both**

Opened the true four-angle Run110 baseline, both Run111 four-angle contacts, and the new real desktop and simulated-mobile software-WebGL screenshots. The front outline is visibly broader and more squat, and the eyes remain genuinely open in 3D. This is a **measurable and visible proportion improvement**, but not a correct baby owl.

**Disqualifiers:** The broad heart-shaped facial disc is still a relatively small hard embossed bowl surrounded by an oversized crown, not the integrated feather-soft heart of the right-hand target. The owl still has a pronounced long backward horizontal wedge at a strict side view, underdeveloped short-wing anatomy and undefined hidden tail, coarse flake/pinecone-like back and spiky rather than fine cream second-down. The feet are large and bare-looking; the body and both feet lack the required supporting eucalypt hollow lip. Face and beak anatomy are too schematic and asymmetric for a professional juvenile. Browser lighting exaggerates a plastic facial disc. Side/back mismatch and incomplete anatomical detail remain.

**Neither variant merits user-facing sample notification.** Proof that GLB loads and orbits in software WebGL is not art acceptance. Initial Run111 workflow success must never be mistaken for Blender success; the second run is the only successful asset build.

## Actually explored free/source alternatives (not represented as obtained meshes)

Checked a newly listed [Grab3D CC0 high-detail horned owl](https://grab3d.com/models/animals/owl/) (claimed CC0, 800k-triangle, ~31MB GLB, 4K textures) and [a public-domain barn owl museum model](https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc) (~262k triangles, CC0 stated). Both may be genuine third-party **adult** anatomy donors but are not a credible *Tyto castanops* downed juvenile by direct substitution; no external files were downloaded or distribution rights independently revalidated here. A [young masked owl photograph](https://www.lukeobrien.com.au/young-masked-owl-raptor-refuge) corroborates that juvenile down can have complex fine fibers; it was not used as a texture or redistributed. Future use requires source verification and actual multi-view appraisal, not faith in license snippets.

The free TRELLIS service's last recorded ZeroGPU allowance at UTC 11:42 Nov 16 indicated a roughly 7-hour reset, so this run deliberately avoided quota-bypass or repeated unavailable inference. All work used only existing research GLB, free Blender, Three.js, Playwright and GitHub-hosted Actions. No paid account or subscription was triggered.

## Scope and required next gates

Branch comparison **from Run110 to Run111** shows only 28 paths: this audit, one dedicated workflow, four Run111-only tools, and quarantined Run111 evidence. **No** 251-species producer, design manifest, species source concept, cat prototype, root vocabulary game or live site was changed. This scoped comparison does not pretend the inherited historical research branch has zero other legacy differences from main.

Next viable quality jump requires **new licensed anatomical head/body sculpt** (not just additional global vertex scaling), the actual soft second-down layer and short concealed wing with believable lateral/back profile, plus a broad hollow-lip environment and genuine iOS/Android hardware performance. Tencent/Hunyuan source globally distributable output rights remain uncleared. The run cannot cross the mandatory quality and license gates without those assets and validations.

**FINAL: two genuinely reopened three-dimensional GLBs, 8 Blender renders, two successful browser software-WebGL probes, complete SHA256-checked quarantine, visibly improved squat front, STILL ART_REJECTED / NO USER RELEASE.**
