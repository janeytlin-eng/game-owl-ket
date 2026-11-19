#!/usr/bin/env python3
"""Run201: actual anonymous zero-fee public Gradio image-to-3D test; never releases art."""
from __future__ import annotations
import hashlib, json, os, time, traceback, urllib.parse
from pathlib import Path
import requests

ROOT = Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT = ROOT / "research-evidence-run201-PUBLIC-ZEROGPU-SOURCEBOUND-NO_RELEASE"
SOURCE = ROOT / "research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
KNOWN = ROOT / "known_rejected_asset_sha256_registry.json"
EXPECTED = "5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
SPACE = "linoyts/sketch-to-3d"
APP = "https://linoyts-sketch-to-3d.hf.space"
OUT.mkdir(parents=True, exist_ok=True)
data = {
    "space": SPACE, "app": APP,
    "input_path": str(SOURCE), "reference_sha256_expected": EXPECTED,
    "reference_sha256_actual": None, "source_upload": False,
    "public_app_config_http": None, "public_app_config_api": [],
    "gradio_api_names": [], "inference_submitted": False,
    "inference_completed": False, "extract_submitted": False,
    "new_native_glb": False, "geometry": {}, "sevenview": False,
    "art_approved": False, "physical_mobile_gpu_tested": False,
    "no_extra_paid_service": True, "final_status": "NO_NEW_GLB_NO_RELEASE",
    "events": [], "errors": [],
}
def event(step, **details):
    obj = {"step":step, "time_utc":__import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(), **details}
    data["events"].append(obj)
    print(json.dumps(obj, ensure_ascii=False), flush=True)
    dump()

def dump():
    (OUT/"run201_status.json").write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str)+"\n")
    (OUT/"NO_RELEASE.flag").write_text("NO_RELEASE: no approved juvenile or physical phone GPU verification.\n")

def digest(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def render_native_sevenview(glb: Path):
    import numpy as np, trimesh
    import vtk
    loaded = trimesh.load(glb, force="scene", process=False)
    meshes = loaded.dump()
    if not isinstance(meshes, (list, tuple)): meshes = [meshes]
    meshes = [m for m in meshes if isinstance(m, trimesh.Trimesh) and len(m.faces)]
    if not meshes: raise ValueError("GLB contained no triangle meshes")
    tri = sum(len(m.faces) for m in meshes)
    vertex = sum(len(m.vertices) for m in meshes)
    data["geometry"] = {"triangles":tri, "vertices":vertex, "mesh_count":len(meshes),
                         "triangles_mobile_provisional_limit":20000,
                         "provisional_geometry_under_limit":tri<=20000}
    merged = trimesh.util.concatenate(meshes)
    pts = np.asarray(merged.vertices)
    center = (pts.max(axis=0)+pts.min(axis=0))/2
    radius = float(max(pts.max(axis=0)-pts.min(axis=0)))*1.9
    if radius<=0: raise ValueError("Degenerate GLB bounding box")
    poly = vtk.vtkPolyData()
    vpts=vtk.vtkPoints()
    vpts.SetNumberOfPoints(len(pts))
    for i,p in enumerate(pts): vpts.SetPoint(i,float(p[0]),float(p[1]),float(p[2]))
    poly.SetPoints(vpts)
    cells=vtk.vtkCellArray()
    for face in np.asarray(merged.faces):
        cells.InsertNextCell(3)
        for idx in face: cells.InsertCellPoint(int(idx))
    poly.SetPolys(cells)
    normals=vtk.vtkPolyDataNormals()
    normals.SetInputData(poly)
    normals.ConsistencyOn()
    normals.Update()
    mapper=vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(normals.GetOutputPort())
    actor=vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0.86,0.85,0.82)
    actor.GetProperty().SetInterpolationToPhong()
    render=vtk.vtkRenderer()
    render.AddActor(actor)
    render.SetBackground(0.21,0.23,0.25)
    win=vtk.vtkRenderWindow()
    win.SetOffScreenRendering(1)
    win.SetSize(640,640)
    win.AddRenderer(render)
    cam=render.GetActiveCamera()
    cam.SetViewUp(0,1,0)
    # Diagnostic only: coordinate orientation is uncalibrated without sculpt metadata.
    dirs={"front":(0,0,1), "right":(1,0,0), "back":(0,0,-1),
          "left":(-1,0,0), "top":(0,1,0), "bottom":(0,-1,0), "quarter":(1,0,1)}
    results=[]
    for label, vec in dirs.items():
        d=np.asarray(vec,dtype=float);d=d/np.linalg.norm(d)
        if label in ("top","bottom"): cam.SetViewUp(0,0,-1 if label=="top" else 1)
        else: cam.SetViewUp(0,1,0)
        cam.SetFocalPoint(*[float(v) for v in center])
        cam.SetPosition(*[float(v) for v in center+d*radius])
        cam.SetClippingRange(0.01,radius*6)
        render.ResetCameraClippingRange()
        win.Render()
        filt=vtk.vtkWindowToImageFilter();filt.SetInput(win);filt.Update()
        writer=vtk.vtkPNGWriter()
        filepath=OUT/("native_geometry_"+label+".png")
        writer.SetFileName(str(filepath))
        writer.SetInputConnection(filt.GetOutputPort());writer.Write()
        if filepath.exists() and filepath.stat().st_size>500: results.append(label)
    win.Finalize()
    data["sevenview"]=len(results)==7
    data["geometry"]["rendered_views"]=results
    return data["sevenview"]

