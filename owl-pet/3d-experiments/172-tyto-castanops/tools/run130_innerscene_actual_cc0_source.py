#!/usr/bin/env python3
"""Run130: acquire genuine publicly offered CC0 owl GLB for independent *art* QA.
Do not release any source or unreviewed output. No authentication or paid access.
"""
import datetime, hashlib, json, struct, sys, urllib.request, urllib.error
from pathlib import Path
from urllib.parse import urlparse
OUT=Path(sys.argv[1]); OUT.mkdir(parents=True,exist_ok=True)
PAGE="https://www.innerscene.com/tools/library/3d-parts/owl-d696472a"
TERMS="https://www.innerscene.com/tools/library/terms"
DOWNLOAD="https://www.innerscene.com/api/library/owl-d696472a/download"
MAX=36*1024*1024
report={"run":130,"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "origin":"Innerscene Free Parts Library / publisher-declared CC0",
        "source_landing":PAGE,"license_terms":TERMS,"official_download":DOWNLOAD,
        "subject":"#172 Tyto castanops v3 right cream age-unknown mesoptile",
        "source":{},"release":"NO_RELEASE","art_gate":"ART_UNREVIEWED",
        "additional_cost_usd":0,
        "disclaimer":"Publisher CC0 assertion is not proof of upstream IP or species / age. No automatic art approval."}
def read(url,cap):
    req=urllib.request.Request(url,headers={"User-Agent":"owl172-free-source-visual-quality-research/1.0"})
    try:
        with urllib.request.urlopen(req,timeout=60) as r:
            data=r.read(cap+1)
            return {"status":r.status,"final_url":r.geturl(),
                    "content_type":r.headers.get("Content-Type",""),
                    "bytes_read":len(data),"truncated":len(data)>cap},data[:cap]
    except urllib.error.HTTPError as e:
        return {"status":e.code,"error":str(e)[:250]},b""
    except Exception as e:
        return {"error":type(e).__name__+": "+str(e)[:250]},b""
def glb_info(data):
    result={"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
    if len(data)<20 or data[:4]!=b"glTF":
        result["valid_glb"]=False;return result
    _,ver,declared=struct.unpack_from("<4sII",data,0)
    length,typ=struct.unpack_from("<I4s",data,12)
    result.update(version=ver,declared_length=declared,json_chunk_length=length)
    result["valid_glb"]=ver==2 and declared==len(data) and typ==b"JSON" and length<=len(data)-20
    if not result["valid_glb"]:return result
    js=json.loads(data[20:20+length])
    result["generator"]=js.get("asset",{}).get("generator")
    result["mesh_names"]=[x.get("name","") for x in js.get("meshes",[])]
    result["mesh_count"]=len(js.get("meshes",[]))
    result["skins"]=len(js.get("skins",[]))
    result["materials"]=len(js.get("materials",[]))
    result["images"]=len(js.get("images",[]))
    result["animations"]=len(js.get("animations",[]))
    acc=js.get("accessors",[])
    tris=0
    for mesh in js.get("meshes",[]):
        for p in mesh.get("primitives",[]):
            idx=p.get("indices",p.get("attributes",{}).get("POSITION",-1))
            count=acc[idx].get("count",0) if 0<=idx<len(acc) else 0
            mode=p.get("mode",4)
            tris+=count//3 if mode==4 else (max(0,count-2) if mode in (5,6) else 0)
    result["triangles_all_meshes"]=tris
    result["extensions_used"]=js.get("extensionsUsed",[])
    return result
for key,url in [("landing",PAGE),("terms",TERMS)]:
    meta,raw=read(url,2*1024*1024)
    text=raw.decode("utf8","replace")
    meta["sha256"]=hashlib.sha256(raw).hexdigest()
    meta["cc0_marked"]="CC0" in text
    meta["original_source_claim"]="Innerscene - original model" in text if key=="landing" else None
    meta["snippet"]=text[:300].replace("\n"," ")
    report["source"][key]=meta
meta,raw=read(DOWNLOAD,MAX)
report["source"]["download"]=meta
if raw and not meta.get("truncated"):
    detail=glb_info(raw)
    report["glb"]=detail
    if detail["valid_glb"]:
        path=OUT/"run130_Innerscene_CC0_owl_SOURCE_ONLY.glb"
        path.write_bytes(raw)
        report["temporary_binary"]=path.name
else:
    report["glb"]={"valid_glb":False,"reason":"not retrieved or max size exceeded"}
(OUT/"run130_public_asset_probe.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
(OUT/"NO_RELEASE.flag").write_text("NO_RELEASE — not an approved juvenile Tyto castanops. Requires native four-view art review, rights verification and real-phone WebGL.\n")
print(json.dumps({"landing":report["source"]["landing"].get("status"),
                  "terms":report["source"]["terms"].get("status"),
                  "download":report["source"]["download"].get("status"),
                  "glb":report["glb"],"release":"NO_RELEASE"},ensure_ascii=False))
