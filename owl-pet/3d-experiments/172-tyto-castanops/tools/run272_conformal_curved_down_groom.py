#!/usr/bin/env python3
"""#172 Run272: two actual true-3D neural-mesh conformal micro-down groom ablations.
Research only, Hunyuan upstream noncommercial, art/phone gates NOT passed. NO RELEASE.
Real underlying connected neural mesh, NOT an SVG, screenshot or primitive replacement.
"""
import os, hashlib, json
from pathlib import Path
import numpy as np, trimesh, vtk
from PIL import Image, ImageDraw
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray

SOURCE=Path(os.environ["OWL172_INPUT"])
ROOT=Path(os.environ["OWL172_OUTPUT"]);ROOT.mkdir(parents=True,exist_ok=True)
PIN="da21a63c0ec7dbdb8da920896599eb7cafd62fcf94de2e25bae016dd218724ea"
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(SOURCE)==PIN, "Abort: source GLB hash mismatch"
mesh=trimesh.load(SOURCE,force="mesh",skip_materials=True)
assert mesh.is_watertight and len(mesh.faces)==133268 and len(mesh.vertices)==66596
v0=mesh.vertices;faces=mesh.faces;colors=mesh.visual.vertex_colors
assert len(colors)==len(v0)
rng=np.random.default_rng(172272)

def pbr(t):
    t["materials"]=[{"name":"Owl172-Cream-Research-Matte-NO_RELEASE",
       "pbrMetallicRoughness":{"baseColorFactor":[1,1,1,1],
       "metallicFactor":0,"roughnessFactor":1},
       "doubleSided":True,"alphaMode":"OPAQUE"}]
    for gm in t["meshes"]:
        for primitive in gm["primitives"]: primitive["material"]=0

def poly(m):
    p=vtk.vtkPolyData()
    pts=vtk.vtkPoints()
    pts.SetData(numpy_to_vtk(np.asarray(m.vertices,dtype=np.float64),deep=True))
    p.SetPoints(pts)
    f=np.asarray(m.faces,dtype=np.int64)
    c=vtk.vtkCellArray()
    c.SetCells(len(f),numpy_to_vtkIdTypeArray(np.column_stack([
       np.full(len(f),3,dtype=np.int64), f]).ravel(),deep=True))
    p.SetPolys(c)
    color=np.asarray(m.visual.vertex_colors,dtype=np.uint8)
    arr=numpy_to_vtk(color,deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
    arr.SetName("Colors"); arr.SetNumberOfComponents(4)
    p.GetPointData().SetScalars(arr)
    return p

views={"front":(0,0,1),"threequarter":(.7,0,1),
       "right":(1,0,0),"back":(0,0,-1),
       "left":(-1,0,0),"top":(0,1,.3)}
def render(scene,label):
    ren=vtk.vtkRenderer();ren.SetBackground(.78,.80,.84)
    for m in scene.geometry.values():
        norms=vtk.vtkPolyDataNormals();norms.SetInputData(poly(m))
        norms.SplittingOff();norms.ConsistencyOn();norms.AutoOrientNormalsOff()
        normap=vtk.vtkPolyDataMapper()
        normap.SetInputConnection(norms.GetOutputPort())
        normap.SetColorModeToDirectScalars();normap.ScalarVisibilityOn()
        actor=vtk.vtkActor();actor.SetMapper(normap)
        actor.GetProperty().SetAmbient(.36);actor.GetProperty().SetDiffuse(.6)
        actor.GetProperty().SetSpecular(.025);actor.GetProperty().BackfaceCullingOff()
        ren.AddActor(actor)
    win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1)
    win.SetSize(550,550);win.AddRenderer(ren)
    result={}
    for name,d in views.items():
        direction=np.array(d,dtype=float);direction/=np.linalg.norm(direction)
        cam=ren.GetActiveCamera()
        cam.SetPosition(*(4.4*direction));cam.SetFocalPoint(0,0,0)
        cam.SetViewUp(*([0,1,0] if abs(direction[1])<.90 else [0,0,-1]))
        cam.ParallelProjectionOn();cam.SetParallelScale(1.16)
        ren.ResetCameraClippingRange();win.Render()
        img=vtk.vtkWindowToImageFilter();img.SetInput(win);img.Update()
        path=ROOT/(label+"_"+name+".png")
        writer=vtk.vtkPNGWriter();writer.SetFileName(str(path))
        writer.SetInputConnection(img.GetOutputPort());writer.Write()
        result[name]=sha(path)
    win.Finalize()
    mosaic=Image.new("RGB",(1650,1100),"white");draw=ImageDraw.Draw(mosaic)
    for i,name in enumerate(views):
        x=i%3*550;y=i//3*550
        mosaic.paste(Image.open(ROOT/(label+"_"+name+".png")),(x,y))
        draw.text((x+9,y+9),label+" "+name,fill="#161616")
    mosaic.save(ROOT/(label+"_six_actual_views.png"))
    return result

