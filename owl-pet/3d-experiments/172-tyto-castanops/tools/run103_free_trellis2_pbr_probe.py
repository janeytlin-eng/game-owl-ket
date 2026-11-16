#!/usr/bin/env python3
"""Run103: zero-dollar official Microsoft TRELLIS.2 ZeroGPU PBR image-to-3D experiment.
Noncommercial research quarantine until license, juvenile art and physical phone gates pass.
Never substitute synthetic 2D images for a native 3D asset.
"""
import sys, os, json, time, pathlib, hashlib, traceback, shutil, struct, re, base64
ROOT = pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT = ROOT / "research-evidence-run103-TRELLIS2-PBR-ART_UNAPPROVED"
SRC = ROOT / "research-evidence-run99-HUNYUAN-ZEROGPU-ART_UNAPPROVED/rightmost_mesoptile_input.jpg"
OUT.mkdir(parents=True, exist_ok=True)
def digest(p):
    h=hashlib.sha256()
    with pathlib.Path(p).open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):h.update(chunk)
    return h.hexdigest()
def save(obj, filename):
    (OUT/filename).write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str))
def inspect_glb(p):
    b=pathlib.Path(p).read_bytes()
    if len(b)<40 or b[:4]!=b"glTF" or struct.unpack_from("<I",b,8)[0]!=len(b):
        raise ValueError("Not a valid GLB binary")
    n, kind=struct.unpack_from("<I4s",b,12)
    if kind!=b"JSON":raise ValueError("GLB JSON chunk missing")
    doc=json.loads(b[20:20+n].decode("utf-8").rstrip(" \\x00"))
    tris=sum(doc["accessors"][pr["indices"]]["count"]//3 for mesh in doc.get("meshes",[]) for pr in mesh["primitives"] if pr.get("mode",4)==4 and "indices" in pr)
    return dict(bytes=len(b),sha256=digest(p),triangles=int(tris),meshes=len(doc.get("meshes",[])),
        textures=len(doc.get("textures",[])),images=len(doc.get("images",[])),
        materials=len(doc.get("materials",[])),animations=len(doc.get("animations",[])))
def locate(r):
    if isinstance(r,(list,tuple)):
        for item in r:
            f=locate(item)
            if f:return f
    if isinstance(r,dict):
        for key in ("path","name","url","value"):
            if key in r:
                f=locate(r[key])
                if f:return f
    if isinstance(r,str):
        p=pathlib.Path(r)
        if p.suffix.lower()==".glb" and p.is_file():return p
    return None
def run_generate():
    from gradio_client import Client,handle_file
    from PIL import Image
    import gradio_client
    report=dict(experiment="Official Microsoft TRELLIS.2 ZeroGPU texture+geometry image-to-3D",
        source=str(SRC),source_sha256=digest(SRC),source_size=list(Image.open(SRC).size),
        provider="microsoft/TRELLIS.2",provider_public_zero_gpu=True,
        no_extra_paid_credits=True,paid_fallback=False,unapproved=True,
        full_pbr_required=True,physical_phone_gpu_tested=False,
        source_plate_license_requires_project_review=True,started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()))
    save(report,"run103_status.json")
    try:
        client=Client("microsoft/TRELLIS.2", verbose=False)
        cfg=client.view_api(return_format="dict")
        # The official live API may change; preserve a bounded, redacted schema.
        endpoints=cfg.get("named_endpoints",{}) if isinstance(cfg,dict) else {}
        report["named_endpoints"]=list(endpoints.keys())
        save({"endpoints":{k:{"parameters":[x.get("label",x.get("parameter_name","")) for x in v.get("parameters",[])],
                                 "return_count":len(v.get("returns",[]))}
                            for k,v in endpoints.items()}},"public_trellis2_api_probe.json")
        names=list(endpoints)
        def ep(word):
            matches=[p for p in names if p.rstrip("/").split("/")[-1]==word]
            if not matches:matches=[p for p in names if word in p.lower()]
            return matches[0] if matches else "/"+word
        image_input=SRC
        pre=ep("preprocess_image")
        try:
            processed=client.predict(handle_file(str(SRC)),api_name=pre)
            if isinstance(processed,(str,dict)):
                fp=processed if isinstance(processed,str) else processed.get("path","")
                if fp and pathlib.Path(fp).is_file():
                    image_input=pathlib.Path(fp)
                    shutil.copy2(image_input,OUT/"preprocessed_image.png")
            report["preprocess"]="SUCCESS"
        except Exception as err:
            report["preprocess"]="FAILED_using_source_crop"
            report["preprocess_error"]=repr(err)[:600]
        save(report,"run103_status.json")
        # Official app.py defaults. One request, no retries consuming extra credits.
        gen=ep("image_to_3d")
        params=(handle_file(str(image_input)),172,"512",7.5,0.7,12,5.0,
                7.5,0.5,12,3.0,1.0,0.0,12,3.0)
        report["generate_endpoint"]=gen
        report["seed"]=172
        report["resolution"]="512"
        result=client.predict(*params,api_name=gen)
        # Gradio exposes the preview but holds gr.State server-side in this client's session.
        # API audit on 2026-11-16 confirmed /image_to_3d has exactly ONE public return.
        preview=result[-1] if isinstance(result,(tuple,list)) else result
        if not isinstance(preview,str) or "previewer" not in preview:
            raise RuntimeError("Generate did not return the expected actual 3D turntable preview")
        report["generate"]="SUCCESS"
        if isinstance(preview,str):
            imgs=re.findall(r'src="(data:image/(?:png|jpeg);base64,[^"]+)"',preview)
            # 48 native rendered snapshots (6 modes x 8 angles); selected views are evidence, NOT deliverables.
            for num in (3,5,7,11):
                if len(imgs)>num:
                    blob=base64.b64decode(imgs[num].split(",",1)[-1])
                    (OUT/("native_trellis_preview_%02d.jpg"%num)).write_bytes(blob)
            report["native_preview_images"]=len(imgs)
        save(report,"run103_status.json")
        extract=ep("extract_glb")
        report["extract_endpoint"]=extract
        # /extract_glb has exactly TWO public parameters. Internal gr.State is implicit.
        extracted=client.predict(100000,1024,api_name=extract)
        p=locate(extracted)
        if p is None:raise RuntimeError("Extract returned no local .glb path; cannot claim a model")
        dest=OUT/"run103_original_trellis2_pbr_NOT_APPROVED.glb"
        shutil.copy2(p,dest)
        report["glb"]=inspect_glb(dest)
        report["outcome"]="REAL_GLB_NEEDS_NATIVE_RENDER_AND_ART_REVIEW"
    except Exception as err:
        report["outcome"]="NO_GLB_FREE_ROUTE_BLOCKED_OR_FAILED"
        report["error"]=type(err).__name__+": "+str(err)[:2000]
        (OUT/"run103_failure_traceback.log").write_text(traceback.format_exc(limit=12))
    report["finished_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
    save(report,"run103_status.json")
    print("RUN103_STATUS",json.dumps(report,default=str),flush=True)
def run_render():
    import bpy,math
    from mathutils import Vector
    source=OUT/"run103_original_trellis2_pbr_NOT_APPROVED.glb"
    if not source.is_file():raise SystemExit("Real TRELLIS GLB absent; no fake fallback render")
    bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=str(source))
    objs=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    if not objs or sum(len(o.data.polygons) for o in objs)<1000:
        raise RuntimeError("No credible real 3D mesh after Blender import")
    points=[o.matrix_world@Vector(c) for o in objs for c in o.bound_box]
    low=Vector(tuple(min(p[i] for p in points) for i in range(3)))
    high=Vector(tuple(max(p[i] for p in points) for i in range(3)))
    center=(low+high)*.5; size=max(high-low)
    scene=bpy.context.scene
    scene.render.engine="CYCLES";scene.cycles.samples=16;scene.cycles.use_denoising=False
    scene.render.resolution_x=512;scene.render.resolution_y=512
    scene.render.resolution_percentage=100
    scene.render.image_settings.file_format="PNG";scene.world.color=(.38,.38,.38)
    scene.view_settings.view_transform="Standard";scene.view_settings.look="Medium High Contrast"
    def lamp(name,xyz,energy,diameter):
        d=bpy.data.lights.new(name,"AREA");d.energy=energy;d.size=diameter*size
        o=bpy.data.objects.new(name,d);scene.collection.objects.link(o)
        o.location=center+Vector(xyz)*size
        o.rotation_euler=(center-o.location).to_track_quat("-Z","Y").to_euler()
    lamp("soft_key",(-2.2,-3,3),320,4)
    lamp("soft_fill",(2,-2,1.5),120,3.2)
    lamp("soft_rim",(1.5,2.5,2.8),170,3.0)
    camera_data=bpy.data.cameras.new("Run103_true_mesh_camera")
    camera=bpy.data.objects.new("Run103_true_mesh_camera",camera_data)
    scene.collection.objects.link(camera);scene.camera=camera
    camera.data.type="ORTHO";camera.data.ortho_scale=1.72*size
    for name,angle in (("front",0),("quarter",45),("side",90),("back",180)):
        a=math.radians(angle)
        camera.location=center+Vector((4*math.sin(a),-4*math.cos(a),1.2))*size
        camera.rotation_euler=(center-camera.location).to_track_quat("-Z","Y").to_euler()
        scene.render.filepath=str(OUT/("run103_"+name+"_native_cycles.png"))
        bpy.ops.render.render(write_still=True)
    report=json.loads((OUT/"run103_status.json").read_text())
    report["blender_reimport_meshes"]=len(objs)
    report["blender_triangles"]=sum(sum(len(p.vertices)-2 for p in o.data.polygons) for o in objs)
    report["cycles_multiview"]=4
    report["blender_materials"]=sum(len(o.data.materials) for o in objs)
    report["native_3d_roundtrip"]=True
    save(report,"run103_status.json")
    print("RUN103_NATIVE_RENDER_COMPLETE",report["blender_triangles"],flush=True)
if __name__=="__main__":
    if len(sys.argv)>=2 and sys.argv[1]=="generate":run_generate()
    elif "render" in sys.argv:run_render()
    else:raise SystemExit("Pass generate or render")
