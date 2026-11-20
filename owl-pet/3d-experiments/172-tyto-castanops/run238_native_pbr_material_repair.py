#!/usr/bin/env python3
"""Run238: repair actual Run236 learned 3D owl's missing PBR materials.
Existing neural positions, triangles, UV, NORMAL, COLOR_0, fur texture and
binary buffer are byte-for-byte preserved. Never treat this as art approval.
"""
import hashlib
import json
import struct
import sys
from pathlib import Path

IN_SHA = "4a4a1b22048734d2926b1e27066dd76f125b4575554b305fd28b3233db300d33"
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/"owl-pet/3d-experiments/172-tyto-castanops"
SOURCE=BASE/"run238-source/run236_real_neural_eye_softdown_STUDY_ART_REJECTED_NO_RELEASE.glb"
OUT=BASE/"run238-evidence"
OUT.mkdir(parents=True, exist_ok=True)
MODEL=OUT/"run238_real_juvenile_core_nonmetal_PBR_NATIVE_3D_ART_REJECTED_NO_RELEASE.glb"
def sha(b): return hashlib.sha256(b).hexdigest()
report={"run":"Run238","release":"NO_RELEASE","art_pass":False,
 "phone_webgl":"UNTESTED","no_new_paid_services":True,
 "method":"native glTF GLB JSON-chunk PBR material repair; original BIN chunk unchanged"}
try:
 b=SOURCE.read_bytes()
 assert b[:4]==b"glTF" and sha(b)==IN_SHA
 version,length=struct.unpack_from("<II",b,4)
 jsonlen,chunktype=struct.unpack_from("<I4s",b,12)
 assert version==2 and length==len(b) and chunktype==b"JSON"
 data=json.loads(b[20:20+jsonlen])
 binary_tail=b[20+jsonlen:]
 binlen,bintype=struct.unpack_from("<I4s",binary_tail,0)
 assert bintype==b"BIN\x00" and binlen==len(binary_tail)-8
 assert len(data["meshes"])==8 and len(data["materials"])==1
 originals=[json.loads(json.dumps(mesh["primitives"])) for mesh in data["meshes"]]
 assert "alphaMode" in data["materials"][0]
 pbr={"name":"nonmetallic_rough_juvenile_colored_neural_sculpt",
  "pbrMetallicRoughness":{
     "baseColorFactor":[1.0,1.0,1.0,1.0],
     "metallicFactor":0.0,"roughnessFactor":0.94
   },
   "doubleSided":True}
 idx=len(data["materials"])
 data["materials"].append(pbr)
 count=0
 for i, mesh in enumerate(data["meshes"]):
  for prim in mesh["primitives"]:
   if i==1:
    assert prim.get("material")==0
    continue
   assert "material" not in prim,("Unexpected preexisting material",i)
   assert {"POSITION","NORMAL","COLOR_0"}<=set(prim["attributes"])
   prim["material"]=idx
   count+=1
 raw=json.dumps(data,separators=(",",":"),ensure_ascii=False).encode("utf8")
 raw+=b" "*((-len(raw))%4)
 out=struct.pack("<4sII",b"glTF",2,12+8+len(raw)+len(binary_tail))
 out+=struct.pack("<I4s",len(raw),b"JSON")+raw+binary_tail
 MODEL.write_bytes(out)
 assert out[20+len(raw):]==binary_tail
 # Verify geometry, attribute indices, buffers, images and all other mesh keys unchanged.
 reread=json.loads(out[20:20+len(raw)])
 assert reread["accessors"]==json.loads(b[20:20+jsonlen])["accessors"]
 assert reread["bufferViews"]==json.loads(b[20:20+jsonlen])["bufferViews"]
 assert reread["buffers"]==json.loads(b[20:20+jsonlen])["buffers"]
 for i, original in enumerate(originals):
  for j, prim in enumerate(original):
   new=dict(reread["meshes"][i]["primitives"][j])
   if i!=1: assert new.pop("material")==idx
   assert new==prim
 report.update(status="REAL_NATIVE_PBR_PATCHED_TECH_ONLY_ART_REJECTED_NO_RELEASE",
   original_glb={"bytes":len(b),"sha256":sha(b)},
   corrected_glb={"bytes":len(out),"sha256":sha(out)},
   original_binary_chunk_sha256=sha(binary_tail),
   corrected_binary_chunk_sha256=sha(out[20+len(raw):]),
   geometry_and_texture_bin_unchanged=True,
   mesh_count=len(data["meshes"]),repaired_primitive_count=count,
   material_after=len(data["materials"]),alpha_down_material_retained=True)
 print(json.dumps(report,ensure_ascii=False,indent=2))
except Exception as e:
 report["status"]="FAILURE_NO_RELEASE";report["error"]=repr(e)
 print(json.dumps(report),file=sys.stderr)
 raise
finally:
 (OUT/"run238_material_patch_machine_report.json").write_text(
  json.dumps(report,ensure_ascii=False,indent=2)+"\n")
