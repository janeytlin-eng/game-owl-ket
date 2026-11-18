#!/usr/bin/env python3
"""Run180: a *fresh*, no-fee image-conditioned 3D from color-normalized original #172
rightmost v3 crop. NOT cosmetic editing of art-rejected GLB. NO_RELEASE until
real multiperspective art and physical phone WebGL pass."""
import hashlib,json,os,re,subprocess,time,traceback
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urlparse
import requests
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/"research-evidence-run180-CLEAN-BG-NEW-NEURAL-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)
SRC=ROOT/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
SHA="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
REJ=ROOT/"known_rejected_asset_sha256_registry.json"
BRANCH="research/owl172-run180-clean-background-neural-rebuild"
REPO="janeytlin-eng/game-owl-ket"
MCP="https://three.ws/api/mcp-studio"
CLEAN=OUT/"run180_rightmost_contiguous_background_replaced.png"
URL=f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run180-CLEAN-BG-NEW-NEURAL-NO_RELEASE/{CLEAN.name}"
PROMPT=("Generate one physically continuous, round, very young Tasmanian masked owl from this "
"actual source reference, using only the bird. It is a cream-white, thick, softly fluffy "
"age-unknown second-down chick (mesoptile). Plump round body, short down-buried wings and "
"tail concealed completely; naturally integrated broad heart facial disc, two wide open dark "
"eyes, tiny ivory bill. Fully formed closed 3D underside, short tucked clawed feet supported "
"on an old eucalyptus cavity lip. Smooth organic full-volume anatomy from back and sides, "
"fine soft white fibre texture. Absolutely NO layered stiff adult wing feathers, scales, "
"crust, disconnected parts, long tail, bulbous protruding eyes or 2D cutout.")
STATE={"run":179,"started":datetime.now(timezone.utc).isoformat(),"source_crop_sha256":SHA,
       "source":"original accepted #172 v3 rightmost image crop, only exterior black-background flood fill",
       "provider":MCP,"tool":"mesh_forge","status":"PRECHECK","new_glb_count":0,
       "release":False,"art":"UNREVIEWED","physical_phone_webgl":"NOT_TESTED",
       "extra_fees_usd":0}
def sha(b):return hashlib.sha256(b).hexdigest()
def save():(OUT/"run180_results.json").write_text(json.dumps(STATE,indent=2,ensure_ascii=False))
def rpc(s,method,params=None,n=1,label=None):
    payload={"jsonrpc":"2.0","id":n,"method":method}
    if params is not None:payload["params"]=params
    r=s.post(MCP,json=payload,timeout=(25,110),headers={
      "Accept":"application/json","Content-Type":"application/json",
      "MCP-Protocol-Version":"2025-06-18"})
    record={"http":r.status_code,"content_type":r.headers.get("content-type",""),
            "response":r.text[:200000]}
    (OUT/f"mcp_{label or method.replace('/','_')}.json").write_text(json.dumps(record,indent=2,ensure_ascii=False))
    if r.status_code!=200:raise RuntimeError("MCP_HTTP_"+str(r.status_code))
    if "json" not in r.headers.get("content-type","").lower():raise RuntimeError("MCP_NOT_JSON")
    z=r.json()
    if "error" in z:raise RuntimeError("MCP_RPC_ERROR_"+str(z["error"])[:600])
    return z.get("result",{})
def structured(result):
    s=result.get("structuredContent") or {}
    if isinstance(s,dict) and s:return s
    for item in result.get("content",[]):
        if item.get("type")=="text":
            try:
                a=json.loads(item.get("text",""))
                if isinstance(a,dict):return a
            except ValueError:pass
    return {}
