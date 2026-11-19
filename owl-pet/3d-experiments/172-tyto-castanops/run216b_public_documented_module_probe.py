#!/usr/bin/env python3
"""Read-only public asset endpoint probe; NO payment, no authentication, no bypass."""
import urllib.request, urllib.error, datetime, hashlib, json, re
from pathlib import Path
out=Path("owl-pet/3d-experiments/172-tyto-castanops/run216b-evidence")
out.mkdir(exist_ok=True,parents=True)
root="https://gaitkit.com"
paths=["/cdn/eaglet.mjs","/cdn/eaglet-params.json"]
result={"experiment":"Run216b Gaitkit officially documented direct code module accessibility",
"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
"published_snippet":"import { createAsset } from 'https://gaitkit.com/cdn/eaglet.mjs'",
"paid_fallback":False,"charged_usd":0,"art_gate":"NOT_PASSED",
"release":"NO_RELEASE","checks":[]}
for p in paths:
    record={"url":root+p}
    request=urllib.request.Request(root+p,headers={"User-Agent":"Mozilla/5.0 Owl172 no-auth research browser QA","Accept":"*/*"})
    try:
        with urllib.request.urlopen(request,timeout=25) as r:
            body=r.read(8_000_001)
            record["status"]=r.status
            record["content_type"]=r.headers.get("Content-Type","")
        assert len(body)<=8_000_000,"Source >8MB bound"
        record["length"]=len(body)
        record["sha256"]=hashlib.sha256(body).hexdigest()
        if p.endswith(".mjs"):
            src=body.decode("utf-8","replace")
            record["export_mentions_createAsset"]=bool(re.search(r"\bcreateAsset\b",src))
            record["declared_import_paths"]=(re.findall(r'from\s+["\x27]([^"\x27]+)',src)+re.findall(r'import\s+["\x27]([^"\x27]+)',src))[:40]
            record["contains_glb_or_buffer"]=bool(re.search(r"GLB|glTF|THREE|BufferGeometry|createAsset",src))
        elif p.endswith(".json"):
            try: record["top_level_keys"]=list(json.loads(body))[:60]
            except (ValueError,TypeError): pass
    except urllib.error.HTTPError as e:
        record["http_status"]=e.code
        record["error"]="HTTP access restriction; no retry or bypass"
    except Exception as e:
        record["error"]=type(e).__name__+": "+str(e)
    result["checks"].append(record)
result["status"]="DOC_MODULE_AVAILABLE_FOR_INSPECTION_ONLY" if result["checks"][0].get("status")==200 else "PUBLIC_MODULE_NOT_RETRIEVABLE_NO_RELEASE"
(out/"run216b_access_report.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
(out/"run216b_access_report.md").write_text(
    "# Run216b — documented no-auth animated juvenile source endpoint probe\n\n"
    "Source publication: https://gaitkit.com/asset/eaglet . "
    "Run216 real GLB download returned **HTTP 402**; this separate trial checks the public JS import route "
    "shown in the published code example. Does not defeat auth, execute remote code or spend money.\n\n"
    "**Outcome:** "+result["status"]+"; **NO_RELEASE**. JSON contains exact HTTP/error evidence. "
    "The biological source remains a golden-eagle nestling, not a Tyto chick; even accessible modules "
    "must never be advertised as target asset.\n")
print(json.dumps(result,ensure_ascii=False,indent=2))
