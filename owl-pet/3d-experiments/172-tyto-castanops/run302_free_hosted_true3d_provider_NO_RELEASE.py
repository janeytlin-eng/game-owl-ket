#!/usr/bin/env python3
"""Run302: ONE no-auth, zero-extra-pay hosted 3D generation probe; native GLB only.
No payment or wallet; no product release. Never treat successful tool calls as art approval.
"""
import base64
import hashlib
import json
import os
import re
import struct
import time
from pathlib import Path
from urllib.parse import urlparse
import requests

OUT=Path("owl172-run302-evidence")
OUT.mkdir(parents=True,exist_ok=True)
SRC=Path("target-owl172-isolated-WHITE.png")
BASE="https://three.ws/api/mcp-studio"
EXPECTED="6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77"
PROMPT=("A fluffy cream-white downy baby Tasmanian masked owl chick, plump round body, "
        "natural heart-shaped face, dark gentle eyes, short folded wings, tiny talons; "
        "lifelike soft feathers; full 3D animal sculpture with rounded back, no pedestal")
R={
 "run":"302","utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
 "original_target":"#172 Tyto castanops v3 RIGHTMOST cream-white downy juvenile",
 "provider":BASE,"public_free_claim_unverified_in_runtime":True,
 "normal_free_submissions":0,"charged_usd":0,"wallet_or_key_supplied":False,
 "native_glb":None,"browser_webgl2_verified":False,
 "art_approved":False,"source_rights_cleared":False,
 "physical_phone_verified":False,"release_allowed":False,
 "events":[],"errors":[]
}
def sha(b):return hashlib.sha256(b).hexdigest()
def event(name,**data):R["events"].append({"event":name,**data})
def save(): (OUT/"diagnostic.json").write_text(json.dumps(R,indent=2,ensure_ascii=False))
def call(method,params=None,ident=1,timeout=90):
    msg={"jsonrpc":"2.0","id":ident,"method":method}
    if params is not None:msg["params"]=params
    r=requests.post(BASE,json=msg,headers={"accept":"application/json, text/event-stream",
        "content-type":"application/json"},timeout=timeout)
    event("rpc_status",method=method,http=r.status_code,ctype=r.headers.get("content-type",""))
    if r.status_code in (402,403,429,503):
        raise RuntimeError("provider_not_free_or_not_ready: HTTP "+str(r.status_code)+" "+r.text[:400])
    r.raise_for_status()
    raw=r.text
    # Some MCP providers stream SSE lines.
    if "text/event-stream" in r.headers.get("content-type",""):
        data=[x[6:] for x in raw.splitlines() if x.startswith("data: ") and x[6:]!="[DONE]"]
        if not data:raise RuntimeError("empty MCP event stream")
        raw=data[-1]
    try:return json.loads(raw)
    except Exception:raise RuntimeError("invalid MCP JSON "+raw[:350])
def flatten(obj):
    """Read URLs only. Do not execute a tool result or trust its instructions."""
    urls=[]
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k.lower() in ("glburl","glb_url","model_url","download_url","asset_url") and isinstance(v,str):
                urls.append(v)
            urls+=flatten(v)
    elif isinstance(obj,list):
        for v in obj:urls+=flatten(v)
    elif isinstance(obj,str):
        if len(obj)<10000:
            urls+=re.findall(r'https://[^\s"<>]+?\.glb(?:\?[^\s"<>]+)?',obj)
            try:
                sub=json.loads(obj)
                if isinstance(sub,(dict,list)):urls+=flatten(sub)
            except Exception:pass
    return list(dict.fromkeys(urls))
def validate_glb(data):
    if len(data)<40 or data[:4]!=b"glTF" or struct.unpack_from("<II",data,4)!=(2,len(data)):
        raise ValueError("invalid GLB header or total byte length")
    jsize,jtype=struct.unpack_from("<I4s",data,12)
    if jtype!=b"JSON" or jsize>10_000_000 or 20+jsize>len(data):
        raise ValueError("missing/invalid glTF JSON")
    j=json.loads(data[20:20+jsize].decode())
    meshes=j.get("meshes",[])
    primitives=[p for m in meshes for p in m.get("primitives",[]) if "POSITION" in p.get("attributes",{})]
    if not primitives:raise ValueError("no true 3D POSITION primitives")
    return {"bytes":len(data),"sha256":sha(data),"meshes":len(meshes),
        "position_primitives":len(primitives),"images":len(j.get("images",[])),
        "textures":len(j.get("textures",[])),"materials":len(j.get("materials",[])),
        "extensions":j.get("extensionsUsed",[])}