def prep():
    assert SRC.is_file() and sha(SRC.read_bytes())==SHA,"REFERENCE_SHA_MISMATCH"
    assert REJ.is_file()
    for name in ("owl-pet/AGENTS.md","owl-pet/README.md",
                 "owl-pet/prototype/index.html",
                 "owl-pet/research/species/172-tyto-castanops-v3.md"):
        assert (ROOT.parents[2]/name).is_file(),name
    im=Image.open(SRC).convert("RGB")
    assert im.size==(512,512),im.size
    # Flood-fill only exterior CONNECTED black background; do not change eyes,
    # small dark facial marks or interior bird pixels.
    original=im.copy()
    # (440,130) is INSIDE the black rectangle, unlike Run179 (510,255),
    # which was in the already-offwhite margin and did not fix the image.
    corner=(440,130)
    before=original.getpixel(corner)
    assert max(before)<70,("BLACK_BACKGROUND_SEED_NOT_DARK",before)
    ImageDraw.floodfill(im,corner,(236,233,227),thresh=26)
    # A second seed is only used if this point remains black; no interior detail altered.
    if max(im.getpixel((440,360)))<70:
        ImageDraw.floodfill(im,(440,360),(236,233,227),thresh=26)
    after=im.getpixel(corner)
    assert min(after)>190,("BLACK_BACKGROUND_STILL_PRESENT",after)
    original_data=list(original.getdata())
    new_data=list(im.getdata())
    changed=sum(a!=b for a,b in zip(original_data,new_data))
    STATE["color_cleanup"]={"seed":corner,"seed_before":before,
       "seed_after":after,"changed_pixels":changed,
       "changed_fraction":round(changed/(512*512),5)}
    assert changed>12000,("NO_MEANINGFUL_BACKGROUND_REMOVAL",changed)
    im.save(CLEAN,optimize=True)
    STATE["clean_source_sha256"]=sha(CLEAN.read_bytes())
    STATE["clean_source_size"]=CLEAN.stat().st_size
    STATE["clean_source_differs_from_original"]=STATE["clean_source_sha256"]!=SHA
    assert STATE["clean_source_differs_from_original"]
    save()
    # Publish only the altered 2D reference in isolated research branch so that
    # the free image-to-3D service can fetch the verified exact new bytes.
    subprocess.run(["git","config","user.name","github-actions[bot]"],check=True)
    subprocess.run(["git","config","user.email","41898282+github-actions[bot]@users.noreply.github.com"],check=True)
    subprocess.run(["git","add","--sparse",str(CLEAN)],check=True)
    subprocess.run(["git","commit","-m","research(owl172): stage genuine cleaned original 2D source for free new image-3D inference"],check=True)
    subprocess.run(["git","push","origin","HEAD:"+BRANCH],check=True)
    ses=requests.Session()
    for attempt in range(8):
        try:
            r=ses.get(URL+"?v="+STATE["clean_source_sha256"][:12],timeout=(10,35))
            STATE["remote_reference_http"]=r.status_code
            STATE["remote_reference_sha256"]=sha(r.content) if r.ok else None
            if r.ok and sha(r.content)==STATE["clean_source_sha256"]:
                STATE["remote_reference_verified"]=True
                save()
                return ses
        except requests.RequestException as e:
            STATE["remote_fetch_last_error"]=repr(e)
        time.sleep(4)
    raise RuntimeError("NEW_REFERENCE_PUBLIC_REMOTE_HASH_NOT_VERIFIED")
def get_glb(s,record):
    z=structured(record)
    glb=z.get("glbUrl") or z.get("glb_url")
    if not glb:
        STATE["status"]="NO_NATIVE_GLB"
        STATE["last_response_status"]=z.get("status")
        return False
    domain=urlparse(glb).hostname or ""
    assert urlparse(glb).scheme=="https" and (domain=="three.ws" or domain.endswith(".three.ws") or domain.endswith(".r2.dev"))
    response=s.get(glb,timeout=(15,160),stream=True)
    STATE["glb_download_http"]=response.status_code
    if not response.ok:raise RuntimeError("GLB_DOWNLOAD_HTTP_"+str(response.status_code))
    b=bytearray()
    for block in response.iter_content(1<<20):
        b+=block
        if len(b)>32<<20:raise RuntimeError("GLB_EXCEEDS_32MB")
    data=bytes(b)
    digest=sha(data)
    STATE["candidate"]={"sha256":digest,"bytes":len(data),"original_url":glb}
    if len(data)<65000 or data[:4]!=b"glTF":raise RuntimeError("NOT_REAL_GLB")
    if digest in set(re.findall(r"\b[a-f0-9]{64}\b",REJ.read_text())):
        STATE["status"]="DUPLICATE_ALREADY_REJECTED_GLB"
        return False
    filename=OUT/"run180_new_image_conditioned_UNREVIEWED.glb"
    filename.write_bytes(data)
    import trimesh
    obj=trimesh.load(str(filename),force="scene",process=False)
    triangles=sum(len(g.faces) for g in obj.geometry.values() if hasattr(g,"faces"))
    STATE["candidate"]["mesh_count"]=len(obj.geometry)
    STATE["candidate"]["triangles"]=triangles
    assert triangles>3000,"TOO_SIMPLE"
    STATE["new_glb_count"]=1
    STATE["status"]="NEW_NATIVE_GLB_ART_UNREVIEWED"
    save()
    # Free read-only model inspector, never treat it as art approval.
    try:
        inspection=rpc(s,"tools/call",{"name":"look_at_model","arguments":{
           "glb_url":glb,"views":["front","three-quarter","side","back","bottom"],"size":512
        }},n=60,label="look_at_actual_new_glb")
        info=structured(inspection)
        STATE["look_at_model_keys"]=list(info.keys())
        STATE["look_at_model_is_error"]=inspection.get("isError")
        save()
    except Exception as e:
        STATE["look_at_model_error"]=repr(e)
        save()
    return True
