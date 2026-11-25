# Run362 — SF3D shading/UV seam factorial ablation
2026-11-25 Asia/Shanghai · ART_REJECTED / NO_RELEASE · extra payment USD 0.

## Preflight
Read main owl-pet/AGENTS.md, README.md and STATUS.md (206/251, 45 remaining), #172 v3 review (cream mesoptile, short buried wings, concealed tail, dark eyes, heart disc, age unknown, science=false), and actual Run361 report at a2c2e557873851e6ce11a11fb715c69624c2baf9. Checked original plate on main: blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b. Recovered actual Run317 workflow artifact 14795923598 via GitHub connector: native SF3D GLB SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be, 1,137,108 bytes; verified hash and examined original browser front/back screenshots. Source geometry faces -Z (historical screenshots named front/back oppositely). No new neural inference.

## Actual experiment
Run361 established SF3D geometry is watertight after welding. This round tests whether the original UV-split normals and the actual baked tangent-space normal map produce the visible crown ridges or face-disc artifacts. Preserve exact original vertex positions, indices, UVs, base color and material factors. Parse binary GLB; group coincident vertices at six decimal places; calculate angle-weighted continuous surface normals; copy each group normal back to each original UV vertex, retaining seams for texture mapping. Independently toggle original normal map off/on. Do not displace vertices or invent fur. Export three diagnostic GLBs and compare original + three variants in a 2x2 factorial design. All four opened using trimesh; vertex equality and triangle count asserted. VTK 9.6.2 GLTFImporter loaded the actual PBR materials; verified normalTex present for on variants, absent for off. VTK EGL offscreen renderer, 3 scene lights, orthographic camera, 4 views per variant (front, 45-degree, profile, rear), actual PNG captures, 240x196 each. Visually inspected full 960x872 contact image.

Core executed algorithm (abridged):
```python
_, inv = np.unique(np.round(p,6),axis=0,return_inverse=True)
q=p[f]
fn=np.cross(q[:,1]-q[:,0],q[:,2]-q[:,0])
fn/=np.maximum(np.linalg.norm(fn,axis=1,keepdims=True),1e-15)
accum=np.zeros((inv.max()+1,3))
for k in range(3):
    a=q[:,(k+1)%3]-q[:,k]; b=q[:,(k+2)%3]-q[:,k]
    cos=(a*b).sum(1)/np.maximum(np.linalg.norm(a,axis=1)*np.linalg.norm(b,axis=1),1e-15)
    np.add.at(accum,inv[f[:,k]],fn*np.arccos(np.clip(cos,-1,1))[:,None])
new=accum[inv]
new/=np.maximum(np.linalg.norm(new,axis=1,keepdims=True),1e-15)
# Patch original NORMAL accessor bytes; retain UV, positions, topology.
# Remove materials[0].normalTexture only in off variants.
```

## Results
27,372 triangles, 16,971 original vertices, 13,688 positional groups, 5,955 vertices in duplicated-position groups. Original normals' angular deviation from normalized group mean: median 5.10°, p90 19.37°, p99 46.33°, max 106.34° (an angular diagnostic, not all intentional seams are errors). Original vs recomputed normals: median .0096°, p90 10.00°, p99 37.01°, max 81.38°.
| Variant | Bytes | SHA256 |
|---|---:|---|
| original normals / map off | 1137080 | cb76d3dfd5eaeccb1f0528b6cae05cb35ecf898f99e84ef73e10fdafafa485be |
| seam-aware normals / map off | 1137080 | b5c49513878ffa3f8266e4a0d3ba9437f0d92fa73de7e596f34eafdcc8ee194f |
| seam-aware normals / map on | 1137108 | 90a2a82abd7d65f64b2e3279e7fabc9c37b4ff57a0579699fddcdc888fe8a302 |

Whole-frame mean absolute RGB difference from original (8-bit channel levels, background included; not a perceptual score), front/oblique/profile/rear:
- map off: 1.959 / 1.766 / 1.280 / .960
- seam-aware normals + map off: 2.014 / 1.827 / 1.315 / .991
- seam-aware normals + map on: .203 / .157 / .109 / .091

## Visual gate
Normal-map-off yields a smoother, softer but blurrier front; retains side silhouette with long protruding beak, shallow rear body, flattened toes and dark gray-brown rear. Original and seam-aware map-on views nearly indistinguishable, with crown ridges still visible. Seam normal discontinuity is measurable but not the primary perceptual bottleneck. No variant is a satisfactory juvenile; no natural shoulder wings or cream down volume. Do not repeat seam-normal smoothing as a route to artistic acceptance; prioritize a genuinely different juvenile mesh or reconstruction engine. No new mobile WebGL or physical phone test; rights not cleared.

## Zero-extra-cost alternatives
Current local environment: trimesh, VTK/EGL, torch CPU available; CUDA false; Blender/bpy absent; Chromium and Xvfb present. getent hosts huggingface.co github.com returned no host records. Fresh research: https://github.com/Stability-AI/stable-point-aware-3d supports point-cloud conditioning to address unseen backside, but remains dependent on obtaining model weights and a working environment; not newly downloaded or executed. https://github.com/lightningpixel/modly requires local GPU; https://github.com/senacula/senacula-shapestudio advertises CPU but previously investigated TripoSR path. https://sketchfab.com/3d-models/barn-owltyto-alba-af3cdd38e029430d9c131370ebf1bb33 lists CC BY and 760 triangles; likely too sparse for target down morphology, not downloaded or visually verified. No billable request submitted.

## Evidence
Executed normal_audit.py SHA256 71e806e6dc9ee57a4bbaef41d7ab81a47c83a1073e15fc82956b5b5dcf20c33d; normal_audit.json 8b18f5779fd2de1a2111abddf9a2f6e3eacafe8327eb296ab4cb98e606cc69df; full normal_audit_contact.jpg d7380252322bb7d4676ebfc9d88e54a061e6c0bfea97020566c03fb0f185dcf2. Full source, diagnostic GLBs and full render contact local to this run only. Original source recoverable through workflow artifact above. Tiny actual render contact archived separately as base64 (192x174, for evidence only, not quality evaluation). No main, 251-species production, source concept or deployment changes.
