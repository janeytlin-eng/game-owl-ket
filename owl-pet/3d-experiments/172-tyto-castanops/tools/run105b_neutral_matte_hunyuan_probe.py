#!/usr/bin/env python3
"""#172 quarantined ZERO-ADDITIONAL-CHARGE HuggingFace ZeroGPU true-mesh study.

This does not call paid fal/Meshy/Tripo accounts or edit the existing pet.
No output is accepted without human visual review against the original rightmost nestling.
"""
import argparse, base64, hashlib, json, os, pathlib, shutil, struct, sys, time, traceback
from datetime import datetime, timezone

PREF="Run105B/free-ZeroGPU/UNAPPROVED"

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
    # Real foreground isolation from Run103; retains actual rightmost chick and hollow.
    # This is genuinely different input from Run99's unsegmented photograph crop.
    from PIL import ImageDraw, ImageFilter
    original=Image.open(source).convert("RGB")
    w,h=original.size
    binary=original.convert("L").point(lambda v: 255 if v>16 else 0)
    ImageDraw.floodfill(binary,(0,0),128,thresh=0)
    alpha=binary.point(lambda v: 0 if v==128 else 255)
    alpha=alpha.filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.GaussianBlur(0.7))
    coverage=sum(v>100 for v in alpha.resize((64,64)).getdata())/4096
    if not (0.10 < coverage < 0.90):
        raise RuntimeError("Unreliable actual foreground segmentation coverage: "+str(coverage))
    cut=original.copy();cut.putalpha(alpha)
    bbox=alpha.getbbox()
    # Preserve isolated full silhouette, avoiding aspect-ratio distortion or fabricated geometry.
    cut=cut.crop(bbox)
    side=max(cut.size)
    canvas=Image.new("RGBA",(side+max(32,side//6),side+max(32,side//6)),(0,0,0,0))
    canvas.alpha_composite(cut,((canvas.width-cut.width)//2,(canvas.height-cut.height)//2))
    crop=canvas.resize((512,512),Image.Resampling.LANCZOS)
    # Hunyuan image preprocess may interpret RGBA as an opaque box when rembg is disabled.
    # Controlled ablation: exact same isolated pixels, COMPOSITED RGB instead of alpha,
    # neutral warm background, then provider-native remove-background enabled.
    neutral=Image.new("RGB",crop.size,(246,245,241))
    neutral.paste(crop,mask=crop.getchannel("A"))
    crop=neutral
    crop.save(out/"rightmost_mesoptile_input.png")
    emit_image_for_review(out/"rightmost_mesoptile_input.png","RUN105B_INPUT_FOREGROUND")
    print("RUN105B_FOREGROUND_SEGMENTATION",{"source":str(source),"coverage":coverage,"bbox":bbox,"shape":crop.size},flush=True)
    status=dict(run="105B",gate="ART_UNAPPROVED",source_repo="janeytlin-eng/game-owl-ket",
      source_path="owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run103-TRELLIS2-PBR-ART_UNAPPROVED/preprocessed_image.png",
      source_image_size=[w,h],crop_box=bbox,crop_size=list(crop.size),
      date_utc=datetime.now(timezone.utc).isoformat(),
      no_extra_charge=True,provider="https://huggingface.co/spaces/tencent/Hunyuan3D-2",
      provider_mode="public ZeroGPU; no auth token; geometry-only; no paid fallback",
      previous_negative_controls=["Run99 original background image neural mesh","Run104 clean matte CPU TripoSR failed"],
      outcome="NOT_ATTEMPTED",segmented_foreground=True,source_black_bg_not_raw_concept=True,source_coverage=coverage,neutral_rgb_background=True,provider_rembg=True,release_license_not_cleared=True)
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
            image=handle_file(str(out/"rightmost_mesoptile_input.png")),
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
                dst=out/"run105b_neural_source_ART_UNAPPROVED.glb"
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
        print("RUN105B_FREE_ROUTE_FAILURE",type(exc).__name__,str(exc)[:400],flush=True)
    finally:
        (out/"run105b_status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2))
        (out/"ART_GATE_NOT_PASSED.md").write_text(
          "# ART_UNAPPROVED / independent Run105B\n\n"
          "Hugging Face public ZeroGPU trial, no user token or paid credit. Actual foreground cutout from Run103 is the **rightmost** owl of #172 v3. "
          "Geometry from one front illustration cannot verify side and back anatomy. "
          "No automatically generated model is approved for release, regardless of glTF validity. "
          "No real phone GPU tests, no animation quality, no license clearance for remote model weights or generated work.\n\n"
          "Current technical outcome: "+status["outcome"]+"\n")
        print("RUN105B_STATUS",json.dumps(status,ensure_ascii=False)[:5000],flush=True)

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
    cam_data=bpy.data.cameras.new("RUN105B_Multiview")
    cam_obj=bpy.data.objects.new("RUN105B_Multiview",cam_data)
    scene.collection.objects.link(cam_obj);scene.camera=cam_obj
    cam_obj.data.type="ORTHO";cam_obj.data.ortho_scale=1.55*size
    for k,ang in [("front",0),("quarter",45),("side",90),("back",180)]:
        a=radians(ang)
        cam_obj.location=center+Vector((4*sin(a),-4*cos(a),1.5))*size
        direction=center-cam_obj.location
        cam_obj.rotation_euler=direction.to_track_quat("-Z","Y").to_euler()
        scene.render.filepath=str(p/f"run105b_{k}_native_cycles_UNAPPROVED.png")
        bpy.ops.render.render(write_still=True)
        print("CYCLES_RENDERED",k,scene.render.filepath,flush=True)
    bpy.ops.export_scene.gltf(filepath=str(p/"run105b_roundtrip_from_blender_UNAPPROVED.glb"), export_format="GLB")
    metrics=dict(imported_meshes=len(meshes),bounding_dimensions=list(dims),blender_version=bpy.app.version_string,rendered_views=4)
    (p/"run105b_blender_metrics.json").write_text(json.dumps(metrics,indent=2))
    print("BLENDER_NATIVE_ROUNDTRIP",json.dumps(metrics),flush=True)

def manifest(args):
    from PIL import Image,ImageDraw
    p=pathlib.Path(args.out)
    names=["front","quarter","side","back"]
    views=[p/f"run105b_{k}_native_cycles_UNAPPROVED.png" for k in names]
    if all(v.is_file() for v in views):
        contact=Image.new("RGB",(1024,1024),(246,244,239))
        for i,path in enumerate(views):
            im=Image.open(path).convert("RGB")
            contact.paste(im,((i%2)*512,(i//2)*512))
            ImageDraw.Draw(contact).text((12+(i%2)*512,10+(i//2)*512),names[i],fill=(0,0,0))
        contact.save(p/"run105b_four_views_ART_UNAPPROVED.jpg",quality=84)
        emit_image_for_review(p/"run105b_four_views_ART_UNAPPROVED.jpg","RUN105B_NATIVE_RENDER_CONTACT")
    for glb in p.glob("*.glb"):
        b=glb.read_bytes()
        print("GLB_INTEGRITY",glb.name,len(b),b[:4],struct.unpack_from("<I",b,8)[0])
    files=sorted(x for x in p.iterdir() if x.is_file() and x.name not in ("SHA256SUMS.txt","manifest_output.log"))
    (p/"SHA256SUMS.txt").write_text("".join(sha256(x)+"  "+x.name+"\n" for x in files))
    print("RUN105B_ARCHIVED",len(files),flush=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",choices=["generate","render","manifest"],required=True)
    parser.add_argument("--source",default="")
    parser.add_argument("--out",required=True)
    parser.add_argument("--model",default="")
    args=parser.parse_args(sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else None)
    dict(generate=generate,render=render,manifest=manifest)[args.mode](args)
