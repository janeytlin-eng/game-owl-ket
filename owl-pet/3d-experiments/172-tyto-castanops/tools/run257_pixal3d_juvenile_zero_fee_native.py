#!/usr/bin/env python3
"""Run257: one new date-scoped, quota-compliant $0 public TencentARC Pixal3D ZeroGPU attempt using
an already genuinely segmented #172 v3 rightmost chick (not the adults).
No paid fallback, tokens, quota workarounds, fake meshes, SVGs or publication.
The true native geometry, if returned, is art-unreviewed research only.
"""
import sys, os, json, time, pathlib, hashlib, traceback, shutil, struct
ROOT=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
SOURCE=ROOT/"research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/rightmost_baby_owl_512_rgba.png"
OUT=ROOT/"research-evidence-run257-PIXAL3D-REAL-PBR-STRICT-NO_RELEASE"
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
    return dict(bytes=len(b),sha256=sha(p),native_indexed_triangles=tris,
                meshes=len(doc.get("meshes",[])),materials=len(doc.get("materials",[])),
                textures=len(doc.get("textures",[])),images=len(doc.get("images",[])),
                animations=len(doc.get("animations",[])))

def generate():
    from PIL import Image
    from gradio_client import Client, handle_file
    import gradio_client
    assert SOURCE.is_file(), "Original reference crop absent"
    im=Image.open(SOURCE).convert("RGBA")
    assert im.size==(512,512)
    assert im.getchannel("A").getextrema()[0]<32, "Input must be isolated transparent rightmost chick"
    actual=sha(SOURCE)
    assert actual=="e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8", "Input provenance mismatch"
    status=dict(run="257", date=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
       provider="TencentARC/Pixal3D", original_source_sha256=actual,
       original_source=str(SOURCE), input_px=[512,512],
       client_version=getattr(gradio_client,"__version__","unknown"),
       inference_calls_permitted=1, actual_gpu_inference_completed=False,
       research_iteration="2026-11-21_after_4_day_quota_reset",
       provider_claim_license="MIT; third-party assets and output rights not audited",
       no_payment=True, no_tokens=True, license_cleared=False, art_approved=False,
       physical_mobile_gpu_tested=False, result="NO_GLB",release="NO_RELEASE",stage="preflight")
    save(status,"run257_status.json")
    shutil.copy2(SOURCE,OUT/"run257_source_rightmost_actual_rgba.png")
    try:
       client=Client(status["provider"],verbose=False)
       api=client.view_api(return_format="dict").get("named_endpoints",{})
       save({k:{"parameter_names":[p.get("parameter_name") for p in v.get("parameters",[])],
          "returns":len(v.get("returns",[]))} for k,v in api.items()},"run257_live_schema.json")
       assert "/generate_3d" in api and "/extract_glb_api" in api,"Expected live endpoints absent"
       gp=[p.get("parameter_name") for p in api["/generate_3d"].get("parameters",[])]
       expected=["image","seed","resolution","ss_guidance_strength","ss_guidance_rescale",
          "ss_sampling_steps","ss_rescale_t","shape_slat_guidance_strength",
          "shape_slat_guidance_rescale","shape_slat_sampling_steps","shape_slat_rescale_t",
          "tex_slat_guidance_strength","tex_slat_guidance_rescale",
          "tex_slat_sampling_steps","tex_slat_rescale_t","manual_fov","fov_unit","session_id"]
       assert gp==expected, "Live Pixal3D schema changed; do not guess GPU arguments"
       ep=[p.get("parameter_name") for p in api["/extract_glb_api"].get("parameters",[])]
       assert ep==["state_path","decimation_target","texture_size","session_id"], "Extractor schema changed"
       args=(handle_file(str(SOURCE)),172,512,7.5,0.7,12,5.0,7.5,0.5,12,3.0,1.0,0.0,12,3.0,-1.0,"deg","")
       status["stage"]="generate_3d";save(status,"run257_status.json")
       t=time.monotonic()
       response=client.predict(*args,api_name="/generate_3d")
       status["gpu_request_wall_seconds"]=round(time.monotonic()-t,2)
       status["actual_gpu_inference_completed"]=True
       status["response_type"]=type(response).__name__
       status["response_keys"]=list(response) if isinstance(response,dict) else []
       (OUT/"run257_generation_response_excerpt.txt").write_text(str(response)[:8000])
       state_path=response.get("state_path") if isinstance(response,dict) else None
       status["state_path_supplied"]=bool(state_path)
       if not state_path: raise RuntimeError("No state_path in genuine provider output; no speculative extraction")
       status["stage"]="extract_glb_api";save(status,"run257_status.json")
       export=client.predict(state_path,100000,1024,"",api_name="/extract_glb_api")
       (OUT/"run257_extract_response_excerpt.txt").write_text(str(export)[:8000])
       p=find_glb(export)
       if p is None:raise RuntimeError("No genuine local binary GLB returned")
       dest=OUT/"run257_pixal3d_original_NATIVE_RESEARCH_ONLY.glb"
       shutil.copy2(p,dest)
       status["glb"]=inspect(dest)
       status["art_approved"]=False
       status["physical_mobile_gpu_tested"]=False
       status["result"]="REAL_GLB_ART_UNREVIEWED"
    except Exception as e:
       status["error"]=type(e).__name__+": "+str(e)[:1800]
       status["traceback_file"]="run257_failure_traceback.txt"
       (OUT/"run257_failure_traceback.txt").write_text(traceback.format_exc(limit=16))
    status["finished"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
    save(status,"run257_status.json")
    print("RUN257_RESULT",json.dumps(status,ensure_ascii=False),flush=True)

def render():
    import bpy, math
    from mathutils import Vector
    source=OUT/"run257_pixal3d_original_NATIVE_RESEARCH_ONLY.glb"
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
    if scene.world is None:scene.world=bpy.data.worlds.new("run257_studio")
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
        scene.render.filepath=str(OUT/("run257_"+name+"_ACTUAL_CYCLES_UNAPPROVED.png"))
        bpy.ops.render.render(write_still=True)
    info=dict(imported_meshes=len(ms),polygon_count=sum(len(o.data.polygons) for o in ms),
              triangles=sum(len(o.data.loop_triangles) for o in ms),blender=bpy.app.version_string,
              bounds=list(high-low),four_actual_views=True,art_approval=False,real_phone_test=False)
    save(info,"run257_native_blender_inspection.json")
    print("RUN257_FOUR_NATIVE_VIEWS_COMPLETE",json.dumps(info),flush=True)

if __name__=="__main__":
    if sys.argv[-1]=="generate":generate()
    elif sys.argv[-1]=="render":render()
    else:raise SystemExit("usage generate|render")
