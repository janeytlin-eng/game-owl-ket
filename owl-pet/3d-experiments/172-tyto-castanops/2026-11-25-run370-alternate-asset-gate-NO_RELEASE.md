# Run370 — alternate foundation asset gate — ART_REJECTED / NO_RELEASE

2026-11-25. Extra spend $0. Independent branch from Run369 a98d42951981de1315280490af66bb4bc4f56b4c.

## Preflight
Re-read main owl-pet AGENTS, README, STATUS (206/251; latest STATUS reports six revisions #75/70/71/72/73/66), and #172 v3 review. Target age unknown, thick cream mesoptile, developed heart-shaped mask, short wings buried under down, concealed tail. Science verification remains false. Read previous Run369: bilateral correction did not resolve anatomy, local WebGL2 failed. No repeat of symmetry/normal or silhouette optimization. Current container has no recovered source models, no Blender executable, torch.cuda.is_available() false; curl tests to api.github.com, raw.githubusercontent.com, github.com and huggingface.co all returned DNS error 6. No paid generation.

## New route: actual third-party GLB import and anatomy gate
Queried repository and code search, inspected pinned Git trees and credits, then fetched actual binary payloads using GitHub base64 contents where available. Parsed GLB header/JSON and decoded POSITION and index accessors, applied node scale/quaternion/translation, and software-rasterized three orthographic views (0/90/180 degrees around Y; not claimed as labeled anatomical front/back). Depth-buffered triangles, grayscale flat lighting, not textured PBR or WebGL. Inspected actual image visually. These are screening diagnostics, not new pet models.

| Asset (pinned ref) | Actual bytes | Triangles | Result |
|---|---:|---:|---|
| [Patobeurre/godot-fishing-game owl](https://github.com/Patobeurre/godot-fishing-game/blob/d61a963dd7e4ef775098243901c5f43fffade2d9/models/Catchables/owl.glb) | 160056 | 1732 | Read complete GLB 2.0, header length equals actual length; single indexed mesh, 3636 position entries, one texture. Adult angular ear tufts and exposed talons, unsuitable naturalistic Tyto chick. Reject. |
| [9MidhunPM/Cindertrail owl](https://github.com/9MidhunPM/Cindertrail/blob/e61eacb1a83d48db46c99d3f53675819eb426a9e/art/wildlife/owl.glb) | 185176 | 1680 | Read complete GLB 2.0; five nonindexed meshes, vertex colors; wings outspread and tail visible, stylized adult. Reject. |

First asset blob a4b5a390aef3ce7df2ffb6f49a2ec47924f44d5c. Second asset blob b0c711bc00578488e5878e260528b4d10cf2f6f8. First transformed bounds [-0.874514,-0.614518,-1.044228] to [0.370484,1.929001,1.049667]. Second transformed bounds [-0.770000,0.020220,-0.264704] to [0.770000,0.618000,0.472000]. Projected covered pixels respectively [3459,4943,3459] and [1063,760,1063] in 120x120 cells.

Core executed raster math: project transformed vertices with x'=cos(a)*x-sin(a)*z, y'=-y, depth=sin(a)*x+cos(a)*z, scale each model uniformly to 100px maximum world axis range. For each triangle use barycentric coordinates from its 2D determinant, reject out-of-triangle samples, interpolate depth, retain the nearest fragment. Intensity from absolute dot of triangle normal with (.35,-.4,.84), mapped to 75–210. PNG grayscale zlib stored blocks with CRC32 chunks. This diagnostic is useful for gross geometry only, cannot assess feather materials.

Actual 360x240 render evidence: [adjacent PNG base64](2026-11-25-run370-alternate-asset-geometry.png.b64), 86713 decoded PNG bytes, first row Patobeurre; second row Cindertrail. Exact base64 readback confirmed, blob 9d67754aaa1caafb0e34908d4346140d9ae28936, archive commit 1a18dfaa4981d1564a6ffb80ba2ef5357a3b9753. Decode with base64 -d. Third-party binaries not copied to project or modified.

License gate: Patobeurre repository LICENSE.md is MIT copyright Kenney, but individual owl provenance not independently confirmed. Cindertrail CREDITS.md identifies its original procedural vertex-painted wildlife, but no explicit asset reuse grant established. Both would require asset-specific provenance review even if morphology passed.

## Larger candidates: actual transport failure, no visual claims
- [ItsJazii/lantern-hallow owl](https://github.com/ItsJazii/lantern-hallow/blob/76fc240b4c8eb04112ea153785b40254ff185c45/game/assets/models/owl.glb), tree 1682240 bytes, blob 56d97c84d8b022cbcd87471183b0c28ca4cc422d. README says Tripo-generated then cleaned, repository MIT; individual rights and anatomy not verified. Connector fetch_file base64 returned content length zero twice; fetch_blob failed UnicodeDecodeError, generic Git blob fetch rejected non-UTF8. Not recovered.
- [Jaabrakus/the-last-frontier smoothed owl](https://github.com/Jaabrakus/the-last-frontier/blob/41ff20fae675a02eb8bb546d4955b5c31a09eca4/assets/wildlife/smooth/great_horned_owl.glb), tree 1630484 bytes, blob b714203923fae104e7403e056f2adc3a5531014f. Credits identify Poly by Google great horned owl CC BY 3.0, modified smoothing. Different genus/adult form; base64 contents produced no parseable header, fetch_blob UnicodeDecodeError and generic fetch rejects binary. No actual visual inspection.
- Rednai/OwlViewer tree is a viewer, no owl GLB/OBJ/FBX found. Not a candidate.

## Decision
Both recovered geometry candidates fail gross form; no reason to recolor, rig, or pretend they are #172. No qualified sample, no new WebGL acceptance. No changes to main, 251-species production, concepts or deployment. No extra spend. Further work should target explicitly licensed juvenile/naturalistic foundation, or a new coherent multi-view reconstruction pipeline. Transport gap for >1MB GitHub binary payload is unresolved; use a verified free asset channel, not another local mesh metric ablation. Do not notify.
