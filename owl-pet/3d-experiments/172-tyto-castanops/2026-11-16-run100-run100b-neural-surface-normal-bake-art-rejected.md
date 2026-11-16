# Run100 + Run100B — neural surface topology repair & real normal-map baking — ART_REJECTED

**2026-11-16 Asia/Shanghai. Technical 3D outputs achieved; no art-approved pet, no release, no user success notification.**

## Preflight and non-production boundary

Re-read project \`owl-pet/AGENTS.md\`, \`README.md\`, archived cat \`prototype/index.html\`, \`research/species/172-tyto-castanops-v3.md\`, \`research/reviews/172-tyto-castanops-v3-review.md\`, and previous Run92C/96–99B rejection conclusions. Reviewed the actual rightmost age-unknown mesoptile crop from Run99 and the saved genuine Run99 source multiview contacts. Target is the **cream/ivory thickly downed, dark-eyed, rounded juvenile with a developed soft heart-shaped face, wings buried beneath down, concealed tail, and belly and feet genuinely supported on a broad eucalyptus hollow lip**; the original image explicitly does **not** justify a specific week-of-age, mature flight anatomy, or an independently validated rear view.

Run99 original source is physically generated neural **3D** (not SVG/quad/primitives): 18,333,652-byte GLB, SHA256 \`eb95158d8a40fc869caef310a70af7e42f5731061725e2a1754aded0e7a8d683\`, 348,101 vertices and 696,834 faces on actual Blender import. Previously simply decimating to 72k/32k and applying cream PBR made shredding/dark mottling worse.

## Run100 — two actually executed mesh-topology cleanup variants

Used only free GitHub Actions Ubuntu + Blender 4.0.x Cycles. On **the same true high-poly 3D neural source**, independently tested:
- **Six-pass mild full-mesh smoothing, then physical decimation to 80,000 faces and rough cream nonmetal PBR.** Actual Blender exporter/reimport result: **79,988 triangles, 1,433,708 bytes**, SHA256 \`60feb7a5e4f4c67a020e3457e7ffbfb52f6fbe3e75f115b970030c00b20cd35d\`.
- **Actual voxel remesh (voxel 0.027387 Blender units), three smoothing passes, decimation cap 55k, identical cream PBR.** Actual topology naturally contained **43,240 triangles** after voxel remesh, not falsely claimed as 55k; exported/reimported **43,240 triangles, 779,732 bytes**, SHA256 \`5fc2eb81f4896a5c1ca9583ac555755029a65a133d4f83dbffe6bd73c627c931\`.

Both are real GLBs, re-importable with nonmetal materials; photographed from 4 physical Blender Cycles angles each. A third matching camera/light control rendered the untouched high-res source. Total **12 native PNGs and three 4-view JPEG contacts**, not synthetic projected sprites. All are retained and checksum-verified on isolated branch. [Successful real experiment](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43789255416).

**Direct visual judgment after inspecting all three original multiview contact sheets:** Mild smoothing noticeably removes some of Run99B's dark crumbling artifacts while preserving the real bird-like volume and face outline. But it still has coarse shell-like/fossilized down instead of suspended cream filaments; the face reads as flat/closed-eyed clay, not the concept's two clearly open dark eyes; legs/toes protrude strongly in air without a tree lip; the side is overlong/stooped with unrealistic shoulder/wing plane and rough rear silhouette. The voxel version is smoother/cheaper but erases the facial relief and most feather cues, becoming a lumpy white bird-shaped solid; no natural fluff. **Both art rejected.**

## Run100B — actually baked UV normal texture from 696k source to 80k true mesh

To test recovery of high-frequency detail without restoring damaging heavy shell geometry, executed a second free Blender workflow on the **original Run99 high-poly GLB and actual Run100 smoothed GLB**, created real UV islands, performed **Cycles selected-to-active tangent-space normal bake at 1024×1024**, connected the baked map to a Blender PBR Normal Map shader, exported embedded-texture GLB, physically **reimported it**, and rendered four native Cycles angles for inspection. This is true high-poly-to-low-poly normal baking, not a 2D painting or fake geometric replacement.

- Actual saved baked normal PNG: **98,138 bytes**, SHA256 \`6488c21838edf3498a14aa36ed0c7f68291c2910d7f38ce5c6ed4b442ab1dbeb\`.
- Actual GLB with real UV and normal material: **3,682,844 bytes**, **79,988 reimported triangles**, SHA256 \`a8f2f4ef8f1ea098d662c943c080e430a68ed4ee4cc7a2dffcba297830223273\`.
- Actual successful free job with archived native PNGs, contact, Blender bake log and hashes: [Run100B](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43790261331).

**Direct visual judgment against original crop and Run100 80k controls:** Normal baking recovers some etched shell microdetail but also reintroduces peppered dark imperfections and jagged-looking back feathers, does not create genuine strand-like down, fails to open/shape dark eyes or correct the unsupported feet and longitudinal shoulder silhouette. It therefore **does not beat** the art gate; technical bake success is NOT character quality success. Both runs remain **ART_REJECTED**.

## Independent evidence and explicit remaining blockers

Research branch: \`research/owl172-run100-neural-surface-topology-repair\`. Quarantined output folders:
- \`research-evidence-run100-REAL-NEURAL-TOPOLOGY-ART_UNAPPROVED/\` — original control, both real GLBs, 12 PNGs, three contact sheets, Blender log, JSON and SHA256 manifest; all 20 listed artifacts verified by GitHub workflow SHA256 check.
- \`research-evidence-run100B-NATIVE-NORMAL-BAKE-ART_UNAPPROVED/\` — real baked-normal GLB and PNG, 4 native Cycles views, JPEG contact, Blender log, JSON and 10-file manifest; archive and remote readback verified.

**Quality gates still missing:** (1) open-eyed, natural 3D heart-shaped facial disc and bill, (2) genuine soft layered ivory down rather than an etched/voxel sculpture, (3) short wing buried in plumage and physically credible side/back, (4) supported feet/belly and old eucalyptus hollow lip, (5) a tested interactive rig, (6) real smartphone/WebGL GPU load, touch and frame pacing (only asset byte/triangle sizes and Blender roundtrip were established), (7) reviewed worldwide licensing. The original reference is a single mostly frontal design image; it cannot validate imagined rear anatomy.

**Use and rights caution:** The source was made via Hunyuan3D-2 Community License, **not CC0**. The terms have regional/redistribution conditions on generated outputs; no commercial/worldwide end-user deployment without qualified review. Research branch contents are publicly accessible, not private. This experiment neither calls paid services nor edits the original 251-species production pipeline, design image/manifest, existing cat prototype, or live deployment. A GitHub \`main...research/owl172-run100-neural-surface-topology-repair\` compare returned **87 changed files, all within \`owl-pet/3d-experiments/172-tyto-castanops/**\` and dedicated \`.github/workflows/owl-pet-172-*\` paths; 0 outside-scope files**.

**Decision:** Continue **ART_REJECTED / NO PUBLISH**. The next valuable step is a genuinely new anatomically grounded juvenile sculpt with open dark eyes, deep integrated heart mask, embedded wings/legs and real layered grooming on a supported cavity lip, rather than further 2D color transfer, uniform smoothing, voxel simplification, high-poly normal replay or arbitrary hair count. Art quality should precede any real-device acceptance and license-cleared user sample.
