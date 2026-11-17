# #172 Tyto castanops v3 — Run141 actual PBR neural-mesh anatomy/eye ablation: ART_REJECTED / NO_RELEASE

**2026-11-17 (Asia/Shanghai). Completed genuine Blender experiment, inspected 12 real Cycles renders.** This is a failed art refinement, **not a suitable openable user-facing pet**. No extra paid tools, no third-party GLB released, no product change.

## Preflight and target gate

Read `owl-pet/AGENTS.md`, `owl-pet/README.md`, authoritative `owl-pet/research/species/172-tyto-castanops-v3.md`, previous Run139/140/140B native Cycles and Three.js WebGL QA, rejected SHA registry, and Run111's prior nonrigid juvenile sculpt. This is specifically the rightmost **age-unknown cream second-down mesoptile** in the unchanged v3 plate, not an adult owl. Required visual anatomy: soft feather-integrated heart mask, fully open dark eyes, tiny pale beak, squat fluff, only short down-buried wings, concealed tail, belly and both feet supported on a broad aged eucalyptus hollow lip. Avoid inventing exact age or scientifically measured side and back from one plate.

Input was exactly the **actual** Run139 free public 3DValley TRELLIS.2 textured GLB from Run140's quarantined Actions artifact, SHA256 `9a154c9e3aeebb34ebcd6f209760e1d9e21e2f544f2b690dae406d9c8bf878e8`, 9,983,448 bytes / 192,765 source polygons / two embedded textures / one PBR material. Source crop `rightmost_baby_owl_512_rgba.png` SHA256 `e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8`. **The source mesh was already rejected for half-closed eyes, long adult wings/tail, flaky back and floating feet.** Run141 is a controlled failure-to-fix test, not a fresh new source or accepted asset.

## Actual tools and work

- Dedicated research branch: `research/owl172-run141-pbr-native-eye-wing-sculpt`, based on the completed Run140B experimental state, never on or merging to `main`.
- Real [GitHub Actions Run141 execution](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44075640931): all seven substantive steps succeeded, including source artifact acquisition, Blender 4.0.2, exports, independent fresh import, all 12 Cycles renders, checksum verification, quarantined artifact upload, scoped nonbinary evidence commit.
- Native continuous-surface deformer actually moved **219,071 genuine neural mesh vertices**, mildly broadening upper head and compressing lower/back wing-and-tail mass. Source bbox (x/y/z Blender units) 0.457668 / 0.700133 / 0.475094; deformed bbox 0.472808 / 0.589527 / 0.471904. The 15.8% depth reduction is real, not evidence of anatomical correctness.
- Second ablation attempted real 3D eye-surface location using Blender mesh ray casts: two successful mesh hits, each modified surface supplemented by a tiny convex iris mesh (288 polygons before triangle export). **These eye elements are not a replacement owl or a pretend professional sculpt**; their use was explicitly contingent on rendered visual approval.
- Actual PBR exports and fresh Blender reimports:
  
| Research-only GLB | File bytes | SHA256 | Fresh reimport |
|---|---:|---|---|
| Native tuck, no added eye | 10,001,892 | `769ad302ae6e88a2aa1a963447b36890cc84664cea854c53933efde8e3fc74be` | 1 mesh, 192,765 polygons |
| Native tuck plus eye inserts | 10,030,948 | `aa5d57babda5239528bb981efe05490f4b070cbd9b43e0c1a6c8d79fb0f9961b` | 3 meshes, 193,821 polygons |

- Four true Blender Cycles views (front, quarter, strict side, back) per condition: untouched source, native-tuck-only, and native-tuck-eyes. **12 actual rendered PNGs plus a 3-column×4-row comparison contact sheet** are in `research-evidence-run141-NATIVE-PBR-EYE-WING-NO_RELEASE/`. Original GLB and both derived GLBs remain in the **restricted, 30-day Actions artifact** `14325401061`, not in distributable Git blobs. Source art and code retained in branch. Manifest checksum validation reported **20/20 OK** on the archivable payload; the source/model binaries themselves also appear in the artifact and its SHA manifest.

## Independent four-angle visual decision: reject BOTH variants

I opened and compared the [actual 12-view image contact sheet](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run141-pbr-native-eye-wing-sculpt/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run141-NATIVE-PBR-EYE-WING-NO_RELEASE/run141_actual_native_three_way_four_view_QUALITY_UNREVIEWED.jpg).

1. **Native tuck only:** face/head occupies more of the front silhouette and side body is slightly more compact, but it still has squinting/closed dark eye slots, unambiguously long layered primary feathers and a tapering visible tail. Deep, harsh black/grey speckling and clumped scale-like back/sides remain. Exposed claws still suspend in empty space; there is no wood hollow or belly support.
2. **Native tuck + eye insert:** **explicitly worse.** Two prominent black globular dots sit too high on the forehead/upper mask and visibly protrude from the face instead of restoring anatomically recessed, natural fully opened eyes. Front and quarter look like pasted-on toy beads; side confirms obvious protrusion. This is the precise **simple-geometric-addition failure** that must not be presented as a high-quality owl. Reject the eye-insert technique at this calibration, do not ship it.
3. **Both:** backs remain hard, flaky and mottled; rear morphology does not naturally continue cream down from the face/chest. Soft fine cream second-down, hidden wing/tail, convincing juvenile anatomy, and aged eucalyptus support **all fail**.

The modified variants were **not tested in a new mobile browser**, because they fail the prior mandatory art gate. Run140B's Chromium SwiftShader success applies only to the previous original and LOD GLBs; do not propagate those test results to these modified GLBs. No real phone hardware GPU or battery benchmarks, no animation, and no finished mobile electronic-pet sample.

## Rights, isolation and action record

[3D Valley terms, last updated 5 Nov 2026](https://3dvalley.com/terms) say the provider claims no rights to generated results and permits commercial use subject to rights in input. This is useful primary-provider wording, **not independent confirmation of every underlying copyright, model license, and redistribution issue**; source/derivatives stay quarantined. Zero additional payment or account/quota bypass.

Compared against immutable Run140B baseline `d1b5d7fe876e8f8af4a5814e0b657fd1c97b3641`, this run had **4 commits ahead, zero behind, 22 changed paths**, all scoped to `owl-pet/3d-experiments/172-tyto-castanops/` or the **new dedicated Run141 workflow**. No edits to 251-species production process, existing pet prototype, v3 concept source, main, root game or deployment.

**Final: ART_REJECTED / NO_RELEASE.** Native surface compression gives a measurable but inadequate visual change, while the eye-overlay strategy is a demonstrated mistake. Future work must prioritize truly new anatomically correct sculpt/soft-down construction or a legally obtainable professional juvenile mesh; do not repeat small primitive patches, take software-WebGL counters as art approval, or notify the user with this rejected asset.
