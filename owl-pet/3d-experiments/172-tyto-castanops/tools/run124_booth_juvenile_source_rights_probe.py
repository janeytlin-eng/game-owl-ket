#!/usr/bin/env python3
"""Run124: actual no-login free artist owlet model and VN3 rights access checks.

No payment, no bypass, no derivative mesh export and no unauthorized model
redistribution. Any downloaded model bytes are held in memory only, never
committed to public GitHub. Research metadata may be archived.
"""
import datetime, hashlib, html, io, json, re, sys, urllib.error, urllib.request, zipfile
from pathlib import Path
from urllib.parse import quote

out=Path(sys.argv[1]).resolve()
out.mkdir(parents=True,exist_ok=True)
ua="owl172-open-source-rights-probe/1.0 (no credentials, no payment)"
req_headers={"User-Agent":ua,"Accept":"text/html,application/pdf,application/zip,application/octet-stream;q=0.8,*/*;q=0.5"}
LIMIT=6_000_000
observations=[]

def probe(name,url,*,expected=None):
    rec={"name":name,"url":url,"timestamp_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"expected":expected}
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers=req_headers),timeout=22) as resp:
            rec["status"]=resp.status
            rec["resolved_url"]=resp.url
            rec["content_type"]=resp.headers.get("Content-Type","")
            rec["content_length"]=resp.headers.get("Content-Length")
            content=resp.read(LIMIT+1)
        rec["read_bytes"]=len(content)
        rec["sha256"]=hashlib.sha256(content).hexdigest()
        if len(content)>LIMIT:
            rec["type"]="too_large_truncated"
        elif content.startswith(b"%PDF"):
            rec["type"]="public_terms_pdf"
            # Store only the license PDF, not the author's 3D work. User wants auditable rights.
            (out/(name+"_terms.pdf")).write_bytes(content)
        elif content.startswith(b"PK\x03\x04"):
            rec["type"]="real_3d_zip_candidate_in_memory_UNVERIFIED_RIGHTS"
            with zipfile.ZipFile(io.BytesIO(content)) as z:
                rec["zip_members"]=[{"name":i.filename,"size":i.file_size} for i in z.infolist()[:60]]
                rec["contains_3d_file"]=any(i.filename.lower().endswith((".fbx",".obj",".glb",".gltf",".blend",".unitypackage")) for i in z.infolist())
            # Model not archived because external redistribution license unknown.
        elif content[:4]==b"glTF":
            rec["type"]="real_glb_candidate_in_memory_UNVERIFIED_RIGHTS"
        else:
            page=content.decode("utf-8","replace")
            title=re.search(r"<title[^>]*>(.*?)</title>",page,flags=re.I|re.S)
            rec["page_title"]=html.unescape(re.sub(r"<[^>]+>","",title.group(1))).strip() if title else None
            if "/users/sign_in" in resp.url or "/users/sign_up" in resp.url:
                rec["type"]="login_required_not_download"
            elif "<html" in page.lower() or "<!doctype" in page.lower():
                rec["type"]="html_page_not_model"
            else:
                rec["type"]="unknown_content_not_model"
            rec["body_excerpt"]=" ".join(html.unescape(re.sub(r"<[^>]+>"," ",page[:4000])).split())[:370]
    except urllib.error.HTTPError as exc:
        rec.update(status=exc.code,type="access_error",resolved_url=exc.geturl(),error=str(exc))
    except Exception as exc:
        rec.update(status=None,type="network_error",error=repr(exc))
    observations.append(rec)
    print(json.dumps({k:rec.get(k) for k in ("name","status","resolved_url","type","contains_3d_file","error")},ensure_ascii=False),flush=True)
    return rec

# Official $0 right-age, right-genus baseline: 'running barn owl chick' (VRChat).
# The official download link can require login even for a free download.
probe("booth_artist_right_juvenile_listing",
      "https://booth.pm/ja/items/6643539",expected="free_page")
probe("booth_artist_zero_yen_download_action",
      "https://booth.pm/downloadables/6814126?variation_id=11184857",expected="signed_in_or_zip")
