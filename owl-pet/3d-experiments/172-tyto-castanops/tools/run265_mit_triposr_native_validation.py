#!/usr/bin/env python3
"""Independent research-only mesh and real multi-view VTK check. Never release."""
import pathlib,sys,json,hashlib
import numpy as np,trimesh
from PIL import Image, ImageDraw
out=pathlib.Path(sys.argv[1]); model=out/'triposr/0/mesh.glb'
assert model.is_file() and model.read_bytes()[:4]==b'glTF'
scene=trimesh.load(model,force='scene')
meshes=list(scene.geometry.values())
tris=sum(len(m.faces) for m in meshes)
verts=sum(len(m.vertices) for m in meshes)
points=np.concatenate([m.vertices for m in meshes])
bounds=np.stack([points.min(0),points.max(0)])
assert np.isfinite(bounds).all() and np.all(bounds[1]>bounds[0]) and tris>1000
report=dict(run='265',engine='MIT TripoSR CPU',native_glb_sha256=hashlib.sha256(model.read_bytes()).hexdigest(),
 glb_bytes=model.stat().st_size,meshes=len(meshes),triangles=tris,vertices=verts,
 watertight_meshes=[bool(m.is_watertight) for m in meshes],bounds=bounds.tolist(),
 normals_missing=[not np.isfinite(m.vertex_normals).all() for m in meshes],
 art='UNREVIEWED',phone_hardware='UNTESTED',release='NO_RELEASE')
(out/'run265_native_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2),flush=True)
try:
 import vtk
 from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
except Exception as e:
 (out/'run265_render_import_error.txt').write_text(repr(e))
 raise
viewlist=[('front',0),('leftquarter',45),('side',90),('back',180),('rightquarter',315)]
center=bounds.mean(axis=0);ext=float((bounds[1]-bounds[0]).max())
records=[]
for name,az in viewlist:
 ren=vtk.vtkRenderer();ren.SetBackground(.77,.78,.80)
 for mesh in meshes:
  pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(mesh.vertices.astype('float32'),deep=True))
  inds=np.column_stack((np.full(len(mesh.faces),3),mesh.faces)).astype('int64').ravel()
  cells=vtk.vtkCellArray();cells.SetCells(len(mesh.faces),numpy_to_vtkIdTypeArray(inds,deep=True))
  poly=vtk.vtkPolyData();poly.SetPoints(pts);poly.SetPolys(cells)
  colors=mesh.visual.vertex_colors[:,:3] if mesh.visual.kind=='vertex' else None
  if colors is not None and len(colors)==len(mesh.vertices):
   c=numpy_to_vtk(np.asarray(colors,dtype='uint8'),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
   c.SetNumberOfComponents(3);poly.GetPointData().SetScalars(c)
  norm=vtk.vtkPolyDataNormals();norm.SetInputData(poly);norm.ConsistencyOn();norm.SplittingOff()
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norm.GetOutputPort())
  actor=vtk.vtkActor();actor.SetMapper(mapper)
  actor.GetProperty().SetAmbient(.33);actor.GetProperty().SetDiffuse(.63)
  if colors is None:actor.GetProperty().SetColor(.92,.87,.78)
  else:mapper.SetColorModeToDirectScalars()
  ren.AddActor(actor)
 cam=vtk.vtkCamera();t=np.deg2rad(az)
 cam.SetPosition(*(center+np.array([4*np.sin(t),.85,4*np.cos(t)])*ext))
 cam.SetFocalPoint(*center);cam.SetViewUp(0,1,0)
 cam.ParallelProjectionOn();cam.SetParallelScale(ext*.75);ren.SetActiveCamera(cam)
 for location,intensity in [((-2,3,3),1.),((3,3,-2),.6)]:
  lamp=vtk.vtkLight();lamp.SetPosition(*(center+ext*np.array(location)))
  lamp.SetFocalPoint(*center);lamp.SetIntensity(intensity);ren.AddLight(lamp)
 window=vtk.vtkRenderWindow();window.SetOffScreenRendering(True);window.AddRenderer(ren)
 window.SetSize(640,640);window.SetMultiSamples(4);window.Render()
 grab=vtk.vtkWindowToImageFilter();grab.SetInput(window);grab.Update()
 path=out/('run265_'+name+'_real3D.png')
 writer=vtk.vtkPNGWriter();writer.SetInputConnection(grab.GetOutputPort());writer.SetFileName(str(path));writer.Write()
 records.append(dict(view=name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),bytes=path.stat().st_size))
 print('Rendered real 3D',name,path.stat().st_size,flush=True)
 window.Finalize()
sheet=Image.new('RGB',(600*5,640)); draw=ImageDraw.Draw(sheet)
for i,(name,az) in enumerate(viewlist):
 im=Image.open(out/('run265_'+name+'_real3D.png')).convert('RGB').resize((600,600))
 sheet.paste(im,(i*600,40));draw.text((i*600+12,15),name,fill=(15,15,15))
sheet.save(out/'run265_five_real3D_angles.jpg',quality=90)
(out/'run265_render_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
