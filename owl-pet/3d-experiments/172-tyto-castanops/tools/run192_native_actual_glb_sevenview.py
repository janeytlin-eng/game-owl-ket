#!/usr/bin/env python3
"""Run192: independent real 3D seven-camera geometry QA of source-bound GLBs.
No artificial shapes, no stock files, no subjective acceptance and no release.
"""
import json, hashlib, pathlib, math
from datetime import datetime, timezone
BASE=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=BASE/"research-evidence-run192-HI3D-HUNYUAN-ANONYMOUS-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)
FILES=sorted(OUT.glob("run192_*actual_new_source_QUARANTINED.glb"))
REFERENCE=BASE/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
PHOTO_HASH="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
assert hashlib.sha256(REFERENCE.read_bytes()).hexdigest()==PHOTO_HASH
REG=BASE/"known_rejected_asset_sha256_registry.json"
assert REG.exists()
known=REG.read_text()
results=[]
if not FILES:
    (OUT/"run192_native_geometry_status.txt").write_text("NO_NEW_NATIVE_GLB; no geometry rendered or approved.\n")
else:
    import numpy as np, vtk, trimesh
    from PIL import Image, ImageDraw
    from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray
    for i,glb in enumerate(FILES):
        digest=hashlib.sha256(glb.read_bytes()).hexdigest()
        r={"name":glb.name,"sha256":digest,"bytes":glb.stat().st_size,
           "source_reference_sha256":PHOTO_HASH,"timestamp_utc":datetime.now(timezone.utc).isoformat(),
           "known_rejected_asset":digest in known,"release":False,"art_approved":False,
           "physical_phone_gpu_tested":False}
        if digest in known:
            r["status"]="ALREADY_REJECTED_SKIP";results.append(r);continue
        scene=trimesh.load(str(glb),force="scene",process=False)
        mesh=scene.dump(concatenate=True)
        r.update({"vertices":int(len(mesh.vertices)),"triangles":int(len(mesh.faces)),
                  "extents":mesh.extents.tolist(),"watertight":bool(mesh.is_watertight),
                  "is_volume":bool(mesh.is_volume)})
        if len(mesh.faces)<1000 or len(mesh.vertices)<1000 or min(mesh.extents)<1e-5:
            r["status"]="DEGENERATE_NATIVE_MESH_ART_REJECTED";results.append(r);continue
        points=vtk.vtkPoints();points.SetData(numpy_to_vtk(mesh.vertices.astype("float64"),deep=True))
        indices=np.column_stack((np.full(len(mesh.faces),3,dtype=np.int64),mesh.faces)).astype("int64")
        cells=vtk.vtkCellArray()
        cells.SetCells(len(mesh.faces),numpy_to_vtkIdTypeArray(indices.ravel(),deep=True))
        poly=vtk.vtkPolyData();poly.SetPoints(points);poly.SetPolys(cells)
        normals=vtk.vtkPolyDataNormals();normals.SetInputData(poly)
        normals.ComputePointNormalsOn();normals.SplittingOff();normals.Update()
        mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(normals.GetOutputPort())
        actor=vtk.vtkActor();actor.SetMapper(mapper)
        actor.GetProperty().SetColor(.85,.81,.74)
        actor.GetProperty().SetInterpolationToPBR()
        actor.GetProperty().SetMetallic(0.0);actor.GetProperty().SetRoughness(.85)
        renderer=vtk.vtkRenderer();renderer.SetBackground(.955,.95,.945);renderer.AddActor(actor)
        renderer.AutomaticLightCreationOff()
        for position,power in [((3,4,6),1.2),((-4,2,-3),.8),((0,-3,2),.45)]:
            l=vtk.vtkLight();l.SetLightTypeToSceneLight();l.SetPosition(*position)
            l.SetFocalPoint(0,0,0);l.SetIntensity(power);renderer.AddLight(l)
        rw=vtk.vtkRenderWindow();rw.SetOffScreenRendering(True);rw.SetSize(520,520)
        rw.SetMultiSamples(0);rw.AddRenderer(renderer)
        centre=mesh.bounds.mean(axis=0);span=float(max(mesh.extents));distance=span*3.3
        views=[("front_posZ",(0,0,1)),("side_posX",(1,0,0)),("back_negZ",(0,0,-1)),
               ("side_negX",(-1,0,0)),("top_posY",(0,1,0)),
               ("underside_negY",(0,-1,0)),("quarter",(0.7,.45,1))]
        frames=[]; viewfiles=[]
        for label,axis in views:
            xyz=np.array(axis,dtype=float);xyz/=np.linalg.norm(xyz)
            cam=renderer.GetActiveCamera();cam.SetFocalPoint(*centre)
            cam.SetPosition(*(centre+distance*xyz))
            cam.SetViewUp(*((0,0,1) if abs(xyz[1])>.85 else (0,1,0)))
            cam.ParallelProjectionOn();cam.SetParallelScale(span*.86)
            renderer.ResetCameraClippingRange();rw.Render()
            filt=vtk.vtkWindowToImageFilter();filt.SetInput(rw)
            filt.ReadFrontBufferOff();filt.Update()
            filename=f"run192_native_{i}_{label}.png"
            writer=vtk.vtkPNGWriter();writer.SetInputConnection(filt.GetOutputPort())
            writer.SetFileName(str(OUT/filename));writer.Write()
            assert (OUT/filename).stat().st_size>4000, "failed 3D camera render"
            img=Image.open(OUT/filename).convert("RGB")
            ImageDraw.Draw(img).text((12,12),label,fill=(20,20,20))
            frames.append(img);viewfiles.append(filename)
        montage=Image.new("RGB",(4*520,2*520),(255,255,255))
        for k,img in enumerate(frames):montage.paste(img,((k%4)*520,(k//4)*520))
        montage.save(OUT/f"run192_native_{i}_sevenview_CONTACT.png")
        r["view_files"]=viewfiles;r["status"]="REAL_NATIVE_SEVEN_VIEW_ART_UNREVIEWED_NO_RELEASE"
        results.append(r)
(OUT/"run192_native_metrics.json").write_text(json.dumps(results,indent=2)+"\n")
(OUT/"NO_RELEASE.flag").write_text("No physical iPhone/Android GPU test or human multi-view art acceptance. Never publish unreviewed native GLB.\n")
print("RUN192_REAL_NATIVE_QA",json.dumps(results),flush=True)
