# Run368 — reference silhouette registration (ART_REJECTED / NO_RELEASE)
2026-11-25. Extra spend $0. Independent research branch only.

## Source and preflight
Read main AGENTS, README, STATUS, #172 v3 review and Run367 (994739d59210fbffe25c9d0ea4b78a17890f36b3). Main snapshot e12a33c67fe2c4630d96f03fa68da2a1f39dd59e; current production STATUS 206/251 unique, 17:29 update. No modification to production workflow. Recovered actual artifact 14795923598 via GitHub connector, exact source GLB SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be. Viewed isolated reference and historical browser views; note historical file named model1_front.png shows rear and model1_back.png shows face. This naming discrepancy is not a newly executed WebGL test. Actual face is negative Z. V3 calls for cream thick mesoptile, developed mask, buried short wings, concealed tail; science=false, age unknown.

## Actual experiment
CPU Python, OpenCV, SciPy, Trimesh and VTK. Test whether matching the *observed* reference front silhouette is sufficient to improve the same neural base, not a new generative reconstruction. Reference alpha from young-REAL-PHOTO-PIXELS-transparent-input-NO_3D.png >=128, tight crop then height normalization to 360 px, preserving reference aspect ratio. Orthographic rasterized projected mesh triangles on 512x512 canvas, same height and vertical alignment, front camera negative Z, image x=-world x. Per-row width and centroid differences estimated and regularized with Gaussian sigma 10 pixels; ratio clamped .75–1.25 and centroid shift ±25 px. Smooth deformation only X, preserving existing UV, material and 27,372 faces; protect head in bodyfit vs 85% fullfit. Two genuine native GLBs exported and reimported. 12 actual textured VTK 360x360 renders plus 3 mask overlays, viewed together. Offline color-texture lighting is not full PBR/browser rendering.

| variant | front mask IoU | projected area px | triangles | GLB bytes | max vertex displacement |
|---|---:|---:|---:|---:|---:|
| baseline | .878350 | 76027 | 27372 | 1137108 | 0 |
| bodyfit | .952901 | 69581 | 27372 | 2556924 | .0702403 |
| fullfit | .960315 | 69262 | 27372 | 2556924 | .0597046 |

Reference area 66876 px; scores are fitting metrics on the same single-view input, not independent validation or evidence of correct rear shape. IoU improves 7.46 and 8.20 percentage points respectively. Both narrower body profiles are closer to the input silhouette but face remains mask-like in side view, toes are flattened/fused with support, rear has banding and no convincing buried wing morphology, down remains largely flat texture. Fullfit also deforms head width. All variants rejected. Do not prioritize optimizing front IoU alone.

Core executed method (v, f from source, H=360, S=512, top=76; reference target as described):
```python
height=np.ptp(v[:,1]); ymin=v[:,1].min(); ymax=v[:,1].max()
def project(v):
    p=np.c_[S/2-v[:,0]*H/height,top+(ymax-v[:,1])*H/height]
    out=np.zeros((S,S),np.uint8)
    for face in f: cv2.fillConvexPoly(out,np.rint(p[face]).astype(np.int32),1)
    return out
# br,tr: row-wise first and last nonzero pixel for baseline and target
ids=np.where(np.isfinite(br[:,0])&np.isfinite(tr[:,0]))[0]
width=(tr[ids,1]-tr[ids,0]+1)/(br[ids,1]-br[ids,0]+1)
delta=tr[ids].mean(1)-br[ids].mean(1)
width=gaussian_filter1d(np.interp(np.arange(S),ids,np.clip(width,.75,1.25)),10)
delta=gaussian_filter1d(np.interp(np.arange(S),ids,np.clip(delta,-25,25)),10)
for name,strength,protect in [('bodyfit',1.,True),('fullfit',.85,False)]:
    nv=v.copy(); row=top+(ymax-v[:,1])*H/height
    fac=np.interp(row,np.arange(S),width); shift=np.interp(row,np.arange(S),delta)
    t=(v[:,1]-ymin)/height
    weight=np.minimum(1,np.minimum(t/.1,(1-t)/.08)).clip(0,1)*strength
    if protect: weight*=1-.85*np.exp(-((t-.75)/.16)**2)
    nv[:,0]=v[:,0]*(1+weight*(fac-1))-weight*shift*height/H
    out=m.copy(); out.vertices=nv; out.export(name+'.glb')
    rt=trimesh.load(name+'.glb',force='mesh',process=False)
    a=project(rt.vertices); iou=(a&target).sum()/(a|target).sum()
```
GLB SHA256 bodyfit 036a64d6eb705fcaadfd12653f21bbb0c0087448399b9e0ceb29bdee1fcb362c; fullfit 0a2248e1238cb2f3b9acdce313ae1dae074b46c3c307874e29f233c1c6bb3811.
Executed fit.py SHA256 e818a1c3a5ccda1133f883765b20301443b1930988d3d77db1f08ba3930947cf. Full contact SHA256 c9f5ce42067b0b726b69b98d93a340f90e3d141c78848b59aee82eb939d92ee2. Full files local to run, not represented as durable remote assets. Tiny evidence thumbnail below (150x98, rows baseline/bodyfit/fullfit, columns front/threequarter/side/rear/mask overlay, green overlap, red mesh-only, blue target-only). Thumbnail SHA256 45f29b8b41f8460c82884e5b7efde9820410339d0364220402c144ed3f39aae0.

## Alternative sources and limitations
Web search 2026-11-25: https://grab3d.com/models/animals/owl/ is advertised CC0 but great horned owl adult with yellow eyes and ear tufts, 400k–800k triangles, unsuitable as ready juvenile base. https://sketchfab.com/3d-models/barn-owltyto-alba-af3cdd38e029430d9c131370ebf1bb33 CC BY 760 triangles, not sufficient evidence of high-quality juvenile anatomy. Previously identified https://vinish.dev/free-3d-models/birds advertises a rigged barn owl under CC BY 4.0, not newly acquired. No additional external model downloaded; local curl api.github.com DNS failure code 6 persists; CUDA false, Blender unavailable. No paid invocation. No new mobile WebGL test. Prioritize a different credible base or genuinely consistent multi-view reference, not another front-only deformation. No changes to main, original concepts, deployed prototype or 251-species pipeline.
