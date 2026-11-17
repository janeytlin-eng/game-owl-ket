# #172 *Tyto castanops* v3 rightmost downy juvenile — Runs 123–124E actual artist source + rights investigation

**2026-11-17 / ART_UNREVIEWED / NO_RELEASE / no extra payment / no 251-species production edits**

## Repository and art-quality gate reread

Starting from the actual rejected Run122 isolated branch/commit `921666ad6be3a211c9048f995b9e309357bbdc0a`, reread `owl-pet/AGENTS.md`, `owl-pet/README.md`, original v3 rightmost juvenile target referenced at `owl-pet/design/concepts/172-tyto-castanops-v3.png`, and the complete Run122 four-angle/Chromium inspection. Its genuine 6,039,668-byte Blender GLB is still ART_REJECTED: rigid flat heart mask, out-of-plane eye rings, white snowball adult-like body, nearly absent short wing tracts, stippled microdown and unrealistic stump. Another procedural sphere or stylized SVG cannot satisfy the mandate.

This time investigated **independently authored, anatomically juvenile 3D source assets rather than further massaging failed primitive/AI geometry**. All probes performed actual unauthenticated HTTP GETs from GitHub Actions and classified full response type/magic bytes; no auth bypass or purchase. A metadata JSON or free listing was never treated as downloadable 3D geometry.

## Run123: artist-source real requests

Three successful research-only GitHub Actions attempts, final successful Run123C: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43990382914

Actual 10 official source HTTP probes covered CGTrader ArtistFrog `Free Baby Owl Sculpt` (real 236,060 polygon artist asset listed 2020-12-18), Sketchfab museum CC0 adult Tyto and search API for `barn owl`, `baby owl`, `owlet` and `tyto castanops`, and all 522 Poly Haven curated CC0 models. Technical outcomes: **zero 3D source files downloaded**. CGTrader listing and direct download returned HTTP 202 non-geometry HTML challenge; Sketchfab museum metadata 200 but official download endpoint 401 Unauthorized; Sketchfab search responses 200 metadata only, with zero matching `tyto castanops` models; curated Poly Haven model list had no relevant owl/chick meshes after filtering out the false-positive English “bowl”. The other lowpoly/adult listings cannot pass art gate.

Run123 full machine-readable response, primary audit, `NO_RELEASE.flag`, source metadata and SHA256 verification:
`research-evidence-run123-ARTIST-SOURCE-REAL-PROBE-NO_RELEASE/`. The Blender inspector source was also written and committed but **intentionally not invoked** because no legitimately obtained GLB was available; no rendered 3D or phone performance was invented.

## Run124: genuinely on-target free Japanese barn owl chick source, official access test

Found a substantially more anatomically relevant independent artist source: **りったいミーム / ゲアーナ — “走るメンフクロウのヒナ”** (running barn owl chick), `https://booth.pm/ja/items/6643539`. Public listing explicitly offers **`Menhukurou.zip` 1.05 MB for ¥0**, and points to the creator's actual VN3 user license. This is still a *different owl species* and its running pose would require appropriate sculpting/retargeting to match the original #172 perched tree hollow; do not claim exact character success.

Run124D successful actual Actions execution https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43991217432 . Seven real HTTP reads:
- BOOTH item page: HTTP 200, HTML listing **not a model**.
- Actual official free download action `https://booth.pm/downloadables/6814126?variation_id=11184857`: redirected to `https://booth.pm/users/sign_in`; no anonymous ZIP bytes. Login cannot be bypassed.
- Original Japanese, English and Chinese VN3 license PDFs: all HTTP 200, valid PDF binary, respectively 1,000,983 / 897,560 / 569,674 bytes, SHA256 recorded. They are **public terms, not the model**.
- Artist-made CC0 owl rig from BlendSwap: public listing HTTP 200; no downloadable mesh directly obtained.
- BlendSwap owl catalogue: public metadata 200; no usable chick asset.

The source-checker intentionally **does not commit external model bytes into public GitHub even if found**, until permission to redistribute is verified.

## Run124B/E: actual public VN3 license PDF extraction and rights threshold

Successful license extraction executed with real `pdfinfo` / `pdftotext` on Ubuntu on three SHA-locked source PDFs: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43991316805 . EN reference PDF 27,089 extractable characters, ZH reference 6,352, authoritative JP PDF 10,535, with per-locale rights excerpts in `research-evidence-run124b-VN3-ACTUAL-TERMS-NO_RELEASE/`. The English terms explicitly flag creator contact for both unmodified and modified digital content distribution (M/N categories), and state Japanese controls over translations. Independent legal confirmation for game-bundled WebGL/GLB reuse and public GitHub redistribution is still needed. **No rights clearance inferred** from the ¥0 price, the creator's permitted media-use list, or the fact these terms are publicly downloadable.

One intermediate Run124B rerun intentionally retained a `FileNotFoundError` for JP PDF in its *old* sparse checkout and a stale-branch push conflict (https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43991299194); the updated `124B` workflow explicitly includes the Japanese PDF and then passed all steps, archives, and SHA checks at run `43991316805`. Negative/retry records are not represented as aesthetic success.

## Strict outcome and isolation

The art gate requires a true continuous anatomical sculpt, cream down integrated with the heart-shaped facial disc, small dark recessed eyes, short down-covered wings, correct shanks/toes and eucalypt hollow support, consistent 45°/side/back, verified phone GPU WebGL and unambiguous rights. **There is still NO permitted, downloaded, reviewable juvenile 3D GLB for this source trial. Therefore no Blender four-view creation, no mobile QA, no approved sample, no release, no user-facing preview.** It would be false to count a marketplace thumbnail, screenshot or API result as a 3D deliverable.

Both sets of actual code, network logs, source JSON, PDF terms audits, step outcomes, SHA256 manifests and flags remain in Run123 and Run124 independent research evidence folders on this branch. All new files remain under `owl-pet/3d-experiments/172-tyto-castanops/**` or two dedicated `.github/workflows/owl-pet-172-run123*.yml`, `owl-pet-172-run124*.yml`. Original concept, 251-species production scripts, main branch, previous prototype, and deployed site were untouched. **Extra payment: $0.**

Priority after this gate: source a legitimately accessible truly sculpted Barn Owl chick (not an adult horned owl), secure author's explicit model redistribution/use rights if needed, inspect actual geometry with Blender multi-angle lighting, and only then validate optimized GLB and **real** mobile WebGL GPU. Do not re-label toy-like procedurally generated shapes as complete.
