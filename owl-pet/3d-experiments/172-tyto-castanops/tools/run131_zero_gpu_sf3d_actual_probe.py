#!/usr/bin/env python3
"""Run131: one no-cost, unauthenticated, evidence-first attempt to reconstruct #172 from the actual v3 crop.
Never publishes or authorizes an art sample. No paid API, no account login, and never bypasses a quota.
"""
import datetime
import hashlib
import json
import os
import shutil
import sys
import time
import traceback
from pathlib import Path

import requests
from PIL import Image, ImageFilter

OUT=Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
SOURCE_URL="https://raw.githubusercontent.com/janeytlin-eng/game-owl-ket/main/owl-pet/design/concepts/172-tyto-castanops-v3.png"
EXPECTED_SOURCE_SHA="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
MODEL="stabilityai/stable-fast-3d"
RESULT={"run":"131","utc_started":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source":SOURCE_URL, "model_space":MODEL,
        "rights":"research-only provisional: model community license is revenue conditioned; no permission to distribute inferred",
        "charge_authorized":False,"external_paid_calls":0,"physical_phone_gpu_verified":False,
        "art_decision":"ART_UNREVIEWED","release":"NO_RELEASE"}
def save():
    (OUT/"run131_result.json").write_text(json.dumps(RESULT,ensure_ascii=False,indent=2,default=str)+"\n")
def stage(name, action):
    t=time.monotonic()
    try:
        result=action()
        RESULT[name]={"status":"success","seconds":round(time.monotonic()-t,3)}
        save()
        return result
    except Exception as exc:
        RESULT[name]={"status":"failed","seconds":round(time.monotonic()-t,3),
                      "exception_type":type(exc).__name__,"error":str(exc)[:1800],
                      "traceback":traceback.format_exc()[-7000:]}
        save()
        return None
def source():
    r=requests.get(SOURCE_URL,timeout=45)
    RESULT["source_http"]={"status":r.status_code,"bytes":len(r.content),"content_type":r.headers.get("content-type")}
    r.raise_for_status()
    d=hashlib.sha256(r.content).hexdigest()
    RESULT["source_sha256"]=d
    if d != EXPECTED_SOURCE_SHA:
        raise ValueError("Source concept differs from immutable Run92 fingerprint; refuse inference until verified")
    p=OUT/"run131_v3_concept_source.png"
    p.write_bytes(r.content)
    im=Image.open(p).convert("RGB")
    RESULT["full_image_size"]=list(im.size)
    if im.size!=(1536,1024):raise ValueError("Unexpected concept plate dimension")
    crop=im.crop((970,260,1435,836))
    crop.save(OUT/"run131_original_rightmost_crop.png")
    RESULT["crop_box"]=[970,260,1435,836]
    return crop
