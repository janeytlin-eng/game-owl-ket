#!/usr/bin/env python3
"""Run125: public, unauthenticated zero-payment independent juvenile owl mesh source check.
Never bypass a login, guess CDN links, or store downloaded third-party asset data.
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

OUT=pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True,exist_ok=True)
UA="Mozilla/5.0 (compatible; owl172-research-audit/1.0; public-source-license-check)"
SOURCES=[
 ("blendswap-baby-owl-artist","https://blendswap.com/blend/11643"),
 ("blendswap-owl-collection","https://blendswap.com/3d/owl"),
 ("blenderkit-baby-owl","https://www.blenderkit.com/api/v1/search/?query=baby%20owl&asset_type=model"),
 ("blenderkit-barn-owl","https://www.blenderkit.com/api/v1/search/?query=barn%20owl&asset_type=model"),
 ("blenderkit-owlet","https://www.blenderkit.com/api/v1/search/?query=owlet&asset_type=model"),
 ("printables-barn-owl-license","https://www.printables.com/model/1813515-barn-owl"),
 ("opengameart-search","https://opengameart.org/art-search-advanced?keys=baby+owl"),
 ("polyhaven-3d-assets","https://api.polyhaven.com/assets?t=models"),
]
results=[]; candidates=[]
def flatten(o,depth=0):
    if depth>2 or not isinstance(o,dict): return {}
    keys=("id","name","description","isFree","is_free","free","assetType","asset_type","license","author","authorName","downloadCount","tags","thumbnailSmallUrl","url","sourceAppName")
    return {k:(v if isinstance(v,(str,int,float,bool,type(None))) else str(v)[:250]) for k,v in o.items() if k in keys}

for name,url in SOURCES:
    status=None; err=None; body=b""; content_type=""; final_url=url
    try:
        request=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"application/json,text/html;q=0.9,*/*;q=0.5"})
        with urllib.request.urlopen(request,timeout=22) as response:
            status=response.status
            final_url=response.geturl()
            content_type=response.headers.get("Content-Type","")
            body=response.read(1000000)
    except urllib.error.HTTPError as exc:
        status=exc.code; final_url=exc.geturl()
        content_type=exc.headers.get("Content-Type","")
        body=exc.read(150000)
        err="HTTPError"
    except Exception as exc:
        err=type(exc).__name__+": "+str(exc)[:250]
    kind=("GLB" if body[:4]==b"glTF" else "ZIP" if body[:4]==b"PK\x03\x04" else "BLEND" if body[:7]==b"BLENDER" else "JSON" if body[:1] in (b"{",b"[") else "HTML" if b"<html" in body[:1200].lower() or b"<!doctype" in body[:1200].lower() else "other")
    rec={"source":name,"url":url,"status":status,"final_url":final_url,"content_type":content_type,"bytes_read":len(body),"kind":kind,"sha256_of_read_response":hashlib.sha256(body).hexdigest() if body else None,"error":err,"is_downloaded_3d":kind in ("GLB","BLEND","ZIP"),"contains_login_redirect":bool(re.search(r"login|log_in|sign_in|login_required",final_url,re.I))}
    if kind=="JSON":
        try:
            obj=json.loads(body)
            arr=obj.get("results",[]) if isinstance(obj,dict) else (obj if isinstance(obj,list) else [])
            rec["json_total"]=obj.get("count",len(arr)) if isinstance(obj,dict) else len(arr)
            rec["json_rows_sampled"]=len(arr)
            if "polyhaven" in name:
                rec["owl_match_assets"]=[k for k in obj.keys() if re.search(r"owl|owlet|chick",k,re.I)][:30] if isinstance(obj,dict) else []
            elif "blenderkit" in name:
                for row in arr:
                    if isinstance(row,dict):
                        rowname=row.get("name","")
                        tags=" ".join(str(t) for t in row.get("tags",[]))
                        if re.search(r"owl|owlet|chick|tyto",rowname+" "+tags,re.I):
                            candidates.append({"query_source":name,**flatten(row)})
                rec["raw_first_five"]=[flatten(row) for row in arr[:5] if isinstance(row,dict)]
        except (ValueError,AttributeError,TypeError) as exc:
            rec["json_parse_error"]=str(exc)[:200]
    if kind=="HTML":
        text=body.decode("utf-8","replace")
        relevant=re.sub(r"<[^>]+>"," ",text)
        relevant=re.sub(r"\s+"," ",relevant)
        rec["document_title"]=re.search(r"<title[^>]*>(.*?)</title>",text,re.I|re.S).group(1)[:250] if re.search(r"<title[^>]*>(.*?)</title>",text,re.I|re.S) else ""
        for token in ("Baby Owl Character","download","login","Creative Commons","CC-BY","commercial","no derivatives"):
            rec["html_keyword_"+re.sub(r"\W","_",token)]=bool(re.search(re.escape(token),relevant,re.I))
        rec["html_text_excerpt"]=relevant[:1100]
    results.append(rec)
    print(name, "HTTP", status,"kind",kind,"bytes",len(body),"redirect",final_url[:100],"error",err,flush=True)

data={"run":"125","date_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"reference_branch":"research/owl172-run124-booth-juvenile-terms-access-check","reference_audit":"2026-11-17-run123-run124-evidence-real-juvenile-source-access-and-rights-ART_UNREVIEWED.md","source_count":len(results),"sources":results,"blenderkit_name_matched_public_metadata":candidates[:60],"strict_provenance":"no third-party mesh file committed; public HTML and API JSON are metadata, not a 3D sculpt"}
(OUT/"run125_real_http_classification.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
downloaded=[x for x in results if x["is_downloaded_3d"]]
report=[
"# Run125 — genuinely new baby-owl sculpt asset avenues (real unauthenticated probe)",
"",
"Art gate: NO_RELEASE. This is a source-access experiment, not Blender modeling or phone WebGL testing.",
f"Actual request count: {len(results)}; actual downloadable 3D magic responses at requested public endpoints: {len(downloaded)}.",
"All responses classified by bytes and content type. Public descriptions and API metadata are not meshes.",
"",
"## Source outcomes",
]
for x in results:
    report.append(f"- {x['source']}: HTTP {x['status']}, {x['kind']}, {x['bytes_read']} bytes, final {x['final_url']}, error={x['error']}")
report+=["","## Rights and quality gate",
"- BlendSwap Baby Owl Character by drothenbucher is listed CC BY, **not** confirmed to be a Tyto castanops chick or to meet the quality gate; check actual art and author attribution before transformation.",
"- BlenderKit metadata can identify free candidates but cannot prove the model's license or download rights; any model remains unapproved until actual clean authorization and visual QA.",
"- Printables Barn Owl (birds_live, August 2026) listing is CC BY-NC-ND, unsuitable for a derived commercial game character.",
"- No links are manufactured and no sign-in, payment, private session, CDN signature or bypass attempted.",
"- Existing 251-species production and prototype untouched. No generated or approved 3D GLB, no phone GPU QA, no distribution.",
]
(OUT/"run125_source_audit.md").write_text("\n".join(report)+"\n")
(OUT/"NO_RELEASE.flag").write_text("ART_UNREVIEWED: no provenance-checked, rights-cleared, multi-view art-approved juvenile GLB. NO_RELEASE.\n")
print("Probe complete: metadata candidates",len(candidates),"3D magic",len(downloaded),flush=True)
