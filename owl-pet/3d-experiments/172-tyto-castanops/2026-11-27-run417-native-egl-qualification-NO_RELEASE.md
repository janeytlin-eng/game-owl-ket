# Run417 — native EGL GLB render qualification — ART_REJECTED / NO_RELEASE

2026-11-27. Re-read main owl-pet AGENTS, README, STATUS (207/251), main root directory, Run416 immutable record (2fb97824bfa20a4a6837d92c93de1529f8fe2d6d), and Run415 native mesh/README at 23aea7e20c09a58c10f7c76c6ba5e06274a3383e. Prior reference v3 blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b, juvenile on right: compact cream down, heart disc, dark eyes, feathered feet, no long adult tail. This run did not re-open that image independently; used previous visual record. Run415 GLB source was recovered in full via connector (blob 1d709a7108eedcda3a74009e5fabac2b965a0d23, 779732 bytes, 21622 vertices, 43240 triangles, indexed position/normal). No new paid call. No main, species production, original concept or deployment changes.

## Actual experiment
Local container has VTK 9.6.2 with EGL, GLTF importer and software OpenGL. DNS for GitHub, API GitHub and Hugging Face still returns errno -3; no Blender, bpy, model cache. Chromium 144 and Playwright present. Tested a checksum-verified small mesh transfer from the actual historical GLB rather than synthesizing primitives. Vertex clustering used a 5x5x5 grid, mean positions, remapped indices, dropped degenerate and duplicate undirected triangles; quantized each coordinate to 8 bits. 98 vertices, 187 triangles. This intentionally coarse native mesh is a transport/render fixture ONLY and cannot qualify as art. Initial 8-bin fixture transcription had 6 surplus bytes, rejected; smaller fixture below passed FNV-1a 1166441206 and 859 bytes.

Actual local export through trimesh created 4200-byte diagnostic GLB, SHA256 7e17e474ef8700b47e4f048b5b6d62ffb087484b8dfada38ed8feb461e1126e8. Chromium was launched with SwiftShader and phone-sized viewport, but navigation to the local diagnostic HTML returned net::ERR_BLOCKED_BY_ADMINISTRATOR. No WebGL or phone performance claim; did not work around the browser policy.

Executed independent VTK EGL import of actual exported GLB, obtained actor and bounds (-0.736705899,0.672588229,-0.867870569,0.851776481,-0.582078457,0.775470614). EGL 1.5 Mesa, GL 4.5 Core Mesa 25.0.7-2, llvmpipe LLVM 19.1.7 (CPU). Three actual 390x390 screenshots front, side and back, non-background pixel counts (max RGB difference from background >10): 58640, 53055, 58623. Viewed actual combined image: distinctly faceted, no eye/face/down detail; expected for a deliberately decimated transport fixture. This is a renderer qualification, not a character improvement. Future use: render full-resolution native candidates and material tests when complete assets can be transferred, not continue polishing this fixture.

