import numpy as np,trimesh,vtk,hashlib,json
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray,vtk_to_numpy
from PIL import Image,ImageDraw
from pathlib import Path
p=Path(__file__).parent
m=next(iter(trimesh.load(p/'run117_trellis_art_unapproved.glb',force='scene').geometry.values()))
v=np.array(m.vertices); f=np.array(m.faces); c=m.visual.to_color().vertex_colors[:,:3].copy()
clay=m.copy();clay.visual=trimesh.visual.ColorVisuals(mesh=clay,vertex_colors=np.tile([222,211,193,255],(len(v),1))); clay.export(p/'clay-diagnostic.glb')
reload=trimesh.load(p/'clay-diagnostic.glb',force='scene');assert sum(len(g.faces) for g in reload.geometry.values())==len(f)
pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(v,deep=True));cells=vtk.vtkCellArray();cells.SetCells(len(f),numpy_to_vtkIdTypeArray(np.column_stack([np.full(len(f),3),f]).astype('int64').ravel(),deep=True)); poly=vtk.vtkPolyData();poly.SetPoints(pts);poly.SetPolys(cells)
normal=vtk.vtkPolyDataNormals();normal.SetInputData(poly);normal.SplittingOff();normal.ConsistencyOn();normal.Update();poly=normal.GetOutput();
mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly);mapper.SetColorModeToDirectScalars();actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetInterpolationToPhong();actor.GetProperty().SetAmbient(.38);actor.GetProperty().SetDiffuse(.62)
ren=vtk.vtkRenderer();ren.SetBackground(0.12,.14,.16);ren.AddActor(actor);win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(384,384);win.AddRenderer(ren);cam=ren.GetActiveCamera();cam.ParallelProjectionOn();cam.SetParallelScale(.59);cam.SetViewUp(0,1,0);cam.SetFocalPoint(0,0,0)
ren.AutomaticLightCreationOff();light=vtk.vtkLight();light.SetLightTypeToCameraLight();light.SetPosition(-.5,.8,1);light.SetFocalPoint(0,0,0);light.SetIntensity(1.0);ren.AddLight(light)
def render(angle,mode):
 a=np.deg2rad(angle);cam.SetPosition(3*np.sin(a),0,3*np.cos(a));ren.ResetCameraClippingRange()
 if mode=='texture':
  arr=numpy_to_vtk(c.astype('uint8'),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR);arr.SetName('rgb');poly.GetPointData().SetScalars(arr);mapper.ScalarVisibilityOn()
 else:
  mapper.ScalarVisibilityOff();actor.GetProperty().SetColor(.87,.83,.76)
 win.Render();w=vtk.vtkWindowToImageFilter();w.SetInput(win);w.ReadFrontBufferOff();w.Update();out=w.GetOutput();im=vtk_to_numpy(out.GetPointData().GetScalars()).reshape(384,384,-1)[::-1,:,:3].copy();return Image.fromarray(im)
# View orientation: +Z is front in recovered source, checked against actual reference orbit.
angles=[0,45,90,135,180]
sheet=Image.new('RGB',(384*5,410*2+28),(28,32,36));d=ImageDraw.Draw(sheet);d.text((8,5),'RUN397 | actual mesh: baked texture versus uniform clay | diagnostic only',fill='white')
for row,mode in enumerate(['texture','clay']):
 for i,a in enumerate(angles):
  im=render(a,mode);im.save(p/f'{mode}-{a}.png');x=i*384;y=28+row*410;sheet.paste(im,(x,y));d.text((x+8,y+386),f'{mode} / {a} deg',fill='white')
sheet.save(p/'comparison.jpg',quality=88)
print(json.dumps({'vertices':len(v),'triangles':len(f),'clay_bytes':(p/'clay-diagnostic.glb').stat().st_size,'clay_sha256':hashlib.sha256((p/'clay-diagnostic.glb').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((p/'run117_trellis_art_unapproved.glb').read_bytes()).hexdigest(),'comparison_sha256':hashlib.sha256((p/'comparison.jpg').read_bytes()).hexdigest()},indent=2))
