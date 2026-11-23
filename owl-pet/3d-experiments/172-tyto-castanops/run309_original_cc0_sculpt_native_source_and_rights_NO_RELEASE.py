#!/usr/bin/env python3
"""Run309. Original-publisher CC0-labelled owl sculpt candidate; strict quarantine.
Actually fetch native GLB using publicly documented no-auth download; never claim target juvenile.
"""
import hashlib
import json
import os
import struct
from pathlib import Path
from urllib.parse import urlparse
import requests
import numpy as np
import trimesh

OUT=Path("owl172-run309-evidence")
OUT.mkdir(exist_ok=True)
SOURCE_PAGE="https://www.innerscene.com/tools/library/3d-parts/owl-d696472a"
DOWNLOAD="https://www.innerscene.com/api/library/owl-d696472a/download"
GLB=OUT/"inn erscene-owl-ORIGINAL_CC0_CLAIM_NON_JUVENILE.glb".replace(" ","")
result={"run":309,"source_page":SOURCE_PAGE,"download_url":DOWNLOAD,"native_glb_acquired":False,
        "actual_target_chick":False,"art_accepted":False,"license":"CC0 per publisher webpage only",
        "license_chain_independently_cleared":False,"spending_usd":0,"release_allowed":False}
try:
    page=requests.get(SOURCE_PAGE,timeout=(15,45),headers={"User-Agent":"Mozilla/5.0 owl172 research QA"})
    html=page.text[:250000]
    (OUT/"publisher-page-probe.txt").write_text(
      f"status={page.status_code}\nfinal_url={page.url}\n"
      f"mentions_CC0={'CC0' in html}\nmentions_original_source={'original model' in html.lower()}\n"
      f"mentions_owl={'owl' in html.lower()}\n")
    result["publisher_status"]=page.status_code
    result["publisher_cc0_label_visible"]=bool('CC0' in html)
except Exception as e:
    result["publisher_page_error"]=repr(e)
try:
    with requests.get(DOWNLOAD,stream=True,timeout=(20,110),
           headers={"User-Agent":"Mozilla/5.0 owl172 research QA"}) as r:
        result["download_status"]=r.status_code
        result["download_final_url"]=r.url
        result["download_content_type"]=r.headers.get("Content-Type","")
        if r.status_code!=200:
            raise RuntimeError(f"download status {r.status_code}")
        sha=hashlib.sha256()
        count=0
        with GLB.open("wb") as out:
            for chunk in r.iter_content(1024*512):
                if not chunk:continue
                count+=len(chunk)
                if count>35000000:
                    raise RuntimeError("Refusing file larger than bounded 35 MB")
                sha.update(chunk)
                out.write(chunk)
        raw_header=GLB.open("rb").read(12)
        if len(raw_header)!=12 or raw_header[:4]!=b'glTF':
            raise RuntimeError("Response is not a GLB; rejecting HTML/placeholder")
        version,length=struct.unpack("<II",raw_header[4:12])
        if version!=2 or length!=GLB.stat().st_size:
            raise RuntimeError(f"Bad glTF version/length: {version} {length}")
        result.update(native_glb_acquired=True,glb_bytes=count,glb_sha256=sha.hexdigest(),
                      glb_version=version)
        scene=trimesh.load(GLB,force="scene",process=False)
        parts=[g for g in scene.geometry.values() if isinstance(g,trimesh.Trimesh)]
        tri=sum(len(g.faces) for g in parts)
        if tri<200:
            raise RuntimeError("No meaningful native triangle geometry")
        for p in parts:
            if not np.isfinite(p.vertices).all():
                raise RuntimeError("Nonfinite mesh vertex coordinates")
        result.update(genuine_geometry_import=True,mesh_count=len(parts),
                      triangle_count=int(tri),source_geometry_names=list(scene.geometry.keys())[:20],
                      has_scene_graph=True,
                      contains_mesh_uv=any(hasattr(g.visual,"uv") and g.visual.uv is not None for g in parts),
                      contains_visual_texture=any(getattr(getattr(g.visual,"material",None),"image",None) is not None for g in parts),
                      imported_scene_extents=[float(x) for x in scene.extents])
except Exception as e:
    result["download_or_import_error"]=str(e)
    if not result["native_glb_acquired"]:
        GLB.unlink(missing_ok=True)
finally:
    result["strict_no_release"]=True
    (OUT/"run309_source_import_metrics_NO_RELEASE.json").write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(json.dumps(result,ensure_ascii=False))
