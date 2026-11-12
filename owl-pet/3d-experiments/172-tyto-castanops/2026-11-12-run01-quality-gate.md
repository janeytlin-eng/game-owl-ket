# 棉棉 #172 — 3D角色自主探索 Run 01 (2026-11-12)

## Scope and provenance
Independent 3D pet experiment only. Canonical concept stays `owl-pet/design/concepts/172-tyto-castanops-v3.png` (Git blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`); target is its **right-hand cream, age-unknown mesoptile**, not the adult birds. Read `research/species/172-tyto-castanops-v3.md` and `research/reviews/172-tyto-castanops-v3-review.md` before building. Exact age and detailed feather chronology remain unsupported. Preserve all source concepts, manifests and production workflows; this run changes none of them.

## Actual tool and prototype work
- Inspected availability: no Blender/bpy, no local image-to-3D pretrained weights, no accessible CUDA GPU. Available: Python trimesh, skimage marching cubes, VTK 9.6.2 offscreen renderer.
- Attempted a **real polygonal 3D mesh** (not SVG, not 2D sprite) using Python: SDF-derived continuous head/body surface, short down-covered wings, volumetric facial shield, raised eyes, curved bill, sculpted toes/talons and 3D down-fiber strands. Exported and reimported GLB; rendered frontal, three-quarter, side and rear checks.
- Initial `v01`: 39 geometry components, 185,807 triangles, GLB 4,920,424 bytes; SHA-256 `b11ef89d240cc3097e82f4adf61e6e9fb6ced9a0e72b357fc940188367440543`.
- Revised `v02`: 38 components, 189,856 triangles, GLB 5,485,548 bytes; SHA-256 `26e9dcbae092b1cb5211225529e54632a528d3d7a1fd8e1c45a0957551e74a02`. Reduced the rigid outline, altered eye sockets and proportions, blended head/body, warmed fur colours and reduced foot proportions. Offscreen VTK 4-angle review regenerated. Reloading GLB succeeded.
- Source of all render and mesh artifacts: current run's separate working bundle `mianmian_3d_exploration_run01.zip` (8,549,102 bytes). This log archives metrics and audit findings, **not** finished character art; binaries remain separate and have not been committed to canonical production assets.

## Visual gate — FAIL / DO NOT NOTIFY USER
Both render sets fail the user's '有点看得过去' bar. Specifically: (1) facial shield still reads like an applied heart emblem rather than the plush, deeply integrated Tyto facial disc, (2) eye sockets still look too manufactured, (3) down fibers render as tiny noisy needles rather than thick soft second down, (4) toes/legs and stance appear stiff, (5) side and oblique views are visibly less convincing than the front. Real 3D alone does not establish quality; do not label this accepted or share these as a polished demo.

## Blockers / next experiments
- fal Hunyuan 3D Pro currently blocked by exhausted connected-account credits. No payment authorized; no further paid generation attempted.
- Public open-source InstantMesh is a plausible image-conditioned reconstruction stack but requires CUDA plus substantial pretrained weights; no such weights/GPU exist in this local runtime. The Anatomy Skill is primarily framework-free isometric SVG technical figures with some optional WebGL demos, not a furry 3D character reconstruction engine.
- Prioritize high-fidelity multiview image-conditioned sculpting or physically groomed dense down with higher-quality physically based material, and rebuild eyes/face geometry before developing animations/interaction. Record independent front/quarter/side/rear QA and only invite user review after visual pass.

**Status:** exploratory FAIL, no approved 3D owl, no effects on the 251-species production process.
