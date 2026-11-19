#!/usr/bin/env python3
"""Run202: genuine source-bound Tyto alba sculpt probe. NEVER art approve/release."""
import hashlib, json, os, sys, traceback, urllib.request
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=ROOT/"research-evidence-run202b-PUBLIC-TYTO-MESA-RECOVERY-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)
SOURCE="https://huggingface.co/datasets/allenai/objaverse/resolve/main/glbs/000-081/19c989a6681145bc999c332699eb852e.glb"
PUBLISHER="Innovation Studio / Common Barn Owl / Sketchfab UID 19c989a6681145bc999c332699eb852e"
SOURCE_LICENSE="CC BY 4.0 as registered in independent PhenoVoxel Archive model-assets.json and source licensing table; independently confirm before any distribution"
EXPECTED="29531600a1f221f6fbb8dded12cee4ceea4251b28bd678c494d947dc4c3fc3aa"
status={"run":"202b","date_utc":datetime.now(timezone.utc).isoformat(),
        "source":SOURCE,"publisher":PUBLISHER,"license_claim":SOURCE_LICENSE,
        "target":"Tyto castanops v3 AGE-UNKNOWN MESOPTILE RIGHTMOST CREAM SECOND DOWN",
        "expected_sha256":EXPECTED,"source_http":None,"new_native_glb":False,
        "sevenview":False,"physical_phone_gpu":False,"art_approved":False,
        "final_status":"NO_RELEASE","errors":[],"events":[]}
def event(s):status["events"].append(str(s));print(s,flush=True)
def save():
    (OUT/"run202_status.json").write_text(json.dumps(status,indent=2,ensure_ascii=False)+"\n")
    (OUT/"NO_RELEASE.flag").write_text("NO_RELEASE: adult alternate-taxon donor, no reviewed cream mesoptile, no physical phone GPU.\n")
def block(message):
    status["errors"].append(str(message))
    event("BLOCK "+str(message))
    status["final_status"]="SOURCE_OR_NATIVE_QA_BLOCKED_NO_RELEASE"
    save()
