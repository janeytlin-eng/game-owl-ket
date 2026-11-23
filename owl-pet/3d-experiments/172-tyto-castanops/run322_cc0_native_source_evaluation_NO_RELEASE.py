#!/usr/bin/env python3
"""Run322 — verify a previously untested primary-source CC0 native GLB.
Research-only; NEVER claim a released juvenile art asset. No paid services.
The source is independent of the rejected SF3D base. No data is sent to outside hosts
except the requested public Innerscene download (no login / captcha bypass).
"""
from __future__ import annotations
import argparse, hashlib, json, struct, time
from pathlib import Path
import requests

SOURCE_PAGE = "https://www.innerscene.com/tools/library/3d-parts/owl-d696472a"
SOURCE_URL = "https://www.innerscene.com/api/library/owl-d696472a/download"
MAX_BYTES = 65 * 1024 * 1024
TARGET = {
    "taxon": "Tyto castanops #172 v3",
    "reference": "rightmost age-unknown cream-mesoptile chick",
    "requirements": [
        "naturally feather-built heart-shaped facial disc",
        "actual cream-white volumetric down",
        "rounded juvenile head-body proportions",
        "credible fully modeled side/rear shoulders and tucked short wings",
        "correct support/contact of feet with old eucalyptus hollow",
        "real mobile WebGL, material/rights checks",
    ],
}
def sha(b:bytes)->str: return hashlib.sha256(b).hexdigest()
def save_json(p:Path,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding="utf-8")
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out", default="owl172-run322-evidence")
    a=ap.parse_args()
    out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
    report={
      "run":"322", "source_page":SOURCE_PAGE,"source_download":SOURCE_URL,
      "source_claim":"Site labels this native 3D Owl GLB 19.7MB as original CC0",
      "source_rights_state":"Unverified for all downstream rights until source provenance reviewed",
      "expected_target":TARGET,"paid_usd":0,
      "art_verdict":"NOT_APPROVED_NO_RELEASE","physical_phone":"UNTESTED",
      "status":"NOT_ATTEMPTED", "steps":[],
    }
    p=out/"innscene_owl_CC0_UNREVIEWED_NO_RELEASE.glb"
    start=time.monotonic()
    try:
        with requests.get(SOURCE_URL,timeout=(15,110),stream=True,
              headers={"User-Agent":"owl-pet-3d-independent-research/322"}) as resp:
            report["http_status"]=resp.status_code
            report["http_content_type"]=resp.headers.get("Content-Type","")
            report["http_final_url"]=resp.url
            report["steps"].append(f"GET public documented download -> HTTP {resp.status_code}")
            resp.raise_for_status()
            raw=bytearray()
            for b in resp.iter_content(1024*1024):
                if not b:continue
                raw.extend(b)
                if len(raw)>MAX_BYTES:raise RuntimeError("Source exceeds size budget")
        if len(raw)<1000 or raw[:4]!=b"glTF":
            raise RuntimeError("Downloaded response is not GLB; no binary asset accepted")
        version,declared=struct.unpack_from("<II",raw,4)
        if version!=2 or declared!=len(raw):
            raise RuntimeError(f"Invalid GLB header/version/length: {version},{declared},{len(raw)}")
        p.write_bytes(raw)
        report.update({"source_bytes":len(raw),"source_sha256":sha(raw),
                       "glb_version":version,"status":"NATIVE_GLB_DOWNLOADED"})
        report["steps"].append("Native glTF binary header and exact length verified")
        import numpy as np
        import trimesh
        scene=trimesh.load(p,force="scene",process=False)
        total_tri=0;uv=0;geo=[]
        for name,m in scene.geometry.items():
            triangles=len(m.faces);total_tri+=triangles
            has_uv=bool(getattr(m.visual,"uv",None) is not None)
            uv+=int(has_uv)
            geo.append({"name":name,"vertices":len(m.vertices),
                        "triangles":triangles,"uv":has_uv,
                        "material_type":type(getattr(m.visual,"material",None)).__name__})
        if total_tri<1000:raise RuntimeError("Insufficient actual 3D triangle count")
        box=scene.bounds
        if box is None:raise RuntimeError("Empty scene bounds")
        ext=(box[1]-box[0]).tolist()
        report.update({"status":"NATIVE_GLB_MESH_VERIFIED",
          "geometry_count":len(geo),"total_triangles":total_tri,
          "uv_geometry_count":uv,"bounds_m":np.asarray(box).tolist(),
          "extents_m":ext,"geometry":geo[:20]})
        report["steps"].append("Trimesh native 3D scene parsed independently; not SVG, photo or geometry stub")
    except Exception as exc:
        report["error"]=type(exc).__name__+": "+str(exc)[:900]
        report["status"]="DOWNLOAD_OR_PARSE_BLOCKED"
        report["steps"].append("Failure recorded without invented asset")
        if p.exists() and (p.stat().st_size<1000 or p.read_bytes()[:4]!=b"glTF"):p.unlink()
    report["elapsed_seconds"]=round(time.monotonic()-start,2)
    save_json(out/"run322-native-diagnostics.json",report)
    (out/"STRICT_NO_RELEASE.txt").write_text(
       "Run322 is RESEARCH ONLY: no art approval; no phone pass; no product release; no main/251 production edits.\n",encoding="utf8")
    print(json.dumps(report,indent=2,ensure_ascii=False))
if __name__=="__main__":main()
