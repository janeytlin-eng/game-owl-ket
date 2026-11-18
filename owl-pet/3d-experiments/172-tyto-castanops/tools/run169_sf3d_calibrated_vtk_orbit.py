#!/usr/bin/env python3
"""Run169: real GLB texture-atlas-calibrated orbit inspection (VTK CPU/EGL). NO_RELEASE."""
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
import trimesh
import vtk
from PIL import Image, ImageDraw

if "--" not in sys.argv:
    raise SystemExit("Use: python run169...py -- MODEL.glb OUT_DIRECTORY")
model_s, output_s = sys.argv[sys.argv.index("--") + 1:][:2]
model = Path(model_s).resolve()
out = Path(output_s).resolve()
out.mkdir(parents=True, exist_ok=True)
EXPECTED = "8ff7341725e4fc27caf3ff4dbb3b07fe9231a96d216de31317bddf2aa07a7b8b"
digest = hashlib.sha256(model.read_bytes()).hexdigest()
if digest != EXPECTED or model.read_bytes()[:4] != b"glTF":
    raise RuntimeError("Run165 generated owl GLB source SHA/format mismatch; refuse")
scene = trimesh.load(str(model), force="scene", process=False)
if len(scene.geometry) != 1:
    raise RuntimeError("Unexpected number of meshes for source-bound GLB")
mesh = next(iter(scene.geometry.values()))
if len(mesh.faces) < 1000 or not hasattr(mesh.visual, "uv"):
    raise RuntimeError("Unexpected topology or missing texture UV")
uv_centers = mesh.visual.uv[mesh.faces].mean(axis=1)
# The ORIGINAL baked atlas visibly has the frontal face in lower-left quadrant,
# x [0,.33], raster image y [.70,1.0] => glTF UV v [0,.30].
# This is a source-specific texture registration, not an assumption about universal GLB axes.
face_mask = (uv_centers[:, 0] < .33) & (uv_centers[:, 1] < .30)
face_triangles = int(face_mask.sum())
if face_triangles < 1000:
    raise RuntimeError("Source face UV patch lost; cannot identify anatomical front")
face_normal = mesh.face_normals[face_mask].mean(axis=0)
face_normal /= max(np.linalg.norm(face_normal), 1e-9)
if face_normal[2] > -.60:
    raise RuntimeError("Negative-Z face direction not confirmed: " + str(face_normal))
tex = getattr(mesh.visual.material, "baseColorTexture", None)
if tex is None:
    raise RuntimeError("Missing source color atlas")
tex.save(out / "run169_source_basecolor_atlas.png")
metrics = {
    "run": 169, "source": model.name, "source_sha256": digest,
    "source_bytes": model.stat().st_size,
    "mesh_count": len(scene.geometry), "vertex_count": len(mesh.vertices),
    "triangle_count": len(mesh.faces), "uv": True,
    "atlas_size": list(tex.size),
    "atlas_frontal_patch_faces": face_triangles,
    "atlas_frontal_patch_mean_normal": [float(v) for v in face_normal],
    "orientation_note": "Front identified by source atlas UV patch and mesh normal; -Z faces camera; +Y upright",
    "native_format": "GLB 2; actual 3D mesh, NOT SVG",
    "mobile_physical_gpu": "NOT_TESTED",
    "release": False, "art_decision": "UNREVIEWED_PENDING_RENDER_INSPECTION",
}
(out / "run169_native_geometry_metrics.json").write_text(json.dumps(metrics, indent=2))

