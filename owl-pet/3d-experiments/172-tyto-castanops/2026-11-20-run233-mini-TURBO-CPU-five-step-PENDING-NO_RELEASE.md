# #172 Run233 — Official Hunyuan3D mini-Turbo CPU actual experiment; PENDING / NO RELEASE

**Date:** 2026-11-20 (Asia/Shanghai). **Target:** rightmost cream age-unknown mesoptile from `owl-pet/design/concepts/172-tyto-castanops-v3.png`, 737,545 bytes, SHA256 `881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d`.

## Rechecked

Read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/STATUS.md`, `owl-pet/research/species/172-tyto-castanops-v3.md`, Run231 art-rejection audit and Run228 official CPU study. Current prototype is still a cat; 251-species plate production is independent. Run228 standard Hunyuan3D-2mini downloaded and loaded weights but reached only the first of 20 CPU diffusion steps before 2,250 s hard timeout; first step took about 12m12s.

## New actual trial

The [Tencent official model zoo](https://github.com/Tencent-Hunyuan/Hunyuan3D-2/blob/main/docs/source/modelzoo.md) names the distinct 0.6B step-distilled `hunyuan3d-dit-v2-mini-turbo` checkpoint. Rather than retrying 20 standard steps, submit five distilled inference steps with the same authenticated rightmost concept crop (including restored pupils), isolated on free public GitHub Actions CPU. No paid external API/GPU, no main or production modifications.

A separate executable Python script produces native GLB only after actual neural shape inference, reimports it to verify finite nonzero spatial axes and faces, then makes seven true 3D-camera VTK renders. Reject solid black, nearly empty and identical views using pixel and hash gates, learning from Run231 FXAA false positives. The GitHub workflow archives logs, model files and images or failure diagnostics as a temporary Actions artifact; independent art review is required after the run. Green CI is not artwork acceptance.

**Actual launch status at writing: PENDING / NO_VERIFIED_NEW_GLB / ART_NOT_APPROVED / PHONE_WEBGL_NOT_TESTED / NO_RELEASE.** The model is community/noncommercial-licensed, so commercial release is not authorized. Require real organic heart disc, cream down, juvenile wing/tail/proportions, plausible rear and profile, broad hollow lip support, then mobile WebGL performance before any user-facing sample. This research only never alters the cat prototype or 251-species pipeline.
