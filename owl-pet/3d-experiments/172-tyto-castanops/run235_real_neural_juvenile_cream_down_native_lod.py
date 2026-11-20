#!/usr/bin/env python3
"""Run235: real Run233 neural owl mesh -> cream vertex pigment + quadric LOD + curved second-down ribbons.
Scientific-art study. Reject automatically: no mobile device test, no eucalypt hollow, rough eye anatomy.
NEVER deploy, merge to main, or label as a released pet.
"""
import os, json, hashlib, traceback, time
from pathlib import Path
import numpy as np, trimesh, vtk
from PIL import Image, ImageDraw
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray, vtk_to_numpy

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"owl-pet/3d-experiments/172-tyto-castanops/run235-evidence"
SOURCE=Path(os.environ.get("RUN235_SOURCE",str(OUT/"run233_real_official_Hunyuan3Dmini_CPU_SHAPE_ART_NOT_APPROVED.glb")))
PHOTO=Path(os.environ.get("RUN235_INPUT_IMAGE",str(OUT/"run233_owl_pupils_restored_2D_input_only.png")))
EXPECTED="0e6eedf3ff0b95269555c590c34e996fdc584986d2912f589d817c6ba3b6a02c"
OUT.mkdir(parents=True,exist_ok=True)
REPORT={"run":"Run235","root_provenance":"Official Hunyuan3D-2mini Turbo CPU Run233 genuine generated mesh",
        "research_only":True,"release":"NO_RELEASE","art_pass":False,
        "phone_webgl":"UNTESTED","extra_paid_cost_usd":0}
