#!/usr/bin/env python3
"""Run271: purely research, organic neural mesh side-proportion sculpt.
WARNING: upstream Hunyuan model noncommercial; NOT art accepted. NO RELEASE.
No SVG, 2D cutout, or primitive replacements: preserve original 133268-face
connected manifold and painted organic eyes; compare two spatial 3D warps.
"""
import hashlib,json,os,time
from pathlib import Path
import numpy as np,trimesh,vtk
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray,vtk_to_numpy
IN=Path(os.environ['OWL172_INPUT'])
OUT=Path(os.environ['OWL172_OUTPUT']);OUT.mkdir(parents=True,exist_ok=True)
SHA='d90960a228b8de1f9479318200fa0b031a599bd3720103fbe2c51c05703721f2'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(IN)==SHA, 'source native 3D GLB mismatch: abort'
base=trimesh.load(IN,force='mesh')
assert len(base.faces)==133268 and base.is_watertight
v0=base.vertices.copy();faces=base.faces;colors=base.visual.vertex_colors.copy()
def poly(v,f):
 p=vtk.vtkPolyData();pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(v.astype(np.float64),deep=True));p.SetPoints(pts)
 cells=vtk.vtkCellArray();conn=np.column_stack([np.full(len(f),3),f]).astype(np.int64).ravel();cells.SetCells(len(f),numpy_to_vtkIdTypeArray(conn,deep=True));p.SetPolys(cells);return p
def ss(a,b,t):
 t=np.clip((t-a)/(b-a),0,1);return t*t*(3-2*t)
sm=vtk.vtkWindowedSincPolyDataFilter();sm.SetInputData(poly(v0,faces));sm.SetNumberOfIterations(95);sm.SetPassBand(.035);sm.FeatureEdgeSmoothingOff();sm.BoundarySmoothingOff();sm.NormalizeCoordinatesOn();sm.Update()
sv=vtk_to_numpy(sm.GetOutput().GetPoints().GetData()).copy()
def sculpt(kind):
 v=v0.copy();x,y,z=v.T
 weight=(1-ss(.04,.57,z))*(.76 if kind=='gentle' else .92)*(.72+.28*(1-ss(.37,.72,y)))
 v+=weight[:,None]*(sv-v)
 x,y,z=v.T
 upper=ss(-.30,.35,y);lower=1-ss(-.65,-.08,y)
 factor=1+(.18 if kind=='gentle' else .27)*upper-(.30 if kind=='gentle' else .47)*lower
 v[:,2]+=np.minimum(z,0)*(factor-1)*(1-ss(-.05,.25,z))
 x,y,z=v.T
 bump=(1-ss(-.70,-.18,y))*ss(-.98,-.65,y)*(1-ss(-.28,.14,z))
 v[:,1]+=(.10 if kind=='gentle' else .17)*bump
 x,y,z=v.T
 chest=ss(-.72,-.50,y)*(1-ss(.10,.41,y))*(1-ss(.28,.68,z))
 v[:,0]+=x*(.025 if kind=='gentle' else .045)*chest
 m=trimesh.Trimesh(vertices=v,faces=faces,process=False);m.visual.vertex_colors=colors;m.fix_normals()
 return m
def render(mesh,name,d):
 v=mesh.vertices;p=poly(v,mesh.faces)
 arr=numpy_to_vtk(mesh.visual.vertex_colors.astype(np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR);arr.SetNumberOfComponents(4);arr.SetName('Colors');p.GetPointData().SetScalars(arr)
 norms=vtk.vtkPolyDataNormals();norms.SetInputData(p);norms.SplittingOff()
 mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norms.GetOutputPort());mapper.ScalarVisibilityOn();mapper.SetColorModeToDirectScalars()
 actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetInterpolationToPhong();actor.GetProperty().SetAmbient(.3);actor.GetProperty().SetDiffuse(.67);actor.GetProperty().SetSpecular(.06)
 ren=vtk.vtkRenderer();ren.AddActor(actor);ren.SetBackground(.78,.80,.83)
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(620,620);win.AddRenderer(ren)
 cam=ren.GetActiveCamera();direction=np.asarray(d,float);direction/=np.linalg.norm(direction);center=mesh.bounds.mean(axis=0)
 cam.SetPosition(*(center+4.4*direction));cam.SetFocalPoint(*center);cam.SetViewUp(*([0,1,0] if abs(direction[1])<.90 else [0,0,-1]))
 cam.ParallelProjectionOn();cam.SetParallelScale(1.2);ren.ResetCameraClippingRange();win.Render()
 image=vtk.vtkWindowToImageFilter();image.SetInput(win);image.Update()
 path=OUT/(name+'.png');wr=vtk.vtkPNGWriter();wr.SetFileName(str(path));wr.SetInputConnection(image.GetOutputPort());wr.Write();win.Finalize()
 return sha(path)
angles={'front':(0,0,1),'threequarter':(.7,0,1),'right':(1,0,0),'back':(0,0,-1),'left':(-1,0,0),'above':(0,1,.3)}
report={'run':271,'upstream_glb_sha256':SHA,'rights':'HUNYUAN_NONCOMMERCIAL','variants':{},'webgl':'NOT_TESTED','phone':'NOT_TESTED','release':False}
for kind in ['gentle','round']:
 start=time.time();m=sculpt(kind);path=OUT/('run271_'+kind+'_native_organic_sculpt_RESEARCH_NO_RELEASE.glb')
 m.export(path);re=trimesh.load(path,force='mesh')
 assert len(re.faces)==133268 and re.is_watertight
 shift=np.linalg.norm(m.vertices-v0,axis=1)
 views={n:render(m,kind+'_'+n,d) for n,d in angles.items()}
 assert len(set(views.values()))==6
 report['variants'][kind]={'glb_sha256':sha(path),'bytes':path.stat().st_size,'triangles':len(re.faces),'watertight':True,'moved_over_001':int((shift>.001).sum()),'max_shift':float(shift.max()),'front_eye_vertex_shift_max':float(shift[(v0[:,2]>.66)&(v0[:,1]>.26)].max()),'views':views,'elapsed_sec':round(time.time()-start,2)}
 print('RUN271',kind,json.dumps(report['variants'][kind]),flush=True)
(OUT/'machine-report.json').write_text(json.dumps(report,indent=2))
(OUT/'NO_RELEASE.flag').write_text('ORGANIC REAL 3D RESEARCH; ART_REJECTED; HUNYUAN_NONCOMMERCIAL; WEBGL_NOT_TESTED; PHONE_NOT_TESTED; NO_RELEASE\n')
