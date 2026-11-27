# Run426 — owl-specific source mesh retrieval and visual gate — NO_RELEASE

2026-11-28. Re-read main owl-pet AGENTS, README, STATUS (207/251), and Run425 at 673f0c55cd1dcc350b2fe6ebc059363fcdb35b2f. Main observed at a55ee9957b06c87485447869a8ce36d104f15e13. Retrieved and visually inspected the exact original v3 PNG, blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b. The right juvenile has a broad tan-edged heart-shaped facial disc, deep dark eyes, short pale bill, round cream-white down envelope and feathered tarsi. No substitution with later versions.

## Actual new source geometry

GitHub code search filename:owl.ply yielded mrbid/SeriousShooter. Retrieved full ASCII PLY meshes (not pointer files) and parsed all vertices and triangles. Both have vertex RGB, normals and alpha. Source: https://github.com/mrbid/SeriousShooter/tree/main/assets/ply ; repository MIT license read, but original third-party asset provenance not established, so no source asset redistribution.

| Level | Git blob | ASCII bytes | Vertices | Triangles | Distinct vertex RGB |
|---|---|---:|---:|---:|---:|
| low | d9465f2f0a5f1c3343dbca4dd22f31b1c4167295 | 72827 | 676 | 1347 | 672 |
| medium | 660c8b0fefbc05e27d1bbe62409d41a61fc41cb0 | 848847 | 7494 | 14983 | 7045 |

All faces triangular, no invalid indices. Medium bounds [-0.604636,-0.6038962,-0.012036985] to [0.60505235,0.60636353,1.710051]. Six actual orthographic triangle z-buffer renders with interpolated vertex colors were generated and visually inspected, low and medium each back/side/front. Medium clearly shows pointed ear tufts, two circular yellow/orange eye rims, dark mottled brown adult plumage, folded wings, orange bare legs and short pointed bill. These persist through views and resolution. Not Tyto, not juvenile, not cream-white down. Higher resolution of same source does not address anatomy. Reject as direct base, not a release.

## Alternative direct retrieval attempts

GitHub fetch_file returned actual LFS pointers only (not model bytes) for these candidates:
- series-ai/jam-ready-assets/codepawl-pixel-art-atlas-models/3D/misc/models/barn_owl.glb, pointer blob 31943d2beccdf98550a505f1b150d032682c48e2, declared size 19532, object SHA256 e573d06c63008794d8bf68158c059e2624de8902fb44e444dbf320dcf3f0e297.
- Bicyclette/Maze-Engine/assets/owl/owl.glb, pointer 5e95c70905802ccb36d52fcebce6677a72288a07, declared 10802428 bytes.
- bgrut/fantasy-studio/backend/assets/library/owl.glb, pointer e95c6081c7008f6b39fdbe18f8114c2cb58333ec, declared 6555032 bytes.
Current local DNS tests for github.com, media.githubusercontent.com and huggingface.co all returned gaierror -3 Temporary failure in name resolution. Blender absent; trimesh, VTK and torch present. No claim that these LFS meshes were opened. Public search also found https://www.embossify.com/models/owl (simple-math stylized owl with tufts, not appropriate) and https://grab3d.com/models/animals/owl/ (adult great horned owl, not appropriate). No payment or paid API invocation.

## Reproducible raster inspection (Python equivalent of executed JS)

Use the two source PLYs in local files low.ply and med.ply. This produces the same 2x3 orthographic vertex-color inspection layout. It is mesh QA, not a character sample.

```python
import numpy as np
from PIL import Image
from pathlib import Path
N=180
out=np.full((N*2,N*3,3),240,dtype=np.uint8)
for row,level in enumerate(('low','med')):
    h,d=Path(level+'.ply').read_text().split('end_header\n',1)
    nv=int(next(l.split()[-1] for l in h.splitlines() if l.startswith('element vertex ')))
    nf=int(next(l.split()[-1] for l in h.splitlines() if l.startswith('element face ')))
    lines=d.strip().splitlines()
    v=np.array([list(map(float,l.split())) for l in lines[:nv]])
    f=np.array([list(map(int,l.split())) for l in lines[nv:]])
    assert f.shape==(nf,4) and (f[:,0]==3).all()
    assert f[:,1:].min()>=0 and f[:,1:].max()<nv
    xyz=v[:,:3]; center=(xyz.min(0)+xyz.max(0))/2
    scale=155/np.ptp(xyz,axis=0).max()
    for col,(axes,sign) in enumerate([((0,2,1),1),((1,2,0),1),((0,2,1),-1)]):
        x,y,z=axes
        p=np.column_stack((N/2+sign*(xyz[:,x]-center[x])*scale,N/2-(xyz[:,y]-center[y])*scale,sign*xyz[:,z],v[:,6:9]))
        zb=np.full((N,N),-np.inf)
        for ids in f[:,1:]:
            A,B,C=p[ids]
            den=(B[1]-C[1])*(A[0]-C[0])+(C[0]-B[0])*(A[1]-C[1])
            if abs(den)<1e-9: continue
            lo=np.maximum(0,np.floor(np.min([A[:2],B[:2],C[:2]],axis=0)).astype(int))
            hi=np.minimum(N-1,np.ceil(np.max([A[:2],B[:2],C[:2]],axis=0)).astype(int))
            for yy in range(lo[1],hi[1]+1):
                for xx in range(lo[0],hi[0]+1):
                    u=((B[1]-C[1])*(xx+.5-C[0])+(C[0]-B[0])*(yy+.5-C[1]))/den
                    t=((C[1]-A[1])*(xx+.5-C[0])+(A[0]-C[0])*(yy+.5-C[1]))/den
                    w=1-u-t
                    if min(u,t,w)<0: continue
                    Z=u*A[2]+t*B[2]+w*C[2]
                    if Z<=zb[yy,xx]: continue
                    zb[yy,xx]=Z
                    out[row*N+yy,col*N+xx]=np.rint(u*A[3:]+t*B[3:]+w*C[3:])
Image.fromarray(out).save('run426_owl_source_qa.png')
```

Decision: ART_REJECTED / NO_RELEASE. Actual owl-specific geometry acquisition succeeded, but art quality/species/age fail. No mobile WebGL pass. Future source gate must specifically target Tyto facial disc and juvenile body; do not spend more runs optimizing the wrong species. No main, original concept, production or deployment writes. No new character mesh represented as a finished sample.
