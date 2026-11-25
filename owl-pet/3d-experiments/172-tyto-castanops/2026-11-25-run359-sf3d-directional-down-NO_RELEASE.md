# Run359 — independent SF3D base recovery + directional down ablation — NO_RELEASE
2026-11-25 Asia/Shanghai. ART_REJECTED / NO_RELEASE. No paid external generation.

## Preflight and new base
Read main at 2152b8bc1a1b4c86daecead5073f68eaac5f3d4b: owl-pet AGENTS, README, STATUS (206/251, 45 remaining), #172 v3 actual review (cream mesoptile, short buried wing, age unknown, science=false), and Run358 at 0ed4873ef7932bcc40607d34de035ea06b3eb236. No change to main or species production. Instead of more TripoSR repairs, recovered genuine alternative Stable Fast 3D source from Run317 artifact 14795923598 (https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45127141518/artifacts/14795923598). Actual downloaded source 1,137,108 bytes SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be, matches prior record. Native 27,372 triangles, two embedded 1024x1024 texture maps, base color and normal, PBR. Viewed prior actual front and right browser frames; original front was -Z (old filenames reversed); rotated 180 degrees Y to +Z. Original Run317 record at 65b45c065d5f7a5b19143257ae6819d8342c06ec. Historical TripoSR artifact 14733006902 also recovered but not used for new meshes. No new neural inference. Local DNS lookup of github.com/huggingface.co/pypi.org yielded no address, no Blender/bpy, VTK EGL usable. Original asset licensing and product rights not cleared.

## Executed test
Preserve SF3D UV base mesh and both texture maps rather than transplanting TripoSR geometry. Sample 44,000 area-weighted surface points with RNG seed 359 and barycentric positions, normals and UV. Exclude lower 14%, facial disc region (front z>.10, relative height>.54 and |x|<.21) and dark texels (RGB mean<=100). Project mostly downward/rearward flow onto tangent plane and add random tangent deviations. Build 12,000 or 26,000 genuinely curved tapered narrow feather ribbons, three triangles per ribbon, two-sided rough nonmetallic material. Sample UV base color, mix 28% cream RGB (238,222,197), brighten tips slightly. No simple primitive-body construction. Core executed geometry:
```python
flow=np.tile([0.,-1.,-.16],(len(p),1))
flow-=np.sum(flow*n,axis=1)[:,None]*n
flow+=rng.normal(0,.19,flow.shape)
flow-=np.sum(flow*n,axis=1)[:,None]*n
flow/=np.maximum(np.linalg.norm(flow,axis=1,keepdims=True),1e-8)
side=np.cross(n,flow)
side/=np.maximum(np.linalg.norm(side,axis=1,keepdims=True),1e-8)
# indexed selected surface p,n,flow,side -> P,N,D,S
L=rng.uniform(.010,.026,len(P))*strength*(1-.35*(R>.84))
W=L*rng.uniform(.075,.14,len(P))
mid=P+N*(L*.41)[:,None]+D*(L*.36)[:,None]
tip=P+N*(L*.55)[:,None]+D*(L*.89)[:,None]
V=np.stack([P-S*W[:,None],P+S*W[:,None],mid-S*(W*.72)[:,None],mid+S*(W*.72)[:,None],tip],1).reshape(-1,3)
F=(np.array([[0,1,2],[1,3,2],[2,3,4]])[None,:,:]+5*np.arange(len(P))[:,None,None]).reshape(-1,3)
```
Strength .75 or 1.15. VTK EGL actual UV base-color + vertex-color ribbons, Phong diagnostic (not full PBR), 420x420 frames at 0/45/90/180. Observed glTF exporter initially omitted ribbon material: fixed JSON chunk to explicitly assign doubleSided:true, metallicFactor:0, roughnessFactor:1; reimport verified triangle totals. Render uses double-sided VTK geometry; browser not retested after material fix.

## Actual output
Three GLBs all reimported, two retained embedded base textures. Baseline 27,372 tris/2,760,856 bytes/1 mesh, SHA256 860710399736a735df1ece004d62cb8e5d88d6d252dc70093f4330560a0a1cdc. Short 63,372 tris/4,153,780 bytes/2 meshes, SHA256 a4d869ba8d094063281e12c225368a0c1ad7d1060204c19a5ed169a0a44047eb. Dense 105,372 tris/5,777,784 bytes/2 meshes, SHA256 1b870ab9db2795493a10e8230ad0dfb039edd04971ce4d1b5e30ea0c59036b66. Actual 12 frames and 1680x1260 full montage inspected. Full comparison.jpg SHA256 eb5aada9a19d47fda034f329682cd10551362432bd9ac721e9d1922ef2073fbb. Executed experiment.py SHA256 dc41fb31c8de9510cd36b25696e4765cc5767cb0133c002b111ce957d43aad72; fix_material.py SHA256 af379aa2a2bdcf74b9a3b3638228945df1d4851b9b26da1925857c406d3a9048; metrics.json SHA256 4691112ccacc758657178b9fde15e2aa49ec7707f4af8acc0645ca5370ce8043. Compact actual 96x72 montage archive.jpg 1,385 bytes SHA256 a3bee4a26df2293a4b8d8f9e539eb5e9a66bb2962e45bedf604744bdec4acd9c, separate encoded evidence; rows baseline/short/dense, columns front/quarter/right/back. Full files in current working directory only, not guaranteed persistent.

## Art gate
SF3D base front is appreciably more owl-like than TripoSR: recognizable heart mask and dark eyes. Short and dense directional surface geometry visibly improves fluffy silhouette, especially on sides/back. However the dense version still has uniformly hairy rather than feathered appearance, crown remains dark/striped, rear has barrel silhouette and horizontal ridges, wing anatomy is absent, face profile projects like a mask, toes/wood remain flattened. Both groomed variants rejected; no new physical phone or WebGL validation. Do not release or notify as a qualifying sample. Future prioritize anatomical mantle and shoulder/foot correction on the alternative base or new professional geometry, rather than repeating TripoSR edits. No additional fees, no live deployment or 251-species changes.
