# Run415 — protected native surface filtering — ART_REJECTED / NO_RELEASE

2026-11-27. Read main owl-pet AGENTS, README, STATUS (207/251 visible), existing v3 concept list, Run406 and Run414 records and actual Run414 six-view image. Successfully recovered and visually inspected the full original v3 PNG, blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b, 1536 × 1024, via base64 file read. Right juvenile is compact cream down, small glossy dark eyes, fine brown heart-disc rim, pale bill, feathered feet, no long adult tail. Reference is a concept, not observed side/back or known biological age. Also inspected Run90 archive listing: prior photo projection and alpha down ablations already exist, so not re-run. Local numpy/scipy/trimesh/skimage/torch are present; Blender absent from PATH; actual DNS resolution of api.github.com, raw.githubusercontent.com and huggingface.co failed errno -3. No external paid calls.

## Executed experiment

Recovered original Run406 true native GLB (source blob e3e50315d3b7d4669e6dc89d700ffa1bbf8f33fb). Hypothesis: removing reconstruction lumps before grooming might reduce artificial ridges without losing facial/foot detail. This is a diagnostic on an already rejected neural-derived mesh, not a new sculpture. No simple primitive assembly or image-only replacement.

Construct unique one-ring neighbors from the indexed triangles. For vertex original y,z, define smooth(t)=clamp(t,0,1)^2*(3-2*clamp(t,0,1)), face=smooth((y-.12)/.24)*smooth((z-.12)/.3), feet=smooth((-.59-y)/.22), w=1-.95*max(face,feet). Apply 24 synchronous paired uniform Laplacian passes, coefficients +.50 and -.48, each displacement k*w*(neighbor mean-current). Recompute area-weighted normalized vertex normals, preserve index topology and original material, update accessor bounds and GLB header. Software rasterize actual indexed triangles with interpolated normals/depth test, front/side/back at 0/90/180 deg, 69px per native unit, 160px panel, baseline top, filtered bottom. Actual PNG viewed; not a WebGL renderer.

- 21,622 vertices, 43,240 triangles, no degenerate triangles at area threshold 1e-10 before/after.
- Uniform one-ring Laplacian RMS 0.00640621 -> 0.00410435 (35.9% reduction; not physical curvature).
- Surface area 9.23484 -> 8.90375 (-3.59%); absolute signed volume 1.81969 -> 1.82064 (+0.052%).
- Whole-mesh RMS displacement 0.005021; max 0.04057 native units. Protected subset w<.2: 6032 vertices, RMS 0.000497.
- Actual six-view visual inspection: rear and side surface bumps soften, some structured side ridges remain. Smooth clay appearance is arguably less like wispy down. Face is still stiff, eyes are empty-looking, rear is sloped, feet/wing anatomy remain incorrect. No meaningful improvement in juvenile identity. Do not promote.
- Native output is 779732 bytes. No rig, soft down, UV or actual device/browser test; no product release.

Assets committed at f452ce0a62e1510241c068c60a271990e50d6b6c and immutable file readback:
```json
[
  {
    "name": "filtered-diagnostic.glb",
    "sha": "1d709a7108eedcda3a74009e5fabac2b965a0d23",
    "bytes": 779732,
    "match": true,
    "prefix": "Z2xURgIAAADU5QsA"
  },
  {
    "name": "before-after.png",
    "sha": "7cb111dfae305a076e88e86c171efdaa374d2c78",
    "bytes": 461223,
    "match": true,
    "prefix": "iVBORw0KGgoAAAAN"
  }
]
```
Metrics JSON parsed successfully, blob 911db528bc95b81b80f16ba84b884ca1c575b851.

[Actual native GLB](filtered-diagnostic.glb) · [Six real mesh views](before-after.png) · [Metrics](metrics.json).

Decision ART_REJECTED / NO_RELEASE. This confirms further geometry smoothing alone is insufficient; do not pursue endless parameter tuning on this rejected base. Independent juvenile-grade sculpt and realistic eyes/disc/down remain bottlenecks. No extra fee, no main, v3, species workflow, or deployment changes.
