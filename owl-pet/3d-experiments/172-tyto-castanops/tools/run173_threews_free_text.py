#!/usr/bin/env python3
"""Run173: one real free, keyless text->3D call; never a product release.

Do not call x402, rig, paid Forge, image endpoints or rotate identities.
The generated model, if any, is a NEW independent source and must NOT be
mistaken for image-bound reconstruction of #172's rightmost concept.
"""
import hashlib
import json
import os
import re
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "research-evidence-run173-THREEWS-FREE-TEXT-NO_RELEASE"
SOURCE = ROOT / "research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
KNOWN = ROOT / "known_rejected_asset_sha256_registry.json"
EXPECTED = "5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
API = "https://three.ws"
PROMPT = (
    "A single realistic three-dimensional sculptural character of a very young Tasmanian "
    "masked owl (Tyto castanops), age-unknown fluffy mesoptile nestling. Rounded compact "
    "crouched chick with thick soft creamy ivory-white down everywhere, a broad continuous "
    "heart-shaped facial disc, two large open dark glossy eyes recessed naturally in the face, "
    "small pale beak, no ear tufts, very short wings almost hidden under down, no visible tail, "
    "two feet tucked naturally underneath. Complete anatomical side and rear silhouette, "
    "organic feather texture rather than spikes, no adult wing feathers, no plastic toy "
    "seams. One isolated full-body subject, neutral lighting, centered."
)
OUT.mkdir(parents=True, exist_ok=True)
STATE = {
    "run": 173, "started_utc": datetime.now(timezone.utc).isoformat(),
    "method": "public documented free three.ws POST /api/3d/generate",
    "generation": "text_to_3d_ONLY_NOT_SOURCE_IMAGE_BOUND",
    "prompt": PROMPT, "reference_sha256": EXPECTED,
    "free_only": True, "payment": 0, "status": "PRECHECK",
    "new_valid_glb": [], "release": False, "art": "UNREVIEWED",
    "physical_mobile_GPU": "NOT_TESTED"
}
def save():
    (OUT / "run173_actual_results.json").write_text(json.dumps(STATE, ensure_ascii=False, indent=2))
def record(kind, response):
    name = re.sub("[^a-z0-9_-]", "_", kind.lower())[:50]
    body = response.text[:60000]
    (OUT / (name + "_http.txt")).write_text("HTTP: " + str(response.status_code) +
        "\nURL: " + response.url + "\nHEADERS: " +
        json.dumps({k:v for k,v in response.headers.items() if k.lower() in
                    ("retry-after", "content-type", "server")}) + "\n\n" + body)
    return response.json() if "json" in response.headers.get("content-type", "").lower() else {}
def preflight():
    for rel in ["owl-pet/AGENTS.md", "owl-pet/README.md", "owl-pet/prototype/index.html",
                "owl-pet/research/species/172-tyto-castanops-v3.md"]:
        assert (ROOT.parents[2] / rel).is_file(), "missing preflight: " + rel
    assert SOURCE.is_file() and KNOWN.is_file(), "missing target image / registry"
    sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert sha == EXPECTED, "reference image content mismatch"
    prior = ROOT / "2026-11-18-run169-source-calibrated-vtk-native-sixview-ART_REJECTED-NO_RELEASE.md"
    assert prior.is_file() and "ART_REJECTED" in prior.read_text(), "missing art rejection"
    (OUT / "source_sha256.log").write_text(sha + "  " + str(SOURCE.relative_to(ROOT)) + "\n")
    STATE["preflight"] = "PASS"
def valid_link(u):
    p = urlparse(u)
    return p.scheme == "https" and (p.hostname == "three.ws" or
        (p.hostname or "").endswith(".r2.dev"))
