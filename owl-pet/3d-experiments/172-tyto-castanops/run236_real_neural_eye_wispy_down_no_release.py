#!/usr/bin/env python3
"""Run236: genuine Run235 neural sculpt -> eye, pigment and alpha-down research.
Do NOT deploy. Visual/art approval and mobile WebGL are NOT inferred from GLB validity.
"""
import os, json, hashlib, traceback, time
from pathlib import Path
import numpy as np, trimesh, vtk
from PIL import Image, ImageDraw
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray, vtk_to_numpy
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"owl-pet/3d-experiments/172-tyto-castanops/run236-evidence"
OUT.mkdir(parents=True,exist_ok=True)
SOURCE=Path(os.environ.get("RUN236_SOURCE",OUT/"run235_real_neural_cream_3d_microdown_ART_REJECTED_NO_RELEASE.glb"))
EXPECTED="97a2df9235310bea850f2a61db15b7930e90e1b9404bc9170cc98706c181dea2"
REPORT={"run":"Run236","research_only":True,"release":"NO_RELEASE","art_pass":False,"phone_webgl":"UNTESTED","additional_paid_usd":0}
def filehash(p):
 p=Path(p); return {"name":p.name,"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def vtkpoly(verts,faces,colors):
 p=vtk.vtkPolyData();a=vtk.vtkPoints()
 a.SetData(numpy_to_vtk(np.asarray(verts,np.float32),deep=True));p.SetPoints(a)
 f=np.column_stack((np.full(len(faces),3,np.int64),np.asarray(faces,np.int64))).ravel()
 cells=vtk.vtkCellArray();cells.SetCells(len(faces),numpy_to_vtkIdTypeArray(f,deep=True));p.SetPolys(cells)
 col=numpy_to_vtk(np.asarray(colors,np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
 col.SetName("RGB");col.SetNumberOfComponents(3);p.GetPointData().SetScalars(col)
 return p
def main():
 assert filehash(SOURCE)["sha256"]==EXPECTED,"Only actual Run235 real diffusion GLB is permitted"
 assert SOURCE.read_bytes()[:4]==b"glTF"
 inp=trimesh.load(SOURCE,force="scene")
 assert set(inp.geometry)=={"neural_base_lod_REAL_3D","neural_surface_second_down_ribbons"}
 core=inp.geometry["neural_base_lod_REAL_3D"].copy()
 ribbon=inp.geometry["neural_surface_second_down_ribbons"].copy()
 assert len(core.faces)==46856 and len(ribbon.faces)==36651
 # Smoothly shorten true rear volume; preserve the actual face and both feet
 for mesh in (core,ribbon):
  p=mesh.vertices.copy()
  blend=(p[:,2]<0)*np.clip((.53-p[:,1])/.95,0,1)
  p[:,2]*=(1-.15*blend)
  mesh.vertices=p
 # Repaint genuine sculpt vertices at the deep-pit eye centers so dark sockets do not look hollow
 p=core.vertices
 rgba=core.visual.vertex_colors.copy().astype(float)
 for cx,cy,cz in ((-.167,.570,.75),(.210,.570,.73)):
  rr=np.sqrt(((p[:,0]-cx)/.112)**2+((p[:,1]-cy)/.116)**2)
  w=np.clip((1.16-rr)/.55,0,1)*np.clip((p[:,2]-.59)/.14,0,1)
  pigment=np.array([145.,115.,83.])
  rgba[:,:3]=rgba[:,:3]*(1-w[:,None]) + pigment*w[:,None]
 core.visual.vertex_colors=np.uint8(np.clip(rgba,0,255))
 # Organic learned owl remains the entire body. Eye globes are only anatomical details.
 eye_parts=[]
 for cx,cy,cz in ((-.167,.570,.751),(.210,.570,.732)):
  for scale,depth,color,subdivision in [
   ((.068,.066,.037),0.,(53,36,25,255),3),
   ((.047,.049,.016),.029,(30,25,21,255),2),
   ((.008,.009,.004),.049,(245,229,212,255),1)]:
   m=trimesh.creation.icosphere(subdivisions=subdivision,radius=1.)
   m.vertices=m.vertices*np.array(scale)+np.array([cx-(0.019 if depth>.04 else 0),cy+(0.018 if depth>.04 else 0),cz+depth])
   m.visual.vertex_colors=np.tile(color,(len(m.vertices),1)).astype(np.uint8)
   eye_parts.append(m)
 # Previously fully opaque ribbon vertices are now a true shared alpha wispy texture
 texsize=256
 yy,xx=np.mgrid[0:texsize,0:texsize].astype(float)
 t=yy/(texsize-1)
 wisps=np.zeros((texsize,texsize))
 for k in range(5):
  centre=128+(k-2)*12*np.sin(np.pi*t)*.65+(k-2)*20*t+5*np.sin(9*t+k)
  wisps=np.maximum(wisps,np.exp(-((xx-centre)/3.8)**2))
 envelope=(np.sin(np.pi*np.clip(t,1e-5,1-1e-5))**.65)
 alpha=np.uint8(np.clip(235*wisps**.68*envelope,0,255))
 atlas=np.empty((texsize,texsize,4),np.uint8)
 atlas[:,:,0]=244;atlas[:,:,1]=229;atlas[:,:,2]=209;atlas[:,:,3]=alpha
 image=Image.fromarray(atlas,"RGBA")
 texture_path=OUT/"run236_soft_down_alpha_texture.png";image.save(texture_path)
 # Actual Run235 surface-following ribbons are 5 vertices / 3 triangles per tuft
 assert len(ribbon.vertices)%5==0
 tuft_count=len(ribbon.vertices)//5
 uv=np.zeros((len(ribbon.vertices),2),np.float32)
 uv[0::5]=[.21,0.];uv[1::5]=[.79,0.]
 uv[2::5]=[.35,.50];uv[3::5]=[.65,.50];uv[4::5]=[.50,1.]
 ribbon.visual=trimesh.visual.TextureVisuals(uv=uv,
  material=trimesh.visual.material.PBRMaterial(
   name="wisp_alpha_down_not_solid_triangles",
   baseColorTexture=image,alphaMode="MASK",alphaCutoff=.27,
   doubleSided=True,metallicFactor=0,roughnessFactor=1))
 scene=trimesh.Scene();scene.add_geometry(core,geom_name="real_neural_owl_juvenile_core")
 scene.add_geometry(ribbon,geom_name="real_3d_surface_following_wispy_down")
 for i,part in enumerate(eye_parts):scene.add_geometry(part,geom_name="sculpt_anatomical_eye_detail_"+str(i))
 outglb=OUT/"run236_real_neural_eye_softdown_STUDY_ART_REJECTED_NO_RELEASE.glb"
 scene.export(outglb)
 opened=trimesh.load(outglb,force="scene")
 assert outglb.read_bytes()[:4]==b"glTF" and len(opened.geometry)==8
 assert all(np.isfinite(m.vertices).all() and np.ptp(m.vertices,axis=0).max()>.01 for m in opened.geometry.values())
 REPORT["source"]=filehash(SOURCE);REPORT["model"]=filehash(outglb)
 REPORT["mesh"]={"core_triangles":len(core.faces),"down_triangles":len(ribbon.faces),
   "source_surface_following_tufts":tuft_count,
   "eye_detail_triangles":sum(len(x.faces) for x in eye_parts),
   "all_real_3d_triangles":sum(len(x.faces) for x in scene.geometry.values()),
   "geometry_count":len(scene.geometry)}
 # VTK true seven-angle spatial QA: genuine 3D geometry, not billboard or photo orbit
 ren=vtk.vtkRenderer();ren.SetBackground(.89,.90,.92)
 for g in [core]+eye_parts:
  pd=vtkpoly(g.vertices,g.faces,g.visual.vertex_colors[:,:3])
  norm=vtk.vtkPolyDataNormals();norm.SetInputData(pd);norm.SplittingOff()
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norm.GetOutputPort())
  mapper.SetScalarModeToUsePointData();mapper.SetColorModeToDirectScalars()
  actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetAmbient(.31)
  ren.AddActor(actor)
 # VTK RGBA texture test for soft down, same 3D ribbon positions as exported GLB
 poly=vtk.vtkPolyData();pts=vtk.vtkPoints()
 pts.SetData(numpy_to_vtk(np.asarray(ribbon.vertices,np.float32),deep=True));poly.SetPoints(pts)
 arr=np.column_stack((np.full(len(ribbon.faces),3,np.int64),np.asarray(ribbon.faces,np.int64))).ravel()
 cells=vtk.vtkCellArray();cells.SetCells(len(ribbon.faces),numpy_to_vtkIdTypeArray(arr,deep=True))
 poly.SetPolys(cells)
 uvar=numpy_to_vtk(uv,deep=True);uvar.SetNumberOfComponents(2);poly.GetPointData().SetTCoords(uvar)
 mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
 actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetLighting(False)
 texim=vtk.vtkImageData();texim.SetDimensions(texsize,texsize,1)
 texim.AllocateScalars(vtk.VTK_UNSIGNED_CHAR,4)
 vtk_to_numpy(texim.GetPointData().GetScalars())[:,:]=np.asarray(image)[::-1].reshape(-1,4)
 tex=vtk.vtkTexture();tex.SetInputData(texim);tex.InterpolateOn();actor.SetTexture(tex)
 ren.AddActor(actor)
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(True)
 win.SetSize(540,540);win.SetMultiSamples(0);win.AddRenderer(ren)
 bounds=np.asarray(ren.ComputeVisiblePropBounds());mid=(bounds[::2]+bounds[1::2])/2
 span=float(max(bounds[1::2]-bounds[::2]))
 poses=[("front",(0,0,3)),("left",(-3,0,0)),("threequarter",(2,0,2)),
  ("right",(3,0,0)),("back",(0,0,-3)),("top",(0,3,0)),("bottom",(0,-3,0))]
 sheet=Image.new("RGB",(4*406,2*438),(238,239,242));draw=ImageDraw.Draw(sheet)
 views=[]
 for idx,(name,direction) in enumerate(poses):
  cam=ren.GetActiveCamera();cam.ParallelProjectionOn()
  cam.SetPosition(*(mid+span*np.asarray(direction,float)));cam.SetFocalPoint(*mid)
  cam.SetViewUp(*(0,1,0) if name not in ("top","bottom") else (0,0,1))
  cam.SetParallelScale(span*.68);ren.ResetCameraClippingRange();win.Render()
  f=vtk.vtkWindowToImageFilter();f.SetInput(win);f.Update()
  p=OUT/("run236_real_3d_"+name+"_ART_REJECTED.png")
  w=vtk.vtkPNGWriter();w.SetFileName(str(p));w.SetInputConnection(f.GetOutputPort());w.Write()
  pic=Image.open(p).convert("RGB")
  raw=np.asarray(pic,dtype=np.int16)
  foreground=int(np.sum(np.max(np.abs(raw-np.array([227,230,235])),axis=2)>35))
  assert foreground>6000,(name,foreground)
  sheet.paste(pic.resize((400,400)),((idx%4)*406,(idx//4)*438+24))
  draw.text(((idx%4)*406+8,(idx//4)*438+5),name,fill="#222222")
  views.append({"view":name,"foreground_pixels":foreground,**filehash(p)})
 win.Finalize()
 assert len({x["sha256"] for x in views})==7
 contact=OUT/"run236_sevenview_eye_wispy_down_ART_REJECTED_NO_RELEASE.png"
 sheet.save(contact);REPORT["contact"]=filehash(contact);REPORT["views"]=views
 REPORT["status"]="TRUE_NEURAL_3D_GLB_SEVEN_VIEWS_ART_UNAPPROVED"
 REPORT["art_reasons"]=["eyes still simplified spherical details","adult-like wing ridge and body shape",
    "soft wisps still below premium second-down fidelity",
    "no physically reviewed broad eucalyptus hollow","no physical phone WebGL/GPU measurements"]
if __name__=="__main__":
 start=time.monotonic()
 try:main()
 except Exception:
  REPORT["status"]="FAILURE_NO_RELEASE";REPORT["traceback"]=traceback.format_exc()
 finally:
  REPORT["seconds"]=round(time.monotonic()-start,2)
  (OUT/"run236_machine_report.json").write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+"\n")
  print(json.dumps(REPORT,ensure_ascii=False))