def is_rejected(sha: str):
    # Only use registry for deduplication; never infer art success from absence.
    if not KNOWN.exists(): return False
    return sha.lower() in KNOWN.read_text().lower()

def inspect_native(path: Path):
    header=path.read_bytes()[:12]
    if header[:4]!=b"glTF" or len(header)<12:
        raise ValueError("Generated artifact is not GLB magic")
    n=int.from_bytes(header[8:12],"little")
    if n!=path.stat().st_size:
        raise ValueError("GLB declared length mismatch")
    sha=digest(path)
    data["native_sha256"]=sha
    data["native_bytes"]=path.stat().st_size
    data["already_rejected_fingerprint"]=is_rejected(sha)
    if data["already_rejected_fingerprint"]:
        data["final_status"]="KNOWN_REJECTED_GLB_NO_RELEASE";return
    data["new_native_glb"]=True
    data["sevenview"]=render_native_sevenview(path)
    data["final_status"]="NEW_NATIVE_GLB_PENDING_HUMAN_ART_REVIEW_NO_RELEASE"
    event("native_glb_inspected",sha256=sha,bytes=path.stat().st_size,
          geometry=data["geometry"],sevenview=data["sevenview"])

def download_output_file(obj):
    """Accept only approved HF-hosted generated GLB URLs or a local Gradio client cache file."""
    paths=[]
    def walk(v):
        if isinstance(v,str):
            if v.endswith(".glb") or ".glb?" in v: paths.append(v)
        elif isinstance(v,dict):
            for w in v.values():walk(w)
        elif isinstance(v,(tuple,list)):
            for w in v:walk(w)
    walk(obj)
    for p in paths:
        if p.startswith("http"):
            host=urllib.parse.urlparse(p).hostname or ""
            if not (host.endswith(".hf.space") or host.endswith(".huggingface.co")):
                raise ValueError("Non HF GLB host is not on allowlist: "+host)
            response=requests.get(p,timeout=45)
            response.raise_for_status()
            raw=response.content
            if raw[:4]!=b"glTF":continue
            dest=Path("/tmp/run201-native-generated.glb")
            dest.write_bytes(raw);return dest
        elif os.path.exists(p):
            dest=Path(p)
            if dest.read_bytes()[:4]==b"glTF":return dest
    return None