def fetch_model(data):
    url = data.get("glbUrl") or data.get("glb_url")
    if not isinstance(url, str) or not valid_link(url):
        STATE["status"] = "NO_TRUSTED_GLB_URL"; return
    r = requests.get(url, timeout=100, stream=True)
    STATE["model_download_http"] = r.status_code
    if r.status_code != 200:
        STATE["status"] = "GLB_DOWNLOAD_BLOCKED"; return
    temp = OUT / "run173_source_UNREVIEWED.glb"
    n = 0
    with temp.open("wb") as f:
        for part in r.iter_content(1024 * 1024):
            n += len(part)
            if n > 32 * 1024 * 1024:
                raise ValueError("GLB exceeds 32MiB research guard")
            f.write(part)
    b = temp.read_bytes()
    sha = hashlib.sha256(b).hexdigest()
    rejected = set(re.findall(r"\b[a-fA-F0-9]{64}\b", KNOWN.read_text()))
    STATE["candidate"] = {"bytes":len(b), "sha256":sha, "source_url":url}
    if len(b)<65000 or b[:4]!=b"glTF" or sha in rejected:
        STATE["status"]="INVALID_OR_DUPLICATE";temp.unlink();return
    import trimesh
    scene = trimesh.load(str(temp), force="scene", process=False)
    count = sum(len(g.faces) for g in scene.geometry.values() if hasattr(g,"faces"))
    STATE["candidate"]["triangles"] = count
    STATE["candidate"]["meshes"] = len(scene.geometry)
    if count<600:
        STATE["status"]="TOO_SIMPLE_NATIVE_GLB";temp.unlink();return
    STATE["new_valid_glb"].append(temp.name)
    STATE["status"]="NEW_NATIVE_UNREVIEWED"
    STATE["source_provenance"]="text prompt only; NOT a #172 concept plate reconstruction"
    save()
    render_native(temp)
