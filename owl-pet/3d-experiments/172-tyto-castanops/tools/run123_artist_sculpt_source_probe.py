#!/usr/bin/env python3
"""Run123: a real, unauthenticated, no-payment artist-source acquisition trial.

This is deliberately not a geometry generator. Do not replace an unavailable,
correct anatomical sculpt by a ball, an SVG or a great-horned adult bird.
Every server response is classified by MIME + magic bytes before use.
"""
from __future__ import annotations
import hashlib, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path
from html import unescape

out = Path(sys.argv[1]).resolve()
out.mkdir(parents=True, exist_ok=True)
headers = {"User-Agent": "owl172-noncommercial-research-source-audit/1.0 (read-only; no purchases)",
           "Accept": "application/json, application/octet-stream, text/html;q=0.8, */*;q=0.5"}
results = []
MAX = 18_000_000

def call(name, url, *, expect_mesh=False):
    record = dict(name=name, url=url, time_utc=datetime.now(timezone.utc).isoformat())
    try:
        req=urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(req, timeout=30) as resp:
            record.update(status=resp.status, final_url=resp.url,
                content_type=resp.headers.get("Content-Type", ""),
                content_length=resp.headers.get("Content-Length", ""))
            # Limit body; never download huge binaries or credentials.
            body=resp.read(MAX+1)
        record["bytes_seen"]=len(body)
        if len(body)>MAX:
            record["classification"]="too_large_to_approve_without_inspection"
        else:
            record["sha256"]=hashlib.sha256(body).hexdigest()
            if body[:4]==b"glTF":
                record["classification"]="real_glb_downloaded_candidate_NOT_ART_APPROVED"
                path=out/(re.sub(r"[^a-z0-9-]+","-",name.lower())+".glb")
                path.write_bytes(body); record["local_file"]=path.name
            elif body.startswith(b"PK\x03\x04"):
                record["classification"]="zip_downloaded_requiring_license_and_format_review"
                path=out/(re.sub(r"[^a-z0-9-]+","-",name.lower())+".zip")
                path.write_bytes(body);record["local_file"]=path.name
            elif body.startswith(b"BLENDER"):
                record["classification"]="real_blend_downloaded_candidate_NOT_ART_APPROVED"
                path=out/(re.sub(r"[^a-z0-9-]+","-",name.lower())+".blend")
                path.write_bytes(body);record["local_file"]=path.name
            elif body.lstrip().startswith((b"{",b"[")):
                record["classification"]="json_metadata_not_mesh"
                try:
                    obj=json.loads(body)
                    if isinstance(obj,dict):
                        record["json_keys"]=sorted(obj.keys())[:25]
                        for key in ("uid","name","downloadable","license","detail","error","message"):
                            if key in obj: record["json_"+key]=str(obj[key])[:240]
                        if name.startswith("polyhaven") and isinstance(obj,dict):
                            # Preserve a compact, *valid* catalog-derived match set, not a truncated JSON blob.
                            matches={k:{"name":v.get("name",""),"type":v.get("type","")} for k,v in obj.items()
                                if isinstance(v,dict) and re.search(
                                r"(?<![a-z])(owl|owlet|bird|chick|nestling|feather)(?![a-z])",
                                (k+" "+str(v.get("name",""))).lower())}
                            record["catalog_total"]=len(obj)
                            record["matched_model_names"]=matches
                            (out/"polyhaven_species_relevance.json").write_text(json.dumps(matches,indent=2,ensure_ascii=False))
                        elif name.startswith("sketchfab_"):
                            (out/(name+"_public_metadata.json")).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding="utf-8")
                except Exception as exc:
                    record["json_parse_error"]=str(exc)
            else:
                record["classification"]="html_or_other_not_a_usable_3d_asset"
                excerpt=unescape(re.sub(r"<[^>]+>"," ",body[:90000].decode("utf-8","replace")))
                record["excerpt"]=" ".join(excerpt.split())[:650]
        if expect_mesh and record["classification"] not in (
          "real_glb_downloaded_candidate_NOT_ART_APPROVED",
          "zip_downloaded_requiring_license_and_format_review",
          "real_blend_downloaded_candidate_NOT_ART_APPROVED"):
            record["acquisition"]="BLOCKED_OR_NOT_DIRECT_MESH"
    except urllib.error.HTTPError as exc:
        record.update(status=exc.code, final_url=exc.geturl(), classification="http_access_blocked_or_not_found",
                      error=str(exc))
        try: record["response_excerpt"]=exc.read(1500).decode("utf-8","replace")[:500]
        except Exception: pass
    except Exception as exc:
        record.update(status=None, classification="network_or_tls_failure",error=repr(exc))
    results.append(record)
    print(json.dumps({k:record.get(k) for k in ("name","status","final_url","classification","error")},ensure_ascii=False),flush=True)
    return record

# Source A: actual separately authored high-poly *baby* owl sculpt, not another adult owl.
# Public listing states 236,060 polygons, OBJ/FBX/BLEND and 'Royalty Free License (no AI)'.
# Listing is not evidence that the download is anonymous or redistribution allowed.
call("cgtrader_artistfrog_listing",
 "https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt")
call("cgtrader_artistfrog_official_download",
 "https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt/download",expect_mesh=True)