def main():
    assert SOURCE.is_file(),"Expected exact pinned v3 rightmost source missing"
    data["reference_sha256_actual"]=digest(SOURCE)
    assert data["reference_sha256_actual"]==EXPECTED,"Wrong or missing pinned reference"
    assert KNOWN.is_file(), "Negative registry missing"
    event("source_integrity_confirmed", sha256=EXPECTED)
    try:
        r=requests.get(APP+"/config",timeout=25)
        data["public_app_config_http"]=r.status_code
        if r.ok:
            cfg=r.json()
            data["public_app_config_api"]=[{"api_name":d.get("api_name"),
                "id":d.get("id"), "inputs":d.get("inputs")} for d in cfg.get("dependencies",[])
                if isinstance(d,dict) and d.get("api_name")]
            (OUT/"public_gradio_config_summary.json").write_text(json.dumps({
                "version":cfg.get("version"),"dependencies":data["public_app_config_api"]},indent=2))
        event("public_config_request",http_status=r.status_code,content_type=r.headers.get("content-type"))
    except Exception as exc:
        data["errors"].append("public_config: "+repr(exc))
    from gradio_client import Client, handle_file
    # This is an actual original-image upload to a free public Space, not fake inference.
    client=Client(SPACE, verbose=False)
    endpoint_names=[ep.api_name for ep in client.endpoints.values() if ep.api_name]
    data["gradio_api_names"]=sorted(set(endpoint_names))
    (OUT/"public_endpoints.txt").write_text("\n".join(data["gradio_api_names"])+"\n")
    event("public_endpoints_discovered",endpoints=data["gradio_api_names"])
    exact=[n for n in data["gradio_api_names"] if n.strip("/")=="image_to_3d"]
    if not exact:
        data["final_status"]="NO_PUBLIC_SOURCEBOUND_IMAGE_TO_3D_API_NO_RELEASE"
        return
    # The ImageSlider API accepts a pair [before image, after image]. Both are the EXACT pinned reference.
    # Do not use a separate synthetic sketch/image instead of the original v3 source.
    pair=[handle_file(str(SOURCE)),handle_file(str(SOURCE))]
    endpoint=exact[0]
    event("submitting_original_image_to_public_zero_gpu",endpoint=endpoint)
    try:
        job=client.submit(pair, [], False, 42, 7.5, 12, 3.0, 12, "stochastic", api_name=endpoint)
        data["inference_submitted"]=True
        event("actual_inference_job_submitted",endpoint=endpoint)
    except Exception as exc:
        data["errors"].append("submit: "+repr(exc))
        data["final_status"]="PUBLIC_API_REJECTED_INPUT_OR_QUOTA_NO_RELEASE"
        return
    deadline=time.monotonic()+240
    while not job.done() and time.monotonic()<deadline:
        time.sleep(4)
    if not job.done():
        data["final_status"]="PUBLIC_QUEUE_TIMEOUT_NO_RELEASE"
        event("inference_queue_timeout",seconds=240)
        return
    try:
        result=job.result()
        data["inference_completed"]=True
        event("inference_output_received",result_type=type(result).__name__)
    except Exception as exc:
        data["errors"].append("inference: "+repr(exc))
        data["final_status"]="REMOTE_INFERENCE_ERROR_NO_RELEASE"
        return
    extract=[n for n in data["gradio_api_names"] if n.strip("/")=="extract_glb"]
    if not extract:
        data["final_status"]="NO_PUBLIC_GLTF_EXTRACTION_API_NO_RELEASE";return
    try:
        state=result[0] if isinstance(result,(tuple,list)) and result else None
        event("submit_glb_extraction",state_type=type(state).__name__)
        extract_job=client.submit(state,0.95,1024,api_name=extract[0])
        data["extract_submitted"]=True
        deadline=time.monotonic()+145
        while not extract_job.done() and time.monotonic()<deadline:
            time.sleep(3)
        if not extract_job.done():
            data["final_status"]="PUBLIC_EXTRACTION_QUEUE_TIMEOUT_NO_RELEASE";return
        extraction=extract_job.result()
        event("extraction_output_received",result_type=type(extraction).__name__)
        glb=download_output_file(extraction)
        if not glb:
            data["final_status"]="REMOTE_EXTRACTION_NO_DOWNLOADABLE_GLB_NO_RELEASE";return
        inspect_native(glb)
        try:glb.unlink()
        except Exception:pass
    except Exception as exc:
        data["errors"].append("extract: "+repr(exc))
        data["final_status"]="REMOTE_EXTRACTION_ERROR_NO_RELEASE"

if __name__=="__main__":
    try: main()
    except Exception as exc:
        data["errors"].append(repr(exc))
        data["traceback_tail"]=traceback.format_exc()[-4000:]
        data["final_status"]="RUNNER_OR_TRANSPORT_ERROR_NO_RELEASE"
        event("exception",error=repr(exc))
    finally:
        dump()
        print("RUN201_FINAL",data["final_status"],"NO_RELEASE",flush=True)
