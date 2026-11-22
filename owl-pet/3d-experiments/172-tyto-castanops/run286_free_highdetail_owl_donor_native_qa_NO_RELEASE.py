#!/usr/bin/env python3
"""#172 research-only source acquisition and independent true-3D six-view QA.
No kitten, production, concept images or main changes. No model promoted to pet.
"""
import io, os, json, pathlib, hashlib, traceback, urllib.request, urllib.error
import numpy as np
from PIL import Image, ImageOps, ImageDraw
import trimesh
import vtk
from vtk.util.numpy_support import vtk_to_numpy

OUT=pathlib.Path(os.environ.get("OWL286_OUTPUT","run286_evidence"))
OUT.mkdir(parents=True,exist_ok=True)
BASE="https://grab3d.com/dl/owl"
SOURCES={
 "manifest": BASE+"/manifest.json",
 "license": BASE+"/LICENSE.txt",
 "full_reference_listing": "https://grab3d.com/models/animals/owl/",
 "light_glb": BASE+"/owl-light.glb"
}
def sha(path): return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
report={"run":"286","target":"#172 Tyto castanops v3 rightmost cream owlet",
        "purpose":"actual acquisition / 3D structure of free professional texture donor",
        "requested_art":"cream down, heart facial disc, juvenile, natural sides/back, grasping feet",
        "asset_candidate":"Grab3D public CC0 great horned owl (adult, different species)",
        "license_status":"site CC0 claim; uploader provenance independently unverified",
        "art":"ART_REJECTED_BY_SPECIES_AND_AGE","mobile":"UNTESTED",
        "release":False,"paid_usd":0,"sources":SOURCES,"download":{}}
headers={"User-Agent":"owl172-research-evidence/1.0 (no automation purchase)"}
for name in ["manifest","license","full_reference_listing","light_glb"]:
 url=SOURCES[name];rec={"url":url}
 try:
  req=urllib.request.Request(url,headers=headers)
  with urllib.request.urlopen(req,timeout=90) as resp:
   data=resp.read(40000000);rec["status"]=resp.status
   rec["content_type"]=resp.headers.get("Content-Type","")
  rec["bytes"]=len(data);rec["sha256"]=hashlib.sha256(data).hexdigest()
  if name=="light_glb":
   rec["magic"]=data[:4].decode("ascii","replace")
   if rec["magic"]!="glTF" or len(data)<1000000:
    raise ValueError("not a real source GLB / too small")
   (OUT/"grab3d_owl_light_DONOR_REJECTED_NO_RELEASE.glb").write_bytes(data)
  else:
   (OUT/{"manifest":"source_manifest.json","license":"source_license.txt","full_reference_listing":"source_listing.html"}[name]).write_bytes(data[:400000])
 except Exception as e:
  rec["error"]=type(e).__name__+": "+str(e)[:350]
 report["download"][name]=rec
(OUT/"download_probe.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
if "error" in report["download"]["light_glb"]:
 report["geometry"]="UNAVAILABLE";(OUT/"run286_report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
 print("SOURCE_BLOCKED:",report["download"]["light_glb"]);raise SystemExit(0)

p=OUT/"grab3d_owl_light_DONOR_REJECTED_NO_RELEASE.glb"
sc=trimesh.load(p,force="scene",process=False)
mesh_parts=[g for g in sc.geometry.values() if isinstance(g,trimesh.Trimesh)]
triangles=sum(len(m.faces) for m in mesh_parts)
vertices=sum(len(m.vertices) for m in mesh_parts)
report["geometry"]={"true_native_glb":True,"mesh_count":len(mesh_parts),"triangles":triangles,
                    "vertices":vertices,"scene_bounds":np.asarray(sc.bounds).tolist(),
                    "glb_sha256":sha(p),"file_bytes":p.stat().st_size}
if not mesh_parts or triangles<100000:raise RuntimeError("expected high detail native mesh, not acquired")
# VTK directly imports original GLB with its actual texture/materials; each view moves a real 3D camera.
ren=vtk.vtkRenderer()
win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(420,420);win.AddRenderer(ren)
imp=vtk.vtkGLTFImporter();imp.SetFileName(str(p));imp.SetRenderWindow(win);imp.Update()
bounds=ren.ComputeVisiblePropBounds()
center=np.array([(bounds[0]+bounds[1])/2,(bounds[2]+bounds[3])/2,(bounds[4]+bounds[5])/2])
size=np.array([bounds[1]-bounds[0],bounds[3]-bounds[2],bounds[5]-bounds[4]])
radius=float(max(size))*2.3
ren.SetBackground(.94,.92,.88);cam=ren.GetActiveCamera();cam.SetViewAngle(28)
positions=[("front_posZ",(0,0,1),(0,1,0)),("quarter_XZ",(0.7,.08,0.7),(0,1,0)),
           ("right_posX",(1,0,0),(0,1,0)),("back_negZ",(0,0,-1),(0,1,0)),
           ("left_negX",(-1,0,0),(0,1,0)),("top_posY",(0,1,0),(0,0,-1))]
views=[]
for name,axis,up in positions:
 cam.SetPosition(*(center+radius*np.asarray(axis)));cam.SetFocalPoint(*center)
 cam.SetViewUp(*up);cam.SetClippingRange(.01,100*radius)
 win.Render()
 filt=vtk.vtkWindowToImageFilter();filt.SetInput(win);filt.SetInputBufferTypeToRGB();filt.ReadFrontBufferOff();filt.Update()
 writer=vtk.vtkPNGWriter();writer.SetFileName(str(OUT/(name+".png")));writer.SetInputConnection(filt.GetOutputPort());writer.Write()
 img=Image.open(OUT/(name+".png")).convert("RGB")
 views.append((name,img.copy()))
contact=Image.new("RGB",(1260,880),(246,244,239));d=ImageDraw.Draw(contact)
for i,(name,img) in enumerate(views):
 x=(i%3)*420;y=(i//3)*440;contact.paste(img,(x,y))
 d.rectangle((x,y+418,x+419,y+439),fill=(248,245,238));d.text((x+10,y+424),name,fill=(55,45,35))
contact.save(OUT/"real_six_camera_contact_RESEARCH.png")
report["render"]={"status":"VTK_NATIVE_GLTF_SIX_VIEWS","camera_count":len(views),
                  "bounding_box":list(bounds),"engine":"VTK GLTF importer offscreen CPU/software"}
report["art"]="ART_REJECTED: source is an adult horned owl, wrong species, tufted head, no infant down or heart-disc"
report["mobile"]="UNTESTED: 400k triangle asset not mobile budget certified"
(OUT/"run286_report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
manifest=[]
for f in sorted(OUT.iterdir()):
 if f.name=="SHA256SUMS.txt" or not f.is_file():continue
 manifest.append(sha(f)+"  "+f.name)
(OUT/"SHA256SUMS.txt").write_text("\n".join(manifest)+"\n")
(OUT/"STATUS_NO_RELEASE.txt").write_text(
 "TRUE_NATIVE_3D_SOURCE_CHECK_PASS / ADULT_WRONG_SPECIES / ART_REJECTED / PHONE_UNTESTED / NO_RELEASE\n")
print(json.dumps({k:report[k] for k in ["geometry","render","art","release"]},indent=2))
