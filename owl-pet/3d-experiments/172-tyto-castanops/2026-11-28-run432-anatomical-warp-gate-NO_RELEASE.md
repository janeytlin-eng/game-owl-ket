# Run432 — continuous anatomical warp gate — ART_REJECTED / NO_RELEASE

2026-11-28. Re-read main owl-pet AGENTS (b9ebde6dc406354b77d4297089a6f8f928f3b878), README and STATUS (207/251), species/172-tyto-castanops-v3.md (5c754f9daf8433ba608107e389659b0271b1480a), actual original 1536x1024 v3 PNG blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b (decoded and visually viewed), and prior Run431 commit d60442d7b49d0bac730194243b0b44145ab6d9c1. Target remains rightmost age-unknown cream mesoptile: compact supported feet, wide warm-rimmed heart mask, dark eyes, dense down, short buried wings and concealed tail. No later concept substituted.

## Actual experiment: can continuous deformation salvage a Tyto-shaped base?

Retrieved the same historical BarnOwl.obj used in Run427 from alvarocasadoc/3December master assets/models/21/BarnOwl.obj, exact blob 15514c8f1b07452af832ba005b5a7743710b0e39. This is not a new source. Unlike earlier subdivision/rotation, tested a continuous, height-dependent anatomical warp of actual native triangle vertices: compress lower body, widen torso and upper head, reduce rear depth near tail. No primitive assembly, no SVG, no independent side/back reconstruction claimed. Source is unlicensed/rights unclear and was used only for internal diagnostic; no original or modified mesh or derivative render redistributed. Mesh extent in source units measured before and after. Actual CPU depth-buffered flat-normal render at 0/90/180/270 degrees, 140x140 each, fixed largest-extent normalization per model; both rows visually inspected.

```json
[
 {"row":"original","vertices":879,"triangles":1682,"extent":[4.97694,10.404284,7.195617],"widthHeight":0.4783548776638546,"coverage":[5448,5094,5448,5094],"nonfinite":0,"degenerate":0},
 {"row":"warp","vertices":879,"triangles":1682,"extent":[6.64900241365521,8.6,5.709904516245087],"widthHeight":0.7731398155413035,"coverage":[9164,5594,9164,5594],"nonfinite":0,"degenerate":0}
]
```

Visual result: frontal silhouette significantly rounder, head wider, but side profile still markedly adult/slanted with a long visible rear wing/tail taper, small unsupported-looking legs in side view, inadequate face anatomy (no readable eyes in geometry-only diagnostic), no actual down surface. Front width/height improvement is not sufficient to pass. Changing the original mesh's silhouette cannot create missing juvenile structures. Do not repeat simple scaling/subdivision as a solution. No texture or PBR or mobile runtime tested.

## Reproduce exact deformation and geometry diagnostic

Load the independently obtained original OBJ only if permitted; do not redistribute. The Python code below is equivalent to the executed JS mesh warp and z-buffer diagnostic. Four images per row, original above, warp below.

```python
import numpy as np
from PIL import Image
from pathlib import Path
V,F=[],[]
for line in Path('BarnOwl.obj').read_text().splitlines():
    a=line.split()
    if not a: continue
    if a[0]=='v': V.append([float(x) for x in a[1:4]])
    if a[0]=='f':
        p=[int(s.split('/')[0])-1 for s in a[1:]]
        F.extend([p[0],p[i],p[i+1]] for i in range(1,len(p)-1))
V=np.array(V); F=np.array(F)
assert np.isfinite(V).all() and F.min()>=0 and F.max()<len(V)
u=(V[:,1]+1.56326)/10.404284
W=V.copy()
W[:,1]=8.6*np.interp(u,[0,.15,.3,.65,1],[0,.09,.22,.58,1])
W[:,0]*=np.interp(u,[0,.15,.3,.65,.8,1],[.8,.9,1.30,1.4,1.78,1.78])
W[:,2]=(W[:,2]-.5)*np.interp(u,[0,.15,.3,.65,1],[.45,.6,.84,1,.9])+.5
N=140
im=np.full((N*2,N*4,3),238,np.uint8)
for row,X in enumerate([V,W]):
    C=(X.min(0)+X.max(0))/2; Q=X-C
    S=(N-16)/np.ptp(X,axis=0).max()
    for k in range(4):
        t=k*np.pi/2; c,s=np.cos(t),np.sin(t)
        P=np.column_stack([N/2+S*(Q[:,0]*c-Q[:,2]*s),N/2-S*Q[:,1],Q[:,0]*s+Q[:,2]*c])
        depth=np.full((N,N),-np.inf)
        for f in F:
            a,b,d=P[f]
            den=(b[1]-d[1])*(a[0]-d[0])+(d[0]-b[0])*(a[1]-d[1])
            if abs(den)<1e-8: continue
            n=np.cross(b-a,d-a); nn=np.linalg.norm(n)
            if nn<1e-8: continue
            shade=round(218*(.4+.6*abs(n@np.array([-.35,-.5,.79])/nn)))
            lo=np.maximum(0,np.floor(P[f,:2].min(0)).astype(int))
            hi=np.minimum(N-1,np.ceil(P[f,:2].max(0)).astype(int))
            for y in range(lo[1],hi[1]+1):
                for x in range(lo[0],hi[0]+1):
                    u=((b[1]-d[1])*(x+.5-d[0])+(d[0]-b[0])*(y+.5-d[1]))/den
                    v=((d[1]-a[1])*(x+.5-d[0])+(a[0]-d[0])*(y+.5-d[1]))/den
                    w=1-u-v
                    if min(u,v,w)<0: continue
                    z=u*a[2]+v*b[2]+w*d[2]
                    if z<=depth[y,x]: continue
                    depth[y,x]=z
                    im[row*N+y,k*N+x]=[shade,round(shade*.95),round(shade*.88)]
        print(row,k,np.isfinite(depth).sum())
Image.fromarray(im).save('local_only_warp_diagnostic.png')
```

## Fresh source/access checks

- GitHub code search filename:barn_owl.obj and filename:tyto.obj returned 0; owl.off returned 216 mostly bowl false positives; owl.ply returned 46 including the previous SeriousShooter source, not a new juvenile-specific model.
- https://github.com/moizahmad418/3d-owl-character-configurator actual repository directory inspection revealed three GLBs (aline_model 10148416 bytes, umber_model 12666404, umber_model_alternate 11637484). Metadata only, no candidate bytes or license verified; no adoption.
- https://www.innerscene.com/tools/library/3d-parts/owl-d696472a lists CC0 original 19.7 MB GLB added 2026-10-21. Actual download link https://www.innerscene.com/api/library/owl-d696472a/download followed; retrieval rejected application/octet-stream, no bytes. No claim of anatomy or usability.
- https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc museum CC0 specimen, page lists 262k triangles. Museum source https://muzea.malopolska.pl/en/objects-list/2394 returned no readable lines. No mesh bytes, no age verified. Skull scan is not an external juvenile base.
- Local runtime: trimesh, VTK, Torch, skimage, cv2, scipy, playwright present; Blender/bpy, pymeshlab, open3d absent. DNS resolution for github.com, huggingface.co, api.sketchfab.com, www.thingiverse.com failed with temporary error -3; local cache only fontconfig. No paid inference or download.

Decision: ART_REJECTED / NO_RELEASE. No qualified sample, no phone WebGL test. Continue with license-clear native juvenile reconstruction/base; avoid further cheap adult mesh re-proportioning. Zero extra spend. No main, 251-species production, original concept or deployment changes.
