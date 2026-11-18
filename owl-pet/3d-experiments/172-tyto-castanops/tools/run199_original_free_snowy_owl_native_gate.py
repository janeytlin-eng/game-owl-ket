#!/usr/bin/env python3
"""Run199: real, zero-fee native GLB source transport, license and art negative gate.

Never redistributes source model binary. A generic snowy owl + fox is NOT the
age-unknown Tyto castanops v3 rightmost mesoptile, irrespective of actual GLB quality.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import traceback
import requests

R=Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run199-SHURIKEN-FREE-NATIVE-ART_REJECTED-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
TEMP=Path("/tmp/owl172-run199-original-private.glb")
SOURCE="https://shuriken.studio/models/characters/arctic-fox-and-snowy-owl"
LICENSE="https://shuriken.studio/legal/models"
DOWNLOAD="https://shuriken.studio/models/download/30ef3435-cec4-4cec-9c93-90f501ac5b06"
EXPECTED_REFERENCE_SHA="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
result={
 "run":199,"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "target":"172 Tyto castanops v3 rightmost age-unknown cream mesoptile",
 "source_url":SOURCE,"license_url":LICENSE,"download_url":DOWNLOAD,
 "total_paid_usd":0,"native_glb_acquired":False,"source_is_target_species":False,
 "source_has_target_morphology":False,"candidate_art_approved":False,
 "physical_mobile_gpu_approved":False,"no_release":True,
 "result":"SOURCE_CHECK_STARTED","network":[],"errors":[]}
(O/"NO_RELEASE.flag").write_text("NEGATIVE ART GATE: wrong adult stylized snowy owl + fox kit; no infant Tyto mesoptile and no physical smartphone validation.\n")
s=requests.Session()
s.headers.update({"User-Agent":"Mozilla/5.0 (compatible; free-asset-verification/1.0)"})
def get_and_record(url, name, maxbytes):
    resp=s.get(url,timeout=(16,42),allow_redirects=True,stream=True)
    status={"url":url,"status":resp.status_code,"final_url":resp.url,
            "content_type":resp.headers.get("content-type"),"content_length":resp.headers.get("content-length")}
    result["network"].append(status)
    raw=b""
    for chunk in resp.iter_content(chunk_size=32768):
        raw+=chunk
        if len(raw)>maxbytes:raise RuntimeError("MAX_BYTES_EXCEEDED "+name)
    status["body_bytes"]=len(raw)
    status["body_sha256"]=hashlib.sha256(raw).hexdigest()
    if name in ("source","license"):
        (O/(name+"_response_excerpt.txt")).write_text(raw.decode("utf-8",errors="replace")[:25000])
    return resp,raw
try:
    for name,url in (("source",SOURCE),("license",LICENSE)):
        resp,_=get_and_record(url,name,700000)
        if resp.status_code!=200:raise RuntimeError(name+" HTTP "+str(resp.status_code))
    licence=(O/"license_response_excerpt.txt").read_text(errors="replace").lower()
    result["license_readable"]=True
    result["licence_excludes_reposting_source_files"]=("don't sell or share" in licence or "do not" in licence and "redistribut" in licence)
    resp,b=get_and_record(DOWNLOAD,"native_glb",5_000_000)
    result["native_http_status"]=resp.status_code
    if resp.status_code!=200:raise RuntimeError("NATIVE_HTTP_"+str(resp.status_code))
    if len(b)<1000 or b[:4]!=b"glTF":
        raise RuntimeError("NOT_GLB_MAGIC content-type="+str(resp.headers.get("content-type"))+" header="+repr(b[:36]))
    TEMP.write_bytes(b)  # intentionally outside repo and evidence artifact; no raw source redistribution
    result["native_glb_acquired"]=True
    result["glb_bytes"]=len(b)
    result["glb_sha256"]=hashlib.sha256(b).hexdigest()
    import trimesh
    scene=trimesh.load(str(TEMP),force="scene",process=False)
    geoms=[g for g in scene.geometry.values() if isinstance(g,trimesh.Trimesh)]
    if not geoms:raise RuntimeError("GLB_IMPORT_EMPTY_MESH")
    result["geometry"]={"mesh_count":len(geoms),
        "triangles":sum(len(g.faces) for g in geoms),
        "vertices":sum(len(g.vertices) for g in geoms),
        "bounds":scene.bounds.tolist(),
        "geometry_names":list(scene.geometry.keys())[:80],
        "material_names":[str(getattr(g.visual.material,"name","")) for g in geoms if hasattr(g.visual,"material")][:30]}
    (O/"run199_native_geometry.json").write_text(json.dumps(result["geometry"],indent=2,ensure_ascii=False)+"\n")
    result["result"]="REAL_GLTF_ACQUIRED_BUT_ART_REJECTED_GENERIC_ADULT_SNOWY_OWL_AND_FOX"
    # Real import/renderer; never call an SVG, mock or procedural geometry a character model.
    try:
        import vtk
        from PIL import Image,ImageDraw
        win=vtk.vtkRenderWindow()
        win.SetOffScreenRendering(1);win.SetSize(600,600)
        imp=vtk.vtkGLTFImporter();imp.SetFileName(str(TEMP));imp.SetRenderWindow(win);imp.Update()
        renderer=win.GetRenderers().GetFirstRenderer()
        if not renderer:raise RuntimeError("NO_NATIVE_RENDERER")
        renderer.SetBackground(.21,.24,.27)
        renderer.SetBackground2(.31,.35,.39)
        renderer.GradientBackgroundOn()
        bounds=renderer.ComputeVisiblePropBounds()
        if not bounds or bounds[0]>=bounds[1]:raise RuntimeError("NO_NATIVE_PROP_BOUNDS")
        center=[(bounds[i]+bounds[i+1])/2 for i in (0,2,4)]
        radius=max(bounds[1]-bounds[0],bounds[3]-bounds[2],bounds[5]-bounds[4],.1)
        vectors={"front":(0,0,1),"right":(1,0,0),"back":(0,0,-1),"left":(-1,0,0),
                 "top":(0,1,0),"bottom":(0,-1,0),"quarter":(.72,.26,.72)}
        imgs=[]
        for name,v in vectors.items():
            cam=renderer.GetActiveCamera()
            cam.SetFocalPoint(*center)
            cam.SetPosition(*(center[i]+v[i]*radius*2.8 for i in range(3)))
            cam.SetViewUp(0,0,-1) if name in ("top","bottom") else cam.SetViewUp(0,1,0)
            cam.ParallelProjectionOn();cam.SetParallelScale(radius*.8)
            renderer.ResetCameraClippingRange()
            win.Render()
            filter=vtk.vtkWindowToImageFilter();filter.SetInput(win)
            filter.SetInputBufferTypeToRGB();filter.ReadFrontBufferOff();filter.Update()
            png=O/("run199_NATIVE_"+name+".png")
            w=vtk.vtkPNGWriter();w.SetFileName(str(png));w.SetInputConnection(filter.GetOutputPort());w.Write()
            if not png.exists() or png.stat().st_size<3000:raise RuntimeError("EMPTY_RENDER "+name)
            imgs.append(png)
        contact=Image.new("RGB",(4*360,2*385),(26,30,34)); draw=ImageDraw.Draw(contact)
        for i,p in enumerate(imgs):
            im=Image.open(p).convert("RGB"); im.thumbnail((350,346))
            x=i%4*360+(360-im.width)//2; y=i//4*385
            contact.paste(im,(x,y))
            draw.text((i%4*360+9,y+350),p.stem.replace("run199_NATIVE_",""),fill=(245,245,245))
        contact.save(O/"run199_REAL_SEVENVIEW_CONTACT.png")
        result["native_render"]={"renderer":"VTK "+vtk.vtkVersion.GetVTKVersion()+" real imported original GLB",
            "rendered_seven_views":True,"views":[p.name for p in imgs],
            "binary_sha256":result["glb_sha256"],"original_binary_not_redistributed":True}
    except Exception as e:
        result["native_render"]={"rendered_seven_views":False,"error":repr(e)}
        (O/"native_render_traceback.txt").write_text(traceback.format_exc())
except Exception as e:
    result["errors"].append(repr(e))
    if not result["native_glb_acquired"]:
        result["result"]="SOURCE_OR_TRANSPORT_BLOCKED_NO_NATIVE_GLB"
    (O/"source_traceback.txt").write_text(traceback.format_exc())
finally:
    # File remains only on isolated runner temp disk, outside source/release and artifacts.
    TEMP.unlink(missing_ok=True)
    result["candidate_art_approved"]=False
    result["no_release"]=True
    (O/"run199_result.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"run":199,"status":result["result"],"native_glb":result["native_glb_acquired"],
           "rendered_views":result.get("native_render",{}).get("rendered_seven_views"),
           "sha256":result.get("glb_sha256"),"errors":result["errors"],"NO_RELEASE":True},ensure_ascii=False))
