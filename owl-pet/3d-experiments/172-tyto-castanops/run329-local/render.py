import vtk,trimesh,numpy as np
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
from pathlib import Path
from PIL import Image, ImageDraw
P=Path(__file__).parent
scene=trimesh.load(P/'sculpt-NO_RELEASE.glb',force='scene'); ren=vtk.vtkRenderer();ren.SetBackground(.19,.205,.23)
for name,m in scene.geometry.items():
 pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(np.asarray(m.vertices),deep=True)); cells=vtk.vtkCellArray();f=np.column_stack([np.full(len(m.faces),3),m.faces]).astype(np.int64);cells.SetCells(len(f),numpy_to_vtkIdTypeArray(f.ravel(),deep=True));poly=vtk.vtkPolyData();poly.SetPoints(pts);poly.SetPolys(cells);rgb=numpy_to_vtk(np.asarray(m.visual.vertex_colors),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR);rgb.SetName('RGBA');poly.GetPointData().SetScalars(rgb);norm=vtk.vtkPolyDataNormals();norm.SetInputData(poly);norm.SplittingOff();norm.ComputePointNormalsOn();norm.Update();mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norm.GetOutputPort());mapper.SetColorModeToDirectScalars();act=vtk.vtkActor();act.SetMapper(mapper);act.GetProperty().SetAmbient(.27);act.GetProperty().SetDiffuse(.72);act.GetProperty().SetSpecular(.06 if 'eye' not in name else .45);act.GetProperty().SetSpecularPower(30);ren.AddActor(act)
win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.AddRenderer(ren);win.SetSize(480,520);win.SetMultiSamples(4);cam=ren.GetActiveCamera();cam.SetFocalPoint(0,0,.75);cam.SetViewUp(0,0,1);cam.ParallelProjectionOn();cam.SetParallelScale(.92)
for i,angle in enumerate([0,45,90,135,180,225,270,315]):
 a=np.deg2rad(angle);cam.SetPosition(3*np.sin(a),3*np.cos(a),1.08);ren.ResetCameraClippingRange();win.Render();w=vtk.vtkWindowToImageFilter();w.SetInput(win);w.Update();writer=vtk.vtkPNGWriter();writer.SetFileName(str(P/f'view-{angle:03d}.png'));writer.SetInputConnection(w.GetOutputPort());writer.Write()
canvas=Image.new('RGB',(960,1080),'#272930');d=ImageDraw.Draw(canvas)
for i,angle in enumerate([0,45,90,135,180,225,270,315]):
 im=Image.open(P/f'view-{angle:03d}.png').resize((240,260));x=(i%4)*240;y=(i//4)*280;canvas.paste(im,(x,y));d.text((x+8,y+260),f'{angle} deg',fill='white')
canvas=canvas.crop((0,0,960,560));canvas.save(P/'eight-views.jpg',quality=85)
