#!/usr/bin/env python3
"""Run231: actual public CC0-claimed true-3D donor qualification, NO RELEASE.
A third-party generic owl is never presumed #172 Tyto castanops mesoptile.
Acquire only the public Download GLB URL explicitly shown on the provider's
public page. Verify nondegenerate native GLB and render actual spatial cameras.
Never substitute SVG/2D rotation, never certify mobile GPU from desktop tests.
"""
import datetime, hashlib, json, math, struct, subprocess, traceback
from pathlib import Path
import numpy as np
import requests
import trimesh
from PIL import Image, ImageDraw
import vtk
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray

ROOT = Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT = ROOT / "run231-evidence"
OUT.mkdir(parents=True, exist_ok=True)
PUBLIC_INFO = "https://www.innerscene.com/tools/library/3d-parts/owl-d696472a"
PUBLIC_BINARY = "https://www.innerscene.com/api/library/owl-d696472a/download"
REF = Path("owl-pet/design/concepts/172-tyto-castanops-v3.png")
KNOWN_REF_SHA = "881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
R = {
    "run": 231,
    "date_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "candidate_url": PUBLIC_INFO, "download_url": PUBLIC_BINARY,
    "license_as_advertised_on_public_page": "CC0, not independently authenticated",
    "target": "#172 Tyto castanops v3 RIGHTMOST AGE-UNKNOWN cream down mesoptile",
    "status": "NOT_STARTED", "art_approved": False, "release": "NO_RELEASE",
    "phone_webgl": "NOT_TESTED", "extra_paid_usd": 0,
    "limitation": "The candidate is generic Owl, not asserted juvenile or correct species. No art approval without manual all-view evaluation."
}
def dig(p):
    b = Path(p).read_bytes()
    return {"bytes":len(b), "sha256":hashlib.sha256(b).hexdigest()}
def inspect_glb(p):
    with p.open("rb") as f:
        h = f.read(20)
        if len(h) != 20: raise ValueError("GLB header truncated")
        magic,ver,total,jslen,chunktype = struct.unpack("<4sIIII",h)
        if magic != b"glTF" or ver != 2 or total != p.stat().st_size or chunktype != 0x4e4f534a:
            raise ValueError("Not a valid complete glTF 2.0 binary")
        d = json.loads(f.read(jslen).decode("utf-8"))
    return {"extensionsRequired":d.get("extensionsRequired",[]),
            "meshes":len(d.get("meshes",[])),"materials":len(d.get("materials",[])),
            "images":len(d.get("images",[])),"nodes":len(d.get("nodes",[]))}
def fetch_binary():
    # Download is a literal publicly advertised link, not guessed private API access.
    r = requests.get(PUBLIC_BINARY, timeout=(25,160), stream=True,
                     headers={"User-Agent":"owl172-research-candidate-check/1.0"})
    R["response"]={"http":r.status_code,"content_type":r.headers.get("content-type"),
                   "final_url":r.url,"content_length":r.headers.get("content-length")}
    r.raise_for_status()
    dest = OUT / "run231_INNERSCENE_GENERIC_OWL_CANDIDATE_NOT_APPROVED.glb"
    limit = 75*1024*1024
    size = 0
    with dest.open("wb") as f:
        for chunk in r.iter_content(1024*1024):
            if not chunk: continue
            size += len(chunk)
            if size>limit: raise ValueError("Download exceeded 75MiB safe cap")
            f.write(chunk)
    if size < 1024: raise ValueError("Empty/too small native model")
    R["download"] = dig(dest)
    R["native_glb_header"] = inspect_glb(dest)
    return dest
