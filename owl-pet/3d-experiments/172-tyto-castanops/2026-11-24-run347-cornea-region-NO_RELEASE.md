# Run347 — integrated corneal patch depth/material ablation — NO_RELEASE
2026-11-24. TWO_NATIVE_GLB_REIMPORTED / TWELVE_VTK_VIEWS / ART_REJECTED / WEBGL_UNTESTED / NO_RELEASE.

Read main owl-pet/AGENTS.md, README.md, STATUS.md (9fe70415778bfc18eb2c762b7f1c44a8374b3da1), prototype/index.html (fb04d85da57b6cb54ec48d455e3fc8570380172d), v3 review (50ab5259987180a6a46a428317440f2436bfce56), Run346 record and its source (a7a9ed61ef03865c8f487568b659727f98841fe7). v3 young rightmost remains fixed, not current v5. Downloaded Actions artifact 14733006902, checked SHA256SUMS, directly inspected masked input and six-view donor sheet. Source GLB SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117. Free local VTK, NumPy, SciPy, Trimesh, Pillow available; no Blender, bpy, ONNX Runtime, PyMeshLab, moderngl; github.com/huggingface.co DNS unresolved. No extra spend or new neural inference.

## Actual experiment
No additional global smoothing/color sweep; use Run346 region-protected B as fixed baseline. Actual baseline 500px frontal render identified eye centers (0,.23) and (.176,.238) in oriented donor world units, +Y up/+Z front. Test replacing the concave eye regions with blended locally convex corneal geometry on the same connected donor, not adding spheres or external eyeball primitives. Fit each eye rim plane from 83/113 vertices, deform only front eye region, separate eye material by face mask. B cap depth .012; C .024. Both use dark brown gradient and distinct PBR roughness .19 vs skin .90, metallic 0.

Core executed algorithm excerpt (not complete script; full local source git blob d86b9d38087b84f42473b065d6f103f4dcaa8ab6). Uses Run346 B vertices vv, colors, faces f, original v and smoothstep s; same source orientation [1,2,0].
```python
vnew=vv.copy();col=colors.copy();eye_mask=np.zeros(len(v),bool)
for cx,cy in [(0,.23),(.176,.238)]:
    dx=vv[:,0]-cx;dy=vv[:,1]-cy
    r=np.sqrt((dx/.042)**2+(dy/.033)**2);front=vv[:,2]>.10
    rim=(r>.78)&(r<1.15)&front
    X=np.c_[np.ones(len(v)),dx,dy]
    coef=np.linalg.lstsq(X[rim],vv[rim,2],rcond=None)[0]
    goal=X@coef+bulge*np.maximum(1-(r/.86)**2,0)**.5
    w=(1-s((r-.64)/.36))*front
    vnew[:,2]+=w*(goal-vv[:,2])
    dark=np.c_[22+19*np.clip(r,0,1)**2,16+13*np.clip(r,0,1)**2,12+8*np.clip(r,0,1)**2]
    cw=(1-s((r-.66)/.22))*front
    col=col*(1-cw[:,None])+dark*cw[:,None]
    eye_mask|=(r<.78)&front
sel=eye_mask[f].all(1)
```
Export submeshes as separate named skin/cornea primitives with vertex colors via TextureVisuals.vertex_attributes['color'] and PBRMaterial, then reimport scene. Both have 100534 triangles (100275 skin +259 cornea), 2012688 bytes. GLB JSON independently inspected: POSITION and COLOR_0 both present; NORMAL absent, a further rendering portability concern. VTK generated normals and Phong specular .75 for eye and .02 for skin (not GLB browser PBR render). Actual 0/45/90/180 renders for baseline/B/C, direct inspection of 1200x954 montage SHA256 44bde085d13e27e551aa318f89373737fb60c3e1cfc863f5fc0ecadf7cec53c9.

- B SHA256 863065d8250015572e741c9798d1eda90b7631f01b9f88cd11b4f5964de1f7e2; max eye-region z change .0238027/.0196123.
- C SHA256 0c2f65873eab2471e892bfc97edcb3cc9167da256588a7f0f09d2501c1f23f1b; max .0356641/.0287906.
- Tiny montage JPEG in run347-local/evidence.jpg.b64, 2047 bytes decoded SHA256 fb1baa61e4c8562014b1c567bf46947450e22fd97407f28da88e509cfdd5b9e1. Full models/source and full renders local only; this note is not a release or fully reproducible archive.

## Art gate
C gives discernibly more convex glossy eyes compared to dark holes in baseline. B has uneven catchlights; C reads as beads, not integrated natural eyelids. Side silhouette still flattened, rear is smooth ridged clay with dark base, no convincing cream down; feet indistinct. Both rejected. No browser WebGL or real phone test. Do not mistake glossy eye improvement for complete pet. No modification of main, source concept, species production or deployment. Next useful work: switch donor or actual fine groom and anatomical eyelid reconstruction, not another small eye-depth sweep.
