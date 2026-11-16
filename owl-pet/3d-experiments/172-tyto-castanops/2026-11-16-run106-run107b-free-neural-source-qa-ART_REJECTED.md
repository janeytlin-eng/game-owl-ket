# #172 *Tyto castanops* v3 — Run106–Run107B real free 3D neural source QA — ART_REJECTED

**2026-11-16 Asia/Shanghai. Research-only; no generated 3D character approved or released.**

## What was verified before attempting new work

Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, and Run99/Run102/Run105–105B evidence/audits. The on-repository `owl-pet/prototype/index.html` remains an unrelated, earlier small-cat WebGL prototype, **not** an approved 3D owl. The original #172 v3 concept targets its **rightmost** cream second-down age-unknown chick: broad heart-shaped facial disc, open dark eyes, plump short-winged body, hidden tail, soft feather halo and stable toes on a wide mature eucalypt hollow. A single concept view never verifies side/back anatomy.

The previously generated Run99 Hunyuan source was actually visually reopened from its independent four native Blender Cycles views. It is a credible *rough* true-3D bird form but is gray, rigid, elongated from the side, too rough and badly articulated at toes/eyes; it is not a showable infant pet. Run105's RGBA attempt generated a true GLB with catastrophic cuboid shape, while Run105B's RGB neutral-matte correction hit free public ZeroGPU quota. None were accepted. No main or 251-species production paths were touched.

## Run106: first live Stable Fast 3D attempt, actual public API failure

Built new standalone `tools/run106_sf3d_alpha_juvenile.py` and dedicated no-cost GitHub Actions workflow. Reused only the actual #172 rightmost chick from the archived Run103 foreground, converted it to a true 512×512 **RGBA input** with preserved dark eyes and cream down rather than generating fake turntable images. The actual image was directly inspected from its base64 evidence in Action logs; it correctly depicts the target chick with open eyes and heart face. Archived SHA256 input: `e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8`; source RGB pixels 548×548, alpha coverage at 64×64 preview **0.5556640625**.

Anonymous live `stabilityai/stable-fast-3d` Gradio client connected and the public API schema was saved. Original `/run_button` call incorrectly supplied seven parameters although **live API exposes five public parameters**; backend responded `AppError: 'AttributeError'`. This is an actual technical failure, **not** a successful 3D model. Standalone run [43823632847](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43823632847) archived the input, source code, schema, traceback, execution log, status, rejection flags, SHA256 manifest and checksum validation under `research-evidence-run106-SF3D-RGBA-ART_UNAPPROVED/`. No GLB and no native render exists.

## Run106B: corrected five-parameter public session, remote failure

New standalone branch, script `tools/run106b_sf3d_stateful.py`, and workflow corrected `/run_button` to five live parameters. First called the real public `/requires_bg_remove` to initialize session state; the provider **did respond** with visibility update values and the session-preprocess state was recorded. The single downstream genuine /run_button inference failed with `AppError: The upstream Gradio app has raised an exception but has not enabled verbose error reporting.` Do not attribute its exact underlying cause without provider logs. Archived second independent probe [43823909018](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43823909018) in `research-evidence-run106b-SF3D-RGBA-ART_UNAPPROVED/`. **No GLB was returned**; no Blender renders, no user sample.

## Run107: inspected TRELLIS free original public endpoints, discovered API change

Switched to another public no-charge route, `trellis-community/TRELLIS`, with a separate reproducible Python script and Actions workflow. Actual remote `Client.view_api` succeeded; it revealed this live Space does **not** publish the older pair `/image_to_3d` and `/extract_glb` expected by the script. The script stopped correctly before false generation and archived the real **78 KB endpoint schema** and error `RuntimeError: Public TRELLIS demo missing required native mesh generation/extraction APIs`. The live endpoint instead offers `/generate_and_extract_glb`, which directly promises video/3D/download outputs; this was a meaningful interface discovery, not a model. Evidence: `research-evidence-run107-TRELLIS-MIT-ART_UNAPPROVED/`, run [43824188161](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43824188161). **No GLB exists.**

## Run107B: corrected native GLB endpoint, actual live inference attempted, timed out

Created and executed `tools/run107b_trellis_direct_glb.py` plus `.github/workflows/owl-pet-172-run107b-free-trellis-single-step.yml`. Called the **actual current** `/generate_and_extract_glb` endpoint once through anonymous public Gradio with the correctly formatted ten public inputs (real #172 RGBA image; no multi-image extras; seed 172; official default guidance, steps, simplification and 1024 texture). The endpoint returned **`ReadTimeout: The read operation timed out`** during the request. This is a transient transport/provider failure; do not infer model quality, a provider quota problem or an output from it. Run [43824500100](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43824500100) completed as an evidence-archiving run, not a generation success. Actual `research-evidence-run107b-TRELLIS-MIT-ART_UNAPPROVED/` includes input, current live API schema, complete traceback, status, log, explicit rejection gate and SHA256 checks.

## Technical result, security and release gate

**Four separate actual external service/API exercises, zero returned new GLB assets.** A green CI job only indicates that exceptions and evidence were captured, NOT that generation, artistic quality, side/back, true-WebGL frame pacing or release passed. All Run106, 106B, 107, 107B outcomes are `FREE_PUBLIC_ROUTE_BLOCKED_OR_FAILED` and **ART_REJECTED** by absence of renderable 3D. No SVG, primitive stand-in, invented geometry, synthetic turntable, paid generation, account switching, token/quota avoidance or new site deployment.

The external providers' published weight/software licenses and model output use require **individual review** (the original project's artwork rights matter too); assume neither unrestricted commercial redistribution nor phone readiness. No iOS/Android physical GPU, touch, memory/thermal, frame pacing or animation acceptance can be claimed. The existing Hunyuan asset additionally carries Tencent community-license geographic/use constraints, separate from these two tools.

All new branch changes are confined to `owl-pet/3d-experiments/172-tyto-castanops/**` and dedicated `.github/workflows/owl-pet-172-*` research workflows. Original three-owl plate, 251-species production automation, production manifests, cat prototype, and site have been left unchanged. The comparison against `main` reports no files outside the approved isolated research namespace.

**Next meaningful route:** retry the correctly discovered TRELLIS single-step native GLB request only on a normal free-service recovery, and then actually reimport GLB, produce genuine front/quarter/side/back Blender renders and physically inspect the complete bird before any user-facing link. Alternatively, use an explicitly licensed professional young-owl sculpt with real natural fluff, eyes and perched cavity; do not keep flattening or recoloring defective existing geometry.

**Final: RESEARCH ARCHIVED / NO NEW GLB / ART_REJECTED / NO NOTIFICATION.**
