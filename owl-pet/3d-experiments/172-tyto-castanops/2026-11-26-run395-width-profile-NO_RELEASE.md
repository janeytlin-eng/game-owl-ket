# Run395 — reference width-profile fit and sagittal hypothesis — ART_REJECTED / NO_RELEASE

2026-11-26 Shanghai. Read main owl-pet AGENTS, README, STATUS (207/251), concept listing (#172 v3 blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b), and prior Run394 at f0caeab00a0be9f3253bf370679510b7eb53d3cd. Recovered actual GitHub Actions TRELLIS artifact 14266706992 through the artifact download connector, 6.5 MiB ZIP. Viewed original 512px juvenile reference and four-view render. Source GLB SHA256 2893e95965a9c6e6fd3af5779c1ebf3b65a16b6cdaebf7c2f743e047b9fa78de; reference SHA256 e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8. Local torch CUDA false, bpy absent, DNS lookup for github.com/huggingface.co returned no address; direct web fetch of original image failed. Run161 evidence directory only contained screenshots/results/flags, no GLB. No paid calls or new neural inference. This is a controlled deformation of an actual recovered neural mesh, not independent new reconstruction.

## Actual experiment

Test whether reference-calibrated width alone, or width plus posterior compression, can overcome previous shape rejection. Use alpha >127 in original reference, normalize vertical height, sample 46 heights 0.06–0.96 and +/-0.024 bands; measure 1–99 percentile horizontal extent divided by total height on image and actual mesh. Smooth their ratio with Gaussian sigma 2 and clip to [0.73,1.35]. Interpolate by normalized vertex height t. Apply x *= 1 + 0.85*(ratio-1)*toe_weight, where toe_weight = smoothstep(clamp((t-.12)/.14,0,1)). For upright hypothesis additionally move posterior midbody in +z by .28*clamp((-z+.02)/.47,0,1)*exp(-((t-.42)/.30)^2)*toe_weight*height*.55, and upper body backward by .28*.16*height*exp(-((t-.82)/.17)^2)*toe_weight. This is not a measured side view; single-reference widths include perspective/pose bias. Texture converted to vertex colors, topology unchanged (37,475 source vertices, 40,623 faces). Export and reload native GLBs. VTK renders at 0,35,70,110,180 degrees at 360x360, fixed camera, diagnostic diffuse lighting (not browser PBR parity).

| Candidate | Mean absolute width/height error | Max displacement | GLB bytes | Triangles | Reload |
|---|---:|---:|---:|---:|---:|
| baseline | .195924 | 0 | — | 40,623 | source |
| width_fit | .077155 | .088984 | 1,088,084 | 40,623 | yes |
| width_upright | .077155 | .147124 | 1,088,084 | 40,623 | yes |

Width error is reduced on the same fitting samples, not an independent accuracy or perceptual score. GLB SHA256 width_fit 8f4b2667e045d87aed644b3ca385e78ad7a11577ce0a207034ce549385bea0af; width_upright e0f6133a8bed58f2f149c46d24a6e9e1c4377351d7d2b86c7235fdaaebfdbc0b.

## Actual visual gate

Inspected 1800x1080 contact sheet of 15 renders. Widening gives fuller head and torso, but flattens facial proportions, dark eye sockets remain, feather plates still look adult and rough, and feet stay unnatural. Upright posterior hypothesis visibly squeezes back and tail but produces a new angular indentation near the rear wing. Neither is visually acceptable. No phone WebGL test or release. Do not treat a numerical fit as successful artwork. Further width-profile optimization of this already rejected source is low priority; independent juvenile geometry or credible multi-view reference remains the actual bottleneck.

Full GLBs, source shape_gate.py and renders produced locally, not remotely archived. Script SHA256 314b2cf286a111e3d1981b63913d7670a40fb58e0bd7735d63db29e6d177668b; contact sheet SHA256 aadd7274e1010f4eb08898505c1d2aa7f12104925776e5d40cec6c29f2f4eb8b. Reduced actual JPEG 150x90, 2986 bytes, SHA256 6c2d9721df8db27a8d2008ba64bb50ad1fd8919ccc5f52ac241ad362fefed50d. Rows baseline, width_fit, width_upright; columns fixed camera views.

No modification of main, original concept, 251-species production or deployment. Extra paid cost zero.
