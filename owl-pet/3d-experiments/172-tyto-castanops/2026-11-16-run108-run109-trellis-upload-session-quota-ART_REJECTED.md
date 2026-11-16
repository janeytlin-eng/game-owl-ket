# #172 *Tyto castanops* v3 — Run108/109 free TRELLIS native GLB experiments — ART_REJECTED

**2026-11-16 Asia/Shanghai · RESEARCH ONLY · No approved 3D owl, no release, no extra spend.**

## Preflight: reread before running

- Rechecked `owl-pet/AGENTS.md` and `owl-pet/README.md`, inspected the actual `owl-pet/prototype/index.html` and `owl-pet/STATUS.md` on `main`. The existing interactive prototype is an older *cat* WebGL demo, not an approved baby owl.
- Re-read the authoritative `owl-pet/research/species/172-tyto-castanops-v3.md`. The target is the **rightmost** age-unknown mesoptile on the v3 three-owl image: thick cream down, broad heart-shaped facial disc, dark *open* eyes, compact crouch, down-buried short wings, concealed tail, both feet and belly supported by a mature eucalypt hollow lip. Its exact age and side/back details are not scientifically established.
- Reviewed Run99–102B true-3D coarse-mesh, local eye, groom, animation and WebGL failures, Run104 CPU TripoSR failure, Run105 matte/alpha failure, and the full Run106–107B free-service error audit. Specifically read the actual Run107B Python traceback rather than inferring its failure stage. Run107B `ReadTimeout` occurred in Gradio client's `process_input_files/_upload_file`, *before* TRELLIS model inference, so that attempt never tested model geometry.

## Run108 — actual corrected real remote request

Research branch: `research/owl172-run108-trellis-upload-timeout-fix`. Isolated script: `tools/run108_trellis_upload_timeout_fix.py`; dedicated branch-only Actions workflow. Reused the archived **actual rightmost v3 chick** image input rather than generating synthetic side/back impostors. Corrected upload-stage Gradio timeout with `Client(... httpx_kwargs={"timeout": httpx.Timeout(90.0, connect=25.0)})`, kept one anonymous public `trellis-community/TRELLIS` `/generate_and_extract_glb` call and no paid fallback.

**Actual execution:** [GitHub Actions run 43859726978](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43859726978). The corrected client (v2.7.2) reached the remote prediction stage, proving the previous upload transport timeout was surmounted. The remote Gradio application then returned **`AppError: FileNotFoundError`**. It does not reveal which upstream file was missing, so do **not** claim a model result or a known root cause. `run108_status.json` records `FREE_PUBLIC_ROUTE_BLOCKED_OR_FAILED`. No GLB, no mesh, no Blender render, no phone GPU acceptance. The genuine input, live 78 KB API schema, state, traceback, logs, SHA256 sums and validation are archived under `research-evidence-run108-TRELLIS-MIT-ART_UNAPPROVED/`. Branch evidence commit `e34f3f0d4019b8f88e9c49f26ad5b6523fef8193` was remotely read.

## Run109 — actual frontend-equivalent session & preprocess

Research branch: `research/owl172-run109-trellis-session-preprocess`. New isolated script `tools/run109_trellis_session_preprocess.py` and its own push-triggered Actions workflow. This tested a concrete hypothesis for Run108: the public frontend invokes `/start_session` and `/preprocess_image` *before* `/generate_and_extract_glb`, whereas Run108 skipped them.

**Actual execution:** [GitHub Actions run 43860121826](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43860121826). On the **same Gradio client/session**, `/start_session` succeeded (`()` response), `/preprocess_image` succeeded and returned a real 212,027-byte PNG, and the upstream `/generate_and_extract_glb` was actually invoked **once**. The preprocessed image was saved and visually opened: it shows a cream downy bird with recognizable heart face and two dark open eyes, but is a **single frontal photograph-like image with an isolated black background and exposed feet**, not validated side/back anatomy or hollow-lip support. SHA256 of provider-processed PNG: `a381f7d81c12ab91cd3474c20a288964f1f583cc086553882c16ac39958578be`.

The real upstream generation response was **ZeroGPU quota exceeded**: `120s requested vs. 91s left`, with `Try again in 6:58:06` (provider-reported at UTC 2026-11-16 11:42:48). Do not infer that quota will reset at any guaranteed absolute time; do not send another request before a normal reset, switch accounts, submit tokens to bypass quota, or spend money. This is a **transient provider quota**, not an artistic rejection based on unseen 3D geometry. The step-level status is `failed_stage=generate_native_glb`; no new GLB was returned. Source image, actual remote preprocessed PNG, live API schema, error traceback, log, state and SHA256 integrity checks archived separately at `research-evidence-run109-TRELLIS-MIT-ART_UNAPPROVED/`; 8 archived payload files passed `sha256sum -c`. Archive commit `d289647c824f2b6b1880153590d2edaf672e8eca` remotely read.

## Art, performance, license and production gates

**Zero new GLBs across Run108 and Run109; there is no 3D sample to show.** Do not treat successful CI, successful image preprocessing, static frontal image or actual upload as a visually acceptable 3D model. No fabricated geometry, SVG proxy, fake turntable, skeleton without sculpt, user-facing sample URL, PR merge or deploy. Neither four-view native Blender renders nor real iOS/Android phone GPU, touch, frame pacing, thermals, quality or animation gates have been passed. The source image rights, third-party model/output license, and globally valid distribution permissions remain separate release gates. Prior Hunyuan assets remain artistically rejected and subject to their own license restrictions.

Diff verified against `main` before this audit: 287 changed paths, **zero paths outside** `owl-pet/3d-experiments/172-tyto-castanops/**` and dedicated `.github/workflows/owl-pet-172-*` experiment workflows. The 251-species main production system, original three-owl concept, manifests, cat prototype and live deployment were untouched. No extra payment.

**Next safe experiment after ordinary free quota recovery:** Reuse Run109's working same-session initialization/preprocess path, allow exactly one bounded public generation, then only if a true GLB is downloaded validate binary, re-import and render the real native front/quarter/side/back geometry and inspect all views for downy cream surface, round baby body, proportional heart disc and supported feet. No mobile readiness or release claim until real phone WebGL QA and rights checks pass. Avoid repeating failed upstream submissions during the quota window.

**Final: REAL FREE TOOL EXECUTION / PREPROCESS SUCCESS / REMOTE QUOTA BLOCK / NO NEW GLB / ART_REJECTED / NO USER NOTIFICATION.**