def get_scene(source):
    record = inspect_glb(source)
    if "KHR_draco_mesh_compression" in record["extensionsRequired"]:
        decoded = OUT / "run231_Draco_decoded_generic_owl_NOT_APPROVED.glb"
        result = subprocess.run(["gltf-transform","copy",str(source),str(decoded)],
                                stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                                text=True,timeout=180)
        R["draco_decode"] = {"return_code":result.returncode,"output_tail":result.stdout[-1500:]}
        if result.returncode: raise RuntimeError("Draco decode failed, native geometry not verified")
        if "KHR_draco_mesh_compression" in inspect_glb(decoded)["extensionsRequired"]:
            raise RuntimeError("Still Draco compressed")
        source = decoded
    scene = trimesh.load(str(source),force="scene",process=False)
    meshes = [m for m in scene.dump() if isinstance(m,trimesh.Trimesh) and len(m.faces)>0]
    if not meshes: raise ValueError("No real triangle mesh")
    total_faces = sum(len(m.faces) for m in meshes)
    xyz = np.concatenate([np.asarray(m.vertices) for m in meshes],axis=0)
    extents = np.ptp(xyz,axis=0)
    if not np.isfinite(xyz).all() or np.sum(extents>1e-5)<3 or max(extents)<1e-3:
        raise ValueError("Degenerate/empty all-zero 3D geometry")
    zero_fraction = float(np.mean(np.max(abs(xyz),axis=1)<1e-8))
    if zero_fraction>.98: raise ValueError("Nearly all vertices are zero: possible undecoded Draco")
    R["native_true3d"]={"source_used":dig(source),"meshes":len(meshes),
        "triangles":int(total_faces),"vertices":int(len(xyz)),
        "extents":extents.tolist(),"bounds":np.array([xyz.min(0),xyz.max(0)]).tolist(),
        "zero_vertex_fraction":zero_fraction,"material_kinds":[m.visual.kind for m in meshes]}
    return meshes