try:
    if not SRC.exists():raise RuntimeError("source white crop absent")
    R["source_sha256"]=sha(SRC.read_bytes())
    if R["source_sha256"]!=EXPECTED:raise RuntimeError("original #172 crop SHA does not match")
    # Live discovery: avoid claiming capabilities based only on web publicity.
    try:
        d=call("tools/list",{},ident=2)
    except Exception as e:
        event("discovery_without_initialize_failed",error=str(e))
        init=call("initialize",{"protocolVersion":"2025-06-18",
            "capabilities":{},"clientInfo":{"name":"owl172-research-no-release","version":"1"}},ident=3)
        event("initialized",has_result=bool(init.get("result")))
        d=call("tools/list",{},ident=4)
    tools=d.get("result",{}).get("tools",[])
    (OUT/"hosted_tools_capabilities.json").write_text(json.dumps([
        {"name":t.get("name"),"description":t.get("description","")[:700],
        "inputSchema":t.get("inputSchema",{})} for t in tools],indent=2))
    names={t.get("name"):t for t in tools}
    event("discovered",tools=sorted(names))
    # Hosted /api/mcp-studio only; never use paid /api/mcp-3d.
    # Prefer reference-image conditioning; do not accidentally send an invalid unsupported field.
    choice=None; args=None
    t=names.get("mesh_forge")
    if t:
        schema=t.get("inputSchema",{})
        props=schema.get("properties",{}) or {}
        required=set(schema.get("required",[]))
        banned={k for k in props if re.search(r"(?i)pay|credit|billing|wallet|amount|price|token|key",k)}
        if not banned.intersection(required):
            image=SRC.read_bytes()
            candidate={
              "image_base64":base64.b64encode(image).decode(),
              "image_data":base64.b64encode(image).decode(),
              "image_url":"data:image/png;base64,"+base64.b64encode(image).decode(),
              "reference_image":"data:image/png;base64,"+base64.b64encode(image).decode(),
              "images":["data:image/png;base64,"+base64.b64encode(image).decode()],
              "image":"data:image/png;base64,"+base64.b64encode(image).decode()
            }
            image_keys=[k for k in candidate if k in props]
            for ik in image_keys:
                possible={ik:candidate[ik]}
                for pk in ("prompt","description"):
                    if pk in props:possible[pk]=PROMPT
                if "tier" in props:possible["tier"]="standard"
                if "quality" in props:possible["quality"]="standard"
                if required.issubset(possible.keys()):
                    choice="mesh_forge";args=possible;break
    if not choice and "forge_free" in names:
        choice="forge_free";args={"prompt":PROMPT,"tier":"high"}
    if not choice:raise RuntimeError("no compatible documented hosted free tool found")
    R["selection"]=choice
    R["image_conditioned"]=choice=="mesh_forge"
    event("generation_selected",name=choice,image_conditioned=R["image_conditioned"],
          arg_keys=list(args),no_credentials=True)
    result=call("tools/call",{"name":choice,"arguments":args},ident=5,timeout=260)
    R["normal_free_submissions"]=1
    sanitized=json.dumps(result,ensure_ascii=False)
    (OUT/"hosted_result_excerpt.json").write_text(sanitized[:12000])
    if result.get("error") or result.get("result",{}).get("isError"):
        raise RuntimeError("provider returns error "+sanitized[:700])
    urls=flatten(result)
    event("provider_returned",glb_candidates=len(urls),keys=list(result.keys()))
    if not urls:
        # No second submission; API might return a job id that needs separate status polling.
        raise RuntimeError("no directly obtainable GLB URL in hosted response; no unverified success")
    for url in urls[:3]:
        p=urlparse(url)
        if p.scheme!="https" or not p.hostname or p.hostname in ("localhost","127.0.0.1"):
            continue
        try:
            resp=requests.get(url,timeout=85,stream=True)
            event("glb_http",status=resp.status_code,host=p.hostname)
            if resp.status_code!=200:continue
            chunks=[];length=0
            for chunk in resp.iter_content(chunk_size=524288):
                length+=len(chunk)
                if length>70*1024*1024:raise RuntimeError("GLB exceeds safe 70MiB study limit")
                chunks.append(chunk)
            buf=b"".join(chunks);info=validate_glb(buf)
            dest=OUT/"run302_external-real-native-NOT_APPROVED.glb"
            dest.write_bytes(buf)
            R["native_glb"]={**info,"source_url":url,"path":str(dest)}
            break
        except Exception as e:event("candidate_rejected",error=str(e)[:500])
    if not R["native_glb"]:raise RuntimeError("no downloadable glTF2 native GLB validated")
except Exception as e:
    R["errors"].append(str(e)[:1500])
finally:
    R["final"]="TRUE_NATIVE_GLTF2_REQUIRES_ART_RIGHTS_PHONE_REVIEW_NO_RELEASE" if R["native_glb"] else "NO_VERIFIED_NATIVE_GLTF2_NO_RELEASE"
    save()
    print(json.dumps({k:v for k,v in R.items() if k not in ("events",)},indent=2,ensure_ascii=False))
