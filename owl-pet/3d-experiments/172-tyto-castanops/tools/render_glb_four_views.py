#!/usr/bin/env python3
"""GLB geometry/vertex-color QA: four genuine 3D VTK renders.

Standalone use (Linux): xvfb-run -a python render_glb_four_views.py model.glb outdir
Requires numpy, trimesh, vtk, pillow. These views DO NOT establish WebGL/mobile.
"""
import json
import pathlib
import sys

import numpy as np
import trimesh
import vtk
from PIL import Image, ImageDraw
from vtk.util.numpy_support import numpy_to_vtk


def actor_for(mesh):
    pd = vtk.vtkPolyData()
    points = vtk.vtkPoints()
    points.SetData(numpy_to_vtk(mesh.vertices.astype('float32'), deep=True))
    pd.SetPoints(points)
    faces = mesh.faces.astype(np.int64)
    cells = vtk.vtkCellArray()
    offsets = np.arange(0, len(faces)*3+1, 3, dtype=np.int64)
    cells.SetData(numpy_to_vtk(offsets, deep=True, array_type=vtk.VTK_ID_TYPE),
                  numpy_to_vtk(faces.ravel(), deep=True, array_type=vtk.VTK_ID_TYPE))
    pd.SetPolys(cells)
    if mesh.visual.kind == 'vertex':
        rgb = mesh.visual.vertex_colors[:, :3].astype('uint8')
    else:
        rgb = np.tile([208, 198, 186], (len(mesh.vertices), 1)).astype('uint8')
    values = numpy_to_vtk(rgb.copy(), deep=True, array_type=vtk.VTK_UNSIGNED_CHAR)
    values.SetNumberOfComponents(3)
    values.SetName('RGB')
    pd.GetPointData().SetScalars(values)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(pd)
    mapper.SetColorModeToDirectScalars()
    mapper.SetScalarModeToUsePointData()
    mapper.ScalarVisibilityOn()
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetAmbient(.44)
    actor.GetProperty().SetDiffuse(.62)
    actor.GetProperty().SetSpecular(.08)
    actor.GetProperty().SetInterpolationToPhong()
    actor.GetProperty().BackfaceCullingOff()
    return actor


def render(input_glb, outdir):
    outdir = pathlib.Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    scene = trimesh.load(input_glb, force='scene', process=False)
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(.84, .86, .85)
    renderer.SetBackground2(.98, .98, .96)
    renderer.GradientBackgroundOn()
    for mesh in scene.geometry.values():
        if isinstance(mesh, trimesh.Trimesh) and len(mesh.faces):
            renderer.AddActor(actor_for(mesh))
    window = vtk.vtkRenderWindow()
    window.SetOffScreenRendering(True)
    window.SetSize(750, 850)
    window.AddRenderer(renderer)
    center = (scene.bounds[0] + scene.bounds[1]) / 2
    extents = scene.bounds[1] - scene.bounds[0]
    scale = max(extents)
    views = [('front', (0, 1, .20)),
             ('threequarter', (.70, .82, .23)),
             ('strict_side', (1, 0, .20)),
             ('rear', (0, -1, .20))]
    thumbs = []
    for name, direction in views:
        direction = np.asarray(direction, dtype=float)
        direction /= np.linalg.norm(direction)
        camera = renderer.GetActiveCamera()
        camera.SetFocalPoint(*center)
        camera.SetPosition(*(center + direction*scale*2.8))
        camera.SetViewUp(0, 0, 1)
        camera.SetViewAngle(30)
        renderer.ResetCameraClippingRange()
        window.Render()
        image_filter = vtk.vtkWindowToImageFilter()
        image_filter.SetInput(window)
        image_filter.ReadFrontBufferOff()
        image_filter.Update()
        writer = vtk.vtkPNGWriter()
        writer.SetInputConnection(image_filter.GetOutputPort())
        target = outdir / (name + '.png')
        writer.SetFileName(str(target))
        writer.Write()
        thumb = Image.open(target).convert('RGB')
        thumb.thumbnail((500, 560))
        thumbs.append((name, thumb))
    sheet = Image.new('RGB', (1000, 1120), '#faf9f5')
    draw = ImageDraw.Draw(sheet)
    for i, (name, thumb) in enumerate(thumbs):
        x, y = (i % 2)*500, (i//2)*560
        sheet.paste(thumb, (x, y))
        draw.text((x+10, y+14), name.upper(), fill='#28302c')
    sheet.save(outdir/'four_views.png')
    summary = {'glb': str(input_glb), 'geometry_count': len(scene.geometry),
               'triangles': sum(len(g.faces) for g in scene.geometry.values() if hasattr(g, 'faces')),
               'bounds': scene.bounds.tolist(), 'rasterizer': 'VTK offscreen Xvfb',
               'webgl_verified': False, 'textures_correctness_verified': False}
    (outdir/'render_report.json').write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('Usage: render_glb_four_views.py INPUT.glb OUTPUT_DIRECTORY')
    render(sys.argv[1], sys.argv[2])
