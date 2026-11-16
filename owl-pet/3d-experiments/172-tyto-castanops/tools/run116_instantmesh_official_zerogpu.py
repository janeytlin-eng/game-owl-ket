#!/usr/bin/env python3
"""#172 standalone TRUE 3D trial: official InstantMesh public ZeroGPU.
No token, card, paid inference, account rotations, fake meshes or silent fallback.
Never mark art approved from file-format or Blender success alone.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import struct
import time
import traceback
from datetime import datetime, timezone

SPACE = "TencentARC/InstantMesh"
EXPECTED_INPUT_SHA256 = "6c66a656f73ee8254b1688a8e572a9f048647053d7552cd8c95c66ae5b4319cb"

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def get_path(value):
    if isinstance(value, (str, Path)):
        p = Path(str(value))
        return p if p.is_file() else None
    if isinstance(value, dict):
        for key in ("path", "name", "file", "value"):
            if key in value:
                p=get_path(value[key])
                if p: return p
    if isinstance(value, (tuple, list)):
        for element in value:
            p=get_path(element)
            if p: return p
    return None

def get_all_paths(value):
    if isinstance(value, (str, Path)):
        p=Path(str(value))
        if p.is_file(): yield p
    elif isinstance(value, dict):
        for element in value.values(): yield from get_all_paths(element)
    elif isinstance(value, (tuple, list)):
        for element in value: yield from get_all_paths(element)

def copy_as(value, dest, required_suffix=""):
    files=list(get_all_paths(value))
    if required_suffix:
        files=[p for p in files if p.suffix.lower()==required_suffix.lower()]
    if not files:
        raise RuntimeError("Remote result did not provide locally readable file "+required_suffix+": "+str(value)[:1200])
    src=files[0]
    if src.resolve()!=dest.resolve(): shutil.copyfile(src, dest)
    if not dest.is_file() or dest.stat().st_size<5000:
        raise RuntimeError("Returned file is missing/tiny: "+str(dest))
    return dest

def image_as_png(value,dest):
    from PIL import Image
    src=get_path(value)
    if not src:
        raise RuntimeError("No returned accessible image for "+str(dest)+": "+str(value)[:600])
    with Image.open(src) as im:
        im.convert("RGBA").save(dest,format="PNG")
    if dest.stat().st_size<5000:
        raise RuntimeError("Provider returned a tiny or blank image: "+str(dest))
    return dest

def main(source,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    status=dict(run="116",probe="InstantMesh official actual multi-view→mesh ZeroGPU",
       source_repo="janeytlin-eng/game-owl-ket",
       input_path=str(source),
       provider="https://huggingface.co/spaces/"+SPACE,
       provider_license_claim="Apache-2.0 (code/weights); result distribution separately unverified",
       auth_token_used=False,paid_charge_authorized=False,free_public_guest=True,
       created_utc=datetime.now(timezone.utc).isoformat(),
       desired_stage="generate real multiview images and true GLB",stage="initial",
       output="NO_ASSET",art_gate="ART_REJECTED",mobile_physical_gpu_test=False,
       previous_main_blocker="Hunyuan neural mesh backside scales and elongated rear")
    try:
        source=Path(source)
        h=sha(source)
        status["input_sha256"]=h
        if h!=EXPECTED_INPUT_SHA256:
            raise RuntimeError("Canonical Run114C RGB input SHA mismatch; do not generate from unrelated owl.")
        copy=out/"rightmost_reference_rgb_512.png"
        shutil.copyfile(source,copy)
        from PIL import Image
        with Image.open(copy) as im:
            status["input_dimensions"]=list(im.size)
            status["input_mode"]=im.mode
        if status["input_dimensions"] != [512,512]:
            raise ValueError("Unexpected image dimension")
        from gradio_client import Client,handle_file
        import httpx
        # client top-level config fetch has independent read timeout; bounded, no bypass.
        native_get=httpx.get
        def bounded_get(*a,**k):
            if not k.get("timeout"):
                k["timeout"]=httpx.Timeout(65.0,connect=18.0)
            return native_get(*a,**k)
        httpx.get=bounded_get
        try:
            client=Client(SPACE,verbose=False,httpx_kwargs={"timeout":httpx.Timeout(65.0,connect=18.0)})
        finally:
            httpx.get=native_get
        schema=client.view_api(return_format="dict")
        (out/"official_live_api.json").write_text(json.dumps(schema,ensure_ascii=False,default=str,indent=2)[:140000])
        status["stage"]="live public Gradio API observed"
        keys=set(schema.get("named_endpoints",{}).keys())
        status["named_endpoints"]=sorted(keys)
        required=("/preprocess","/generate_mvs","/make3d")
        if not all(k in keys for k in required):
            raise RuntimeError("Official live API changed; incompatible endpoints: "+repr(sorted(keys)))
        # A single free request at each GPU step; never retry over quota.
        status["stage"]="provider preprocess request"
        before=time.monotonic()
        prep=client.predict(handle_file(str(copy)),True,api_name="/preprocess")
        image_as_png(prep,out/"run116_preprocessed_actual.png")
        status["preprocess_seconds"]=round(time.monotonic()-before,3)
        status["stage"]="real multi-view diffusion inference"
        before=time.monotonic()
        mvs=client.predict(handle_file(str(out/"run116_preprocessed_actual.png")),30,42,api_name="/generate_mvs")
        status["multi_view_seconds"]=round(time.monotonic()-before,3)
        if not isinstance(mvs,(tuple,list)) or len(mvs)<1:
            raise RuntimeError("Multiview returned unrecognized shape: "+str(mvs)[:1000])
        image_as_png(mvs[0],out/"run116_multi_view_actual.png")
        if len(mvs)>1:
            image_as_png(mvs[1],out/"run116_multi_view_grid_actual.png")
        status["stage"]="actual sparse-view reconstruction to polygon mesh"
        before=time.monotonic()
        recon=client.predict(handle_file(str(out/"run116_multi_view_actual.png")),api_name="/make3d")
        status["mesh_reconstruction_seconds"]=round(time.monotonic()-before,3)
        dst=out/"run116_instantmesh_actual_ART_UNAPPROVED.glb"
        copy_as(recon,dst,required_suffix=".glb")
        b=dst.read_bytes()
        if b[:4]!=b"glTF" or struct.unpack_from("<I",b,8)[0]!=len(b):
            raise RuntimeError("Returned file is not valid binary glTF")
        status["actual_glb_sha256"]=sha(dst)
        status["actual_glb_bytes"]=len(b)
        status["stage"]="true GLB validated; native Blender still required"
        status["output"]="TRUE_GLTF_GLb_UNAPPROVED"
    except Exception as exc:
        status["output"]="NO_USABLE_GLTF_MODEL"
        status["error_type"]=type(exc).__name__
        status["error_message"]=str(exc)[:3000]
        (out/"failure_traceback.txt").write_text(traceback.format_exc())
        print("RUN116_ACTUAL_FREE_ROUTE_BLOCKED",type(exc).__name__,str(exc)[:1000],flush=True)
    finally:
        (out/"run116_status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2))
        (out/"ART_REJECTED.flag").write_text(
            "NOT A RELEASE: no full face/side/rear anatomy approval, fine cream down or hollow lip QA; "
            "no physical-phone GPU or full commercial/global rights verification.\n")
        print("RUN116_AUDIT",json.dumps(status,ensure_ascii=False,default=str),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    main(a.source,a.out)
