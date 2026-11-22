#!/usr/bin/env python3
"""#172 Run289: genuine textured adult museum Tyto alba GLB LOD experiment.
Not a sculpt of the intended rightmost cream-white Tyto castanops chick.
No geometry-primitive stand-in and no product release.
"""
import hashlib, json, os
from pathlib import Path
import numpy as np
import requests, trimesh, vtk
from PIL import Image, ImageDraw
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray, vtk_to_numpy

OUT=Path(os.environ.get('OWL172_OUTPUT','owl172-run289-evidence'))
OUT.mkdir(parents=True,exist_ok=True)
SOURCE='https://doc.ayootech.com/galeri/model/0e65de5934db4f0eae02835ba7227dcc.glb'
PIN='6412ffd575360397bd90d391d3d4c23397f225945cdef3ec5727bfd91504cd44'
sha=lambda b:hashlib.sha256(b).hexdigest()
resp=requests.get(SOURCE,timeout=240);resp.raise_for_status();binary=resp.content
if binary[:4]!=b'glTF' or sha(binary)!=PIN:
    raise RuntimeError('Failed to pin actual original adult museum 3D source: abort')
p=OUT/'source_adult_MUSEUM_NOT_TARGET.glb';p.write_bytes(binary)
source=trimesh.load(p,force='scene',process=False)
original=source.dump(concatenate=False)
if not original or sum(len(m.faces) for m in original)<250000:
    raise RuntimeError('Missing native adult owl geometry')

def poly(m):
    pts=np.ascontiguousarray(m.vertices,dtype=np.float32)
    faces=np.ascontiguousarray(m.faces,dtype=np.int64)
    obj=vtk.vtkPolyData();points=vtk.vtkPoints()
    points.SetData(numpy_to_vtk(pts,deep=True));obj.SetPoints(points)
    cells=vtk.vtkCellArray()
    offsets=np.arange(0,3*len(faces)+1,3,dtype=np.int64)
    cells.SetData(numpy_to_vtkIdTypeArray(offsets,deep=True),numpy_to_vtkIdTypeArray(faces.ravel(),deep=True))
    obj.SetPolys(cells)
    uv=getattr(m.visual,'uv',None)
    if uv is not None and len(uv)==len(pts):
        uv=np.asarray(uv,dtype=np.float32)
        if 2<uv.max()<=65535: uv=uv/65535.0
        t=numpy_to_vtk(np.ascontiguousarray(uv),deep=True)
        t.SetName('UV0');t.SetNumberOfComponents(2);obj.GetPointData().SetTCoords(t)
    return obj

def decomp(obj,m):
    verts=np.asarray(vtk_to_numpy(obj.GetPoints().GetData()),dtype=np.float64)
    faces=vtk_to_numpy(obj.GetPolys().GetConnectivityArray()).reshape(-1,3)
    UV=obj.GetPointData().GetTCoords()
    if UV is not None:
        visual=trimesh.visual.texture.TextureVisuals(
            uv=np.asarray(vtk_to_numpy(UV),dtype=np.float32),material=m.visual.material)
    else:
        visual=trimesh.visual.ColorVisuals(
            vertex_colors=np.tile([211,194,172,255],(len(verts),1)))
    return trimesh.Trimesh(vertices=verts,faces=faces,visual=visual,process=False)

result=[];parts=[]
for i,m in enumerate(original):
    before=len(m.faces)
    if before<20:
        result.append(m.copy());parts.append({'mesh':i,'before':before,'after':before,'tiny_preserved':True});continue
    obj=poly(m)
    dec=vtk.vtkQuadricDecimation();dec.SetInputData(obj)
    dec.SetTargetReduction(0.68);dec.AttributeErrorMetricOn();dec.SetTCoordsWeight(2.)
    dec.Update();reduced=dec.GetOutput()
    if reduced.GetNumberOfPolys()<5:
        raise RuntimeError('Mesh part erased: '+str(i))
    if obj.GetPointData().GetTCoords() is not None and reduced.GetPointData().GetTCoords() is None:
        raise RuntimeError('Source UVs were lost in mesh '+str(i))
    mesh=decomp(reduced,m);result.append(mesh)
    parts.append({'mesh':i,'before':before,'after':len(mesh.faces),'has_uv':getattr(mesh.visual,'uv',None) is not None})

