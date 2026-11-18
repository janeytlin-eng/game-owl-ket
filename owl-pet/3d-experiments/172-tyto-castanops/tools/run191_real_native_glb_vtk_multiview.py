#!/usr/bin/env python3
"""Render actual Run190 quarantined Hunyuan native GLB in 7 3D camera views.

This is visual and mesh QA, NOT generation, not an artistic repair, not approval.
The exact uploaded source and model SHA256 are asserted. Never use sample assets.
"""
import pathlib, json, hashlib, math
import numpy as np
import trimesh, vtk
from PIL import Image, ImageDraw
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
from datetime import datetime,timezone

BASE=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=BASE/"research-evidence-run191-WHITE-MESH-SEVENVIEW-ART_REJECTED-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)
GLB=OUT/"run190_paint-3d-dev_actual_new_source_QUARANTINED.glb"
SRC=BASE/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
MODEL_SHA="6c71558189df19947f1492faf8ecb9ed74bf5c2844cff200ea486f19f2e6a836"
SOURCE_SHA="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(GLB)==MODEL_SHA, "native generated source asset changed"
assert sha(SRC)==SOURCE_SHA, "original v3 mesoptile photo changed"
rejected=BASE/"known_rejected_asset_sha256_registry.json"
assert rejected.exists(),"rejection registry absent"
scene=trimesh.load(str(GLB),force="scene",process=False)
meshes=list(scene.geometry.values())
assert meshes and len(meshes)==1, "unexpected source geometry"
mesh=meshes[0]
assert len(mesh.faces)>1000 and len(mesh.vertices)>1000
stats={"run":191,"timestamp_utc":datetime.now(timezone.utc).isoformat(),"source_generation_run":190,
       "source_photo_sha256":sha(SRC),"model_sha256":sha(GLB),"model_bytes":GLB.stat().st_size,
       "vertices":int(len(mesh.vertices)),"triangles":int(len(mesh.faces)),
       "meshes":len(meshes),"bbox_xyz":mesh.extents.tolist(),
       "is_watertight":bool(mesh.is_watertight),"euler_number":int(mesh.euler_number),
       "materials_in_glb":0,"textures_in_glb":0,
       "offscreen_renderer":"VTK native polygon renderer (not simulated geometry)",
       "physical_mobile_webgl_tested":False,"art_accepted":False,
       "release":False}
# VTK exact loaded source mesh and normals
points=vtk.vtkPoints()
points.SetData(numpy_to_vtk(mesh.vertices.astype("float64"),deep=True))
faces=np.column_stack([np.full(len(mesh.faces),3,dtype=np.int64),mesh.faces]).astype("int64")
cells=vtk.vtkCellArray()
cells.SetCells(len(mesh.faces),numpy_to_vtkIdTypeArray(faces.ravel(),deep=True))
pd=vtk.vtkPolyData();pd.SetPoints(points);pd.SetPolys(cells)
norm=vtk.vtkPolyDataNormals();norm.SetInputData(pd);norm.ComputePointNormalsOn();norm.SplittingOff();norm.Update()
mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norm.GetOutputPort())
actor=vtk.vtkActor();actor.SetMapper(mapper)
actor.GetProperty().SetColor(.83,.81,.75)
actor.GetProperty().SetInterpolationToPBR()
actor.GetProperty().SetMetallic(.03)
actor.GetProperty().SetRoughness(.84)
ren=vtk.vtkRenderer();ren.SetBackground(.95,.945,.92);ren.AddActor(actor)
ren.AutomaticLightCreationOff()
for pos,light_power in [((3,4,6),1.15),((-4,2,-3),.75),((0,-3,2),.48)]:
    light=vtk.vtkLight();light.SetLightTypeToSceneLight()
    light.SetPosition(*pos);light.SetFocalPoint(0,0,0)
    light.SetIntensity(light_power);ren.AddLight(light)
rw=vtk.vtkRenderWindow();rw.SetOffScreenRendering(True);rw.SetSize(560,560)
rw.SetMultiSamples(0);rw.AddRenderer(ren)
ctr=mesh.bounds.mean(axis=0);extent=max(mesh.extents);dist=extent*3.3
views=[("front_posZ",(0,0,1)),("side_posX",(1,0,0)),
       ("back_negZ",(0,0,-1)),("side_negX",(-1,0,0)),
       ("top_posY",(0,1,0)),("underside_negY",(0,-1,0)),
       ("quarter",(0.7,.45,1))]
screenshots=[]
for name,axis in views:
    xyz=np.array(axis,dtype=float);xyz/=np.linalg.norm(xyz)
    camera=ren.GetActiveCamera()
    camera.SetFocalPoint(*ctr);camera.SetPosition(*(ctr+dist*xyz))
    camera.SetViewUp(*( (0,0,1) if abs(xyz[1])>.85 else (0,1,0) ))
    camera.ParallelProjectionOn()
    camera.SetParallelScale(extent*.86)
    ren.ResetCameraClippingRange()
    rw.Render()
    image=vtk.vtkWindowToImageFilter()
    image.SetInput(rw);image.ReadFrontBufferOff();image.Update()
    filename=f"run191_REAL_{name}.png"
    writer=vtk.vtkPNGWriter();writer.SetInputConnection(image.GetOutputPort())
    writer.SetFileName(str(OUT/filename));writer.Write()
    size=(OUT/filename).stat().st_size
    assert size>4500,"empty native raster: "+filename
    screenshots.append({"name":name,"path":filename,"bytes":size})
frames=[]
for record in screenshots:
    image=Image.open(OUT/record["path"]).convert("RGB")
    ImageDraw.Draw(image).text((12,13),record["name"],fill=(20,25,20))
    frames.append(image)
sheet=Image.new("RGB",(560*4,560*2),(255,255,255))
for index,im in enumerate(frames):sheet.paste(im,((index%4)*560,(index//4)*560))
sheet.save(OUT/"run191_REAL_NATIVE_SEVENVIEW_CONTACT.png")
stats["screenshots"]=screenshots
stats["status"]="SEVEN_REAL_NATIVE_VIEWS_CREATED_NO_RELEASE"
(OUT/"run191_native_metrics.json").write_text(json.dumps(stats,indent=2)+"\n")
(OUT/"NO_RELEASE.flag").write_text("Source native GLB is an untextured grey white mesh with adult-like rigid wings and posterior; actual seven-camera VTK views, no art approval or real mobile GPU test.\n")
manifest={}
for file in sorted(OUT.iterdir()):
    if file.is_file() and file.name!="run191_sha256_manifest.json":
        manifest[file.name]={"bytes":file.stat().st_size,"sha256":sha(file)}
(OUT/"run191_sha256_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
assert all(sha(OUT/k)==v["sha256"] for k,v in manifest.items())
print("RUN191_NATIVE_7VIEW_CREATED",json.dumps({"model_sha":MODEL_SHA,"triangles":stats["triangles"],"views":len(screenshots),"files":len(manifest),"NO_RELEASE":True}),flush=True)
