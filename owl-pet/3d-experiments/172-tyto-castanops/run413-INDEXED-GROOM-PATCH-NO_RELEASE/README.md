# Run413 — indexed crown/back groom diagnostic — NO_RELEASE

2026-11-27. Re-read main AGENTS, README/STATUS (207/251), #172 v3 review and actual mesoptile crop (2915b7c86316359ff2b8cbd26eb174bfa0280613), plus Run412 (c1c615324c52294fb59c48737704d1a4dede9c47) and actual Run406 six-view rendering. V3 reference remains age unknown / science=false, warm cream down, brown-rimmed heart disc, dark eyes, narrow pale bill, wings and tail mostly concealed. Run406 base still has blank eye sockets and adult-like back/wing division.

## Executed experiment
Decoded immutable native GLB e3e50315d3b7d4669e6dc89d700ffa1bbf8f33fb from 16045db5e461b2b524b238c44aba742734c36b74; sampled real triangle area on upper crown/posterior (centroid y>0.23,z<0.18, Y up/+Z front). Seed 413 LCG (1664525*s+1013904223) modulo 2^32, 1200 area-weighted roots with sqrt barycentric sampling; interpolate actual vertex normals and reject roots with dot against face normal <0.35. At each accepted root construct a tapered five-vertex three-triangle curved ribbon along interpolated normal and randomized tangent. Length 0.025–0.05, width 0.003–0.005 in model units. This is isolated actual mesh geometry, not a character or a production groom. No face or feet modifications. Generated indexed ASCII PLY and tested triangle area for degeneracy. No skin, UV, transparency, coloration or animation yet; no visual or mobile acceptance claimed.

```json
{
  "sourceBytes": 779740,
  "sourceVertices": 21622,
  "sourceTriangles": 43240,
  "eligibleFaces": 6855,
  "area": 1.4373121150765158,
  "roots": 1195,
  "rejected": 5,
  "minNormalDot": -0.16479855782494238,
  "patchVertices": 5975,
  "patchTriangles": 3585,
  "degenerate": 0,
  "plyChars": 227846,
  "indexedPositionBytes": 93210,
  "unindexedPositionBytes": 129060
}
```

The position+uint16 indices estimate excludes normals, UVs, colors, bones, texture and GPU overhead. Compared with unindexed triangles it saves 27.8% of position/index bytes at this patch density. The complete PLY preserves actual roots/curves for future QA. It is a diagnostic, not a replacement for the 3D sculpt, and is not eligible for user delivery.

## No-cost source search
Rechecked https://mint.gg/free-3d-models/barn-owl (previously known CC0 adult, 19966 triangles); https://grab3d.com/models/animals/owl/ (CC0 great horned owl, adult ear tufts, 400k/800k tris); https://vinish.dev/free-3d-models/birds (CC BY 4.0 rigged collection, description folded adult flight feathers); https://www.embossify.com/models/owl (CC0 standard simple-math owl with ear tufts, 4196 triangles; paid higher resolutions excluded); https://sketchfab.com/3d-models/barn-owltyto-alba-af3cdd38e029430d9c131370ebf1bb33 (CC BY 760 triangles, no detailed description). Metadata screening only for these sources; no new candidate geometry or pixels retrieved. No extra fees incurred. No new suitable juvenile base found.

Decision ART_REJECTED / NO_RELEASE. No mobile WebGL performance or full-character visual acceptance. Independent branch only, main and species production workflow unchanged.
