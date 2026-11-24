# Run348 — native crossed tapered down ribbons / density-length ablation — NO_RELEASE
2026-11-24. THREE_NATIVE_GLB_REIMPORTED / 12_VTK_VIEWS / ART_REJECTED / WEBGL_UNTESTED / NO_RELEASE.

Read main owl-pet/AGENTS.md, README.md, STATUS.md (9fe70415778bfc18eb2c762b7f1c44a8374b3da1), prototype/index.html, #172 v3 review (50ab5259987180a6a46a428317440f2436bfce56), immutable Run347 (5e1c8865de1083f879490cd5a176c5270f0d8700) and Run344. User-selected v3 rightmost cream mesoptile remains fixed. Downloaded historical Actions artifact 14733006902, verified SHA256SUMS, directly viewed masked v3 input and six-camera donor render. Real pretrained TripoSR donor SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117. No fresh inference or paid API. Local NumPy/SciPy/Trimesh/VTK/Pillow available; Blender/bpy/ONNX Runtime/PyMeshLab/moderngl absent; getent hosts github.com huggingface.co returned no addresses.

## Actual experiment
Keep largest connected donor, orient axes [1,2,0], region-protected 12 Taubin passes .5/-.51, cream body color blend .78 with facial/foot preservation. A is fixed base. B/C add actual curved tapered cross ribbons on the continuous donor, NOT a primitive body replacement. Area-weighted random face roots with barycentric interpolation of position and normals; exclude protected face/feet, bottom-facing roots. Seed348. Project downward direction onto tangent, add randomized flow. Two crossing ribbons per root, each 5 paired cross sections / 8 triangles. B=4500 roots nominal length .023, C=9000 roots nominal length .030; length variation .55–1.5, width .035–.075 times length. Density and length covary so not isolated effects.

Core executed centerline and taper (excerpt, not full script):
```python
ts=np.array([0,.28,.60,.85,1.])
center=root[:,None,:]+L[:,None,None]*(n[:,None,:]*(.80*ts[None,:,None]-.32*ts[None,:,None]**2)+flow[:,None,:]*(.75*ts[None,:,None]**1.5))
taper=np.array([.5,1,.78,.42,.035])
for axis in [across,np.cross(across,.6*n+.8*flow)]:
    pts=center[:,:,None,:]+axis[:,None,None,:]*width[:,None,None,None]*taper[None,:,None,None]*np.array([-1,1])[None,None,:,None]
```
Full local script SHA256 3a605776f201347da8b1b077eb0f6d69acfe5669d326e0f277ac7512280640ef; Git blob a0ad50480c306cc763ba01273d2ed61466e6abb9 (local only). All exported with include_normals=True, reimported as scene, independently parsed GLB JSON confirms POSITION/COLOR_0/NORMAL for every primitive, addressing Run347 portability omission. No explicit materials in GLB; default one-sided material may hide ribbon faces in browser. VTK actual 480px renders 0/45/90/180, 12 total. VTK normals and lighting are not browser PBR.
- A 100534 triangles, 2613428 bytes, SHA256 0ad8fba68a83feee74ddf29c98ca59b283013093be9e82d08801ad93d46449f1.
- B 172534 triangles, 5998460 bytes, SHA256 0cd1526186d17d128b5c91addaf7ea331dfdd041eba7f66fc0807b5d48151c51.
- C 244534 triangles, 9382464 bytes, SHA256 6732e61022b18ccb84bc41a124a5657da68393b77efd0ec85a6c760879dde7d1.
Full contact JPEG SHA256 f47e2e426b009c7967d984edaf09087d8bd5cb5a3a6910ab658ed79b6c1aa952. Tiny contact JPEG 192x149, 2231 bytes, SHA256 a2e58a49d4a280e76673290168d9a4194a58809de2809163d0a10c6eea60ba62, archive run348-local/evidence.jpg.b64. Native GLBs, full script and full-size images local only.

## Gate
A baseline looks like embossed stone. B hardly covers surface. C visibly adds fine filament silhouette across crown and rear but looks like sparse straw over cracked clay, with uneven flank coverage, dark lower rim, hollow eyes (Run347 patch not carried forward), flat face and rough fused feet. 244k triangles and 9.38MB before textures/animation is costly for mobile and no proven web render. All rejected. No real phone or WebGL test. Next avoid increasing density further on this donor; a new anatomical base or true alpha-tested groom with explicit material and measured mobile rendering is needed. No change to main, species production, v3 source or deployment; no extra spend.
