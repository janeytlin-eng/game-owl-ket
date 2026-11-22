#!/usr/bin/env python3
"""Run292: inspect two genuinely new, published, original native owlet/forest owl GLBs.
Research-only: unrelated game owner, no reusable license or derivative grant verified.
Do not archive or release the downloaded source geometry.
"""
import os, json, pathlib, hashlib, urllib.request, traceback, time
import trimesh
ROOT=pathlib.Path('owl172-run292-evidence'); ROOT.mkdir(exist_ok=True)
SCRATCH=pathlib.Path('owl172-run292-PRIVATE_UNLICENSED_INPUTS'); SCRATCH.mkdir(exist_ok=True)
BASE="https://raw.githubusercontent.com/zeveck/central-park-pigeon/main/game/assets/models/"
CANDIDATES={"game_owlet":"owlet.glb","game_owl":"owl.glb"}
PROVENANCE={
 "repo":"https://github.com/zeveck/central-park-pigeon",
 "description":"Other publisher's 3D game; README describes Meshy-generated game animal models.",
 "repo_readme":"https://github.com/zeveck/central-park-pigeon/blob/main/README.md",
 "asset_ledger":"https://github.com/zeveck/central-park-pigeon/blob/main/design/ASSETS.md",
 "license_status":"No applicable GLB reuse/redistribution license independently established; not CC0",
 "permission":"Evaluation metadata only. NO reuse, model redistribution, modification for product, upload to another AI model, or commercial deployment.",
 "novelty":"Different author and binaries from #172 previous adult taxidermy, public asset website, neural and Blender procedural experiments."
}
def sha(b): return hashlib.sha256(b).hexdigest()
state={"run":"292","date_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
       "target":"Tyto castanops v3 RIGHTMOST cream-white second-down young owl; not a generic owl",
       "source":PROVENANCE,"cost_usd":0,"user_release":False,"art":"UNAPPROVED",
       "physical_phone_test":"NOT_PERFORMED", "models":{}}
for label,filename in CANDIDATES.items():
 url=BASE+filename
 item={"url":url,"license":"NOT_CLEARED","no_product_use":True}
 try:
  req=urllib.request.Request(url,headers={"User-Agent":"owl172-rights-bounded-research/1.0"})
  with urllib.request.urlopen(req,timeout=90) as res:
   length=res.headers.get("Content-Length")
   if length and int(length)>35000000: raise RuntimeError("Remote model exceeds 35MB cap")
   raw=res.read(35000001)
   item["http_status"]=res.status
  if len(raw)>35000000: raise RuntimeError("Download exceeds 35MB cap")
  item.update(bytes=len(raw),sha256=sha(raw),magic=raw[:4].decode("latin-1"))
  if raw[:4]!=b"glTF" or len(raw)<10000:raise RuntimeError("No substantial native glTF mesh")
  file=SCRATCH/filename;file.write_bytes(raw)
  scene=trimesh.load(file,force="scene",process=False)
  meshes=[m for m in scene.dump(concatenate=False) if isinstance(m,trimesh.Trimesh)]
  item["native_geometry"]={
   "meshes":len(meshes),"triangles":sum(len(x.faces) for x in meshes),
   "vertices":sum(len(x.vertices) for x in meshes),
   "uv_meshes":sum(getattr(x.visual,"uv",None) is not None for x in meshes),
   "finite_vertices":all(__import__('numpy').isfinite(x.vertices).all() for x in meshes),
   "bounds_raw_WARNING_quantized_gltf_may_need_transforms":scene.bounds.tolist()
  }
  if item["native_geometry"]["triangles"]<2000:raise RuntimeError("Insufficient native triangles for donor research")
  item["private_ephemeral_path"]=str(file)
  item["result"]="BINARY_GEOMETRY_INSPECTED_RIGHTS_HOLD_NO_RELEASE"
 except Exception as ex:
  item["error"]=type(ex).__name__+": "+str(ex)[:500]
  item["traceback_tail"]=traceback.format_exc()[-2000:]
  item["result"]="NO_ELIGIBLE_ASSET"
 state["models"][label]=item
(ROOT/"machine_source_gate.json").write_text(json.dumps(state,indent=2,ensure_ascii=False)+"\n")
(ROOT/"NO_RELEASE.flag").write_text(
 "Rights not cleared. Other game original/Meshy models. Never distribute GLBs or publish as Tyto castanops juvenile; "
 "all user-facing release gates FAIL; virtual browser QA not physical mobile GPU.\n")
print(json.dumps(state,indent=2,ensure_ascii=False))
