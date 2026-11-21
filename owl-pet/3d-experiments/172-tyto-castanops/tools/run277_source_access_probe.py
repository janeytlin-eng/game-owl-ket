#!/usr/bin/env python3
"""#172 Run277 public, no-login source access + rights gate; never bypass account/paywall.
Real HTTP responses only; do not infer possession of downloaded binary from a listing.
"""
import hashlib,json,os,urllib.request,urllib.error,urllib.parse,time,traceback
from pathlib import Path
out=Path(os.environ.get("OWL172_OUTPUT","owl172-run277-evidence"))
out.mkdir(parents=True,exist_ok=True)
sources=[
 {"key":"booth_free_barn_owl_chick","landing":"https://booth.pm/ja/items/6643539","download":"https://booth.pm/downloadables/6814126?variation_id=11184857","listed_price":"JPY 0; public listing but free-download click redirects to account sign-in","terms":"https://drive.google.com/file/d/1nx3UjuJAnlyRTc5g02Wpxi6UMSqeZSeq/view","claim":"author りったいミーム; VN3 agreement, redistribution not cleared"},
 {"key":"cgtrader_artistfrog_baby_owl_sculpt","landing":"https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt","download":None,"listed_price":"Free, account/workflow potentially required; 236060 polygons per seller","terms":"CGTrader Royalty Free (no AI), license needs confirmation for this workflow","claim":"artist ArtistFrog; artist source, not necessarily Tyto"}
]
class SafeRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  x=urllib.parse.urlsplit(newurl)
  if x.scheme!="https" or x.hostname not in {"booth.pm","www.cgtrader.com","cgtrader.com"}:
   raise RuntimeError("refusing redirect to unexpected origin")
  return super().redirect_request(req,fp,code,msg,headers,newurl)
opener=urllib.request.build_opener(SafeRedirect)
records={}
for s in sources:
 rr={"listed":s,"downloaded_3d_asset":False,"native_3d_verified":False,"rights_cleared":False}
 for endpoint in ["landing","download"]:
  u=s.get(endpoint)
  if not u:continue
  try:
   req=urllib.request.Request(u,headers={"User-Agent":"owl172-asset-access-research/1.0","Accept":"text/html,application/octet-stream,*/*"})
   with opener.open(req,timeout=35) as resp:
    prefix=resp.read(2048)
    url=resp.geturl()
    ctype=resp.headers.get("Content-Type","")
    rr[endpoint+"_http"]={"status":resp.status,"final_url":url,
     "content_type":ctype,"prefix_sha256":hashlib.sha256(prefix).hexdigest(),
     "prefix_bytes":len(prefix)}
    if prefix[:4] in (b"glTF",b"PK\\x03\\x04"):
     rr[endpoint+"_http"]["note"]="Binary prefix ONLY; incomplete body, NOT a verified asset"
    if "users/sign_in" in url:rr[endpoint+"_http"]["gate"]="LOGIN_REQUIRED_NO_DOWNLOAD"
    elif "text/html" in ctype:rr[endpoint+"_http"]["gate"]="HTML_NOT_3D"
    else:rr[endpoint+"_http"]["gate"]="NEEDS_FULL_FILE_AND_LICENSE"
  except Exception as e:
   rr[endpoint+"_http"]={"error":type(e).__name__+": "+str(e)[:350],
     "gate":"ACCESS_UNAVAILABLE_NOT_3D"}
 records[s["key"]]=rr
 print(s["key"],rr,flush=True)
report={"run":"277","date":"2026-11-22","purpose":"Real HTTP access gating for direct juvenile 3D candidates",
 "consent":"No login, no account creation, no payment, no bypass, no redistribution",
 "gates":{"actual_free_high_quality_juvenile_binary_acquired":False,
          "full_model_license_verified":False,
          "art_accepted":False,"phone_gpu_tested":False},
 "sources":records,"release":"NO_RELEASE"}
(out/"run277-source-access.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
(out/"SOURCE_ACCESS_NO_RELEASE.flag").write_text("No complete free high quality juvenile asset acquired. No product release.\n")
