# Run98 — independent free rigged-bird 3D source examination — **ART_REJECTED**

**Date:** 2026-11-16 (Asia/Shanghai). **Release gate: ART_REJECTED. No model should be shown or deployed as the target pet.**

## Preflight and why this is a different experiment

Read existing `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, the #172 v3 species/review file, and Run92C/Run96/96B/Run97 failures before beginning. Target remains the **rightmost cream mesoptile** from the original #172 v3 three-bird concept, not its adults. Developmentally uncertain age is retained; no taxon-specific precise developmental week is fabricated. Required: plump cream second down, deep softly feathered heart disc, dark eyes, down-buried short wings, tail concealed, supported toes on an old eucalypt hollow, plausible lateral/back mass, true 3D mobile WebGL character.

Previous physically created GLBs and native renders failed primarily in art anatomy and grooming, not simply in glTF export. Run97 demonstrated that nonlinear width warping of a toy-like 220k-triangle sculpt worsened the silhouette. Run98 deliberately changes strategy to inspect **a real pre-rigged, independently authored source mesh and separate its possible animation value from its art suitability**. No more SDF body inflation or hair-count inflation.

## Actual free tool/source discovery and execution

On 2026-11-16, inspected the public `https://gobkit.com/api/free` catalog and its explicitly listed `gobkit-animal013-pack` / `barnowl` entry at `https://gobkit.com/freebies/animal013/BarnOwl.glb`. The catalog itself states a CC0 1.0 license, four named actions `idle`, `attack`, `dead`, `walk`, and a low-poly skinned rig. **Publisher's license assertion is recorded, but the original author chain of title was not independently checked.**

Created dedicated branch `research/owl172-run98-free-rig-source-qa` with self-contained Blender 3D inspection script and a free Ubuntu/Blender GitHub Actions workflow. Successful actual job: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43777236746 . Downloaded the authentic remote binary, verified its glTF magic and size; Blender actually imported it, listed meshes/bones/animation actions, rendered four independent native Cycles azimuths, applied a controlled warm cream material-only test to the true 3D geometry, exported a *new* GLB, re-imported it in Blender, and rendered four more original Cycles azimuths. The source GLB, derivative GLB, eight individual native renders, 2×4 contact, script, execution log, JSON metrics, mandatory nonrelease note and 14-item SHA256 manifest were committed to isolated research evidence. The workflow artifact ZIP (id `14186318305`) was independently downloaded and extracted; **all 14/14 stored SHA256 files verified OK**, with GLB binary headers/lengths checked separately.

| Measured item | Actual result |
| --- | --- |
| Source GLB | 91,784 bytes; SHA256 `6219f98a1582cba03bcfa45cdd9971c8e740a56eb2d4c7f873a8a10f28796fdb` |
| Geometry | 2 meshes, **600 triangles** |
| Rig | 1 armature, 16 bones |
| Blender imported actions | 4 (`idle`, `attack`, `dead`, `walk`); action presence is **not** an animation playback or usability test |
| Warm ablation GLB | 98,568 bytes; SHA256 `9f3c6c1a80d6f3e86d304877a8088bb9c13acdc0b93aef4de1a26957b8757877` |
| New GLB re-import | 2 meshes, 600 triangles, 1 armature, 16 bones, 4 actions |
| Native Cycles views | 8 images; source and warm ablation at 0°, 90°, 180°, 270° |
| True mobile WebGL2 GPU, FPS, animation controls/gestures | **Not tested**; 4 action names do not establish interactive performance |

## Direct visual inspection of the actual saved images

Downloaded the completed 2,509,924-byte compressed Actions evidence bundle and **opened the 1720×920 pixel 2×4 Cycles contact sheet**, rather than inferring beauty from metadata. The original source is a **flat-faceted cartoon owl with two pointed horn-like head tufts, circular sticker-like pale eye patches, huge dark disc eyes, sharp triangular yellow bill, separate side appendages, plate-like yellow back marks and two straight tiny block feet**. No natural cream fluff, proper Tyto disc, infant shoulder/short wings, tree-hollow support, soft back plumage or believable juvenile volume. It visually resembles a simplified horned cartoon bird, despite the provider filename "BarnOwl." Source is clearly **not** a viable artist-grade base for #172.

The warm material trial visibly destroys eye/pupil definition and makes nearly all facial/bill/wing/back surfaces the same beige-white. The structure, horn tufts, toy facets and implausible feet remain completely intact. This is an instructive **negative control, not a juvenile model**. Even the four-view side/back consistency is only the consistency of the wrong stylized bird. Manual art judgement: **ART_REJECTED** for both.

**No physical phone WebGL performance claims** are made. The downloaded model's four Blender actions indicate a potentially usable *independent rig study* only; they do not show that a later anatomically faithful model could be rigged by simple transfer. Avoid converting the current cartoon into a claimed high-quality sample.

## No-pay alternative/tool boundary

A connected external image-to-3D model-selection route was attempted with an absolute USD 0 budget, but demanded interactive user approval in this non-interactive run; no image-to-3D job was submitted, no charge made. Explored open-source Stable Fast 3D: the official checkpoint requires Hugging Face gated access/token, unavailable without login; its CPU backend alone does not remove that access requirement. Earlier free TripoSR CPU source experiments were already negative for reconstructed side/back anatomy. Download/login-gated commercial meshes and royalty-free/no-AI ambiguities were **not** treated as cleared source rights.

## Isolation and decision

Artifacts: `owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run98-FREE-RIG-DONOR-ART_UNAPPROVED/`, scripts in adjacent `tools/`, workflow `.github/workflows/owl-pet-172-run98-cc0-barnowl-rig-probe.yml`. GitHub compare to `main` showed **17 changed paths, all within the #172 independent research directory or its single dedicated workflow**. Existing root word game, 251-species pipeline, source concept, science ledger, cat pet prototype and production deployment were not changed; no external purchase was made.

**Next discriminating gate:** acquire a genuinely artist-grade, adequately licensed **juvenile Tyto** sculpt with real facial feather relief, rounded down surface, short concealed wings and side/back evidence before any rigging or mobile optimization. Exclude low-poly rigs and adult/horned birds as final art sources; do not equate technical GLB functionality or animation labels with artistic success. Keep this donor evidence quarantined. **No release, no user-success notification.**
