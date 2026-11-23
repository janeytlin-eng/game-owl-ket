#!/usr/bin/env python3
"""Run327: inspect a genuinely juvenile, publicly downloadable 3D source.
It is an EAGLET, NOT a Tyto chick. Keep it a strict research-only negative
control, not a mislabeled owl. No login, paid credit or access bypass.
"""
import hashlib
import json
import struct
import sys
from pathlib import Path
from urllib.parse import urlparse
import requests

OUT=Path(sys.argv[1] if len(sys.argv)>1 else "owl172-run327-evidence")
OUT.mkdir(parents=True,exist_ok=True)
SOURCE="https://gaitkit.com/cdn/eaglet.glb"
PAGE="https://gaitkit.com/asset/eaglet"
FILE="gaitkit_eaglet_juvenile_anatomy_comparison_NOT_AN_OWL_NO_RELEASE.glb"
report={
  "run":327, "source_page":PAGE, "source_url":SOURCE,
  "target":"#172 Tyto castanops v3 rightmost cream-white mesoptile chick (age unknown)",
  "source_taxon":"golden eagle nestling, NOT an owl; donor for juvenile geometry QA only",
  "source_license_claim":"Gaitkit free download, commercial use no credit, no asset resale or model-training; independently verify conditions before derivatives",
  "true_juvenile_source":True, "correct_species":False, "reference_face_match":False,
  "art_approved":False, "release":False, "additional_paid_usd":0,
  "physical_iphone_android_tested":False,
  "independent_species_production_untouched":True,
  "verified_native_glb":False,
}
try:
  page=requests.get(PAGE,timeout=30,headers={"User-Agent":"Mozilla/5.0 (research)"})
  report["source_page_http_status"]=page.status_code
  text=page.text.lower() if page.status_code==200 else ""
  report["published_free_label_present"]=("free download" in text or "free" in text)
  report["published_species_label_present"]=("eaglet" in text)
  r=requests.get(SOURCE,timeout=90,headers={"User-Agent":"Mozilla/5.0 (owl172-research-no-purchase)"},stream=True)
  report["source_http_status"]=r.status_code
  report["mime"]=r.headers.get("Content-Type")
  r.raise_for_status()
  chunks=[];n=0
  for chunk in r.iter_content(256*1024):
    if chunk:
      n+=len(chunk)
      if n>25_000_000: raise ValueError("unexpected size exceeds 25MB research safety budget")
      chunks.append(chunk)
  raw=b"".join(chunks)
  report["bytes"]=len(raw)
  report["sha256"]=hashlib.sha256(raw).hexdigest()
  if len(raw)<100_000 or raw[:4]!=b"glTF":
    raise ValueError("no native GLB bytes")
  magic,vers,length=struct.unpack_from("<4sII",raw)
  if magic!=b"glTF" or vers!=2 or length!=len(raw):
    raise ValueError("GLB header inconsistent")
  jslen,jstype=struct.unpack_from("<I4s",raw,12)
  if jstype!=b"JSON" or jslen>len(raw)-20:raise ValueError("GLB JSON chunk invalid")
  data=json.loads(raw[20:20+jslen].rstrip(b" \x00"))
  acc=data.get("accessors",[])
  triangles=0
  for mesh in data.get("meshes",[]):
    for prim in mesh.get("primitives",[]):
      if prim.get("mode",4)==4:
        k=prim.get("indices",prim.get("attributes",{}).get("POSITION"))
        if isinstance(k,int):triangles+=int(acc[k]["count"])//3
  report["native_structure"]={
    "triangles":triangles,"mesh_count":len(data.get("meshes",[])),
    "node_count":len(data.get("nodes",[])),"animation_clips":[a.get("name") for a in data.get("animations",[])],
    "materials":len(data.get("materials",[])),"skins":len(data.get("skins",[])),
    "images":len(data.get("images",[])), "asset":data.get("asset",{}),
    "node_names":[n.get("name","") for n in data.get("nodes",[])][:70],
  }
  if triangles<2000 or not data.get("meshes"):raise ValueError("native geometry below minimum meaningful threshold")
  p=OUT/FILE
  p.write_bytes(raw)
  import trimesh
  model=trimesh.load(str(p),force="scene",process=False)
  report["independent_trimesh_reimport"]={
    "success":True,"mesh_count":len(model.geometry),
    "bounds":model.bounds.tolist() if model.bounds is not None else None,
  }
  report["verified_native_glb"]=True
except Exception as e:
  report["failure"]=repr(e)
finally:
  (OUT/"source_native_report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
  (OUT/"NO_RELEASE.txt").write_text(
    "THIS IS A GOLDEN EAGLE NESTLING NOT TYTO CASTANOPS. "
    "Technical geometry donor test only. No rightmost concept replication, "
    "no facial-disc acceptance, no actual phone test, no licence chain-of-title approval. "
    "Do not publish as pet.\n")
  print(json.dumps(report,indent=2,ensure_ascii=False))
  if not report["verified_native_glb"]: sys.exit(2)
