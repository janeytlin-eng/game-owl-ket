# Run366 — native GLB transport optimization / compatibility ablation (NO_RELEASE)
2026-11-25 Asia/Shanghai. ART_REJECTED. Extra spend $0.

## Preflight
Read main owl-pet AGENTS, README, STATUS (206/251, new production batch 0/6), original #172 v3 review (cream thick mesoptile, developed mask, short buried wings, concealed tail; age unknown and science=false), and Run365 commit 3f596b29114c7732d94ed327bfdd2f90b9e1d021. Restored actual Run317 Actions artifact 14795923598; source SF3D GLB SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be matches. Viewed isolated reference and historic WebGL renders. No replacement of requested v3 with newer concept. Previous repairs repeatedly failed art gate; this round isolates mobile delivery overhead rather than pretending transport changes solve anatomy.

## Executed
Direct GLB buffer repacking, not geometry simplification. Original index max 16970, 82116 indices; 16971 vertices, 27372 triangles. Converted uint32 indices to uint16 with exact equality, optionally normalized uint16 UV. Preserved position, normals, both original 1024px JPEG textures and material byte payloads (material JSON values unchanged). Four-byte alignment and accessor component types updated. Each output reopened using Trimesh. Actual core:
```python
idx=np.frombuffer(chunks[0],'<u4')
uv=np.frombuffer(chunks[4],'<f4')
assert idx.max()<65536 and uv.min()>=0 and uv.max()<=1
c[0]=idx.astype('<u2').tobytes()
d['accessors'][0]['componentType']=5123
# optional variant only:
u=np.rint(uv*65535).astype('<u2')
c[4]=u.tobytes()
a=d['accessors'][2]
a['componentType']=5123
a['normalized']=True
a['min']=u.reshape(-1,2).min(0).tolist()
a['max']=u.reshape(-1,2).max(0).tolist()
# rebuild all bufferViews with 4-byte alignment, JSON/BIN chunks,
# buffer byteLength, and GLB header total size.
```
|Variant|Bytes|Triangles|SHA256|
|---|---:|---:|---|
|control|1137108|27372|c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be|
|index16|972876|27372|64a1097565d708290f880edb523cdd68fed270747ea92ceb46d0b4bed538a902|
|index16_uv16|904948|27372|31f17d8a2832aa6edccae47542194607f6f93e391ba6fa96c576ec65dbfa49cd|

Index-only saves 164232 bytes (~14.44%) exactly. UV variant saves 232160 bytes (~20.42%); max UV quantization error 7.658e-6. But Trimesh returned raw UV range 218..65319 rather than normalized 0..1; it requires explicit decoding. Hence conservative recommendation index-only; normalized UV compatibility not established. Actual VTK offline base-color renders (not full PBR), 240x240 front/45/profile/rear each. Index-only had zero differing RGB pixels in all four views. UV variant rendered after direct accessor decoding and V flip: mean absolute channel difference 0.010382/0.009653/0.007494/0.007164 on 0..255 scale; max difference 2/2/2/1, changed pixels 1280/1136/780/673. Viewed all 12 renders. Art remains rejected: flattened profile, dark crown, missing wing structure, fused feet, insufficient fluffy volume. Identical visual quality is not an art improvement.

## Actual browser attempt and external route
Wrote a dependency-free WebGL2 diagnostic viewer including normal map and mobile viewport 390x780; Playwright Chromium launch succeeded but navigation to loopback HTTP returned net::ERR_BLOCKED_BY_ADMINISTRATOR. Stopped browser attempt; no new browser/phone PASS, no circumvention. VTK is independent offline render only.
Reviewed https://grab3d.com/models/animals/owl/ (CC0 high-detail 800k triangles, 400k light; adult great horned owl with ear tufts and yellow eyes, unsuitable as direct juvenile Tyto base); actual curl failed DNS code 6. https://sketchfab.com/3d-models/barn-owltyto-alba-af3cdd38e029430d9c131370ebf1bb33 is CC BY but only 760 triangles; not equivalent to target fluffy anatomy. Florida Museum skull https://sketchfab.com/3d-models/barn-owl-skull-310673d074af40ddabac5b84d168fc3a is anatomy reference only, not whole bird. No external assets obtained. CUDA False, Blender absent. No paid model invocation.

