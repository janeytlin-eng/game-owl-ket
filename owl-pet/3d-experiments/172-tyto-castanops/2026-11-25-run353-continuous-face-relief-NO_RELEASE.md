# Run353 — continuous facial anatomy relief ablation — NO_RELEASE
2026-11-25 Asia/Shanghai. ART_REJECTED / NO_RELEASE.

Read current main README, STATUS (206/251), DESIGN_WORKFLOW, prototype/index.html, #172 v3 review, and Run352 at cf4db259f2a48ad30177fd2032b87c2129ae5734. Target remains v3 rightmost young, not subsequent concept revisions. Downloaded historical artifact 14733006902, unzip test passed, inspected source crop and six-direction sheet. Donor SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117. No new neural inference. CUDA unavailable, Blender/bpy absent; huggingface.co DNS failed from local runtime. No new external generation or charges.

## Actual experiment
Test whether replacing the front face depth field with a continuous, anatomically landmarked surface can fix flat/concave face without replacing the entire body or adding primitive parts. Largest connected donor component (50,205 vertices / 100,534 triangles), axes reorder [1,2,0], bounding-box center. Fit a tilted facial disc with shallow bilateral orbital recess, raised corneal center, nasal ridge and shortened bill. Soft spatial patch weight; affine correspondence from three manually marked donor landmarks to the actual source image. Blend front face colors only. Baseline vs partial (geometry .65 / color .60) vs full (1 / .85). This is a local sculpting test, not a new learned mesh or independent full anatomy reconstruction.

Actual core of executed face.py:
```python
face=(1-expit(18*((((x-.065)/.225)**2+((y-.225)/.205)**2)-1)))*expit((z-.12)/.018)
base=.251-.205*(x-.055)+.025*(y-.22)
def g(cx,cy,sx,sy):return np.exp(-.5*(((x-cx)/sx)**2+((y-cy)/sy)**2))
relief=base-.034*g(-.012,.218,.043,.032)-.034*g(.165,.23,.043,.032)+.036*g(-.012,.218,.023,.019)+.036*g(.165,.23,.023,.019)+.026*g(.073,.179,.032,.057)+.031*g(.083,.104,.025,.032)
a=np.array([[-.012,.218,1],[.165,.23,1],[.083,.104,1]])
b=np.array([[257,154],[330,153],[303,223]])
uv=np.c_[x,y,np.ones(len(x))]@np.linalg.solve(a,b)
img=np.array(Image.open('juvenile_rightmost_masked_512_RESEARCH.png').convert('RGB'))
photo=np.column_stack([map_coordinates(img[:,:,i].astype(float),[uv[:,1],uv[:,0]],order=1,mode='nearest') for i in range(3)])
# for each strength/colorstrength:
w=v.copy();w[:,2]=z+strength*face*(relief-z)
col=c.copy();col[:,:3]=np.clip((1-colorstrength*face[:,None])*c[:,:3]+colorstrength*face[:,None]*photo,0,255).astype(np.uint8)
```
Three actual native GLBs exported with normals and independently reimported, each 2,613,436 bytes / 100,534 triangles / 50,205 vertices / watertight connectivity. Displacement max in normalized donor units and number of triangles with negative normal dot vs baseline (not a self-intersection proof):
|Variant|Max displacement|Negative normal dot|SHA256|
|---|---:|---:|---|
|baseline|0|0|d5bde22c49edbfdc20da45e4785a2b6bfa1bec06803d8348f555b85e34681459|
|partial|.0426093|0|4cee5c7e7045bbb86e7adbae8f3680084f475a948d368bbf1cea9076b2a7c893|
|full|.0655528|46|08c8b47d96d3fcd665fb9ac74ed1b764bf7a8da34ecf5da48177c30ce67a24f9|

12 actual VTK offscreen Phong views, each 330x370, 0/45/90/180 degrees, same camera and lights. Opened full contact sheet. Partial softens nose and face edge but eyes remain recessed and blurred; full creates a conspicuous flat mask with a hard edge in side profile and 46 reversed-normal indicators. Both retain ugly dark back, clay-like nodules, and artificial feet. All rejected. The partial result is not a viable release. Neither local face reconstruction nor repeated body smoothing/material patches resolves missing base sculpture; prioritize genuinely different donor or reconstruction engine.

## Browser probe
Actual Chromium 144 Playwright mobile viewport 390x844 DPR2. First data URL navigation blocked ERR_BLOCKED_BY_ADMINISTRATOR; reran using page.set_content on blank page. Five configs (default, ANGLE swiftshader, ANGLE swiftshader-webgl, ANGLE gl/Mesa, ANGLE Vulkan) tested WebGL2, WebGL, experimental-webgl: all 15 returned null. No device benchmark or usable mobile viewer; VTK offscreen render does not count as browser evidence.

## Evidence
Executed face.py SHA256 e49b97902f28878298a6e1e95981d0a25567a44099ff19aa14ae41fec62d3b30
render.py SHA256 71623c250f093c95633ebd4eea0e6e1bf3e07e1bcdfa5920c1e06602914a6ec4
browser_probe.py SHA256 31e8c42adc13712dfda98b1ae536010079710f9e7404578b56ceb4cfced38716
browser_probe.json SHA256 0a4f82dba7ef2bc900a2398bfae8175b991692aa7dd9f778d43b6449efba8683
contact.jpg SHA256 45ad824e444c5d107a52fa416cbf971979b0d75055eb416dcf79004c206be841
metrics.json SHA256 44911b9d9dfd4714fb270cedc89eb488b222c7395fcf5097b3c1bba4f5d0e47a
Full GLBs, scripts and full-size renders local only. Separate tiny JPEG base64 evidence (96x81, 2042 bytes, SHA256 5518185c8d005b1ca9a76faef1cde05697f26f1eafc1b7aa4600d795c160578c) is only an orientation thumbnail, not art approval.

Independent research branch from main. No change to main, species workflow, original concepts or deployment. Zero extra spending.
