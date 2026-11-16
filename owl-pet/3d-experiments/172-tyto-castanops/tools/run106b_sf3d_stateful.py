#!/usr/bin/env python3
"""Run106B: independent zero-charge Stable Fast 3D real-textured mesh probe, ART_UNAPPROVED.
No SVG, dummy geometry, paid fallback, synthetic 2D turntable or deployment.
Original #172 v3 rightmost baby owl only; never use other wildlife photos as training input.
"""
import argparse,base64,hashlib,io,json,pathlib,shutil,struct,sys,time,traceback
from datetime import datetime,timezone

def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def emit(p,label):
    from PIL import Image
    im=Image.open(p).convert("RGB");im.thumbnail((490,410))
    out=io.BytesIO();im.save(out,format="JPEG",quality=64,optimize=True)
    print("BEGIN_"+label+"_BASE64",flush=True)
    print(base64.b64encode(out.getvalue()).decode(),flush=True)
    print("END_"+label+"_BASE64",flush=True)

def find_glb(v):
    if isinstance(v,(str,pathlib.Path)):
        q=str(v)
        if q.lower().split("?")[0].endswith(".glb"):yield q
    elif isinstance(v,dict):
        for z in v.values():yield from find_glb(z)
    elif isinstance(v,(list,tuple)):
        for z in v:yield from find_glb(z)

