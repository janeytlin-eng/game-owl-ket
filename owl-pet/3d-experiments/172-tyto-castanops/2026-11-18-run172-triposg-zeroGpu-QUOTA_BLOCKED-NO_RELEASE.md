# Run172 — Official TripoSG ZeroGPU actual inference gate: QUOTA_BLOCKED / NO_RELEASE

**Executed:** 2026-11-18 07:15 UTC, dedicated research branch only. **No accepted art, no 3D model or mobile test, no purchases.**

## Preflight and actual operations

The CI job reread the existing owl-pet project rules, README and older cat WebGL prototype, the #172 v3 rightmost cream-white mesoptile design boundary, the Run169 six-angle rejection, and the rejected model SHA registry. The actual 512×512 rightmost juvenile input passed SHA256 comparison: `5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9`. Run170 yielded no new GLB, and the independently completed Run171 public 3dai trial also yielded no GLB (`PUBLIC_GENERATION_ERROR`).

New Run172 used the *official* public Hugging Face ZeroGPU space `VAST-AI/TripoSG` via its published Gradio Client interface. It successfully connected and retrieved the real live schema: 9 endpoints, including `/run_segmentation`, `/image_to_3d`, and `/run_texture`. This proves transport/API discovery, **not** generation.

Actual public inference outcome, captured verbatim in `research-evidence-run172-TRIPOSG-OFFICIAL-NO_RELEASE/run172_actual_results.json` and `run172_exception.txt`:
- `/run_segmentation`: provider denied the request because it requested **60 GPU seconds** and reported **0 remaining**; `gradio_client.exceptions.AppError` suggested authentication for quota.
- `/image_to_3d`: provider denied the one shape-generation request because it requested **90 GPU seconds** and reported **0 remaining**; same quota error.
- **No inference completed, no downloaded GLB, no Blender/VTK 3D-angle renders, no real phone GPU/WebGL test, no accepted juvenile anatomy/down.** CI's green status represents evidence recording and archive, not visual quality.
- No login, quota/account rotation, security challenge bypass or external purchase was attempted. **Additional spending: $0.**

## Reproducibility and isolation

Actual run: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44257401025 .

Research-only workflow: `.github/workflows/owl-pet-172-run172-triposg-native-qa.yml`; script: `owl-pet/3d-experiments/172-tyto-castanops/tools/run172_official_triposg.py`. The workflow saved live official API schema, raw request outcome, exception trace, explicit `NO_RELEASE.flag`, negative native-render note, execution logs, source SHA verification and SHA256 manifest, all under `owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run172-TRIPOSG-OFFICIAL-NO_RELEASE/`. Eight raw payload hashes were checked before archival. The isolated GitHub Actions artifact ID is **14406705967** (archive digest SHA256 `a36d01afb3bd72a9ac2c2157cdd317ee0c012bba1b5f516bfac5e86a69593664`); it contains **no successful model**. No model binaries were committed.

Immediately before this postmortem, branch comparison with Run170 baseline reported **4 commits ahead, 0 behind, 12 changed paths**, all either in the dedicated #172 experiment directory or its unique Run172 workflow. Nothing on `main`, the 251-species production flow, original concept plate, old WebGL prototype, deployment or other owl species was changed.

## Next legitimate path

The ZeroGPU quota is an access block for this provider, not a failure of an actual TripoSG geometry or art render. On a later authorized free allocation, a single genuine shape inference can be attempted with provenance bound to the juvenile reference; render and visually inspect anatomical front/side/back before a product-quality claim. In parallel prioritize freely accessible, licensed artist-sculpted *juvenile Tyto* anatomy and a WebGL-compatible natural down groom. Do not disguise old rigid adult/neurally generated rejected sources with material-only improvements. Any downstream model must meet the independent visual, rights, and physical-phone WebGL gate before any user sample or notification.

**Final status: SOURCE_QUOTA_BLOCKED / NO_NEW_GLB / ART_UNREVIEWED / NO_RELEASE.**
