# Run387 — independent reference-derived implicit visual hull — ART_REJECTED / NO_RELEASE

2026-11-26 Shanghai. Read main AGENTS, README, STATUS (207/251), design/concepts directory confirming exact 172-tyto-castanops-v3.png remains present, and Run386 at a48bbe5c4abdb30ab7285b8a54dbca311ab2db63. Preserve v3 rightmost juvenile, cream mesoptile, heart disc, concealed short wings/tail, unknown age and science=false. Recovered actual source crop from GitHub Actions artifact 14599833411, SHA256 df6403266687be43268423461c4daf0672be88f4111db2f822b28c604e28d0d0, visually inspected. Also recovered artifact 14174978922 but did not reuse its mesh. Checked previous SF3D Run169: known rejected source registry; no circular re-test. Local github.com/huggingface.co DNS unavailable, Blender absent; VTK/scipy/trimesh/skimage usable. No paid calls.

## Actual new geometry, two iterations

Not a neural inference, not a textured plane, not primitives or a modification of the previously rejected mesh. Reconstructed continuous three-dimensional implicit surfaces from the 512px RGBA reference silhouette plus explicit inferred transverse-depth priors (single three-quarter image cannot determine rear anatomy). First pass: alpha >100 resampled to 180x180, Gaussian sigma 1.05, fill holes and close; signed 2D distance transform smoothed .8; depth profile interpolated at relative image rows [0,.08,.18,.35,.50,.68,.83,.91,.97,1] with values [.03,.12,.26,.29,.34,.36,.27,.12,.07,.025]. Two variants multiply depth by .86/1.07 and raise normalized distance to .65/.52; independent front/rear boundaries with a shallow facial relief. 152 depth samples over [-.46,.46], 3D field min of silhouette and front/back constraints, Gaussian .65, marching cubes zero level. Smooth normals; deterministic procedural surface displacement and vertex color blending from front RGBA and a real down patch.

Inspected both actual five-view renders. Periodic displacement and distance-field ridges produced unacceptable mesh corrugation. Second iteration uses row-wise smoothed silhouette bounds (sigma 2.5), elliptical transverse cross-section, depth multiplier .93, field smoothing 1.2, and nonperiodic seeded 3D Gaussian noise at amplitude .0007. Side color uses 20% reference patch and 80% neutral cream plus noise. All three exported as native GLB, independently reimported in trimesh, then actually rasterized from imported geometry and colors using VTK offscreen at 0/45/90/135/180 degrees (360px each, parallel scale .54). Fifteen renders total.

| Candidate | Vertices | Triangles | Bytes | SHA256 |
|---|---:|---:|---:|---|
| hull_compact |78032|156060|4058920|0da482eb8eeef57de2fe6dfc021307c102be7f24cae1fb829dc20656ec4323bc|
| hull_round |89562|179120|4658480|a107ea7130fab80ce47a31c2dc9eb086447304f50888e15fe1e9b997c1825cc8|
| hull_refined |81590|163176|4243936|e7e1cd6925b5aa028d5b3327ee9050c76871f4a27046040e60f581acc1144477|

All independently reimported watertight. Refined bounds [-.35545,-.46892,-.34097] to [.34780,.46379,.31318]. Not a mobile GPU or browser test.

## Visual gate

All rejected. First pass exhibits periodic woven grid and pinched side/rear ridges. Second removes most grid and improves cream coloration, compact torso and absence of adult wing seams/long exposed tail, but appears as a waxy silhouette extrusion with flat texture-dependent eyes and beak, no genuinely sculpted eyes/feet, uneven vertical seam and broad flat rear. No down volume or convincing side/back anatomy. Do not mistake improved frontal projection for three-dimensional fidelity. Avoid further single-view hull refinements as final asset route; pursue an independently sculpted or genuinely multiview juvenile base. No new paid generation; no release; no main, 251-species production, original reference, or deployed changes.

## Evidence

Full three GLBs, 15 actual PNGs, scripts and metrics created in local working container only. Remote evidence includes this report and [actual refined five-view thumbnail](run387-actual-refined-five-view-NO_RELEASE.jpg); full binaries not uploaded. Thumbnail 240x48, SHA256 8d33f33936dc3fe8ccf5480338aa3943897d0b9921951c495d1b1998682a8e24.
- build.py SHA256 b405741990b2406d0505b26cde6f615a2fdc94b0133d9f664e25326415be0859
- refine.py SHA256 59b3211b24b2c7ab5c1625094f786dfd926e3dd093a19777d6768ad28a5ca49f
- sheet.jpg SHA256 57a438ea57c7b14a1d43bcaecd41cc1a443dffe2d136ae00dfe75976c39f5faa
- refined_sheet.jpg SHA256 dd7b145c32af4ec46212559831868d9853e63185284f1ff5cc57091e700a5c9e

ART_REJECTED / NO_RELEASE. Additional spend zero.