def generate(a):
    from PIL import Image,ImageDraw,ImageFilter
    out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
    p=pathlib.Path(a.source)
    original=Image.open(p).convert("RGB")
    w,h=original.size
    # Source from Run103 foreground of SAME rightmost #172 v3 project illustration.
    # ZeroRGB is background; flood-fill only border-connected darkness, retain interior pupils.
    binary=original.convert("L").point(lambda v:255 if v>16 else 0)
    ImageDraw.floodfill(binary,(0,0),128,thresh=0)
    alpha=binary.point(lambda v:0 if v==128 else 255).filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.GaussianBlur(0.7))
    bbox=alpha.getbbox()
    cut=original.copy();cut.putalpha(alpha);cut=cut.crop(bbox)
    # Stable Fast 3D consumes 512 RGBA foreground against its own neutral gray.
    # Keep actual aspect ratio and 85% foreground size; no unverified side/back synthesis.
    side=max(cut.size);canvas=Image.new("RGBA",(side,side),(0,0,0,0))
    canvas.alpha_composite(cut,((side-cut.width)//2,(side-cut.height)//2))
    target=Image.new("RGBA",(512,512),(0,0,0,0))
    inner=canvas.resize((435,435),Image.Resampling.LANCZOS)
    target.alpha_composite(inner,((512-435)//2,(512-435)//2))
    inp=out/"rightmost_baby_owl_512_rgba.png";target.save(inp)
    emit(inp,"RUN106B_REAL_RIGHTMOST_INPUT")
    coverage=sum(v>100 for v in target.getchannel("A").resize((64,64)).getdata())/4096
    state={"run":"106B","gate":"ART_UNAPPROVED","date_utc":datetime.now(timezone.utc).isoformat(),
       "source":"owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run103-TRELLIS2-PBR-ART_UNAPPROVED/preprocessed_image.png",
       "same_owl_v3_rightmost":True,"input_sha256":sha(inp),"input_dims":list(original.size),
       "alpha_bbox":bbox,"alpha_coverage_64":coverage,
       "provider":"stabilityai/stable-fast-3d","public_space":"https://huggingface.co/spaces/stabilityai/stable-fast-3d",
       "provider_license":"Stability AI Community License; not CC0; output/revenue usage restrictions must be reviewed",
       "no_extra_payment":True,"api_token_used":False,"requested_total_generations":1,
       "status":"NOT_ATTEMPTED","actual_phone_gpu_tested":False,
       "visual_review_required":True,"global_release_cleared":False}
    (out/"preflight.json").write_text(json.dumps(state,indent=2,ensure_ascii=False))
    if not (0.10<coverage<0.85):
        state["status"]="BAD_FOREGROUND_MASK_BLOCKED"
    else:
        try:
            from gradio_client import Client,handle_file
            cli=Client("stabilityai/stable-fast-3d",verbose=False)
            schema=cli.view_api(return_format="dict")
            (out/"provider_api_schema.json").write_text(json.dumps(schema,default=str,indent=2)[:150000])
            print("RUN106B_SF3D_PUBLIC_API_READY",flush=True)
            start=time.monotonic()
            # The official Gradio Space exposes run_button with preprocessed RGBA image state.
            # Supplying already segmented RGBA avoids a second paid/background model call.
            # Gradio run_button API exposes five parameters, NOT seven: two States are hidden.
            # First update its session with the official preprocess callback, then run once.
            # This is a real stateful API sequence, not a second mesh generation.
            prep=cli.predict(handle_file(str(inp)),0.85,api_name="/requires_bg_remove")
            state["actual_stateful_preprocess"]=True
            state["preprocess_response_summary"]=str(prep)[:600]
            print("RUN106BB_PREPROCESS_SESSION_READY",str(prep)[:200],flush=True)
            result=cli.predict(
                handle_file(str(inp)),0.85,"None",-1,1024,
                api_name="/run_button")
            state["elapsed_seconds"]=round(time.monotonic()-start,3)
            state["result_summary"]=str(result)[:3000]
            paths=list(find_glb(result))
            if not paths:raise RuntimeError("run_button produced no GLB: "+str(result)[:900])
            saved=False
            for val in paths:
                q=pathlib.Path(val)
                if q.is_file() and q.stat().st_size>20000:
                    dst=out/"run106b_sf3d_texture_art_unapproved.glb"
                    shutil.copyfile(q,dst)
                    dat=dst.read_bytes()
                    if dat[:4]!=b"glTF" or len(dat)!=struct.unpack_from("<I",dat,8)[0]:
                        dst.unlink(missing_ok=True);raise ValueError("GLB magic/declared length invalid")
                    state["source_glb_size"]=len(dat)
                    state["source_glb_sha256"]=sha(dst)
                    saved=True;break
            if not saved:raise RuntimeError("No local GLB binary in response "+str(paths)[:700])
            state["status"]="REAL_TEXTURED_GLB_CREATED_UNAPPROVED"
        except Exception as ex:
            state["status"]="FREE_PUBLIC_ROUTE_BLOCKED_OR_FAILED"
            state["error_type"]=type(ex).__name__;state["error"]=str(ex)[:1500]
            (out/"traceback.txt").write_text(traceback.format_exc())
            print("RUN106B_PUBLIC_FREE_FAILURE",type(ex).__name__,str(ex)[:700],flush=True)
    (out/"run106b_status.json").write_text(json.dumps(state,indent=2,ensure_ascii=False))
    (out/"ART_NOT_APPROVED.flag").write_text(
        "Research only. Actual art and full 360-degree juvenile anatomy unverified; no real phone GPU proof. "
        "No user-facing sample or deployment. Source license requires case-specific review.\n")
    print("RUN106B_OUTCOME",json.dumps(state,ensure_ascii=False)[:3500],flush=True)

def render(a):
    import bpy
    from mathutils import Vector
    from math import sin,cos,radians
    o=pathlib.Path(a.out);o.mkdir(exist_ok=True,parents=True)
    bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=a.model)
    meshes=[m for m in bpy.context.scene.objects if m.type=="MESH"]
    if not meshes:raise RuntimeError("Imported GLB had no 3D meshes")
    bounds=[m.matrix_world @ Vector(c) for m in meshes for c in m.bound_box]
    low=Vector((min(p[i] for p in bounds) for i in range(3)))
    high=Vector((max(p[i] for p in bounds) for i in range(3)))
    center=(low+high)*.5;size=max(high-low)
    if size<=0:raise RuntimeError("Mesh has zero dimensions")
    tris=sum(len(m.data.loop_triangles) if m.data.loop_triangles else len(m.data.polygons) for m in meshes)
    scene=bpy.context.scene
    scene.render.engine="CYCLES";scene.cycles.samples=20;scene.cycles.use_denoising=False
    scene.render.resolution_x=512;scene.render.resolution_y=512;scene.render.resolution_percentage=100
    scene.world.color=(.34,.34,.34)
    def area(name,direction,energy):
        light=bpy.data.lights.new(name,type="AREA");light.energy=energy;light.size=4.5*size
        ob=bpy.data.objects.new(name,light);scene.collection.objects.link(ob)
        ob.location=center+Vector(direction)*size
        ob.rotation_euler=(center-ob.location).to_track_quat("-Z","Y").to_euler()
    area("key",(-3,-3,3),350);area("rim",(2,2,2),250)
    camera=bpy.data.cameras.new("run106b_multiview")
    cam=bpy.data.objects.new("run106b_multiview",camera);scene.collection.objects.link(cam);scene.camera=cam
    camera.type="ORTHO";camera.ortho_scale=1.6*size
    for name,angle in [("front",0),("quarter",45),("side",90),("back",180)]:
        r=radians(angle)
        cam.location=center+Vector((4*sin(r),-4*cos(r),1.2))*size
        cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
        scene.render.filepath=str(o/("run106b_"+name+"_real_cycles_unapproved.png"))
        bpy.ops.render.render(write_still=True)
        print("RUN106B_TRUE_CYCLES_VIEW",name,flush=True)
    metrics={"blender_version":bpy.app.version_string,"actual_imported_meshes":len(meshes),
             "mesh_polygon_count":sum(len(m.data.polygons) for m in meshes),
             "estimated_triangles":tris,"bounding_dimensions":list(high-low),
             "views":4,"material_count":len(bpy.data.materials)}
    (o/"native_render_metrics.json").write_text(json.dumps(metrics,indent=2))
    print("RUN106B_NATIVE_METRICS",json.dumps(metrics),flush=True)
    bpy.ops.export_scene.gltf(filepath=str(o/"run106b_sf3d_blender_roundtrip_unapproved.glb"),export_format="GLB")

def manifest(a):
    from PIL import Image,ImageDraw
    o=pathlib.Path(a.out)
    paths=[o/("run106b_"+v+"_real_cycles_unapproved.png") for v in ("front","quarter","side","back")]
    if all(p.is_file() for p in paths):
        contact=Image.new("RGB",(1024,1024),(242,239,232))
        for i,p in enumerate(paths):
            im=Image.open(p).convert("RGB");contact.paste(im,((i%2)*512,(i//2)*512))
            ImageDraw.Draw(contact).text(((i%2)*512+12,(i//2)*512+12),("front","quarter","side","back")[i],fill="black")
        dest=o/"run106b_four_true_views_ART_UNAPPROVED.jpg";contact.save(dest,quality=78)
        emit(dest,"RUN106B_FOUR_NATIVE_CYCLES_CONTACT")
    files=sorted(p for p in o.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS.txt","checksum_validation.log","manifest_execution.log","generate_execution.log","render_execution.log"))
    (o/"SHA256SUMS.txt").write_text("".join(sha(p)+"  "+str(p.relative_to(o))+"\n" for p in files))
    print("RUN106B_HASHED_EVIDENCE_FILES",len(files),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=("generate","render","manifest"),required=True)
    ap.add_argument("--source",default="");ap.add_argument("--model",default="")
    ap.add_argument("--out",required=True)
    a=ap.parse_args(sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else None)
    dict(generate=generate,render=render,manifest=manifest)[a.mode](a)