def main():
    s=prep()
    listing=rpc(s,"tools/list",n=1,label="live_tools_list")
    names={k.get("name") for k in listing.get("tools",[])}
    if not {"mesh_forge","get_job"}.issubset(names):
        STATE["status"]="MCP_TOOL_UNAVAILABLE";return
    STATE["source_verified_and_tools_present"]=True;save()
    key="owl172-run180-refill-black-background-20261118-v1"
    output=rpc(s,"tools/call",{"name":"mesh_forge","arguments":{
        "image_url":URL+"?v="+STATE["clean_source_sha256"][:12],
        "prompt":PROMPT,"idempotency_key":key
    }},n=10,label="new_clean_background_image_to_3d")
    sdata=structured(output)
    STATE["initial_response_keys"]=list(sdata.keys())
    STATE["initial_job_status"]=sdata.get("status")
    STATE["idempotency_key"]=key;save()
    if sdata.get("glbUrl") or sdata.get("glb_url"):
        get_glb(s,output);return
    job=sdata.get("jobId") or sdata.get("job_id")
    if not job or output.get("isError"):
        STATE["status"]="MCP_NO_VALID_JOB";return
    STATE["new_image_conditioned_job_receipt"]=job;save()
    for i in range(15):
        time.sleep(12 if i==0 else 17)
        r=rpc(s,"tools/call",{"name":"get_job","arguments":{"job_id":job}},
              n=20+i,label=f"get_job_{i+1}")
        data=structured(r)
        STATE["polls"]=i+1
        STATE["poll_status"]=data.get("status")
        STATE["poll_phase"]=data.get("phase")
        save()
        if data.get("glbUrl") or data.get("glb_url"):
            get_glb(s,r);return
        if data.get("status") in ("failed","error","cancelled") and not data.get("retryable",False):
            STATE["status"]="UPSTREAM_"+str(data.get("status"))
            STATE["upstream_error"]=str(data.get("message") or data.get("reason"))[:700]
            return
    STATE["status"]="JOB_STILL_PENDING_AFTER_BOUNDED_POLL"
if __name__=="__main__":
    try:main()
    except Exception as e:
        STATE["status"]="EXPERIMENT_ERROR"
        STATE["exception"]=repr(e)
        (OUT/"exception_traceback.txt").write_text(traceback.format_exc())
    finally:
        STATE["finished"]=datetime.now(timezone.utc).isoformat()
        save()
        (OUT/"NO_RELEASE.flag").write_text("NO_RELEASE: new model, if any, requires independent true front/side/back art review AND actual mobile GPU acceptance; no paid usage.\n")
        manifest={p.name:{"bytes":p.stat().st_size,"sha256":sha(p.read_bytes())}
            for p in OUT.iterdir() if p.is_file() and p.name!="sha256_manifest.json"}
        (OUT/"sha256_manifest.json").write_text(json.dumps(manifest,indent=2))
        assert all(sha((OUT/k).read_bytes())==v["sha256"] for k,v in manifest.items())
        print("RUN180_FINAL",STATE["status"],"NEW_GLB",STATE["new_glb_count"],"ITEMS",len(manifest),flush=True)
