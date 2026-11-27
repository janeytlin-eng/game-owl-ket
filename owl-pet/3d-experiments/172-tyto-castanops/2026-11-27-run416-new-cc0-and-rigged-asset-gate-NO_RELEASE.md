# Run416 — independent CC0 and rigged asset source gate — ART_REJECTED / NO_RELEASE

2026-11-27. Read main owl-pet AGENTS, README, STATUS (207/251), concept directory, and Run415 immutable README and actual six-view before/after PNG (blob 7cb111dfae305a076e88e86c171efdaa374d2c78). Re-read and visually inspected actual #172 v3 concept PNG from main (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b). Right juvenile: cream fluffy body, compact body with no long visible tail, heart disc with fine brown rim, dark glossy eyes and feathered legs. The prior mesh still lacks correct facial detail, eyes and juvenile silhouette. No new smoothing/groom repetition on that rejected base.

## Executed independent asset acquisition and visual screening

1. Mint barn owl, published 2026-11-24: https://mint.gg/free-3d-models/barn-owl . Source reports CC0, static, 19,966 triangles, embedded four textures, 1,857,216 bytes. Actually opened front and three-quarter preview pixels:
   - https://mint.gg/free-3d-models/barn-owl.webp
   - https://mint.gg/free-3d-models/barn-owl-front.webp
   - Visible heart disc and dark eyes are useful references, but smooth surface, adult golden wings, projecting tail, bare toes and fused display pedestal silhouette do not match the juvenile. The pedestal may or may not be a separate mesh; not verified. No side/back evidence.
   - Actual GLB endpoint https://cdn.mint.gg/owned-artifacts/84b573359bed07b2dbee22e143ac9fd79a000e2ae4c10d7d88077a5f36902f53 ; web fetch rejected content type model/gltf-binary (400); direct file download separately attempted and failed. No binary recovered.
2. Vinish rigged barn owl: https://vinish.dev/free-3d-models/birds . Source reports 52,276 triangles, ~2.5 MB, CC BY 4.0 with attribution and six animation clips.
   - Actually viewed https://vinish-models.pages.dev/birds/barn-owl.webp . Adult body, mottled wing surfaces, long naked legs and blocky feather edges; not an acceptable juvenile base. Rig could be interesting as an implementation reference, but no verified joint or clip data.
   - Actual GLB endpoint https://vinish-models.pages.dev/birds/barn-owl.glb ; web fetch rejected model/gltf-binary (400); direct file download separately attempted and failed. No binary recovered.

Both source-reported licenses and metrics are not independently verified from GLB. Preview images are provider renders, not locally rendered geometry. No assets redistributed. Rejected based on observed appearance, not on hypothetical mesh topology.

## Local capability checks

Actual DNS lookups github.com, api.github.com, huggingface.co returned errno -3 Temporary failure in name resolution. Local blender not on PATH, no bpy, diffusers, transformers, pyrender or moderngl modules; torch, trimesh and cv2 available. No Hugging Face cache listing. GitHub connector remains able to read project source and archive text. No external paid generation or inference called.

Decision: ART_REJECTED / NO_RELEASE. No new actual role model, no mobile WebGL test. Do not substitute source preview images for the requested 3D character. The two new binary acquisition routes failed; the previews also fail juvenile identity. Future candidates should first meet juvenile silhouette, down and face gates before pursuing costly download/rigging. No fee, no changes to main, original concept, species pipeline or deployment.
