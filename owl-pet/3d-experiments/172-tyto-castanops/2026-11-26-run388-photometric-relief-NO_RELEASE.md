# Run388 — reference photometric relief controlled ablation — ART_REJECTED / NO_RELEASE

2026-11-26 Shanghai. Main AGENTS, README and STATUS read (207/251); v3 exact source path confirmed, original blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b; Run387 read at d2da795b11ae4f4b1499fd041a8bed5bd51b7e7e. Preserve the rightmost cream-down juvenile, unknown age, science=false, no main or deployment changes.

Recovered actual 512×512 RGBA reference and official Run233 Hunyuan3Dmini CPU mesh from Actions artifact 14599833411. Reference SHA256 df6403266687be43268423461c4daf0672be88f4111db2f822b28c604e28d0d0; actual base mesh SHA256 0e6eedf3ff0b95269555c590c34e996fdc584986d2912f589d817c6ba3b6a02c. Viewed actual reference and original axial sheet. Artifact 14174978922 also downloaded but not reused. Not a new neural inference. Local DNS for github.com and huggingface.co failed, no Blender, VTK/scipy/trimesh available. fal image-to-3D catalog read returned user input required; no generation or payment. Source discovery: Grab3D adult great horned owl already unsuitable per Run182; Vinish.Dev CC BY 4.0 adult barn owl is not juvenile; photo-to-mesh multi-view Hunyuan2mv requires GPU and actual additional views, PicToMesh multi-photo DUSt3R has noncommercial restriction. No new donor bytes acquired.

## Executed experiment
Controlled comparison of scanline-adaptive reprojection, with and without band-pass log-luminance surface displacement. For each reference alpha scanline, use smoothed silhouette bounds; map per-row mesh 1st–99th percentile X to reference row bounds. Front factor = clamp((normal_z+.05)/.8)*clamp((z-.12)/.35). Reference front blend .86*front, cream base RGB [.84,.77,.67]. Log luminance of RGB uses .025 offset; alpha normalized Gaussian coarse band sigma 2 minus 12; fine band sigma .7 minus 3.2. Displacement along original actual mesh normals, coarse coefficient .018 and fine .009, eye-region guard .85; reduced second variant .012/.006 with .9 eye guard and localized face relief .008. These are photometric heuristics, not metric depth recovered from a single image. Geometry is not new independent base. Control has same color mapping, zero displacement.

All three native GLB files reimported with trimesh, actually rasterized from the imported geometry and colors via VTK offscreen, 360px, angles 0/45/90/135/180, 15 renders. Each 137851 vertices, 275630 triangles, watertight, 5514188 bytes.

| variant | max displacement (mesh units) | SHA256 |
|---|---:|---|
| control |0|4f6c2908d60bb63904390662c0983b47ab92eb3d4731b768fede3186842c2a36|
| bandpass |0.0269326|b03abad0697bc7dc4acede31cc0a1946b6ef328a68c2abc69fc7cb397bbc485a|
| eye_guarded |0.0212478|2d70c5090a242341715c7aa98c12373ed89b359fcaf278ba2384477359f0fc80|

## Art rejection
Viewed actual 15-render contact sheet. Control looks rigid clay with overprojected face, adult-like wing seam and exposed toes. Bandpass adds dark flecks and rough grooves rather than natural down; eye-guarded reduces extreme detail but does not remove dark flecks, eye misalignment, elongated body, protruding face or adult-like wing geometry. Rear is essentially unchanged. All rejected; no mobile browser or physical GPU test. Do not continue photometric surface detail as a replacement for a genuinely independent juvenile base. No new paid calls. No release.

## Evidence
Actual [15-view thumbnail](run388-actual-ablation-NO_RELEASE.jpg), 200×120, top control, middle bandpass, bottom eye_guarded, left to right 0/45/90/135/180. SHA256 a22c4615e7f34fd4c998a8c190220ff5b73b4ef3f4f87fb305291ba620332488. Full sheet SHA256 f910115f4e95ba06691a0ff96e052017fece97c8b3e405d80767c593d17b8fa8. Actual script SHA256 42cde44e8f35093bbfb3dd3656fa061b45afa1bafeb69aa2bcc32b5bf3a19883. Full model binaries, 15 PNG renders, script and metrics local only, not uploaded. Next legitimate option: source a true multi-view or independently sculpted juvenile base, only use verified free routes. ART_REJECTED / NO_RELEASE.
