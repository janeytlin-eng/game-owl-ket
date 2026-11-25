# Run369 — bilateral mesh correspondence, ART_REJECTED / NO_RELEASE

2026-11-25. Extra spend $0. Independent research branch, forked from verified Run368 commit 7027ebe1b580a86ba7dc79d19136060f884a6c22.

## Preflight and source
Read main owl-pet AGENTS, README, STATUS (17:29, 206/251 unique), and 172-tyto-castanops-v3-review (science=false, age unknown, thick cream mesoptile, developed mask, short wings buried under down, concealed tail). Read Run368 actual record; front silhouette fitting alone failed. Recovered actual artifact 14795923598, verified source GLB SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be; viewed historical front and side renders. Actual face negative Z.

## Actual bilateral correspondence experiment
Hypothesis: asymmetric neural shape contributes to uneven shoulder outline; use reflected 3D nearest-neighbor correspondence, not front-only silhouette fitting. CPU NumPy, SciPy, Trimesh, VTK. Weld only for displacement calculation using rounded unique positions (13,688); original 16,971 UV vertices / 27,372 triangles kept. Robust 8-neighbor reflection, confidence weighting, 24-neighbor displacement smoothing and upper-front face/foot protective weighting; move X only. Two native GLB exports reimported successfully. Viewed 12 actual VTK renders (per-vertex texture samples with diffuse lighting; not full PBR).

| variant | reflected nearest mean | p95 | maximum X displacement | bytes |
|---|---:|---:|---:|---:|
| baseline | .0166290 | .0564282 | 0 | 1137108 |
| soft | .0152081 | .0537940 | .0088644 | 2556928 |
| strong | .0136810 | .0511835 | .0199450 | 2556928 |

The mean reflected nearest-neighbor distance decreased about 8.5% and 17.7%, respectively; these are internal geometric metrics, not independent evidence of anatomical correctness. Frontal lateral silhouette became slightly more even, but side mask protrusion, rear lack of buried wing structure, flat down and fused toes remain. Both rejected; no new foundation mesh. Symmetry alone is not a sufficient path to visual quality.

Core executed code (v = source vertices; original m and UV retained):
```python
u,inv=np.unique(np.round(v,6),axis=0,return_inverse=True)
center=(np.percentile(u[:,0],1)+np.percentile(u[:,0],99))/2
r=u.copy();r[:,0]=2*center-r[:,0]
tree=cKDTree(u);d,i=tree.query(r,k=8)
w=np.exp(-(d/.025)**2);w/=np.maximum(w.sum(1,keepdims=True),1e-12)
partner=(u[i]*w[:,:,None]).sum(1)
raw=(2*center-partner[:,0]-u[:,0])/2
conf=np.exp(-(d[:,0]/.065)**2)
nd,ni=tree.query(u,k=24);nw=np.exp(-(nd/.045)**2);nw/=nw.sum(1,keepdims=True)
raw=(raw[ni]*nw).sum(1)
y=(u[:,1]-u[:,1].min())/np.ptp(u[:,1]);z=u[:,2]
mask=np.clip((y-.10)/.14,0,1)*np.clip((.99-y)/.12,0,1)
mask*=1-.95*np.exp(-((y-.72)/.23)**2)*np.clip((-z-.03)/.17,0,1)
mask*=conf
for name,strength in [('soft',.6),('strong',1.35)]:
    uu=u.copy();uu[:,0]+=strength*mask*raw
    out=m.copy();out.vertices=v+(uu-u)[inv];out.export(name+'.glb')
    rt=trimesh.load(name+'.glb',force='mesh',process=False)
```

SHA256:
- soft.glb 2dd235a52f0e04cf30ffabe32ff3c2abba0bbe28b93841b663b3a4d08405ee52
- strong.glb f26bdbfeee96c525371bb83c2027f462ef5f54a6a5de97f02fadec0300aca4bc
- executed symmetry.py 32d77757c55ab6e95165d2c1a720e74a0e4276200740dab4c6a8db666171fdce
- full 1200x930 contact sheet 7c150f3e425c8693313c5688cde4435a603923bc959645120c9016657d59243d
- tiny evidence JPEG (96x74, rows baseline/soft/strong; columns front/45/side/rear) SHA256 a5ae1d5f39e03b82701f91bec80fcf030724cd8eca28c6219e8b08805019575f, 1658 bytes, in adjacent .jpg.b64. Decode with base64 -d. This evidence thumbnail is not adequate for art acceptance. Full models and full contact sheet are local to this run only, not claimed as durable assets.

## New foundation asset search and actual transport tests
- https://www.innerscene.com/tools/library/3d-parts/owl-d696472a advertises original CC0 owl, 19.7 MB GLB. Direct endpoint https://www.innerscene.com/api/library/owl-d696472a/download: web fetch rejected octet-stream, container download failed, curl DNS code 6. No model bytes recovered or morphology verified.
- GitHub connector search found Inefy/project-rat/assets/models/barn_owl.glb at e7625a2fc481a45c9d5710edd3523de6518ede43; actual base64 content returned (597650 characters including line breaks, GLB header, blob 229d702ce56206dbe5357d0a58642ef820719a27). Repo MIT LICENSE and README read. README explicitly identifies a cartoon boss in flat-paint/human-feature style, incompatible with this naturalistic juvenile brief. Not imported or reused. This confirms connector retrieval can work for public GitHub assets, unlike direct DNS downloads; seek anatomically credible openly licensed models via this route, verify individual asset licenses.
- No Blender; torch CUDA false. No paid invocations.

## WebGL gate
Chromium + Playwright actually launched with 390x780 mobile emulation; attempted WebGL2 context with ANGLE SwiftShader, EGL and swiftshader-webgl, all returned null, creation error BindToCurrentSequence failed. No browser render or real-device acceptance. GLB reimport is not WebGL acceptance.

No changes to main, original concepts, deployed prototype or 251-species production. Do not release or notify. Further work should prioritize credible alternate base via connector or genuinely consistent multiple views instead of another local geometry metric optimization.
