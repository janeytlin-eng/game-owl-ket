# #172 *Tyto castanops* v3 — Run259 / Run259p / Run259pp actual native neural 3D reference pigment and rear smoothing

**Executed 2026-11-21 Asia/Shanghai. FINAL: TRUE_NATIVE_3D_PASS / SOFTWARE_WEBGL2_PASS / ART_REJECTED / PHYSICAL_PHONE_UNTESTED / RIGHTS_UNCLEARED / ZERO_EXTRA_PAYMENT / NO_RELEASE.**

This is independent reproducible research on **the genuine rightmost cream-white juvenile concept**, not a pet release or artistic acceptance.

## Source identity, prior attempts and boundaries

Before the run, checked `owl-pet/AGENTS.md`, `owl-pet/README.md`, the saved kitten-WebGL prototype directory, Run258/258p actual producing/repairing scripts, 2026-11-21 Run258–258p audit, actual reference image and actual native **front, side and back Blender images**. Real reference is the far-right 512×512 RGBA baby owl SHA256 `e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8`, depicting a plump softly layered cream juvenile with two open dark eyes, small integrated heart-shaped facial disc, buried short wings and visible feet. Run258p actual generated and norm-repaired native source GLB SHA256 `4b74b8d045b50ad2075ccf262647824e06d1d51e440c7634c864651800a5541e` remains a **single real continuous 20,000-triangle neural mesh** with smooth normal attributes; its true side/back showed a rigid, pointed, elongated rear and spikes; front showed white blank eyes.

No SVG, no 2D-turntable fake, no owl assembled from simple spheres, no re-use of adult bird, no external image-to-3D generation fee, no new free-service quota consumed. Exact source model was **downloaded from the successful preexisting Run258p Actions artifact**, independently SHA-checked, and never placed on a public deployment.

## Actual Run259 experiment and failure recovery

Isolated research branch: `research/owl172-run259-juvenile-neural-reference-color-back-relief-no-release`.

Script: `owl-pet/3d-experiments/172-tyto-castanops/tools/run259_real_hy3d_reference_eyepigment_posterior_fairing.py`. Workflow: `.github/workflows/owl172-run259-true-native-reference-color-and-rear-smooth-no-release.yml`.

Rather than yet another adult-body cut or opaque texture claimed as feathers, we tested:
- **A**: unchanged **true 20k neural geometry**, real COLOR_0 per-face-loop vertex pigment from front-facing projection of the SHA-locked rightmost image, with provisional ocular dark-pigment on the existing real eye surface. No invented full 3D feathers.
- **B**: same source and color method, applying Blender's true spatial smoothing **to rearward original mesh vertices only**, leaving frontal head and feet geometry unchanged and preserving the single watertight neural body. As a controlled ablation, this tests whether spikes are locally treatable. It does **not** claim to generate wing anatomy or realistic layered down.

