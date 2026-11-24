# Run357 — visibility-gated source colour projection — NO_RELEASE

2026-11-25 Asia/Shanghai. ART_REJECTED / NO_RELEASE.

## Preflight
Read main owl-pet/AGENTS.md, README.md, STATUS.md (206/251, 45 remaining), #172 v3 review (cream mesoptile, age unknown, science=false), and Run356 at 9b4075874692da364b695d833ca656cbfd5eeb19. Recovered actual historical Actions artifact 14733006902; source GLB SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117 matches prior report. Opened original RGBA source crop and six-axis rendered montage. Original is genuine TripoSR output, not a new inference. Local VTK 9.6 with EGL works; bpy and GPU-based new engine not available (no Blender executable; direct DNS lookup for github.com and huggingface.co returned no addresses). No external paid job.

## Executed experiment
Unlike Run352 normal map synthesis, this tests depth-gated direct colour transfer from the original target photo-concept into the actual 3D surface, and a distinct rear-diffuse correction hypothesis. No new anatomy or geometry synthesis. Original has 110 connected components; largest closed component 50,205 vertices /100,534 triangles. Standardized axes by cyclic (old y,z,x) -> (new x,y,z) so glTF Y-up and front +Z. Rendered with VTK EGL orthographic camera, size 480 x 480, unlit for alignment. Used largest hard alpha source component from Run356 method; registered its silhouette against actual depth-buffer foreground using 225 discrete affine tests (5x5 scale choices and 3x3 offsets). Best IoU 0.94933612. Transform source pixels to render pixels [[0.8800959233,0,43.67865707],[0,0.8346551724,11.63913793]].

Per vertex, compute orthographic projected pixel, expected normalized depth, sample actual z buffer bilinearly. Accept only abs(expected-observed)<0.012 and observed<0.999; multiply by eroded mask distance/8 and forward normal gate clamp((nz-.05)/.6). 16,167 vertices with nonzero weight, 14,127 with >0.5. Sample source RGB bilinearly and blend into existing vertex colours. Rear-diffuse experiment separately compresses dark baked values towards source belly sample median [172,134,104], retaining 15% luminance modulation and tapering near feet. It is a design hypothesis, NOT evidence for the unseen back. Source belly median is too tan, not a validated cream target.

Core calculation from executed experiment:
```python
observed=map_coordinates(z,[yp,xp],order=1,mode='nearest')
expected=(3-(vv[:,2]-mid[2])-near)/(far-near)
vis=(np.abs(expected-observed)<.012)&(observed<.999)
dist=distance_transform_edt(main)
maskw=np.clip(map_coordinates(dist,[w,u],order=1,mode='constant')/8,0,1)
anglew=np.clip((m.vertex_normals[:,2]-.05)/.6,0,1)
weight=vis*maskw*anglew
samp=np.stack([map_coordinates(src[:,:,i].astype(float),[w,u],order=1,mode='nearest') for i in range(3)],axis=1)
front=base*(1-weight[:,None])+samp*weight[:,None]
backw=np.clip((.25-m.vertex_normals[:,2])/.8,0,1)*np.clip((yfrac-.10)/.15,0,1)*(1-weight)
lum=base@np.array([.2126,.7152,.0722])
target=cream[None,:]*(.85+.15*np.clip(lum/160,0,1))[:,None]
rear=front*(1-.85*backw[:,None])+target*(.85*backw[:,None])
```

## Actual native outputs
All three 2,613,436-byte GLBs reimported successfully (trimesh), 50,205 vertices, 100,534 triangles, watertight; explicit normals requested. Each rendered at 0/45/90/180 degrees (12 genuine 480x480 VTK frames). SHA256:
- baseline_NO_RELEASE.glb: 87c15ddff0725219dcb8914eedc29263c7444172b8119fe1fc90dd6a63692d5d
- project_front_NO_RELEASE.glb: a490135c79d9ea28bb8c589da28de6842885e0954c248ee8302ebbfcf5e5bdad
- project_front_rear_diffuse_NO_RELEASE.glb: 54269708e9484ebfb2d32d2e15421e2d63a95e7d416ec267e3234c1ff4e84420
- Actual full comparison JPG SHA256 f76a999bf989e88589b6863d53a4abdddb238153f377bf10a255319ca19dd357
- Executed complete source SHA256 a244154cfbefa77c11c8399e1dde36c909372e9a500fe95ae34da2ef98c9b2c6
Full GLBs, code, render frames and report.json saved in current run's local /mnt/data/run357 only; not guaranteed persistent. Separate compact JPEG evidence is 200x160, 2,786 bytes, SHA256 281749cfdafe2dadad47628ca8752420280f4eab8daa59ec68b5b514cb7dcbd9, Git blob SHA1 79a842273fa345578ba5b9d011e24d7fa5b5f283. Thumbnail rows are baseline, front projection, front+rear correction; columns 0/45/90/180.

## Visual review and gate
Actual full 1200x960 comparison viewed. Direct projection restores some front disc colour, but soft photo details do not overcome sunken eyes or scalloped clay-like surface; one eye appears smudged due to imperfect registration. Rear correction removes dark-charcoal cast but replaces it with flat tan, abrupt transition at lower body, and conspicuous vertical grooves. Profile remains unnaturally flat. No candidate passes. No new mobile browser or physical phone test, previous Run355 software browser test only. This confirms improving colour alone does not overcome poor topology/geometry. Do not repeat this as a route to art acceptance. Need new neural base or sculpted geometry from multiple coherent views. Zero additional spend. Only isolated research branch; do not alter production, main, concept images, or live site.