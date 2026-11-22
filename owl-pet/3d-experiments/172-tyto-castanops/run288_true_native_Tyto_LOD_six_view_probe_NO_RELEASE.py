#!/usr/bin/env python3
"""Research only: reproducible native mesh optimization + real geometry QA.
This program does not sculpt a baby Tyto. Adult museum model stays ART_REJECTED.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess

import numpy as np
import requests
import trimesh
import vtk
from PIL import Image, ImageDraw
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray

OUT = Path(os.environ.get("OWL172_OUTPUT", "owl172-run288-evidence"))
OUT.mkdir(parents=True, exist_ok=True)
URL = "https://doc.ayootech.com/galeri/model/0e65de5934db4f0eae02835ba7227dcc.glb"
PINNED = "6412ffd575360397bd90d391d3d4c23397f225945cdef3ec5727bfd91504cd44"
sha = lambda b: hashlib.sha256(b).hexdigest()
r = requests.get(URL, timeout=200)
r.raise_for_status()
raw = r.content
assert raw[:4] == b"glTF" and sha(raw) == PINNED, "Invalid museum original: no unpinned inputs"
original = OUT / "reference_museum_adult_NO_RELEASE.glb"
original.write_bytes(raw)
optimized = OUT / "adult_donor_mobile_lod_ART_REJECTED_NO_RELEASE.glb"

# Geometry-only simplification and standard quantization: keep glTF material textures.
# Avoid meshopt/Draco extension here, so unextended GLTFLoader can parse it.
cmd = [
    "gltf-transform", "optimize", str(original), str(optimized),
    "--compress", "quantize", "--texture-compress", "false",
    "--simplify", "true", "--simplify-ratio", "0.42",
    "--simplify-error", "0.002"
]
with (OUT / "gltf_transform_execution.log").open("w") as log:
    subprocess.run(cmd, check=True, stdout=log, stderr=subprocess.STDOUT)

def inspect(p):
    sc = trimesh.load(p, force="scene", process=False)
    meshes = sc.dump(concatenate=False)
    count = sum(len(m.faces) for m in meshes)
    if not meshes or not count:
        raise RuntimeError(f"no real geometric data in {p}")
    return sc, meshes, {
        "bytes": p.stat().st_size,
        "sha256": sha(p.read_bytes()),
        "mesh_count": len(meshes),
        "triangles": int(count),
        "vertices": int(sum(len(m.vertices) for m in meshes)),
        "baseColorTexture_meshes": sum(bool(getattr(getattr(m.visual,"material",None),"baseColorTexture",None) is not None) for m in meshes),
    }

old_sc, old_mesh, old = inspect(original)
new_sc, meshes, new = inspect(optimized)
if not (0 < new["triangles"] < old["triangles"] and
        0 < new["bytes"] < old["bytes"] and
        new["baseColorTexture_meshes"] >= 1):
    raise RuntimeError("LOD failed: geometry, file size or actual PBR texture lost")

renderer = vtk.vtkRenderer()
window = vtk.vtkRenderWindow()
window.SetOffScreenRendering(True)
window.SetSize(440, 440)
window.AddRenderer(renderer)
for i, m in enumerate(meshes):
    if not len(m.faces):
        continue
    v = np.ascontiguousarray(m.vertices, dtype=np.float32)
    f = np.ascontiguousarray(m.faces, dtype=np.int64)
    poly = vtk.vtkPolyData()
    pts = vtk.vtkPoints()
    pts.SetData(numpy_to_vtk(v, deep=True))
    poly.SetPoints(pts)
    ca = vtk.vtkCellArray()
    offs = np.arange(0, len(f)*3 + 1, 3, dtype=np.int64)
    ca.SetData(numpy_to_vtkIdTypeArray(offs, deep=True),
               numpy_to_vtkIdTypeArray(f.reshape(-1), deep=True))
    poly.SetPolys(ca)
    uv = getattr(m.visual, "uv", None)
    tex = getattr(getattr(m.visual, "material", None), "baseColorTexture", None)
    if tex is not None and uv is not None and len(uv)==len(v):
        rgb=np.asarray(tex.convert("RGB"), dtype=np.uint8)
        H,W=rgb.shape[:2]
        coords=np.asarray(uv,dtype=float)
        uu=np.clip(((coords[:,0]%1)*(W-1)).astype(np.int64),0,W-1)
        vv=np.clip(((1-coords[:,1]%1)*(H-1)).astype(np.int64),0,H-1)
        colors=np.ascontiguousarray(rgb[vv,uu],dtype=np.uint8)
    else:
        col=getattr(getattr(m.visual,"material",None),"baseColorFactor",[.86,.79,.71,1])
        colors=np.tile(np.asarray(col[:3],dtype=float)*255,(len(v),1)).astype(np.uint8)
    vtkcols=numpy_to_vtk(colors,deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
    vtkcols.SetNumberOfComponents(3)
    poly.GetPointData().SetScalars(vtkcols)
    mapper=vtk.vtkPolyDataMapper()
    mapper.SetInputData(poly)
    mapper.SetScalarModeToUsePointData()
    mapper.SetColorModeToDirectScalars()
    actor=vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetInterpolationToPhong()
    actor.GetProperty().SetAmbient(.32)
    actor.GetProperty().SetDiffuse(.75)
    renderer.AddActor(actor)
if renderer.GetActors().GetNumberOfItems()<1:
    raise RuntimeError("zero actors: last Run287 original silent empty VTK mistake")
renderer.SetBackground(.95,.93,.89)
lamp=vtk.vtkLight()
lamp.SetLightTypeToSceneLight()
lamp.SetPosition(-2,3,4)
lamp.SetIntensity(.85)
renderer.AddLight(lamp)
lamp2=vtk.vtkLight()
lamp2.SetLightTypeToSceneLight()
lamp2.SetPosition(2,2,-3)
lamp2.SetIntensity(.45)
renderer.AddLight(lamp2)
b=renderer.ComputeVisiblePropBounds()
assert b[0]<=b[1], "empty bounds"
center=np.asarray([(b[0]+b[1])/2,(b[2]+b[3])/2,(b[4]+b[5])/2])
dist=max(b[1]-b[0],b[3]-b[2],b[5]-b[4])
camera=renderer.GetActiveCamera()
camera.SetViewAngle(33)
views=[]
contact=Image.new("RGB",(1320,920),(246,242,235))
draw=ImageDraw.Draw(contact)
for j,(name,axis,up) in enumerate([
    ("front",(0,0,1),(0,1,0)),
    ("front45",(.7,.04,.7),(0,1,0)),
    ("right",(1,0,0),(0,1,0)),
    ("back",(0,0,-1),(0,1,0)),
    ("left",(-1,0,0),(0,1,0)),
    ("top",(0,1,0),(0,0,-1)),
]):
    camera.SetPosition(*(center+2.7*dist*np.asarray(axis)))
    camera.SetFocalPoint(*center)
    camera.SetViewUp(*up)
    renderer.ResetCameraClippingRange()
    window.Render()
    flt=vtk.vtkWindowToImageFilter()
    flt.SetInput(window)
    flt.ReadFrontBufferOff()
    flt.Update()
    dest=OUT / ("optimized_TRUE_3D_"+name+".png")
    wr=vtk.vtkPNGWriter()
    wr.SetFileName(str(dest))
    wr.SetInputConnection(flt.GetOutputPort())
    wr.Write()
    frame=Image.open(dest).convert("RGB")
    px=np.asarray(frame,dtype=np.int16)
    fg=float(np.mean(np.max(np.abs(px - np.asarray([242,237,227])),axis=2)>45))
    if fg<0.008:
        raise RuntimeError(f"fake blank successful render on {name}: foreground {fg}")
    digest=sha(dest.read_bytes())
    views.append({"view":name,"sha256":digest,"foreground_fraction":fg,"bytes":dest.stat().st_size})
    x=(j%3)*440
    y=(j//3)*460
    contact.paste(frame,(x,y))
    draw.text((x+10,y+441),name,fill=(40,30,25))
if len({x["sha256"] for x in views})!=6:
    raise RuntimeError("six named screenshots are not six distinct spatial projections")
contact.save(OUT/"ACTUAL_6_DISTINCT_NATIVE_3D_CAMERAS_REFERENCE_ONLY.png")
report={
  "date":"2026-11-22",
  "target":"#172 Tyto castanops v3 RIGHTMOST baby",
  "run":"288",
  "source":"original adult Tyto alba museum scan from source model ID 0e65de5934db4f0eae02835ba7227dcc",
  "primary":"https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc",
  "license":"primary page CC0 claim; third-party mirror binary identity not certified",
  "original":old,"lod":new,"six_real_3D_cameras":views,
  "technical":"Genuine native triangulated textured glTF geometry reduced with open-source glTF-Transform; no 2D illusion",
  "art":"ART_REJECTED: adult Tyto alba skeleton, mature wing/tail; no cream-white juvenile plush groom, no old eucalyptus cavity",
  "phone":"NOT_TESTED: software VTK six-camera rendering is not mobile WebGL",
  "rights":"UNVERIFIED_SOURCE_CHAIN / research only",
  "paid_spend_usd":0,"release":False
}
(OUT/"run288_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
(OUT/"NO_RELEASE.txt").write_text("ACTUAL_NATIVE_TEXTURED_LOD / ART_REJECTED / PHONE_UNTESTED / SOURCE_RIGHTS_UNCERTAIN / NO_RELEASE\n")
# Omit the already pinned, previous-run original 43MB from the new archive.
original.unlink()
sums=[]
for p in sorted(OUT.iterdir()):
    if p.is_file() and p.name!="SHA256SUMS.txt":
        sums.append(sha(p.read_bytes())+"  "+p.name)
(OUT/"SHA256SUMS.txt").write_text("\n".join(sums)+"\n")
print(json.dumps({"gate":"TRUE_NATIVE_3D_MOBILE_FORMAT_LOD_PASS_BUT_ART_REJECTED_NO_RELEASE",
"original":old,"lod":new,"cameras":views,"evidence":str(OUT)},ensure_ascii=False))
