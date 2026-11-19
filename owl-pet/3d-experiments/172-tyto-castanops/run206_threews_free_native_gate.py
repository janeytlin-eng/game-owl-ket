#!/usr/bin/env python3
"""Run206: truly keyless no-spend text-to-3D attempt, byte-level/native multi-view QA.
No art approval, release, billing, production edits or untrusted URL execution.
"""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse
import hashlib, json, os, time, traceback
import numpy as np
import requests
from PIL import Image, ImageDraw

ROOT = Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT = ROOT / "research-evidence-run206-THREEWS-KEYLESS-TEXT3D-NO_RELEASE"
SRC = ROOT / "research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
SHA_SRC = "5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
PROMPT = ("Single realistic 3D animal sculpture of a crouching juvenile Tasmanian masked owl "
          "(Tyto castanops) with thick airy cream-white soft second-down fluff. Wide gently "
          "continuous recessed heart-shaped facial disc integrated into the fluffy head, "
          "two deep dark glossy eyes, small pale hooked bill. Very round fluffy juvenile "
          "proportions, tiny tucked wings almost invisible in its down, completely hidden tail. "
          "Belly and both feet rest naturally on a broad old eucalyptus tree-hollow lip. "
          "Soft ivory and warm buff, realistic natural fluffy feather surface, complete "
          "credible volume from every angle; no long flight feathers, no horns, no "
          "plush toy fabric, no stylized polygonal facets, no extraneous animals, "
          "no studio pedestal, no text.")
DOCS = [
 "owl-pet/AGENTS.md", "owl-pet/README.md", "owl-pet/STATUS.md",
 "owl-pet/prototype/index.html", "owl-pet/research/species/172-tyto-castanops-v3.md",
 str(ROOT / "known_rejected_asset_sha256_registry.json"),
 str(ROOT / "2026-11-19-run205b-independent-matte-native-sevenview-human-audit-ART_REJECTED-NO_RELEASE.md")
]
STATE = {"run": 206, "utc_start": datetime.now(timezone.utc).isoformat(),
         "source": "three.ws public keyless free draft POST /api/3d/generate",
         "method": "TEXT_TO_3D_NOT_SOURCE_IMAGE_CONDITIONED",
         "billing": "none; never retries 402", "cost_usd": 0,
         "art_approved": False, "true_mobile_GPU_accepted": False, "release": False,
         "prompt": PROMPT, "gate": "NO_RELEASE"}

def sha(b): return hashlib.sha256(b).hexdigest()
def dump(path,data):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2,default=str)+"\n")
def preflight():
    p={}
    for name in DOCS:
        b=Path(name).read_bytes()
        if len(b)<30: raise RuntimeError("MISSING_PREFLIGHT "+name)
        p[name]={"bytes":len(b),"sha256":sha(b)}
    b=SRC.read_bytes()
    if sha(b)!=SHA_SRC:raise RuntimeError("WRONG_RIGHTMOST_OWLET_REFERENCE")
    p[str(SRC)]={"bytes":len(b),"sha256":sha(b),"expectation":"v3 rightmost reference"}
    dump(OUT/"preflight.json",p)
    return p

def safe_json_response(r,tag):
    try: body=r.json()
    except ValueError: body={"body_excerpt":r.text[:1200]}
    dump(OUT/(tag+".json"),{"status_code":r.status_code,
          "retry_after":r.headers.get("retry-after"), "body":body})
    return body