def main():
    for p in ["owl-pet/README.md","owl-pet/AGENTS.md",
              "owl-pet/prototype/index.html",
              "owl-pet/research/species/172-tyto-castanops-v3.md",
              str(ROOT/"known_rejected_asset_sha256_registry.json"),
              str(ROOT/"2026-11-19-run201d-hf-zerogpu-quota-original-source-correction-NO_RELEASE.md")]:
        assert Path(p).stat().st_size>10,p
        event("preflight "+p+" "+hashlib.sha256(Path(p).read_bytes()).hexdigest())
    image=ROOT/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED"/"rightmost_mesoptile_input.png"
    targetsha=hashlib.sha256(image.read_bytes()).hexdigest()
    assert targetsha=="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
    status["reference_sha256"]=targetsha
    reg=(ROOT/"known_rejected_asset_sha256_registry.json").read_text()
    if EXPECTED in reg:
        status["final_status"]="EXACT_KNOWN_REJECTED_SOURCE_NO_RELEASE"
        event("source SHA already in rejected hash registry: skip network")
        save();return
    status["license_record"]={
        "publisher":"Innovation Studio","work":"Common Barn Owl",
        "source":"https://sketchfab.com/3d-models/common-barn-owl-19c989a6681145bc999c332699eb852e",
        "secondary_documentation":"https://github.com/canopico-world/PhenoVoxel-Archive/blob/main/ASSET-LICENSES.md",
        "license":"CC BY 4.0 per secondary archive; original source rights not independently revalidated"}
    import requests
    res=requests.get(SOURCE,timeout=(16,70),headers={"User-Agent":"owl172-source-qa/2026"},allow_redirects=True)
    status["source_http"]=res.status_code
    status["resolved_host"]=res.url.split("/")[2]
    status["response_mime"]=res.headers.get("content-type")
    status["response_bytes"]=len(res.content)
    event("download HTTP "+str(res.status_code)+" len="+str(len(res.content))+" mime="+str(res.headers.get("content-type")))
    if res.status_code!=200:raise RuntimeError("source HTTP="+str(res.status_code))
    raw=res.content
    if len(raw)<20 or raw[:4]!=b"glTF":raise RuntimeError("NOT_GLB_MAGIC")
    sha=hashlib.sha256(raw).hexdigest()
    status["native_sha256"]=sha
    status["native_bytes"]=len(raw)
    if sha!=EXPECTED:raise RuntimeError("PINNED_GLB_SHA_MISMATCH; expected="+EXPECTED+" got="+sha)
    if sha in reg:
        status["final_status"]="EXACT_KNOWN_REJECTED_SOURCE_NO_RELEASE";save();return
    glb=OUT/"artist_tyto_alba_original_restricted_review.glb"
    glb.write_bytes(raw)
    import trimesh
    scene=trimesh.load(glb,force="scene",process=False)
    geom=list(scene.geometry.values())
    status["geometry"]={"meshes":len(geom),
        "vertices":sum(len(getattr(g,"vertices",[])) for g in geom),
        "faces":sum(len(getattr(g,"faces",[])) for g in geom),
        "material_count":len(set(str(getattr(getattr(g,"visual",None),"material",None))[:80] for g in geom)),
        "bounds":scene.bounds.tolist(),
        "scaling":scene.scale}
    status["new_native_glb"]=True
    status["final_status"]="REAL_ADULT_TYTO_GLB_IMPORTED_RENDER_PENDING_NO_RELEASE"
    event("TRIMESH_IMPORTED "+json.dumps(status["geometry"]))
    # Durable checkpoint before native renderer; a C++ VTK crash cannot suppress true source evidence.
    save()
    try:
        import vtk
        vtk.vtkObject.GlobalWarningDisplayOff()
        importer=vtk.vtkGLTFImporter()
        importer.SetFileName(str(glb))
        render_window=vtk.vtkRenderWindow()
        render_window.SetOffScreenRendering(1)
        render_window.SetSize(720,720)
        # vtkGLTFImporter owns the first renderer. Do not attach a separate one before Update.
        importer.SetRenderWindow(render_window)
        importer.Update()
        renderer=render_window.GetRenderers().GetFirstRenderer()
        if renderer is None:
            raise RuntimeError("vtkGLTFImporter provided no renderer")
        renderer.SetBackground(0.86,0.86,0.83)
        actors=renderer.GetActors()
        status["vtk_actors"]=actors.GetNumberOfItems()
        renderer.ResetCamera()
        bounds=renderer.ComputeVisiblePropBounds()
        center=[(bounds[2*i]+bounds[2*i+1])/2 for i in range(3)]
        lengths=[bounds[2*i+1]-bounds[2*i] for i in range(3)]
        radius=max(lengths)*2.0
        views={
          "front":((0,0,1),(0,1,0)),
          "right":((1,0,0),(0,1,0)),
          "back":((0,0,-1),(0,1,0)),
          "left":((-1,0,0),(0,1,0)),
          "top":((0,1,0),(0,0,-1)),
          "bottom":((0,-1,0),(0,0,1)),
          "quarter":((0.7,0.3,1),(0,1,0))}
        import numpy as np
        photos=[]
        for name,(direction,up) in views.items():
            d=np.array(direction,dtype=float);d/=np.linalg.norm(d)
            cam=renderer.GetActiveCamera()
            cam.SetFocalPoint(*center)
            cam.SetPosition(*(np.array(center)+radius*d))
            cam.SetViewUp(*up)
            cam.ParallelProjectionOn()
            cam.SetParallelScale(max(lengths)*0.71)
            renderer.ResetCameraClippingRange()
            render_window.Render()
            w=vtk.vtkWindowToImageFilter();w.SetInput(render_window);w.SetInputBufferTypeToRGB();w.ReadFrontBufferOff();w.Update()
            f=OUT/("native_"+name+".png")
            writer=vtk.vtkPNGWriter();writer.SetFileName(str(f));writer.SetInputConnection(w.GetOutputPort());writer.Write()
            from PIL import Image
            im=Image.open(f).convert("RGB");photos.append((name,im.copy()))
            event("rendered "+name+" size="+str(f.stat().st_size))
        from PIL import Image,ImageDraw
        sheet=Image.new("RGB",(720*4,756*2),(245,245,243))
        draw=ImageDraw.Draw(sheet)
        for i,(name,im) in enumerate(photos):
            x=(i%4)*720;y=(i//4)*756
            sheet.paste(im,(x,y+30));draw.text((x+12,y+9),name,fill=(0,0,0))
        sheet.save(OUT/"native_contact.png")
        status["sevenview"]=all((OUT/("native_"+v+".png")).stat().st_size>1000 for v in views)
        event("native sevenview "+str(status["sevenview"]))
    except Exception as e:
        status["errors"].append("VTK_RENDER_FAILED: "+repr(e))
        (OUT/"native_vtk_error.txt").write_text(traceback.format_exc())
        event("VTK_RENDER_FAILED "+repr(e))
    status["final_status"]="REAL_ADULT_TYTO_ARTIST_GLB_QUARANTINED_NO_JUVENILE_ART_QA_NO_RELEASE"
    save()
if __name__=="__main__":
    try:main()
    except Exception as e:
        block(repr(e))
        (OUT/"run202_exception.txt").write_text(traceback.format_exc())
    finally:save()
