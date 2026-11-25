# Run373 — native morph targets in WebGL2 — ART_REJECTED / NO_RELEASE
2026-11-25. Independent experiment from Run372 404278814cdd5922640a053b29f528c25e2219ad. Extra spend $0.

## Preflight
Read main AGENTS, README, STATUS (206/251, 45 remaining), #172 v3 review and Run372. Target cream mesoptile, developed heart mask, short wings buried in down, concealed tail, unknown age, science=false. Recovered original SF3D artifact 14795923598 via GitHub Actions download, unzipped and verified SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be. 1,137,108 bytes. No Blender executable, torch.cuda.is_available() false. Do not confuse original reference art with mesh.

## Alternative foundation search
New source https://sketchfab.com/3d-models/snowy-owl-e63aacf6b63a41f6bf9b302aad460835 describes Carnegie Museum educational collection snowy owl, CC BY, 30.9k triangles. Wrong genus and juvenile morphology unverified; no binary acquired. https://sketchfab.com/3d-models/barn-owltyto-alba-af3cdd38e029430d9c131370ebf1bb33 CC BY, only 760 triangles, no morphological description; no binary acquired. https://paprika3d.com/docs/models/birds describes CC BY/CC0 GLB catalog, 569 birds; searches for barn owl and chick entries yielded no results; no specific suitable asset acquired. Florida Museum's specimen https://www.floridamuseum.ufl.edu/digital-lab/gallery/north-american-barn-owl-skull/ is a skull only, not a feathered juvenile foundation. Paid statue scan excluded. No paid inference or purchases. Continue search for actual new naturalistic juvenile foundation; do not repeat texture repair.

## Executed native GLB and real browser test
Run372 VTK animation did not change framebuffer. Here tested an independent morph-only approach instead of skinning. Actual native GLB morph-NO_RELEASE.glb: 2,156,972 bytes, SHA256 f67e77a04c0cdd2e6060d4baa72ab8b5d665d17dc56d252ceea1b60ad985049f, 16,971 vertices, 27,372 triangles, 3 POSITION targets, two also have NORMAL deltas, original baseColor and normal texture preserved. Named targets YawPlus12, YawMinus12, Breath; one native animation IdleMorphTest, weights path, 7 keys at 0..6 s. Core actual computation:
```python
pivot=np.array([0,.10,-.035])
t=np.clip((v[:,1]-.015)/.25,0,1); w=t*t*(3-2*t)
theta=np.deg2rad(deg)
R=np.array([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta),0,np.cos(theta)]])
delta=w[:,None]*((v-pivot)@R.T+pivot-v)
nn=(1-w[:,None])*normals+w[:,None]*(normals@R.T)
nn/=np.linalg.norm(nn,axis=1,keepdims=True).clip(1e-9)
mask=np.exp(-((v[:,1]+.105)/.16)**2)*np.clip((v[:,1]+.34)/.12,0,1)*(1-w)
delta_breath=np.zeros_like(v)
delta_breath[:,0]=v[:,0]*.035*mask
delta_breath[:,2]=(v[:,2]-.015)*.025*mask
```
Both yaw targets have max displacement .05585496, foot vertices y<-.25 unchanged (max 0). GPU vertex shader computed position from actual emitted GLB accessors, not independently drawn image:
```glsl
vec3 v=pos+w.x*da+w.y*db+w.z*dc;
n=rot*normalize(norm+w.x*na+w.y*nb);
```
Custom limited glTF subset loader reads embedded baseColor, indices, positions, UV, normals, target deltas and animation sampler from binary. First localhost HTTP attempt blocked by browser admin policy (ERR_BLOCKED_BY_ADMINISTRATOR); used local embedded bytes in page.set_content, no external network. Xvfb + Chromium with SwiftShader flags, emulated mobile viewport 390x780. Actual WebGL2 reported WebGL 2.0 (OpenGL ES 3.0 Chromium), renderer string WebKit WebGL. Nine captures from actual drawElements (27372 triangles every frame) at three angles 0,1.57,3.14 rad and three key times 0,1,3 s; weights [0,0,0], [1,0,.5], [0,1,.5]. All getError=0. Nine SHA256 hashes distinct. This is explicit sampled keyframe rendering in a custom shader, NOT full general glTF player conformance, not continuous-playback FPS or real iOS/Android hardware QA. Original normal texture not sampled in this custom shader. No animation quality approval.

| angle | rest SHA256 | +12 SHA256 | -12 SHA256 |
|---|---|---|---|
| rear | 50c2e8477add689d79913edff957ec3e3ba07b16598d4896e975a25fa06f6661 | 60dd14ea918ef2366e3cbba47f2e91f1cb6398d011e421c88bd73f63ba047e40 | 293ba0850539fbd7c22669bde5521ffc74ecd0980e5cca8e470909e4e93483e2 |
| side | c3d448d6428986f4a2e1444f21ef394ff07aac51a24fa78131f37bf49df0c9dc | 1587fcb00d30aa769d72b00bef13ba8cee851054fd6f899edcb25b41207897b5 | 9a52061b299441541a5f354a059d4246ee9f97fa05bf99f06a77f71829ece743 |
| front | a567a149df5142c35b9f991b99f9cd4d56b9e2530c8f50c2d769ffdd0584e155 | 27dee2da097e8943f333a7bc28d1e9d041dfc947e3ea18233e694534a274aad1 | 67d8239acae2a9e1dbb6975c9f0fd50608683cd202a376e05341bda6d88fc608 |

Full contact sheet visually inspected: front heart mask remains identifiable with slight turn, base remains planted; side dark seam, flat rear shoulder/wing region, crown dark edge, insufficient cream down volume, and fused foot/support remain. Reject. This is engineering readiness only; new high-quality artwork still absent. No real phone test; no release.

## Evidence
Full GLB/scripts/images local only, no claim of remote binary archive. Actual SHA256: morph.py 8dce2f7ded1c1deb318e253248be63ca52ef0aeeef5e53ad9d02cb34eae0c88d; viewer.html fa45f94a85ded91039755ff954df7348185c6b35f3191e54061edba36b0c4297; check.py 0a88b0ab8b3ce8513b7fcf8454c6522685f9ed9a3dbc01c34556f4b3f8ccb426; report.json 7b46382c76643f788659ad2ff611807220f327b2db65e3d4248e6012ba718f70; contact.jpg d9b26d369c11e58e4e6579f0928f86810bdad1161253e3eb818a9541a563f518. Tiny actual screenshot contact sheet, rear/side/front columns, rest/+12/-12 rows; 90x97 JPEG, 1959 bytes, SHA256 347984bb702797c9772527891f08c813b74b9e360c61a1f89189b793964d16fc. Evidence only:
```base64
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
```
No main, production flow, concept or deployment writes. ART_REJECTED / NO_RELEASE. Do not notify.