def generate():
    # Server documents this precise endpoint as $0, keyless. No payment headers.
    url="https://three.ws/api/3d/generate"
    t=time.monotonic()
    r=requests.post(url,json={"prompt":PROMPT},
            headers={"User-Agent":"owl172-isolated-free-research/1.0"},
            timeout=(15,320))
    response=safe_json_response(r,"submit_response")
    STATE.update({"submit_status":r.status_code, "submit_seconds":round(time.monotonic()-t,2)})
    if r.status_code==402:
        STATE["gate"]="PAYMENT_REQUIRED_ABORTED_NO_SPEND"
        return None
    if r.status_code==429:
        STATE["gate"]="FREE_QUOTA_LIMIT_RETRY_LATER"
        return None
    if r.status_code>=400:
        STATE["gate"]="FREE_API_HTTP_FAILURE"
        return None
    job=response.get("job")
    if response.get("status")=="pending" and not job:
        STATE["gate"]="PENDING_MISSING_JOB_ID"
        return None
    deadline=time.monotonic()+300
    attempts=0
    while response.get("status")=="pending" and time.monotonic()<deadline:
        wait=min(max(float(response.get("retryAfter") or 4),2),25)
        time.sleep(wait)
        attempts+=1
        try:
            r=requests.get(url,params={"job":job},timeout=(15,65))
            response=safe_json_response(r,"poll_response_%02d"%attempts)
        except requests.RequestException as e:
            (OUT/("poll_transport_%02d.txt"%attempts)).write_text(repr(e))
            continue
        if r.status_code==402:STATE["gate"]="POLL_PAYMENT_REQUIRED_ABORTED";return None
        if r.status_code==429:
            # poll same job, never resubmit
            response={"status":"pending","job":job,"retryAfter":min(float(r.headers.get("retry-after") or 10),40)}
            continue
        if r.status_code>=400:
            STATE["gate"]="FREE_POLL_HTTP_FAILURE";return None
    STATE["poll_attempts"]=attempts
    STATE["final_api_status"]=response.get("status")
    if response.get("status")!="done" or not response.get("glbUrl"):
        STATE["gate"]="GENERATION_PENDING_OR_FAILED_NO_GLB"
        return None
    if response.get("free") is False or str(response.get("tier") or "draft").lower() not in ("draft","free"):
        STATE["gate"]="NOT_CONFIRMED_FREE_DRAFT";return None
    glburl=response["glbUrl"]
    parse=urlparse(glburl)
    if parse.scheme!="https" or not parse.hostname or parse.hostname in ("localhost","127.0.0.1"):
        STATE["gate"]="INVALID_EXTERNAL_GLB_URL";return None
    # Preserve the third-party output URL as trace evidence only; do not publish as approved.
    STATE["api_glb_url"]=glburl
    STATE["api_viewer_url"]=response.get("viewerUrl")
    return glburl

def download_and_inspect(url):
    import trimesh
    with requests.get(url,stream=True,timeout=(20,120)) as r:
        STATE["glb_http"]=r.status_code
        r.raise_for_status()
        data=bytearray()
        for part in r.iter_content(1024*1024):
            data.extend(part)
            if len(data)>55_000_000:raise RuntimeError("GLB_TOO_LARGE_55MB")
    raw=bytes(data)
    if len(raw)<20000 or raw[:4]!=b"glTF":raise RuntimeError("NOT_A_NATIVE_GLB")
    file=OUT/"generated_draft_raw.glb"
    file.write_bytes(raw)
    sc=trimesh.load(str(file),force="scene",process=False)
    meshes=[m for m in sc.geometry.values() if hasattr(m,"faces")]
    vcount=sum(len(m.vertices) for m in meshes)
    trcount=sum(len(m.faces) for m in meshes)
    if trcount<500:raise RuntimeError("INVALID_TINY_MESH")
    reg=json.loads((ROOT/"known_rejected_asset_sha256_registry.json").read_text())
    previously_rejected=sha(raw) in json.dumps(reg)
    metrics={"native_glb_sha256":sha(raw),"bytes":len(raw),
             "mesh_count":len(meshes),"vertices":vcount,"triangles":trcount,
             "duplicate_rejected_asset_fingerprint":previously_rejected}
    dump(OUT/"native_glb_metrics.json",metrics)
    STATE["native_glb"]=metrics
    if previously_rejected:
        STATE["gate"]="KNOWN_REJECTED_DUPLICATE"
        return
    render(file)
    STATE["gate"]="NATIVE_MULTIVIEW_RENDERED_ART_UNREVIEWED_NO_RELEASE"

