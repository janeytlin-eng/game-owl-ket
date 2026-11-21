#!/usr/bin/env python3
"""#172 Run270 isolated noncommercial neural mesh material/juvenile-form experiment.
Never deploy: the real 3D Hunyuan source is NON-COMMERCIAL, art is unaccepted.
"""
import os, json, time, hashlib
from pathlib import Path
import numpy as np, trimesh, vtk
from PIL import Image
from scipy.ndimage import map_coordinates
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray, vtk_to_numpy

START=time.time()
OUT=Path(os.environ["OWL172_OUTPUT"]); OUT.mkdir(parents=True,exist_ok=True)
SRC=Path(os.environ["OWL172_INPUT"]); REF=Path(os.environ["OWL172_REFERENCE"])
EXPECTED="161c21926b14226b245f045988019d620b0f3a0111d2ee4121bb75e1a13f1ef6"
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(SRC)==EXPECTED, "Refuse changed real-3D source"
m=trimesh.load(SRC,force="mesh")
assert len(m.faces)==133268 and m.is_watertight
v=m.vertices.copy(); x,y,z=v.T
def ss(a,b,t):
 t=np.clip((t-a)/(b-a),0,1);return t*t*(3-2*t)
def vtkpoly(points,faces):
 p=vtk.vtkPolyData();a=vtk.vtkPoints()
 a.SetData(numpy_to_vtk(points.astype(np.float64),deep=True));p.SetPoints(a)
 conn=np.column_stack([np.full(len(faces),3),faces]).astype(np.int64).ravel()
 cells=vtk.vtkCellArray()
 cells.SetCells(len(faces),numpy_to_vtkIdTypeArray(conn,deep=True))
 p.SetPolys(cells);return p

# Sculpt only the original continuous neural mesh: smoother rear, shorter rear
# taper; no extruded 2D cutout, procedural eye balls or disconnected primitives.
flt=vtk.vtkWindowedSincPolyDataFilter()
flt.SetInputData(vtkpoly(v,m.faces));flt.SetNumberOfIterations(75)
flt.SetPassBand(.028);flt.FeatureEdgeSmoothingOff()
flt.BoundarySmoothingOff();flt.NormalizeCoordinatesOn();flt.Update()
sv=vtk_to_numpy(flt.GetOutput().GetPoints().GetData()).copy()
w=(1-ss(-.40,.32,z))*ss(-.95,-.55,y)*.82
v=v*(1-w[:,None])+sv*w[:,None]
x,y,z=v.T
rear=(1-ss(-.18,.20,z))*ss(-.95,-.50,y)
v[:,2]+=np.maximum(-z,0)*.27*rear
x,y,z=v.T

# Reference-aware face paint is applied to actual neural 3D vertices,
# and is depth/heart-region gated so the photograph is NOT wrapped on the rear.
ref=np.asarray(Image.open(REF).convert("RGBA"),dtype=np.float32)
assert ref.shape==(512,512,4)
u=271+213*x
vv=144-295*(y-.52)
coords=np.stack([vv,u])
sample=np.stack([map_coordinates(ref[:,:,i],coords,order=1,mode="constant",cval=0)
                 for i in range(4)],axis=1)
base=np.empty((len(v),3),np.float32)
base[:,0]=245;base[:,1]=234;base[:,2]=216
lower=1-ss(-.45,.45,y)
base-=lower[:,None]*np.array([4,9,13],np.float32)
mask=ss(.55,.72,z)*ss(.20,.35,y)*(1-ss(.78,.88,y))*(1-ss(.33,.47,np.abs(x)))
blend=(mask*.78*np.clip(sample[:,3]/255,0,1))[:,None]
photo=.91*sample[:,:3]+.09*np.array([253,244,226],np.float32)
color=base*(1-blend)+photo*blend

# Two dark irises/pupils + glints painted ON THE ORGANIC 3D EYE SURFACE.
# This is color work on existing mesh, not added sphere/ellipse geometry.
for cx,cy in [(-.185,.513),(.157,.518)]:
 d=np.sqrt(((x-cx)/.055)**2+((y-cy)/.052)**2)
 front=ss(.645,.727,z)
 for inner,outer,rgb in [( .87,1.07,[92,60,33]),(.58,.78,[57,39,27]),(.35,.55,[23,20,19])]:
  w=(1-ss(inner,outer,d))*front
  color=color*(1-w[:,None])+np.array(rgb)[None,:]*w[:,None]
 glint=np.exp(-(((x-(cx-.016))/.011)**2+((y-(cy+.017))/.014)**2)*1.6)*front
 color=color*(1-glint[:,None])+np.array([255,249,231])[None,:]*glint[:,None]