report={"run":272,"source_sha256":PIN,"upstream_rights":"HUNYUAN_NONCOMMERCIAL",
        "art_gate":"REQUIRES_HUMAN_VISUAL_REVIEW","phone_hardware":"UNTESTED",
        "variants":{},"release":False}
for count in (9000,26000):
    pts,idx=trimesh.sample.sample_surface(mesh,count*3,seed=172272+count)
    normals=mesh.face_normals[idx].copy()
    cols=colors[faces[idx]].mean(axis=1)[:,:3]
    yy=pts[:,1];zz=pts[:,2]
    keep=(yy>-.56)&(~((yy>.15)&(zz>.42)&(abs(pts[:,0])<.54)))&(
          cols.mean(axis=1)>120)&(normals[:,1]>-.72)
    pts,normals,cols=pts[keep][:count],normals[keep][:count],cols[keep][:count]
    n=len(pts); yy=pts[:,1]
    cross=np.cross(normals,np.array([0,1,0])[None,:])
    clen=np.linalg.norm(cross,axis=1)
    cross[clen<.02]=np.cross(normals[clen<.02],np.array([0,0,1]))
    clen=np.linalg.norm(cross,axis=1)
    tx=cross/np.maximum(clen[:,None],1e-8);ty=np.cross(normals,tx)
    angle=rng.uniform(0,np.pi*2,n)
    lateral=np.cos(angle)[:,None]*tx+np.sin(angle)[:,None]*ty
    length=rng.uniform(.021,.065,n)*np.clip(.92-.19*yy,.6,1.2)
    direc=normals*.70+np.array([0,-.28,-.10])[None,:]+.28*lateral
    direc/=np.maximum(np.linalg.norm(direc,axis=1)[:,None],1e-6)
    verts=[];tris=[];vc=[]
    widths=np.array([.0034,.0041,.0024,.00013])
    col=.65*cols+.35*np.array([248,242,224])
    col=np.clip(col,188,251)+rng.normal(0,4,(n,1))
    col=np.clip(col,0,255).astype(np.uint8)
    col=np.column_stack([col,np.full(n,255,dtype=np.uint8)])
    for axis in (tx,ty):
        starts=pts-normals*.001
        centers=np.stack([starts+length[:,None]*q*direc+
             length[:,None]*(q*q*.22)*lateral for q in (0,.42,.77,1)],axis=1)
        part=np.stack([centers+axis[:,None,:]*widths[None,:,None]/2,
                       centers-axis[:,None,:]*widths[None,:,None]/2],axis=2)
        part=part.reshape((-1,3))
        f=[]
        for j in range(3):
            a=np.arange(n)*8+j*2
            f.extend([np.stack([a,a+1,a+2],axis=1),
                      np.stack([a+1,a+3,a+2],axis=1)])
        offset=sum(len(a) for a in verts)
        verts.append(part);tris.append(np.concatenate(f,axis=0)+offset)
        vc.append(np.repeat(col,8,axis=0))
    hair=trimesh.Trimesh(vertices=np.concatenate(verts),
         faces=np.concatenate(tris),process=False)
    hair.visual.vertex_colors=np.concatenate(vc)
    scene=trimesh.Scene()
    scene.add_geometry(mesh,geom_name="original_connected_neural_body")
    scene.add_geometry(hair,geom_name="curved_conformal_microdown")
    label="run272_groom_"+str(n)
    glb=ROOT/(label+"_TRUE3D_NO_RELEASE.glb")
    glb.write_bytes(trimesh.exchange.gltf.export_glb(
       scene,include_normals=True,tree_postprocessor=pbr))
    reopened=trimesh.load(glb,force="scene")
    total=sum(len(geo.faces) for geo in reopened.geometry.values())
    assert total==len(mesh.faces)+len(hair.faces)
    actual=render(scene,label)
    assert len(set(actual.values()))==6
    report["variants"][str(n)]={"glb":glb.name,"glb_sha256":sha(glb),
       "glb_bytes":glb.stat().st_size,"continuous_original_triangles":len(mesh.faces),
       "curved_down_triangles":len(hair.faces),"total_triangles":total,
       "curved_tufts":n,"spatial_views":actual}
    print("RUN272",label,json.dumps(report["variants"][str(n)]),flush=True)
(ROOT/"machine-report.json").write_text(json.dumps(report,indent=2)+"\n")
(ROOT/"NO_RELEASE.flag").write_text(
    "TRUE_Neural_3D_Research; ART_UNREVIEWED; HUNYUAN_NONCOMMERCIAL; "+
    "PHONE_UNTESTED; NO_RELEASE\n")
