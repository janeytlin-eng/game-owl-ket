# #172 *Tyto castanops* v3 — Run113 / Run113B real 3D source suitability, LOD and software-browser experiment — ART_REJECTED

**Date:** 2026-11-17 Asia/Shanghai. **Art gate:** ART_REJECTED. **No target juvenile sample, no deployment, no purchase.**

## Actual preflight and source selection

Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, the full Run112 audit, Run112 Blender workflow/source and original **full 1536×1024 v3 concept PNG** at `owl-pet/design/concepts/172-tyto-castanops-v3.png`. Previous Run110–Run112 used a genuine Hunyuan neural 3D surface but repeatedly failed on an overlong side/rear, plastic heart mask, scaly rather than downy surface, short-wing anatomy and unsupported feet. The target is **right-hand cream, soft-mesoptile compact juvenile with open dark eyes and large feathered heart disc, resting on the lip of a mature eucalypt hollow**. Not either adult.

Instead of another blind smooth/warp of the rejected neural source, actually **downloaded and imported a separate textured 3D animal asset** to test (a) legally claimed CC0 provenance, (b) true multi-view anatomical integrity, (c) real textured-mesh LOD reduction and (d) a no-charge mobile-viewport GLB/WebGL technical path. The benchmark source is conspicuously an **adult GREAT HORNED OWL, not Tyto or a chick**. It was never presented as a #172 candidate.

- Provider source: https://grab3d.com/models/animals/owl/ (free, no login).
- Exact GLB: https://grab3d.com/dl/owl/owl-light.glb, actual download **13,356,032 bytes**, SHA256 `fdcd83d53a5346eac8259a861614f5adae46ce7ad11e33919d05dd1bcd52aaba`.
- Archived original terms and manifest: https://grab3d.com/dl/owl/LICENSE.txt and https://grab3d.com/dl/owl/manifest.json. Provider claims CC0 1.0, **explicitly discloses an AI-assisted Meshy origin**. The provider's claim was recorded, but rights to globally redistribute every upstream ingredient were **not independently established**. Do not market this as cleared final pet art.
- No additional paid tool, subscription, account switch, credit bypass or license workaround.

## Actual Run113, free Blender 4.0.2

Run113 source code: `tools/run113_real_cc0_owl_anatomy_lod.py`. New isolated push workflow: `.github/workflows/owl-pet-172-run113-free-cc0-3d-source.yml`.

