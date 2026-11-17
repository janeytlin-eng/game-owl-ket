# #172 *Tyto castanops* v3 rightmost mesoptile — Run152 verified real-GLB anatomical camera & PBR ablation

**2026-11-18 Asia/Shanghai — FINAL: ART_REJECTED / NO_RELEASE.** No acceptable mobile WebGL pet, no publishable replacement model, no extra external payment. The native renderer and GitHub Actions evidence-gathering did run; their success is **not** art approval.

## Re-checked inputs before any modeling

Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/research/species/172-tyto-castanops-v3.md`, the negative GLB registry, and actual Run151 status and native four-view output. Original #172 rightmost 512x512 RGBA juvenile is independently pinned in Run151; its clean-alpha 1024px submission generated a **real textured GLB** via 3D Valley free daily TRELLIS.2. Model bytes **11,489,420**, SHA256 `f05ad553ebf00a495a4f1593ca2a1949a277ad98ecdd334cb4a75d7283bbec76`, glTF-reported **195,160 triangles**, 1 mesh, 2 images, 1 material. This SHA was *not* in the eight-fingerprint negative list when the Run152 test began. It was re-fetched directly from the actual Run151 GitHub Actions research artifact (source run ID `44177303698`) and its exact bytes verified before Blender import. No repeated neural API generation or paid call was made.

**Important actual Run151 camera finding:** Reading its genuine native 2x2 sheet showed that `front` unexpectedly displayed the bird's back and `back` the facial disc, due to camera direction, not a zero-face mesh. The correct **anatomical front** for this imported model is **+Y**, and **anatomical back** is **-Y**; side is +X. The new test explicitly uses these labels. This corrects evidence interpretation, not the deficient mesh.

## Real experiment executed and inspected

Isolated `tools/run152_orientation_pbr_audit.py` was run on a GitHub Actions Ubuntu 24.04 CPU runner with **Blender 4.0.2**. Original imported polygon count: **195,159**, bounding dimensions **0.625 x 0.992 x 0.765 Blender units**. First attempt failed because the Ubuntu Blender installation lacked `python3-numpy`; the workflow was fixed and actually rerun. Cycles denoising was disabled, avoiding Run150's missing OpenImageDenoiser problem. Eight independent **480x480** real Cycles 16-sample renders were produced: true front, 45-degree quarter, strict side and back, each for the original and one *shader-only* PBR cream-lift control. The only material `Material_0` was touched for the control. There was **no edited geometry, sculpt, hair groom, GLB export or rig** in this ablation.

**Actual visual comparison, after opening the complete eight-view contact sheet:**

- The true front has a recognizable, quite small heart-like facial disc, but its eyes read too narrow and recessed; the source has two substantially rounder, open dark eyes. Large talons are exposed in midair, with no broad old eucalypt hollow-lip support.
- Original body and crown are covered by coarse, dirty brown/grey fractured patches and crystalline-looking islands, *not* airy ivory/cream second-down. Strict side shows an elongated mature wing/body contour and a rear silhouette unlike a short-winged, tail-hidden crouched juvenile; the back is more obviously an unstructured speckled mound.
- Mixing roughly 28% warm cream into the existing base-colour shader **makes eyes pale/grey and erases useful dark-eye contrast**, while the coarse back/side texture and anatomical failures persist. This version is in important respects **worse**. Material recolouring does not create real down or juvenile morphology.

Thus the controlled ablation **rejects** the whitening shortcut; neither version is visually basically acceptable. No phone WebGL test was done, since art already fails. The machine-learning output has no animation or tree-hollow support. A rendered material test is not a distributable new GLB, and source terms do not prove morphology or device compatibility. Do not use either image as a good sample.

## Evidence and rights boundary

Open the [actual original-versus-PBR true-direction comparison](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run152-orientation-controlled-true-pbr-audit/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run152-ORIENTATION-PBR-NO_RELEASE/run152_native_comparison_actual_UNAPPROVED.jpg), [Blender dimensions and complete view manifest](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run152-orientation-controlled-true-pbr-audit/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run152-ORIENTATION-PBR-NO_RELEASE/run152_actual_blender_stats.json) and [full actual Blender log](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run152-orientation-controlled-true-pbr-audit/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run152-ORIENTATION-PBR-NO_RELEASE/run152_blender_actual.log). The source GLB and other binary repeats remain only in the 30-day quarantined Actions artifact, not the final Git branch, nor in production. The research branch records 8 new actual views, the contact sheet, hashes, actual source acquisition records and the NO_RELEASE flag. **37/37 evidence checksum entries verified OK**.

3D Valley's official [terms dated 2026-11-05](https://3dvalley.com/terms) say it claims no rights to outputs and allows results to be used, including commercially, subject to law and rights in uploaded content. This is **provider's published claim**, not a complete independent legal clearance of the generated GLB, inputs or model weights, and does not authorize publishing failed art. No paid credit or billing action was performed.

The first Run152 test incidentally staged third-party GLBs when copying the prior complete artifact; **the temporary Run152-only branch was reset to its own pre-artifact commit**, then the workflow was corrected to remove *all* GLB/FBX/BLEND/OBJ/ZIP files from git staging. The successful rerun archived only evidence. Subsequent GitHub comparison confirmed **zero GLBs in final Run152 branch delta**; the binary is quarantined in Actions artifacts. The new rejected SHA was appended to `known_rejected_asset_sha256_registry.json` to prevent re-downloading this same asset.

## Isolation and next gate

All additions/changes relative to Run151 are limited to `owl-pet/3d-experiments/172-tyto-castanops/**` and dedicated `.github/workflows/owl-pet-172-run152-...`; no changes to `main`, the 251-species production pipeline, concept images, original cat WebGL prototype or deployment.

The failed lighting-only variant reinforces existing Run121/Run141 negative results: do not try to hide adult morphology under recolouring, add large crude eye balls or decorate a wrong source mesh with spiky procedural fibers. The missing art foundation remains a specialist-quality naturally downy Tyto juvenile full 3D sculpt/groom or significantly stronger true multiview generation with rights and rear/side verification. Only after **actual front/quarter/side/back art pass** should we prepare a rigged/LOD GLB and test touch-controlled WebGL on real mobile hardware.

**Final: ART_REJECTED / NO_RELEASE. No public pet sample or notification.**