# VN3 Japanese/English/Chinese independent license. Publicly viewable vs.
# free model license grants are not interchangeable.
for language,google_id in [
 ("en","1nx3UjuJAnlyRTc5g02Wpxi6UMSqeZSeq"),
 ("zh","1BrlF8LW9Cwy9OvRCpiKp5VIcrxEjnEes")
]:
    probe("booth_vn3_"+language+"_terms",
        "https://drive.google.com/uc?export=download&id="+quote(google_id),
        expected="pdf_or_access_block")
# Secondary actual authored source where hair was created by film artists.
# A listing is not a mesh; if access fails, don't create a primitive replacement.
probe("blendswap_CC0_filmed_feathers_owl_listing",
      "https://blendswap.com/blend/7951",expected="listing_only")
probe("blendswap_baby_owl_catalog",
      "https://blendswap.com/3d/owl",expected="listing_only")

acquired=[r for r in observations if r["type"].startswith(("real_3d_zip_candidate","real_glb_candidate"))]
authorized=0 # Do not assert reuse before actual license reading
summary={
 "time_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "species_target":"Tyto castanops v3 rightmost cream-white downy nestling",
 "observations":observations,
 "actual_in_memory_model_candidates":len(acquired),
 "downloaded_model_files_committed":0,
 "license_clearance_for_public_3d_redistribution":False,
 "art_approval":False,
 "actual_3d_import":False,
 "real_phone_webgl":False,
 "paid_usd":0,
 "reason":"Auth/rights/download gate. A zero-price listing is not a free-standing redistributable GLB."
}
(out/"run124_official_booth_and_cc0_access_evidence.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
notes=["# #172 Run124 independent authentic downy-chick 3D asset access/rights trial",
       "",
       "**NO_RELEASE / zero added payment / no content reused without terms review**.",
       "",
       "Re-read Run122 actual Blender/WebGL aesthetics rejection and Run123 access results: continued primitive snowball/bump/face-mask sculpting is unproductive. Investigated actual hand-authored white barn-owl chick from independent VRChat artist (the free BOOTH model is the correct *age/genus look*, unlike adult Bubo copies).",
       "",
       "Run124 used actual Python HTTP GET from GitHub Actions, following standard public redirects only, and checked binary signatures, official account gate and public VN3-license links. No scraped private files, no auth bypass, no paid credits.",
       "",
       "| URL purpose | HTTP | Observed resource type | Final URL |",
       "|---|---:|---|---|"]
for item in observations:
    notes.append("| "+item["name"]+" | "+str(item["status"])+" | "+item["type"]+" | "+item.get("resolved_url",item["url"]).replace("|","%7C")+" |")
notes+=["",
 f"Actual model bytes accessible legitimately in memory: **{len(acquired)}**; none are committed, exported, or shown as a sample. The public ¥0 listing is not proof of an unconditional anonymous download or a redistribution license.",
 "",
 "The source author uses VN3 model-specific terms (EN/ZH/JA). Check actual rights for modification, model extraction, public repository redistribution and commercial WebGL before importing a source mesh. Never use a VRChat source model in the public GitHub repository without that approval.",
 "",
 "No Blender render performed without a legally obtained and rights-reviewed relevant source model. No SwiftShader or phone performance claims. Source metadata and negative findings only; no contact to merchant or spending.",
 "",
 "Status **ART_UNREVIEWED / NO_RELEASE**; avoid the previous low-quality primitive/AI model route. Independent #172 experiment only; all 251-species production, deployment and original reference unchanged."]
(out/"run124_observed_access_license_gate_NO_RELEASE.md").write_text("\n".join(notes)+"\n",encoding="utf-8")
(out/"NO_RELEASE.flag").write_text("External artist source gate only; no model has art or licensing approval; no production edits.\n")
files=sorted(f for f in out.iterdir() if f.is_file() and f.name not in ("SHA256SUMS.txt","sha_checked.log"))
(out/"SHA256SUMS.txt").write_text("".join(hashlib.sha256(f.read_bytes()).hexdigest()+"  "+f.name+"\n" for f in files))
print("RUN124_3D_FILES_ACCESSIBLE="+str(len(acquired))+" PAID=0 NO_RELEASE=True")
