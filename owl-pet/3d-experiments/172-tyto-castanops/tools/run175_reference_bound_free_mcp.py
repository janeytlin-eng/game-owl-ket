#!/usr/bin/env python3
"""Run175: one real no-fee image-conditioned three.ws MCP studio mesh, audit only.

Never use payment endpoints, alternate quota identities, screenshots of a viewer
as a GLB, or previous rejected meshes. The output is UNREVIEWED by construction.
"""
import hashlib
import json
import os
import re
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "research-evidence-run175-FREE-MCP-IMAGE-BOUND-NO_RELEASE"
SOURCE = ROOT / "research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
KNOWN = ROOT / "known_rejected_asset_sha256_registry.json"
EXPECTED = "5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
BRANCH = "research/owl172-run175-reference-bound-free-mcp-native-qa"
SRC_URL = ("https://raw.githubusercontent.com/janeytlin-eng/game-owl-ket/" + BRANCH + 
    "/owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png")
MCP = "https://three.ws/api/mcp-studio"  # official documented keyless, NON-x402 route
PROMPT = (
    "Use the supplied actual target image, rightmost owl chick ONLY. Reconstruct this "
    "single young cream-white Tasmanian masked owl (Tyto castanops) with a broad organically "
    "integrated heart-shaped face, recessed dark eyes, tiny pale bill, very dense silky "
    "cream-white soft down, round compact juvenile body, short wings buried under down, "
    "concealed tail, well-formed naturally rounded side and back, tucked feet and eucalypt "
    "hollow lip under feet. Full 3D model, continuous anatomy, no adult stiff flight "
    "feathers, no spikes, no toy sphere eyeballs, no disconnected pieces, no 2D cutout, "
    "no other birds, no text."
)
KEY = "owl172-run175-rightmost-cream-mesoptile-20261118-v1"
OUT.mkdir(parents=True, exist_ok=True)
STATE = {
    "run":175, "utc_started":datetime.now(timezone.utc).isoformat(),
    "provider":"official https://three.ws/api/mcp-studio", "tool":"mesh_forge",
    "source_image_url":SRC_URL, "expected_reference_sha256":EXPECTED,
    "method":"image_url + optional art direction, never text-only substitution",
    "idempotency_key":KEY, "payment_usd":0, "status":"PRECHECK", 
    "new_glb_count":0, "native_render":"NOT_EXECUTED",
    "art_review":"NOT_PASSED", "physical_phone_gpu":"NOT_TESTED",
    "release":False
}
def save():
    (OUT/"run175_actual_results.json").write_text(json.dumps(STATE,indent=2,ensure_ascii=False))
def preflight():
    for relative in ("owl-pet/AGENTS.md", "owl-pet/README.md", 
                     "owl-pet/prototype/index.html", 
                     "owl-pet/research/species/172-tyto-castanops-v3.md"):
        assert (ROOT.parents[2]/relative).is_file(), relative
    assert SOURCE.is_file() and KNOWN.is_file()
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == EXPECTED, "SOURCE_MISMATCH"
    old = ROOT/"2026-11-18-run169-source-calibrated-vtk-native-sixview-ART_REJECTED-NO_RELEASE.md"
    assert old.exists() and "ART_REJECTED" in old.read_text()
    (OUT/"local_reference_sha256.txt").write_text(EXPECTED+" "+str(SOURCE.relative_to(ROOT))+"\n")
    STATE["preflight"] = "PASS"
    save()
def rpc(session, method, params=None, index=1, label=""):
    payload={"jsonrpc":"2.0","id":index,"method":method}
    if params is not None: payload["params"]=params
    r=session.post(MCP,json=payload,timeout=(20,75),
        headers={"Accept":"application/json","Content-Type":"application/json",
                 "MCP-Protocol-Version":"2025-06-18"})
    record={"http":r.status_code,"content_type":r.headers.get("content-type",""),
            "response":r.text[:90000]}
    (OUT/("mcp_"+(label or method.replace("/","_"))+".json")).write_text(
        json.dumps(record,indent=2,ensure_ascii=False))
    if r.status_code!=200: raise RuntimeError("MCP_HTTP_"+str(r.status_code))
    if "json" not in r.headers.get("content-type","").lower():
        raise RuntimeError("MCP_NOT_JSON")
    z=r.json()
    if "error" in z:raise RuntimeError("MCP_RPC_ERROR_"+str(z["error"])[:800])
    return z.get("result",{})
def structured(result):
    s=result.get("structuredContent",{})
    if isinstance(s,dict) and s: return s
    for x in result.get("content",[]):
        if x.get("type")=="text":
            t=x.get("text","")
            try:
                z=json.loads(t)
                if isinstance(z,dict):return z
            except ValueError:pass
    return {}
