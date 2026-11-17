# #172 Tyto castanops v3 Run153 — genuine original Blender sculpt/groom feasibility test

**Date:** 2026-11-18 Asia/Shanghai. **Final human-reviewed art verdict: ART_REJECTED / NO_RELEASE.** Do not present the visuals or test GLB as an acceptable juvenile pet.

## Source and boundary checked before work

Re-read the owl-pet AGENTS/README, the v3 #172 research species file and Run152 negative native four-view/PBR audit; checked the known-rejected GLB SHA256 registry. The rightmost v3 source shows open dark eyes, a broad *integrated* heart disc, creamy very short second down, hidden wings/tail and fully supported feet. Run152's TRELLIS model fails coarse brittle grey/brown patches, overly mature side/back and unsupported claws. This new experiment **does not reuse its rejected mesh**; it tests a genuinely independent original Blender-native sculpt, without extra paid providers or unauthorized commercial assets.

## Actual execution and corrected error

A new isolated research branch, dedicated workflow and Python source were created; no production code was touched. First actual GitHub Actions attempt [44182831105](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44182831105) reached Blender 4.0.2 but exited on a real Python exception: MetaBallElements.new required keyword argument `type="ELLIPSOID"`. Blender itself exited code 0 despite the traceback, causing a **false-green workflow**; the only model artifact was a tiny failure log. That first attempt was **not** a successful render or export. Corrected both the Blender API and workflow's explicit traceback/file-output gates; also ensured the main sculpt is selected for mesh export. The second actual GitHub Actions attempt [44183510767](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44183510767) completed the native renderer and four camera images.

Run153 creates a fused voxel-remeshed Blender mesh rather than an SVG/billboard, with a three-dimensional procedural face surface, open eyes, tucked wings/feet and **11,400 individually curved short-down fibre strands** in the saved Blender source. It places an experimental support ring under the character. Blender 4.0.2 rendered **front (+Y), 45-degree quarter, strict side, back (-Y)** via real CPU Cycles at 480×480 and 16 samples each. The independent saved `.blend` is **7,042,832 bytes**. The **mesh-only** GLB exports/imports as real glTF and is **1,145,400 bytes**, SHA256 `073e5d7193b66909866d85a7a82a10db2f8b20f1faa7acb440eee9da82468471`, with **51,976 triangles across 23 glTF geometries** according to subsequent independent trimesh parsing. There are no animations. **Blender curve grooming is NOT contained in the GLB**; this alone precludes WebGL hair acceptance.

## Actual four-view visual review — rejected

The [real four-view evidence sheet](research-evidence-run153-ORIGINAL-SCULPT-NO_RELEASE/run153_actual_four_views_UNAPPROVED.jpg) and original 480 px view files were inspected. The front is recognizable as an owl-shaped concept, but has conspicuously protruding circular cartoon eyes and a thin face disc rather than an integrated natural masked-owl juvenile. In the 45-degree view, both eyes jut out on the face. The strict side reveals the **heart mask and eye assemblies visibly detached in space from the head**; hence it has no valid anatomically continuous profile. Head/body fibre silhouettes appear needle-like and thin, not dense natural creamy down; the rear displays a featureless broad blob with a conspicuous sparse blank patch. The support looks like a smooth solid cylinder with a torus, **not a believable aged eucalypt hollow with integrated feet and body weight**. Tucked short wings alone do not rescue these fails.

This is **not** a good-looking finished 3D chick; the test is a clear negative result for this particular manually scripted geometry/groom shortcut. Do not turn this model into a public demo, mobile pet, product asset or technical benchmark. Since it fails the art and GLB fur gates, **no physical phone/WebGL performance test was performed**, and none is claimed.

## Evidence, rights, isolation

The [actual Blender log](research-evidence-run153-ORIGINAL-SCULPT-NO_RELEASE/blender_actual.log), [runtime status](research-evidence-run153-ORIGINAL-SCULPT-NO_RELEASE/run153_status.json), [contact sheet](research-evidence-run153-ORIGINAL-SCULPT-NO_RELEASE/run153_actual_four_views_UNAPPROVED.jpg), NO_RELEASE marker and SHA256 evidence manifest were committed. Rendered four original PNGs, editable .blend and mesh-only GLB are quarantined in the [second run's 30-day artifact](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44183510767), **not** in the product branch. The Blender sculpt source is newly written for this #172 test; no provider licensing grants were assumed. No external paid tool was used and no purchase was made.

Compared against Run152 branch SHA `9773b5180eda7cae045ae6e4f4224c1259ac637d`, the isolated changes are one dedicated workflow and Run153 experiment scripts/record/evidence only. `main`, 251-species production, existing WebGL prototype and deployment remain untouched. Workflow green means script execution and archiving only, **not** artistic approval.

## Technical conclusion

The genuinely new native sculpt proves Blender CPU, four-view geometry render, editable source and quarantine pipeline can work without a paid neural service, but also demonstrates a **hard stop**: procedural eye/face placement breaks anatomical continuity, volume-to-fibre offsets make spiky and empty patches, and Blender-only curve hair does not produce portable mobile GLB. Further cosmetic revision of this placeholder would risk repeating rejected primitive-assembly routes. Next meaningful path is an actual artist-grade juvenile sculpt/groom or truly multiview mesh with integrated anatomy, baked or optimized down, source-rights checks and four-view QA **before** phone optimization.

**ART_REJECTED / NO_RELEASE — no approved sample, no user notification.**
