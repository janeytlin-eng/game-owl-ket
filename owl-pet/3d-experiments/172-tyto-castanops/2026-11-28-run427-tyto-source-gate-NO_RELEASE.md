# Run427 — Tyto-specific source gate — NO_RELEASE

2026-11-28. Read main owl-pet AGENTS, README and STATUS (207/251; main SHA 8cb4cd3b078465733db1a4a3eda0eeda2973e998) and Run426 commit 9982a9de94b3b6c985a9358ea9cf635d26ba49dc. Fetched exact original #172 v3 PNG (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b) as base64 and visually inspected it. Right bird: rounded cream down, tan-edged wide heart disc, dark eyes, pale small bill, stout body and feathered tarsi. No later version substituted.

## Actual source mesh and visual rejection

GitHub filename:barnowl.obj search returned alvarocasadoc/3December/assets/models/21/BarnOwl.obj. Retrieved full 204533-character OBJ (blob 15514c8f1b07452af832ba005b5a7743710b0e39); parsed 879 vertices, 1144 UV entries, 3454 normals, 796 quads and 1682 triangles after fan triangulation, all position indices valid. Bounds [-2.48847,-1.56326,-3.69011] to [2.48847,8.841024,3.505507]. Four actual orthographic depth-buffered triangle renders at 0/90/180/270 degrees were produced and visually inspected. The mesh does have a Tyto-like facial outline with no ear tufts, but the adult upright proportions, small head, long tapered tail and distinct folded flight feathers are inconsistent with the target downy juvenile. Width/height 0.478, not a direct juvenile base. Surface lacks fine feather geometry. Untextured render only: MTL retrieved and references BarnOwl_BaseColor.png; texture blob 909d5e753ef10b32cd49799b31402fd2cecf2e9d (1786297 bytes per directory) not retrieved: fetch_file base64 returned empty content, fetch_blob UnicodeDecodeError, GitHub fetch rejected non-UTF8. Repository metadata reports license null and LICENSE/README.md fetches returned 404. No redistribution of source geometry or derived asset; no claim of license clearance. Source: https://github.com/alvarocasadoc/3December/tree/master/assets/models/21

## New free source lead

https://mint.gg/free-3d-models/barn-owl states CC0, adult barn owl model generated 2026-11-24, 19966 triangles, 1857216 bytes, four embedded textures and white stand. Direct GLB link actually followed: https://cdn.mint.gg/owned-artifacts/84b573359bed07b2dbee22e143ac9fd79a000e2ae4c10d7d88077a5f36902f53 . Web retrieval rejected model/gltf-binary; container download failed; Python requests returned DNS NameResolutionError (-3). No GLB bytes obtained or locally opened. Publisher's specifications not independently verified. Adult model would still require juvenile remodelling and stand removal. Additional low-poly CC BY lead https://sketchfab.com/3d-models/barn-owltyto-alba-af3cdd38e029430d9c131370ebf1bb33 (760 triangles listed) not opened; not a high-quality juvenile solution. No paid generation invoked.

## Reproduce geometry-only gate

Python equivalent of actual JS raster experiment; use locally obtained BarnOwl.obj. Real triangle surfaces, no constructed primitives, no UV texture used. Four views are inspection only.

```python
import numpy as np
from PIL import Image
from pathlib import Path
V,F=[],[]
for l in Path('BarnOwl.obj').read_text().splitlines():
    a=l.split()
    if not a: continue
    if a[0]=='v': V.append(list(map(float,a[1:])))
    if a[0]=='f':
        p=[int(x.split('/')[0])-1 for x in a[1:]]
        F.extend([p[0],p[i],p[i+1]] for i in range(1,len(p)-1))
V=np.array(V); F=np.array(F); assert F.min()>=0 and F.max()<len(V)
N=220; im=np.full((N,N*4,3),238,dtype=np.uint8)
C=(V.min(0)+V.max(0))/2; X=V-C; S=195/np.ptp(V,axis=0).max()
for k in range(4):
    t=k*np.pi/2; c,s=np.cos(t),np.sin(t)
    p=np.column_stack((N/2+S*(X[:,0]*c-X[:,2]*s),N/2-S*X[:,1],X[:,0]*s+X[:,2]*c))
    dep=np.full((N,N),-np.inf)
    for ids in F:
        a,b,d=p[ids]
        den=(b[1]-d[1])*(a[0]-d[0])+(d[0]-b[0])*(a[1]-d[1])
        if abs(den)<1e-8: continue
        n=np.cross(b-a,d-a); nn=np.linalg.norm(n)
        if nn<1e-8: continue
        shade=round(220*(.40+.60*abs(n@np.array([-.35,-.5,.79])/nn)))
        lo=np.maximum(0,np.floor(p[ids,:2].min(0)).astype(int))
        hi=np.minimum(N-1,np.ceil(p[ids,:2].max(0)).astype(int))
        for y in range(lo[1],hi[1]+1):
            for x in range(lo[0],hi[0]+1):
                u=((b[1]-d[1])*(x+.5-d[0])+(d[0]-b[0])*(y+.5-d[1]))/den
                v=((d[1]-a[1])*(x+.5-d[0])+(a[0]-d[0])*(y+.5-d[1]))/den
                w=1-u-v
                if min(u,v,w)<0: continue
                z=u*a[2]+v*b[2]+w*d[2]
                if z<=dep[y,x]: continue
                dep[y,x]=z; im[y,k*N+x]=[shade,round(shade*.95),round(shade*.88)]
Image.fromarray(im).save('run427_geometry_only.png')
```

Decision ART_REJECTED / NO_RELEASE. First directly retrieved named BarnOwl OBJ in this immediate sequence, but adult anatomy and unclear rights reject it. No actual qualifying character or phone WebGL test. No writes to main, production, original concept or deployment. Zero additional payment. Prioritize license-clear juvenile source geometry and real mesh generation, not repeated resolution upgrades or repackaging unsuitable adult assets.