window = vtk.vtkRenderWindow()
window.SetOffScreenRendering(1)
window.SetSize(640, 640)
window.SetMultiSamples(0)
imp = vtk.vtkGLTFImporter()
imp.SetFileName(str(model))
imp.SetRenderWindow(window)
imp.Update()
renderer = imp.GetRenderer()
renderer.SetBackground(.14, .16, .19)
renderer.SetBackground2(.21, .23, .26)
renderer.GradientBackgroundOn()
bounds = [1e6,-1e6,1e6,-1e6,1e6,-1e6]
actors = renderer.GetActors()
actors.InitTraversal()
actor_count = 0
while True:
    a = actors.GetNextActor()
    if a is None:
        break
    bb = a.GetBounds()
    if bb:
        for i in range(3):
            bounds[2*i] = min(bounds[2*i], bb[2*i])
            bounds[2*i+1] = max(bounds[2*i+1], bb[2*i+1])
    # Avoid dark unlit PBR face: register camera-facing area lighting and broad ambient.
    a.GetProperty().SetAmbient(.65)
    a.GetProperty().SetDiffuse(.55)
    a.GetProperty().SetSpecular(0.0)
    actor_count += 1
if not actor_count:
    raise RuntimeError("GLTF importer produced no real mesh actors")
center = np.array([(bounds[2*i] + bounds[2*i+1]) / 2.0 for i in range(3)])
span = max(bounds[2*i+1] - bounds[2*i] for i in range(3))
renderer.RemoveAllLights()
key = vtk.vtkLight()
key.SetLightTypeToSceneLight()
renderer.AddLight(key)
fill = vtk.vtkLight()
fill.SetLightTypeToSceneLight()
renderer.AddLight(fill)
camera = renderer.GetActiveCamera()
camera.ParallelProjectionOn()
camera.SetParallelScale(span * .78)
views = [
    ("front_negZ", (0,.1,-1)),
    ("front_oblique_posX_negZ",(1,.1,-1)),
    ("side_posX",(1,.1,0)),
    ("back_posZ",(0,.1,1)),
    ("side_negX",(-1,.1,0)),
    ("underside_negY",(0,-1,-.15)),
]
images = []
for name, vec in views:
    v = np.array(vec, dtype=float)
    v /= np.linalg.norm(v)
    camera.SetPosition(*(center+v*span*3))
    camera.SetFocalPoint(*center)
    camera.SetViewUp(*(np.array([0,0,1]) if abs(v[1])>.85 else np.array([0,1,0])))
    renderer.ResetCameraClippingRange()
    key.SetPosition(*(center+v*span*2.5))
    key.SetFocalPoint(*center)
    key.SetIntensity(1.8)
    fill.SetPosition(*(center+v*span*1.5+np.array([.2,.2,.2])*span))
    fill.SetFocalPoint(*center)
    fill.SetIntensity(.6)
    window.Render()
    frame = vtk.vtkWindowToImageFilter()
    frame.SetInput(window)
    frame.SetInputBufferTypeToRGB()
    frame.ReadFrontBufferOff()
    frame.Update()
    dest = out / ("run169_"+name+"_UNREVIEWED.png")
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(str(dest))
    writer.SetInputConnection(frame.GetOutputPort())
    writer.Write()
    if not dest.exists() or dest.stat().st_size < 20000:
        raise RuntimeError("Missing real rendered view: " + name)
    images.append((name,dest))
window.Finalize()
contact = Image.new("RGB", (1440, 1040), "white")
draw = ImageDraw.Draw(contact)
for i,(name,imgpath) in enumerate(images):
    img = Image.open(imgpath).convert("RGB").resize((480,480))
    x,y = (i%3)*480,(i//3)*520
    contact.paste(img, (x,y))
    draw.text((x+12,y+485), name, fill="black")
contact.save(out/"run169_sixview_lit_contact_UNREVIEWED.png")
metrics["rendered_views"] = [{"name":name,"file":p.name,"bytes":p.stat().st_size,
    "sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for name,p in images]
metrics["vtk_version"] = vtk.vtkVersion.GetVTKVersion()
metrics["actor_count"] = actor_count
metrics["bounds"] = [float(v) for v in bounds]
(out/"run169_native_geometry_metrics.json").write_text(json.dumps(metrics,indent=2))
print("RUN169_FACE_CALIBRATED_REAL_GLB_SIXVIEW_COMPLETE",json.dumps({
    k:metrics[k] for k in ("source_sha256","triangle_count","atlas_frontal_patch_faces","actor_count","vtk_version")}))
