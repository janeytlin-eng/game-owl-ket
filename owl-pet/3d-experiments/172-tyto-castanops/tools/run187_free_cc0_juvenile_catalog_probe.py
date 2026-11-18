#!/usr/bin/env python3
"""Run187: one-off, read-only free/CC0 juvenile owl asset census and native GLB probe.
Not a source of approved art. Never claims geometry counts establish visual acceptance.
"""
import datetime
import hashlib
import json
import pathlib
import re
import struct
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError

ROOT = pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT = ROOT / "research-evidence-run187-CC0-JUVENILE-CATALOG-NO_RELEASE"
OUT.mkdir(parents=True, exist_ok=True)
REF = ROOT / "research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
EXPECTED = "5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
REG = ROOT / "known_rejected_asset_sha256_registry.json"
TERMS = ["baby owl", "owlet", "owl chick", "juvenile owl", "barn owl chick", "nestling owl"]
HEADERS = {"User-Agent": "owl172-research-catalog-audit/1.0 (one-off, nonbulk)", "Accept": "application/json"}
RESULT = {"utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "provider": "3dassets.dev",
          "terms": TERMS, "reference_expected_sha256": EXPECTED, "reference_actual_sha256": None,
          "preflight": {}, "requests": [], "assets_discovered": [], "downloads": [],
          "release": False, "physical_mobile_gpu_tested": False, "extra_spend_usd": 0}
for p in [pathlib.Path("owl-pet/AGENTS.md"), pathlib.Path("owl-pet/README.md"),
          pathlib.Path("owl-pet/prototype/index.html"),
          pathlib.Path("owl-pet/research/species/172-tyto-castanops-v3.md"),
          ROOT/"2026-11-18-run186-dom-submission-verified-no-new-glb-NO_RELEASE.md", REG]:
    RESULT["preflight"][str(p)] = {"exists": p.exists(), "bytes": p.stat().st_size if p.exists() else 0}
RESULT["reference_actual_sha256"] = hashlib.sha256(REF.read_bytes()).hexdigest() if REF.exists() else "MISSING"
if RESULT["reference_actual_sha256"] != EXPECTED:
    RESULT["fatal"] = "Source-bound input hash mismatch/missing; no asset can be accepted"
if REG.exists():
    reg = json.loads(REG.read_text())
    rejected = {a["sha256"] for a in reg.get("known_rejected_source_glbs", []) if a.get("sha256")}
else:
    rejected = set()
RESULT["known_rejected_sha_count"] = len(rejected)

def fetch(url, limit=1_000_000):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=24) as response:
            code = response.status
            body = response.read(limit + 1)
            mime = response.headers.get("Content-Type", "")
            return code, body, mime
    except HTTPError as exc:
        return exc.code, exc.read(4096), exc.headers.get("Content-Type", "")
    except (TimeoutError, URLError, OSError) as exc:
        return 0, repr(exc).encode(), "ERROR"

def records_from(raw):
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        for field in ("data", "results", "assets", "items"):
            val = raw.get(field)
            if isinstance(val, list):
                return val
            if isinstance(val, dict):
                for inner in ("assets", "results", "items"):
                    if isinstance(val.get(inner), list):
                        return val[inner]
    return []

def relevant(a):
    t = (" ".join(str(a.get(k, "")) for k in ("name", "title", "slug", "description", "summary"))).lower()
    owl = bool(re.search(r"\b(owl|owlet|tyto)\b", t))
    juvenile = bool(re.search(r"\b(baby|young|juvenile|owlet|nestling|chick|fledgling|downy)\b", t))
    return owl and juvenile

def get_link(a):
    for k in ("cdnUrl", "cdn_url", "downloadUrl", "download_url", "modelUrl", "model_url"):
        val = a.get(k)
        if isinstance(val, str) and val.startswith("https://cdn.3dassets.dev/assets/") and val.endswith(".glb"):
            return val
    for key in ("download", "files", "model"):
        z = a.get(key)
        if isinstance(z, dict):
            got = get_link(z)
            if got:
                return got
    return None

def license_cc0(a):
    x = a.get("license")
    if isinstance(x, dict):
        x = " ".join(str(v) for v in x.values() if isinstance(v, (str,int)))
    return "cc0" in str(x).lower() or "public domain" in str(x).lower()

