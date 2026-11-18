#!/usr/bin/env python3
"""Run182: Actual no-fee CC0 high-detail owl GLB source audit.
Research-only donor gate, NEVER claim it is the #172 mesoptile. No synthetic mesh.
"""
import hashlib, json, os, pathlib, struct, urllib.request, traceback, datetime
ROOT=pathlib.Path(__file__).resolve().parent.parent
OUT=ROOT/"research-evidence-run182-HIGHDETAIL-CC0-SOURCE-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)
URL="https://grab3d.com/dl/owl/owl-light.glb"
LICENSE="https://grab3d.com/dl/owl/LICENSE.txt"
SHA=lambda b:hashlib.sha256(b).hexdigest()
status={"run":182,"date_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "source_url":URL,"source_page":"https://grab3d.com/models/animals/owl/",
 "actual_juvenile_Tyto":False,"no_release":True,"paid_spend_usd":0,
 "physical_mobile_gpu":"NOT_TESTED","art":"SOURCE_NOT_VETTED",
 "note":"Claimed source describes an adult GREAT HORNED owl, not Tyto castanops young."}
def record():
 (OUT/"run182_metrics.json").write_text(json.dumps(status,ensure_ascii=False,indent=2))
def fetch(url,max_size):
 req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 owl172-research-no-fee/182","Accept":"*/*"})
 with urllib.request.urlopen(req,timeout=60) as r:
  code=r.status;ct=r.headers.get("Content-Type","")
  b=r.read(max_size+1)
 if len(b)>max_size:raise RuntimeError("SOURCE_TOO_BIG")
 return b,code,ct
try:
 preflight=[ROOT/"../../AGENTS.md",ROOT/"../../README.md",
  ROOT/"../../research/species/172-tyto-castanops-v3.md",
  ROOT/"known_rejected_asset_sha256_registry.json",
  ROOT/"2026-11-18-run181-independent-sevenaxis-art-review-ART_REJECTED-NO_RELEASE.md",
  ROOT/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"]
 for p in preflight:
  if not p.exists():raise RuntimeError("MISSING_PREFLIGHT:"+str(p))
 ref=preflight[-1].read_bytes()
 assert SHA(ref)=="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9","REFERENCE_MISMATCH"
 status["reference_sha256"]=SHA(ref)
 rejects=json.loads((ROOT/"known_rejected_asset_sha256_registry.json").read_text())
 known={e["sha256"] for e in rejects["known_rejected_source_glbs"]}
 status["registry_count"]=len(known)
 record()
 lic,code,typ=fetch(LICENSE,100000)
 lictext=lic.decode("utf8",errors="replace")
 (OUT/"run182_source_license_verbatim.txt").write_text(lictext)
 status.update(license_http=code,license_mime=typ,license_sha256=SHA(lic),
  claimed_cc0=("CC0 1.0" in lictext),source_ai_assisted=("AI-assisted" in lictext))
 if not status["claimed_cc0"]:raise RuntimeError("NOT_CONFIRMED_CC0")
 # Source is not assumed acceptable; this test only checks new real mesh and its traits.
 b,code,typ=fetch(URL,28000000)
 status.update(download_http=code,content_type=typ,download_bytes=len(b),download_sha256=SHA(b))
 if len(b)<65536:raise RuntimeError("DOWNLOAD_TOO_SMALL")
 if b[:4]!=b"glTF":raise RuntimeError("NOT_GLB_MAGIC")
 _,v,total=struct.unpack_from("<4sII",b,0)
 if v!=2 or total!=len(b):raise RuntimeError("INVALID_GLB_HEADER_LENGTH")
 n,kind=struct.unpack_from("<II",b,12)
 if kind!=0x4e4f534a or n>len(b)-20:raise RuntimeError("INVALID_GLB_JSON")
 gltf=json.loads(b[20:20+n].decode("utf8"))
 accessors=gltf.get("accessors",[])
 meshes=gltf.get("meshes",[])
 stats={"meshes":len(meshes),"primitives":0,"triangles":0,"material_count":len(gltf.get("materials",[])),
  "image_count":len(gltf.get("images",[])),"texture_count":len(gltf.get("textures",[])),
  "animations":len(gltf.get("animations",[])),"nodes":len(gltf.get("nodes",[])),
  "skins":len(gltf.get("skins",[]))}
 for mesh in meshes:
  for p in mesh.get("primitives",[]):
   stats["primitives"]+=1
   if p.get("mode",4)==4:
    ind=p.get("indices")
    if ind is not None:stats["triangles"]+=accessors[ind]["count"]//3
    elif "POSITION" in p.get("attributes",{}):stats["triangles"]+=accessors[p["attributes"]["POSITION"]]["count"]//3
 status["gltf"]=stats
 if status["download_sha256"] in known:raise RuntimeError("ALREADY_REJECTED_HASH")
 (OUT/"grab3d_adult_horned_owl_light_UNAPPROVED.glb").write_bytes(b)
 status["status"]="REAL_HIGHDETAIL_CC0_GLB_DOWNLOADED_QUALITATIVE_REVIEW_REQUIRED"
 status["art"]="SOURCE_MORPHOLOGY_INCOMPATIBLE_UNLESS_REVIEW_PROVES_OTHERWISE"
 # high-poly adult mesh cannot be named Tyto chick; NO_RELEASE regardless of rendering.
except Exception as e:
 status["status"]="SOURCE_OR_PARSE_BLOCKED"
 status["error"]=repr(e)
 status["traceback"]=traceback.format_exc()[-3000:]
finally:
 status["no_release"]=True
 record()
 (OUT/"NO_RELEASE.flag").write_text("NO_RELEASE: generic adult Great Horned owl donor is not juvenile Tyto. Source/license/native import must be independently verified. Never publish as pet.\n")
 print("RUN182_SOURCE",status["status"],status.get("download_bytes",0),status.get("gltf",{}),flush=True)
