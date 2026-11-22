#!/usr/bin/env python3
"""Run291: independent NO-COST genuine downloadable 3D source qualification.
Research only. Adult barn owl != #172 rightmost Tyto castanops downy juvenile.
No substitute geometric primitivies, SVG or fake turntables are ever generated.
"""
import json, os, pathlib, urllib.request, hashlib, re, traceback, sys
OUT=pathlib.Path(os.getenv("OWL291_OUT","owl172-run291-evidence"));OUT.mkdir(parents=True,exist_ok=True)
MANIFEST="https://3dassets.dev/api/v1/packs/birds-and-reptiles-hd"
SOURCE="https://3dassets.dev/packs/birds-and-reptiles-hd"
def sha(b):return hashlib.sha256(b).hexdigest()
def save_status(status):
 (OUT/"run291_status.json").write_text(json.dumps(status,indent=2,ensure_ascii=False)+"\n")
def http(url,limit=40000000):
 req=urllib.request.Request(url,headers={"User-Agent":"owl172-open-asset-research/1.0"})
 with urllib.request.urlopen(req,timeout=85) as res:
  data=res.read(limit+1)
  if len(data)>limit:raise ValueError("Response exceeds capped bytes")
  return data,int(res.status),res.headers.get("Content-Type","")
def objects(x):
 if isinstance(x,dict):
  yield x
  for a in x.values():yield from objects(a)
 elif isinstance(x,list):
  for a in x:yield from objects(a)
def urls(o):
 for x in objects(o):
  for v in x.values():
   if isinstance(v,str) and v.startswith("https://") and ".glb" in v and "cdn.3dassets.dev/" in v:
    yield v
def candidate(ob,phrase):
 for d in objects(ob):
  text=" ".join(str(d.get(k,"")) for k in ["title","name","slug","description","display_name"]).lower()
  if phrase in text:
   direct=list(urls(d))
   if direct:return d,direct[0]
   for k in ["id","assetId","asset_id","model_id"]:
    val=d.get(k)
    if isinstance(val,(int,str)) and re.fullmatch("[0-9]{3,10}",str(val)):
     return d,"https://cdn.3dassets.dev/assets/"+str(val)+"/v1/model.glb"
 return None,None
state={"run":291,"date":"2026-11-22","target":"Tyto castanops v3 rightmost cream-white juvenile",
 "source_url":SOURCE,"manifest":MANIFEST,"cost_usd":0,"release":False,
 "art":"NOT_APPROVED","phone":"NOT_TESTED","provenance":"publisher self-reported CC0; author chain not independently verified",
 "assets":{}}
try:
 raw,st,ct=http(MANIFEST,2500000);(OUT/"source_pack_manifest.json").write_bytes(raw)
 state["manifest_response"]={"status":st,"bytes":len(raw),"sha256":sha(raw),"type":ct}
 data=json.loads(raw)
 # Original public source describes CC0, user-provided 3D content does not authorize unrelated catalog assets.
 for label,phrase in [("barn_owl","barn owl"),("tree_hollow","tree stump with hollow")]:
  d,url=candidate(data,phrase)
  rec={"found_entry":bool(d),"download_url":url}
  if not url:
   # Expose exact manifest fields for debugging, never guess a model or invent a GLB.
   rec["error"]="No provider asset URL/id inside matching manifest entry"
   state["assets"][label]=rec;continue
  try:
   buf,st,ct=http(url)
   rec.update({"status":st,"bytes":len(buf),"sha256":sha(buf),"type":ct,"magic":buf[:4].decode("ascii","replace")})
   if buf[:4]!=b"glTF" or len(buf)<10000:raise ValueError("Not a real substantial native 3D GLB")
   p=OUT/(label+"_SOURCE_ONLY_NOT_JUVENILE_NO_RELEASE.glb")
   p.write_bytes(buf)
   import trimesh
   sc=trimesh.load(p,force="scene",process=False)
   mesh=[m for m in sc.dump(concatenate=False) if isinstance(m,trimesh.Trimesh)]
   rec["geometry"]={"meshes":len(mesh),"triangles":sum(len(m.faces) for m in mesh),
    "vertices":sum(len(m.vertices) for m in mesh),
    "materials":len({id(getattr(m.visual,"material",None)) for m in mesh}),
    "UV_meshes":sum(getattr(m.visual,"uv",None) is not None for m in mesh),
    "bounds":sc.bounds.tolist()}
   if rec["geometry"]["triangles"]<2000:raise ValueError("Not detailed enough to serve as character/art source")
   rec["path"]=str(p)
  except Exception as e:
   rec["error"]=type(e).__name__+": "+str(e)[:500]
   (OUT/(label+"_download_error.txt")).write_text(traceback.format_exc()[-3000:])
  state["assets"][label]=rec
except Exception as e:
 state["fatal_error"]=type(e).__name__+": "+str(e)[:600]
 (OUT/"manifest_error.txt").write_text(traceback.format_exc()[-3500:])
state["gate"]="SOURCE_NATIVE_GLBS_OBTAINED_UNREVIEWED" if any("geometry" in x for x in state["assets"].values()) else "NO_NEW_VALID_NATIVE_MESH"
state["release"]=False
(OUT/"NO_RELEASE.txt").write_text("RESEARCH ONLY / ART_UNAPPROVED / target young Tyto castanops NOT YET MODELED / physical phone GPU NOT_TESTED / RIGHTS NOT_CLEARED / NO_RELEASE\n")
save_status(state)
print(json.dumps(state,indent=2,ensure_ascii=False))
