# Run386 — alternative TripoSR axis recovery — ART_REJECTED / NO_RELEASE

2026-11-26 Shanghai. Read main AGENTS, README, STATUS (207/251), exact v3 review/species profile and Run385 at 3990766f42f09dc7aa31efef61d913ec191bf9a0. Pinned rightmost cream mesoptile, developed heart disc, short buried wings, concealed tail, age unknown, science=false. Do not replace reference with v4/v5/v6.

## Actual independent-base experiment
Recovered the previously generated TripoSR control GLB from actual GitHub Actions artifact 14174978922 (Run92B), not a new neural inference and not the repeatedly modified Hunyuan/TRELLIS source. Its SHA256 matched the earlier report: df49cefcccb6f72b379400cd07053907040a0ef8adae46638c334143ab379346. Recovered 512x512 pupil-restored reference PNG from artifact 14599833411, SHA256 df6403266687be43268423461c4daf0672be88f4111db2f822b28c604e28d0d0. Inspected earlier four-angle render montage, exact reference crop and six newly rendered orthogonal views. The older reported sideways orientation was real: +Z faces camera, head toward +X, feet toward -X. Corrected with right-handed rotation (x,y,z)->(-y,x,z), then centered bounds. This is an independent existing neural mesh from a different model, not a new external generation.

Generated three actual native GLBs: rotated control, frontal reference reprojection on rotated control, and projected + 20 rounds Taubin smoothing (lambda .48, mu -.50, unique undirected edges and row-normalized adjacency). Reference foreground alpha bbox x75..435 y16..495; map new x and inverted y to reference bounds, bilinear sampling. Blend factor smoothstep(clamp((z+.02)/.22,0,1))*alpha/255, posterior neutral RGB (208,192,168) at 80% blended with 20% original color. Projection only front; no assertion that backside is observed. Retain topology, fix normals, export and independently reimport. VTK offscreen actual six orthogonal diagnostic renders and twelve front/45/90/back renders, view up Y, parallel scale .56, 320x320 each.

| Candidate | Vertices | Triangles | Bytes | SHA256 |
|---|---:|---:|---:|---|
| upright_control |15691|31342|628164|e5d0a0666440cb9c824b54b9177853a72f161b4e31aea0a2f5357a72a1398ae6|
| upright_projected |15691|31342|628164|5d2d0526ce4512063bedab595c1fdafb3cbf6f5a68088e5e426129bf4a567286|
| upright_faired_projected |15691|31342|628160|c18fd5929f907c831651d325ce313579cc93365113f59f78a2bfd5e073afdc7f|

All independently reimported watertight. Final max/mean displacement relative to rotated control .0160494/.00538634. Native mesh is relatively small but not a mobile validation.

## Actual visual decision
Inspected full six-axis sheet and 1280x960 three-candidate four-view render sheet. Rotation corrects gross sideways appearance: compact, recognizable upright bird, no long exposed adult tail. Source has distorted raised eye geometry, mottled scale-like surface, long vertical grooves and incorrect toe anatomy. Reference reprojection makes face and cream color closer but raised false eye structures remain, a hard projection boundary on flanks and a streaked back. Smoothing removes some ridges but yields waxy lumpy surface, poor heart-disc depth and unnatural feet. None show genuine natural soft cream down or correct glossy eyes; all ART_REJECTED. No new browser or physical phone tests after art gate failure. Avoid more repetitions of this base; prioritize independent appropriately sculpted juvenile geometry and reference-consistent eyes.

## Access / scope
Container DNS failed for github.com, api.github.com and huggingface.co; Blender absent; VTK, scipy, trimesh available. GitHub connector successfully retrieved actual old artifacts. New source scout: Grab3D owl CC0 https://grab3d.com/models/animals/owl/ is adult great horned owl with tufts and 400k–800k triangles, unsuitable; Innerscene https://www.innerscene.com/tools/library/3d-parts/owl-d696472a CC0 generic owl and 19.7 MB, not evidence of juvenile anatomy; ArtistFrog https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt explicitly says no AI, not adopted. No fresh external model download or paid invocation. No main, original concept, 251 species pipeline or deployment mutation.

Three full GLBs, 18 new PNGs, two scripts, metrics and contact sheets created in current working container; full binary model not uploaded remotely. This branch contains report and compressed actual-render thumbnail (next to report), not a release. 
- probe.py SHA256 3470882732a1af634fde60a16e5722a549bf5dd68f692536e660c7cacbf56c4f
- experiment.py SHA256 39fd7a5feac32086bd56bbbf5dd06cd55867016830046479536061d0f542f41f
- axes.jpg SHA256 48e2c2c6ebeb8cab22102bdd5514c40ddc7d8f282646e0456003839be8a0dc8f
- experiment_sheet.jpg SHA256 1e3f427643adebd39370a0383ac087ba79c5284a4a20cca61a342b0cef42a90b
- thumb.jpg SHA256 51cede5b0b9aa6c03b48377f3d5178c0e4ded836a6e9fb89d06d243ce5cb6ca3 (160x120, 3309 bytes)

ART_REJECTED / NO_RELEASE. Additional spend zero.
