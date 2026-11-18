#!/usr/bin/env python3
"""Run172: real official TripoSG ZeroGPU image-to-mesh test, never a release.
Only public Gradio API discovered from the official running Space; no token,
payment, CAPTCHA bypass, sample-asset substitution, or retry quota evasion.
"""
import hashlib
import json
import re
import shutil
import traceback
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "research-evidence-run172-TRIPOSG-OFFICIAL-NO_RELEASE"
SOURCE = ROOT / "research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED = "5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
KNOWN = ROOT / "known_rejected_asset_sha256_registry.json"
OUT.mkdir(parents=True, exist_ok=True)
RESULT = {
    "run": 172, "utc_start": datetime.now(timezone.utc).isoformat(),
    "provider": "VAST-AI/TripoSG official public Hugging Face ZeroGPU",
    "provider_url": "https://huggingface.co/spaces/VAST-AI/TripoSG",
    "source_sha256": EXPECTED,
    "providers": {"official_triposg": {"state": "PREFLIGHT"}},
    "new_valid_glb": [], "release": False, "art": "UNREVIEWED",
    "physical_mobile_GPU_tested": False, "payment": 0,
}
P = RESULT["providers"]["official_triposg"]

def persist():
    (OUT / "run172_actual_results.json").write_text(
        json.dumps(RESULT, indent=2, ensure_ascii=False, default=str), encoding="utf-8"
    )

def normalize_files(value):
    found=[]
    if isinstance(value,str):
        path=Path(value)
        if path.is_file(): found.append(path)
    elif isinstance(value,dict):
        for v in value.values(): found += normalize_files(v)
    elif isinstance(value,(list,tuple)):
        for v in value: found += normalize_files(v)
    return found

def validate(path):
    import trimesh
    data=path.read_bytes()
    sha=hashlib.sha256(data).hexdigest()
    rejected=set(re.findall(r"\\b[a-fA-F0-9]{64}\\b",KNOWN.read_text()))
    info={"sha256":sha,"bytes":len(data)}
    if sha in rejected: return {**info,"valid":False,"reason":"known rejected fingerprint"}
    if len(data)<65000 or data[:4]!=b"glTF":
        return {**info,"valid":False,"reason":"missing native substantial binary glTF"}
    try:
        obj=trimesh.load(path,force="scene",process=False)
        triangles=sum(len(m.faces) for m in obj.geometry.values() if hasattr(m,"faces"))
        info.update(triangles=triangles,geometry=len(obj.geometry))
        return {**info,"valid":triangles>=600 and bool(obj.geometry),
                "art":"UNREVIEWED", "mobile_gpu":"NOT_TESTED"}
    except Exception as e:
        return {**info,"valid":False,"reason":"native reimport: "+repr(e)[:400]}

def main():
    assert SOURCE.is_file()
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED
    assert KNOWN.is_file()
    RESULT["source_image_size"]=list(Image.open(SOURCE).size)
    P["state"]="CONNECTING_PUBLIC_SPACE"
    persist()
    from gradio_client import Client, handle_file
    client=Client("VAST-AI/TripoSG",verbose=False)
    P["state"]="DISCOVERING_PUBLIC_API"
    api=client.view_api(return_format="dict")
    (OUT/"official_api_schema.json").write_text(json.dumps(api,indent=2,default=str))
    endpoints=[]
    for e in client.endpoints.values():
        endpoints.append({"api_name":getattr(e,"api_name",None),
                          "fn_index":getattr(e,"fn_index",None),
                          "is_continuous":getattr(e,"is_continuous",None)})
    P["discovered_endpoints"]=endpoints
    persist()

    def pick(needle):
        choices=[x for x in endpoints if x.get("api_name") and needle in str(x["api_name"]).lower()]
        return choices[0]["api_name"] if choices else None

    seg_api=pick("run_segmentation")
    shape_api=pick("image_to_3d")
    if not shape_api:
        P["state"]="NO_PUBLIC_SHAPE_API"
        return

    original_input=str(SOURCE)
    if seg_api:
        P["state"]="PUBLIC_SEGMENTATION_REQUEST"
        persist()
        try:
            seg=client.predict(handle_file(original_input),api_name=seg_api)
            paths=normalize_files(seg)
            if paths:
                im=Image.open(paths[0]).convert("RGBA")
                dest=OUT/"official_foreground_processed.png"
                im.save(dest)
                original_input=str(dest)
                P["segmentation"]="PUBLIC_SEGMENTATION_SUCCESS"
            else:
                P["segmentation"]="NO_DOWNLOADABLE_SEGMENTATION"
        except Exception as e:
            P["segmentation"]="PUBLIC_SEGMENTATION_ERROR"
            P["segmentation_error"]=repr(e)[:900]
            # This original PNG is independently verified and already preprocessed.
    P["state"]="PUBLIC_TRIPOSG_SHAPE_REQUEST"
    persist()
    # Single public inference. Untextured mesh is only a shape candidate; not the final pet.
    result=client.predict(handle_file(original_input),172,36,7.0,True,65000,api_name=shape_api)
    P["returned_value_excerpt"]=str(result)[:600]
    paths=normalize_files(result)
    if not paths:
        P["state"]="NO_NATIVE_MODEL_RESPONSE"
        return
    for i,path in enumerate(paths[:5]):
        if path.suffix.lower() not in (".glb",".gltf"):
            continue
        dest=OUT/f"run172_official_triposg_generated_{i}_UNREVIEWED.glb"
        shutil.copyfile(path,dest)
        check=validate(dest)
        P.setdefault("verified_downloads",[]).append({**check,"input_bound":True})
        if check["valid"]:
            RESULT["new_valid_glb"].append({"file":dest.name,**check,"source_sha256":EXPECTED})
        else:
            dest.unlink(missing_ok=True)
    P["state"]="NATIVE_SOURCE_BOUND_GLB_VALIDATED" if RESULT["new_valid_glb"] else "NO_VALID_NATIVE_GLB"
    persist()

if __name__=="__main__":
    try: main()
    except Exception as e:
        P["state"]="PUBLIC_SPACE_ERROR_OR_QUOTA"
        P["error"]=repr(e)[:1000]
        (OUT/"run172_exception.txt").write_text(traceback.format_exc())
        print("RUN172_PUBLIC_ERROR",repr(e),flush=True)
    finally:
        RESULT["utc_end"]=datetime.now(timezone.utc).isoformat()
        persist()
        print("RUN172_FINAL",P["state"],"FRESH_GLB",len(RESULT["new_valid_glb"]),flush=True)
