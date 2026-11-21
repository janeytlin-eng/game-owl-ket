#!/usr/bin/env python3
"""Real 8-view VTK rendering of source and Run263 native GLBs, never 2D rotation.
Positive Z = front in source glTF Y-up. NO_RELEASE.
"""
import sys,hashlib,json,pathlib
import numpy as np,trimesh,vtk
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
from PIL import Image,ImageDraw
out=pathlib.Path(sys.argv[3]);out.mkdir(parents=True,exist_ok=True)
cases=(("source",pathlib.Path(sys.argv[1])),("candidate",pathlib.Path(sys.argv[2])))
views=(("front",0),("quarter",45),("side",90),("back",180))
results=[]
for label,path in cases:
    obj=trimesh.load(path,force="scene")
    meshes=list(obj.geometry.values())
    pts=np.concatenate([m.vertices for m in meshes])
    center=(pts.min(axis=0)+pts.max(axis=0))/2
    ext=max(np.ptp(pts,axis=0))
    for name,degrees in views:
        ren=vtk.vtkRenderer();ren.SetBackground(.56,.56,.56)
        for m in meshes:
            points=vtk.vtkPoints()
            points.SetData(numpy_to_vtk(m.vertices.astype(np.float32),deep=True))
            cells=np.column_stack([np.full(len(m.faces),3),m.faces]).astype(np.int64).ravel()
            polys=vtk.vtkCellArray();polys.SetCells(len(m.faces),numpy_to_vtkIdTypeArray(cells,deep=True))
            poly=vtk.vtkPolyData();poly.SetPoints(points);poly.SetPolys(polys)
            colors=m.visual.vertex_colors if m.visual.kind=="vertex" else None
            if colors is not None and len(colors)==len(m.vertices):
                scal=numpy_to_vtk(np.asarray(colors[:,:3],dtype=np.uint8),deep=True,
                                     array_type=vtk.VTK_UNSIGNED_CHAR)
                scal.SetNumberOfComponents(3);poly.GetPointData().SetScalars(scal)
            normal=vtk.vtkPolyDataNormals()
            normal.SetInputData(poly);normal.SetFeatureAngle(180);normal.SplittingOff()
            mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(normal.GetOutputPort())
            actor=vtk.vtkActor();actor.SetMapper(mapper)
            actor.GetProperty().SetAmbient(.26);actor.GetProperty().SetDiffuse(.72)
            actor.GetProperty().SetSpecular(.08)
            if colors is None:actor.GetProperty().SetColor(.87,.86,.82)
            else:mapper.SetColorModeToDirectScalars()
            ren.AddActor(actor)
        r=np.deg2rad(degrees)
        camera=vtk.vtkCamera()
        camera.SetPosition(*(center+np.array([4*np.sin(r),1.25,4*np.cos(r)])*ext))
        camera.SetFocalPoint(*center);camera.SetViewUp(0,1,0)
        camera.ParallelProjectionOn();camera.SetParallelScale(ext*.92)
        ren.SetActiveCamera(camera)
        for loc,intensity in (((-2,3,3),.95),((3,2,-1),.55)):
            l=vtk.vtkLight();l.SetPosition(*(center+ext*np.asarray(loc)))
            l.SetFocalPoint(*center);l.SetIntensity(intensity);ren.AddLight(l)
        win=vtk.vtkRenderWindow();win.SetOffScreenRendering(True)
        win.AddRenderer(ren);win.SetSize(640,640);win.SetMultiSamples(8)
        win.Render()
        capture=vtk.vtkWindowToImageFilter();capture.SetInput(win);capture.Update()
        file=out/f"run263_{label}_{name}_REAL_VTK.png"
        writer=vtk.vtkPNGWriter();writer.SetFileName(str(file))
        writer.SetInputConnection(capture.GetOutputPort());writer.Write()
        assert file.stat().st_size>1000
        results.append(dict(model=label,view=name,sha256=hashlib.sha256(file.read_bytes()).hexdigest(),file=file.name))
        win.Finalize()
    sheet=Image.new("RGB",(1000,1000))
    for i,(name,_) in enumerate(views):
        img=Image.open(out/f"run263_{label}_{name}_REAL_VTK.png").convert("RGB").resize((500,500))
        ImageDraw.Draw(img).text((12,12),label+" / "+name,fill=(0,0,0))
        sheet.paste(img,((i%2)*500,(i//2)*500))
    sheet.save(out/f"run263_{label}_4_REAL_VIEWS.jpg",quality=92)
assert len(results)==8
assert len(set(a["sha256"] for a in results))==8
(out/"run263_8view_machine_report.json").write_text(json.dumps(results,indent=2)+"\n")
print(json.dumps(results,indent=2))