- [Initial execution #43911283212](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43911283212): actual source downloaded and SHA recorded, then Blender's glTF import failed with **`ModuleNotFoundError: No module named 'numpy'`**. Not claimed as success; original Actions log remains the failure evidence.
- Installed `python3-numpy` / `python3-pil` alongside free Blender and re-executed [Run113 #43911693725](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43911693725): actual source import and **all 8 native Cycles real-mesh orbit views** succeeded, with original textures/material intact.
- Real original GLB: **399,999 triangles**, 1 mesh, 1 material, two 1024×1024 texture images, bounds around 0.288×0.321×0.550 m. Decimated native topology with Blender to **91,999 triangles** (77% fewer), exported **4,155,740 byte GLB**, SHA256 `66eae3597240b9c02e7b27be57c7f5b7556ff8d68d30cdc43fea83d184832f17`; separate Blender fresh GLB import recovered the same 91,999 triangles. This is a **real adult bird mesh**, not spheres/SVG/2D view tricks.
- Actually inspected the native front, strict side and back raster renderings and compared to the concept plate. Adult ear tufts, brown barred feathers, prominent adult wings/tail, exposed legs/claws, sharply adult silhouette: intact from several real 3D viewpoints, but totally incompatible with the cream downed, small-winged, short-bodied **Tyto** mesoptile. Some native Cycles views are slightly overexposed under research lighting; this is no art-quality certification.
- Output archived under `research-evidence-run113-REAL-CC0-ADULT-LOD-ART_REJECTED/`: LOD GLB, eight real native PNG renders, metrics JSON, original source SHA and manifest, license disclosure, execution logs, ART_REJECTED flag and SHA256 manifest. Original large source GLB remains at the verified provider URL; no redundant original mesh was claimed as separately committed.
- Run113 evidence SHA256 check: **18 actual evidence payloads passed**; workflow completed and archived successfully.

## Actual Run113B, real Three.js loaded GLB

Source: `tools/run113b_cc0_adult_lod_webgl_qa.mjs`. New dedicated workflow `.github/workflows/owl-pet-172-run113b-real-cc0-webgl-qa.yml`, against the exact 4,155,740-byte GLB and locked SHA256 above.

- [Initial browser attempt #43912198414](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43912198414) exposed an ESM module resolution error (`ERR_MODULE_NOT_FOUND: playwright`) because the QA script lived outside the npm directory. Recorded in original run's Actions log; fixed by copying QA into the browser workspace, not by pretending first attempt passed.
- [Corrected Run113B #43912495505](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43912495505) **really loaded** the 91,999-triangle textured adult GLB with Three.js `GLTFLoader` in Chromium WebGL2 on 1280×720 desktop and 390×844 simulated iPhone-style viewport.
- Both tests: **1 actual mesh, 91,999 triangles, in-frame before/after orbit interaction, orbitMoved=true, glError=0, no application or page errors**. Independently inspected the desktop and simulated-mobile *real browser screenshots*: the original adult horn tufts, yellow eyes, brown mature feathers and long folded wings are clearly visible; not the target chick.
- **Software SwiftShader only**. iOS/Android physical GPU, performance/FPS thresholds, touch response, battery/thermals, animations and publish rights are **NOT validated**. The technically passing adult benchmark is still **ART_REJECTED** as juvenile art.
- Run113B evidence under `research-evidence-run113B-CC0-ADULT-WEBGL-ART_REJECTED/`: actual desktop and phone-viewport screenshots, QA JSON/log, ART_REJECTED, checksums; **7 actual evidence payloads passed**.

## Further no-charge source check

An apparently more relevant `Baby Owl Animated` / `Barn Owl Kid` with 26 claimed animations was located at https://www.blendkit.com/asset-gallery-detail/af064619-74d4-496f-bdde-bdc742e08824/ but **is explicitly marked Full Plan** on its listing, so did not download/purchase or assume permission. A museum CC0 barn owl adult taxidermy model and very-low-poly free Tyto/other models likewise do not solve this specific downed juvenile sculpt. Do not silently substitute adult/taxonomically unrelated assets merely because they have a licensed GLB.

## Branch integrity, blockers and next viable route

Run113/113B branch: `research/owl172-run113-cc0-real-mesh-mobile-lod-source-audit`, based on isolated Run112 research, **not main**. Before this audit, GitHub compare against Run112 showed exactly **33 changed paths**, all inside the isolated `owl-pet/3d-experiments/172-tyto-castanops/` research directory or the two new `.github/workflows/owl-pet-172-run113*` one-off workflows. No edit to the 251-species concept producer, original #172 design plate, old electronic-pet prototype, vocabulary game or deployed site. Zero new spending.

This experiment establishes a real PBR animal-mesh -> Blender LOD -> genuine WebGL2 pipeline under controlled free tooling, but **does not advance the desired owl chick's actual anatomy enough to release a sample**. This finding prevents misrepresenting an attractive adult owl as the juvenile. Source search and original mesh inspection should next focus specifically on a rights-cleared young *Tyto* body/face that genuinely matches the broad downy heart shape and short-winged compact silhouette; otherwise independent handcrafted high-quality juvenile sculpt/feather grooming is required. The original Hunyuan neural source global licensing and actual phone hardware tests remain open.

**FINAL: ART_REJECTED. No user-facing 3D pet sample link, no production modification, no notification.**