def sha(p):
 p=Path(p)
 return {"name":p.name,"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def poly(v,f,col):
 d=vtk.vtkPolyData();points=vtk.vtkPoints()
 points.SetData(numpy_to_vtk(np.asarray(v,np.float32),deep=True));d.SetPoints(points)
 arr=np.column_stack((np.full(len(f),3,np.int64),np.asarray(f,np.int64))).ravel()
 cells=vtk.vtkCellArray();cells.SetCells(len(f),numpy_to_vtkIdTypeArray(arr,deep=True));d.SetPolys(cells)
 scal=numpy_to_vtk(np.asarray(col,np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
 scal.SetName("RGB");scal.SetNumberOfComponents(3);d.GetPointData().SetScalars(scal)
 return d
def run():
 assert sha(SOURCE)["sha256"]==EXPECTED,"Run233 unmodified GLB required"
 assert SOURCE.read_bytes()[:4]==b"glTF","not a native GLB"
 m=trimesh.load(SOURCE,force="mesh")
 assert len(m.faces)==275630 and len(m.vertices)==137851
 v=np.asarray(m.vertices);N=np.asarray(m.vertex_normals)
 rng=np.random.default_rng(235172)
 im=np.asarray(Image.open(PHOTO).convert("RGBA"))
 assert im.shape[:2]==(512,512)
 # Image-camera projection paints the true sculpt, rather than building a fake bird from primitives.
 px=np.clip(np.rint(286+225*v[:,0]).astype(int),0,511)
 py=np.clip(np.rint(275-225*v[:,1]).astype(int),0,511)
 sample=im[py,px].astype(float)
 front=np.clip((v[:,2]+.50)/1.05,0,1)**1.15
 front*=np.clip((N[:,2]+.25)/1.25,0,1)**.5 * (sample[:,3]/255.)
 face=np.clip((v[:,1]-.21)/.24,0,1)*np.clip((v[:,2]-.05)/.35,0,1)
 face*=np.clip((.53-np.abs(v[:,0]))/.18,0,1)
 cream=np.array([240.,224.,206.])
 photo=cream*.76+sample[:,:3]*.24
 photo=face[:,None]*(cream*.24+sample[:,:3]*.76)+(1-face[:,None])*photo
 low=(face>.60)&(sample[:,:3].mean(axis=1)<95)
 photo[low]=sample[low,:3]*.93
 base=np.tile(np.array([238.,221.,202.]),(len(v),1))
 base[:,1]-=np.clip(v[:,1]-.25,0,1)*7
 base[:,2]-=np.clip(v[:,1]-.25,0,1)*9
 c=base*(1-front[:,None])+photo*front[:,None]
 c+=rng.normal(0,2.4,len(v))[:,None]*np.array([1,.9,.75])
 # Picked true XYZ surface points for both eyes in actual front +Z geometry.
 for cx,cy in [(-.167,.570),(.210,.570)]:
  radial=np.sqrt(((v[:,0]-cx)/.110)**2+((v[:,1]-cy)/.119)**2)
  visible=np.clip((v[:,2]-.58)/.10,0,1)
  iris=np.clip((1.10-radial)/.22,0,1)*visible
  pupil=np.clip((.70-radial)/.23,0,1)*visible
  c=c*(1-iris[:,None]*.82)+np.array([67.,46.,27.])*iris[:,None]*.82
  c=c*(1-pupil[:,None]*.85)+np.array([21.,17.,14.])*pupil[:,None]*.85
 C=np.clip(c,0,255).astype(np.uint8)
 # Quadric reduction of continuous generated mesh, preserve RGB scalar approximation.
 dec=vtk.vtkQuadricDecimation();dec.SetInputData(poly(v,m.faces,C))
 dec.SetTargetReduction(.83)
 dec.AttributeErrorMetricOn();dec.ScalarsAttributeOn();dec.SetScalarsWeight(.04)
 dec.VolumePreservationOn();dec.Update()
 dp=dec.GetOutput()
 cv=vtk_to_numpy(dp.GetPoints().GetData()).copy()
 cf=vtk_to_numpy(dp.GetPolys().GetConnectivityArray()).copy().reshape(-1,3)
 cc=vtk_to_numpy(dp.GetPointData().GetScalars()).copy()
 core=trimesh.Trimesh(vertices=cv,faces=cf,process=False)
 core.visual.vertex_colors=np.column_stack((cc,np.full(len(cc),255,np.uint8)))
 # Surface-grafted micro-down. Not a geometric owl substitute: every tuft grows from the neural surface.
 np.random.seed(235)
 samples,indices=trimesh.sample.sample_surface(m,19500)
 n=m.face_normals[indices]
 okay=(samples[:,1]>-.75)&~((samples[:,1]>.26)&(samples[:,2]>.12)&(np.abs(samples[:,0])<.52))
 p=samples[okay][:13000]
 n=n[okay][:13000];count=len(p)
 tangent=np.tile(np.array([0.,-1.,0.]),(count,1))
 tangent-=n*np.sum(n*tangent,axis=1)[:,None]
 tl=np.linalg.norm(tangent,axis=1)
 tangent[tl>1e-6]/=tl[tl>1e-6,None]
 tangent[tl<=1e-6]=[1,0,0]
 side=np.cross(n,tangent);side/=np.maximum(np.linalg.norm(side,axis=1),1e-5)[:,None]
 leng=rng.uniform(.027,.060,count);width=rng.uniform(.003,.009,count)
 start=p+n*rng.uniform(.006,.016,count)[:,None]
 a=start-side*(width*.60)[:,None];b=start+side*(width*.60)[:,None]
 midpoint=start+n*(leng*.28)[:,None]+tangent*(leng*.36)[:,None]
 d=midpoint-side*(width*.27)[:,None];e=midpoint+side*(width*.27)[:,None]
 tip=start+n*(leng*.48)[:,None]+tangent*(leng*.94)[:,None]
 hv=np.stack((a,b,d,e,tip),axis=1).reshape(-1,3)
 ids=np.arange(count)*5
 hf=np.stack((np.stack((ids,ids+1,ids+2),1),
              np.stack((ids+1,ids+3,ids+2),1),
              np.stack((ids+2,ids+3,ids+4),1)),axis=1).reshape(-1,3)
 feather=trimesh.Trimesh(vertices=hv,faces=hf,process=False)
 rgb=np.stack((rng.normal(242,3,count),rng.normal(227,3,count),rng.normal(207,4,count)),axis=1)
 fc=np.repeat(np.clip(rgb,0,255).astype(np.uint8),5,axis=0)
 fc[4::5]=[245,233,216]
 feather.visual.vertex_colors=np.column_stack((fc,np.full(len(hv),255,np.uint8)))
 scene=trimesh.Scene()
 scene.add_geometry(core,geom_name="neural_base_lod_REAL_3D")
 scene.add_geometry(feather,geom_name="neural_surface_second_down_ribbons")
 glb=OUT/"run235_real_neural_cream_3d_microdown_ART_REJECTED_NO_RELEASE.glb"
 scene.export(glb)
 reloaded=trimesh.load(glb,force="scene")
 assert glb.read_bytes()[:4]==b"glTF" and len(reloaded.geometry)==2
 assert (np.ptp(cv,axis=0)>.1).all()
 REPORT["source"]=sha(SOURCE);REPORT["image"]=sha(PHOTO)
 REPORT["export"]=sha(glb)
 REPORT["mesh"]={"original_faces":len(m.faces),"lod_faces":len(cf),
    "microdown_faces":len(hf),"total_faces":len(cf)+len(hf),
    "source_down_tufts":count,"lod_vertices":len(cv),"finite":bool(np.isfinite(cv).all())}
 renderer=vtk.vtkRenderer();renderer.SetBackground(.91,.92,.94)
 for geom in (core,feather):
  d=poly(geom.vertices,geom.faces,geom.visual.vertex_colors[:,:3])
  normals=vtk.vtkPolyDataNormals();normals.SetInputData(d);normals.SplittingOff()
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(normals.GetOutputPort())
  mapper.SetScalarModeToUsePointData();mapper.SetColorModeToDirectScalars()
  actor=vtk.vtkActor();actor.SetMapper(mapper)
  actor.GetProperty().SetInterpolationToPhong();actor.GetProperty().SetAmbient(.25)
  renderer.AddActor(actor)
 window=vtk.vtkRenderWindow();window.SetOffScreenRendering(True)
 window.SetSize(560,560);window.SetMultiSamples(0);window.AddRenderer(renderer)
 bounds=np.array(renderer.ComputeVisiblePropBounds())
 ctr=(bounds[::2]+bounds[1::2])/2;extent=max(bounds[1::2]-bounds[::2])
 poses=[("front",(0,0,3)),("left",(-3,0,0)),
        ("threequarter",(2,0,2)),("right",(3,0,0)),
        ("back",(0,0,-3)),("top",(0,3,0)),("bottom",(0,-3,0))]
 sheet=Image.new("RGB",(4*420,2*465),(244,245,247))
 draw=ImageDraw.Draw(sheet);records=[]
 for i,(name,xyz) in enumerate(poses):
  camera=renderer.GetActiveCamera();camera.ParallelProjectionOn()
  camera.SetPosition(*(ctr+extent*np.array(xyz,float)))
  camera.SetFocalPoint(*ctr)
  camera.SetViewUp(*(0,1,0) if name not in ("top","bottom") else (0,0,1))
  camera.SetParallelScale(extent*.76)
  renderer.ResetCameraClippingRange();window.Render()
  frame=vtk.vtkWindowToImageFilter();frame.SetInput(window);frame.Update()
  path=OUT/("run235_real3d_"+name+"_ART_REJECTED.png")
  writer=vtk.vtkPNGWriter();writer.SetFileName(str(path))
  writer.SetInputConnection(frame.GetOutputPort());writer.Write()
  pic=Image.open(path).convert("RGB")
  sheet.paste(pic.resize((416,416)),((i%4)*420,(i//4)*465+26))
  draw.text(((i%4)*420+6,(i//4)*465+5),name,fill="#222222")
  raw=np.asarray(pic,dtype=np.int16)
  fg=int((np.max(abs(raw-np.array([232,235,240])),axis=2)>38).sum())
  assert fg>10000,(name,fg)
  records.append(dict(view=name,foreground=fg,**sha(path)))
 window.Finalize()
 assert len({r["sha256"] for r in records})==7
 contact=OUT/"run235_real3d_sevenview_ART_REJECTED_NO_RELEASE.png"
 sheet.save(contact)
 REPORT["views"]=records;REPORT["contact"]=sha(contact)
 REPORT["status"]="REAL_3D_GLB_7_VIEWS_ART_REJECTED_NO_RELEASE"
 REPORT["art_reasons"]=["eye globes still too hollow","fur still thin or noisy",
   "long silhouette and sideways wing shape need sculpt","no wide realistic eucalypt hollow",
   "no actual smartphone WebGL/GPU validation"]
 return REPORT
if __name__=="__main__":
 started=time.monotonic()
 try:
  run()
 except Exception:
  REPORT["status"]="FAILURE_NO_RELEASE";REPORT["traceback"]=traceback.format_exc()
 finally:
  REPORT["seconds"]=round(time.monotonic()-started,2)
  (OUT/"run235_machine_report.json").write_text(json.dumps(REPORT,indent=2,ensure_ascii=False)+"\n")
  print(json.dumps(REPORT,ensure_ascii=False))
