# Run363 — posterior signed-distance remesh + barycentric color transfer
2026-11-25 Asia/Shanghai. ART_REJECTED / NO_RELEASE. Extra payment USD 0.

## Preflight
Read main owl-pet AGENTS, README, STATUS (206/251, 45 remaining), #172 v3 review (thick cream mesoptile, developed heart disc, dark eyes, short buried wings, concealed tail, exact age unknown, science=false); fetched source concept main blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b. Read Run362 at 2009b1fa9e6e61b1b97a7eaa26dfae778bc88cc3: normal and shading repair insufficient. Recovered actual Run317 workflow artifact 14795923598; source GLB SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be. Inspected isolated juvenile reference and original browser front (historically labeled back). No new neural inference.

## Actual experiment
Instead of deforming existing UV-split vertices, reconstruct a continuous implicit solid from actual SF3D geometry with voxel filling, signed Euclidean distance, region-dependent Gaussian filtering, marching cubes and closest-triangle barycentric transfer of original 1024x1024 base color. This tests whether genuine remeshing can remove posterior ridges without destroying reference-facing morphology. No invented wing meshes. Front faces -Z. Pitch .006; padded grid 117x156x101, origin (-.348,-.438,-.312). Two posterior sigma values 1.8 and 3.4 voxels, front sigma .7; smoothstep across z from -.04 to .20. Control converts original UV base color into vertex RGB with original geometry, no normal map; comparisons all vertex RGB, not original PBR, so appearance cannot be compared to PBR as an isolated geometry effect.

Core executed code:
```python
vox=m.voxelized(.006).fill()
occ=np.pad(vox.matrix,5)
origin=vox.transform[:3,3]-.006*5
sdf=(distance_transform_edt(occ)-distance_transform_edt(~occ))*.006
z=origin[2]+np.arange(occ.shape[2])*.006
w=np.clip((z+.04)/.24,0,1); w=(w*w*(3-2*w))[None,None,:]
field=gaussian_filter(sdf,.7)*(1-w)+gaussian_filter(sdf,sigma)*w
v,f,_,_=marching_cubes(field,level=0,spacing=(.006,)*3)
v+=origin
mesh=trimesh.Trimesh(vertices=v,faces=f,process=False)
mesh.fix_normals()
# vtkStaticCellLocator.FindClosestPoint for each new vertex;
# compute barycentric weights on source triangle and interpolate UV,
# bilinearly sample original texture, then export native vertex-color GLB.
```

## Measurements
All 3 exported GLBs actually reopened with trimesh. Control retains UV split seams (reported watertight=false, prior Run361 positional welding verified true); both new geometries watertight without seam welding.
| Variant | vertices | triangles | volume (source units^3) | bytes | SHA256 |
|---|---:|---:|---:|---:|---|
| control | 16971 | 27372 | .140083 | 601004 | 969178dba8d4a81799483b8e0468dee7c187c0216fd1c3f93b4fdbed8bc18e0b |
| rear-soft | 65192 | 130380 | .146205 | 2608640 | 8cd84a5070f65cc1597192d73236971ed41c84578332b5c2d721de34afe44c7b |
| rear-strong | 65020 | 130036 | .145754 | 2601760 | abbbcdc7311e984f36b63ca8d28e952d35d89947e57ddea0066059a757e8b9c5 |

Rendered 12 actual 3D views with VTK offscreen (260x240 each, 3 lights, same orthographic camera front/45/profile/back). Inspected full 1040x780 contact. Posterior surface looks smoother, but front and side show new pronounced voxel-contour stripes and small dark sampling defects; front heart disc survives but eyes and beak remain unnatural, feet flattened and back unstructured brown. Neither variant achieves natural cream down or buried shoulder wings. Triangle count rises 4.75x without meaningful visual improvement. Reject all, including control. No mobile WebGL test or physical phone test for this round. Do not continue this particular voxel resolution/filter combination or mistake watertightness for visual quality.

## Free route investigation
Current environment: trimesh 4.11.1, VTK, scipy, skimage, torch CPU; CUDA unavailable, Blender/bpy absent; getent hosts github.com huggingface.co grab3d.com returned no host records. New catalog lead https://grab3d.com/models/animals/owl/ advertises CC0, 800k/400k triangle great horned owl, 31 MB full GLB, no rig. Wrong species/adult horn tufts and yellow iris; not appropriate as juvenile base, not downloaded. https://github.com/Yaromir-Anokhin/MeshForge3D advertises free offline core but explicitly uses TripoSR, previously rejected; not a different reconstruction engine. Prior free SPAR3D/asset access barriers remain. No external billable submission or spending.

## Evidence
Full execution remesh.py SHA256 f71fed3dd513340e0b54cde2ffb98b3014141f49dd9325402c8b7233f87623dc; report.json d69b4a0e6fa2de4395a5307227788748b09a9a742eda127b5ab36a2d4278d764; full contact.jpg 5d2da4b4df2fe52ddbcfbf88c0cec6c162784dc3fa4786525807ba99c4c98c90. Full code, GLBs and images are local to this execution; original recoverable via artifact. Tiny real-render contact embedded below as base64 JPEG (140x105, SHA256 5ebba84caac1932dbce878f799d7436490bb85e77a298c773c4982e64cb07211; evidence only, not adequate for artistic review). No main, source concept, 251 species production or deployment modifications.

```base64
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
```
