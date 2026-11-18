#!/usr/bin/env python3
"""Run183: zero-spend live source transport + rights + real GLB gate; NO_RELEASE."""
import datetime, hashlib, json, pathlib, re, struct, traceback, urllib.request, urllib.error
R=pathlib.Path(__file__).resolve().parent.parent
O=R/"research-evidence-run183-FREE-JUVENILE-SOURCE-NO_RELEASE"
O.mkdir(parents=True, exist_ok=True)
SHA=lambda b:hashlib.sha256(b).hexdigest()
report={"run":183,"timestamp_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "art_decision":"NO_RELEASE","physical_mobile_gpu":"NOT_TESTED","real_model_of_target":"NOT_OBTAINED",
 "paid_spend_usd":0,"sources":[]}
def request(url, cap, label):
 item={"label":label,"url":url,"max_bytes":cap}
 try:
  req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; Owl172-Research-NoFee/183; provenance-check)","Accept":"*/*"})
  with urllib.request.urlopen(req,timeout=18) as r:
   item["http_status"]=r.status
   item["content_type"]=r.headers.get("Content-Type","")
   item["final_url"]=r.geturl()
   length=r.headers.get("Content-Length")
   item["advertised_bytes"]=length
   b=r.read(cap+1)
  item["size_bytes"]=len(b)
  item["sha256"]=SHA(b)
  item["oversize"]=len(b)>cap
  if item["oversize"]:
   item["result"]="OVER_SIZE_LIMIT"
   return item,None
  item["result"]="HTTP_RECEIVED"
  return item,b
 except urllib.error.HTTPError as e:
  item.update(result="HTTP_ERROR",http_status=e.code,error=str(e))
 except Exception as e:
  item.update(result="NETWORK_ERROR",error=repr(e))
 return item,None
def glb_stats(b):
 if b[:4]!=b"glTF" or len(b)<20:raise ValueError("NOT_A_GLB_MAGIC")
 magic,version,total=struct.unpack_from("<4sII",b,0)
 if version!=2 or total!=len(b):raise ValueError("BAD_GLB_LENGTH_OR_VERSION")
 n,kind=struct.unpack_from("<II",b,12)
 if kind!=0x4e4f534a or n>len(b)-20:raise ValueError("BAD_GLB_JSON_CHUNK")
 d=json.loads(b[20:20+n].decode("utf-8"))
 access=d.get("accessors",[])
 triangles=0
 for m in d.get("meshes",[]):
  for p in m.get("primitives",[]):
   if p.get("mode",4)==4:
    idx=p.get("indices")
    if idx is not None:triangles+=access[idx]["count"]//3
    elif p.get("attributes",{}).get("POSITION") is not None:triangles+=access[p["attributes"]["POSITION"]]["count"]//3
 return {"meshes":len(d.get("meshes",[])),"triangles":triangles,"materials":len(d.get("materials",[])),
         "textures":len(d.get("textures",[])),"images":len(d.get("images",[])),
         "skins":len(d.get("skins",[])),"animations":len(d.get("animations",[]))}
def add(item):report["sources"].append(item);print("LIVE_SOURCE",json.dumps(item,ensure_ascii=False),flush=True)
checks={
 "AGENTS":pathlib.Path("owl-pet/AGENTS.md"),
 "README":pathlib.Path("owl-pet/README.md"),
 "prototype":pathlib.Path("owl-pet/prototype/index.html"),
 "design":pathlib.Path("owl-pet/research/species/172-tyto-castanops-v3.md"),
 "Run181":R/"2026-11-18-run181-independent-sevenaxis-art-review-ART_REJECTED-NO_RELEASE.md",
 "Run182":R/"2026-11-18-run182-new-highdetail-cc0-source-native-ART_REJECTED-NO_RELEASE.md",
 "registry":R/"known_rejected_asset_sha256_registry.json",
 "reference":R/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png",
}
report["preflight"]={k:p.exists() and p.stat().st_size>0 for k,p in checks.items()}
if not all(report["preflight"].values()):raise RuntimeError("MISSING_REQUIRED_PREFLIGHT "+str(report["preflight"]))
ref=checks["reference"].read_bytes()
report["reference_sha256"]=SHA(ref)
assert SHA(ref)=="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
rejects=json.loads(checks["registry"].read_text())["known_rejected_source_glbs"]
report["rejected_registry_count"]=len(rejects)
known={x["sha256"] for x in rejects}
# Primary source: genuinely license-first; previous Run182 never reached any fetch due 28-minute apt stall.
li,license_bytes=request("https://grab3d.com/dl/owl/LICENSE.txt",131072,"grab3d_cc0_license")
if license_bytes is not None:
 lic=license_bytes.decode("utf-8","replace")
 (O/"run183_grab3d_license_actual.txt").write_text(lic)
 li["cc0_token_detected"]=bool(re.search(r"CC0|creative\s+commons\s+zero",lic,re.I))
 li["explicit_license_content"]=lic[:2000]
add(li)
if li.get("cc0_token_detected"):
 model,b=request("https://grab3d.com/dl/owl/owl-light.glb",26000000,"grab3d_adult_great_horned_light_glb")
 if b is not None:
  try:
   model["gltf"]=glb_stats(b)
   model["known_rejected_sha"]=SHA(b) in known
   (O/"grab3d_REAL_ADULT_NOT_TYTO_UNAPPROVED.glb").write_bytes(b)
   model["art_decision"]="ART_REJECTED_AS_TYTO_CHICK_ADULT_HORNED"
  except Exception as e:model["parse_error"]=repr(e)
 add(model)
else:report["grab3d_transport_skipped"]="LICENSE_CANNOT_BE_INDEPENDENTLY_VERIFIED"
# A higher-relevance candidate is listed FREE as Baby Owl Sculpt, but access and derivative rights must actually be checked.
for label,url in [
 ("cgtrader_free_baby_owl_sculpt","https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt"),
 ("blenderkit_baby_barn_owl_animated","https://www.blenderkit.com/asset-gallery-detail/af064619-74d4-496f-bdde-bdc742e08824/")
]:
 item,b=request(url,550000,label)
 if b is not None:
  html=b.decode("utf-8","replace")
  item["is_html"]=("<html" in html[:10000].lower() or "<!doctype" in html[:10000].lower())
  item["page_signals"]={s:bool(re.search(re.escape(s),html,re.I)) for s in ["Free Baby Owl Sculpt","Royalty Free License","no AI","Download","Full Plan","Baby Owl Animated","Sign in","Log in"]}
  item["direct_model_binary"]=b[:4]==b"glTF"
  (O/(label+"_http_excerpt.txt")).write_text(html[:15000])
 add(item)
report["conclusion"]="NO_RELEASE_NO_ART_PASS"
(O/"run183_results.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
(O/"NO_RELEASE.flag").write_text("Run183: NOT an art-passing Tyto castanops v3 chick; no model adopted or released. No paid credits.\n")
print("RUN183_FINAL",report["conclusion"],len(report["sources"]),flush=True)