# Tiny color variation is NOT claimed to be genuine dense down/fur.
n=np.sin((x*12.73+y*28.31+z*19.31)*3.3)*np.sin((x*27.1-y*17.8+z*7.37)*2.2)
color+=(1-mask)[:,None]*ss(-.65,-.25,y)[:,None]*n[:,None]*np.array([2,2,3],np.float32)
color=np.clip(color,0,255).astype(np.uint8)
mesh=trimesh.Trimesh(vertices=v,faces=m.faces,process=False);mesh.fix_normals()
mesh.visual.vertex_colors=np.column_stack([color,np.full(len(v),255,np.uint8)])
assert mesh.is_watertight
glb=OUT/"run270_native_neural_cream_eyes_RESEARCH_ART_UNREVIEWED_NO_RELEASE.glb"
mesh.export(glb)
re=trimesh.load(glb,force="mesh")
assert len(re.faces)==133268 and np.allclose(re.vertices,mesh.vertices,atol=1e-6)

def render(n,d):
 p=vtkpoly(v,m.faces)
 c=numpy_to_vtk(np.column_stack([color,np.full(len(v),255,np.uint8)]).astype(np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
 c.SetNumberOfComponents(4);c.SetName("Colors");p.GetPointData().SetScalars(c)
 norms=vtk.vtkPolyDataNormals();norms.SetInputData(p);norms.SplittingOff()
 mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norms.GetOutputPort());mapper.ScalarVisibilityOn();mapper.SetColorModeToDirectScalars()
 actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetInterpolationToPhong();actor.GetProperty().SetAmbient(.28);actor.GetProperty().SetDiffuse(.68);actor.GetProperty().SetSpecular(.09)
 ren=vtk.vtkRenderer();ren.AddActor(actor);ren.SetBackground(.78,.80,.83)
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(620,620);win.AddRenderer(ren)
 cam=ren.GetActiveCamera();center=mesh.bounds.mean(axis=0)
 d=np.asarray(d,float);d/=np.linalg.norm(d)
 cam.SetPosition(*(center+4.4*d));cam.SetFocalPoint(*center)
 cam.SetViewUp(*([0,1,0] if abs(d[1])<.9 else [0,0,-1]))
 cam.ParallelProjectionOn();cam.SetParallelScale(1.2);ren.ResetCameraClippingRange()
 win.Render();winimg=vtk.vtkWindowToImageFilter();winimg.SetInput(win);winimg.Update()
 path=OUT/("view_"+n+".png")
 wr=vtk.vtkPNGWriter();wr.SetFileName(str(path));wr.SetInputConnection(winimg.GetOutputPort());wr.Write();win.Finalize()
 return sha(path)
angles={"front":(0,0,1),"threequarter":(.7,0,1),"right":(1,0,0),"back":(0,0,-1),"left":(-1,0,0),"above":(0,1,.3)}
views={n:render(n,d) for n,d in angles.items()}
report={"run":270,"source_sha256":sha(SRC),"reference_sha256":sha(REF),
        "glb":glb.name,"glb_sha256":sha(glb),"bytes":glb.stat().st_size,
        "triangles":len(re.faces),"watertight":bool(re.is_watertight),
        "changed_vertices_over_0.001":int(np.sum(np.linalg.norm(v-m.vertices,axis=1)>.001)),
        "max_displacement":float(np.linalg.norm(v-m.vertices,axis=1).max()),
        "views":views,"distinct_views":len(set(views.values())),
        "art":"REVIEW_REQUIRED","webgl2":"NOT_TESTED","phone":"NOT_TESTED",
        "license":"HUNYUAN_NONCOMMERCIAL","release":False,
        "elapsed_seconds":round(time.time()-START,2)}
(OUT/"machine-report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
(OUT/"NO_RELEASE.flag").write_text("RESEARCH ART_REJECTED / RIGHTS_RESTRICTED / WEBGL2_UNTESTED / PHONE_UNTESTED / NO_RELEASE\n")
print("RUN270_RESULT",json.dumps(report),flush=True)
