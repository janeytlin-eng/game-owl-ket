# Run365 — localized foot/support relief ablation (NO_RELEASE)
2026-11-25 Asia/Shanghai. ART_REJECTED. Extra cost $0.

## Preflight
Read main owl-pet AGENTS, README, STATUS (206/251), #172 v3 review (cream thick mesoptile, developed mask, short buried wings, concealed tail, age unknown, science=false), and Run364 at 32f04b63177499d83a8ca6c83952ee1499579733. Downloaded historical Run317 Actions artifact 14795923598 and checked native SF3D source SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be. Viewed isolated reference, and historical true WebGL face/rear/profile images; note historical filenames front/back are reversed anatomically. Reference has bark immediately beneath feet, model fuses this support with feet/body.

## Executed diagnostic
Tested whether targeted relief at the fused basal support can restore a usable toe silhouette without replacing the source geometry. This differs from Run364's triplanar microtexture and Run363's global remesh. Actual local Python/Trimesh/VTK code, retained UV and PBR material; three native GLB exports, reopened, 12 actual 340x340 textured offscreen renders in identical orthographic front/45/profile/rear cameras (base color, not browser PBR). Coordinates in source model units, not biological measurements.
```python
v=m.vertices.copy(); x,y,z=v.T
def smooth(x):
    t=np.clip(x,0,1); return t*t*(3-2*t)
feet=np.maximum(np.exp(-((x-.145)/.094)**4),np.exp(-((x+.145)/.094)**4))
underside=smooth((-.30-y)/.105)
front=smooth((-.045-z)/.13)
rear=smooth((z+.12)/.23)
for name,central,back in [('control',0,0),('gentle',.055,.035),('strong',.105,.070)]:
    q=m.copy(); vv=v.copy()
    dy=underside*(central*(1-feet)*front+back*rear)
    vv[:,1]+=dy; q.vertices=vv
    q.export(name+'.glb')
    re=trimesh.load(name+'.glb',force='scene').dump(concatenate=True)
    welded=re.copy(); welded.merge_vertices(merge_tex=True,merge_norm=True)
```

| Variant | vertices | triangles | bytes | affected vertices >.001 | max lift | SHA256 |
|---|---:|---:|---:|---:|---:|---|
|control|16971|27372|2556924|0|0|f27f9244f3657806c50d0922fc24f446c52183397d66f1979802a3a912c7f14b|
|gentle|16971|27372|2556924|3861|.05480785|c86b7daca809c1b584e08ca854e82785f24fd8c07d4f83bf39f32a2820193730|
|strong|16971|27372|2556924|4019|.10463317|fadef118e0c3d38220fa96f288bb4fcc857f738d3618969e03106f55f555be0f|

All three reopened and welded copies watertight. Viewed actual 1360x1020 contact. Gentle improves midline relief only slightly; strong makes a false arch in the fused support and distorts rear underside into a visible horizontal strip. Neither separates digits or recovers believable ankle anatomy; side profile still flattened, rear wings absent, crown dark, no volumetric down. Reject all. Watertightness is not proof of anatomical fidelity or absence of self-intersections. No new browser or phone validation; no release.

## Alternative route / limits
Checked https://github.com/Chethan-ULTIMAX/VIEWFORGE (six orthographic silhouettes, no license declared; no use of its code), https://github.com/zaidku/Pix2Mesh (multi-image visual hull/SfM), https://github.com/cdcseacave/openMVS (multi-view stereo). These require consistent multi-view inputs/poses or point cloud. Current original is a single view with fused bark, so these cannot establish unseen toe concavities or rear anatomy. They are research leads only, not executed reconstructions. Actual curl HEAD github.com failed DNS code 6; torch.cuda.is_available() False, Blender/bpy absent. No paid service invoked. Prior repair series suggests new source anatomy or coherent multiview references are needed; do not continue identical support-only morph as an art solution.

## Evidence
Local executed experiment.py SHA256 e71faf0ae11248f938caf11ea38c6e7c5533eb2a9ed1181d4a660b9b985d64a9; report.json 1781697e38afcc5a6c77ddb23c9fd01a1176757a7f64e50cd74ac837b51ea7ce; full contact.jpg 56490d61bd7ff2c7bf62364ad9f70506337ce8abdfd58e8c98fe2d1fd9c71c7c. Full artifacts local to execution. Embedded tiny actual-render contact (120x90; SHA256 4e54d00725ad020afffdf26389c7841a3b92438f32d1ded4c203b47b7a02d3bd, evidence only; not adequate for art review), rows control/gentle/strong, columns face/45/profile/rear. No changes to main, production, original concept or deployment.

```base64
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
```