## Evidence
Executed source optimize.py SHA256 66b96d732c16d8862c8e987eaae31552899e493d57588ae8d0e06f9f2d3dafe3; optimize.json 105d954e8e41287b33b561728e0f111a5c93d3775ad47dfd6914a0aa2a6f49c8; render.py 020be61f112cc65bf6c3f3753bfdda0eadb5d7536878e0ca838989e78bc96789; vtk.json 6f011fda061b1fc6a9103d431fb50da64c3b2e462cdfec84b9c8cc3ecd8faae4; full vtk-contact.jpg ecf90f82788e009eecea900513b90b52dfac97666a0803a047148b4951ea10e2. Viewer a92d28dd4cde07255a8395db758f39e8a8218a4a5991734348e08d68110a7018; browser.py 9c94260336686a379b51ea71601b8066fa2939c89712bceb180f660c77248535. Full outputs local to this execution, not claimed durable remote. Tiny actual render contact below (96x72 evidence only, not sufficient for art review), rows control/index16/index16_uv16; columns front/45/profile/rear. SHA256 b77312d9a6772c4d25a1758db1e36920ec128c5ad3b385149bacd7fcbce60378.
```base64
/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCABIAGADASIAAhEBAxEB/8QAGQAAAwEBAQAAAAAAAAAAAAAAAAMEAgEF/8QAJxAAAgIBAwMEAwEBAAAAAAAAAQIAAxESQVEEITETIjJhFIGRIzP/xAAWAQEBAQAAAAAAAAAAAAAAAAABAAL/xAAXEQEBAQEAAAAAAAAAAAAAAAAAARFB/9oADAMBAAIRAxEAPwD03bSpPmT+pv6hzxHW/ED7iiuCCPMxa1Icja0BhY4RCx2mKD2ZeDO9Qf8AI/ZE0OlB2bJWz3DyNo9G1oG5ikxjvNUHKEcEwlNjdjiutmPgCJzaDqD5+to21ddZEQLMr+pVSKUbUobmcsbQhO+0zQc0rOdQcBRyYgvNoGrWc8bR6NrQN4iifbNdOc1n6MJTYLw5ClBkg+JOfyS3eo45yJY7aVJ8yf1N/UOeJXFNNoQpX7vke5nOo1GrCKWOdptG1oDCxwiFjtEIwvUYwaz/AGU9PWa6sN8icmLDs2StnuHkbR6NrQNzCYbodiq5CljwJE1N2okIRnbMtscV1sx8ARObAdQfP1tKiGdOjJSFbzC9C9Z0j3DuJtG1KG5nLG0ITvtFJNN2MemY/pkdFbWMZPYTGbQNWs542j0bWgbxCYbrlvxA+4orggjzN3hyFKDJB8Sc/klu9RxzkQumYooPZl4M71B/yP2RChClfu+R7mc6jUasIpY52jxnrKYx3mqDlCOCZMF6jGDWf7KenrNdWG+ROTCQ2tWrrrIiBZlf1KHYquQpY8CRNTdqJCEZ2zGxSq6DmlZzqDgKOTO9OjJSFbzC9C9Z0j3DuIjrBPtmunOaz9GT6bsY9Mx/TI6K2sYyewmZGrTXbSpPmT+pv6hzxHW/ED7iiuCCPMrRIcja0BhY4RCx2mKPDLwZ3qP+R+yJodKDs2Sth1DyNo9G1oG5ikxjvNUHKEcEwlNjdjiutmPgCJzYDqD5+to21ddZEQLMr+pVRSjalDczljaEJ32maDmlZzqDgKOTEF5tA1aznjaPRtaBvEUT7Zrpzms/RmZTYLw5ClBkg+JOfyS3eo45yIQjYpVNCFK/d8j3M51Go1YRSxztCEQmC9RjBrP9lPT1murDfInJhCEitbdiq5CljwJE1N2okIRnbMIRSvp0ZKQreYXoXrOke4dxCEkm03Yx6Zj+mR0VtYxk9hCEMWv/2Q==
```
Next: prioritize alternative source anatomy or coherent multiview assets; transport optimization can be applied later to an art-passing model. No release or production changes.