## Reproduction (actual small fixture and VTK pipeline)
Save the following exact base64 as mesh.b64:
```
YgC7ABxUrhiAtg9IgASBfx8bSygifQpLTSkZrk4csUtLti55zT54yFGC108ZgTY2lkwT1GBjzYEV04Fg0H6B544cr4BFtoIfgYAOTSaoph+xgBF/TCGpTD25uzLOe0jmf1HarUTCSDXHaVOx1VTfVH+x42HNzn/Q0n/is4D4fn/lTiRNJkwOTCl8KCgcK04TH0qBEUtNEH8UG39NBoCBBC+iLk6vHYC2E2nMNoLNMKoU1qNiz7KB27Mcs7VJt7YagbMNTM0Wx79oytd5z+RSsMs0mfJJgdspeNdlze2AtOEaSuh/TPaAf7Cw2p7O0LHcrrXufrLcU8O+wdmwrtDPn9HWgcDAQM3NY9asUeGzf7MWILNNDrWCENgbKtZ7JttLJPFLS7GvHc2fLwMCAAMAAQUCBAwKAQwBCwsBAAsACQ0FBwUNCAUIBw0HCAACCQkCDg0CBQINDgwLCRAMCQ0ICQkODRIQCRIJFRMMEBMQEg0WCBYUCAgUFQgVCRQIDRQNFhYVFBkDARkBGBsaAxsDGRwYARwBCxkYHB0ZGB4ZHB4cHx4dGR4hGSAbGSAZIRwMIh8cIgsMHCAhHiMgHiQiDCQMEyUfIiYiJCYlIicfJSclJiceHygeJykjHikeKAYEAhoGAhoCAwQrDQQNBS0uKy0rBAQqLQYqBCoGGiwqGi4tKjAuKi8qLCovMCsXFisWDS4xFy4XKzAzMjMwLzAxLjIxMBo0LDQaGzQ1LC8sNSA1GzU0GykgIzcgKTY1IDYgNzY3KTg2KTMvNTYzNTsTEjsSOjoSFToVPRY+PBY8FD0UPD0VFDs6PUE7PTtDQjs9Qz08PkQ9PkRDPT5FRENHQkhCR0hHQ0NERUU+RkVLSEVIQzskE0wkO00mJE0kTE4nJk4mTU5NTE8oJ08nTlApTykoT1FOTFRPTlBPVFVQVkhMO0g7QlJRTFJMSFJOUVJTTlROU1hTUlRTWEhYUktYSEpXWEpYS1dWWFZUWFZQVFdVVhc/Phc+FjFZPzE/FzIzWjNbWjJZMVkyWllJPz9JRj9GPklfRUlFRllcSVxeX1xfSV5dSl5KX1leXFpeWVtdXlteWl9KS19LRTZVYFU2KVUpUDZgWzZbM11hV11XSl1gYVtgXWFgVWFVVw==
```
```python
from pathlib import Path
import base64, struct, numpy as np, trimesh, vtk
p=Path('.')
b=base64.b64decode((p/'mesh.b64').read_text())
h=2166136261
for x in b: h=((h^x)*16777619)&0xffffffff
assert h==1166441206 and len(b)==859
n,t=struct.unpack_from('<HH',b)
v=np.frombuffer(b[4:4+3*n],dtype=np.uint8).reshape(n,3)/255*np.array([1.485,1.866,1.525])+[-.76,-.963,-.606]
f=np.frombuffer(b[4+3*n:],dtype=np.uint8).reshape(t,3)
m=trimesh.Trimesh(vertices=v,faces=f,process=False)
(p/'diagnostic.glb').write_bytes(m.export(file_type='glb'))
w=vtk.vtkEGLRenderWindow(); w.SetOffScreenRendering(1); w.SetSize(390,390)
r=vtk.vtkRenderer(); w.AddRenderer(r);r.SetBackground(.12,.15,.18)
i=vtk.vtkGLTFImporter();i.SetFileName(str(p/'diagnostic.glb'));i.SetRenderWindow(w);i.Update()
r=w.GetRenderers().GetFirstRenderer();r.SetBackground(.12,.15,.18)
a=r.GetActors();a.InitTraversal();actor=a.GetNextActor()
actor.GetProperty().SetColor(.97,.9,.77)
cam=r.GetActiveCamera();cam.ParallelProjectionOn();cam.SetParallelScale(1.12);cam.SetFocalPoint(0,0,0);cam.SetViewUp(0,1,0)
for name,xyz in [('front',(0,0,4)),('side',(4,0,0)),('back',(0,0,-4))]:
    cam.SetPosition(*xyz);r.ResetCameraClippingRange();w.Render()
    capture=vtk.vtkWindowToImageFilter();capture.SetInput(w);capture.Update()
    writer=vtk.vtkPNGWriter();writer.SetFileName(str(p/(name+'.png')));writer.SetInputConnection(capture.GetOutputPort());writer.Write()
print(w.ReportCapabilities())
```

Decision ART_REJECTED / NO_RELEASE. No acceptable sample, no mobile WebGL validation. This establishes a genuine offline native GLB renderer and transfer method but not a solution to the juvenile sculpt/down bottleneck. Zero additional fee. 
