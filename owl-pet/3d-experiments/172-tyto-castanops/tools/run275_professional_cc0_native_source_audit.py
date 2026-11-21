#!/usr/bin/env python3
"""Run275: acquire and inspect independently licensed professional owl sources.
Actual GLB bytes, multi-view renders, structural QA, NO_RELEASE.
No transformations into a fake juvenile; all source rights separately recorded.
"""
import os, json, hashlib, struct, time, urllib.request, urllib.error, traceback
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
import trimesh
import vtk

OUT = Path(os.environ.get("OWL172_OUTPUT", "run275-output"))
OUT.mkdir(parents=True, exist_ok=True)
SOURCES = {
    "grab3d_cc0_horned_adult_light": {
       "url": "https://grab3d.com/dl/owl/owl-light.glb",
       "license": "CC0 stated on https://grab3d.com/models/animals/owl/",
       "declared_bytes": 13356032,
       "disclosed_origin": "Meshy AI-assisted base and Blender cleanup",
       "subject": "great horned adult, NOT target Tyto juvenile"
    },
    "innerscene_cc0_owl": {
       "url": "https://www.innerscene.com/api/library/owl-d696472a/download",
       "license": "CC0 stated on https://www.innerscene.com/tools/library/3d-parts/owl-d696472a",
       "declared_bytes": None,
       "disclosed_origin": "Innerscene original model per page, not independently audited",
       "subject": "generic owl, target identification UNCONFIRMED"
    }
}
def sha(b): return hashlib.sha256(b).hexdigest()
def fetch(url, dest):
    request=urllib.request.Request(url,headers={"User-Agent":"owl172-research-asset-audit/1.0","Accept":"model/gltf-binary,application/octet-stream,*/*"})
    with urllib.request.urlopen(request,timeout=90) as response:
        status=response.status
        ctype=response.headers.get("Content-Type","")
        n=0
        with dest.open("wb") as f:
            while True:
                chunk=response.read(1024*1024)
                if not chunk:break
                n+=len(chunk)
                if n>75_000_000: raise RuntimeError("asset exceeds 75 MB hard limit")
                f.write(chunk)
    return {"http_status":status,"content_type":ctype,"bytes":n}

def header(p):
    with p.open("rb") as f:
        head=f.read(20)
        if len(head)<20 or head[:4]!=b"glTF":
            raise ValueError("download not real glTF binary")
        magic,version,total,chunklen,kind=struct.unpack("<4sIIII",head)
        assert version==2 and kind==0x4e4f534a and total==p.stat().st_size
        data=json.loads(f.read(chunklen).decode())
    return data

def render(glb, label, scene):
    window=vtk.vtkRenderWindow();window.SetOffScreenRendering(1);window.SetSize(390,390)
    imp=vtk.vtkGLTFImporter()
    imp.SetFileName(str(glb));imp.SetRenderWindow(window);imp.Update()
    ren=window.GetRenderers().GetFirstRenderer()
    ren.SetBackground(.77,.80,.83)
    b=np.asarray(scene.bounds,float)
    center=b.mean(axis=0)
    scale=float(max(np.ptp(b,axis=0).max(),1e-4))
    ren.RemoveAllLights()
    for xyz,intensity in [((2,4,5),1.1),((-3,2,-2),.65)]:
        light=vtk.vtkLight()
        light.SetPosition(*(center+np.asarray(xyz)*scale))
        light.SetFocalPoint(*center);light.SetIntensity(intensity)
        ren.AddLight(light)
    viewpoints={"front":(0,0,1),"quarter":(.8,.15,.9),"right":(1,0,0),
                "back":(0,0,-1),"left":(-1,0,0),"above":(0,1,.24)}
    report={}
    canvas=Image.new("RGB",(390*3,390*2),(232,232,232))
    dr=ImageDraw.Draw(canvas)
    for i,(name,d) in enumerate(viewpoints.items()):
        v=np.asarray(d,float);v/=np.linalg.norm(v)
        cam=ren.GetActiveCamera()
        cam.SetFocalPoint(*center);cam.SetPosition(*(center+3.1*scale*v))
        cam.SetViewUp(*((0,0,-1) if abs(v[1])>.9 else (0,1,0)))
        cam.ParallelProjectionOn();cam.SetParallelScale(scale*.7)
        ren.ResetCameraClippingRange();window.Render()
        extract=vtk.vtkWindowToImageFilter();extract.SetInput(window);extract.Update()
        dest=OUT/(label+"_"+name+"_real_3d.png")
        writer=vtk.vtkPNGWriter();writer.SetFileName(str(dest))
        writer.SetInputConnection(extract.GetOutputPort());writer.Write()
        x,y=(i%3)*390,(i//3)*390
        canvas.paste(Image.open(dest).convert("RGB"),(x,y))
        dr.text((x+6,y+6),name,fill=(24,24,24))
        report[name]={"sha256":sha(dest.read_bytes()),"bytes":dest.stat().st_size}
    sheet=OUT/(label+"_six_genuine_3d_views.png")
    canvas.save(sheet,optimize=True)
    assert len({v["sha256"] for v in report.values()})==6,"camera shots identical"
    window.Finalize()
    return {"views":report,"sheet_sha256":sha(sheet.read_bytes())}

report={"run":275,"date":"2026-11-22","research_only":True,"release":False,
 "art":"UNREVIEWED","phone_hardware":"UNTESTED","license_provenance_needs_further_review":True,
 "sources":{}}
for label,meta in SOURCES.items():
    item={"source":meta}
    path=OUT/(label+".glb")
    try:
        item["transfer"]=fetch(meta["url"],path)
        if meta["declared_bytes"]:
            assert path.stat().st_size==meta["declared_bytes"], "supplier manifest length mismatch"
        gltf=header(path)
        item["sha256"]=sha(path.read_bytes())
        item["gltf"]={"meshes":len(gltf.get("meshes",[])),
                      "materials":len(gltf.get("materials",[])),
                      "images":len(gltf.get("images",[])),
                      "skins":len(gltf.get("skins",[])),
                      "animations":len(gltf.get("animations",[])),
                      "extensions":gltf.get("extensionsUsed",[])}
        scene=trimesh.load(path,force="scene")
        item["geometry"]={"scene_geometry_count":len(scene.geometry),
          "triangles":int(sum(len(g.faces) for g in scene.geometry.values() if hasattr(g,"faces"))),
          "bounds":np.asarray(scene.bounds).tolist(),
          "finite":bool(np.isfinite(scene.bounds).all())}
        if item["geometry"]["triangles"]<1000: raise RuntimeError("not sufficiently detailed for source QA")
        item["actual_renders"]=render(path,label,scene)
        item["status"]="REAL_3D_ACQUIRED_AND_MULTIVIEW_RENDERED_NOT_ACCEPTED"
    except Exception as e:
        item["status"]="BLOCKED_OR_INVALID"
        item["error"]=type(e).__name__+": "+str(e)
        item["traceback_tail"]=traceback.format_exc()[-1200:]
    report["sources"][label]=item
    print(label, json.dumps(item,ensure_ascii=False)[:2000],flush=True)
(OUT/"machine-report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
(OUT/"NO_RELEASE.flag").write_text("EXTERNAL ASSETS ARE UNREVIEWED / NOT A TYTO CASTANOPS JUVENILE / NO_RELEASE\n")
files=[p for p in OUT.rglob("*") if p.is_file() and p.name!="SHA256SUMS.txt"]
(OUT/"SHA256SUMS.txt").write_text("".join(sha(p.read_bytes())+"  "+str(p.relative_to(OUT))+"\n" for p in sorted(files)))
