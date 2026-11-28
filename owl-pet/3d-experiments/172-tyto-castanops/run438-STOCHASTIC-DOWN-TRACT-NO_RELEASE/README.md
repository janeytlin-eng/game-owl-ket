# Run438 — stochastic down tract — ART_REJECTED / NO_RELEASE

2026-11-28. Read current main AGENTS, README, STATUS (207/251, 1490 original numbered versions per STATUS), #172 v3 species and review documents, and visually inspected original v3 mesoptile crop (blob 2915b7c86316359ff2b8cbd26eb174bfa0280613). V3 rightmost age-unknown mesoptile remains the reference, not later concepts. Read Run437 report, metrics, script and native GLB (immutable blob 7092e797a1cf8fb860cdc7789eb4635b9776fb2a); inspected baseline through newly rendered geometry. Historical Run88B groom archive also checked (c73b1631d6f06856ab3aab9c6fc58a1f53b6975c); this is an ablation of a separate surface-rooted layer on the Run437 mesh, not a claim of first-ever grooming.

Executed zero-fee deterministic CPU geometry experiment. Sampled triangle surface proportional to area with face/foot exclusion, projected downward growth direction into tangent plane, randomized curl and length, generated 6000 individual tapered curved ribbons with world-fixed orientation, cream root-to-tip vertex colors, normals, and indexed triangles. Exported independent native GLB layer (949136 bytes, 30000 vertices, 18000 triangles, no degenerate triangles, finite). Base mesh unchanged (43240 triangles); combined 61240 triangles, 1988424 total bytes in two GLBs. Actual software z-buffer eight-view comparison: front, 45 degrees, side, rear; baseline top, groom bottom. Coverage increases 2.2–3.0% depending on view. Region roots front 1279, side 2794, rear 1119, upper head 808. Seed 438172, script and metrics archived. No paid calls. No browser/device runtime tested; triangles/bytes are measurements not proof of mobile performance.

Visual decision: reject. The groom creates isolated speckles and a slightly fringed outline, not the reference's dense coherent creamy soft down. It leaves obvious sculptural lumps and adult-like side profile untouched; eyes remain painted-looking, heart rim mask-like. Density, filament geometry and shading require different treatment, but improving only groom cannot cure base shape. No qualifying sample; do not release. Independent layer is not a complete pet and must not be presented as one. Preserve previous files. No changes to main, production, concepts, or deployment.

Readback at artifact commit 90c11889844d9415c724ffab7456c2bed6cbbd28:

```json
{
  "down-layer-ART_UNAPPROVED.glb": {
    "sha": "71b6111f39744048e06162ad92fa69e9b7796fb4",
    "shaMatches": true,
    "bytes": 949136,
    "headerValid": true,
    "vertices": 30000,
    "triangles": 18000,
    "maxIndex": 29999,
    "indexValid": true
  },
  "comparison.png": {
    "sha": "47695dc9f446173259a0eca314728a2a4806f98e",
    "shaMatches": true,
    "bytes": 614833,
    "width": 640,
    "height": 320,
    "iend": true
  },
  "metrics.json": {
    "sha": "788062ac9b6e76190cac45f3e111d21875c04287",
    "shaMatches": true,
    "characters": 778
  },
  "experiment.js": {
    "sha": "87ee72d5417e28e3530251f693ceb38a6d559cee",
    "shaMatches": true,
    "characters": 8110
  }
}
```

The comparison was actually viewed at creation; readback verifies PNG header, dimensions, end marker and blob SHA, not a second visual pixel-by-pixel comparison. GLB readback parses header, accessors and index bounds. All files isolated on research branch.
