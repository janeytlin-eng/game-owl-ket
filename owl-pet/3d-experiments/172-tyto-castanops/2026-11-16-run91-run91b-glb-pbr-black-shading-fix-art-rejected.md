# Run91 / Run91B — genuine glTF 2.0 PBR dark-body root-cause ablation and COLOR_0-preserving repair — **ART_REJECTED**

**Date:** 2026-11-16 Asia/Shanghai. **Release decision: ART_REJECTED.** The experiments below are real Blender/GLB/Three.js technical evidence, **not** a displayable, visually acceptable #172 *Tyto castanops* v3 age-unknown downy electronic pet. **Do not publish any candidate as finished art, update the live pet site, or notify the user about a sample.**

## Re-read and constraints before doing work

Actually inspected the repository's `owl-pet/AGENTS.md`, `README.md`, `research/species/172-tyto-castanops-v3.md`, true 1536×1024 `design/concepts/172-tyto-castanops-v3.png` (including full-resolution displayed pixels), Run86, Run87, Run89, Run90 audits, preceding real GLB tool source and prior Three.js loader. The target is the **rightmost** cream age-unknown mesoptile, with naturally feathered broad tan heart-shaped face, dark eyes, compact crouching down-covered juvenile, down-buried tiny wings, hidden tail, two feet/abdomen supported by the broad eucalypt hollow lip. Its original front-only concept does **not** validate exact age, side/back anatomy or nest interior. Existing `prototype/index.html` is an unrelated archived cat WebGL application, not an acceptable owl.

Run90 had exposed a severe QA false positive: a genuine 3D `GLB` loads and rotates with `gl.getError()===0` but the bird is essentially black in lit Three.js. Here we isolated that technical defect without pretending to repair still-inaccurate young-Tyto anatomy. We deliberately reused the **same continuous connected signed-distance surface**, not a collection of new primitive spheres; that mesh is itself **already art-rejected**.

## Run91 — three genuine GLB normal/material controls and real screenshot pixel checks

Built and independently reimported three 102,744-triangle, 24-mesh real GLBs with the **same geometry**, from repository v31 connected sculpt (the main body is watertight and positive-volume). Genuine source `COLOR_0`, implicit vs explicit `NORMAL`, and flat-cream nonmetallic `PBRMaterial` were toggled as controlled variables:

| Control | Actual GLB bytes | SHA256 |
|---|---:|---|
| vertex `COLOR_0`, implicit normal, missing explicit matte PBR | 2,050,956 | `0843275b46ae496bbbffdc075606e7e848d73152350b17324a9282f442fc040f` |
| vertex `COLOR_0`, explicit normal, missing explicit matte PBR | 2,714,380 | `7f0b0226e77634b98a782d969123e7cebbeb3feb559d9fe76ff20bd30363b633` |
| flat cream matte PBR, explicit normal but **no original `COLOR_0` facial pigment** | 2,547,728 | `9449c591f85d51955015079c60ff061839ae8330c84d3d288112e18880415469` |

Successful [Run91 Actions 43740695304](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43740695304) actually performed **12** Blender 4.0.2 Cycles four-direction renders, **six** genuine Three.js Chromium SwiftShader desktop/emulated-phone render captures, three GLB independent reimports and screenshots + hash reporting, all saved and read from [Run91 permanent **ART_REJECTED** research evidence](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run91-pbr-foreground-validation/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run91-PBR-FOREGROUND-ART-REJECTED). Run91's automatic pixel gate (central ROI of post-orbit screenshots, segmentation approximated from known background) found desktop bright fraction **0.0157** for original implicit normal, **0.0309** for original explicit normal, and **0.3002** for flat matte PBR; original desktop foreground non-background median luma was **0** for both dark variants versus **166.76** for matte PBR. All THREE browser smoke tests nevertheless returned exit code 0. The pixel measure is a **technical visibility heuristic** and remains subject to visual inspection. Changing normals alone did **not** fix this dark-body problem; abandoning original vertex colour for flat matte material helps brightness but destroys useful heart/eye colour information.

## Run91B — actual isolated **vertex-colour-preserving** glTF PBR repair, not fake art

Audited GLB JSON chunks and identified that exported `COLOR_0` vertex-colour meshes lack a glTF material. Under the glTF 2.0 PBR default, such a material has `metallicFactor=1.0`, so normal-lit rendering is wrongly metallic/dark for soft bird down. Verified with a new genuine GLB binary patcher that changes the **23** `COLOR_0` mesh primitives missing a material to a correct `pbrMetallicRoughness` material with **`baseColorFactor=[1,1,1,1]`, `metallicFactor=0.0`, `roughnessFactor=0.95`**, keeping original `COLOR_0`, original geometry, explicit `NORMAL`, binary buffer data, eyes, face pigment and existing alpha-textured down cards rather than replacing colour. Parsed patched real glTF JSON and reimported both variants independently:

