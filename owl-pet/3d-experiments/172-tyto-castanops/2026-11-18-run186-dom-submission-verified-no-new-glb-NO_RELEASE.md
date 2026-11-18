# #172 Tyto castanops v3 — Run186 independent operational review (2026-11-18)

**NO_RELEASE / NO_NEW_GLB / ART_UNREVIEWED / PHYSICAL_MOBILE_UNTESTED. No extra paid tools.**

## Read-before-run baseline
This run reread owl-pet/AGENTS.md, README.md, prior WebGL prototype, #172 v3 research record, Run181's seven-axis rejection, Run182's high-detail CC0 route failure, Run183's source-transport block, and the negative GLB fingerprint registry. The **rightmost** v3 mesoptile input was independently verified SHA256 `5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9`; no other animal/photo/sample input is permitted.

## Real operation: corrected UI, not a marketing CTA
Run184 clicked a landing CTA instead of submitting; Run185 attempted a regex with incorrectly doubled backslashes and saw no candidates. In Run186 we corrected `Fast\\s*&\\s*Private` to the real whitespace regex `Fast\s*&\s*Private`, audited the live DOM of buttons, selected the **visible** and enabled exact GENERATE / Fast & Private submit control, and clicked it.

[Run186 GitHub Actions real execution](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44315402110) recorded the real target image being uploaded (`source_bound=true`), two matching buttons (one hidden responsive duplicate and one visible), `generate_clicked=true`, and the UI immediately entering **Uploading your image… / GENERATING** at t=10.5 seconds. The browser performed 12 further polls across 202.67 seconds. No legitimate downloadable generated GLB appeared; the final provenance-qualified count was **0**. This proves the actual UI click and intermediate processing state, **not** that a remote GPU completed a successful inference. We observed no HTTP >=400 among the locally captured selected response records; those records did not include all third-party service responses, so a backend diagnosis cannot be made from them.

Provenance and evidence: [machine-readable result](research-evidence-run186-DOM-EXACT-SUBMIT-NO_RELEASE/run186_results.json), [actual browser state and button HTML](research-evidence-run186-DOM-EXACT-SUBMIT-NO_RELEASE/trellis2_state.json), [generated-step screenshot](research-evidence-run186-DOM-EXACT-SUBMIT-NO_RELEASE/trellis2_02_after_generation_click.png), [final screenshot](research-evidence-run186-DOM-EXACT-SUBMIT-NO_RELEASE/trellis2_04_final_ui.png), [SHA256 evidence manifest](research-evidence-run186-DOM-EXACT-SUBMIT-NO_RELEASE/run186_sha256_manifest.json), and an isolated 30-day Actions artifact. The Action uploaded evidence and committed the audit; no GLB was included or represented as accepted.

## Licence, spend, and controlled non-release
[Official Trellis2.dev terms, updated 2026-08-19](https://trellis2.dev/terms-of-service) say the service is free without registration, users retain rights to their uploads and outputs, and third-party models can impose separate terms; the page also disallows bulk automated scraping. This was a one-off interaction with a user-project-owned reference, **not** scraping, repeated bulk inference, account bypass or purchase. No credit purchase or paid subscription was used. Commercial reuse of any future actual GLB still requires checking the *specific underlying model licence*; mere marketing copy is not enough.

Run184's separate 3DAI Studio white-mesh attempt had genuinely submitted the uploaded reference but visibly reported `Generation failed. Try another image or setting.` by 25.7 seconds, and its textured mode was unavailable. Neither that source nor this run delivered an art-reviewable target model.

## Decision and next engineering gate
No new valid native GLB exists to inspect. Therefore do **not** run a fake art approval, simulated mobile FPS claim, or publish a geometry stand-in. Keep the accepted target criteria: continuous fluffy cream mesoptile, rounded crouching juvenile proportions, naturally integrated heart facial disc with dark eyes, believable wings and back from real side/rear cameras, solid supported underside and eucalyptus hollow lip, mobile-size WebGL load, *followed by* actual-device GPU review.

Prior Run181 textureless 26,016-triangle model remains explicitly rejected and must not be repackaged under a new name. The next meaningful route is a **new source-bound fully coloured three-dimensional anatomical juvenile base** with documented download rights, not further cosmetic reskinning of rejected topology. Avoid retrying landing-page buttons already disproven.

**Repository boundary:** This run changed only the `research/owl172-run186-actual-submit-locator-free-native` experiment branch, its #172 research evidence and one isolated workflow. main, 251-species production pipeline, existing WebGL prototype, and deployment were not modified.
