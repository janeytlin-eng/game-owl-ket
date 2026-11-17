# #172 *Tyto castanops* v3 — Run143 independent zero-fee text-conditioned real-3D probes (NO_RELEASE)

**17 November 2026, 21:58–22:01 Asia/Shanghai. Final ART_UNREVIEWED / NO_RELEASE. No valid GLB generated; no owl sample approved or posted.**

## Preflight — not a restart of failed sculpt tricks

Read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/research/species/172-tyto-castanops-v3.md`, and Run142 real PBR anatomical rejection. Prior Run89 hair/baked-ribbon failure, Run119 neural/down failure and Run125B unauthenticated official BlendSwap free-chick 403 were checked to avoid repeating those doomed routes. The previous v3 source crop has pinned SHA256 `e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8`; its target has open round dark eyes, softly integrated broad heart disc, thick cream down, short down-hidden wings, concealed tail, compact crouch and supported belly/feet on aged eucalypt hollow lip. Run142's real glTF failed at least eye openness, rear soft down, adult-like wing/tail and foot support.

This run tested a **different conditioning mechanism**: detailed text explicitly calling for *young* Tyto anatomy rather than yet another resampling, whitening, or strand-groom of an anatomically wrong single-view model. Text-only output would still require visual comparison with the original v3 image and the independent morphology/rights/mobile gates. No substitute concept image or generic toy asset could be approved.

## Actual execution (new isolated branch, no purchase)

Branch `research/owl172-run143-free-text-neural-reconstruction`, derived from immutable Run142 audit commit `56b14890d374b9816ec1533db1bf016e835b6cd9`. Executable experiment `tools/run143_free_text_neural_3d.py`, new dedicated Actions workflow only. The prompt states both **open** round eyes, thick cream-white juvenile down, a developed feather-integrated Tyto heart mask, very short buried wings, tail hidden, no ear tufts/long remiges, close-tucked feet, compact crouch. No text-generation service received a paid API key or authorization to spend.

1. **three.ws keyless draft 3D API (new source)**: actual unauthenticated `POST https://three.ws/api/3d/generate` received **HTTP 200** with explicit `free: true`, a real pending job, draft status, and ETA. The subsequent real job poll returned HTTP 200 JSON `status: "error"` and message **"3D generation hit a snag, please try again."** No GLB URL or model file. The API offer to upgrade to a paid tier was not used. The first request took 44.85 seconds. All returned response bodies/metadata and the full execution trace were captured, including the provider-side error. The local `run143_three_ws_status.json` retains a stale outer `"status": "STARTED"` despite the **inner polled response explicitly being ERROR**; classify correctly as **UPSTREAM_GENERATION_ERROR** and do not confuse HTTP success with 3D success.
2. **3D Valley genuine public no-signup text-to-3D browser**: actual Chromium Playwright opened `https://3dvalley.com/tools/create/text-to-3d`, found and filled the live description `textarea`, and clicked the genuine **Generate model** button. UI then reported **"Today's free GPU time is used up"**, with reset **within 24 hours** (website displayed tomorrow at 02:00 PM at the latest, provider clock unspecified). This was verified by captured final visible text and page screenshots. Status: **FREE_DAILY_QUOTA_EXHAUSTED**. The site offered paid credits; none were purchased, and no attempt was made to bypass daily limits.

[Actual GitHub Actions Run143](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44098114119) completed with each step successful as an **evidence collection / failure quarantine job**, not generation success.

## Negative quality gate and evidence integrity

**Neither source returned any actual valid GLB.** Therefore actual Blender import, four-view Cycles render, 3D model comparison, Three.js screenshot, and physical-phone WebGL GPU checks were **correctly skipped**. Do not invent triangle counts, PBR materials, moving eyes, native down/fur or visual acceptance. Do not publish an SVG, 2D preview, primitive assembly or a prior rejected GLB to fill the gap.

The isolated research archive `research-evidence-run143-FREE-TEXT-3D-CHICK-STRICT-NO_RELEASE/` contains **12 SHA256-verified files** (run logs, initial/polled API response records, actual browser screenshots, public UI text, status JSON, skip reason and explicit `NO_RELEASE.flag`), plus the checksum verification log. No third-party binary is tracked. Fees paid: **zero**. No model redistribution claims are made.

Change-scope comparison against Run142 showed **16 changed files, 0 outside** `owl-pet/3d-experiments/172-tyto-castanops/**` and this dedicated `.github/workflows/owl-pet-172-*.yml` workflow. `main`, the 251-species production process, the source v3 concept, the cat/WebGL prototype, game files and public deployment remain untouched.

**Final ART_UNREVIEWED / NO_RELEASE.** The new no-account free textual route has been exercised and its exact failure classified. A later zero-fee opportunity is a single permitted retry of the upstream error with a simpler prompt, or resuming 3D Valley only after its stated allowance reset; neither upstream error nor temporary quota justifies a recurring hard-block designation. Continue to require real mesh + independently inspected front/45°/side/back softness, supported juvenile morphology, confirmed redistribution rights, and on-device WebGL checks before any user-facing character sample.
