# Run384 — crossed alpha down-card groom — ART_REJECTED / NO_RELEASE

2026-11-26 Shanghai. Main observed db8ad5c8fe386214b9b816132030f638fba5ff13; read AGENTS, README, STATUS (206/251), prototype listing, exact #172 v3 review (cream thick mesoptile, heart disc, wing buried under down, age unknown, science=false), and Run383 at 93f45fa9cb4aed21f52abf9bb6a8fcb015a2f273. Recovered actual neural base and pupil-restored reference from artifact 14599833411; inspected reference and axial renders. No new independent neural base: container getent returned no addresses for github.com or huggingface.co; Blender unavailable. VTK, scipy, trimesh available. No paid model call or purchase.

## Executed experiment

Test a different low-polygon groom approach from Run379/381 geometric strands and Run383 flat UV atlas: crossed textured 3D cards as a surface layer over the actual Hunyuan neural mesh, not a sprite or primitive-built character. VTK quadric decimation 88%, volume preservation, 33,074 base triangles. Base cream RGB (.78,.72,.64), front color projection from exact input with alpha and smoothstep(.30,.65,Z). Sample 14,000 surface points, 10,114 retained after excluding front face region and Y<-.84. Seed 384; create RGBA 256x256 tuft texture from 175 curved tapered-color strands. Two crossed quads per root in random tangent orientations, roots inset .009, tips along surface normals with -.012 Y lean, length random .65–1.35, width .7–1.3. GLB material doubleSided, alpha MASK cutoff .38, roughness 1, metallic 0. Two distinct root density/length budgets. Actual export and independent trimesh reimport verified both geometries. VTK textured offscreen 320x320 renders at 0/45/90/135/180°, ten images total; depth peeling requested. VTK preview uses blended RGBA, not exact glTF MASK/PBR or phone WebGL. No claim of mobile acceptance.

| Candidate | Roots | Length/width | Triangles | GLB bytes | SHA256 |
|---|---:|---|---:|---:|---|
| short |3200|.047/.052|45874|1355552|fdcacc99d3432e3f5a51f4901de7008bae391d822c20d924a008800074ca7e56|
| soft |6500|.078/.075|59074|2041952|af3dc760c80f43a51f530f400815274de5942cc17c9260ef4ab1fe4782cf0116|

## Actual visual review

Viewed full 1600x640 two-row render sheet. Short variant appears sparse, like pale flakes on a dark sculpt. Soft variant increases silhouette fuzz substantially, but the rim and surface look like coarse white particles rather than coherent delicate down; back remains visibly sculpted and sparse centrally, head remains too small with projected face and prominent disc edge, side wing shape remains adult-like, feet uncovered. Both reject. Card density raises potential mobile overdraw despite favorable file sizes; no mobile test after art rejection. Not a release. Next prioritize a genuinely different base mesh with a short-wing juvenile silhouette before further groom work.

## Evidence and scope

Full two GLBs, ten PNGs, texture, script, stats and full sheet generated locally in this run; remote archive contains this report, exact parameter description, hashes and tiny actual render contact sheet (not full binaries). No main, production, concept or deployment mutation.
- source GLB SHA256 0e6eedf3ff0b95269555c590c34e996fdc584986d2912f589d817c6ba3b6a02c
- source PNG SHA256 df6403266687be43268423461c4daf0672be88f4111db2f822b28c604e28d0d0
- experiment.py SHA256 f20a641aafcea796efc6b86ce0b08fd7e5a4f7878d30d8753c2b5d44dcdfe7c5
- tuft.png SHA256 5a74e58371d2e58f03da166f9c436b6d2775d53f0648244257884977c4b32071
- sheet.jpg SHA256 43216b38689d263ff8339cc575b17170616b6c451d9fac2351cedb1b13bf85e3
- evidence.jpg 160x64, 1563 bytes, SHA256 69763d522a9cf2d98cc068795507ee6e77706a3a8adee6bb90e6b9b69af271dc

Base64 actual two-row render thumbnail:
```
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
```

ART_REJECTED / NO_RELEASE.