| Genuine identical-geometry GLB | Bytes | SHA256 |
|---|---:|---|
| original implicit-default-metal GLB control, `COLOR_0` + explicit `NORMAL` | 2,714,380 | `50f718e060de416de6c40189561bd65ef16b524dcc09a86dc0e6f228e40f9582` |
| original `COLOR_0` + `NORMAL` with proper nonmetal matte PBR | 2,714,864 | `47088e4e5a3c6267bdb01d0cf9e5bdd344e1a6ba4f9d4955cb17a22ed61870c6` |

Both are actual **24-mesh, 102,744-triangle** GLBs. Successful [Run91B Actions 43741174677](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43741174677) independently produced **eight** locked-light real Blender Cycles views (front, 3/4, strict side, back for both variants), **four** Three.js Chromium SwiftShader actual screen captures in desktop and emulated iPhone viewports, original browser QA JSON, Python pixel checks, build logs, hashes and research-only source code. Actual files were permanently saved in the isolated [Run91B negative-evidence branch archive](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run91b-glb-color-pbr-fix/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run91b-MATTE-COLOR-PBR-ART-REJECTED) and read back.

The **actual desktop Three.js screenshots** were independently inspected: the original GLB remains almost entirely black, while the repaired GLB becomes visible cream and renders the eyes, feet and original vertex colour. Pixel measure changed from **0.0090 bright-foreground fraction** / **0.0 median non-background luminance** for original to **0.3182 bright fraction** / **167.20 median non-background luminance** for corrected. The repaired desktop and simulated-phone capture both pass the narrow material-visibility heuristic. Both browser model loads, framing/orbit and zero-GL-error smoke tests returned exit 0. This is a genuine **material-path bug repair** for glTF export, **not** an art, creature-identity, mobile device or performance pass. Keep the repaired source and binary only in the research branch; no deployment or replacement of 251-species production models.

## Actual four-view aesthetic decision: **ART_REJECTED without exception**

The actual Run91B repaired **front, strict side, rear** Cycles images and actual browser screenshots were opened and judged against the original rightmost cream juvenile concept. More correct colour and less black shading finally make defects clearly visible:

- The sculpt remains a **tiered, ribbed/pillow/pear-shaped synthetic toy blob**, not a realistically rounded and supported age-unknown mesoptile.
- The face is a **hard engraved/embossed schematic heart**; eye bulbs are like buttons, bill is a small artificial nub, not natural soft facial feathers.
- The side has a **protruding eye and no believable tucked juvenile wing**; the rear is an almost featureless symmetrical barrel with horizontal ridges. Neither has valid Tyto feather tracts or credible 3D side/back anatomical continuity.
- Down still appears as **tiny scattered points/short needles rather than dense natural cream fluff**; feet and tree-hollow prop are crude, cylindrical or detached from believable weight/support.
- The physical **Android/iOS GPU**, hardware FPS/memory/thermal, real mobile PBR consistency, rigs, wing articulation, blink, touch and animation have **not** been measured. SwiftShader software with a phone-size viewport is **not** physical phone acceptance.

Thus **normal and PBR correction improve a real technical issue, but do not satisfy a single release-ready juvenile character**. Export/import, browser draw, bright pixels, watertight head/body and 0 GL errors do not imply art quality.

## Free tools, isolated provenance and what cannot be claimed

Only free GitHub Actions Ubuntu, Python/NumPy/scikit-image/trimesh/Pillow, Blender 4.0.2 Cycles CPU, Three.js, Playwright Chromium SwiftShader and GitHub source/evidence archive were actually used. An optional external 3D generation service was not used or charged; no paywall/credits purchased. Source is original repository design and self-authored experimental modeling script, **not** a side/back reconstruction. Branch comparisons with main show differences confined to dedicated `.github/workflows/owl-pet-172-run90/run91/run91b...` research workflows and `owl-pet/3d-experiments/172-tyto-castanops/` isolated research code/evidence; prior Run90 files are inherited from the Run90 experimental branch. No species production workflow, ledger, immutable species archive, original plate/manifest, old cat pet prototype, root vocabulary game, or online deployment was modified. This main-branch audit is **text only**.

**Follow-up priority:** retain the matte `COLOR_0` glTF material fix in research pipeline while pivoting art development to an **anatomically authored juvenile Tyto head, shoulders, tucked wings, rear and foot/hollow support**, genuine soft groom/LOD and real-device performance proof. Avoid further superficial deformations of this rejected base model. **Do not advertise any Run91/91B GLB as completed electronic pet.**
