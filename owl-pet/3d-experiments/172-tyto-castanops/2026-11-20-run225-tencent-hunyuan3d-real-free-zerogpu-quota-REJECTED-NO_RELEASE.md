# #172 Run225 — official Tencent Hunyuan3D-2, real public textured-GLB request: QUOTA_BLOCKED / NO_RELEASE

Date: 2026-11-20 Asia/Shanghai (real workflow UTC 2026-11-19 20:34–20:41). Study branch: `research/owl172-run225-hunyuan-zero-gpu-real-juvenile-glb-qa-no-release`. Extra payment: **USD 0**. No production change.

## Source, constraints and prior evidence actually checked

Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `research/species/172-tyto-castanops-v3.md`, Run01 visual gate, Run211c/212 official free inference failures, Run223 museum donor and Run224–224b corrected true 3D donor studies. The existing prototype is a cat WebGL prototype, not a validated owl. This trial is detached from the 251-species flow and does not alter the original concept or manifests.

Verified the full 1536×1024 official `owl-pet/design/concepts/172-tyto-castanops-v3.png` SHA256 `881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d`. Extracted exactly [950,255,1440,850] (rightmost AGE-UNKNOWN MESOPTILE), preserving original RGB, calculated a true-alpha subject mask and repaired the two former transparent pupil holes: 676 and 539 pixels, 1,215 total. Input RGBA SHA256 `7216a7d311408eb0ccb4853397c0233a9da0c7af7881bf58595fef1112c09812`. The composite was **actually opened visually** after downloading the evidence ZIP and confirmed to contain the dark pupils, broad integrated heart face, cream down, compact chick anatomy and both feet; this is **source concept**, not 3D output.

## Distinct actual free 3D generation attempt

Selected the official public `tencent/Hunyuan3D-2` [Hugging Face Space](https://huggingface.co/spaces/tencent/Hunyuan3D-2) rather than retrying the quota-failed Microsoft TRELLIS.2 or Stability AI SF3D runs. Read Tencent's [actual Space implementation](https://huggingface.co/spaces/tencent/Hunyuan3D-2/blob/main/gradio_app.py): `generation_all` has `@spaces.GPU(duration=90)` and exports both `white_mesh.glb` and `textured_mesh.glb`; this is an actual 3D inference interface, not a fake SVG or text prompt. Note that Tencent's repo states a **non-commercial model license**; if a usable model were produced, license suitability would need review before app publication.

Created and remotely verified the independent [Run225 source program](run225_hunyuan2_official_zerogpu_juvenile_qa.py) and [dedicated Actions workflow](../../../.github/workflows/owl172-run225-official-hunyuan2-zerogpu-juvenile-realglb-qa.yml). Actual public GitHub Actions [Run #44610131949](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44610131949) completed successfully at the workflow level; run job ID `135864205797`.

The script authenticated with **no token**, dynamically enumerated the real Gradio endpoints, confirmed `/generation_all` exists, and **actually submitted exactly one** 13-argument native textured-GLB generation call using the validated alpha source. The remote GPU **did not start inference**, returning the explicit message:

```text
You have exceeded your ZeroGPU runs limit. Authenticate with a Hugging Face token for more quota - https://huggingface.co/settings/tokens
```

Do **not** confuse a successful GitHub Actions job with successful generation. The actual source-probe runtime was 5.43 seconds, `submitted:true`, `status:NO_NEW_VERIFIED_GLB_NO_RELEASE`; there is **no GLB, native 3D camera preview, PBR mesh, fur/wing solution, or phone GPU test**. No fallback to paid GPU, no secrets, no service upgrade, no repeated quota submissions. The full machine report and error trace are committed [here](run225-evidence/run225_report.json).

## Independently downloaded and byte-verified raw evidence

GitHub Actions uploaded [Research evidence artifact #14570794889](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44610131949/artifacts/14570794889) (retention through 2026-12-19). The archive **was downloaded independently**, opened in a separate local runtime, and inspected. Archive size **617,300 bytes**; SHA256 **`f05d45288e36fbc88e39f94439533db021303dd81517fe9e72172d191032ac9a`**, matching GitHub artifact metadata. All four internal files opened, and SHA256/bytes checked:

| File | Bytes | SHA256 |
| --- | ---: | --- |
| `run225_exact_young_crop.png` | 297445 | `85a9e50d58ea49ee10e690a835be1d756602b2232d5d77c563fe98dcf2080b06` |
| `run225_canonical_young_RGBA_restored_eyes.png` | 317289 | `7216a7d311408eb0ccb4853397c0233a9da0c7af7881bf58595fef1112c09812` |
| `run225_report.json` | 3710 | `4ad788346db6cf092eed8fa1269b1dc02752e896353d02ddff289304f2e91784` |
| `run225_report.md` | 411 | `a0b2fd0bef645e9f09af0afdc0d3562fcc63ae01df69300bf42049bcb33a0cb4` |

No GLB file in this archive, as independently established by the archive membership. Source image/JSON/Markdown represent genuine execution traces, **not an art deliverable**. The binary artifact is time-limited; the JSON report, scripts, workflow, and this audit are durable research-branch files.

## Decision, release gate and safe direction

**NO_NEW_VERIFIED_GLB / REMOTE_QUOTA_BLOCKED / NO_ART_PASS / NO_REAL_PHONE_TEST / NO_RELEASE / NO_NOTIFICATION.**

Run225 adds a third independently confirmed public ZeroGPU quota barrier, this time a total **runs-limit** rather than Run211/212's remaining-second quota. Anonymous endpoint existence and green CI do not imply GPU entitlement. Do not hammer more anonymous ZeroGPU Spaces or promise models until real legitimate allocation exists. The only actual visually checked asset this run is the unchanged **2D** young concept cutout; do not promote it as 3D. Future work should prioritize genuinely free licensed juvenile 3D assets/art-grade sculpting and reuse the real GroomLab native down/groom test once a believable juvenile base exists. Any future native GLB requires nondegenerate spatial bounds, correct Draco/texture decoding, seven independent real 3D angles, natural heart face, down, short wings, hidden tail, broad hollow support, and separate **real smartphone WebGL** verification. No release until all gates pass.

Branch isolation: Run225 adds only its script, dedicated workflow, run machine report and this audit. No main changes; 251-species prototype production, existing cat code and deployments untouched.
