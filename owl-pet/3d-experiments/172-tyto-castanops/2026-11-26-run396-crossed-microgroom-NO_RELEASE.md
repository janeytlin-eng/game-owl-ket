# Run396 — geometry-based crossed microgroom density test — ART_REJECTED / NO_RELEASE

2026-11-26 Shanghai. Re-read main owl-pet AGENTS, README, STATUS (207/251 in read results), #172 Tyto castanops v3 original PNG blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b, and Run395 at 220e7b396a4ea1bfb2b5453fa3207a7289bc39b3. Recovered actual GitHub Actions artifact 14266706992 (6.5 MiB ZIP). Visually inspected the historic four-view render. Reference crop SHA256 e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8; neural source GLB SHA256 2893e95965a9c6e6fd3af5779c1ebf3b65a16b6cdaebf7c2f743e047b9fa78de. This is a controlled fur geometry diagnostic, not a new independent base mesh.

## Independent zero-cost route checks
- InstantMesh model card https://huggingface.co/TencentARC/InstantMesh (Apache 2.0, sparse-view reconstruction). No hosted inference provider on card; actual weight URL probe failed local DNS before HTTP. Local torch CUDA unavailable, Blender/bpy absent.
- https://vinish.dev/free-3d-models/birds advertises CC BY 4.0 barn owl GLB, adult geometry; https://grab3d.com/models/animals/owl/ advertises CC0 great horned owl, not juvenile Tyto. Actual HTTPS GET probes for both failed local DNS. Neither was downloaded or used.
- Read-only fal 3D library attempt required interactive user input and could not proceed. No generation or paid call initiated.

## Executed experiment
Use recovered true neural geometry (37,475 vertices / 40,623 faces). Sample roots on actual triangles with area-proportional distribution and uniform barycentrics, interpolate vertex normals smoothed across 24 spatial nearest neighbors to reduce UV seam and plate fold discontinuities. Exclude feet and approximate facial disc using y/z/x mask (y>-.30 and not z>.14, .035<y<.36, abs(x)<.27). Project downward direction into surface tangent, add small random splay, normalize. Each root grows two crossed tapered bent ribbons, three triangles each; deterministic RNG seed 396. Vary length and width per root; cream colors mixed 76% with source texture color and slight stochastic variation. Base retains actual neural geometry and vertex-converted texture. Compare lengths .014 and .028 in normalized source units, widths .0012 and .0015; 18k and 30k roots. Render actual reimported GLB geometry using VTK fixed orthographic angles 0/45/90/135/180, 384x384, diffuse diagnostic lighting (not browser PBR parity).

| Candidate | Roots | Total triangles | GLB bytes | Reload |
|---|---:|---:|---:|---|
| baseline | 0 | 40623 | source | yes |
| short_dense | 18000 | 148623 | 5264956 | yes |
| longer_dense | 30000 | 220623 | 8048952 | yes |

GLB SHA256 short f5594627287f877fca9efacfe85c6f51c2ba700897d80c3b5311536e19717884; long fc31d5175c443d9bc6b00f1437ee5c32220866f7eb50ef62b200deab50d6ec82. Fur ribbons are intentionally open geometry; not a claim of watertightness. Full GLBs, 15 renders and script created locally; not remotely archived as complete assets. Source script SHA256 321fa417712c43825e21ba7fc25d1952125d8d28e6b14d6a8d103ce810fbc6ad; full 1920x1230 contact sheet SHA256 bd1aa252574cf090c02d678812d9ffb26edaeaac75140f02b095be4d3bcc8f41.

## Visual gate
Inspected all 15 renders as actual contact sheet. Longer groom visibly improves cream-colored silhouette fuzz at crown and breast, but looks prickly/noisy rather than plush. Back retains the hard feather plates; visible mask boundary at lower body and face, adult wing profile and dark eye sockets remain. Added geometry inflates size and triangle count considerably. Both rejected; no phone WebGL validation and no release. Do not repeat increased groom density on same rejected base as a primary solution. Independent juvenile anatomy and smooth underbody remain priority. No main, concept, species workflow or deployment changes. Extra paid cost zero.