def render(file):
    import vtk
    vtk.vtkObject.GlobalWarningDisplayOff()
    window=vtk.vtkRenderWindow()
    window.SetOffScreenRendering(True)
    window.SetSize(440,440)
    importer=vtk.vtkGLTFImporter()
    importer.SetFileName(str(file.resolve()))
    importer.SetRenderWindow(window)
    importer.Update()
    ren=window.GetRenderers().GetFirstRenderer()
    if ren is None:raise RuntimeError("NO_NATIVE_RENDERER")
    ren.SetBackground(.91,.91,.89)
    bb=ren.ComputeVisiblePropBounds()
    mid=np.array([(bb[0]+bb[1])/2,(bb[2]+bb[3])/2,(bb[4]+bb[5])/2])
    span=max(bb[1]-bb[0],bb[3]-bb[2],bb[5]-bb[4])
    if not 0<span<1e7 or not np.isfinite(span):raise RuntimeError("INVALID_MESH_BOUNDS")
    cameras={
       "zplus_front_world":([0,0,1],[0,1,0]),
       "zminus_back_world":([0,0,-1],[0,1,0]),
       "xminus_left_world":([-1,0,0],[0,1,0]),
       "xplus_right_world":([1,0,0],[0,1,0]),
       "yplus_top_world":([0,1,0],[0,0,-1]),
       "yminus_bottom_world":([0,-1,0],[0,0,1]),
       "quarter_xz_world":([.65,.2,1],[0,1,0])}
    allimg=[]
    for name,(v,up) in cameras.items():
        v=np.asarray(v,float);v/=np.linalg.norm(v)
        cam=ren.GetActiveCamera()
        cam.SetFocalPoint(*mid)
        cam.SetPosition(*(mid+2.7*span*v))
        cam.SetViewUp(*up)
        cam.ParallelProjectionOn()
        cam.SetParallelScale(.75*span)
        ren.ResetCameraClippingRange()
        window.Render()
        f=vtk.vtkWindowToImageFilter()
        f.SetInput(window);f.ReadFrontBufferOff();f.Update()
        out=OUT/("real_vtk_"+name+".png")
        w=vtk.vtkPNGWriter();w.SetFileName(str(out));w.SetInputConnection(f.GetOutputPort());w.Write()
        if out.stat().st_size<1500:raise RuntimeError("BLANK_RENDER_"+name)
        allimg.append((name,Image.open(out).convert("RGB").copy()))
    sheet=Image.new("RGB",(1760,940),(245,245,243))
    d=ImageDraw.Draw(sheet)
    for i,(name,im) in enumerate(allimg):
        x=i%4*440;y=i//4*465
        sheet.paste(im,(x,y+22))
        d.text((x+7,y+5),name,fill=(20,20,20))
    sheet.save(OUT/"real_native_seven_views.png")
    STATE["seven_native_world_axis_views"]=True
    STATE["anatomical_axes_calibrated"]=False

def archive():
    STATE["utc_end"]=datetime.now(timezone.utc).isoformat()
    dump(OUT/"status.json",STATE)
    inv={}
    for p in sorted(OUT.rglob("*")):
        if p.is_file() and p.name!="manifest.json":
            b=p.read_bytes()
            inv[str(p.relative_to(OUT))]={"bytes":len(b),"sha256":sha(b)}
    dump(OUT/"manifest.json",inv)
    text="# Run206: independent free/keyless TRELLIS draft GLB experiment\n\n"
    text+="Preflight: owl-pet, #172 v3, earlier Run205 art rejection and rejected asset registry.\n"
    text+="Source reference SHA256: "+SHA_SRC+" (locally verified only; not uploaded to three.ws).\n"
    text+="Free provider: https://three.ws/3d ; exact POST /api/3d/generate, no keys or payments.\n"
    text+="This is **text-to-3D**, not image-conditioned target reconstruction.\n"
    text+="Status: "+str(STATE.get("gate"))+"; technical native GLB facts: "+json.dumps(STATE.get("native_glb",{}))+".\n"
    text+="Result URLs, all 7 real VTK views, response receipts, exact hash evidence retained only in isolated expiring Actions artifact.\n"
    text+="No final human art judgement implied by successful GLB transport; no physical smartphone GPU acceptance.\n"
    text+="**NO_RELEASE, no deployment, no existing pet prototype or 251-species workflow changes.**\n"
    (ROOT/"2026-11-19-run206-threews-keyless-text3d-sourcebound-NO_RELEASE.md").write_text(text)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    try:
        preflight()
        u=generate()
        if u:download_and_inspect(u)
    except Exception as e:
        STATE["gate"]="TECHNICAL_OR_NETWORK_ERROR_NO_RELEASE"
        STATE["error"]=repr(e)
        (OUT/"traceback.txt").write_text(traceback.format_exc())
    finally:
        archive()
        print(json.dumps(STATE,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
