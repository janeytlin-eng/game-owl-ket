#!/usr/bin/env python3
"""Run268: independent CPU-only Hunyuan3D-2mini neural geometry feasibility.
Never publish this output as pet art; research-only under Tencent license.
Input is the SHA256-verified #172 cleaned rightmost juvenile reference.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback
import numpy as np

OUT = Path(os.environ.get("OWL172_OUTPUT", "run268-evidence")).resolve()
OUT.mkdir(parents=True, exist_ok=True)
report = {"run": "268", "subject": "#172 Tyto castanops v3 rightmost juvenile",
          "release": False, "art_status": "UNREVIEWED", "phone_status": "UNTESTED",
          "licensing": "TENCENT HUNYUAN NON-COMMERCIAL LICENSE; NO_REUSE_OR_PUBLIC_RELEASE",
          "phases": [], "cpu_only": True}
START=time.monotonic()
def phase(name, **details):
    value={"name":name,"elapsed_s":round(time.monotonic()-START,2),**details}
    report["phases"].append(value)
    print("RUN268_STAGE "+json.dumps(value,ensure_ascii=False),flush=True)
    (OUT/"machine-report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
def sha(b):
    return hashlib.sha256(b).hexdigest()

def render_views(mesh):
    import vtk
    from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray
    verts=np.asarray(mesh.vertices,dtype=np.float64)
    faces=np.asarray(mesh.faces,dtype=np.int64)
    poly=vtk.vtkPolyData()
    points=vtk.vtkPoints()
    points.SetData(numpy_to_vtk(verts,deep=1))
    poly.SetPoints(points)
    arr=np.column_stack([np.full(len(faces),3),faces]).astype(np.int64)
    cells=vtk.vtkCellArray()
    cells.SetCells(len(faces),numpy_to_vtkIdTypeArray(arr.ravel(),deep=1))
    poly.SetPolys(cells)
    norms=vtk.vtkPolyDataNormals()
    norms.SetInputData(poly)
    norms.SetFeatureAngle(60)
    norms.SplittingOff()
    mapper=vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(norms.GetOutputPort())
    actor=vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(.95,.87,.76)
    actor.GetProperty().SetInterpolationToPhong()
    actor.GetProperty().SetSpecular(.08)
    ren=vtk.vtkRenderer()
    ren.SetBackground(.76,.78,.82)
    ren.AddActor(actor)
    rw=vtk.vtkRenderWindow()
    rw.SetOffScreenRendering(1)
    rw.SetSize(600,600)
    rw.AddRenderer(ren)
    center=verts.mean(axis=0)
    extent=np.ptp(verts,axis=0)
    r=float(max(extent))*2.7
    camera=ren.GetActiveCamera()
    views={"x_plus":(1,0,.15),"x_minus":(-1,0,.15),
           "y_plus":(0,1,.15),"y_minus":(0,-1,.15),
           "z_plus":(.15,0,1),"z_minus":(.15,0,-1)}
    hashes={}
    for name,v in views.items():
        cam=np.asarray(v,dtype=float)
        cam/=np.linalg.norm(cam)
        camera.SetPosition(*(center+cam*r))
        camera.SetFocalPoint(*center)
        camera.SetViewUp(*( (0,0,1) if abs(cam[2])<.8 else (0,1,0) ))
        camera.SetClippingRange(.01,100)
        ren.ResetCameraClippingRange()
        rw.Render()
        wi=vtk.vtkWindowToImageFilter()
        wi.SetInput(rw); wi.Update()
        writer=vtk.vtkPNGWriter()
        dst=OUT/("view_"+name+"_NATIVE_UNREVIEWED.png")
        writer.SetFileName(str(dst))
        writer.SetInputConnection(wi.GetOutputPort())
        writer.Write()
        hashes[name]=sha(dst.read_bytes())
    rw.Finalize()
    return hashes

try:
    from PIL import Image
    import torch
    import trimesh
    source=Path(sys.argv[1])
    raw=source.read_bytes()
    expected="9413b2b017001462f330fead80dd261100235975878b937c952d25984aba4540"
    if sha(raw)!=expected:
        raise ValueError("INPUT_SHA256_MISMATCH; refusing inference")
    img=Image.open(source).convert("RGBA")
    phase("source_verified",sha256=sha(raw),size=img.size,upstream=os.environ.get("UPSTREAM_COMMIT","unrecorded"))
    torch.set_num_threads(2)
    from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline
    phase("imports_ready",torch=torch.__version__,device="cpu")
    pipe=Hunyuan3DDiTFlowMatchingPipeline.from_pretrained(
        "tencent/Hunyuan3D-2mini",
        subfolder="hunyuan3d-dit-v2-mini-turbo",
        device="cpu",dtype=torch.float32,variant="fp16",use_safetensors=True)
    phase("weights_loaded",model="hunyuan3d-dit-v2-mini-turbo")
    generator=torch.Generator(device="cpu").manual_seed(172268)
    results=pipe(image=img,num_inference_steps=5,octree_resolution=128,
       num_chunks=4000,mc_algo="mc",generator=generator,enable_pbar=True)
    mesh=results[0]
    if mesh is None or not len(mesh.faces):
        raise ValueError("NEURAL_INFERENCE_RETURNED_NO_MESH")
    mesh.fix_normals()
    # Deliberately untextured: geometric feasibility only, never label as a finished owl.
    mesh.visual.vertex_colors=np.repeat(np.array([[237,216,190,255]],dtype=np.uint8),len(mesh.vertices),axis=0)
    dst=OUT/"hunyuan_mini_cpu_native_UNREVIEWED_NO_RELEASE.glb"
    mesh.export(dst)
    loaded=trimesh.load(dst,force="scene")
    assert len(loaded.geometry)>0 and dst.read_bytes()[:4]==b"glTF"
    phase("native_glb_created",path=dst.name,bytes=dst.stat().st_size,
          sha256=sha(dst.read_bytes()),vertices=len(mesh.vertices),
          triangles=len(mesh.faces),watertight=bool(mesh.is_watertight),
          extents=np.asarray(mesh.extents).round(4).tolist())
    view_hashes=render_views(mesh)
    phase("true_spatial_render_complete",views=view_hashes,
          distinct=len(set(view_hashes.values())))
    report["geometry_status"]="NATIVE_TRUE_3D"
except BaseException as exc:
    report["fatal_error"]=repr(exc)
    report["traceback"]=traceback.format_exc()
    phase("failed",error=repr(exc))
    raise
finally:
    report["wall_seconds"]=round(time.monotonic()-START,2)
    report["release"]=False
    (OUT/"machine-report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
    (OUT/"NO_RELEASE.flag").write_text(
        "ART_UNREVIEWED; NOT_A_QUALIFIED_PET; PHONE_UNTESTED; LICENSE_NOT_CLEARED; NO_RELEASE\n")
