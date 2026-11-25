# Run378 — alternate Hunyuan3D base with depth-aware vertex coloration — ART_REJECTED / NO_RELEASE

2026-11-26 Shanghai. Parent bbef01902679c246d07925f41572713fb5dceda7. Read main owl-pet README, STATUS (206/251, 45 remaining), AGENTS, #172 v3 review and Run377. Target cream mesoptile, heart disc, short buried wings, concealed tail and supported feet; exact age unknown, science=false. No extra spend; no production or deployment changes.

## Different real mesh recovered
Recovered GitHub Actions artifact 14599833411 from [Run233](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44668960253), official Hunyuan3D-2mini Turbo CPU inference. Actual 4,962,588-byte GLB SHA256 0e6eedf3ff0b95269555c590c34e996fdc584986d2912f589d817c6ba3b6a02c matches prior report; 137851 vertices, 275630 triangles. Viewed prior seven-view sheet, front render and both recovered source images (Run233 eye-restored source; Run139 original juvenile crop recovered from artifact 14321440568). This is a genuinely different neural base from TRELLIS.2, NOT a newly executed neural inference. Current local tools trimesh, scipy, VTK, Xvfb and Chromium; no Blender or GPU detected, DNS queries huggingface.co/api.github.com returned no addresses. No external paid requests.

## Actual test and iteration
Preserved original geometry and assigned native vertex RGB/A. Front +Z, upright +Y; manually register eye, face and body using source pixel landmarks from Run233 source and actual front render. Nearest opaque source pixels via distance transform. Piecewise linear source y mapping from mesh y [-1,-.65,.10,.5,1] to [490,407,234,144,20]; source x center interpolates y [-1,-.4,.05,.5,1] to [252,254,277,289,282] plus 230*x. Sample bilinearly. Rear and side tint from actual feather patch [266:365,180:260], median RGB [176,146,116], plus [16,14,10] or revised [42,42,40], plus seed378 Gaussian-filtered 3D noise (64 cubed, sigma .75, standardized, amplitude RGB 8,7,6). This rear color is synthesized, not a recovered rear photograph. Front visibility estimated using max Z per x/y bin, 5-pixel max dilation and normal direction, with smoothstep taper. For soft/strong, blend front projection by .5/.8; retain strong front face coloration. Hard face mask caused obvious side striping. Third variant cream replaces the hard mask with smoothstep products across y,z,abs(x), tightens normal taper and raises base cream values. All three files actually exported and reimported as native vertex-colored GLBs, unchanged 137851 vertices/275630 triangles. Not a flat billboard.

Actual 12 VTK Xvfb renders, 420x420, 0/45/90/180 degrees from +Z, y=.15 camera offset, parallel scale 1.18; rendered distinct real meshes, all images have >1400 unique RGB values. Visually examined both sheets. Registered pupils and face recognizable from front; side projected stripes reduced but still visible; rear color brighter in cream. Rejected all three: strong adult-like folded wing relief, flat/pronounced face rim and mismatched eyes at side angle, stiff body surface rather than fluffy down, feet broad and insufficiently feathered, rear silhouette too sloping. Geometry has no new feather grooming, no scientific rear reference. No mobile WebGL or physical phone test for these variants; visual gate fails first.

## Local files and checksums
All three GLBs 5514288 bytes:
- soft.glb e28d85bcc8ff04b73778cde7fb6a1a3038e2fbbfa9f57392fa88a6223c9ed1de
- strong.glb 3bff21973c7bcbd27dec6ee60980de0d931c1b16b692b07e1028bd3c7adae0cc
- cream.glb 76f3206d659629f9e53d12094a4b4ac75693820697f01bbb59664e7ccc0dd974
- paint.py b870752773ad4bba8d6a75d3982d801ed64b971636e2aad149731a485303031b
- refine.py 4a1e9d144ab3b7c5c0e8d980186a4042a39f5cda9016556f82910d468eb2235e
- render.py c530147b7d7a7c4d2ac408c71e084a8dadddc442213282971ee63a8f400f4579
- render-cream.py 25bfe1189f7714113ef9e541d4618c4cf33750b87598ec16a2315eeb2e1e49ff
- sheet.jpg 553f36a009faece0bc12cffa6fe0adf32c81704e3b7a47f4f39260cb5d625b2d
- cream-sheet.jpg ca9ccf1269c0c39eb4745c9c9de2dfb268e5daee295be8ea60a191649389ac47
- archived actual 192x51 thumbnail SHA256 93a6d02e52b6b0b7324383e426e1eebc842d5b548c4181c4455ecdae64a0a87f

![Actual cream variant four spatial renders, not approved](run378-cream-fourview-ART_REJECTED.jpg)

Full newly colored binaries, scripts and renders are local only. Original mesh remains in Actions artifact subject to retention. Next: prioritize actual down surface and buried wing geometry, not merely stronger projected color. No main, original concepts, production, deployment or automation changes. ART_REJECTED / NO_RELEASE.