def render_native(meshes):
    renderer = vtk.vtkRenderer();renderer.SetBackground(.89,.90,.91)
    renderer.SetUseFXAA(True)
    window = vtk.vtkRenderWindow();window.SetOffScreenRendering(True)
    window.SetSize(420,420);window.AddRenderer(renderer)
    texture_count=0
    for k,m in enumerate(meshes):
        poly=vtk.vtkPolyData()
        pts=vtk.vtkPoints()
        pts.SetData(numpy_to_vtk(np.ascontiguousarray(m.vertices,dtype=np.float64),deep=True))
        poly.SetPoints(pts)
        f = np.column_stack([np.full(len(m.faces),3,dtype=np.int64),m.faces.astype(np.int64)]).ravel()
        cells=vtk.vtkCellArray()
        cells.SetCells(len(m.faces),numpy_to_vtkIdTypeArray(f,deep=True))
        poly.SetPolys(cells)
        mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
        actor=vtk.vtkActor();actor.SetMapper(mapper)
        actor.GetProperty().SetColor(.86,.80,.70)
        actor.GetProperty().SetAmbient(.22)
        actor.GetProperty().SetDiffuse(.73)
        mat=getattr(m.visual,"material",None)
        tex=getattr(mat,"baseColorTexture",None)
        if tex is None: tex=getattr(mat,"image",None)
        uv=getattr(m.visual,"uv",None)
        if tex is not None and uv is not None and len(uv)==len(m.vertices):
            try:
                img=Image.fromarray(np.asarray(tex)).convert("RGB")
                q=OUT/("run231_native_texture_%02d.png"%k)
                img.save(q)
                tc=numpy_to_vtk(np.asarray(uv,dtype=np.float32),deep=True)
                tc.SetName("uv")
                poly.GetPointData().SetTCoords(tc)
                reader=vtk.vtkPNGReader();reader.SetFileName(str(q));reader.Update()
                tx=vtk.vtkTexture();tx.SetInputConnection(reader.GetOutputPort())
                tx.InterpolateOn();actor.SetTexture(tx);texture_count+=1
            except Exception as e:
                R.setdefault("texture_warnings",[]).append(repr(e))
        renderer.AddActor(actor)
    bounds=np.array(renderer.ComputeVisiblePropBounds(),dtype=float).reshape(3,2)
    if not np.isfinite(bounds).all() or np.any(bounds[:,1]<=bounds[:,0]):
        raise ValueError("Renderer geometry missing")
    center=bounds.mean(axis=1)
    sizes=bounds[:,1]-bounds[:,0]
    up_axis=int(np.argmax(sizes))
    side_axes=[i for i in range(3) if i!=up_axis]
    axis=np.eye(3)
    scale=float(max(sizes))
    R["camera_coordinate_notice"]="up-axis inferred from max bounding dimension; azimuth labels are NOT independently anatomically oriented"
    R["camera_up_axis"]=up_axis
    poses=[]
    for degrees in [0,90,180,270]:
        direction=math.cos(math.radians(degrees))*axis[side_axes[0]]+math.sin(math.radians(degrees))*axis[side_axes[1]]
        poses.append(("azimuth_%03d"%degrees,direction,axis[up_axis]))
    poses += [("oblique", (axis[side_axes[0]]+axis[side_axes[1]]+axis[up_axis]) / math.sqrt(3), axis[up_axis]),
              ("top", axis[up_axis],-axis[side_axes[1]]),
              ("bottom",-axis[up_axis],axis[side_axes[1]])]
    pictures=[]; records=[]
    background=np.array([227,230,232],dtype=np.int16)
    for name,direction,up in poses:
        camera=renderer.GetActiveCamera()
        camera.ParallelProjectionOn()
        camera.SetPosition(*(center+direction*3.5*scale))
        camera.SetFocalPoint(*center)
        camera.SetViewUp(*up)
        camera.SetParallelScale(scale*.72)
        renderer.ResetCameraClippingRange()
        window.Render()
        q=OUT/("run231_NATIVE_3D_%s_ART_NOT_APPROVED.png"%name)
        shot=vtk.vtkWindowToImageFilter();shot.SetInput(window);shot.Update()
        writer=vtk.vtkPNGWriter();writer.SetFileName(str(q));writer.SetInputConnection(shot.GetOutputPort());writer.Write()
        im=np.asarray(Image.open(q).convert("RGB"),dtype=np.int16)
        foreground=int((np.max(np.abs(im-background),axis=2)>26).sum())
        if foreground<700: raise ValueError("EMPTY CAMERA %s foreground=%s"%(name,foreground))
        pictures.append((name,q));records.append({"camera":name,"foreground_pixels":foreground,"sha":dig(q)})
    window.Finalize()
    R["views"]=records
    R["native_texture_actors"]=texture_count
    sheet=Image.new("RGB",(4*280,2*320),(242,244,246))
    pen=ImageDraw.Draw(sheet)
    for i,(name,p) in enumerate(pictures):
        x=i%4*280;y=i//4*320
        pen.text((x+8,y+6),"INNERSCENE GENERIC OWL - "+name,fill=(33,33,33))
        sheet.paste(Image.open(p).convert("RGB").resize((270,270)),(x+5,y+30))
    dest=OUT/"run231_SEVEN_REAL_3D_CAMERAS_GENERIC_OWL_NOT_APPROVED.png"
    sheet.save(dest)
    R["contact_sheet"]=dig(dest)
try:
    R["ref"]=dig(REF)
    if R["ref"]["sha256"]!=KNOWN_REF_SHA: raise ValueError("Reference concept changed; stop experiment")
    img=Image.open(REF).convert("RGB")
    img.crop((img.width*2//3,0,img.width,img.height)).save(OUT/"run231_source_RIGHTMOST_juvenile_concept_reference_ONLY.png")
    source=fetch_binary()
    meshes=get_scene(source)
    render_native(meshes)
    R["status"]="REAL_GLTF_GEOMETRY_AND_SEVEN_CAMERAS_GENERATED_ART_UNREVIEWED_NO_RELEASE"
except BaseException as ex:
    R["status"]="NO_VERIFIED_QUALIFIED_MODEL_NO_RELEASE"
    R["error"]=repr(ex);R["traceback"]=traceback.format_exc()[-4000:]
finally:
    R["files"]={p.name:dig(p) for p in OUT.iterdir() if p.is_file() and p.name!="run231_machine_report.json"}
    (OUT/"run231_machine_report.json").write_text(json.dumps(R,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":R["status"],"download":R.get("download"),
          "native_true3d":R.get("native_true3d"),"views":len(R.get("views",[])),
          "error":R.get("error")},ensure_ascii=False),flush=True)
