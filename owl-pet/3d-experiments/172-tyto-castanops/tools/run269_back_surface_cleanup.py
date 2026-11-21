#!/usr/bin/env python3
"""Run269 isolated research: prune neural debris, selectively soften the true rear shell,
and reduce triangles for a future mobile candidate. NOT an accepted character design.
Parent: verified #172 Run268 Hunyuan3D-2mini CPU native mesh.
Third-party noncommercial usage restrictions remain. Do not deploy these outputs.
"""
import os, json, time, hashlib
from pathlib import Path
import numpy as np
import trimesh
import vtk
from vtk.util.numpy_support import numpy_to_vtk, vtk_to_numpy, numpy_to_vtkIdTypeArray

START = time.time()
OUT = Path(os.environ["OWL172_OUTPUT"])
OUT.mkdir(parents=True, exist_ok=True)
SRC = Path(os.environ["OWL172_INPUT"])
EXPECTED = "b6004b868b8608bb3b1e9a489778de33e3fc1673a856b67824bb200ba5975b8b"

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

assert sha(SRC) == EXPECTED, "REFUSE_UNKNOWN_MESH"
raw = trimesh.load(SRC, force="mesh")
assert len(raw.faces) == 145860
parts = sorted(raw.split(only_watertight=False), key=lambda m: len(m.faces), reverse=True)
main = parts[0]
assert len(parts) >= 100 and len(main.faces) > 130000 and main.is_watertight

def vtkpoly(mesh):
    p = vtk.vtkPolyData()
    points = vtk.vtkPoints()
    points.SetData(numpy_to_vtk(np.asarray(mesh.vertices, dtype=np.float64), deep=True))
    p.SetPoints(points)
    conn = np.column_stack([np.full(len(mesh.faces), 3, dtype=np.int64), mesh.faces.astype(np.int64)]).ravel()
    cells = vtk.vtkCellArray()
    cells.SetCells(len(mesh.faces), numpy_to_vtkIdTypeArray(conn, deep=True))
    p.SetPolys(cells)
    return p

smooth_filter = vtk.vtkWindowedSincPolyDataFilter()
smooth_filter.SetInputData(vtkpoly(main))
smooth_filter.SetNumberOfIterations(24)
smooth_filter.SetPassBand(.08)
smooth_filter.BoundarySmoothingOn()
smooth_filter.FeatureEdgeSmoothingOff()
smooth_filter.NormalizeCoordinatesOn()
smooth_filter.Update()
all_smooth = vtk_to_numpy(smooth_filter.GetOutput().GetPoints().GetData()).copy()
assert all_smooth.shape == main.vertices.shape
# Front face (towards +Z) stays identical to the real neural source.
z = np.asarray(main.vertices)[:, 2]
t = np.clip((.12 - z) / .70, 0, 1)
w = t * t * (3 - 2 * t)
new_vertices = main.vertices * (1 - w[:, None]) + all_smooth * w[:, None]
smooth = trimesh.Trimesh(vertices=new_vertices, faces=main.faces, process=False)
assert len(smooth.faces) == len(main.faces) and smooth.is_watertight
smooth.fix_normals()
smooth.visual.vertex_colors = np.tile([237, 216, 190, 255], (len(smooth.vertices), 1))
smooth_glb = OUT / "run269_island_pruned_back_smooth_TRUE3D_ART_REJECTED_NO_RELEASE.glb"
smooth.export(smooth_glb)
# True mesh simplification; not conversion into a photo plane or primitive.
dec = vtk.vtkQuadricDecimation()
dec.SetInputData(vtkpoly(smooth))
dec.SetTargetReduction(.55)
dec.VolumePreservationOn()
dec.Update()
red = dec.GetOutput()
v = vtk_to_numpy(red.GetPoints().GetData()).copy()
f = vtk_to_numpy(red.GetPolys().GetConnectivityArray()).reshape(-1, 3).copy()
mobile = trimesh.Trimesh(vertices=v, faces=f, process=False)
mobile.fix_normals()
mobile.visual.vertex_colors = np.tile([237, 216, 190, 255], (len(mobile.vertices), 1))
mobile_glb = OUT / "run269_reduced_55percent_TRUE3D_ART_REJECTED_NO_RELEASE.glb"
mobile.export(mobile_glb)

