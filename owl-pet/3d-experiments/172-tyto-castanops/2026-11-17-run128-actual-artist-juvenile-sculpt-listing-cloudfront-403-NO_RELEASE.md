# #172 Tyto castanops v3 rightmost mesoptile — Run128 (2026-11-17)

**Actual zero-cost experiment: two creator-listed juvenile 3D sculpt sources were opened with fresh Chromium in GitHub Actions. Both publisher websites returned CloudFront HTTP 403. No authorized model download, no native GLB, no four-view art review. Final `ART_UNREVIEWED / NO_RELEASE`.**

## Read-before-run and boundary
Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/research/species/172-tyto-castanops-v3.md`, and the verified Run126–127 technical/art rejection. Prior Run127's CC0 owl model is a useful 12-animation/skin/LOD engineering donor but demonstrably a horned, rigid toy owl; no cosmetic repaint is a valid substitute for the age-unknown, cream-white, heart-disc juvenile on a real eucalypt hollow. Goal stays true 3D, correct integrated heart facial disc, down-buried wings and tail, reliable 360° anatomy, convincing delicate cream down, licensed use, optimized mobile WebGL/physical GPU quality.

## Actual independent free-asset access experiment
Source candidates selected for their claimed artist-made baby-owl geometry rather than another toy/adult model:

1. ArtistFrog, "Free Baby Owl Sculpt" (`https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt`). Search-indexed public listing describes a high-polygon BLEND/FBX/OBJ baby sculpt, but a search snippet is **not a downloaded or reviewed asset**.
2. richardshaw1918, "Baby Owl Animated Black" (`https://www.cgtrader.com/free-3d-models/character/man/baby-owl-animated-black`). Search-indexed listing describes an animated barn-owl kid; the listing claims a free download under royalty-free/no-AI terms, not confirmed rights to redistribute raw GLB.

Run128 [actual GitHub Actions](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44016132691) installed Playwright Chromium, **actually navigated both exact official listing pages without authentication**, attempted to find a visible authorized free download control, inspected HTTP response/title/body, captured two real screenshots and wrote machine-readable source verdicts. Both returned HTTP **403**, CloudFront `ERROR: The request could not be satisfied`; neither site delivered its published listing to the runner, so there was no button to click, no file event and no mesh. This is a publisher/CDN access barrier from that runtime, **not proof that the listed assets do not exist**. We did not defeat CAPTCHA/CloudFront, invent direct file URLs, use private APIs, authenticate, buy, or download any licensed/paid pack.

Source verdict evidence: `research-evidence-run128-REAL-JUVENILE-ARTIST-SOURCE-NO_RELEASE/run128_source_access.json`; original page screenshots, real console log and SHA256 records are in the same directory. Six archived evidence items passed independent `sha256sum -c`. No third-party raw files are re-hosted.

## Gate and next useful direction
- **Actual 3D model obtained this run:** none. No rendered four-view, no physical-phone WebGL, no distributable license verification. Do **not** infer a quality pass, append source to the successful model gallery or publish a screenshot as a model.
- Both third-party listings say "Royalty Free (no AI)" in indexed descriptions. Neither license is a blanket authorization to publish standalone derivative model files; actual terms and downloaded source would need inspection.
- Source acquisition should move to artist-controlled no-login downloads carrying an explicit commercial redistribution license, preferably a real 3D downy Tyto sculpt; otherwise professional native sculpting with direct four-view evidence, not programmatic sphere/flat-mask assembly. Previously blocked BOOTH/BlendSwap/login sources do not become accessible merely by repeated requests.

## Isolation
Research branch: `research/owl172-run128-true-juvenile-sculpt-official-access`, based on Run127 `5a6fc314f05ebd4f90d3e37a5d0c1662af6e33f1`. Source code: `tools/run128_actual_baby_owl_sculpt_access.py`; dedicated workflow: `.github/workflows/owl-pet-172-run128-genuine-chick-sculpt-source-qa.yml`. Automatic evidence-only commit: `a1a326e92dfcb7bc0f603bd1606f36ce0d302794`; real workflow concluded success. All branch changes relative to Run127 are confined to this #172 research/experimental work and workflow; no edits to `main`, 251-species production, original concept, existing prototype, or live site. Added external spend $0.

**No notification-worthy character sample in this run.**
