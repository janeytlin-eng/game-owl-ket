# Run89 / Run89B — genuine Blender fiber-guide → GLB ablation — **ART_REJECTED**

**2026-11-15 Asia/Shanghai.** This run **does not** produce a user-facing Tyto castanops v3 pet or a mobile-approved model. Strict no-demo/no-deploy/no-user-notification gate continues. All binary research artifacts are stored on the isolated branch `research/owl172-run89-baked-fiber-glb-ablation`, not on main.

## Rechecks and source constraints

Re-read `owl-pet/README.md`, `owl-pet/AGENTS.md`, `owl-pet/STATUS.md`, `owl-pet/research/species/172-tyto-castanops-v3.md`, Run87 audit, and Run88 native-particle proof. The target is the **rightmost** age-unknown cream mesoptile in `design/concepts/172-tyto-castanops-v3.png`. Its broad softly feathered heart face, dark open eyes, thick soft cream down, down-buried short wings, concealed tail, two supported feet and hollow lip are **visual gates**, not details proven by an adult model.

Run88B had a real Blender Cycles strand groom, but only in a native `.blend`, with **no GLB-portable hair** and a visibly wrong adult horned-owl body base. A genuine alternative CC0 [young Tasmanian masked owl/chick photo](https://www.lukeobrien.com.au/young-masked-owl-raptor-refuge) was found as observational reference; it is **not** a license to copy the photograph into textures or to assign the concept bird an exact developmental age. The free [Innerscene owl CC0 source](https://www.innerscene.com/tools/library/3d-parts/owl-d696472a) is still publisher-claimed CC0 and *adult horned owl*, not a scientifically correct chick.

## Actual reproducible transfer experiment (no mockups)

In the free Ubuntu GitHub Actions + Blender 4.0.2 environment, fetched the **original 23,619,180-byte Run88B `.blend`** after exact SHA256 verification (`12d0fe6bf598fb5f5e0017551ca96a9edfb7c1797f3bfbc2664f19f4ea597ce1`). Loaded a real artist-authored 59-mesh Run87B retargeted body and real native Blender hair particle system.

Experimentally sampled **2,800 native parent hair curves** (half-resolution of 5,600 parents) from *evaluated* particle keys rather than inventing synthetic radial feathers. Converted their real bent paths into 33,600 mesh vertices and **28,000 tapered, transparent triangle-ribbon faces**. Blender exported and **freshly reimported** real GLBs; independent reload found **60 meshes** and all **28,000 baked ribbon triangles**. This is a *technical portability experiment*, not acceptable baby down or an aesthetic win.

A first attempt incorrectly treated a Blender Python `AssertionError` as a successful action because Blender returned exit code 0 despite the exception; it archived only log and an explicit rejection marker. Workflow was hardened to use `--python-exit-code 42` plus mandatory GLB/metrics presence and checksums. The second attempt correctly evaluated the saved particle system and exported a GLB.

The first paired-view experiment mistakenly toggled the **evaluated** Blender particle modifier rather than the persistent emitter, making the native and baked visuals almost indistinguishable. It remains historically archived under `research-evidence-run89-REAL-HAIR-GLB-ART-REJECTED` as a **CONTROL_INVALID** ablation, notwithstanding that its GLB export/reimport worked.

The corrected **Run89B** switches the persistent emitter off during baked mesh rendering and keeps it on during native hair rendering, maintaining the same Cycles cameras and studio light across front, three-quarter, strict side and back. Successful [Actions Run89B](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43731785913) exported and round-tripped:
- Actual **18,489,868-byte GLB**, SHA256 `4487d7c057163ca53ba5ff0123a546e7c5153735ea6bb969143dff930632d179`.
- 2,800 genuine sampled guide trajectories, 33,600 mesh vertices and 28,000 ribbon triangles. 60 GLB reimported meshes; 28,000 reimported ribbon triangles.
- **Eight actual 420×420 Blender Cycles paired renders**, four full-angle native hair and four full-angle converted-GLB ribbon renders. Machine metrics, build log, negative gate and SHA256SUMS persisted with actual binary.
- [Run89B independently archived evidence](https://github.com/janeytlin-eng/game-owl-ket/tree/research/owl172-run89-baked-fiber-glb-ablation/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run89b-ISOLATED-HAIR-RENDER-ART-REJECTED).

## Independent visual acceptance: **ART_REJECTED**

Reviewed the actual Run88B groom and all Run89B native-versus-baked front/side/back images. The native groom forms a visually speckled blanket over the entire face: eyes and bill disappear into noisy stipple rather than a natural fluffy feather topology. After true particle removal, the GLB mesh ribbons are sparse **pin-like spikes** on a smooth cylindrical adult body, not soft fine cream down; the slight outline changes are real but inadequate.

Both versions retain a flat cap-shaped forehead, no credible soft Tyto heart-shaped disc, adult-looking narrow wing slabs and long bony feet. Profile reads as a rectangular/bag-shaped body on spindly legs, rear resembles a featureless barrel with symmetrical hard wing scars. The target's crouched hollow-lip-supported mesoptile anatomy and side/back consistency fail. Adding geometry does not correct underlying taxon, age or facial anatomy.

**Portable GLB ≠ acceptable WebGL pet**: Blender fresh GLB reimport works; no physical phone GPU, Three.js standard PBR shader parity, FPS, memory, touch, animation, thermal or real WebGL context was tested. 18.49MB is not an approved phone asset budget. Do not treat a Cycles preview as browser or mobile QA.

## Provenance and noninterference

- No paid generation/tool usage; free Blender, Python and GitHub Actions only.
- Entire experiment and failed binary models remain in the dedicated branch `research/owl172-run89-baked-fiber-glb-ablation`; earlier Run87/Run88 source and experiments untouched. The main branch receives only this **text audit**.
- Comparing main against research branch shows only `.github/workflows/owl-pet-172-...` and `owl-pet/3d-experiments/172-tyto-castanops/...` files changed. **No edits** to 251-species production automation, species ledger or manifests, concept image, old pet prototype or live deployment.
- Next meaningful test requires a **fresh accurate young Tyto head + tucked wing + legs + belly sculpt**, then professionally groomed feather layers and actual mobile WebGL render. Merely increasing ribbon/guide count on the adult base would repeat this failure.

**Verdict: real experiment + durable negative evidence, no releasable sample, NO USER NOTIFICATION.**
