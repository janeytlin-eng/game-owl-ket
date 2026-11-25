# Run360 — SF3D continuous mantle volume + UV crown ablation — NO_RELEASE
2026-11-25 Asia/Shanghai. ART_REJECTED / NO_RELEASE. Extra fee zero.
## Preflight
Read main owl-pet AGENTS, README, STATUS (206/251, 45 remaining) and #172 v3 review (cream mesoptile, short buried wings, age unknown, science=false); read Run359 at dbbce14b6e7b138ef886d4bd9f2b9cc40fb8ddb7. Recovered historical Run317 artifact 14795923598 via GitHub connector, extracted original native SF3D GLB (1,137,108 bytes, SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be, matches Run359). Viewed actual old front and side browser images and isolated reference. Rotated model 180 degrees around Y to align face +Z. Actual local environment: trimesh, VTK, scipy, torch available; Blender/bpy, moderngl and pyrender absent; DNS lookup github.com/huggingface.co returned no address. No new neural inference or charged calls.
## Executed ablation
Instead of more uniform ribbons, isolate shoulder and mantle volume on the alternative genuine UV-textured mesh. Continuous displacement of existing surface, not attached primitives; preserve facial disc and feet. Moderate and strong strength (1/1.8). Apply a cream crown/back correction within existing UV atlas by nearest UV vertex weighting, preserving original texture detail, embedded normal map unchanged. This is art experimentation, not scientifically inferred wing structure. Core equations (actual experiment.py):
```python
x,y,z=v.T
h=(y-y.min())/np.ptp(y)
wing=np.exp(-(((h-.52)/.16)**2+((z+.055)/.17)**2+((np.abs(x)-.24)/.105)**2))
wing*=np.clip((np.abs(x)-.08)/.12,0,1)
mantle=np.exp(-(((h-.72)/.13)**2+((z+.17)/.13)**2))*np.clip(-z/.13,0,1)
vv[:,0]+=np.sign(x)*scale*.045*wing
vv[:,2]-=scale*.04*mantle
crown=np.exp(-((h-.94)/.13)**2)*np.clip((.24-z)/.15,0,1)
rear=np.clip((-z+.04)/.20,0,1)*np.clip((h-.17)/.20,0,1)
weights=np.maximum(crown*.65,rear*.36)
# KDTree nearest UV vertices, pixel distance fade 16 px
w=(weights[idx]*np.clip(1-dist/16,0,1)).reshape(H,W,1)
tex=np.uint8(np.clip(orig*(1-w)+np.array([235,220,195])*w,0,255))
```
Exported three native GLBs, successfully reopened each with trimesh. Actual VTK EGL diagnostic base color + lighting render (not complete PBR), 420x420 four views each. 1680x1260 montage inspected. No new browser or device test.
## Measured outputs
All three 27,372 triangles; all reported non-watertight by trimesh (including baseline, UV seams may contribute; not claimed closed). Baseline 2,556,884 bytes, SHA256 b01dc7a81c0d75e063f837a37ecc745921868d19b6dfc0e644ef3a1c05081552; mantle 2,625,592 bytes, SHA256 98eb7c63a701faa788645cd9cd5f79f70ec657ac8955c6541b6154a141868b46, max displacement .0445628621; strong 2,625,596 bytes, SHA256 2f84f761fc66c0882ec9ba973189bac050a67e4b9b8138ab6221cc8dd15c098d, max .0802131518. Executed experiment.py SHA256 ab08c9c2c83a538586f79bbe467d09374c957e339771f70043a1f8f80f880ca6; metrics.json SHA256 824660a96c9781f0d04a982ae23c772ab302a45c280d9020799859ff1ac0f33d; full comparison.jpg SHA256 a418730bcbb3ebe9fc38332724f03fd03e90e04f55a2280359084c38da50c00f. Compact actual montage 96x72 JPEG (2082 bytes, SHA256 09cfe5c19826816052d24e821d86da2b7c78bfaf5d791ac0dbceb47b695d314c); rows baseline/moderate/strong, columns front/quarter/side/back. Encoded evidence separate. Full models and original render files in current runtime only, not guaranteed persistent.
## Actual visual decision
Crown/back lighter and moderate shoulder silhouette slightly more rounded, front mask preserved. Strong variant exaggerates side bulge and squared lower torso. Side still reads as flat projecting mask, rear broad featureless barrel with horizontal crown ridges, visible feet flattened into wood. Neither wing anatomy nor soft down is convincing. All rejected. No art gate pass, no physical phone/WebGL qualification or release. Source asset rights not cleared. Do not keep increasing same displacement. Next prioritize materially different base geometry (new no-fee reconstruction or documented licensed artist mesh), not more cosmetic repair. Main, species production, original concepts and deployment untouched.
