# Run211c — independent readback of actual official TRELLIS.2 ZeroGPU trial: QUOTA_BLOCKED / NO_RELEASE

Date: 2026-11-19 UTC. #172 *Tyto castanops* v3 rightmost age-unknown cream-down juvenile. Research branch only; no production changes or user release.

## Evidence actually recovered

The previously unverified push-triggered workflow **did execute**: [Run211 Actions run 44504537633](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44504537633), job ID `135492574941`, created 2026-11-19 10:19:10Z, finished 10:24:12Z. Retrieved complete job-step summary and decoded job logs independently via GitHub connector in the next research run. Preflight succeeded; exact v3 plate `owl-pet/design/concepts/172-tyto-castanops-v3.png` hash: `881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d`, rightmost crop `(950,255,1440,850)`, mask nonzero ratio `0.5475252958326188`, masked input hash `fcb3527dae6fa9aee4428d9c76ee803106a4be313a9f2ae40047465e84fa8819`.

`gradio_client` successfully discovered official `microsoft/TRELLIS.2` Gradio endpoints `/image_to_3d` and `/extract_glb`, and submitted one unauthenticated public generation task (`submitted:true`). It returned **before generation**:

> You have exceeded your ZeroGPU quota (120s requested vs. 26s left). Try again in 0:18:44. Authenticate with a Hugging Face token for more quota

No inference, PBR geometry, preview, GLB, native seven-view render or smartphone GPU test was produced. Report status `REMOTE_OR_INPUT_FAILURE_NO_RELEASE`, runtime 5.29s, extra paid spend $0.

## Durable evidence and write error

The evidence upload step **succeeded**, creating [Run211 artifact 14518503130](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44504537633/artifacts/14518503130), name `owl172-run211-source-zero-gpu-evidence-NO_RELEASE`, 617,373 archive bytes, digest `sha256:18720fd90b1ffdabc3a242cb32e68a7638f543fa2f12fa825b0aa4738413a7fb`, expiry 2026-12-19T10:24:05Z. Contains four recorded files (crop, RGBA crop, report JSON and Markdown). Archive existence and digest were independently checked through GitHub's artifact metadata, but ZIP bytes were **not** downloaded or individually hashed this run.

The Actions workflow's last step attempted commit `e86d0d9` to the Run211 research branch; remote push was rejected **non-fast-forward** because branch was updated concurrently by the earlier audit commit `aae457ca...`. Thus its report never reached that branch, although the execution and artifact upload succeeded. This new Run211c note records the recovered facts on a **separate** Run212 research branch; it does not rewrite Run211 and does not claim that the original artifact was promoted to a permanent release.

## Decision and next distinct attempt

**NO_NEW_GLB / NO_ART_PASS / NO_MOBILE_GPU / NO_RELEASE.** Two GPU-only TRELLIS.2 stages each declare a potential 120s allocation; unauthenticated ZeroGPU includes 120 seconds daily, so unauthenticated completion cannot be assumed even after quota refresh. Do not spend money or repeatedly hammer that blocked endpoint. The next experiment tests a distinct official single-stage PBR-capable model with public free quota, while treating any success as unapproved until seven independent true-3D views pass aesthetic inspection. No edits to main, 251-species production, established prototype or deployment.