def glb_inspect(b):
    if len(b) < 24 or b[:4] != b"glTF":
        raise ValueError("No glTF binary magic")
    magic, version, total = struct.unpack_from("<4sII", b)
    if version != 2 or total != len(b):
        raise ValueError(f"Invalid GLB header version={version}, reported={total}, actual={len(b)}")
    off, scene = 12, None
    while off + 8 <= len(b):
        size, kind = struct.unpack_from("<I4s", b, off)
        off += 8
        if off + size > len(b):
            raise ValueError("GLB chunk overrun")
        if kind == b"JSON":
            scene = json.loads(b[off:off + size].rstrip(b" \n\r\t\x00"))
        off += size
    if scene is None or off != len(b):
        raise ValueError("GLB missing JSON or invalid chunk span")
    accessors = scene.get("accessors", [])
    meshes = scene.get("meshes", [])
    total_triangles = 0
    for mesh in meshes:
        for prim in mesh.get("primitives", []):
            if prim.get("mode", 4) != 4:
                continue
            idx = prim.get("indices")
            if isinstance(idx, int) and idx < len(accessors):
                total_triangles += accessors[idx].get("count", 0)//3
            else:
                pos = prim.get("attributes", {}).get("POSITION")
                if isinstance(pos, int) and pos < len(accessors):
                    total_triangles += accessors[pos].get("count", 0)//3
    return {"glb_bytes":len(b), "triangles":total_triangles, "mesh_count":len(meshes),
            "material_count":len(scene.get("materials", [])),
            "image_count":len(scene.get("images", [])),
            "node_count":len(scene.get("nodes", [])),
            "extensions_required":scene.get("extensionsRequired", [])}

seen={}
for index,term in enumerate(TERMS):
    url="https://3dassets.dev/api/v1/assets?" + urllib.parse.urlencode({"q":term, "limit":30})
    code,body,mime=fetch(url)
    (OUT/f"query_{index:02d}.response").write_bytes(body[:100_000])
    info={"q":term, "url":url, "http":code, "mime":mime,
          "captured_bytes":len(body), "sha256":hashlib.sha256(body).hexdigest()}
    try:
        rows=records_from(json.loads(body))
        info["row_count"]=len(rows)
        for a in rows:
            if not isinstance(a, dict):
                continue
            k=str(a.get("slug") or a.get("id") or a.get("name") or a.get("title") or "")
            if k and relevant(a):
                seen[k]=a
    except (json.JSONDecodeError, UnicodeError):
        info["json"] = "INVALID_OR_UNAVAILABLE"
    RESULT["requests"].append(info)

for j,(key,a) in enumerate(sorted(seen.items())):
    detail=a
    slug=a.get("slug")
    if isinstance(slug,str) and re.fullmatch(r"[a-zA-Z0-9_-]+",slug):
        du="https://3dassets.dev/api/v1/assets/"+urllib.parse.quote(slug)
        code,body,mime=fetch(du)
        (OUT/f"detail_{j:02d}.response").write_bytes(body[:100_000])
        if code==200:
            try:
                dd=json.loads(body)
                if isinstance(dd,dict):
                    if isinstance(dd.get("data"),dict):
                        detail=dd["data"]
                    elif isinstance(dd.get("asset"),dict):
                        detail=dd["asset"]
                    else:
                        detail=dd
            except json.JSONDecodeError: pass
    record={"id":key, "name":detail.get("name",a.get("name",a.get("title",""))),
            "slug":slug, "description":str(detail.get("description",a.get("description","")))[:600],
            "triangles_reported":detail.get("triangles"), "license":detail.get("license"),
            "url":get_link(detail), "rights_verified_cc0":license_cc0(detail) or license_cc0(a)}
    RESULT["assets_discovered"].append(record)
    if len(RESULT["downloads"]) >= 3 or not record["rights_verified_cc0"] or not record["url"]:
        record["download_status"]="SKIPPED_RIGHTS_OR_URL"
        continue
    code,b,mime=fetch(record["url"],limit=25_000_000)
    dl={"id":key,"url":record["url"],"http":code,"bytes":len(b),
        "sha256":hashlib.sha256(b).hexdigest(),"mime":mime}
    if code!=200 or len(b)>25_000_000:
        dl["status"]="ACCESS_OR_SIZE_BLOCKED"
    elif dl["sha256"] in rejected:
        dl["status"]="KNOWN_REJECTED_FINGERPRINT"
    else:
        try:
            dl["geometry"]=glb_inspect(b)
            dl["status"]="REAL_GLTF_UNREVIEWED"
            outfile=OUT/f"new_candidate_{len(RESULT['downloads'])+1:02d}_NOT_APPROVED.glb"
            outfile.write_bytes(b)
            dl["local_file"]=str(outfile)
            if dl["geometry"]["triangles"]<7000 or dl["geometry"]["image_count"]==0:
                dl["art_gate"]="REJECTED_BY_MINIMAL_STRUCTURE_OR_TEXTURE_SCREEN"
            else:
                dl["art_gate"]="VISUAL_MULTIVIEW_REVIEW_REQUIRED_NOT_RELEASED"
        except (ValueError,IndexError,KeyError,struct.error) as exc:
            dl["status"]="GLB_INVALID"
            dl["error"]=repr(exc)
    RESULT["downloads"].append(dl)
(OUT/"run187_results.json").write_text(json.dumps(RESULT,indent=2,ensure_ascii=False,default=str)+"\n")
(OUT/"NO_RELEASE.flag").write_text("Run187: free juvenile owl CC0 catalog audit only; no art or mobile acceptance.\n")
print(json.dumps({"reference_verified":RESULT["reference_actual_sha256"]==EXPECTED,
                  "queries":len(RESULT["requests"]),"juvenile_results":len(seen),
                  "downloads":[{k:d.get(k) for k in ("id","status","art_gate","bytes")} for d in RESULT["downloads"]],
                  "release":False},indent=2),flush=True)