def render_native(path):
    import numpy as np
    import vtk
    from PIL import Image, ImageDraw
    out=OUT
    win=vtk.vtkRenderWindow()
    win.SetOffScreenRendering(1)
    win.SetSize(512,512)
    imp=vtk.vtkGLTFImporter()
    imp.SetRenderWindow(win)
    imp.SetFileName(str(path))
    imp.Update()
    ren=imp.GetRenderer()
    ren.SetBackground(.20,.21,.24)
    ren.ResetCamera()
    ac=ren.GetActors();ac.InitTraversal()
    bb=[1e9,-1e9,1e9,-1e9,1e9,-1e9];n=0
    while True:
        actor=ac.GetNextActor()
        if actor is None: break
        bounds=actor.GetBounds()
        if bounds:
            for k in range(3):
                bb[2*k]=min(bb[2*k],bounds[2*k])
                bb[2*k+1]=max(bb[2*k+1],bounds[2*k+1])
        actor.GetProperty().SetAmbient(.60)
        n+=1
    assert n and all(abs(x)<1e8 for x in bb), "invalid VTK model bounds"
    center=np.array([(bb[2*k]+bb[2*k+1])/2 for k in range(3)])
    span=max(bb[2*k+1]-bb[2*k] for k in range(3))
    assert span>0
    cam=ren.GetActiveCamera();cam.ParallelProjectionOn();cam.SetParallelScale(span*.82)
    ren.RemoveAllLights()
    light=vtk.vtkLight();light.SetLightTypeToSceneLight();ren.AddLight(light)
    labels=[("negativeZ",(0,.1,-1)),("positiveX",(1,.1,0)),
            ("positiveZ",(0,.1,1)),("negativeX",(-1,.1,0)),
            ("positiveY",(.2,1,.5)),("negativeY",(.2,-1,.5))]
    sheet=Image.new("RGB",(1536,1024),(230,230,230))
    ims=[]
    for i,(name,pos) in enumerate(labels):
        v=np.array(pos,dtype=float);v/=np.linalg.norm(v)
        cam.SetPosition(*(center+v*span*3));cam.SetFocalPoint(*center)
        cam.SetViewUp((0,0,-1) if name in ("positiveY","negativeY") else (0,1,0))
        light.SetPosition(*(center+v*span*2));light.SetFocalPoint(*center);light.SetIntensity(1.8)
        ren.ResetCameraClippingRange();win.Render()
        grab=vtk.vtkWindowToImageFilter();grab.SetInput(win)
        grab.ReadFrontBufferOff();grab.Update()
        p=out/("run173_native_"+name+"_UNREVIEWED.png")
        writer=vtk.vtkPNGWriter();writer.SetFileName(str(p))
        writer.SetInputConnection(grab.GetOutputPort());writer.Write()
        assert p.exists() and p.stat().st_size>4000
        im=Image.open(p).convert("RGB")
        sheet.paste(im,((i%3)*512,(i//3)*512))
        ims.append(p.name)
    win.Finalize()
    draw=ImageDraw.Draw(sheet)
    for i,(name,_) in enumerate(labels):
        draw.text(((i%3)*512+12,(i//3)*512+12),name+" (axes uncalibrated)",fill="red")
    sheet.save(out/"run173_native_six_axes_UNREVIEWED.png")
    STATE["native_qa"]={"renderer":"VTK "+vtk.vtkVersion.GetVTKVersion(),
        "actors":n,"axis_labels":"not anatomically calibrated",
        "images":ims,"art_review":"NOT_PASSED",
        "real_phone_gpu":"NOT_TESTED"}
    STATE["status"]="NEW_NATIVE_6VIEW_UNREVIEWED"
    save()
def main():
    preflight();save()
    s=requests.Session()
    r=s.get(API+"/api/3d",headers={"Accept":"application/json"},timeout=30)
    catalogue=record("free_api_catalog",r)
    STATE["catalogue_http"]=r.status_code
    if r.status_code!=200 or not catalogue.get("free") or not catalogue.get("keyless"):
        STATE["status"]="FREE_API_NOT_CONFIRMED";return
    STATE["status"]="SUBMIT_ONE_FREE_TEXT_GENERATION";save()
    # This is the ONLY inference POST. No paid endpoints or keys.
    resp=s.post(API+"/api/3d/generate",json={"prompt":PROMPT,"format":"glb"},
                headers={"Accept":"application/json"},timeout=120)
    body=record("generation_submit",resp)
    STATE["submit_http"]=resp.status_code
    if resp.status_code!=200:
        STATE["status"]="PROVIDER_HTTP_"+str(resp.status_code);return
    deadline=time.monotonic()+320
    for i in range(32):
        status=body.get("status")
        STATE["last_response_status"]=status
        STATE["polls"]=i
        save()
        if status in ("done","completed"):
            fetch_model(body);return
        if status in ("error","failed","cancelled"):
            STATE["status"]="UPSTREAM_ERROR"; STATE["provider_error"]=str(body.get("error",""))[:800];return
        if status not in ("pending","queued","processing"):
            STATE["status"]="UNRECOGNIZED_RESPONSE";return
        poll=body.get("poll")
        if not isinstance(poll,str) or not poll.startswith("/api/3d/generate?"):
            STATE["status"]="UNSAFE_POLL_URL";return
        if time.monotonic()>deadline:
            STATE["status"]="POLL_DEADLINE";return
        delay=max(3,min(30,int(body.get("retryAfter") or 6)))
        time.sleep(delay)
        rr=s.get(API+poll,headers={"Accept":"application/json"},timeout=60)
        body=record("generation_poll_"+str(i+1),rr)
        STATE["poll_http"]=rr.status_code
        if rr.status_code!=200:
            STATE["status"]="POLL_HTTP_"+str(rr.status_code);return
    STATE["status"]="POLL_ATTEMPT_LIMIT"
if __name__=="__main__":
    try: main()
    except Exception as e:
        STATE["status"]="ERROR_UNREVIEWED"
        STATE["exception"]=repr(e)
        (OUT/"run173_exception.txt").write_text(traceback.format_exc())
        print("EXCEPTION",repr(e),flush=True)
    finally:
        STATE["completed_utc"]=datetime.now(timezone.utc).isoformat()
        save()
        (OUT/"NO_RELEASE.flag").write_text("Run173 NO_RELEASE: no art approval; no real phone WebGL GPU validation; no purchases; no deployment.\n")
        manifest={p.name:{"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
          for p in OUT.iterdir() if p.is_file() and p.name!="run173_sha256_manifest.json"}
        (OUT/"run173_sha256_manifest.json").write_text(json.dumps(manifest,indent=2))
        assert all(hashlib.sha256((OUT/k).read_bytes()).hexdigest()==v["sha256"]
                   for k,v in manifest.items())
        print("RUN173_FINAL",STATE["status"],"new_glbs",len(STATE["new_valid_glb"]),
              "evidence",len(manifest),flush=True)
