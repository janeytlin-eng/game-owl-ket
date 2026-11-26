# Run385 — implicit volumetric reconstruction — ART_REJECTED / NO_RELEASE

2026-11-26 Shanghai. Read main AGENTS, README, STATUS (207/251), exact #172 v3 review and Run384 at 0f884021888352ef92cfc65f5d2cde4b41564c36. Exact review: cream thick mesoptile, heart disc, short wing buried under down, concealed tail, age unknown; science=false. Recovered the source GLB and pupil-restored reference PNG from actual Actions artifact 14599833411; visually inspected source seven-axis renders and reference. No independent new neural base acquired; container DNS lookup for github.com and huggingface.co returned no addresses. Blender absent; VTK, scipy, scikit-image, trimesh available. No paid generation or purchase.

## Executed experiment
Rather than another vertex-space compression or feather-card density increase, reconstruct a continuous implicit surface from the neural base using volumetric signed distance and morphological closing. VTK polydata image stencil sampled closed mesh at spacing .014, origin (-1.05,-1.15,-1.1), dimensions 151x165x158. Signed distance = inside EDT minus outside EDT times spacing. Close with dilation sdf>=-radius followed by EDT(dilated)*spacing>=radius. Gaussian filtered closed SDF blended with original SDF using smoothstep mask protecting face and feet: S(t)=clamp(t,0,1)^2*(3-2*clamp(t,0,1)); w=S((.55-Y)/.4)*S((Y+.91)/.23)*(1-S((Z-.35)/.28)*S((Y+.15)/.4)). Marching cubes at zero; retain largest component, fix normals, export real GLB and independently reimport. Two radii .10/.20, sigma 1.8/2.8; after seeing voxel bands in first 10 renders, third variant Gaussian smooths original SDF with sigma .95 before mixing, radius .20/sigma 2.8. Vertex color from exact front reference projected via u=(x+.784)/1.555*358+75 and pixel row=(.988-y)/1.988*480+16, alpha blend S((z-.25)/.37) over cream (.84,.78,.69). Actual VTK offscreen five angles each 0/45/90/135/180 degrees (15 renders total), view up Y, focal origin, parallel scale 1.17. Not browser/mobile acceptance.

| Candidate | Vertices | Triangles | Bytes | Volume | SHA256 |
|---|---:|---:|---:|---:|---|
| closure_small |74310|148632|2973568|2.259185|bfdb6a2771a795da6da1368e4cedb24139639b0a318b215ca9753e8e66a0dae5|
| closure_large |73712|147436|2949648|2.267018|4b25f6be29f2ab3b9039daf341ae03dea621ba4a0fcdf238cf9ca3a4d28b14de|
| closure_antialias |71784|143564|2872336|2.265409|5bb1f1aed91dd984fb980f0d9cbb2745769d710dc52c2b33eebe864453bca83e|

All reimported watertight. Original volume 2.255995, 275630 triangles. Final retains volume within +0.42% and removes 47.9% triangles relative to original; this is not an independent neural asset.

## Actual visual review
Viewed full 1600x640 and 1600x320 render sheets. Larger closing softens adult wing groove relative to smaller closing. Both first variants show pronounced voxel contour lines on crown and feet. Antialias variant largely removes contour lines but looks like smooth clay with projected frontal colors; side wing outline still visible, heart disc protrudes, eyes lack glossy depth, head shape sloped and feet insufficiently covered. No natural fluffy cream down or consistent front/back material. All three reject. No phone WebGL test after art gate failure. Stop repeating local groom/closure on this source; prioritize genuinely new base geometry or properly sculpted juvenile asset.

## Scope and evidence
Three GLBs, 15 PNGs, scripts and stats created locally; remote report holds exact parameters, hashes and a tiny actual-render thumbnail only, not complete binary models. No main/production/concept/deployment mutation.
- original GLB SHA256 0e6eedf3ff0b95269555c590c34e996fdc584986d2912f589d817c6ba3b6a02c
- reference PNG SHA256 df6403266687be43268423461c4daf0672be88f4111db2f822b28c604e28d0d0
- experiment.py SHA256 5c37e2baaaab3159cc12b3a18990d4a162dbb3df3703240fbf5995f960c707f9
- experiment_v2.py SHA256 0e4e283eb751b8040aea4051183362975d878c803a2d717fb75cf04b7151bbe9
- sheet.jpg SHA256 6ac5f57be2bd125b50d60c411b1afdf320b83546dac48d9fedb09eccbda789d4
- sheet_v2.jpg SHA256 c78bd1440ab369db263014505380355591e84517f3472ed6f7650aa5a711eadf
- thumb.jpg 125x75, 1733 bytes, SHA256 78b222248354f05ee863888dda551e6cd96a3d94f62daf25582ddfaefb0aaf98

Base64 actual three-row render thumbnail:

```
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
```

ART_REJECTED / NO_RELEASE.