output=trimesh.Scene()
for i,m in enumerate(result):output.add_geometry(m,node_name='real_decimated_part_'+str(i))
lodpath=OUT/'adult_barn_owl_ACTUAL_TEXTURED_GEOMETRIC_LOD_NOT_JUVENILE_NO_RELEASE.glb'
lodpath.write_bytes(output.export(file_type='glb'))
loaded=trimesh.load(lodpath,force='scene',process=False).dump(concatenate=False)
oldtris=sum(len(m.faces) for m in original);newtris=sum(len(m.faces) for m in loaded)
if not loaded or newtris>oldtris*.5:
    raise RuntimeError('True geometry LOD did not achieve >50% triangles removed')
if not any(getattr(getattr(m.visual,'material',None),'baseColorTexture',None) is not None for m in loaded):
    raise RuntimeError('New GLB missing actual source PBR texture')
if len(loaded)!=len(original):raise RuntimeError('Lost mesh parts on GLB re-import')
views=[('front',(0,0,1),(0,1,0)),('front45',(.7,0,.7),(0,1,0)),
 ('right',(1,0,0),(0,1,0)),('back',(0,0,-1),(0,1,0)),
 ('left',(-1,0,0),(0,1,0)),('top',(0,1,0),(0,0,-1))]

def six(label,meshes):
    ren=vtk.vtkRenderer();win=vtk.vtkRenderWindow();win.SetOffScreenRendering(True)
    win.SetSize(420,420);win.AddRenderer(ren);uv_samples=[]
    for i,m in enumerate(meshes):
        obj=poly(m)
        uv=getattr(m.visual,'uv',None)
        tex=getattr(getattr(m.visual,'material',None),'baseColorTexture',None)
        if uv is not None and tex is not None:
            rgb=np.asarray(tex.convert('RGB'),dtype=np.uint8);h,w=rgb.shape[:2]
            uv=np.asarray(uv,dtype=float)
            if 2<uv.max()<=65535:uv=uv/65535.
            if uv.min()<-.01 or uv.max()>1.05:raise RuntimeError('Invalid normalized UV in '+label)
            u=np.clip((np.mod(uv[:,0],1)*(w-1)).astype(int),0,w-1)
            v=np.clip(((1-np.mod(uv[:,1],1))*(h-1)).astype(int),0,h-1)
            colors=np.ascontiguousarray(rgb[v,u],dtype=np.uint8)
            uv_samples.append(np.std(colors.astype(float),axis=0).tolist())
        else:
            colors=np.tile([206,187,166],(len(m.vertices),1)).astype(np.uint8)
        vtkcolors=numpy_to_vtk(colors,deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
        vtkcolors.SetNumberOfComponents(3);obj.GetPointData().SetScalars(vtkcolors)
        mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(obj)
        mapper.SetScalarModeToUsePointData();mapper.SetColorModeToDirectScalars()
        actor=vtk.vtkActor();actor.SetMapper(mapper)
        actor.GetProperty().SetAmbient(.34);actor.GetProperty().SetDiffuse(.75)
        ren.AddActor(actor)
    if not uv_samples or max(np.mean(x) for x in uv_samples)<12:
        raise RuntimeError('False color: UV quantization/texture collapsed '+label)
    ren.SetBackground(.96,.95,.93);light=vtk.vtkLight()
    light.SetPosition(-2,4,5);light.SetIntensity(1.2);ren.AddLight(light)
    bounds=ren.ComputeVisiblePropBounds()
    if bounds[0]>bounds[1]:raise RuntimeError('No real VTK actors')
    center=np.array([(bounds[0]+bounds[1])/2,(bounds[2]+bounds[3])/2,(bounds[4]+bounds[5])/2])
    span=max(bounds[1]-bounds[0],bounds[3]-bounds[2],bounds[5]-bounds[4])
    camera=ren.GetActiveCamera();camera.SetViewAngle(33)
    sheet=Image.new('RGB',(1260,880),'#f6f4f0');draw=ImageDraw.Draw(sheet)
    qa=[]
    for j,(name,axis,up) in enumerate(views):
        camera.SetPosition(*(center+2.7*span*np.asarray(axis)))
        camera.SetFocalPoint(*center);camera.SetViewUp(*up)
        ren.ResetCameraClippingRange();win.Render()
        grab=vtk.vtkWindowToImageFilter();grab.SetInput(win);grab.ReadFrontBufferOff();grab.Update()
        path=OUT/(label+'_'+name+'_real_native_camera.png')
        writer=vtk.vtkPNGWriter();writer.SetFileName(str(path))
        writer.SetInputConnection(grab.GetOutputPort());writer.Write()
        img=Image.open(path).convert('RGB');array=np.asarray(img,dtype=np.int16)
        bg=array[0,0];occupancy=float(np.mean(np.max(abs(array-bg),axis=2)>38))
        if occupancy<.01:raise RuntimeError('Blank render false success: '+label+' '+name)
        digest=sha(path.read_bytes());qa.append({'angle':name,'sha256':digest,'foreground':occupancy})
        xx=(j%3)*420;yy=(j//3)*440;sheet.paste(img,(xx,yy))
        draw.text((xx+9,yy+422),label+': '+name,fill=(30,25,22))
    if len(set(x['sha256'] for x in qa))!=6:raise RuntimeError('False non-orbit identical images')
    sheet.save(OUT/(label+'_six_real_cameras_NO_RELEASE.png'))
    return {'views':qa,'uv_texture_rgb_stdev':uv_samples}

source_views=six('adult_original',original)
lod_views=six('adult_geometric_lod',loaded)
report={'date':'2026-11-22','run':'289','target':'#172 Tyto castanops v3 rightmost fluffy cream-white juvenile',
 'purpose':'UV-aware QUADRIC TRUE GEOMETRIC LOD test on an anatomically real ADULT reference ONLY',
 'primary':'https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc',
 'source_license':'Author declares CC0; anonymous binary mirror not fully verified',
 'source_SHA256':PIN,'source_triangles':oldtris,'output_triangles':newtris,
 'true_triangle_reduction':1-newtris/oldtris,
 'source_bytes':len(binary),'output_bytes':lodpath.stat().st_size,
 'output_sha256':sha(lodpath.read_bytes()),'mesh_parts':parts,
 'original_six_views':source_views,'lod_six_views':lod_views,
 'art':'ART_REJECTED: real adult grey-brown Tyto alba reference is not the target cream downy young Tyto castanops',
 'phone':'NOT_TESTED: offscreen VTK is NOT Chromium WebGL2 or physical phone GPU',
 'rights':'UNVERIFIED_ORIGINAL_TO_MIRROR_CHAIN','external_paid_USD':0,'release':False}
(OUT/'run289_machine_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
(OUT/'NO_RELEASE.txt').write_text('REAL_TEXTURED_NATIVE_3D_GEOMETRY_LOD_TECH_ONLY / ART_REJECTED / PHONE_UNTESTED / RIGHTS_UNCLEARED / NO_RELEASE\n')
p.unlink() # already pinned; do not duplicate 43 MB source artifact
(OUT/'SHA256SUMS.txt').write_text(''.join(
 sha(x.read_bytes())+'  '+x.name+'\n'
 for x in sorted(OUT.iterdir()) if x.is_file() and x.name!='SHA256SUMS.txt'))
print(json.dumps({'result':'TRUE_NATIVE_TEXTURED_LOD_RESEARCH_ONLY_ART_REJECTED_NO_RELEASE',
 'before':oldtris,'after':newtris,'reduction':1-newtris/oldtris,'bytes':lodpath.stat().st_size}))
