#!/usr/bin/env python3
"""Run146T: one quota-compliant $0 public Microsoft TRELLIS.2 ZeroGPU attempt using
an already genuinely segmented #172 v3 rightmost chick (not the adults).
No paid fallback, tokens, quota workarounds, fake meshes, SVGs or publication.
The true native geometry, if returned, is art-unreviewed research only.
"""
import sys, os, json, time, pathlib, hashlib, traceback, shutil, struct
ROOT=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
SOURCE=ROOT/"research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/rightmost_baby_owl_512_rgba.png"
OUT=ROOT/"research-evidence-run146T-TRELLIS2-ZEROGPU-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)

def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def save(o,name):
    (OUT/name).write_text(json.dumps(o,indent=2,ensure_ascii=False,default=str)+"\n")

def find_glb(v):
    if isinstance(v,str):
        p=pathlib.Path(v)
        if p.suffix.lower()==".glb" and p.is_file(): return p
    if isinstance(v,dict):
        for x in v.values():
            r=find_glb(x)
            if r:return r
    if isinstance(v,(list,tuple)):
        for x in v:
            r=find_glb(x)
            if r:return r
    return None

def inspect(p):
    b=pathlib.Path(p).read_bytes()
    if len(b)<1024 or b[:4]!=b"glTF" or struct.unpack_from("<I",b,8)[0]!=len(b):
        raise RuntimeError("Provider did not return a valid full GLB")
    n,k=struct.unpack_from("<I4s",b,12)
    if k!=b"JSON":raise RuntimeError("Missing native GLB JSON chunk")
    doc=json.loads(b[20:20+n].decode("utf8").rstrip(" \u0000"))
    prim=[pr for m in doc.get("meshes",[]) for pr in m.get("primitives",[])]
    tris=sum(doc["accessors"][x["indices"]]["count"]//3 for x in prim if "indices" in x and x.get("mode",4)==4)
    if tris<1000:raise RuntimeError("Returned geometry under min research integrity tri-count")
    reject=json.loads((ROOT/"known_rejected_asset_sha256_registry.json").read_text())["known_rejected_source_glbs"]
    known=any(x["sha256"]==sha(p) for x in reject)
    return dict(bytes=len(b),sha256=sha(p),known_art_rejected_fingerprint=known,native_indexed_triangles=tris,
                meshes=len(doc.get("meshes",[])),materials=len(doc.get("materials",[])),
                textures=len(doc.get("textures",[])),images=len(doc.get("images",[])),
                animations=len(doc.get("animations",[])))

def generate():
    from PIL import Image
    from gradio_client import Client, handle_file
    import gradio_client
    if not SOURCE.is_file():raise RuntimeError("Original genuine rightmost crop absent")
    im=Image.open(SOURCE).convert("RGBA")
    assert im.size==(512,512)
    assert im.getchannel("A").getextrema()[0]<32,"Source lacks transparency"
    # Pin the exact source to avoid accidentally using a toy owl/adult/other input.
    expected="e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8"; actual=sha(SOURCE)
    if actual != expected: raise RuntimeError("Source SHA256 mismatch; will not infer from wrong owl input")
    # Hash is always recorded; 512 RGBA and branch path are hard preconditions.
    result=dict(run=146,date_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
      source=str(SOURCE),source_sha256=actual,source_dimensions=list(im.size),
      provider="microsoft/TRELLIS.2",model_license_claim="MIT; verify downstream rights before any release",
      actual_public_token_used=False,paid_endpoints_allowed=False,max_inference_calls=1,
      previous_run103="no mesh, unauthenticated ZeroGPU quota; waited for a later date",
      previous_run131="SF3D upstream AppError; no mesh",
      actual_hardware_mobile_tested=False,art_approved=False,release="NO_RELEASE",
      stage="preflight",result="NO_GLB")
    save(result,"run146t_status.json")
    # The source is generated only within this repository, not copied from a third party.
    shutil.copy2(SOURCE,OUT/"run146t_source_rightmost_actual_rgba.png")
    try:
        client=Client("microsoft/TRELLIS.2",verbose=False)
        result["client_version"]=getattr(gradio_client,"__version__","unknown")
        schema=client.view_api(return_format="dict")
        named=schema.get("named_endpoints",{})
        public={k:{"params":[{"label":x.get("label"),"component":x.get("component"),"type":x.get("type")}
                       for x in v.get("parameters",[])],
                   "returns":len(v.get("returns",[]))}
                for k,v in named.items()}
        save(public,"run146t_actual_public_api_schema.json")
        result["endpoints"]=list(named)
        if "/image_to_3d" not in named or "/extract_glb" not in named:
            raise RuntimeError("Current public TRELLIS.2 API incompatible: no expected endpoints")
        gen_args=(handle_file(str(SOURCE)),172,"512",7.5,0.7,12,5.0,7.5,0.5,12,3.0,1.0,0.0,12,3.0)
        gparams=named["/image_to_3d"].get("parameters",[])
        # Gradio may include State/internal components among documented params.
        # Fail safely rather than spending quota on a guessed schema.
        if len(gparams)!=len(gen_args):
            raise RuntimeError("Public /image_to_3d parameter count changed: "+str(len(gparams)))
        if len(named["/extract_glb"].get("parameters",[]))!=2:
            raise RuntimeError("Public /extract_glb parameter count changed")
        result["stage"]="image_to_3d"; save(result,"run146t_status.json")
        t=time.monotonic()
        preview=client.predict(*gen_args,api_name="/image_to_3d")
        result["inference_seconds"]=round(time.monotonic()-t,2)
        result["preview_type"]=type(preview).__name__
        result["preview_present"]=bool(preview)
        (OUT/"run146t_preview_response_excerpt.txt").write_text(str(preview)[:2000])
        if not preview:raise RuntimeError("No native preview or state after inference")
        result["stage"]="extract_glb";save(result,"run146t_status.json")
        extracted=client.predict(100000,1024,api_name="/extract_glb")
        found=find_glb(extracted)
        (OUT/"run146t_extract_response_excerpt.txt").write_text(str(extracted)[:2000])
        if found is None:raise RuntimeError("No genuine GLB file returned by provider")
        target=OUT/"run146t_trellis2_original_NATIVE_RESEARCH_ONLY.glb"
        shutil.copy2(found,target)
        result["glb"]=inspect(target)
        result["result"]="REAL_NATIVE_GLB_ART_UNREVIEWED" if not result["glb"]["known_art_rejected_fingerprint"] else "KNOWN_ART_REJECTED_FINGERPRINT"
    except Exception as e:
        result["error"]=type(e).__name__+": "+str(e)[:1800]
        result["traceback_file"]="run146t_failure_traceback.txt"
        (OUT/"run146t_failure_traceback.txt").write_text(traceback.format_exc(limit=16))
    result["finished_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
    save(result,"run146t_status.json")
    print("RUN133_RESULT",json.dumps(result,ensure_ascii=False),flush=True)

def render():
    import bpy, math
    from mathutils import Vector
    source=OUT/"run146t_trellis2_original_NATIVE_RESEARCH_ONLY.glb"
    if not source.is_file():raise RuntimeError("Cannot render nonexistent GLB")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(source))
    ms=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    assert ms, "No real imported meshes"
    pts=[o.matrix_world@Vector(v) for o in ms for v in o.bound_box]
    low=Vector(tuple(min(v[i] for v in pts) for i in range(3)))
    high=Vector(tuple(max(v[i] for v in pts) for i in range(3)))
    center=(low+high)*.5;extent=max(high-low)
    scene=bpy.context.scene
    if scene.world is None:scene.world=bpy.data.worlds.new("run146t_studio")
    scene.world.color=(.38,.38,.38)
    scene.render.engine="CYCLES";scene.cycles.samples=18
    scene.render.resolution_x=480;scene.render.resolution_y=480
    scene.view_layers[0].cycles.use_denoising=False
    def light(name,xyz,power):
        ld=bpy.data.lights.new(name,"AREA");ld.energy=power;ld.size=4*extent
        ob=bpy.data.objects.new(name,ld);scene.collection.objects.link(ob)
        ob.location=center+Vector(xyz)*extent
        ob.rotation_euler=(center-ob.location).to_track_quat("-Z","Y").to_euler()
    light("key",(-3,-3,3),370);light("fill",(3,1.5,3),240)
    cam=bpy.data.objects.new("orbit_camera",bpy.data.cameras.new("orbit_camera"))
    scene.collection.objects.link(cam);scene.camera=cam
    cam.data.type="ORTHO";cam.data.ortho_scale=1.62*extent
    for name,deg in (("front",0),("quarter",45),("side",90),("back",180)):
        a=math.radians(deg)
        cam.location=center+Vector((4*math.sin(a),-4*math.cos(a),1.3))*extent
        cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
        scene.render.filepath=str(OUT/("run146t_"+name+"_ACTUAL_CYCLES_UNAPPROVED.png"))
        bpy.ops.render.render(write_still=True)
    info=dict(imported_meshes=len(ms),polygon_count=sum(len(o.data.polygons) for o in ms),
              triangles=sum(len(o.data.loop_triangles) for o in ms),blender=bpy.app.version_string,
              bounds=list(high-low),four_actual_views=True,art_approval=False,real_phone_test=False)
    save(info,"run146t_native_blender_inspection.json")
    print("RUN133_FOUR_NATIVE_VIEWS_COMPLETE",json.dumps(info),flush=True)

if __name__=="__main__":
    if sys.argv[-1]=="generate":generate()
    elif sys.argv[-1]=="render":render()
    else:raise SystemExit("usage generate|render")
