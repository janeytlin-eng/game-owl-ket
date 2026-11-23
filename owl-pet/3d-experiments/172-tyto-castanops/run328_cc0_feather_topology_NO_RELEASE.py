#!/usr/bin/env python3
"""Run328: independently obtain and inspect an AI-assisted CC0 3D adult-owl anatomy donor.
NOT a Tyto castanops mesoptile. No credentials/paid services. No product release.
"""
import argparse
import hashlib
import json
import struct
import time
from pathlib import Path
from urllib.parse import urlparse
import requests

BASE="https://grab3d.com/dl/owl/"
SOURCE=BASE+"owl-light.glb"
LICENSE_URL=BASE+"LICENSE.txt"
MANIFEST_URL=BASE+"manifest.json"
CAP=45*1024*1024

def sha(data):return hashlib.sha256(data).hexdigest()
def write(path, data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf8")

def get(session,url,max_bytes,timeout=(15,100)):
    with session.get(url,timeout=timeout,stream=True,allow_redirects=True) as response:
        status=response.status_code
        ct=response.headers.get("Content-Type","")
        chunks=bytearray()
        if status==200:
            for block in response.iter_content(chunk_size=1<<20):
                if block:
                    chunks.extend(block)
                    if len(chunks)>max_bytes:raise ValueError("Source response exceeds resource cap")
        return {"status":status,"content_type":ct,"final_url":response.url},bytes(chunks)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",default="owl172-run328-evidence")
    args=ap.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic()
    report={"run":"328","asset":"Grab3D CC0 great horned owl LIGHT GLB, AI-assisted",
      "requested_url":SOURCE,"target":"#172 Tyto castanops v3 RIGHTMOST cream-down age-unknown mesoptile",
      "source_taxon_mismatch":"Bubo virginianus-like adult great horned owl with ear tufts; NEVER target",
      "free_only":True,"money_spent_usd":0,"model_verified":False,
      "webgl2_pass":False,"physical_phone":"UNTESTED","art_approved":False,
      "rights_approved_for_product":False,"release":False,"result":"SOURCE_NOT_TESTED"}
    session=requests.Session()
    session.headers.update({"User-Agent":"Owl172Research328/1.0 (independent CC0 geometry test)"})
    try:
        lm,lic=get(session,LICENSE_URL,250000)
        mm,manifest_bytes=get(session,MANIFEST_URL,250000)
        report["license_get"]=lm
        report["manifest_get"]=mm
        if lm["status"]!=200 or mm["status"]!=200:
            raise RuntimeError("Publisher license/manifest not publicly available; fail closed")
        (out/"publisher-LICENSE.txt").write_bytes(lic)
        (out/"publisher-manifest.json").write_bytes(manifest_bytes)
        manifest=json.loads(manifest_bytes)
        report["publisher_license"] = manifest.get("extras",{}).get("license")
        report["publisher_origin"]=manifest.get("origin")
        if manifest.get("extras",{}).get("license")!="CC0-1.0":
            raise RuntimeError("Publisher manifest does not declare CC0-1.0")
        expected=manifest["files"]["glb_light"]["bytes"]
        meta,body=get(session,SOURCE,CAP,timeout=(20,150))
        report["download_http"]=meta
        report["source_received_bytes"]=len(body)
        report["source_sha256"]=sha(body)
        if meta["status"]!=200:raise RuntimeError("Native GLB HTTP "+str(meta["status"]))
        if len(body)!=expected:raise RuntimeError(f"GLB bytes {len(body)} differ from publisher manifest {expected}")
        if body[:4]!=b"glTF" or len(body)<120:raise RuntimeError("Not a real glTF binary")
        version,declared=struct.unpack_from("<II",body,4)
        if version!=2 or declared!=len(body):raise RuntimeError("Invalid GLB version or declared length")
        glen,gtype=struct.unpack_from("<II",body,12)
        if gtype!=0x4e4f534a:raise RuntimeError("GLB first chunk not JSON")
        header=json.loads(body[20:20+glen].decode("utf8"))
        report["glb_json_summary"]={
            "meshes":len(header.get("meshes",[])),
            "nodes":len(header.get("nodes",[])),
            "materials":len(header.get("materials",[])),
            "textures":len(header.get("textures",[])),
            "images":len(header.get("images",[])),
            "accessors":len(header.get("accessors",[])),
            "extensionsUsed":header.get("extensionsUsed",[])}
        model_path=out/"adult-great-horned-owl-light-CC0-SOURCE_ONLY-NO_RELEASE.glb"
        model_path.write_bytes(body)
        import numpy as np
        import trimesh
        scene=trimesh.load(model_path,force="scene",process=False)
        geo=[]
        for name,m in scene.geometry.items():
            if not isinstance(m,trimesh.Trimesh):continue
            uv=getattr(m.visual,"uv",None)
            geo.append({"name":name,"vertices":int(len(m.vertices)),"triangles":int(len(m.faces)),
               "uv":bool(uv is not None),
               "material_type":type(getattr(m.visual,"material",None)).__name__,
               "bounds":np.asarray(m.bounds).tolist()})
        triangles=sum(d["triangles"] for d in geo)
        if triangles<1000 or not geo:raise RuntimeError("Native GLB lacks sufficient real triangle geometry")
        report["mesh_geometry"]={"geometry_count":len(geo),"total_triangles":triangles,
          "uv_geometry_count":sum(int(m["uv"]) for m in geo),
          "scene_bounds":np.asarray(scene.bounds).tolist(),"geometry":geo[:16]}
        report["model_verified"]=True
        report["result"]="ADULT_NATIVE_GLB_VERIFIED_ART_NOT_APPROVED"
        report["independent_mesh_conclusion"]="Real textured native triangle mesh; no assertion of individually sculpted feathers or chick suitability; must inspect all views. High triangle count alone does not establish down."
    except Exception as e:
        report["error"]=type(e).__name__+": "+str(e)[:1200]
        report["result"]="SOURCE_DOWNLOAD_OR_PARSE_BLOCKED"
    finally:
        report["elapsed_seconds"]=round(time.monotonic()-start,2)
        write(out/"run328-native-diagnostic.json",report)
        (out/"STRICT_NO_RELEASE.txt").write_text(
            "CC0 adult great-horned owl is NOT the #172 cream-down Tyto castanops baby. "
            "This is research only: no juvenile art pass, no physical phone, no product rights approval, NO_RELEASE.\n",encoding="utf8")
        print(json.dumps(report,indent=2,ensure_ascii=False))
if __name__=="__main__":
    main()
