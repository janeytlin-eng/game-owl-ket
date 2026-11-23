# Run329 — local continuous implicit sculpt and down geometry A/B — ART_REJECTED / NO_RELEASE

Date: 2026-11-24 Asia/Shanghai. Status: TWO_NEW_NATIVE_EXPERIMENT_GLB / VTK_16_VIEW_REVIEW / WEBGL_TEST_BLOCKED / ART_REJECTED / PHYSICAL_PHONE_UNTESTED / NO_RELEASE.

## Actual preflight
Read main owl-pet/AGENTS.md, README.md, STATUS.md, research/species/172-tyto-castanops-v3.md, research/reviews/172-tyto-castanops-v3-review.md and Run328 audit at 33aa76a5ca4322ef26351f60db2ecf0ffc416d74. Opened the full original v3 concept image through the GitHub connector (original Git blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b). Visually confirmed rightmost cream-white chick, heart disc with dark eyes and brown feather rim, thick fluffy body, short down-buried wing, concealed tail, supported toes on eucalypt hollow lip. No exact age or science=true claim. Current species-production status 203/251; left entirely untouched. Run328 adult donor rejected; do not recolor an adult donor.

## Actual local CPU experiments
Environment: NumPy 2.3.5, SciPy 1.17.0, scikit-image 0.26.0, Trimesh 4.11.1, VTK 9.6.2. Blender/bpy unavailable, CUDA false; ordinary raw GitHub HTTPS from the local container failed DNS resolution, but the actual concept was opened via authorized connector. No external paid service. Instead of another download of an adult bird, constructed an original experimental continuous implicit volume using smooth unions, a hand-defined heart-disc surface with orbital relief, a tapered lofted beak, separate eyes and thousands of non-billboard tapered 3D down barbs. This is a deliberately rejected procedural study, not a professional hand sculpt, and no simple primitives are presented as a finished asset.

A used periodic sculpt relief; actual eight rendered views show repeating diagonal corduroy ridges. B replaced these with two scales of random smoothed volumetric noise, softened face relief, reduced eye protrusion and thinned/lengthened barbs. Both physically generated and reimported as native glTF2 GLB via Trimesh. Both body meshes watertight. Each full scene had 10 geometries. Real VTK offscreen camera render at yaw 0,45,90,135,180,225,270,315 for each model, 480x520, sixteen images total. Both 960x560 montage images were opened and visually inspected, not inferred from geometry counts.

| actual result | A | B |
|---|---:|---:|
| Body triangles | 79980 | 75232 |
| Face triangles | 10080 | 10080 |
| Down barbs | 9380 | 9319 |
| Full GLB triangles | 154212 | 149098 |
| GLB bytes | 3309764 | 3205540 |
| Real VTK views | 8 | 8 |

A GLB SHA256: 4b336a58cd6b340467b36c4e81a47d04e72714a25afe1e7ffcde45455cbf5d3b
B GLB SHA256: ba0e7988538bb574f6667dc73026225c178177dbb9f08b909aa82331a25c5c54
A original eight-view montage SHA256: 241a844716d3239d00cbba2c86b4ac30819212a00300056de7589122e317f6c6
B original eight-view montage SHA256: b23364a5d7c4d579b69869dfc97b298595c82788e71c9854e0568a88e77e0584

## Independent art rejection
B reduced the unnatural repetitive ridges but still looks like a cream-colored woolly toy rather than the specified realistic chick. The heart disc reads as an attached mask, eyes and bill remain simplified, side/back show a generic bulky ellipsoid rather than convincing shoulder and buried short-wing anatomy. Down is mostly prickly points/patches rather than soft layered mesoptile. Feet and tree support are not modeled. No target-quality candidate, no rig, no mobile performance pass. Both A and B ART_REJECTED. Do not use either as released art; these are negative controls, not a substitute for a professional organic sculpt.

A local real Chromium/Playwright WebGL2 GLB-parser draw attempt was made for B in a 390x780 mobile-shaped viewport. Browser navigation to the local HTTP server was blocked with net::ERR_BLOCKED_BY_ADMINISTRATOR, before WebGL execution. Respect this environment restriction; no bypass attempted. WebGL views 0; VTK views are not WebGL views. No physical Android/iPhone testing. No web deployment.

## Independent source and evidence archive
Exact executed B source [sculpt.py](run329-local/sculpt.py), local SHA256 63d7cffe5cfbab2f9e809c075002cf44d573840bdb371c07de512ce50f9045ca; Git blob 6b664207cf59087a1afa9922cc0cecda789b51f7 matched local git hash-object. Exact executed [render.py](run329-local/render.py), local SHA256 69d045af6b816cf042e900a6bb9aa9343c5a8e166d5c1c5f32d6ab75e1c05019; Git blob 6f53064040f10201a20714b97f6f12906863386f matched local git hash-object. Both remotely reread. [B-to-A patch](run329-local/B-to-A.patch) reconstructs actual A from B, A source SHA256 62d01c8bc6b4b94369adfe2f7cde5c6b7dd43ba6ccc9426afdc63cffb262919f. Use separate folders for A/B because both scripts write the same GLB/diagnostic names. Run python sculpt.py and python render.py, or copy source and apply patch for A before execution. Pinned package versions above aid reproducibility; cross-environment binary identity is not guaranteed.

[Actual B eight-view thumbnail bytes](run329-local/actual-B-eight-view-thumbnail.jpg.b64) are the base64 encoding of the 192x112 downsampled JPEG derived from the actual rendered contact sheet (2101 decoded bytes, SHA256 d94eb0e2bc1f04553188d9c9ec3d9f6f803db327e979793ac6104a1fecda4cb7). Base64 remote readback exactly matched the submitted 2804 characters. Decode with base64 -d actual-B-eight-view-thumbnail.jpg.b64 > B-thumbnail.jpg. This is compact research evidence, not an art release. Full two GLBs and full-resolution montages were produced locally but not uploaded to GitHub in this run; the exact reproducible source, reverse patch, thumbnail and measurements are archived instead. No remote CI or independent phone pass claimed. No new paid usage.

No writes to main, 251-species production, original concept, kitten prototype or deployment. All writes isolated under this experimental branch and #172 directory. New native procedural research GLBs = 2; new approved chick GLBs = 0; user-deliverable samples = 0. NO_RELEASE. Future work should prioritize manually sculpted or legitimately accessible age-correct anatomy and multilayer feather grooming, not repeating simple smooth-volume perturbation.