def render(mesh, label):
    normals = vtk.vtkPolyDataNormals()
    normals.SetInputData(vtkpoly(mesh))
    normals.SplittingOff()
    normals.SetFeatureAngle(90)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(normals.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(.96, .89, .80)
    actor.GetProperty().SetInterpolationToPhong()
    actor.GetProperty().SetSpecular(.13)
    ren = vtk.vtkRenderer()
    ren.AddActor(actor)
    ren.SetBackground(.77, .79, .83)
    rw = vtk.vtkRenderWindow()
    rw.SetOffScreenRendering(1)
    rw.SetSize(620, 620)
    rw.AddRenderer(ren)
    camera = ren.GetActiveCamera()
    center = np.array(mesh.bounds.mean(axis=0))
    pos = {"front":(0,0,1), "threequarter":(.7,0,1), "right":(1,0,0),
           "back":(0,0,-1), "left":(-1,0,0), "above":(0,1,.3)}
    hashes = {}
    for name, direction in pos.items():
        direction = np.array(direction, dtype=float)
        direction /= np.linalg.norm(direction)
        camera.SetPosition(*(center + 4.4 * direction))
        camera.SetFocalPoint(*center)
        camera.SetViewUp(*([0,1,0] if abs(direction[1]) < .9 else [0,0,-1]))
        camera.ParallelProjectionOn()
        camera.SetParallelScale(1.2)
        ren.ResetCameraClippingRange()
        rw.Render()
        wi = vtk.vtkWindowToImageFilter()
        wi.SetInput(rw)
        wi.Update()
        fn = OUT / ("view_" + label + "_" + name + ".png")
        writer = vtk.vtkPNGWriter()
        writer.SetFileName(str(fn))
        writer.SetInputConnection(wi.GetOutputPort())
        writer.Write()
        hashes[name] = sha(fn)
    rw.Finalize()
    return hashes

a = render(smooth, "smooth")
b = render(mobile, "mobile")
report = {
    "run":269, "source_run268_sha256":EXPECTED,
    "original_triangles":len(raw.faces), "component_count":len(parts),
    "removed_components":len(parts)-1,
    "removed_island_triangles":int(len(raw.faces)-len(main.faces)),
    "largest_component_triangles":len(main.faces),
    "largest_component_watertight":bool(main.is_watertight),
    "smoothing":{"vertices_moved_over_0.0005":int(np.sum(np.linalg.norm(new_vertices-main.vertices,axis=1)>.0005)),
                 "max_displacement":float(np.max(np.linalg.norm(new_vertices-main.vertices,axis=1))),
                 "unchanged_front_vertices":int(np.sum(w == 0)),
                 "method":"vtkWindowedSinc 24 iterations/.08 passband blended on -Z backside"},
    "reduced_mesh":{"triangles":len(mobile.faces), "vertices":len(mobile.vertices),
                    "watertight":bool(mobile.is_watertight)},
    "versions":{p.name:{"size_bytes":p.stat().st_size,"sha256":sha(p)} for p in [smooth_glb,mobile_glb]},
    "views":{"smooth":a,"mobile":b},
    "distinct_view_image_digests":len(set([*a.values(),*b.values()])),
    "status":"ART_REJECTED / SOFTWARE_WEBGL_UNTESTED / PHONE_HARDWARE_UNTESTED / RIGHTS_UNCLEARED / NO_RELEASE",
    "elapsed_seconds":round(time.time()-START,2)
}
(OUT/"machine-report.json").write_text(json.dumps(report,indent=2))
(OUT/"NO_RELEASE.flag").write_text(report["status"]+"\nTencent noncommercial source; never publish as a pet.\n")
print("RUN269_RESULT",json.dumps(report,ensure_ascii=False),flush=True)
