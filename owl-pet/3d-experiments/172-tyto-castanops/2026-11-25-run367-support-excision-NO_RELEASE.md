# Run367 — support excision, topology and cap ablation (ART_REJECTED / NO_RELEASE)
2026-11-25. Extra spend $0. Independent research branch only.

## Preflight and actual source
Read main AGENTS, README, STATUS (206/251 unique; six concept revisions completed at 17:00), #172 v3 review (cream thick mesoptile, developed mask, buried short wings, concealed tail, age unknown/science=false), and Run366 at ab1042d6a788aae46b9519420e4bcfb5b3a1f8f9. Source recovered through actual GitHub Actions artifact 14795923598; exact SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be. Inspected isolated v3 reference and historic browser front/profile/back. The model fuses toe tips and support; prior deformation did not remove material. This run tests a topological cut rather than another vertex displacement. Main snapshot 1031b99c3f02f7235db4f2c40a15d31648d7a465.

## Executed
Python/VTK/Trimesh CPU, native three-dimensional clipping of neural SF3D surface. Source 16971 vertices, 27372 triangles, y-up, negative Z faces front; minimum y=-0.40712109. The cut height increases toward posterior support and central toe gap. Two strengths, each with two different color transfer/welding methods. Four actual GLBs, reopened and rendered. First pass clips original seam-split mesh, cleans points, fills holes, triangulates, transfers nearest-three sampled vertex colors. Second pass welds exact-position UV duplicates before clipping, averages original sampled RGB, and interpolates RGB at the clipping intersection. VTK fills boundary loops, not reconstructed toe anatomy. No claim of PBR material preservation; research output vertex colors only. 20 actual offline renders at 320x320: original and four variants, each front/profile/rear/underside. Viewed two 12-view contact sheets with common control. No actual new browser/phone validation.

Core reproduction:
```python
# m = trimesh.load(SF3D_file, force='mesh',process=False)
# rgb = sample baseColorTexture using (u,1-v) at each vertex.
_,idx,inv=np.unique(np.round(m.vertices,8),axis=0,return_index=True,return_inverse=True)
acc=np.zeros((len(idx),3));np.add.at(acc,inv,rgb);acc/=np.bincount(inv)[:,None]
m=trimesh.Trimesh(m.vertices[idx],inv[m.faces],process=False)
m.fix_normals();assert m.is_watertight
rgb=np.rint(acc).astype('uint8')
# p = vtkPolyData from m vertices/faces; attach float32 RGB array source_rgb.
x,y,z=m.vertices.T
back=1/(1+np.exp(-(z+.035)/.035))
center=np.exp(-(x/.07)**2)*(1-back)
# (a,b,c) mild=(.008,.018,.012), strong=(.017,.038,.026)
signed=y-(m.bounds[0,1]+a+b*back+c*center)
pd=vtk.vtkPolyData();pd.DeepCopy(p)
pd.GetPointData().SetScalars(numpy_to_vtk(signed,deep=True))
clip=vtk.vtkClipPolyData();clip.SetInputData(pd);clip.SetValue(0);clip.Update()
clean=vtk.vtkCleanPolyData();clean.SetInputConnection(clip.GetOutputPort());clean.SetTolerance(1e-7);clean.Update()
fill=vtk.vtkFillHolesFilter();fill.SetInputConnection(clean.GetOutputPort());fill.SetHoleSize(.8);fill.Update()
tri=vtk.vtkTriangleFilter();tri.SetInputConnection(fill.GetOutputPort());tri.Update()
q=tri.GetOutput()
v=vtk_to_numpy(q.GetPoints().GetData()).copy()
f=vtk_to_numpy(q.GetPolys().GetData()).reshape(-1,4)[:,1:].copy()
vc=np.rint(vtk_to_numpy(q.GetPointData().GetArray('source_rgb'))).clip(0,255).astype('uint8')
out=trimesh.Trimesh(v,f,vertex_colors=vc,process=False);out.fix_normals()
out.export(filename)
rt=trimesh.load(filename,force='mesh',process=False)
```
| variant | vertices | triangles | bytes | boundary edges | nonmanifold | watertight | SHA256 |
|---|---:|---:|---:|---:|---:|---|---|
| mild | 13160 | 26304 | 527212 | 6 | 0 | false | 20ead8e5fc1880aa1b41c979496462a2bbec3b54cc861220b9e5ce5735db6c6a |
| strong | 12043 | 24082 | 482676 | 0 | 0 | true | ad656bf9227792a12fc44d6c75f03a05ed3e65352644fd9e24699367cdde6101 |
| weld-mild | 13160 | 26304 | 527212 | 6 | 0 | false | ab9928e0c9e2a13a3fa560033889663a0d254266207c5123307cf1e8441a1350 |
| weld-strong | 12043 | 24082 | 482676 | 0 | 0 | true | c0f2e6045353085c0be39025156c951d0a6109567cc11fc30c19ee32f8f2db20 |

Welded source 13688 vertices; 1014/2050 lie below mild/strong cut respectively. Strong clip 23681 faces before cap, 24082 after. Original signed volume 0.1400826, strong 0.1357622 (~3.08% removed). Both strong outputs consistent winding; no degenerate faces below 1e-12 area. Despite closed topology, support and toes are still fused, underside has broad non-anatomical faceted cap and all clipped variants introduce dark surface speckles. Preweld/interpolated color did not solve speckles. Exact cause not established; do not attribute to seams alone. Original disc visible but side mask protrudes and wings/down remain poor. All variants rejected. This excludes crude height-field excision as a useful standalone anatomical repair.

## Alternative route check
Read Run93 archived artist asset intake source (e6c119310966eec95f40e9b6a22c947c9b681587). It already tested adult/unverified Innerscene owl, not a suitable juvenile Tyto base. Actual curl to https://www.innerscene.com/api/library/owl-d696472a/download failed DNS code 6, as did API GitHub/Hugging Face/raw GitHub directly in local execution. Connector artifact retrieval works. CUDA false, Blender absent, VTK available. No paid invocation, no external asset acquired. Next avoid repeated single-view repair; prioritize retrieving an anatomically appropriate alternative source or coherent multiview reconstruction input. Existing source remains an experimental baseline only.

## Evidence
Local executed source SHA256: trim-v1.py d7bc93781a081e44e6e3cc96ec3d979ae4ba2b3e2bc27bd70551aedb4a7a920d; trim.py 58b233a3b07dd35ad531b0ecdfe6183120886919c6b7c970ba519c19493babbb; render.py 1dea30b44f23690f1601fc26a58c7ae095de4d7f168fd14a94e719dc4a2be6ea; metrics-v2.json de2f0fd20fba8492469dd61f955841d9a83dabdc63443dae81a26db26e56ef65; metrics.json 6a1903b49f107f7baca64d066f775c5b5d0e15953e3ceec8a174d2d825df2179. Full second contact SHA256 71eaf3b325cf1e4b32c3ac34bbf96fdce1f86e10591cbc807a5720d3da253e7d. Full model files, exact scripts and renders local to execution only; not claimed remotely durable. Tiny actual render contact JPEG 96x72 (rows control, weld-mild, weld-strong; columns front, side, rear, underside), SHA256 a1b59cdb79a273d62c053b922a8def25f5e42f6ae655095e17660b7c11fb173b, base64 below; thumbnail evidence only, not enough for art approval.
```base64
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
```

No changes to main, existing concepts, 251-species process, or deployed prototype. No release.
