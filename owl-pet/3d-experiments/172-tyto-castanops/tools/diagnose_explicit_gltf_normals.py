#!/usr/bin/env python3
"""Diagnostic only: add explicit normalized vertex NORMAL to an existing genuine GLB.
Do not claim anatomy, plumage, physical phone, or art approval."""
import hashlib,json,struct,sys
from pathlib import Path
import trimesh
from trimesh.exchange.gltf import export_glb
inp,out=map(Path,sys.argv[1:3])
original=trimesh.load(inp,force="scene",process=False)
out.write_bytes(export_glb(original,include_normals=True,unitize_normals=True))
again=trimesh.load(out,force="scene",process=False)
assert len(original.geometry)==len(again.geometry)
assert sum(len(g.faces) for g in original.geometry.values())==sum(len(g.faces) for g in again.geometry.values())
assert again.geometry["ORGANIC_CONNECTED_HEAD_BODY_HEART_RELIEF"].is_watertight
data=out.read_bytes();n=struct.unpack_from("<I",data,12)[0]
doc=json.loads(data[20:20+n])
body=next(mesh for mesh in doc["meshes"] if mesh["name"]=="ORGANIC_CONNECTED_HEAD_BODY_HEART_RELIEF")
assert "NORMAL" in body["primitives"][0]["attributes"]
print(json.dumps({"original_bytes":inp.stat().st_size,"output_bytes":len(data),
    "meshes":len(again.geometry),"triangles":sum(len(g.faces) for g in again.geometry.values()),
    "body_normal_attribute":True,"sha256":hashlib.sha256(data).hexdigest()},indent=2))
