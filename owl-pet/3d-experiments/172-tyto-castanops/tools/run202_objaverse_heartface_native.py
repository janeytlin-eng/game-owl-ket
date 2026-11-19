#!/usr/bin/env python3
"""Run202: actual openly hosted Objaverse 1.0 Barn Owl mesh (museum CC0) QA.
Research-only, never a user-facing release; no synthetic geometry.
"""
import datetime,hashlib,json,os,sys,traceback
from pathlib import Path

R=Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run202-OBJAVERSE-MUSEUM-BARNOWL-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
UID="0e65de5934db4f0eae02835ba7227dcc"
PIN="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
q={"run":202, "date_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
   "target":"#172 Tyto castanops v3 rightmost age-unknown cream mesoptile",
   "candidate":"Polish Virtual Museums Barn owl CC0 scanned taxidermy, adult Tyto / potential reference donor only",
   "source_uid":UID,
   "source_original":"https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc",
   "distribution":"https://huggingface.co/datasets/allenai/objaverse",
   "license_claim":"Original Sketchfab page says CC0; dataset-level ODC-By does not replace per-object license",
   "original_verified":False, "source_downloaded":False, "new_native_glb":False,
   "geometry_parsed":False, "sevenview":False, "independent_art_approval":False,
   "actual_physical_phone_gpu":False, "no_extra_payment":True,
   "final_status":"NO_NEW_MODEL_NO_RELEASE","errors":[],"events":[]}
def note(s):
    q["events"].append(s)
    print(s,flush=True)
def save():
    (O/"run202_status.json").write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n")
