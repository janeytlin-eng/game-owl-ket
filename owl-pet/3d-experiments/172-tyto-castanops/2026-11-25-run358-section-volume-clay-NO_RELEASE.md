# Run358 — sectional dorsal-volume correction, neutral clay diagnostic — NO_RELEASE

2026-11-25 Asia/Shanghai. ART_REJECTED / NO_RELEASE.

## Preflight
Read main owl-pet AGENTS, README, STATUS (206/251, 45 remaining), #172 v3 review (cream mesoptile, exact age unknown, science=false), Run357 at cb7e0f9e823cc47b4c432d6d78b6af724b1966a4. Recovered genuine historical TripoSR Actions artifact 14733006902. Actual source GLB SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117 matches Run357. Viewed actual six-axis prior renders. No new neural inference. Prior SF3D and Hunyuan mini-turbo branches inspected: Run166 render incomplete, Run233 report pending, neither is evidence of new successful inference. Rechecked official https://github.com/Stability-AI/stable-point-aware-3d: CPU supported, but model weights gated and require Hugging Face login/access. Local DNS requests for github.com, huggingface.co and pypi.org all returned temporary name resolution failure. No Blender/bpy installed. VTK EGL works. No paid job, no access-control bypass.

## Actual experiment
Test whether excessive flatness of the profile, independently of baked vertex colour, is correctable using smoothly varying section-wise dorsal volume rather than more fur or colour projection. Extract largest connected real neural mesh, orient glTF Y-up, front +Z, calculate 5/50/95 percentiles for 39 overlapping horizontal slices, smooth lateral and depth midpoints (Gaussian sigma=2), taper the correction near feet and crown. Preserve face-side depth, adjust rear half by 20% or 40% relative to slice midpoint, and shift lateral center by 80% of smoothed estimated offset. These are design hypotheses, not measured owl anatomy. Export neutral cream diagnostic GLBs with explicit normals, reimport using trimesh, render at 0/45/90/180 degrees with actual VTK EGL Phong lighting. Core executed algorithm:
```python
m=trimesh.load(source,force='mesh')
m=max(m.split(only_watertight=False),key=lambda x:len(x.faces))
v=m.vertices[:,[1,2,0]].copy()
yf=(v[:,1]-v[:,1].min())/np.ptp(v[:,1])
ts=np.linspace(.025,.975,39)
q=np.array([np.percentile(v[np.abs(yf-t)<.035],[5,50,95],axis=0) for t in ts])
cx=gaussian_filter1d((q[:,0,0]+q[:,2,0])/2,2)
cz=gaussian_filter1d((q[:,0,2]+q[:,2,2])/2,2)
interp=lambda a:np.interp(yf,ts,a)
smooth=lambda x:np.clip(x,0,1)**2*(3-2*np.clip(x,0,1))
gate=smooth((yf-.08)/.15)*smooth((1-yf)/.08)
w=v.copy()
w[:,0]-=interp(cx)*gate*.8
back=np.minimum(v[:,2]-interp(cz),0)
w[:,2]+=back*strength*gate # strength=.20 or .40
```

## Actual results
All three native GLBs reimported, watertight, 50,205 vertices/100,534 triangles each. Baseline 2,613,444 bytes; other two 2,613,440 bytes each. Twelve actual 420x420 render frames and 1680x1260 full sheet produced, visually inspected. Volume baseline 0.207276, moderate 0.225172, strong 0.243069 (unitless model coordinates; +8.6%, +17.3%). Depth/width ratios at relative height 0.2,0.4,0.6,0.8:
- Baseline: .640/.686/.749/.806
- Moderate: .696/.754/.825/.886
- Strong: .756/.823/.901/.964
GLB SHA256:
- baseline_CLAY_NO_RELEASE.glb: 662ab98b5c5d72371c2f29f47b7e20ba64c5afd14275262aeddcbb1b124f82d7
- moderate_CLAY_NO_RELEASE.glb: 3d7b6cd318e68fbbfc36d452141c5c7d3fcab0b5371619aab2fd24a8af8f4acb
- strong_CLAY_NO_RELEASE.glb: addc42de0aefc6d759a525cd4e7298a5a2a036991404079b4ca41146305175ca
- executed section_test.py: eb126f0cdc1bd8a814a7fc414ef70b02a06a53d67eb848d47be9496498a1568e
- metrics.json: 01e7ed574311cffdafed74cf00a42e533f3323d9f69ef1f4efe661a0df2b4c5d
- full comparison.jpg: 631126339104d0162ecc3d7b4d46ce1b86e60a237c646744df9121f887ca0154
- compact actual render evidence tiny.jpg 120x90 2,361 bytes SHA256 7c7739098637c78e6b01ca56f895056417586e2c6636dd59e8a88ae99be4d931; see separate base64 evidence. Rows baseline, moderate, strong; columns 0/45/90/180 degrees. Full artifacts local current run only, not guaranteed persistent.

## Visual gate
The neutral clay test reveals that many of the lumpy pebble shapes are actual geometry, not merely colour or texture. Side volume increases as intended but stronger inflation makes the rump excessively bulbous. The eye cavities, heavy beak, indistinct feet and scalloped body/back persist even when the baked material is removed. No art pass; the neutral clay is deliberately diagnostic and not a feather material or deliverable. No new browser or physical phone acceptance. Future effort should switch away from repeated edits of this base, ideally new source-bound geometry or coherent multiview reconstruction. No additional spend. No modifications to main, 251-species pipeline, concept art, prototype or deployment.