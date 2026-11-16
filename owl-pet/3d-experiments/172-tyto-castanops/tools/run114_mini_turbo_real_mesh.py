#!/usr/bin/env python3
"""Run114 isolated artistically unapproved true-image-to-mesh study.
One anonymous ZeroGPU call; no paid provider, no proxy art, no deployment.
Target: RIGHTMOST age-unknown downy chick from canonical #172 v3 concept.
"""
import argparse, hashlib, io, json, pathlib, shutil, struct, time, traceback
from datetime import datetime,timezone

RUN="114"
PROVIDER="tencent/Hunyuan3D-2mini-Turbo"
def digest(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def paths(v):
    if isinstance(v,(str,pathlib.Path)):
        s=str(v)
        if s.lower().split("?")[0].endswith(".glb"): yield s
    elif isinstance(v,dict):
        for x in v.values(): yield from paths(x)
    elif isinstance(v,(list,tuple)):
        for x in v: yield from paths(x)

def generate(a):
    from PIL import Image,ImageDraw,ImageFilter
    out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
    concept=Image.open(a.concept).convert("RGB")
    assert concept.size==(1536,1024),"Canonical concept dimensions unexpectedly changed"
    reference=concept.crop((960,272,1412,878))
    reference.save(out/"canonical_rightmost_reference_crop.png")
    src=Image.open(a.source).convert("RGB")
    # Same recovered actual rightmost owl, no fabricated back/side images.
    # Preserve dark interiors (eyes) via border-connected floodfill; use warm
    # neutral RGB matting and upstream built-in rembg to avoid Run105's
    # transparent alpha Hunyuan failure.
    mask=src.convert("L").point(lambda t:255 if t>16 else 0)
    ImageDraw.floodfill(mask,(0,0),128,thresh=0)
    alpha=mask.point(lambda x:0 if x==128 else 255)
    alpha=alpha.filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.GaussianBlur(.7))
    bbox=alpha.getbbox()
    assert bbox is not None
    owl=src.copy();owl.putalpha(alpha);owl=owl.crop(bbox)
    side=max(owl.size)
    canvas=Image.new("RGBA",(side,side),(0,0,0,0))
    canvas.alpha_composite(owl,((side-owl.width)//2,(side-owl.height)//2))
    canvas=canvas.resize((420,420),Image.Resampling.LANCZOS)
    framing=Image.new("RGBA",(512,512),(0,0,0,0))
    framing.alpha_composite(canvas,(46,46))
    inp=Image.new("RGB",(512,512),(243,241,236))
    inp.paste(framing,mask=framing.getchannel("A"))
    input_path=out/"rightmost_cream_mesoptile_neutralRGB_512.png"
    inp.save(input_path)
    state={"run":RUN,"stage":"input_prepared","gate":"ART_REJECTED_UNLESS_INDEPENDENT_VISUAL_PASS",
           "date_utc":datetime.now(timezone.utc).isoformat(),
           "provider":PROVIDER,"endpoint":"https://huggingface.co/spaces/"+PROVIDER,
           "method":"actual public image->native geometry, mini Turbo 0.6B; one call",
           "input_source":"preprocessed_image.png of same rightmost #172 v3 target",
           "source_sha256":digest(a.source),"concept_sha256":digest(a.concept),
           "reference_crop_sha256":digest(out/"canonical_rightmost_reference_crop.png"),
           "input_sha256":digest(input_path),"input_mask_bbox":bbox,
           "background":"neutral RGB, native rembg on","zero_extra_spend":True,
           "no_api_key_or_token":True,"source_model_license":"Tencent Hunyuan non-commercial",
           "full_global_use_license_cleared":False,
           "real_physical_phone_gpu_tested":False,"outcome":"NOT_ATTEMPTED"}
    (out/"preflight.json").write_text(json.dumps(state,ensure_ascii=False,indent=2))
    try:
        from gradio_client import Client,handle_file
        import httpx,gradio_client
        state["client_version"]=gradio_client.__version__
        cli=Client(PROVIDER,verbose=False,
                   httpx_kwargs={"timeout":httpx.Timeout(90,connect=25)})
        api=cli.view_api(return_format="dict")
        (out/"live_public_api.json").write_text(json.dumps(api,default=str,indent=2)[:130000])
        eps=list(api.get("named_endpoints",{}))
        state["named_endpoints"]=eps
        if "/shape_generation" not in eps:
            raise RuntimeError("No public /shape_generation endpoint on the live official Space")
        state["stage"]="one_native_shape_generation"
        # Official live gradio_app.py (Tencent mini Turbo) lists precisely:
        # caption, image, mv_front, mv_back, mv_left, mv_right,
        # steps, cfg, seed, octree, rembg, chunks, random_seed.
        # Shape ONLY: no texture claim; no invented multiview evidence.
        started=time.monotonic()
        result=cli.predict(None,handle_file(str(input_path)),
                           None,None,None,None,
                           5,5.0,172,256,True,8000,False,
                           api_name="/shape_generation")
        state["elapsed_sec"]=round(time.monotonic()-started,2)
        state["response_brief"]=str(result)[:2500]
        saved=False
        for item in paths(result):
            q=pathlib.Path(item)
            if not q.is_file() or q.stat().st_size<20000:continue
            data=q.read_bytes()
            if data[:4]!=b"glTF" or struct.unpack_from("<I",data,8)[0]!=len(data):
                continue
            dest=out/"run114_true_3d_geometry_UNAPPROVED.glb"
            shutil.copyfile(q,dest)
            state.update({"glb_bytes":len(data),"glb_sha256":digest(dest)})
            saved=True;break
        if not saved:raise RuntimeError("No valid native .glb downloaded from public prediction")
        state["outcome"]="ACTUAL_NATIVE_GLB_GENERATED_ART_UNAPPROVED"
    except Exception as e:
        state["outcome"]="FREE_TOOL_FAILED_OR_BLOCKED_NO_GLB"
        state["error_type"]=type(e).__name__
        state["error"]=str(e)[:3500]
        (out/"generation_error_traceback.txt").write_text(traceback.format_exc())
        print("REAL_TOOL_FAILURE",str(e)[:1200],flush=True)
    (out/"run114_status.json").write_text(json.dumps(state,indent=2,ensure_ascii=False))
    print("RUN114_GENERATION_SUMMARY",json.dumps(state,ensure_ascii=False)[:4500],flush=True)

def render(a):
    import bpy
    from mathutils import Vector
    from math import radians,sin,cos
    out=pathlib.Path(a.out);out.mkdir(exist_ok=True,parents=True)
    bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=str(pathlib.Path(a.model).resolve()))
    meshes=[m for m in bpy.context.scene.objects if m.type=="MESH"]
    if not meshes:raise RuntimeError("No real meshes after native Blender GLB import")
    worldpts=[m.matrix_world @ Vector(p) for m in meshes for p in m.bound_box]
    low=Vector(tuple(min(p[i] for p in worldpts) for i in range(3)))
    high=Vector(tuple(max(p[i] for p in worldpts) for i in range(3)))
    center=(high+low)*.5;size=max(high-low)
    assert size>0
    scene=bpy.context.scene
    scene.render.engine="CYCLES";scene.cycles.samples=16
    scene.cycles.use_denoising=False
    scene.render.resolution_x=512;scene.render.resolution_y=512
    scene.render.resolution_percentage=100
    scene.world.color=(.27,.28,.29)
    # Neutral warm clay preview, explicitly *not* synthesized actual down.
    mat=bpy.data.materials.new("UNAPPROVED_NEUTRAL_PREVIEW_NO_REAL_FEATHER_TEXTURE")
    mat.diffuse_color=(.77,.70,.58,1)
    mat.use_nodes=True
    bs=mat.node_tree.nodes.get("Principled BSDF")
    if bs:bs.inputs["Base Color"].default_value=(.79,.71,.57,1);bs.inputs["Roughness"].default_value=.93
    for mesh in meshes:
        mesh.data.materials.clear();mesh.data.materials.append(mat)
    for name,pos,power in [("softbox",(-3,-3,4),330),("rim",(2,2,3),240)]:
        la=bpy.data.lights.new(name,"AREA");la.energy=power;la.size=5*size
        obj=bpy.data.objects.new(name,la);scene.collection.objects.link(obj)
        obj.location=center+Vector(pos)*size
        obj.rotation_euler=(center-obj.location).to_track_quat("-Z","Y").to_euler()
    camd=bpy.data.cameras.new("actual_native_4view");cam=bpy.data.objects.new("actual_native_4view",camd)
    scene.collection.objects.link(cam);scene.camera=cam;camd.type="ORTHO";camd.ortho_scale=1.64*size
    for name,ang in [("front",0),("quarter",45),("side",90),("back",180)]:
        rad=radians(ang);cam.location=center+Vector((4*sin(rad),-4*cos(rad),1.18))*size
        cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
        scene.render.filepath=str((out/("run114_"+name+"_real_native_cycles.png")).resolve())
        bpy.ops.render.render(write_still=True)
    metrics={"blender":bpy.app.version_string,"mesh_count":len(meshes),
             "polygons":sum(len(m.data.polygons) for m in meshes),
             "bounding_dimensions":list(high-low),"true_native_views":4,
             "preview_shader":"neutral clay only, NO true cream down or alpha fur"}
    (out/"run114_native_metrics.json").write_text(json.dumps(metrics,indent=2))
    bpy.ops.export_scene.gltf(filepath=str((out/"run114_blender_roundtrip_UNAPPROVED.glb").resolve()),export_format="GLB")
    print("REAL_BLENDER_RENDERED",json.dumps(metrics),flush=True)

def manifest(a):
    from PIL import Image,ImageDraw
    out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
    names=["front","quarter","side","back"]
    p=[out/("run114_"+n+"_real_native_cycles.png") for n in names]
    if all(q.is_file() for q in p):
        contact=Image.new("RGB",(1024,1024),(246,244,240))
        for i,q in enumerate(p):
            im=Image.open(q).convert("RGB").resize((512,512))
            x=(i%2)*512;y=(i//2)*512;contact.paste(im,(x,y))
            ImageDraw.Draw(contact).text((x+12,y+12),names[i],fill=(0,0,0))
        contact.save(out/"run114_four_true_angles_NOT_APPROVED.jpg",quality=83)
    (out/"ART_REJECTED.flag").write_text(
       "No release. Image-to-shape geometry alone lacks validated down, mature bark support, trustworthy side/back, actual mobile GPU, and commercial/worldwide asset rights. Human visual review mandatory.\n")
    files=sorted(q for q in out.iterdir() if q.is_file() and q.name not in ("SHA256SUMS.txt","sha_check.log"))
    (out/"SHA256SUMS.txt").write_text("".join(digest(q)+"  "+q.name+"\n" for q in files))
    print("EVIDENCE_ARCHIVED",len(files),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["generate","render","manifest"],required=True)
    ap.add_argument("--source",default="")
    ap.add_argument("--concept",default="")
    ap.add_argument("--model",default="")
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    dict(generate=generate,render=render,manifest=manifest)[a.mode](a)