try:
    for rel in ["owl-pet/AGENTS.md","owl-pet/README.md","owl-pet/prototype/index.html",
      "owl-pet/research/species/172-tyto-castanops-v3.md",
      str(R/"known_rejected_asset_sha256_registry.json"),
      str(R/"2026-11-19-run201d-hf-zerogpu-quota-original-source-correction-NO_RELEASE.md")]:
        f=Path(rel)
        if not f.is_file():raise RuntimeError("missing required repository preflight "+rel)
        with (O/"preflight_sha256.txt").open("a") as out:
            out.write(hashlib.sha256(f.read_bytes()).hexdigest()+"  "+rel+"\n")
    ref=R/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
    h=hashlib.sha256(ref.read_bytes()).hexdigest()
    (O/"original_reference_sha256.txt").write_text(h+"  "+str(ref)+"\n")
    if h!=PIN:raise RuntimeError("WRONG_PINNED_RIGHTMOST_REFERENCE")
    q["original_verified"]=True
    note("Validated owl-pet existing cat prototype, v3 design, Run201d, negative SHA register and exact pinned rightmost owl image")
    import requests
    uri="https://api.sketchfab.com/v3/models/"+UID
    try:
        resp=requests.get(uri,timeout=25)
        (O/"sketchfab_metadata_http.txt").write_text("status="+str(resp.status_code)+"\nfinal_url="+str(resp.url)+"\n"+resp.text[:6000])
        if resp.status_code==200:
            meta=resp.json()
            q["sketchfab_metadata"]={k:meta.get(k) for k in ("uid","name","isDownloadable","license","faceCount","vertexCount")}
            note("Public Sketchfab metadata HTTP200 read (read-only, no unauthorized download API)")
    except Exception as e:q["errors"].append("SKETCHFAB_METADATA:"+repr(e))
    import objaverse
    note("Official objaverse.load_objects([known_exact_Sketchfab_UID]) started; no auth or paid service")
    paths=objaverse.load_objects(uids=[UID],download_processes=1)
    p=Path(paths[UID])
    if not p.is_file():raise RuntimeError("Objaverse returned a non-existing GLB path")
    data=p.read_bytes()
    if data[:4]!=b"glTF" or len(data)<1000:raise RuntimeError("Source is not valid GLB container")
    digest=hashlib.sha256(data).hexdigest()
    q.update({"source_downloaded":True,"new_native_glb":True,"native_sha256":digest,
              "native_bytes":len(data),"original_path_in_cache":str(p)})
    note("Downloaded "+str(len(data))+" bytes valid GLB magic SHA256="+digest)
    registry=json.loads((R/"known_rejected_asset_sha256_registry.json").read_text())
    rejected={x["sha256"] for x in registry["known_rejected_source_glbs"]}
    if digest in rejected:
        q["final_status"]="EXACT_KNOWN_REJECT_NO_RELEASE"
        note("Native GLB matches already rejected SHA; no repeat art review")
    else:
        # retain original only in isolated 30-day action artifact, never in GitHub git commit.
        (O/"run202_original_museum_CC0_taxidermy.glb").write_bytes(data)
        import trimesh
        scene=trimesh.load(p,force="scene",process=False)
        meshes=[m for m in scene.geometry.values() if isinstance(m,trimesh.Trimesh)]
        q["geometry_parsed"]=bool(meshes)
        q["geometry"]={
           "unique_meshes":len(meshes),
           "triangles":int(sum(len(m.faces) for m in meshes)),
           "vertices":int(sum(len(m.vertices) for m in meshes)),
           "bounds":scene.bounds.tolist() if scene.bounds is not None else None,
           "material_kinds":sorted(set(type(m.visual.material).__name__ for m in meshes if hasattr(m.visual,"material"))),
        }
        if not meshes:raise RuntimeError("No native triangle meshes found")
        note("True native trimesh import passed "+json.dumps(q["geometry"],ensure_ascii=False))
        import vtk
        from PIL import Image,ImageDraw
        win=vtk.vtkRenderWindow()
        win.SetOffScreenRendering(True)
        win.SetSize(540,540)
        importer=vtk.vtkGLTFImporter()
        importer.SetFileName(str(p))
        importer.SetRenderWindow(win)
        importer.Update()
        renderer=win.GetRenderers().GetFirstRenderer()
        if renderer is None:raise RuntimeError("VTK glTF importer had no renderer")
        renderer.SetBackground(0.20,0.23,0.25)
        renderer.SetBackground2(0.35,0.39,0.42)
        renderer.GradientBackgroundOn()
        renderer.AutomaticLightCreationOn()
        bb=renderer.ComputeVisiblePropBounds()
        if bb[0]>bb[1]:raise RuntimeError("No imported VTK props")
        cx,cy,cz=[(bb[i]+bb[i+1])/2 for i in (0,2,4)]
        radius=max(bb[1]-bb[0],bb[3]-bb[2],bb[5]-bb[4],0.05)
        cams={"front":(0,0,1),"right":(1,0,0),"rear":(0,0,-1),
              "left":(-1,0,0),"top":(0,1,0),"bottom":(0,-1,0),"quarter":(0.7,0.3,0.7)}
        files=[]
        for name,v in cams.items():
            camera=renderer.GetActiveCamera()
            camera.SetFocalPoint(cx,cy,cz)
            camera.SetPosition(cx+v[0]*radius*3.1,cy+v[1]*radius*3.1,cz+v[2]*radius*3.1)
            camera.SetViewUp(0,0,-1) if name in ("top","bottom") else camera.SetViewUp(0,1,0)
            camera.ParallelProjectionOn()
            camera.SetParallelScale(radius*0.8)
            renderer.ResetCameraClippingRange()
            win.Render()
            filt=vtk.vtkWindowToImageFilter()
            filt.SetInput(win);filt.SetInputBufferTypeToRGB();filt.ReadFrontBufferOff();filt.Update()
            f=O/("run202_native_"+name+".png")
            writer=vtk.vtkPNGWriter()
            writer.SetFileName(str(f));writer.SetInputConnection(filt.GetOutputPort());writer.Write()
            if not f.is_file() or f.stat().st_size<5000:raise RuntimeError("Rendered image absent "+name)
            files.append(f)
        sheet=Image.new("RGB",(4*420,2*460),(29,34,40))
        d=ImageDraw.Draw(sheet)
        for i,f in enumerate(files):
            im=Image.open(f).convert("RGB");im.thumbnail((410,414))
            x=(i%4)*420+(420-im.width)//2;y=(i//4)*460+8
            sheet.paste(im,(x,y))
            d.text(((i%4)*420+16,(i//4)*460+425),f.stem.replace("run202_native_",""),fill=(255,255,255))
        sheet.save(O/"run202_native_sevenview_contact.png")
        q["sevenview"]=True
        q["renders"]=[f.name for f in files]
        q["vtk_version"]=vtk.vtkVersion.GetVTKVersion()
        q["render_bounds"]=list(bb)
        # A taxidermy adult never passes juvenile down, buried short wings, hollow support
        q["final_status"]="REAL_CC0_ADULT_TAXIDERMY_DONOR_ART_REVIEW_REQUIRED_NO_RELEASE"
        note("Seven real native VTK textured GLB camera views saved. Not accepted as juvenile.")
except Exception as e:
    q["errors"].append(type(e).__name__+": "+str(e))
    (O/"run202_exception.txt").write_text(traceback.format_exc())
    print(traceback.format_exc(),file=sys.stderr)
finally:
    save()
    import hashlib
    index={}
    for f in O.rglob("*"):
        if f.is_file() and f.name not in ("run202_original_museum_CC0_taxidermy.glb","run202_sha256_manifest.json"):
            index[f.name]={"bytes":f.stat().st_size,"sha256":hashlib.sha256(f.read_bytes()).hexdigest()}
    (O/"run202_sha256_manifest.json").write_text(json.dumps(index,indent=2,ensure_ascii=False)+"\n")
    assert all(hashlib.sha256((O/k).read_bytes()).hexdigest()==v["sha256"] for k,v in index.items())
    audit=R/"2026-11-19-run202-objaverse-museum-open-barnowl-native-NO_RELEASE.md"
    audit.write_text("# Run202 actual no-charge Objaverse museum barn owl native QA\n\n"+
       "Date: "+datetime.datetime.now(datetime.timezone.utc).isoformat()+"\n\n"+
       "Source: https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc (museum-provided CC0) via official Objaverse 1.0 HuggingFace mirror. Adult taxidermy source is only a potential sculpt/anatomy donor, **not** proof of the v3 age-unknown cream second-down juvenile.\n\n"+
       "Actual results: "+json.dumps({k:v for k,v in q.items() if k not in ["events","errors"]},ensure_ascii=False,indent=2)+"\n\n"+
       "Actual events: "+json.dumps(q["events"],ensure_ascii=False)+"\n\nErrors: "+json.dumps(q["errors"],ensure_ascii=False)+"\n\n"+
       "Real art acceptance is deliberately false: source age/feather tract and tree-hollow anatomy conflict with target; seven views are diagnostic, NOT an accepted figure. Native renderer does not establish physical smartphone GPU performance. Source GLB remains in the private runner artifact, not committed to public Git. No additional payment or main/251-species changes. NO_RELEASE.\n")
    print("RUN202 FINAL",q["final_status"],"EVIDENCE_FILE_COUNT",len(index),flush=True)
