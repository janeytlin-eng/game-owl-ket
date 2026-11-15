# Run87B independent visual + GLB QA — **ART_REJECTED**

2026-11-15 Asia/Shanghai. This is **not** an approved species model, 3D pet, downloadable sample, or deployment.

## Verifiable source and actual modeling

Pre-flight reread `owl-pet/AGENTS.md`, `README.md`, the #172 v3 species record, original concept image `design/concepts/172-tyto-castanops-v3.png` (all three owls, visual comparison only to the **right** cream baby), Run85/86 rejected reviews and the current cat-only interaction prototype. The reference is an **age-unknown mesoptile**, not a labelled-week juvenile, with warm cream natural down, broad feathered Tyto heart, dark eyes, no adult-length wing/remiges/tail, full supported body and feet on a broad old hollow lip. Side/back characteristics are **not present** in the single frontal art.

Public source: [Innerscene Owl GLB](https://www.innerscene.com/tools/library/3d-parts/owl-d696472a). The publisher states it is its own CC0 model. Independent confirmation of provenance beyond the publisher's claim has **not** occurred. Source is visually an **adult horned owl, not Tyto**.

First isolated Blender run [43723360895](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43723360895) downloaded an actual 20,671,040-byte GLB, SHA256 `c11c94db20065c6c6f252e768e8c748f22dc69ef9b4e7199110b96de0625c12e`; Blender importer saw 129 meshes, 62,592 triangles, 14 authored materials and high-resolution textures, no animations. Eight original 540px native Cycles source turntable renders and original/reimported GLB are durably archived in sibling `research-evidence-run87-CC0-SOURCE-ONLY`. The mesh has open boundaries and unsuitable adult long remiges, ear tufts, long tail and exposed feet.

Run87B applied **actual 3D mesh vertex morphs** to the existing original sculpt (not SVG or separate sphere assembly): removed 70 adult ear/flight/tail components, retained and changed 59 mesh objects, compressed and broadened the anatomical volume, shortened wing bud and beak, pigmented near-front head with sculpted/vertex-color heart-shaped disc, rendered all four original Blender Cycles front, three-quarter, side, back views. Real GLB export plus Blender reimport passed, workflow [43724422997](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43724422997), with evidence archived in this isolated research branch. Two non-art failures in prior tries: Blender import did not match the original geometry filename, and evidence git add fell outside sparse checkout; both were fixed/retried. An earlier source-only trial was missing `python3-numpy`, similarly corrected.

Final 17,079,204-byte GLB SHA256 `cbbca8d70d8a8b83639d927096e9302be9d49b8dbae81cd5726cebca753db253`; independent `trimesh` import: **59 meshes / 48,312 final triangles / 30,171 vertices / 0 entirely watertight meshes**. Native Blender reimport preserved 59 mesh objects. Note `textures_tinted=[]` in original metrics: the source's actual texture image names did **not** match the planned `basecolor` recolor branch; do **not** claim successful 2K cream texture recoloring. The model already renders a whitish material from original asset. GLB, 4 native Cycles screenshots, metric JSON, SHA and Blender log are in this folder.

## Four-view image inspection — decisive art rejection

- **Front**: upper head forms a wide flattened cap, facial pigment produces a high-contrast *smiling/chevron throat mark* rather than naturally feathered Tyto heart; eyes still resemble a hard adult horned-owl expression, pale/brown scales repeat across body.
- **Three-quarter/profile**: head-to-shoulder narrows into an elongated rigid funnel, short wing resembles a hard oval paddle stuck to flank, no fine down halo; exposed raptor shanks and thin long toes violate the supported mesoptile form.
- **Strict side**: folded wing has no credible buried down, torso tips forward, bill remains adult hook; chest/body positioning and shoulder anatomy do not match intended compact crouched chick.
- **Back**: surface is a smooth almost rectangular tube with repeating stamped chevrons, two tiny unconvincing wing traces, no soft naturally layered feathers.
- There is **no supporting tree hollow**, no authentic down-groom asset/LOD and no rig or animation.

Mobile usability is not established: 17.08 MB binary with large textures and nonwatertight elements, no genuine mobile GPU, native glTF PBR/normal map parity, measured FPS, touch, animation or power/thermal review. An independent local Chromium attempt to load a stripped-down normal-lit geometry smoke test was blocked by the container's browser administrator policy at both localhost and file URLs (`ERR_BLOCKED_BY_ADMINISTRATOR`); **no successful WebGL draw is claimed for Run87B**. This should not be conflated with the successful GLB-to-Blender reimport.

**Verdict ART_REJECTED.** This exercise validates only that a zero-extra-payment, textured CC0 owl asset can be downloaded, imported, surgically edited and roundtripped with fully preserved source meshes. Transferring even a high-detail **adult horned owl** cannot establish the required **Tyto age-unknown cream mesoptile** morphology and realistic down. Stop polishing that particular wrong-species source. Next route should acquire/author a species-appropriate organic youth sculpture with actual correctly shaded short wing and layered groom; require full 4-side renders and physical phone GLB/PBR testing before release. No extra paid tools used.

## Noninterference and retention

All source, binary outputs and render images exist **only** under `owl-pet/3d-experiments/172-tyto-castanops/` in the dedicated `research/owl172-run87-cc0-organic-base-audit` branch; the two workflows under `.github/workflows/owl-pet-172-run87*.yml` are unique research-only workflows. Comparison `main...research/owl172-run87-cc0-organic-base-audit` shows **zero edits** to 251-species pipeline, production concepts/manifest, root word game, existing pet prototype or deployment. No external billing or paid inference.
