#!/usr/bin/env python3
"""Run307: independent, real GLB/provenance audit of a CC0 adult owl as anatomy reference ONLY.
No conversion to a Tyto castanops chick, no model release, no payments.
"""
import hashlib, json, pathlib, traceback, urllib.request
from datetime import datetime, timezone

OUT=pathlib.Path("owl172-run307-evidence/cc0-adult-anatomy-reference")
OUT.mkdir(parents=True, exist_ok=True)
manifest_url="https://grab3d.com/dl/owl/manifest.json"
license_url="https://grab3d.com/dl/owl/LICENSE.txt"
glb_url="https://grab3d.com/dl/owl/owl-light.glb"
report={"run":307,"checked_utc":datetime.now(timezone.utc).isoformat(),
        "source":"Grab3D adult GREAT HORNED owl, not Tyto castanops or a chick",
        "license_claim":"CC0 1.0 on provider manifest, not independently adjudicated",
        "provider_origins":"AI assisted (Meshy plus Blender cleanup), check exact manifest",
        "urls":{"manifest":manifest_url,"license":license_url,"glb":glb_url},
        "model_downloaded":False,"glb_reimported":False,
        "reference_only":True,"juvenile_design_pass":False,
        "mobile_pass":False,"release_allowed":False,"paid_usd":0,"errors":[]}

def read_url(url, max_bytes):
    req=urllib.request.Request(url,headers={"User-Agent":"OwlResearchAudit/1.0 noncommercial-research","Accept":"*/*"})
    with urllib.request.urlopen(req,timeout=120) as response:
        mime=response.headers.get("content-type","")
        data=response.read(max_bytes+1)
        if len(data)>max_bytes:
            raise ValueError("oversized response, refused")
        return data,mime

try:
    m,mt=read_url(manifest_url,500000)
    manifest=json.loads(m.decode("utf-8"));(OUT/"manifest.json").write_bytes(m)
    report["manifest"]={"slug":manifest.get("slug"),"origin":manifest.get("origin"),
        "claimed_license":manifest.get("extras",{}).get("license"),
        "declared_triangles_light":manifest.get("triangles_light"),
        "declared_light_glb_bytes":manifest.get("files",{}).get("glb_light",{}).get("bytes")}
    assert report["manifest"]["claimed_license"]=="CC0-1.0"
    try:
        lic,_=read_url(license_url,100000);(OUT/"LICENSE.txt").write_bytes(lic)
        report["license_document_saved"]=True
    except Exception as ex: report["errors"].append("LICENSE_FETCH "+str(ex)[:240])
    glb,ct=read_url(glb_url,45000000)
    if glb[:4]!=b"glTF" or len(glb)<100:
        raise ValueError("GLB request returned no binary glTF (mime="+ct+")")
    path=OUT/"adult-source-NOT_A_CHICK.glb";path.write_bytes(glb)
    report["model_downloaded"]=True
    report["glb"]={"bytes":len(glb),"sha256":hashlib.sha256(glb).hexdigest(),"content_type":ct}
    if report["manifest"]["declared_light_glb_bytes"]:
        report["glb"]["byte_size_matches_provider"]=len(glb)==report["manifest"]["declared_light_glb_bytes"]
    import trimesh
    scene=trimesh.load(path,force="scene")
    geo=list(scene.geometry.values())
    tris=sum(len(g.faces) for g in geo)
    visuals={str(g.visual.kind):sum(1 for h in geo if h.visual.kind==g.visual.kind) for g in geo}
    report["reimport"]={"geometry_count":len(geo),"triangles":tris,
        "vertices":sum(len(g.vertices) for g in geo),
        "visual_types":visuals,"material_names":[str(getattr(getattr(g.visual,"material",None),"name",""))[:50] for g in geo][:20],
        "scene_bounds":scene.bounds.tolist()}
    report["glb_reimported"]=tris>1000 and len(geo)>0
    report["mobile_preflight_40k_tri_budget"]=tris<=40000
    report["art_rejection_reasons"]=[
        "Source is an adult great horned owl with ear tufts and yellow eyes, not Tasmanian masked owl",
        "Adult wing and long tail feathers contradict compact mesoptile down-buried wings and concealed tail",
        "Not shaped as a cream-white fluffy chick with a natural broad Tyto heart face",
        "Source is reference-only; authorisation/provenance are not sufficient to claim reference-conditioned derivative",
        "Real physical iPhone/Android WebGL2 benchmark not performed"]
except Exception as ex:
    report["errors"].append(type(ex).__name__+": "+str(ex)[:500])
    report["traceback_tail"]=traceback.format_exc()[-1600:]
finally:
    (OUT/"audit.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
    print(json.dumps({k:v for k,v in report.items() if k in ("model_downloaded","glb_reimported","glb","reimport","errors","mobile_preflight_40k_tri_budget","release_allowed")},indent=2))
