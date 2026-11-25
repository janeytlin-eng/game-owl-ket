# Run361 — cross-engine seam-weld and geometry-only gate
2026-11-25, Asia/Shanghai. ART_REJECTED / NO_RELEASE. No extra fee.
## Preflight
Read main owl-pet AGENTS, README, STATUS (206/251, 45 remaining), #172 v3 review and original plate listing (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b), plus Run360 at 565817390705adaa894b5f44a3a0a80caf16fd4a. Target is rightmost cream mesoptile, short buried wings, dark eyes, heart face, hidden tail, age unknown, science=false. Read Run117 and Run118 rejection records. Recover actual Run117 and Run317 artifacts through GitHub connector (IDs 14266706992 and 14795923598). Original native hashes match prior records: TRELLIS 2893e95965a9c6e6fd3af5779c1ebf3b65a16b6cdaebf7c2f743e047b9fa78de, SF3D c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be. Blender roundtrip d84e9938aaa2ab5bf23433caba6185ea568b0b369fa9ebd6ea070ecde49aa21a. No new neural inference.
## Independent alternative
https://vinish.dev/free-3d-models/birds lists a CC BY 4.0 barn owl, 52,276 triangles, 2.5 MB, foldable adult wings and six animation clips. The site describes dark eyes, spotted white breast and barred golden wings, not juvenile down. Exact native download https://vinish-models.pages.dev/birds/barn-owl.glb returned binary content-type unsupported in web reader; curl failed DNS (6) and container download failed. No bytes obtained, no visual or rig verification, no source imported. If used, retain creator credit and modification notice; adult rig is not itself target geometry. Grab3D CC0 great horned owl has ear tufts and adult feather anatomy, unsuitable as-is. CGTrader baby owl no-AI license already flagged; do not use in AI workflow. No purchased tool. Current local trimesh/VTK/torch available, Blender/bpy absent; public DNS unavailable.
## Executed new diagnostic (not a cosmetic patch)
Compare two genuinely different neural meshes without texture; distinguish UV duplication from structural cracks. Load GLB scene, apply scene transforms, copy positions/faces to untextured mesh. At each precision (8,6,4 decimal digits) weld coincident vertices, remove degenerate and duplicate faces, unreferenced vertices; count edge incidence, connected components, largest-component face share, watertightness, winding. At precision 6 export three native diagnostic GLBs and reopen. Render 8 actual VTK EGL orthographic clay views (two engines, four cardinal directions), 250x245 each; both source geometries normalized by largest dimension. No image impostor. Core code:
```python
mesh=trimesh.Trimesh(vertices=v.vertices,faces=v.faces,process=False)
mesh.merge_vertices(digits_vertex=digits)
mesh.update_faces(mesh.nondegenerate_faces())
mesh.update_faces(mesh.unique_faces())
mesh.remove_unreferenced_vertices()
count=np.bincount(mesh.edges_unique_inverse,minlength=len(mesh.edges_unique))
parts=mesh.split(only_watertight=False)
boundary=int((count==1).sum()); nonmanifold=int((count>2).sum())
mesh.export(out); re=trimesh.load(out,force='mesh',process=False)
```
## Actual results
| Source | Raw vertices | Welded vertices (6) | Faces | Boundary edges | Nonmanifold edges | Components | Watertight |
|---|---:|---:|---:|---:|---:|---:|---|
| Run117 TRELLIS native | 37475 | 20128 | 40623 | 116 | 147 | 93 | no |
| Run117 Blender roundtrip | 121851 | 20128 | 40623 | 116 | 147 | 93 | no |
| Run317 SF3D native | 16971 | 13688 | 27372 | 0 | 0 | 1 | yes |
All consistent winding. Same TRELLIS values at 8/6/4 digits, largest component 99.36% faces. SF3D same at 8/6; 4 digits 13627 vertices/27250 faces, remains closed. Raw meshes all report non-watertight, so SF3D raw result is seam-related, whereas TRELLIS defects persist after welding. This corrects the uncertainty in Run360, for the original source only. TRELLIS Blender roundtrip did not repair topology. Depth/height TRELLIS .98573378, SF3D .62221203 (includes substrate/feet; not calibrated juvenile anatomy).
Three GLBs reopened: two TRELLIS diagnostics identical 729812 bytes / SHA256 fb4f7a0af96f0c491def5240b3fb72376d44f5a768132d048295d06fc8c14758; SF3D 493516 bytes / SHA256 ff47b9f92765be3229db64f507f8a28a25db09ebf7d7e219c874c309d77fa865. Geometry-only, no material, not release assets.
## Actual visual gate
Inspected new 1000x540 clay contact: TRELLIS faces +Z and has pronounced adult wing plates, jagged cracks, scaly rear and deeply formed beak; SF3D faces -Z, continuous but shallow body, flat/back barrel, crown ridges, projecting beak and flattened feet. Removing texture confirms major shape limitations independent of color. Neither matches the intended plush juvenile; topology success is not art acceptance. Do not repeat simple recoloring or claim Blender roundtrip repairs TRELLIS. Use a separately authorized juvenile base or a different actual reconstruction engine; use this seam-aware diagnostic before material experiments. No new mobile WebGL or physical phone test; no rights clearance. 
## Evidence
Executed topology_audit.py SHA256 23d0f33dcd81cc582ac57cd9047a39d5cc4bab337886859d64a0adfb2bcd94a4; topology.json 6d02f4d8003b099a8395ad5b9d38ab60380ca53d1f6fb0c5bd71d409d154cce5; render_audit.py 48de9b5b58dbc51f0bf6055a3a84cf5128ebd51c23564b296b010971890cd666; full clay_comparison.jpg f46801bff33b433147c4e8cbc21d163cca24eaa42ddbccdabb61d405d9933a05. Full diagnostic files local to this runtime only. Source artifacts linked above by IDs for recovery. Main, original concepts, 251-species production and deployment untouched.
