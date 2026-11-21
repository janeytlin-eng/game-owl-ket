#!/usr/bin/env python3
"""Run276: acquire and inspect artist-authored freely downloadable rigged owl assets, with animation metadata.
Actual GLB bytes, multi-view renders, structural QA, NO_RELEASE.
No transformations into a fake juvenile; all source rights separately recorded.
"""
import os, json, hashlib, struct, time, urllib.request, urllib.error, traceback
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
import trimesh
import vtk

OUT = Path(os.environ.get("OWL172_OUTPUT", "run276-output"))
OUT.mkdir(parents=True, exist_ok=True)
SOURCES = {
  "gobkit_barnowl_rigged_cc0": {
    "url": "https://gobkit.com/freebies/animal013/BarnOwl.glb",
    "license": "Supplier CC0 claim at https://github.com/Ariescar/gobkit-free-assets and https://gobkit.com/api/free",
    "declared_bytes": None,
    "disclosed_origin": "Gobkit original game asset; supplier license not independently chain-audited",
    "subject": "Barn owl (age unknown), possible animation skeleton donor, NOT target accepted chick"
  },
  "gobkit_chick_rigged_cc0": {
    "url": "https://gobkit.com/freebies/animal007/Chick.glb",
    "license": "Supplier CC0 claim at https://github.com/Ariescar/gobkit-free-assets and https://gobkit.com/api/free",
    "declared_bytes": None,
    "disclosed_origin": "Gobkit original game asset, source license independently unverified",
    "subject": "Different taxon domestic chick, juvenile proportion reference ONLY"
  },
  "gobkit_generic_owl_rigged_cc0": {
    "url": "https://gobkit.com/freebies/animalB/Owl.glb",
    "license": "Supplier CC0 claim at https://github.com/Ariescar/gobkit-free-assets and https://gobkit.com/api/free",
    "declared_bytes": None,
    "disclosed_origin": "Gobkit original game asset, source license independently unverified",
    "subject": "Generic owl rig donor negative control, NOT exact species"
  },
  "gobkit_agentowl_rigged_cc0": {
    "url": "https://gobkit.com/freebies/animal013/Agentowl.glb",
    "license": "Supplier CC0 claim at https://github.com/Ariescar/gobkit-free-assets and https://gobkit.com/api/free",
    "declared_bytes": None,
    "disclosed_origin": "Gobkit original game asset, source license independently unverified",
    "subject": "Stylized character rig negative control, NOT target chick"
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

def animation_skin_audit(gltf):
    """Check actual glTF rig/clip structures without claiming visual animation success."""
    animations=gltf.get("animations", [])
    skins=gltf.get("skins", [])
    primitives=[p for m in gltf.get("meshes",[]) for p in m.get("primitives",[])]
    skin_primitives=sum("JOINTS_0" in p.get("attributes",{}) and "WEIGHTS_0" in p.get("attributes",{}) for p in primitives)
    skin_joints=[len(s.get("joints",[])) for s in skins]
    clips=[]
    for a in animations:
        channels=a.get("channels", [])
        samplers=a.get("samplers", [])
        target_nodes={ch.get("target",{}).get("node") for ch in channels}
        clips.append({"name":a.get("name","(unnamed)"),
                      "samplers":len(samplers),
                      "channels":len(channels),
                      "affected_nodes":len(target_nodes),
                      "paths":sorted(set(ch.get("target",{}).get("path","?") for ch in channels))})
    return {"skins":len(skins), "joint_counts":skin_joints,
            "mesh_primitives":len(primitives),
            "skinned_primitives":skin_primitives,
            "animation_clip_count":len(animations),
            "clips":clips,
            "actual_skeleton_evaluation_in_webgl":"PENDING browser QA",
            "real_animation_in_mobile_hardware":"UNTESTED"}

report={"run":276,"date":"2026-11-22","research_only":True,"release":False,
 "art":"LOW_POLYGON_COUNT_AUTOMATED_REJECTION_NOT_VISUAL_APPROVAL","phone_hardware":"UNTESTED","license_provenance_needs_further_review":True,
 "sources":{},"rigged_candidate_quality":"UNREVIEWED"}
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
        item["rig_audit"]=animation_skin_audit(gltf)
        scene=trimesh.load(path,force="scene")
        item["geometry"]={"scene_geometry_count":len(scene.geometry),
          "triangles":int(sum(len(g.faces) for g in scene.geometry.values() if hasattr(g,"faces"))),
          "bounds":np.asarray(scene.bounds).tolist(),
          "finite":bool(np.isfinite(scene.bounds).all())}
        item["art_density_gate"] = ("AUTO_REJECT_TOO_FEW_TRIANGLES_NOT_FUZZY_CHICK" if item["geometry"]["triangles"]<1000 else "UNREVIEWED_NEEDS_VISUAL")
        item["actual_renders"]=render(path,label,scene)
        item["status"]="REAL_NATIVE_SKINNED_MULTIVIEW_LOW_POLY_ART_REJECTED_NO_RELEASE" if item["geometry"]["triangles"]<1000 else "REAL_NATIVE_SKINNED_MULTIVIEW_ART_UNREVIEWED_NO_RELEASE"
    except Exception as e:
        item["status"]="BLOCKED_OR_INVALID"
        item["error"]=type(e).__name__+": "+str(e)
        item["traceback_tail"]=traceback.format_exc()[-1200:]
    report["sources"][label]=item
    print(label, json.dumps(item,ensure_ascii=False)[:2000],flush=True)
(OUT/"machine-report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
(OUT/"NO_RELEASE.flag").write_text("RIG SOURCES UNREVIEWED; WRONG AGE/STYLE UNTIL CONFIRMED; NO RELEASE\n")
files=[p for p in OUT.rglob("*") if p.is_file() and p.name!="SHA256SUMS.txt"]
(OUT/"SHA256SUMS.txt").write_text("".join(sha(p.read_bytes())+"  "+str(p.relative_to(OUT))+"\n" for p in sorted(files)))
