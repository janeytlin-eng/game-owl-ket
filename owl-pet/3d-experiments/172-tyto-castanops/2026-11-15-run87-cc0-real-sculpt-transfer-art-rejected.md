# Run87 — public CC0 organic owl 3D transfer experiment for #172 *Tyto castanops* v3 — **ART_REJECTED**

**2026-11-15 Asia/Shanghai**. Experimental research with genuine binary GLBs and native Blender rendering, **not** a quality-approved cream mesoptile 3D pet, and **not** a releasable sample. **Do not show as a working pet, deploy, or mark user art approval.**

## Prerequisites and fixed design boundaries

Rechecked main `owl-pet/README.md`, `AGENTS.md`, `prototype/index.html` (old unrelated cat WebGL), relevant #172 v3 species design `research/species/172-tyto-castanops-v3.md`, original full-size `design/concepts/172-tyto-castanops-v3.png` (specifically **rightmost** cream mesoptile) and Run85–Run86 failed 3D audits, with earlier failure patterns also considered. V3 intentionally does **not** assert chick's exact developmental age, side/back plumage details or nest interior. The design target is thick soft cream down, a naturally feathered tan heart-shaped disc, dark eyes, a compact supported juvenile, down-concealed wings and tail and two supported feet.

Run86 already proved that more synthetic needle-like feather guides or procedurally deforming the same pear shape does not reach desired quality. To change the underlying sculpt and asset provenance, this run tested a **free download of genuine hand-authored textured owl 3D mesh** instead of further sphere assembly or SVG masquerading as a model.

## Run87A — actual external 3D asset toolchain and anatomical feasibility

Publisher [Innerscene's Owl GLB](https://www.innerscene.com/tools/library/3d-parts/owl-d696472a) states **CC0 / original Innerscene artwork**. This is a publisher license claim, not independently audited ownership. Zero paid inference, keys, services or purchases; actual source downloaded by Actions. The source is an **adult horned owl**, wrong taxon and developmental stage, so original asset is **SOURCE_ONLY_ART_REJECTED** and will not ship.

Successful free Blender 4.0.2 + NumPy Ubuntu Actions [Run87A 43723360895](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43723360895):
- Original 20,671,040-byte authentic `owl.glb`, SHA256 `c11c94db20065c6c6f252e768e8c748f22dc69ef9b4e7199110b96de0625c12e`.
- Actual import 129 mesh objects, 62,592 triangles, 14 materials with image textures, no animations; geometry source bounding box 0.408×0.212×0.513m. Main source mesh is **open**, not watertight.
- Rendered **8 real 540×540 Blender Cycles native turntable views**, exported and reimported GLB (20,670,772 bytes, SHA256 `d100dd0a10184d93bafa5e0c9647f1ac7d49405d8f67240f6355a7d8d516c498`) preserving 129 objects. Original binary, reimported binary, all 8 views, topology/material audit JSON and logs **persisted and re-read** in dedicated branch [Run87A source-only evidence](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run87-cc0-organic-base-audit/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run87-CC0-SOURCE-ONLY).

First action [43723231295](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43723231295) failed because packaged Blender Python lacked `numpy`; adding distro `python3-numpy` fixed it. This was a real installation/import failure, not aesthetic success.

## Run87B — true 3D mesh retarget (not merely a plan)

In a new [Blender actual sculpt/transfer source](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run87-cc0-organic-base-audit/owl-pet/3d-experiments/172-tyto-castanops/tools/run87_cc0_mesh_retarget.py), imported 20 MB fully modeled owl, removed **70 adult features** (adult long primaries/covert details, tail and tufts), deformed the **remaining genuine 3D authored vertex mesh** towards a compact wide-head juvenile with short embedded wing buds and shortened beak, and added a pigment-based softly displaced front facial region on the artist's original continuous topology instead of a floating face mask mesh. Reimported final genuine binary GLB in Blender. Do not mistake one head pigmentation pass for a professionally groomed Tyto heart disc.

Successful final free Actions [Run87B 43724422997](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43724422997) generated:
- Binary **17,079,204 bytes**; SHA256 `cbbca8d70d8a8b83639d927096e9302be9d49b8dbae81cd5726cebca753db253`.
- Independent Python `trimesh` GLB parse: **59 meshes, 48,312 final triangles, 30,171 vertices; 0/59 individually watertight meshes**.
- **4 original Blender Cycles 600×600 actual views** (front, three-quarter, strict side, back), all inspected, plus original Blender reimport 59 mesh objects, source/GLB checksums, full build log and machine metrics.
- Evidence **saved durably and re-read** in [Run87B research binary and native image archive](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run87-cc0-organic-base-audit/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run87b-ANATOMY-TRANSFER-UNAPPROVED), with [independent four-view and geometric rejection audit](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run87-cc0-organic-base-audit/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run87b-ANATOMY-TRANSFER-UNAPPROVED/INDEPENDENT_VISUAL_AND_GEOMETRY_QA_ART_REJECTED.md).

Run87B earlier two Actions failed at (i) incorrect Blender-visible source mesh object name, corrected to verified `Continuous anatomical skin | owl`, and (ii) archived binary `git add` excluded by sparse-checkout, corrected using `git add --sparse`. The final workflow succeeded for **both actual modeling and durable branch-only evidence**. Distinguish machine outcomes from art quality. `textures_tinted=[]` in the machine metrics means attempted automatic texture recoloring matched zero image names; **do not claim successful 2K albedo recoloring**.

## Actual visual comparison and independent negative gates

**ART_REJECTED.** In frontal real Cycles image the skull remains a flat, wide rectangular/capped horned-owl form, eyes stern and adult-like and face shading reads as a smiling chevron/chin patch, **not** a continuous feathered Tyto heart. Profile still exposes a rigid paddle-like short wing, slender adult raptor tarsus/claws, unnatural belly angle and hooked adult bill. Rear is an almost featureless symmetrical barrel with repetitive stamped-scale texture, not cream down or correctly layered juvenile feathers. Does not sit naturally in a wide hollow lip. The source's original hard 2K feather skin survives the retarget and **does not form natural soft down**. Retarget did not solve wrong taxon, age, surface groom or grounded support.

Mobile quality **not passed**: even though Blender imported/roundtripped real glTF 2.0, the 17.08 MB GLB has no proven physical-phone WebGL GPU, standard PBR renderer/material parity, animation, FPS, touch or thermal benchmark. A local independent Chromium normal-lit smoke attempt from the actual GLB was **blocked at file/localhost navigation by `ERR_BLOCKED_BY_ADMINISTRATOR`**, so **no positive WebGL2 drawing result is asserted** for this run. Passing Blender GLB import is insufficient for mobile deploy. No actual app is built or updated.

## Evidence and noninterference

All Run87A/B GLBs, actual Blender renders and logs exist durably in **isolated** research branch `research/owl172-run87-cc0-organic-base-audit`; provenance and negative QA remain clearly marked `NOT_APPROVED`. Workflow action artifacts are extra temporary 14-day proofs, not the sole archival source. Research scripts, branch-local unique action workflows and proof files are the only changes in `main...research/owl172-run87-cc0-organic-base-audit`, as confirmed by GitHub compare. **No changes to 251-species production workflow, concept and manifest, root vocabulary game, original old cat WebGL pet, live site or paid tools.** Main receives **this text-only rejected technical audit**. Follow-up direction is a *genuinely age-appropriate Tyto head/wing/feet sculpt and layered fluffy groom* with supporting real side/back photo references, rather than automatically recoloring adult horned owl. No publishable model or user-notification threshold reached.
