# Run96 + Run96B — native 3D anatomical/feather-tract comparison — **ART_REJECTED**

**2026-11-16, Asia/Shanghai. Both real experimental GLBs are visually rejected. No public pet sample, no production deployment.** This audit is in an isolated research branch; it does not certify a new usable character.

## Preflight actually performed

Re-read `owl-pet/AGENTS.md`, `README.md`, `research/species/172-tyto-castanops-v3.md`, the existing owl-pet prototype and Run92C/Run95/previous failed studies. Opened the original **three-bird** concept `owl-pet/design/concepts/172-tyto-castanops-v3.png` and visually compared its **rightmost** cream age-unknown mesoptile against the newly rendered true front / three-quarter / strict side / rear frames. Design requirements: warm cream second down; deep, broad, naturally feathered heart facial disc; recessed dark eyes; large but not bald juvenile head; compact plump chest; extremely short down-buried wings and fully concealed tail; and feet completely supported by a broad natural eucalyptus hollow lip. The source is a front reference, not proof of the exact side/back anatomy.

## Actual free creation / validation / archive

Used genuine script-authored 3D geometry, NOT an SVG or a stack of flat 2D images. Both studies build a continuously joined head/body/neck/wing outer SDF isosurface via skimage marching cubes, implement a 3D facial surface colour / shallow inset and small real geometry for eyes, bill, curved toes, keratin tips and a research-only tree rim, and create overlapping directionally placed feather ribbons from sampled surface normals. Export to GLB, enforce nonmetallic rough glTF PBR with vertex COLOR_0, re-import through both trimesh and Blender, and render **four genuine Blender Cycles 3D views** for each. Also run actual desktop and simulated mobile Chromium SwiftShader WebGL2 loader/rotation/framing/error tests. There is **no physical mobile GPU, actual FPS / memory / battery, animation, touch-driven pet interaction or suitable mobile LOD certificate**.

| Trial | GLB bytes | Meshes / triangles | Sculpted local-groom guides | SHA256 | GitHub Actions |
| --- | ---: | ---: | --- | --- | --- |
| Run96, original anatomical feather-tract attempt | 4,381,476 | 24 / 210,660 | 2,500 body + 264 short-wing ribbons | `506d0b416c30ab96e7825150f8d4df5c4c6f3a2f6984a993bbf51dde8ae29915` | [43765285288](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43765285288) |
| Run96B, warm face / buried feather trousers / shorter vellus / lower exposure | 4,483,508 | 24 / 220,216 | 1,550 body + 286 short-wing ribbons | `9d70385786763ff7bdadd740299de6ddb563b2f0902eb6690b1a822b723d6e2f` | [43765708783](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43765708783) |

Both actual Actions jobs completed successfully, permanent evidence was independently checked by GitHub readback and contains GLB, four actual original Cycles renders, contact sheet, two browser screenshots with machine-readable JSON, sculpt/render scripts, logs, metrics, SHA256SUMS, non-release warning. Research directories:

- `research/owl172-run96-anatomical-feather-tract-native-sculpt` → `owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run96-REAL-ANATOMICAL-FEATHERTRACT-UNAPPROVED/`
- `research/owl172-run96b-disc-wing-shortdown-light-ablation` → `owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run96B-DISC-WING-SHORTDOWN-UNAPPROVED/`

Run96 and 96B technical controls: 3D body outer mesh watertight, real GLB parsed/reimported, glTF has 24 COLOR_0/PBR material primitives, correct +Z eye-forward model axes, both Chromium WebGL2 cases loaded and rotated with zero graphical errors and in-frame bounds. These are **only technical smoke checks**, not beauty, rigging or mobile performance tests. Notably the rotated browser screenshot displays a side/back view because the automatic test moves the camera before capture, not necessarily the starting front view.

## Actual visual review — reject BOTH

**Run96 four-view contact sheet actually opened:** creamy white blunt smooth round skull sits above stringy wet-mop/fibrous body. The tiny dot eyes and flat beige rim make the apparent heart disc more like a pasted mask than natural dense facial plumage. Strict profile has virtually no credible buried wing shape; legs are long bare sticks; wood support is a scalloped cylindrical cut section instead of the reference's broad tree hollow. Rear is a tall oval seed covered in dangling fibres. This does not meet a high-quality juvenile Tyto anatomy gate.

**Run96B contact sheet actually opened and compared:** warm facial-disc shading and lower lighting make less visual clipping; shorter wider feather ribbons reduce dangling strings but instead reveal scattered **white cornflake/flaking stipple**. Upper head becomes an almost unfeathered smooth egg and face remains a shallow heart-shaped plastic mask with two disconnected bead eyes and tiny pointed nose. New wing/feather-trouser bulges produce **oversized lateral arms and short separate thigh lumps**, worsening juvenile anatomy. The circular scalloped wood base remains unlike a eucalyptus hollow. In side and rear, elongated upright body and no plausible shoulder / covert planes persist. Real-browser desktop screenshot was opened: it renders a genuine interactive 3D mesh but exposes the same geometry defects and noisy short feathers.

The second iteration is **not** a successful transformation; changing strand length, darkening the heart and inflating the wing mounds produces another toy shape. The user explicitly rejects simplistic artificial-looking character quality. Both model versions remain **ART_REJECTED**; do not send the actual GLB as a 'good sample' or call it mobile-ready.

## New technical learning and stop-loss guidance

- Existing Run91 PBR black-body fix remains valuable. Technical material, axes, watertight geometry, render pipeline and software-browser validation no longer block experimental production.
- More procedural SDF ellipsoid/protrusion editing and procedural feather ribbons cannot match the real target's rounded plumage, neck/shoulder silhouette, facial micro-feather texture, and natural wing tracts. Do **not** increase 3D triangles or hair count as a substitute for art quality. Both versions already exceed 200k triangles; actual phone GPU cost could be prohibitive.
- The next useful independent path is **human-grade anatomically sculpted juvenile source** with documented licensed provenance, realistic short layered down/hair from professionally placed guides, then retopology into a much lower-poly mobile LOD with baked feather maps and native physical-device verification. Image-to-3D single-photo reconstruction lacks grounded side/back and earlier TripoSR already failed. A connected external creative model selected with a strict US$0 budget returned **interactive approval required**; no unapproved charge or model run was attempted.

GitHub compare `main...research/owl172-run96b-disc-wing-shortdown-light-ablation` returned all 154 modified paths within `.github/workflows/owl-pet-172-*` or `owl-pet/3d-experiments/172-tyto-castanops/**`; **zero** edits to 251-species production, scientific record, original reference plate, current pet prototype, root game, or deployment. No external payment or private credit usage.

**Release gate: ART_REJECTED. Keep research evidence; no success notification or approved 3D sample.**
