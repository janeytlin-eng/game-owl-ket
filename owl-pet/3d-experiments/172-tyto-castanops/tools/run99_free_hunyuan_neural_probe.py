#!/usr/bin/env python3
"""#172 quarantined ZERO-ADDITIONAL-CHARGE HuggingFace ZeroGPU true-mesh study.

This does not call paid fal/Meshy/Tripo accounts or edit the existing pet.
No output is accepted without human visual review against the original rightmost nestling.
"""
import argparse, base64, hashlib, json, os, pathlib, shutil, struct, sys, time, traceback
from datetime import datetime, timezone

PREF="Run99/free-ZeroGPU/UNAPPROVED"

def sha256(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def walk_files(v):
    if isinstance(v, (str, pathlib.Path)):
        s=str(v)
        if s.lower().split("?")[0].endswith(".glb"):
            yield s
    elif isinstance(v, dict):
        for w in v.values():
            yield from walk_files(w)
    elif isinstance(v, (list, tuple)):
        for w in v:
            yield from walk_files(w)

def emit_image_for_review(p,label):
    # Image is from the actual image on disk; base64 in logs only for independent inspection.
    from PIL import Image
    import io
    im=Image.open(p).convert("RGB")
    im.thumbnail((500,440))
    b=io.BytesIO()
    im.save(b,format="JPEG",quality=64,optimize=True)
    print(f"BEGIN_{label}_BASE64",flush=True)
    print(base64.b64encode(b.getvalue()).decode("ascii"),flush=True)
    print(f"END_{label}_BASE64",flush=True)

def generate(args):
    from PIL import Image
    out=pathlib.Path(args.out);out.mkdir(parents=True,exist_ok=True)
    source=pathlib.Path(args.source)
    original=Image.open(source).convert("RGB")
    w,h=original.size
    # Rightmost of 1536x1024 3-bird concept plate; preserve supported toes and a little hollow.
    bbox=(round(w*.615),round(h*.175),round(w*.993),round(h*.96))
    crop=original.crop(bbox)
    crop.thumbnail((800,1000))
    crop.save(out/"rightmost_mesoptile_input.jpg",quality=92)
    emit_image_for_review(out/"rightmost_mesoptile_input.jpg","RUN99_INPUT_CROP")
    status=dict(run="99",gate="ART_UNAPPROVED",source_repo="janeytlin-eng/game-owl-ket",
      source_path="owl-pet/design/concepts/172-tyto-castanops-v3.png",
      source_image_size=[w,h],crop_box=bbox,crop_size=list(crop.size),
      date_utc=datetime.now(timezone.utc).isoformat(),
      no_extra_charge=True,provider="https://huggingface.co/spaces/tencent/Hunyuan3D-2",
      provider_mode="public ZeroGPU; no auth token; geometry-only; no paid fallback",
      previous_negative_controls=["Run92/92B TripoSR CPU","Run96B native SDF anatomy","Run98 free low-poly rig donor"],
      outcome="NOT_ATTEMPTED")
    (out/"preflight.json").write_text(json.dumps(status,ensure_ascii=False,indent=2))
    try:
        from gradio_client import Client, handle_file
        # No hf_token, no API key. If free guest access is blocked, stop.
        client=Client("tencent/Hunyuan3D-2",verbose=False)
        schema=client.view_api(return_format="dict")
        (out/"public_gradio_api_schema.json").write_text(json.dumps(schema,default=str,indent=2)[:100000])
        status["api_visible"]=True
        print("GRADIO_PUBLIC_API_CONNECTED",flush=True)
        before=time.monotonic()
        result=client.predict(
            image=handle_file(str(out/"rightmost_mesoptile_input.jpg")),
            steps=30,
            guidance_scale=5.0,
            seed=172,
            octree_resolution=256,
            check_box_rembg=True,
            num_chunks=8000,
            randomize_seed=False,
            api_name="/shape_generation")
        status["elapsed_seconds"]=round(time.monotonic()-before,2)
        status["result_types"]=str(type(result))
        status["result_brief"]=str(result)[:4000]
        paths=list(walk_files(result))
        if not paths:
            raise RuntimeError("Public Space finished without a usable GLB path")
        valid=False
        for s in paths:
            if s.startswith(("http://","https://")):
                # gradio returns local downloaded file for shape_generation normally.
                continue
            p=pathlib.Path(s)
            if p.exists() and p.is_file() and p.stat().st_size > 20000:
                dst=out/"run99_neural_source_ART_UNAPPROVED.glb"
                shutil.copyfile(p,dst)
                b=dst.read_bytes()
                if b[:4]!=b"glTF" or struct.unpack_from("<I",b,8)[0]!=len(b):
                    dst.unlink(missing_ok=True)
                    raise ValueError("Returned content fails binary glTF length and magic")
                status["source_glb_bytes"]=len(b)
                status["source_glb_sha256"]=sha256(dst)
                status["outcome"]="TRUE_GLB_GENERATED_UNAPPROVED"
                valid=True
                break
        if not valid:
            raise RuntimeError("Space returned no locally readable binary .glb: "+str(paths)[:500])
    except Exception as exc:
        status["outcome"]="FREE_ROUTE_BLOCKED_OR_FAILED_NO_MODEL"
        status["error_type"]=type(exc).__name__
        status["error_message"]=str(exc)[:4000]
        (out/"failure_traceback.txt").write_text(traceback.format_exc())
        print("RUN99_FREE_ROUTE_FAILURE",type(exc).__name__,str(exc)[:400],flush=True)
    finally:
        (out/"run99_status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2))
        (out/"ART_GATE_NOT_PASSED.md").write_text(
          "# ART_UNAPPROVED / independent Run99\n\n"
          "Hugging Face public ZeroGPU trial, no user token or paid credit. Original reference is the **rightmost** owl of #172 v3. "
          "Geometry from one front illustration cannot verify side and back anatomy. "
          "No automatically generated model is approved for release, regardless of glTF validity. "
          "No real phone GPU tests, no animation quality, no license clearance for remote model weights or generated work.\n\n"
          "Current technical outcome: "+status["outcome"]+"\n")
        print("RUN99_STATUS",json.dumps(status,ensure_ascii=False)[:5000],flush=True)

def render(args):
    import bpy
    from mathutils import Vector
    from math import radians, sin, cos
    p=pathlib.Path(args.out); p.mkdir(exist_ok=True,parents=True)
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=args.model)
    meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    if not meshes:
        raise RuntimeError("No meshes after Blender glTF import")
    bounds=[o.matrix_world @ Vector(c) for o in meshes for c in o.bound_box]
    lo=Vector((min(v[i] for v in bounds) for i in range(3)))
    hi=Vector((max(v[i] for v in bounds) for i in range(3)))
    center=(lo+hi)/2
    dims=hi-lo
    size=max(dims)
    if size<=0: raise RuntimeError("degenerate mesh")
    # Original Gradio GLB may be Z-up in Blender, native import handles glTF axis.
    scene=bpy.context.scene
    scene.render.engine="CYCLES"
    scene.cycles.samples=22
    scene.cycles.use_denoising=False
    scene.render.resolution_x=512
    scene.render.resolution_y=512
    scene.render.resolution_percentage=100
    scene.world.color=(0.30,0.30,0.30)
    for o in bpy.data.objects:
        if o.type=="LIGHT":
            bpy.data.objects.remove(o,do_unlink=True)
    def area(name, xyz, power, scale):
        data=bpy.data.lights.new(name,type="AREA")
        data.energy=power;data.shape="DISK";data.size=scale
        obj=bpy.data.objects.new(name,data);scene.collection.objects.link(obj)
        obj.location=center+Vector(xyz)*size
        direct=center-obj.location
        obj.rotation_euler=direct.to_track_quat("-Z","Y").to_euler()
    area("softbox-left",(-2.5,-3,3.2),400,4.5*size)
    area("rim",(1.9,1.8,2.8),300,2.9*size)
    cam_data=bpy.data.cameras.new("RUN99_Multiview")
    cam_obj=bpy.data.objects.new("RUN99_Multiview",cam_data)
    scene.collection.objects.link(cam_obj);scene.camera=cam_obj
    cam_obj.data.type="ORTHO";cam_obj.data.ortho_scale=1.55*size
    for k,ang in [("front",0),("quarter",45),("side",90),("back",180)]:
        a=radians(ang)
        cam_obj.location=center+Vector((4*sin(a),-4*cos(a),1.5))*size
        direction=center-cam_obj.location
        cam_obj.rotation_euler=direction.to_track_quat("-Z","Y").to_euler()
        scene.render.filepath=str(p/f"run99_{k}_native_cycles_UNAPPROVED.png")
        bpy.ops.render.render(write_still=True)
        print("CYCLES_RENDERED",k,scene.render.filepath,flush=True)
    bpy.ops.export_scene.gltf(filepath=str(p/"run99_roundtrip_from_blender_UNAPPROVED.glb"), export_format="GLB")
    metrics=dict(imported_meshes=len(meshes),bounding_dimensions=list(dims),blender_version=bpy.app.version_string,rendered_views=4)
    (p/"run99_blender_metrics.json").write_text(json.dumps(metrics,indent=2))
    print("BLENDER_NATIVE_ROUNDTRIP",json.dumps(metrics),flush=True)

def manifest(args):
    from PIL import Image,ImageDraw
    p=pathlib.Path(args.out)
    names=["front","quarter","side","back"]
    views=[p/f"run99_{k}_native_cycles_UNAPPROVED.png" for k in names]
    if all(v.is_file() for v in views):
        contact=Image.new("RGB",(1024,1024),(246,244,239))
        for i,path in enumerate(views):
            im=Image.open(path).convert("RGB")
            contact.paste(im,((i%2)*512,(i//2)*512))
            ImageDraw.Draw(contact).text((12+(i%2)*512,10+(i//2)*512),names[i],fill=(0,0,0))
        contact.save(p/"run99_four_views_ART_UNAPPROVED.jpg",quality=84)
        emit_image_for_review(p/"run99_four_views_ART_UNAPPROVED.jpg","RUN99_NATIVE_RENDER_CONTACT")
    for glb in p.glob("*.glb"):
        b=glb.read_bytes()
        print("GLB_INTEGRITY",glb.name,len(b),b[:4],struct.unpack_from("<I",b,8)[0])
    files=sorted(x for x in p.iterdir() if x.is_file() and x.name!="SHA256SUMS.txt")
    (p/"SHA256SUMS.txt").write_text("".join(sha256(x)+"  "+x.name+"\n" for x in files))
    print("RUN99_ARCHIVED",len(files),flush=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",choices=["generate","render","manifest"],required=True)
    parser.add_argument("--source",default="")
    parser.add_argument("--out",required=True)
    parser.add_argument("--model",default="")
    args=parser.parse_args()
    dict(generate=generate,render=render,manifest=manifest)[args.mode](args)