def prepare(crop):
    import rembg
    # The actual rembg u2netp segmentation is a test hypothesis, not a guaranteed accurate anatomy mask.
    mask=rembg.remove(crop,only_mask=True,session=rembg.new_session("u2netp")).convert("L")
    mask=mask.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))
    mask.save(OUT/"run131_predicted_alpha_mask.png")
    b=mask.getbbox()
    RESULT["segmentation_bbox"]=b
    if b is None or mask.getextrema()[1]<50: raise ValueError("No foreground after segmentation")
    # Do not repaint or invent hidden 3D anatomy. Preserve original RGB so small dark eyes aren't replaced.
    rgba=crop.copy().convert("RGBA")
    rgba.putalpha(mask)
    source_region=rgba.crop(b)
    canvas=Image.new("RGBA",(512,512),(127,127,127,0))
    source_region.thumbnail((435,435),Image.Resampling.LANCZOS)
    xy=((512-source_region.width)//2,(512-source_region.height)//2)
    canvas.alpha_composite(source_region,dest=xy)
    canvas.save(OUT/"run131_rgba_zero_gpu_input.png")
    RESULT["mask_nonzero_fraction"]=round(sum(v for v in mask.getdata())/(255.0*mask.width*mask.height),5)
    RESULT["input_png_bytes"]=(OUT/"run131_rgba_zero_gpu_input.png").stat().st_size
    return OUT/"run131_rgba_zero_gpu_input.png"
def api_inspect():
    from gradio_client import Client
    c=Client(MODEL, verbose=False, httpx_kwargs={"timeout":60.0})
    api=c.view_api(return_format="dict")
    (OUT/"run131_live_gradio_api.json").write_text(json.dumps(api,indent=2,default=str)[:50000])
    RESULT["gradio_endpoints"]=list((api or {}).get("named_endpoints",{}).keys())
    return c
def attempt_predict(cli, input_path):
    from gradio_client import handle_file
    # This Space's public source gradio_app.py specifies requires_bg_remove + run_button.
    # For an already-transparent input, requires_bg_remove fills the session's background_state;
    # do not fabricate its value or use premium endpoints.
    RESULTS_LOG=[]
    image=handle_file(str(input_path.resolve()))
    RESULT["client_call"]={"preprocess":"requires_bg_remove","mesh":"run_button","scope":"one inference at most"}
    try:
        x=cli.predict(image,0.85,api_name="/requires_bg_remove")
        RESULTS_LOG.append({"preprocess":"ok","response_type":type(x).__name__,"preview":str(x)[:500]})
    except Exception as exc:
        RESULTS_LOG.append({"preprocess":"error","type":type(exc).__name__,"error":str(exc)[:1200]})
        (OUT/"run131_inference_calls.json").write_text(json.dumps(RESULTS_LOG,indent=2))
        raise RuntimeError("Live Gradio preprocessing failed; no GPU inference sent") from exc
    # The preprocessor stores img_proc_state and background_remove_state in Gradio's session.
    # The Gradio client excludes state parameters from the public API schema in some releases.
    # Inspect public schema and supply exactly its nonstate inputs.
    public=(cli.view_api(return_format="dict") or {}).get("named_endpoints",{})
    chosen=next((v for k,v in public.items() if "run_button" in k),None)
    if not chosen: raise RuntimeError("No public run_button; respect private API boundary")
    params=chosen.get("parameters",[])
    names=[str(p.get("parameter_name") or p.get("label") or "").lower() for p in params]
    RESULT["inference_parameter_names"]=names
    available={"run_btn":"Run","input_image":image,"background_state":None,
               "foreground_ratio":0.85,"remesh_option":"None",
               "vertex_count":-1,"texture_size":1024}
    positional=[]
    for p in params:
        n=(p.get("parameter_name") or p.get("label") or "").lower()
        if "run" in n and "btn" in n: positional.append("Run")
        elif "input" in n and "image" in n: positional.append(image)
        elif "background" in n and "state" in n: positional.append(None)
        elif "foreground" in n and "ratio" in n: positional.append(0.85)
        elif "remesh" in n: positional.append("None")
        elif "vertex" in n: positional.append(-1)
        elif "texture" in n: positional.append(1024)
        else:
            if p.get("has_default"):
                positional.append(p.get("parameter_default"))
            else:raise RuntimeError("Unknown mandatory Gradio input: "+str(p))
    if not positional:
        # Public source's seven input components, with hidden Gradio states removed.
        positional=["Run",image,0.85,"None",-1,1024]
    (OUT/"run131_inference_argument_types.json").write_text(json.dumps({"names":names,"types":[type(x).__name__ for x in positional]},indent=2))
    try:
        response=cli.predict(*positional,api_name="/run_button")
    except Exception as exc:
        RESULTS_LOG.append({"inference":"error","type":type(exc).__name__,"error":str(exc)[:2000]})
        (OUT/"run131_inference_calls.json").write_text(json.dumps(RESULTS_LOG,indent=2))
        raise
    RESULTS_LOG.append({"inference":"returned","response_type":type(response).__name__,"preview":str(response)[:1000]})
    (OUT/"run131_inference_calls.json").write_text(json.dumps(RESULTS_LOG,indent=2))
    # Gradio returns a local downloaded path if the model is actually available.
    def paths(x):
        if isinstance(x,str):
            if os.path.isfile(x) and x.lower().endswith(".glb"):yield x
        elif isinstance(x,dict):
            for v in x.values():yield from paths(v)
        elif isinstance(x,(tuple,list)):
            for v in x:yield from paths(v)
    hits=list(paths(response))
    if not hits:raise RuntimeError("No actual downloaded GLB in returned response; never claim successful 3D")
    found=Path(hits[0])
    data=found.read_bytes()
    if len(data)<1000 or data[:4]!=b"glTF":raise ValueError("Returned payload not a real GLB")
    target=OUT/"run131_zero_gpu_SOURCE_RESEARCH_ONLY.glb"
    target.write_bytes(data)
    RESULT["generated_glb"]={"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),
                            "model":MODEL,"generated_from":"rightmost crop of actual source concept"}
    return target
def main():
    save()
    crop=stage("source_verify",source)
    if crop is None:return
    inp=stage("background_segmentation",lambda:prepare(crop))
    if inp is None:return
    cli=stage("public_space_api_inspect",api_inspect)
    if cli is None:return
    file=stage("free_neural_mesh_inference",lambda:attempt_predict(cli,inp))
    if file is None:return
    def check_mesh():
        import trimesh
        obj=trimesh.load(str(file),force="scene")
        mlist=list(obj.geometry.values())
        nfaces=sum(len(m.faces) for m in mlist if isinstance(m,trimesh.Trimesh))
        RESULT["generated_mesh_inspection"]={"submesh_count":len(mlist),"triangles":nfaces}
        if nfaces<2000:raise ValueError("GLB has too little geometry to assess premium sculpt")
        return True
    stage("actual_glb_topology",check_mesh)
    save()
if __name__=="__main__":
    main()
