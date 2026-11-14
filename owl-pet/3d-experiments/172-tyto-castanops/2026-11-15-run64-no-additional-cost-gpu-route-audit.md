# Run64 independent zero-additional-spend 3D route audit (2026-11-15)

**Objective:** replace repeatedly rejected low-quality scripted down/wing geometry with a professionally plausible real 3D image-to-mesh + manual grooming pipeline for #172, without extra charges.

## Actual environment probe and connector attempt
- Executed local `nvidia-smi` and `torch.cuda.is_available()`: NVIDIA device/utility **absent**, installed torch 2.10.0+cpu, `cuda.is_available() == False`, CUDA GPU count **0**. Current runtime cannot perform heavy local CUDA image-to-3D diffusion inference.
- Blender CLI / `bpy`: absent. CPU environment does have trimesh, scipy/numpy, VTK glTF2 importer, Chromium/Xvfb and Playwright; all were used to produce and inspect actual R/S GLBs in Run64.
- Sandboxed Python download DNS failed for github.com, drive.google.com and huggingface.co; cannot install/download additional open weights through the local container.
- Explicit **$0 per-request** image-to-3D fal service discovery was attempted using the connected model recommender; it required interactive user authorization. In this unattended run **no generation** was executed, no credit was consumed, and no payment was initiated.

## Officially documented alternatives, not executed (hardware/network blocked)
1. **Microsoft TRELLIS.2**, https://github.com/microsoft/TRELLIS.2 and https://microsoft.github.io/TRELLIS.2/ . Open image-to-3D with PBR shape/material output; official README requires NVIDIA CUDA GPU with **at least 24 GB VRAM**. Best candidate for a truly new learned mesh rather than adding fur geometry to the 63 rejected prototypes, but current runtime fails prerequisite. Single-view backside would still be inferred and need manual art approval.
2. **Tencent Hunyuan3D 2.1**, official repository https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1 ; single-image shape/PBR texturing route. The Tencent Community License has use/region conditions unlike MIT and must be separately reviewed; CUDA/inference resources and accessible model weights required. **Not executed**, no claim of free hosted available credits.
3. **Professional Blender mesh / feather grooming** as DCC target, with export to optimized GLB; locally unavailable. Blender 5.2 documentation indicates Geometry Nodes hair/physics tooling, though game export needs baking/mesh/material conversion rather than assuming strand-hair exports as real-time fur.

**Decision:** user requires no surprise charges. Keep ML service executions blocked until a preauthorized truly free quota or GPU-equipped environment is accessible. The Run64 genuine R/S GLB experiments and evidence were completed anyway, but remain ART_REJECTED.

## Next trial, gated
Acquire a legally reusable multiview sculpt/design reference of a similar mesoptile (owner's frontal concept remains art target; third-party photography only viewed where licensed), run zero-cost learned 3D only with verified access, then measure side/back topology and fur in a proper Blender/groom/GLB round trip and real smartphone WebGL. Do not claim these steps completed here.

No production changes, no added fees, no published sample.