def make_native_sheet(file):
    import vtk
    from PIL import Image,ImageDraw
    import numpy as np
    renwin=vtk.vtkRenderWindow();renwin.SetOffScreenRendering(1)
    renwin.SetSize(480,480)
    imp=vtk.vtkGLTFImporter();imp.SetRenderWindow(renwin);imp.SetFileName(str(file))
    imp.Update();ren=imp.GetRenderer()
    ren.SetBackground(.17,.20,.24)
    actors=ren.GetActors();actors.InitTraversal()
    bounds=[1e9,-1e9,1e9,-1e9,1e9,-1e9];num=0
    while True:
        actor=actors.GetNextActor()
        if actor is None: break
        b=actor.GetBounds()
        if b:
            num+=1
            for i in range(3):
                bounds[2*i]=min(bounds[2*i],b[2*i])
                bounds[2*i+1]=max(bounds[2*i+1],b[2*i+1])
            actor.GetProperty().SetAmbient(.62)
    assert num>0 and max(abs(x) for x in bounds)<1e8
    center=np.array([(bounds[2*i]+bounds[2*i+1])/2 for i in range(3)])
    span=max(bounds[2*i+1]-bounds[2*i] for i in range(3))
    assert span>0
    ren.RemoveAllLights()
    light=vtk.vtkLight();light.SetLightTypeToSceneLight();ren.AddLight(light)
    camera=ren.GetActiveCamera();camera.ParallelProjectionOn()
    camera.SetParallelScale(span*.82)
    axes=[("-Z",(0,.1,-1)),("+X",(1,.1,0)),("+Z",(0,.1,1)),("-X",(-1,.1,0)),
          ("+Y",(.1,1,.4)),("-Y",(.1,-1,.4))]
    sheet=Image.new("RGB",(1440,960),(235,235,235))
    for i,(name,vec) in enumerate(axes):
        v=np.array(vec,dtype=float);v/=np.linalg.norm(v)
        camera.SetPosition(*(center+v*span*3));camera.SetFocalPoint(*center)
        camera.SetViewUp((0,0,-1) if name in ("+Y","-Y") else (0,1,0))
        light.SetPosition(*(center+v*span*2));light.SetFocalPoint(*center)
        light.SetIntensity(1.8)
        ren.ResetCameraClippingRange();renwin.Render()
        grab=vtk.vtkWindowToImageFilter()
        grab.SetInput(renwin);grab.ReadFrontBufferOff();grab.Update()
        w=vtk.vtkPNGWriter()
        p=OUT/("run175_native_axis_"+name.replace("+","p").replace("-","m")+".png")
        w.SetInputConnection(grab.GetOutputPort());w.SetFileName(str(p));w.Write()
        assert p.stat().st_size>3000
        sheet.paste(Image.open(p).convert("RGB"),((i%3)*480,(i//3)*480))
    d=ImageDraw.Draw(sheet)
    for i,(label,_) in enumerate(axes):
        d.text(((i%3)*480+12,(i//3)*480+12),label+" (not anatomically calibrated)",fill="red")
    sheet.save(OUT/"run175_native_sixaxis_UNREVIEWED.png")
    renwin.Finalize()
    STATE["native_render"]="VTK "+vtk.vtkVersion.GetVTKVersion()
    STATE["render_axes"]="six geometry axes; anatomical front uncalibrated"
    STATE["native_actor_count"]=num
    STATE["status"]="NATIVE_SIX_AXIS_READY_FOR_ART_REVIEW"
    save()
def capture_model(result,session):
    s=structured(result)
    if result.get("isError"):
        STATE["status"]="PROVIDER_TOOL_ERROR";STATE["error"]=str(s or result.get("content",[]))[:1500];return
    model=s.get("glbUrl") or s.get("glb_url")
    if not model:
        STATE["status"]="NO_NATIVE_MODEL_IN_SUCCESS_RESPONSE"
        STATE["response_shape"]=list(s.keys())
        return
    p=urlparse(model)
    assert p.scheme=="https" and (
        p.hostname=="three.ws" or p.hostname.endswith(".three.ws")
        or p.hostname.endswith(".r2.dev")), "untrusted_glb_host"
    response=session.get(model,timeout=(15,150),stream=True)
    STATE["glb_download_http"]=response.status_code
    if response.status_code!=200: STATE["status"]="MODEL_HTTP_ERROR";return
    filename=OUT/"run175_image_bound_UNREVIEWED.glb"
    size=0
    with filename.open("wb") as f:
        for block in response.iter_content(1<<20):
            size+=len(block)
            if size>32*1024*1024:raise RuntimeError("GLB_TOO_LARGE")
            f.write(block)
    data=filename.read_bytes()
    sha=hashlib.sha256(data).hexdigest()
    prev=set(re.findall(r"\b[0-9a-fA-F]{64}\b",KNOWN.read_text()))
    STATE["candidate"]={"bytes":size,"sha256":sha,"glb_url":model,
        "viewer_url":s.get("viewerUrl") or s.get("viewer_url"),
        "poster_url":s.get("poster_png_url")}
    if size<65000 or data[:4]!=b"glTF" or sha in prev:
        STATE["status"]="INVALID_OR_PREVIOUSLY_REJECTED_GLB";filename.unlink();return
    import trimesh
    scene=trimesh.load(str(filename),force="scene",process=False)
    triangles=sum(len(g.faces) for g in scene.geometry.values() if hasattr(g,"faces"))
    STATE["candidate"].update({"triangle_count":triangles,
                               "mesh_count":len(scene.geometry)})
    if triangles<1000:
        STATE["status"]="MODEL_TOO_SIMPLE";filename.unlink();return
    STATE["new_glb_count"]=1
    STATE["status"]="NATIVE_NEW_GLB_UNREVIEWED"
    save()
    try:
        make_native_sheet(filename)
    except Exception as e:
        STATE["native_render"]="FAILED_"+repr(e)
        (OUT/"render_exception.txt").write_text(traceback.format_exc())
        STATE["status"]="GLB_VALID_RENDER_FAILED"
def main():
    preflight()
    ses=requests.Session()
    src=ses.get(SRC_URL,timeout=(15,60))
    STATE["source_fetch_http"]=src.status_code
    if src.status_code!=200:
        STATE["status"]="PUBLIC_IMAGE_NOT_AVAILABLE";return
    STATE["remote_image_sha256"]=hashlib.sha256(src.content).hexdigest()
    if STATE["remote_image_sha256"]!=EXPECTED:
        STATE["status"]="REMOTE_IMAGE_HASH_MISMATCH";return
    STATE["remote_reference_pass"]=True;save()
    listing=rpc(ses,"tools/list",index=1,label="tools_list")
    tools={x.get("name"):x for x in listing.get("tools",[])}
    if "mesh_forge" not in tools:
        STATE["status"]="FREE_IMAGE_TOOL_NOT_LISTED";return
    properties=tools["mesh_forge"].get("inputSchema",{}).get("properties",{})
    if "image_url" not in properties:
        STATE["status"]="IMAGE_FIELD_NOT_ACCEPTED";return
    STATE["mcp_free_tool_count"]=len(tools)
    STATE["mcp_preflight"]="PASS";save()
    # Exactly one model generation; stable key avoids duplicate generation on retries.
    response=rpc(ses,"tools/call",{"name":"mesh_forge","arguments":{
        "image_url":SRC_URL,"prompt":PROMPT,"idempotency_key":KEY}},index=2,label="mesh_forge_one")
    data=structured(response)
    STATE["initial_result_keys"]=list(data.keys())
    STATE["initial_provider_status"]=data.get("status")
    save()
    job=data.get("jobId") or data.get("job_id")
    if data.get("status")=="pending" and not job:
        STATE["status"]="PENDING_NO_JOB_ID";return
    for i in range(12):
        if data.get("status")!="pending":break
        delay=min(40,max(10,int(data.get("etaRemainingSeconds") or 24)))
        time.sleep(delay)
        response=rpc(ses,"tools/call",{"name":"check_job","arguments":{"job_id":job}},
            index=3+i,label="check_job_"+str(i+1))
        data=structured(response)
        STATE["last_poll"]={"i":i+1,"status":data.get("status"),
            "retryable":data.get("retryable",False)}
        save()
    if data.get("status")=="pending":
        STATE["status"]="PENDING_AFTER_BOUNDED_POLLS";return
    if data.get("status") in ("failed","error","unknown"):
        STATE["status"]="UPSTREAM_"+str(data.get("status"))
        STATE["provider_error"]=str(data.get("message") or data.get("reason") or data.get("error"))[:800]
        return
    capture_model(response,ses)
if __name__=="__main__":
    try:
        main()
    except Exception as ex:
        STATE["status"]="ERROR_UNREVIEWED"
        STATE["exception"]=repr(ex)
        (OUT/"exception_traceback.txt").write_text(traceback.format_exc())
        print("ERROR",repr(ex),flush=True)
    finally:
        STATE["utc_finished"]=datetime.now(timezone.utc).isoformat()
        save()
        (OUT/"NO_RELEASE.flag").write_text("NO_RELEASE; candidate is unreviewed; no real phone GPU; zero fees, no product deployment.\n")
        manifest={f.name:{"bytes":f.stat().st_size,
            "sha256":hashlib.sha256(f.read_bytes()).hexdigest()}
            for f in OUT.iterdir() if f.is_file() and f.name!="sha256_manifest.json"}
        (OUT/"sha256_manifest.json").write_text(json.dumps(manifest,indent=2))
        assert all(hashlib.sha256((OUT/k).read_bytes()).hexdigest()==v["sha256"]
                for k,v in manifest.items())
        print("RUN175_FINAL",STATE["status"],"new_GLB",STATE["new_glb_count"],
              "evidence",len(manifest),flush=True)
