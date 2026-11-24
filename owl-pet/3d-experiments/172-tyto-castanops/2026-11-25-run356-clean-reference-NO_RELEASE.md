# Run356 — source alpha cleanup and new-engine feasibility — NO_RELEASE

2026-11-25 Asia/Shanghai. INPUT_PREPARED / ART_REJECTED / NO_RELEASE. No new 3D inference or release.

## Preflight
Re-read main README, STATUS (206/251, 45 remaining), DESIGN_WORKFLOW, actual prototype/index.html and 172-tyto-castanops-v3-review.md (blob 50ab5259987180a6a46a428317440f2436bfce56). Two guessed AGENTS/species paths returned 404; no claim of reading them. Run355 note retrieved at 6e1439b04aa4634b376fff37e70771ac56efe487. Restored Actions artifact 14733006902 and extracted ZIP; actual GLB SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117 matches Run355. Visually opened historical 512px masked source and the 451×540 RGBA original crop. Target remains the rightmost age-unknown cream mesoptile, no replacement by later v4+.

## New, executed input experiment
Historical mask contains two disconnected bark/branch fragments at lower right. OpenCV connected components on alpha>127 yielded [x,y,w,h,area] = [14,12,418,523,164197], [404,500,33,28,429], [384,521,4,5,16]. Removed the 445 hard foreground pixels outside the largest connected component, retained all main-component hard alpha values exactly. Retained soft edge only within 7×7 dilation of main component; made separate edge-decontaminated variant using nearest opaque pixel colour, 0.8×(1−alpha) blend. No generative additions, no anatomy invention, no opaque-interior RGB changes (measured 0). Used premultiplied INTER_AREA resampling into 512×512, longest foreground dimension 440, exported true RGBA and neutral gray RGB for each of three inputs. Cleaned crop bbox [13,10,433,536] vs original [13,10,438,536], resized hard foreground 114803 vs 115056 pixels. Actual 768×282 comparison JPEG visually checked: small isolated branch pieces disappear, eyes/face/feet remain discernible, fur silhouette substantially retained. Edge decontamination visually subtle. The benefit to reconstruction is untested; do not infer that the prior floating 3D fragment necessarily came from the source debris.

### Reproducible method (core operations, not verbatim full executed source)
```python
# src = RGBA source_crop_and_alpha_RESEARCH.png from artifact 14733006902
import cv2, numpy as np
from scipy.ndimage import distance_transform_edt
rgb, af = src[:,:,:3], src[:,:,3].astype(np.float32)/255
n, labels, stats, _ = cv2.connectedComponentsWithStats((af>127/255).astype(np.uint8),8)
main=1+np.argmax(stats[1:,4])
component=(labels==main).astype(np.uint8)
near=cv2.dilate(component,np.ones((7,7),np.uint8))>0
other=(labels>0)&(labels!=main)
clean=af*near
clean[other]=0
interior=clean>=.98
_, inds=distance_transform_edt(~interior,return_indices=True)
nearest=rgb[inds[0],inds[1]].astype(np.float32)
weight=(1-clean)[...,None]*.8
rgb2=np.rint(rgb*(1-weight)+nearest*weight).clip(0,255).astype(np.uint8)
# Fit alpha>.08 bounding box to longest dimension 440 in 512 square;
# INTER_AREA resize premultiplied RGB and alpha, divide by alpha; export RGBA
# and composite over (128,128,128).
```
Executed full source SHA256 90bb5b95daf3d115872120f76142d52ef1ad43441b64f69726a1025751d72779. Actual full comparison SHA256 ff1536614bb248f64b1e264062318110b3ee290777ea49f5a021391b76e547a1. Clean RGBA SHA256 093d162ce0e5b28f3be6019006c7c44bf579da4b0bd092eee6d841ffe24d8da7; clean gray 2bba24820d84f3c3ac234f455d1da7642b47a8461698842cccb3f43bcf63ed18; decontaminated RGBA 15660f8f66c33a832ed7d2f32c6fc34a2deb0f93960a3e8aa76d744c4f0711b9; decontaminated gray 1258cda9fa28dccfc761fb4944f3a2378440f8e50cd81f76b2af88747045298b. Full files local to execution unless separately archived.

## Free donor / alternate engine attempts
- https://www.innerscene.com/tools/library/3d-parts/owl-d696472a advertises 19.7 MB textured GLB CC0, species/age unspecified. Actual download endpoint https://www.innerscene.com/api/library/owl-d696472a/download: web fetch unsupported octet-stream, direct Python requests DNS failure, container download failed. No model inspection or adoption. Not a validated juvenile donor.
- https://github.com/senacula/senacula-shapestudio/ README: CPU tier is TripoSR (not a different reconstruction engine); TRELLIS tier requires 16GB NVIDIA GPU and not integrated; README explicitly says measured full trained reconstruction not yet reported. No useful new engine here. Actual release URL GET DNS failure.
- SPAR3D model page https://huggingface.co/stabilityai/stable-point-aware-3d direct GET DNS failure. Current local torch 2.10.0+cpu, CUDA false, 5 CPUs, bpy absent. Restored earlier artifact reports GitHub hosted runner 15GiB memory and real successful TripoSR CPU inference; no dispatch action available in current GitHub connector. No new workflow created, no paid jobs submitted, zero extra spend.
- https://sketchfab.com/3d-models/owl-86ec461ab6404628b10fcdc26ac004dd listed CC BY-NC despite description referring to CC BY, adult/unspecified morphology, not qualified for unrestricted reuse or target identity.

## Gate
No new GLB. No repeat cosmetic repair of rejected donor. Previous headed software WebGL test stands; no new physical phone test. Future actual engine input should use cleaned RGBA and gray pair and compare with original under same reconstruction engine. Preserve target reference and all original production assets. Research branch only; no edits to main, production, prototype, or deployed site.
