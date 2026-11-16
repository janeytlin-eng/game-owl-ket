# #172 Tyto castanops v3 — Run105 / Run105B independent alpha-vs-matte neural geometry test — **ART_REJECTED**

**2026-11-16, Asia/Shanghai. Research-only. No role-player GLB is an approved pet or user-showable sample.**

## Preflight actually checked

Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, and the archived Run99 + Run99B, Run102 and Run103 + Run104 reports and real preceding model records. The official target is the **rightmost age-unknown cream second-down chick** from the #172 v3 three-owl plate: rounded cuddly young proportions, an actual broad heart disc, **open dark eyes**, down-buried tiny wings, hidden tail and supported feet on a broad eucalypt hollow. Exact age and side/back morphology are **not verified** by the single concept view.

Existing live `owl-pet/prototype/index.html` remains the older unrelated cat prototype. The 251-species production mechanism, design plate, manifest and deployment are out of scope.

## Run105 — actual ZeroGPU generated GLB, but neural structure collapsed

Created `research/owl172-run105-foreground-hunyuan-reconstruction`, new independent Python 3D inference script `tools/run105_foreground_hunyuan_probe.py`, and the dedicated workflow `.github/workflows/owl-pet-172-run105-foreground-hunyuan-probe.yml`. Base was the confirmed Run104 research branch, not main/production.

To discriminate whether the original noisy photo/background explains Run99's poor geometry, reused **only** the actual rightmost owl foreground segment extracted in Run103. Verified the 548×548 original; applied border-connected background selection and alpha silhouette, isolated and padded it into a 512×512 RGBA input, preserved the true photographed feathers and feet. Measured segmentation foreground coverage **0.776611328125** (at 64×64 mask preview), without inventing back/side views. Opened the actual input image emitted by the running workflow; it is recognizably the correct baby owl.

Called the real public `tencent/Hunyuan3D-2` ZeroGPU `/shape_generation` endpoint anonymously, with 30 steps, guidance 5.0, seed 172, octree resolution 256, `check_box_rembg=False`. It responded with an authentic binary GLB in 7.33 seconds. Validated magic/length and SHA256:
- `run105_neural_source_ART_UNAPPROVED.glb`: **13,194,120 bytes**, **SHA256 00f926c234f462354587741fab040c847e25ae5732c868053e9d677a0224a30b**.
- Blender 4.0.2 actually imported one mesh, exported `run105_roundtrip_from_blender_UNAPPROVED.glb` (**37,050,144 bytes**), and generated **four genuine Cycles camera views**. Imported object's bounding dimensions were [1.619115, 1.203310, 1.957358] (Blender units; not anatomical measurements).
- Provider-reported `number_of_faces=872696` is **provider metadata**, not an independently audited Blender triangle count. Do not equate these.
- Run [43812628249](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43812628249) succeeded at generation, Blender camera renders, SHA256 evidence checks and isolated evidence push. Actual evidence folder is `research-evidence-run105-FOREGROUND-HUNYUAN-ART_UNAPPROVED/`.

**Visual review:** We actually decoded and opened the original 512px render contact from the archived workflow log (`BEGIN_RUN105_NATIVE_RENDER_CONTACT_BASE64`). The model **does not look like a bird at all**. Front, 45°, strict side and rear present featureless gray, flat-sided **rectangular cuboid/box-like solids**, with no visible heart mask, open eyes, fluffy crown, tucked wings, feet or hollow. This is a catastrophic reconstruction failure. It is not evidence that the model is suitable merely because Blender exported four PNGs. The provider may be mishandling alpha/background preprocessing, but that is a **hypothesis, not a verified cause**.

**Bookkeeping caveat:** The copied Run99 script left `"run":"99"` inside Run105 `preflight.json` and `run105_status.json`; these are **Run105** files as established by scripts, paths, source SHA, timestamp, model hash and the linked Run105 job. This is a metadata labeling defect, not an alternative generation event. Record explicitly, do not hide or silently rewrite hashed original logs.

## Run105B — actual zero-charge corrective attempt, quota blocked

Created second independent branch `research/owl172-run105b-neutral-background-hunyuan`, `tools/run105b_neutral_matte_hunyuan_probe.py`, and dedicated workflow `.github/workflows/owl-pet-172-run105b-neutral-hunyuan-probe.yml`. This controlled adjustment **composites the same segmented RGBA owl onto neutral warm-gray RGB**, enables the provider's native `check_box_rembg=True`, then repeats the otherwise same genuine inference call. This tests whether RGBA transparency and disabling native background removal caused Run105's cuboid. Actual input segmentation and API schema are archived, with source coverage 0.776611328125, and status is correctly labeled `run=105B`.

The live endpoint replied **`AppError: You have exceeded your ZeroGPU runs limit. Authenticate with a Hugging Face token for more quota`**. The workflow was an actual API attempt, not merely a plan. **No GLB exists for Run105B, so there is no artwork comparison, no render and no claim that the RGB adjustment fixes Run105.** Its failure traceback, input PNG, logs, schema, rejection gate and SHA256 manifest were independently committed under `research-evidence-run105b-NEUTRAL-MATTE-ART_UNAPPROVED/`. CI can finish successfully to archive a correctly handled **quota failure**; CI green is **not** an art pass. Workflow run [43812909398](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43812909398).

No token, payment, account switching, proxy quota avoidance or other billed workaround was used. Quota is transient, therefore this route may be retried within future permitted public limits; no forced repeated API calls now.

## Gate and isolation

**ART_REJECTED.** Run105 has real 3D binary geometry and genuine four-view renders, but **catastrophically incorrect cuboid anatomy**; Run105B could not obtain geometry under the free public quota. Neither has cream PBR down, true facial relief, convincing short wings and supported feet, anatomically confirmed side/rear or a natural broad eucalypt hollow. No actual iOS/Android GPU/WebGL frame-time, touch, motion, memory or thermal testing has been performed. No user-facing model, online prototype or release link is approved.

Tencent's [Hunyuan3D-2 community license](https://github.com/Tencent-Hunyuan/Hunyuan3D-2/blob/main/LICENSE) is **not CC0/MIT for model output** and includes use/distribution territory limits, including EU, UK and South Korea exclusions. A public research branch is **not** proof of global commercial redistribution rights; verify legal scope before distribution. External wildlife chick photos can help analyze morphology but are not authorized model training/output sources in these trials.

Both dedicated branches were created without touching the 251-species pipeline. The only new paths are under `owl-pet/3d-experiments/172-tyto-castanops/**` or dedicated `.github/workflows/owl-pet-172-*` research workflows. No original concept overwrite, no user prototype change, no public site deployment, no payment.

**Next meaningful discriminating action:** retry RGB-matte-plus-native-rembg only after legitimate free quota becomes available, inspect actual true four views and reject any cuboid; otherwise prioritize artist-directed topology and natural down sculpture on a properly licensed true juvenile source. Neither additional polygon counts nor a CI-success badge is a quality substitute.

**Final: RESEARCH ARCHIVED / ART_REJECTED / NO USER-SHOWABLE 3D SAMPLE.**