[Run259 initial remote #44861318500](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44861318500) generated a true A GLB and seven actual Chromium WebGL2 views but failed Blender camera render on a missing world object. [Run259p #44861529043](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44861529043) fixed the world creation and recalibrated source color but exposed Blender's Ubuntu package being built **without OpenImageDenoiser**; again exported an actual A GLB, then failed render. Both runs were strictly quarantined with full machine exceptions; their green GitHub Action wrapper was **not** considered art/overall success. Their original proof-of-failure ZIPs were downloaded, SHA/CRC checked independently, and the genuine Blender tracebacks inspected.

**Run259pp corrected** Cycles render to explicitly disable denoising; the [remote execution #44861742166](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44861742166) successfully built **both** real neural GLBs, produced **eight different Blender Cycles rendered spatial views** (front, quarter, side, back for each), plus **14 Chromium/Three.js GLTFLoader actual WebGL2 views** (seven each), signed SHA256 manifest and archived nonbinary visual evidence independently. Both variants passed all **10 true software WebGL2 geometry/browser gates**. Software GPU was **ANGLE SwiftShader**, not a physical phone.

| Metric | A native source-pigment | B true rear smoothing |
|---|---:|---:|
| GLB original 3D triangle count | 20,000 | 20,000 |
| Original mesh vertices | 9,626 | 9,626 |
| Mesh count and closure | 1; watertight | 1; watertight |
| Actual changed mesh vertices | 0 | 5,782 |
| Maximum original-vertex displacement | 0 | 0.055519 model units |
| GLB bytes | 506,280 | 506,280 |
| SHA256 | `b2f8ff7f7024e1900445486e746d6fa255a74f5f4b3ac3695f87aed46d0df005` | `0f83def756e9d593a0ca4494e18dff9ddf34c63a795013a0f3303d1eec24b6b8` |
| GLB attributes | POSITION + NORMAL + COLOR_0 | POSITION + NORMAL + COLOR_0 |
| True Blender perspectives | 4 | 4 |
| True Three.js/Chromium WebGL2 perspectives | 7; 10/10 gates | 7; 10/10 gates |
| Physical Android/iPhone GPU | UNTESTED | UNTESTED |
| Art approval / release | REJECTED / NO_RELEASE | REJECTED / NO_RELEASE |

## Original remote proof independently checked

Final [Run259pp raw GitHub Actions artifact #14690276502](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44861742166/artifacts/14690276502) is **4,387,220 bytes**, SHA256 `744ba2430afe81d26b57ac75ce80538828b7c57090526cb8219ce4de116097ea`, GitHub digest and separately downloaded local bytes matching exactly. ZIP has **36 actual entries**, passes complete CRC validation, and all **34 signed files in its SHA256SUMS.txt** independently recomputed and matched. Independently re-imported A/B using Trimesh: each **one watertight genuine mesh of 20,000 real triangles, 30,000 unique edges**, and actual binary glTF with `POSITION`, `NORMAL` and `COLOR_0`. Both browser JSON reports had seven separate actual camera position records, seven distinct screenshot hashes and **10/10 gates true with no page errors**. All eight Blender render hashes and real mesh metrics are in `run259_real_3d_machine_report.json`.

Research branch holds the original [8-view **actual** Blender sheet](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run259-juvenile-neural-reference-color-back-relief-no-release/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run259-REAL-HY3D-PROJECTED-PIGMENT-POSTERIOR-ART_UNAPPROVED/run259_8_ACTUAL_NATIVE_BLENDER_VIEWS_ART_UNAPPROVED.jpg), eight raw Blender frames, 14 raw true Chromium WebGL2 screenshots, machine reports, full logs, SHA manifest and explicit NO_RELEASE flag. Actual binary A/B GLBs stay **only within the separate no-release Actions artifact**, not in app public deploy or main.

## Independent actual-pixel visual inspection: **ART_REJECTED**

I personally opened the final eight-view Blender sheet **and seven-angle B WebGL2 screenshot montage** and compared them to the real rightmost reference; this is independent of the automatically-green technical QA. The color projection turns the front moderately warm cream with a faint face, but introduces a very conspicuous **black vertical cleft/wing-shaped stripe along the bird's right side**, and the eye mapping makes dark **smudges/blurred closed-looking orbits rather than two clear dark alert eyes**. The heart border is warped and harsh, not an integrated soft heart disc. Side shows a large over-long **tapering adult wing/tail-like rear**; the fatness is still false from the side; rear remains pale and spike-textured, not high-quality layered cream down. B removes some spikes and makes the back smoother than A, **but it remains a featureless long pointed shell**, with no compact anatomical folded juvenile wing. Feet are unsupported and **no real eucalyptus hollow exists**. Neither A nor B passes natural multi-angle anatomic plausibility, real volumetric feathers, eye appearance, original reference resemblance or the intended pet quality threshold.

Actual experimental finding: source-image pigment projection is **not genuine volumetric down**, can introduce dangerous camera/UV side projection artifacts, and smoothing the posterior gives an unnaturally bland shell instead of convincing downy young-bird anatomy. This line is a **negative control**, not a new art baseline. The 3D format/graphics runtime passed but art categorically failed.

## Scope and next work

Comparison from exact Run258p research branch to Run259 branch before this audit showed eight isolated commits, 36 changed items all strictly under the #172 experiments subtree or the **new dedicated Run259 workflow**; **no changes to main, 251 species production, existing kitten prototype, original concept, vocabulary game or deployment**. Additions remain research-only. Extra external payment **USD 0**, no login/credit bypass, and source model/game-commercial redistribution rights **remain unverified**.

Further iterations need genuinely juvenile-shaped input or artist-generated genuine sculpt, real independently layered down groom, proper dark open eye anatomy with eyes in consistent positions and a natural old eucalyptus hollow support. Do not treat this Run259 projection/smoothing as an acceptable pet model. Physical iPhone/Android performance, memory, touch and thermals untested. **NO_RELEASE**.