# Source B: museum-origin Tyto alba specimen model, CC0 declared on Sketchfab.
# Proper heart disc/genus but an adult taxidermy scan, not a chick.
# Do not circumvent the provider's access controls.
uuid="0e65de5934db4f0eae02835ba7227dcc"
call("sketchfab_museum_tyto_cc0_metadata",f"https://api.sketchfab.com/v3/models/{uuid}")
call("sketchfab_museum_tyto_official_download",f"https://api.sketchfab.com/v3/models/{uuid}/download",expect_mesh=True)

# Source C: API discovery of other artist-produced juvenile geometry.
call("sketchfab_juvenile_catalog",
 "https://api.sketchfab.com/v3/search?type=models&q=barn%20owl%20chick&downloadable=true&count=20")
call("sketchfab_owlet_catalog",
 "https://api.sketchfab.com/v3/search?type=models&q=owlet&downloadable=true&count=20")
call("sketchfab_barn_owl_catalog",
 "https://api.sketchfab.com/v3/search?type=models&q=barn%20owl&downloadable=true&count=20")
call("sketchfab_baby_owl_catalog",
 "https://api.sketchfab.com/v3/search?type=models&q=baby%20owl&downloadable=true&count=20")
call("sketchfab_tyto_castanops_catalog",
 "https://api.sketchfab.com/v3/search?type=models&q=tyto%20castanops&downloadable=true&count=20")

# Source D: truly independent, no-login and clear-license artist asset catalogue.
# Poly Haven is curated handcrafted CC0; catalog filtering tests whether
# a matching owl/owlet/sculpt actually exists, not just whether API responds.
ph=call("polyhaven_CC0_artist_model_catalog","https://api.polyhaven.com/assets?t=models")


candidate_meshes=[x for x in results if x.get("classification","").startswith(("real_glb_downloaded","real_blend_downloaded","zip_downloaded"))]
summary={
    "project":"janeytlin-eng/game-owl-ket / owl-pet / #172 Tyto castanops v3 rightmost chick",
    "timestamp_utc":datetime.now(timezone.utc).isoformat(),
    "run":"123",
    "actual_source_probes":len(results),
    "actual_downloaded_mesh_or_archives":len(candidate_meshes),
    "license_gate":"UNVERIFIED even when listing claims free/CC0: model-specific rights and actual source provenance must be checked",
    "visual_gate":"ART_UNREVIEWED / NO_RELEASE; no substitute adult/owl toy accepted",
    "physical_phone_gate":"NOT_TESTED; no verified model to benchmark",
    "paid_spend":0,
    "results":results
}
(out/"run123_actual_source_probe_results.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False))
paragraphs=[
 "# #172 Run123 independent real artist-sculpt source acquisition audit",
 "",
 "Run date: "+summary["timestamp_utc"]+"; **NO_RELEASE / ART_UNREVIEWED / no payment**.",
 "",
 "Before this trial, the repository's Run122 four-angle Cycles/WebGL results and the original rightmost chick requirements were reread. The latest Run122 is a real 6 MB GLB but aesthetically rejected due flat mask, protruding eyes, snowball body, absent wing and glittering fur. Repeating the same procedural edits cannot satisfy the art gate.",
 "",
 "This run performed real HTTP GETs against legitimate official source endpoints. It neither bypassed accounts nor paid, copied thumbnails into art, generated primitive substitute figures, modified the 251-species production pipeline, or published an unapproved asset.",
 "",
 "| Source | HTTP | Classification | Evidence |",
 "|---|---:|---|---|",
]
for r in results:
    paragraphs.append("| "+r["name"]+" | "+str(r.get("status","network-error"))+" | "+r["classification"]+" | "+(r.get("local_file") or r.get("error","")[:70] or "public metadata / response log")+" |")
paragraphs+=["",
 "The CGTrader baby-owl sculpt is a genuinely separate **artist-made juvenile** candidate, but a public web listing or thumbnail cannot be counted as a downloaded, visual-validated and distributable GLB. The Sketchfab CC0 Tyto source is a real museum taxidermy adult; anatomical genus fit does not override age/surface mismatch. API metadata is not itself geometry.",
 "",
 f"Actual acquired 3D file/archive candidates: **{len(candidate_meshes)}**. A candidate file is NOT a passed sample without import, four genuine views and license review.",
 "",
 "Blocking gates: cream-white multi-layer down, organic heart-shaped facial disc, recessed dark eyes, compact chick silhouette and short wings, coherent side/back, stout feathered shanks and bark hollow support; then true mobile WebGL hardware, animation, provenance/licence.",
 "",
 "Status: **NO_RELEASE**. No user-facing 3D sample and no fictional preview link. Tests/replies retained as JSON plus SHA256 manifest. Continue only by obtaining a verifiably redistributable juvenile sculpt or a professionally produced organic base.",
]
(out/"run123_art_source_access_audit_NO_RELEASE.md").write_text("\n".join(paragraphs)+"\n",encoding="utf-8")
(out/"NO_RELEASE.flag").write_text("Run123 source acquisition is an experimental audit only. DO NOT publish an unreviewed or unrelated model.\n")
files=sorted(p for p in out.iterdir() if p.is_file() and p.name not in ("SHA256SUMS.txt","sha_checked.log"))
(out/"SHA256SUMS.txt").write_text("".join(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.name+"\n" for p in files))
print("run123 completed probes=",len(results),"actual_downloads=",len(candidate_meshes),flush=True)
