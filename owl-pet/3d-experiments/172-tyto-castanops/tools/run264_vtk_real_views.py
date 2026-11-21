import pathlib,sys,json,hashlib
import vtk,numpy as np,trimesh
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
from PIL import Image,ImageDraw
out=pathlib.Path(sys.argv[1]);src=out/'run263_RESEARCH_NATIVE_ART_REJECTED_NO_RELEASE.glb';new=out/'run264_native_juvenile_socket_compaction_DOWN_REJECTED_NO_RELEASE.glb'
views=[('front',0),('quarter',40),('side',90),('back',180),('otherquarter',320)]
records=[]
for label,path in [('baseline',src),('experiment',new)]:
 sc=trimesh.load(path,force='scene');meshes=list(sc.geometry.values());pts=np.concatenate([g.vertices for g in meshes]);center=(pts.min(axis=0)+pts.max(axis=0))/2;extent=max(np.ptp(pts,axis=0))
 for name,deg in views:
  ren=vtk.vtkRenderer();ren.SetBackground(.72,.73,.74)
  for mesh in meshes:
   points=vtk.vtkPoints();points.SetData(numpy_to_vtk(mesh.vertices.astype('float32'),deep=True))
   arr=np.column_stack([np.full(len(mesh.faces),3),mesh.faces]).astype('int64').ravel()
   cells=vtk.vtkCellArray();cells.SetCells(len(mesh.faces),numpy_to_vtkIdTypeArray(arr,deep=True))
   poly=vtk.vtkPolyData();poly.SetPoints(points);poly.SetPolys(cells)
   rgb=mesh.visual.vertex_colors[:,:3] if mesh.visual.kind=='vertex' else None
   if rgb is not None:
    color=numpy_to_vtk(np.asarray(rgb,dtype='uint8'),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR);color.SetNumberOfComponents(3);poly.GetPointData().SetScalars(color)
   norms=vtk.vtkPolyDataNormals();norms.SetInputData(poly);norms.SetFeatureAngle(180);norms.SplittingOff();norms.ConsistencyOn()
   mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norms.GetOutputPort())
   actor=vtk.vtkActor();actor.SetMapper(mapper)
   actor.GetProperty().SetAmbient(.32);actor.GetProperty().SetDiffuse(.65);actor.GetProperty().SetSpecular(.07)
   if rgb is None:actor.GetProperty().SetColor(.9,.88,.84)
   else:mapper.SetColorModeToDirectScalars()
   ren.AddActor(actor)
  theta=np.deg2rad(deg)
  cam=vtk.vtkCamera();cam.SetPosition(*(center+np.array([4*np.sin(theta),1.05,4*np.cos(theta)])*extent));cam.SetFocalPoint(*center);cam.SetViewUp(0,1,0);cam.ParallelProjectionOn();cam.SetParallelScale(extent*.86);ren.SetActiveCamera(cam)
  for pos,intens in [((-2,3,3),.96),((3,3,-2),.66)]:
   light=vtk.vtkLight();light.SetPosition(*(center+extent*np.array(pos)));light.SetFocalPoint(*center);light.SetIntensity(intens);ren.AddLight(light)
  win=vtk.vtkRenderWindow();win.SetOffScreenRendering(True);win.AddRenderer(ren);win.SetSize(640,640);win.SetMultiSamples(4);win.Render()
  snap=vtk.vtkWindowToImageFilter();snap.SetInput(win);snap.Update()
  file=out/f'run264_{label}_{name}_REAL_VTK.png';wr=vtk.vtkPNGWriter();wr.SetInputConnection(snap.GetOutputPort());wr.SetFileName(str(file));wr.Write();records.append(dict(label=label,view=name,sha=hashlib.sha256(file.read_bytes()).hexdigest()));win.Finalize()
  print(label,name,file.stat().st_size,flush=True)
 sheet=Image.new('RGB',(600*5,640));d=ImageDraw.Draw(sheet)
 for i,(name,_) in enumerate(views):
  im=Image.open(out/f'run264_{label}_{name}_REAL_VTK.png').convert('RGB').resize((600,600))
  sheet.paste(im,(i*600,40));d.text((i*600+15,15),label+' / '+name,fill=(0,0,0))
 sheet.save(out/f'run264_{label}_5view_contact.jpg',quality=90)
(out/'run264_10view_record.json').write_text(json.dumps(records,indent=2))
