#!/usr/bin/env python3
"""Research only: free, licensed, real glTF juvenile bird asset, anatomical negative control.
Never publish it as #172. No paid API, user-facing/prototype or main edits.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, urllib.request, struct, traceback, math, os
from PIL import Image, ImageDraw
import trimesh

OUT = Path("owl-pet/3d-experiments/172-tyto-castanops/run216-evidence")
OUT.mkdir(parents=True, exist_ok=True)
SOURCE = Path("owl-pet/design/concepts/172-tyto-castanops-v3.png")
ORIGINAL_HASH = "881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
ASSET_URL = "https://gaitkit.com/cdn/eaglet.glb"
SOURCE_PAGE = "https://gaitkit.com/asset/eaglet"
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
r = {
  "experiment": "Run216: open-access animated fluffy juvenile bird native base feasibility negative-control",
  "utc": datetime.now(timezone.utc).isoformat(),
  "target": "#172 Tyto castanops v3 rightmost age-unknown cream mesoptile",
  "source_url": SOURCE_PAGE,
  "asset_url": ASSET_URL,
  "source_has_right_species": False,
  "source_species": "Golden eagle nestling, NOT Tyto castanops",
  "reference_source_hash_expected": ORIGINAL_HASH,
  "charged_usd": 0,
  "release": "NO_RELEASE",
  "art_status": "REJECTED_DIFFERENT_FAMILY_NO_HEART_FACE",
  "mobile_hardware_test": "NOT_PERFORMED",
  "status": "STARTED"
}
try:
    assert SOURCE.is_file(), "Original v3 concept not found"
    r["reference_hash_actual"] = sha(SOURCE)
    assert r["reference_hash_actual"] == ORIGINAL_HASH, "Source art hash mismatch"
    crop = Image.open(SOURCE).convert("RGB").crop((950,255,1440,850))
    crop.save(OUT/"rightmost_v3_unmodified_reference_crop.png")
    r["crop_sha256"] = sha(OUT/"rightmost_v3_unmodified_reference_crop.png")
    req = urllib.request.Request(ASSET_URL,headers={"User-Agent":"Mozilla/5.0 owl172-research-rig-review"})
    with urllib.request.urlopen(req,timeout=45) as stream:
        r["http_status"] = stream.status
        data = stream.read(25_000_001)
    assert len(data)<25_000_001, "Source exceeded bounded 25MB cap"
    r["bytes"] = len(data)
    assert data[:4]==b"glTF" and struct.unpack_from("<I",data,4)[0]==2, "Not GLB2"
    glb = OUT/"unapproved_gaitkit_eaglet_source.glb"
    glb.write_bytes(data)
    r["source_glb_sha256"]=sha(glb)
    chunk_len, chunk_kind = struct.unpack_from("<II",data,12)
    assert chunk_kind==0x4e4f534a
    doc = json.loads(data[20:20+chunk_len])
    r["gltf_nodes"] = len(doc.get("nodes",[]))
    r["gltf_meshes"] = len(doc.get("meshes",[]))
    r["animation_clips"] = [c.get("name","unnamed") for c in doc.get("animations",[])]
    r["gltf_materials"] = len(doc.get("materials",[]))
    scene=trimesh.load(glb,force="scene",process=False)
    r["loaded_geometry_count"]=len(scene.geometry)
    r["loaded_triangles"] = sum(len(mesh.faces) for mesh in scene.geometry.values() if hasattr(mesh,"faces"))
    assert r["loaded_triangles"]>2000, "Expected real multi-part/native 3D"
    r["scene_bounds"] = scene.bounds.tolist()
    r["native_real_3d_geometry"]=True
    import vtk
    from vtk.util.numpy_support import vtk_to_numpy
    importer=vtk.vtkGLTFImporter()
    importer.SetFileName(str(glb))
    render=vtk.vtkRenderer()
    render.SetBackground(0.90,0.92,0.91)
    win=vtk.vtkRenderWindow()
    win.SetOffScreenRendering(1)
    win.SetSize(720,720)
    win.AddRenderer(render)
    importer.SetRenderWindow(win)
    importer.Update()
    bounds=scene.bounds
    center = ((bounds[0]+bounds[1])/2).tolist()
    span = float(max(bounds[1]-bounds[0]))
    focal=center
    views = {
      "front":(0,0,1),
      "back":(0,0,-1),
      "left":(-1,0,0),
      "right":(1,0,0),
      "quarter":(0.72,0.22,0.72),
      "top":(0,1,0),
      "bottom":(0,-1,0),
    }
    screenshots = []
    for label,d in views.items():
        camera=render.GetActiveCamera()
        camera.SetFocalPoint(*focal)
        camera.SetPosition(*(center[i]+d[i]*span*2.7 for i in range(3)))
        camera.SetViewUp(*( (0,0,-1) if label=="top" else (0,0,1) if label=="bottom" else (0,1,0) ))
        camera.SetViewAngle(36)
        render.ResetCameraClippingRange()
        win.Render()
        w=vtk.vtkWindowToImageFilter()
        w.SetInput(win)
        w.ReadFrontBufferOff()
        w.Update()
        im=w.GetOutput()
        widths=im.GetDimensions()
        raw=vtk_to_numpy(im.GetPointData().GetScalars())
        from PIL import Image
        import numpy as np
        rgb=np.flipud(raw.reshape((widths[1],widths[0],-1))[:,:,:3])
        p=OUT/("native_"+label+".png")
        Image.fromarray(rgb).save(p)
        screenshots.append((label,p))
    summary=Image.new("RGB",(4*420,2*450),(241,240,237))
    draw=ImageDraw.Draw(summary)
    for idx,(label,p) in enumerate(screenshots):
        tile=Image.open(p).convert("RGB").resize((410,410))
        col,row=idx%4,idx//4
        summary.paste(tile,(col*420+5,row*450+27))
        draw.text((col*420+12,row*450+7),label.upper(),fill=(25,29,35))
    small=Image.open(OUT/"rightmost_v3_unmodified_reference_crop.png").convert("RGB")
    small.thumbnail((405,412))
    summary.paste(small,(3*420+5,450+26))
    draw.text((3*420+12,450+7),"TARGET CONCEPT (NOT 3D)",fill=(25,29,35))
    summary.save(OUT/"Run216_seven_native_views_vs_target_ART_REJECTED.png")
    r["seven_view_rendered"]=True
    r["contact_sha256"]=sha(OUT/"Run216_seven_native_views_vs_target_ART_REJECTED.png")
    r["status"]="FREE_NATIVE_ANIMATED_BASE_TESTED_WRONG_SPECIES_ART_REJECTED"
except Exception as exc:
    r["status"]="TEST_ERROR_NO_RELEASE"
    r["error"]=type(exc).__name__+": "+str(exc)
    r["traceback"]=traceback.format_exc()[-4500:]
finally:
    r["utc_completed"]=datetime.now(timezone.utc).isoformat()
    files={}
    for p in sorted(OUT.iterdir()):
        if p.is_file() and p.name not in ("run216_report.json","run216_report.md"):
            files[p.name]={"bytes":p.stat().st_size,"sha256":sha(p)}
    r["evidence_files"]=files
    (OUT/"run216_report.json").write_text(json.dumps(r,ensure_ascii=False,indent=2)+"\n")
    (OUT/"run216_report.md").write_text(
      "# Run216 native juvenile-anatomy research (NO_RELEASE)\n\n"
      "Actual result: **"+r["status"]+"**. Source: "+SOURCE_PAGE+".\n\n"
      "This GLB is a golden-eagle chick, **NOT #172 Tyto castanops**. "
      "It has a different bill, facial anatomy, wing development and lacks the heart-shaped Tyto disk. "
      "No face replacement, repaint or mobile success is claimed. "
      "Free download test and original seven native views are evidence only. "
      "Do NOT publish as an owl pet. Extra paid spend $0.\n\n"
      "Raw metrics and SHA256 per file: [run216_report.json](run216_report.json).\n")
    print(json.dumps({k:v for k,v in r.items() if k!="traceback"},ensure_ascii=False,indent=2))
