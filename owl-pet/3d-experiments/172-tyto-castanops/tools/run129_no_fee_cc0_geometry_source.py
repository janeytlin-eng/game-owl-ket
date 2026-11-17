#!/usr/bin/env python3
"""Run129: real, no-cost public CC0 candidate download and glTF geometry audit.

Source URLs are official catalogue entries, never invented signed CDN URLs.
Inspect only; every source is NO_RELEASE until professional four-view art + physical GPU QA.
"""
import datetime
import hashlib
import json
import re
import struct
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit
OUT=Path(sys.argv[1]); OUT.mkdir(parents=True,exist_ok=True)
MAX_JSON=18*1024*1024
MAX_MODEL=24*1024*1024
SOURCE={
  "catalog":"https://gobkit.com/api/free",
  "community":"https://gobkit.com/api/community",
  "juvenile_eagle":"https://gaitkit.com/asset/eaglet",
  "pixabay_chick":"https://pixabay.com/3d-models/chick-bird-animal-yellow-cute-816/",
}
HEADERS={"User-Agent":"owl172-noncommercial-research/1.0 (automated source verification)"}
def get(url,cap):
    req=urllib.request.Request(url,headers=HEADERS)
    with urllib.request.urlopen(req,timeout=35) as resp:
        status=resp.status;final=resp.geturl();ctype=resp.headers.get("Content-Type","")
        b=resp.read(cap+1)
        return {"status":status,"final_host":urlsplit(final).hostname,"type":ctype,"bytes":len(b),
          "sha256":hashlib.sha256(b).hexdigest(),"truncated":len(b)>cap},b[:cap]
def inspect_glb(data):
    r={"magic":data[:4].decode("ascii","replace"),"size_bytes":len(data)}
    if len(data)<20 or data[:4]!=b"glTF":
        r["valid_glb"]=False;return r
    magic,version,total=struct.unpack_from("<4sII",data,0)
    r.update({"version":version,"declared_length":total,"valid_glb":version==2 and total==len(data)})
    if not r["valid_glb"]:return r
    n,ctype=struct.unpack_from("<I4s",data,12)
    if ctype!=b"JSON" or n>len(data)-20: r["valid_glb"]=False;return r
    obj=json.loads(data[20:20+n].decode("utf-8"))
    r["asset"]=obj.get("asset",{});r["mesh_count"]=len(obj.get("meshes",[]))
    r["skins"]=len(obj.get("skins",[]));r["materials"]=len(obj.get("materials",[]))
    r["textures"]=len(obj.get("textures",[]));r["images"]=len(obj.get("images",[]))
    r["animation_names"]=[a.get("name","") for a in obj.get("animations",[])]
    r["mesh_names"]=[m.get("name","") for m in obj.get("meshes",[])]
    triangles=0;unknown=0
    accessors=obj.get("accessors",[])
    for mesh in obj.get("meshes",[]):
      for prim in mesh.get("primitives",[]):
        mode=prim.get("mode",4)
        if "indices" in prim:
            ix=prim["indices"]; count=accessors[ix]["count"] if ix < len(accessors) else 0
        else:
            ix=prim.get("attributes",{}).get("POSITION",-1)
            count=accessors[ix]["count"] if 0<=ix<len(accessors) else 0
        if mode==4: triangles+=count//3
        elif mode in (5,6):triangles+=max(0,count-2)
        else:unknown+=1
    r["triangles_all_meshes"]=triangles;r["non_triangle_primitives"]=unknown
    return r
report={"run":129,"date_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "task":"#172 Tyto castanops v3 right-side cream mesoptile",
        "sources":{},"candidate":[],"art_gate":"ART_UNREVIEWED","release":"NO_RELEASE","extra_payment_usd":0,
        "boundary":"No 251-species production edits; no paid downloads or logins"}
for tag,url in SOURCE.items():
  try:
    info,payload=get(url,MAX_JSON)
    report["sources"][tag]={"url":url,**info}
    if tag=="catalog" and not info["truncated"]:
      catalog=json.loads(payload);packs=catalog.get("packs",[])
      rows=[{"pack":p.get("name"),**m} for p in packs for m in p.get("models",[])]
      report["catalog_summary"]={"declared":catalog.get("totalFreeModels"),
          "pack_count":len(packs),"model_count":len(rows),
          "owl_matches":[{"id":m.get("id"),"name":m.get("name"),"pack":m.get("pack"),
               "url":m.get("url"),"rigged":m.get("rigged"),
               "lowPoly":m.get("lowPoly"),"license":m.get("license")} for m in rows if
                 re.search(r"\\b(owl|owlet|owls|barn[ -]?owl|chick)\\b",(m.get("id","")+" "+m.get("name","")).lower())][:40]}
      for m in rows:
        if ((m.get("id","").lower()=="owl" or m.get("name","").lower()=="owl") and
            m.get("url","").startswith("https://gobkit.com/")):
          url=m["url"];detail,b=get(url,MAX_MODEL)
          item={"catalog_id":m.get("id"),"source_url":url,"source_meta":detail,
                "licence_claim":m.get("license"),"claimed_low_poly":m.get("lowPoly"),
                "release":"NO_RELEASE"}
          if not detail["truncated"]:
            item["geometry"]=inspect_glb(b)
            if item["geometry"].get("valid_glb"):
              p=OUT/"owl_gobkit_CC0_technical_donor_ONLY.glb"
              p.write_bytes(b); item["file_path"]=p.name
          report["candidate"].append(item);break
    elif tag=="community" and not info["truncated"]:
      community=json.loads(payload)
      report["community_keys"]=list(community.keys())
      entries=community.get("models",community.get("items",[]))
      if isinstance(entries,list):
        report["community_summary"]={"count":len(entries),"owl_matches":[
          {"name":x.get("title",x.get("name")), "url":x.get("model_url",x.get("url"))}
          for x in entries if isinstance(x,dict) and re.search(r"owl|chick",json.dumps(x.get("title",x.get("name",""))),re.I)][:20]}
    elif tag=="juvenile_eagle":
      html=payload.decode("utf-8","replace")
      report["sources"][tag]["publisher_pro_label"]=bool(re.search(r"Pro download|Pro[^a-z]{0,20}eaglet\\.glb",html,re.I))
      report["sources"][tag]["decision"]="METADATA_ONLY_NOT_TARGET_SPECIES_NO_PAYMENT"
    elif tag=="pixabay_chick":
      report["sources"][tag]["decision"]="DISTINCT_SPECIES_STYLIZED_CHICK; browser free-download path requires separate gated QA"
  except Exception as e:
    report["sources"][tag]={"url":url,"error":str(e)[:360],"outcome":"REQUEST_FAILED"}
(OUT/"run129_source_metrics.json").write_text(json.dumps(report,indent=2,ensure_ascii=False,default=str)+"\n")
(OUT/"NO_RELEASE.flag").write_text("NO_RELEASE — an owl-shaped real GLB, if downloaded, is a technical donor only. Art, exact juvenile Tyto anatomy, copyright provenance, physical phone WebGL and redistribution are NOT approved.\n")
print(json.dumps({"source_status":{k:v.get("status",v.get("error")) for k,v in report["sources"].items()},
                  "catalog_matches":report.get("catalog_summary",{}).get("owl_matches",[]),
                  "geometry":[v.get("geometry") for v in report["candidate"]],
                  "release":report["release"]},ensure_ascii=False))
