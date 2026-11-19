# Run211 — official Microsoft TRELLIS.2 public ZeroGPU trial setup and execution boundary (NO_RELEASE)

Date: 2026-11-19. Species: **#172 Tyto castanops v3 / rightmost AGE-UNKNOWN MESOPTILE**. Independent research branch: `research/owl172-run211-hf-trellis2-zero-gpu-evaluation`. Not an accepted model and not part of 251-species production.

## Preflight re-read

The repository's `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/STATUS.md`, and `owl-pet/research/species/172-tyto-castanops-v3.md` and cat-only `owl-pet/prototype/index.html` were retrieved on this run. Previous Run208b face/groom rejection, Run209 WebGL technical proof for an older refused GLB, and Run210b complete adult tufted owl source refusal were reread. The scientific design target is a compact cream down-covered **juvenile with naturally integrated heart facial disk, dark eyes, short buried wings, concealed tail, and both feet/belly supported on mature hollow lip**, with **no claimed exact age**. No photorealistic or mobile-ready sample exists yet.

Source design plate `owl-pet/design/concepts/172-tyto-castanops-v3.png` fetched from main as original base64 and decoded for visual inspection via connected GitHub. It shows a cream nestling at far right; full-plate SHA256 `881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d` was confirmed by prior Run210b audit; **this run did not independently hash the 983,396-character decoded pixel content** (workflow will hash original checkout bytes before inference). This is premium stylized 2D concept art, **not** a ready-made 3D asset.

## Distinct model-generator route and actual isolated repository actions

Abandoned previous repeated free adult asset searches, SDF geometric fur tweaking, TripoSR single-view attempt, and failed third-party keyless TRELLIS service. Read the official [Microsoft TRELLIS.2 public Hugging Face Space](https://huggingface.co/spaces/microsoft/TRELLIS.2) and its [published Python inference functions](https://huggingface.co/spaces/microsoft/TRELLIS.2/blob/main/app.py). At research time, official Space publicly declares **Running on Zero**; its image-to-3D stage generates sparse/shape/material latent plus PBR previews and a **separate GLB extraction** stage. This is technically different from the earlier Run206 free third-party text-to-3D endpoint, and it can represent non-flat PBR geometry when successful. Availability or free quota for this account is NOT assumed.

Created actual reproducible script [run211_hf_zero_gpu_trellis2_probe.py](run211_hf_zero_gpu_trellis2_probe.py) and branch-only workflow `.github/workflows/owl172-run211-zero-gpu-research.yml`, using GitHub connector and remote readback. The script checks the exact original plate hash, crops only `[950,255,1440,850]`, performs GrabCut and validates alpha coverage, then **attempts exactly one** official, unauthenticated, low-resolution ZeroGPU inference (seed `172211`), separately requests GLB extraction, checks returned binary magic and Trimesh geometry, and if present actually VTK-renders seven viewpoints. On any failure it writes an explicit error JSON and NO_RELEASE, with model/art never auto-approved. The workflow uploads trial evidence for 30 days and commits **only** the report JSON+Markdown into this isolated research branch.

Verified repository commit for script: `655b599e336fb41f084e94b155ca10c2b1147d99`, workflow: `f817f7dfcda689bd8e50749725333c61c628be2e`. Repository comparison from exact Run210b SHA `56e34c72d062066dde001c7cf1611bb3bbeb8032` reports exactly **two added files**, script and dedicated workflow. No `main`, root game, 251-species pipeline, existing prototype, published render, design manifest or deployment mutation.

## Synchronous execution evidence and limitation at writing

The isolated push-triggered GitHub Actions workflow was **submitted through a real GitHub commit**. On this turn, the remote output `run211-evidence/run211_report.json` was probed via GitHub twice and **returned HTTP 404 both times**. The workflow run ID, its status, any actual accepted public GPU job, GLB extraction, seven-view screenshot and artifact ZIP **have not been retrieved or verified**. A push is not proof the hosted inference executed or succeeded. **Do not claim a new GLB or 3D advance without actual report, model-hash readback, seven-view independent aesthetic review and real-device acceptance.**

Checked sources for other legally accessible assets: [Blendkit's 2025 baby barn owl](https://www.blendkit.com/asset-gallery-detail/af064619-74d4-496f-bdde-bdc742e08824/) requires its **Full Plan** and is not a gratis option; [CGTrader ArtistFrog baby owl](https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt) has a no-AI license and prior download HTTP 403, so not reused; CC0 Great Horned Owl and Innerscene adult are biologically unsuitable. A documentary [2018 photograph of a young Tasmanian masked owl with fluffy chick](https://www.lukeobrien.com.au/young-masked-owl-raptor-refuge) confirms photographic juvenile facial/fluff differences but was **not imported or used as texture/model input** (no permission to reuse asserted).

## Gate and costs

**PENDING_EXECUTION_READBACK / NO_NEW_VERIFIED_GLB / ART_NOT_PASSED / NO_MOBILE_HARDWARE_QA / NO_RELEASE / NO_NOTIFICATION.** No fee was authorized, no paid call submitted in this run; remote workflow strictly selects the public unauthenticated route and has no paid fallback. When any remotely reported GLB becomes accessible, seven-view independent art inspection is still mandatory. Do not link or display an unreviewed result as the electronic pet.

Artifact storage: this Markdown and source/workflow are persistent GitHub research records. **No binary or image report archive has yet been confirmed from this trial.**
