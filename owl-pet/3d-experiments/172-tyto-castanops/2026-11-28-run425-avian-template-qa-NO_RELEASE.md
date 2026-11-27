# Run425 — actual avian template retrieval and multi-axis visual gate — NO_RELEASE

2026-11-28 Asia/Shanghai. Re-read main owl-pet AGENTS, README, STATUS (207/251) and Run424 at ad6bbb0bbbf4ebd5ba6695266b02cf178bdc69f9. Recovered and visually inspected original #172 v3 PNG from main (737545 bytes, blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b). Right juvenile: cream fluffy down, broad heart facial disc, dark eyes, compact body, feathered feet. Do not substitute the later concept versions.

## New actual asset route

Local DNS for github.com, raw.githubusercontent.com and huggingface.co still failed; Blender not installed; torch/trimesh/VTK available. Unlike the previous large binary acquisition failures, the GitHub connector successfully retrieved three complete small binary PLY assets directly from the authors' AVES CVPR 2021 repository, https://github.com/yufu-wang/aves/tree/master/bird_meshes (Wang et al., Birds of a Feather). This is an actual public research mesh route, not inference or a mere search result. The published species list has 17 species, no owl. Tested puffin (rounder head), waxwing (compact bird) and generic template. Code repository MIT license; no assumption of independent commercial mesh rights beyond verified scope, no third-party mesh redistributed.

Parsed every byte of each 327044-byte binary little-endian PLY: 8210 xyz float32 vertices, 14268 triangle faces, each with 3 indices and RGB face color. Zero out-of-range face indices; one unique face color per asset. Nine actual orthographic z-buffer triangle rasterizations (XY, ZY, XZ; rows puffin, waxwing, template) were generated and visually reviewed. They show narrow, adult-like elongated bodies, pointed beaks, bare long feet, tail and no owl heart disc, no down or eyes. The views are consistent with their geometry but are unsuitable for this specific juvenile; transferring them would need major anatomical resculpting and new feather system, not simple texture transfer.

| Asset | Source blob | xyz span (source units, approximate) |
|---|---|---|
| 106.Horned_Puffin.ply | e85fa44cd78b73091007c97833c9f92ca8022daf | 6.1905, 18.4930, 11.0443 |
| 186.Cedar_Waxwing.ply | 2798898e771c7aa47e0f493b7c8a28805e996ce9 | 6.3741, 20.0261, 11.1676 |
| template.ply | 1d1bc5e49af0eecaf0bbc7f28a4cd63c67aa618e | 6.8961, 20.0575, 10.8511 |

Also checked an alternate ASCII OBJ acquisition path: https://github.com/Mcamento8/omnimod-3d-library, recursive tree 18441 entries, not truncated. Exact owl/bird/chick filename matching found only Kenney cube-pets/animal-chick.obj; actually fetched and parsed 33411 bytes, 288 vertices, 490 triangles, zero invalid indices; explicitly cube-pet style, wrong species. No role as character candidate. https://github.com/3dloom/3dloom-sample-models tree lists dragon, helmet, mushroom and speaker only, no avian asset.

## Reproduction (same PLY parsing and orthographic depth test)

Save the three source PLY files locally from the cited source and verify Git blob hashes. Python equivalent of the executed JS raster test below. Render colors are neutral clay for geometry inspection only, not an asset material. No new character mesh produced.

```python
import hashlib, struct, pathlib
import numpy as np
from PIL import Image
names=['106.Horned_Puffin.ply','186.Cedar_Waxwing.ply','template.ply']
tile=208
canvas=np.full((tile*3,tile*3,3),246,np.uint8)
for row,name in enumerate(names):
    raw=pathlib.Path(name).read_bytes()
    offset=raw.index(b'end_header\n')+11
    v=np.frombuffer(raw,dtype='<f4',count=8210*3,offset=offset).reshape(-1,3)
    offset+=len(v)*12
    fmt=struct.Struct('<BiiiBBB')
    faces=[]
    colors=set()
    for _ in range(14268):
        n,a,b,c,r,g,bl=fmt.unpack_from(raw,offset)
        offset+=fmt.size
        assert n==3 and min(a,b,c)>=0 and max(a,b,c)<len(v)
        faces.append((a,b,c))
        colors.add((r,g,bl))
    assert offset==len(raw)==327044
    print(name,hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest(),len(v),len(faces),v.min(0),v.max(0),len(colors))
    center=(v.min(0)+v.max(0))/2
    scale=175/np.ptp(v,axis=0).max()
    for col,axes in enumerate(((0,1,2),(2,1,0),(0,2,1))):
        p=v[:,axes].copy()
        p[:,0]=tile/2+(p[:,0]-center[axes[0]])*scale
        p[:,1]=tile/2-(p[:,1]-center[axes[1]])*scale
        depth=np.full((tile,tile),-np.inf)
        img=canvas[row*tile:(row+1)*tile,col*tile:(col+1)*tile]
        for inds in faces:
            a,b,c=p[list(inds)]
            den=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
            if abs(den)<1e-7: continue
            normal=np.cross(b-a,c-a)
            shade=.48+.52*abs(np.dot(normal,[-.35,-.45,.82])/(np.linalg.norm(normal) or 1))
            lo=np.maximum(0,np.floor(np.min([a[:2],b[:2],c[:2]],axis=0)).astype(int))
            hi=np.minimum(tile-1,np.ceil(np.max([a[:2],b[:2],c[:2]],axis=0)).astype(int))
            for y in range(lo[1],hi[1]+1):
                for x in range(lo[0],hi[0]+1):
                    s=((b[1]-c[1])*(x+.5-c[0])+(c[0]-b[0])*(y+.5-c[1]))/den
                    t=((c[1]-a[1])*(x+.5-c[0])+(a[0]-c[0])*(y+.5-c[1]))/den
                    q=1-s-t
                    if min(s,t,q)<0: continue
                    z=s*a[2]+t*b[2]+q*c[2]
                    if z>depth[y,x]:
                        depth[y,x]=z
                        img[y,x]=np.rint(np.array([205,185,157])*shade)
Image.fromarray(canvas).save('run425_source_mesh_qa.png')
```

Decision: ART_REJECTED / NO_RELEASE. Actual geometry access route improved but no suitable owl base; prioritize freely licensed owl-specific geometry accessible as text or small binary, or actual new reconstruction. Do not count generic bird models or prior rejected sculpture as release. No paid invocation, no mobile WebGL pass, no main edits, no production manifest edits, no original concept edits, no deployment changes.
