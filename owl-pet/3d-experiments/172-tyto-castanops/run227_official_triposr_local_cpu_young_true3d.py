#!/usr/bin/env python3
"""Run227: one legitimate OFFLINE/LOCAL CPU TripoSR inference on the exact #172 v3
young reference, using public MIT model weights; isolated nonproduction experiment.
A real native GLB and seven actual mesh cameras are prerequisites, not approval.
No paid APIs, no external credentials, no deployment, no production writes.
"""
import os, sys, types, json, time, hashlib, traceback, importlib.util
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"owl-pet/3d-experiments/172-tyto-castanops/run227-evidence"
OUT.mkdir(parents=True,exist_ok=True)
REFERENCE=ROOT/"owl-pet/design/concepts/172-tyto-castanops-v3.png"
REFERENCE_SHA="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
R={"experiment":"Run227", "created_utc":datetime.now(timezone.utc).isoformat(),
   "target":"Tyto castanops v3 RIGHT young cream mesoptile only",
   "method":"official MIT Stability AI / Tripo AI TripoSR, local CPU, no ZeroGPU/API",
   "weights":"https://huggingface.co/stabilityai/TripoSR",
   "upstream":"https://github.com/VAST-AI-Research/TripoSR",
   "source_spatial_status":"NOT_YET_GENERATED",
   "display_approved":False,"release":"NO_RELEASE","paid_usd":0,
   "production_changed":False,"real_phone_webgl_test":False,
   "art_gate":"PENDING_MANUAL_VISUAL_REVIEW_DEFAULT_REJECT","phases":{}}
def sha(path):
    p=Path(path);return {"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def phase(label, fn):
    start=time.monotonic()
    try:
        result=fn()
        R["phases"][label]={"ok":True,"seconds":round(time.monotonic()-start,2)}
        return result
    except BaseException as exc:
        R["phases"][label]={"ok":False,"seconds":round(time.monotonic()-start,2),"error":repr(exc)}
        raise

def preprocess():
    from PIL import Image
    assert sha(REFERENCE)["sha256"]==REFERENCE_SHA,"original v3 concept checksum mismatch"
    R["reference"]=sha(REFERENCE)
    # Reuse independently verified Run225 cutout method, including its correction
    # for 1,215 mistakenly transparent pupil pixels. This is still only TWO-D input.
    p=ROOT/"owl-pet/3d-experiments/172-tyto-castanops/run225_hunyuan2_official_zerogpu_juvenile_qa.py"
    spec=importlib.util.spec_from_file_location("owl172_previous_validated_crop",p)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    img=Image.open(mod.prep()).convert("RGBA")
    bb=img.getchannel("A").getbbox()
    assert bb,"no foreground after source segmentation"
    cut=img.crop(bb)
    cut.thumbnail((438,438),Image.Resampling.LANCZOS)
    # Official TripoSR preprocessor expects a square and neutral grey canvas.
    canvas=Image.new("RGB",(512,512),(128,128,128))
    stage=Image.new("RGBA",(512,512),(128,128,128,255))
    stage.alpha_composite(cut,((512-cut.width)//2,(512-cut.height)//2))
    canvas=stage.convert("RGB")
    path=OUT/"run227_validated_young_neutral_input_2D_ONLY.png"
    canvas.save(path)
    R["preprocessed_2d"]=dict(sha(path),bounding_box=bb,pupil_holes=mod.R.get("restored_eye_holes"))
    return canvas

def run_model(image):
    import torch,numpy as np,skimage.measure
    torch.set_num_threads(2)
    os.environ.setdefault("OMP_NUM_THREADS","2")
    # Avoid requiring compiled CUDA torchmcubes: adapt its documented CPU
    # zero-level marching-cubes interface using skimage on this CPU-only runner.
    fake=types.ModuleType("torchmcubes")
    def cpu_mc(t,level=0.0):
        a=t.detach().cpu().numpy().astype(np.float32)
        if not (a.min()<level<a.max()):
            raise ValueError("no isosurface: occupancy never crosses level")
        verts,faces,_,_=skimage.measure.marching_cubes(a,level=float(level))
        return torch.from_numpy(verts.copy()).float(),torch.from_numpy(faces.copy()).long()
    fake.marching_cubes=cpu_mc
    sys.modules["torchmcubes"]=fake
    # TSR imports rembg as an optional preprocessor, but input already has
    # clean transparency and neutral backdrop, so no ONNX/rembg inference.
    rembg_stub=types.ModuleType("rembg")
    sys.modules["rembg"]=rembg_stub
    REPO=Path(os.environ.get("RUN227_TRIPOSR_ROOT","/tmp/TripoSR"))
    sys.path.insert(0,str(REPO))
    from tsr.system import TSR
    def calc():
        model=TSR.from_pretrained("stabilityai/TripoSR",
            config_name="config.yaml",weight_name="model.ckpt")
        model.renderer.set_chunk_size(1024)
        model=model.to("cpu").eval()
        R["model_initialised"]=True
        with torch.no_grad():
            codes=model([image],device="cpu")
        R["scene_codes_shape"]=list(codes.shape)
        # 96^3 points, bounded CPU and RAM rather than default 256^3.
        with torch.no_grad():
            meshes=model.extract_mesh(codes,has_vertex_color=True,resolution=96)
        assert len(meshes)==1
        m=meshes[0]
        assert len(m.faces)>1000 and len(m.vertices)>500,"no meaningful native mesh"
        assert np.isfinite(m.vertices).all()
        span=np.ptp(m.vertices,axis=0)
        assert (span>0.03).all(),"zero/degenerated 3D bounds"
        dst=OUT/"run227_TRIPOSR_CPU_native_REAL3D_ART_UNAPPROVED.glb"
        m.export(dst)
        imported=__import__("trimesh").load(str(dst),force="scene")
        ms=[x for x in imported.geometry.values() if len(getattr(x,"faces",[]))>0]
        assert ms and sum(len(x.faces) for x in ms)>1000
        verts=np.vstack([x.vertices for x in ms])
        spans=np.ptp(verts,axis=0)
        assert np.isfinite(verts).all() and (spans>0.03).all()
        R["native_mesh"]={"format":"binary glTF GLB","vertices":len(verts),
            "triangles":int(sum(len(x.faces) for x in ms)),
            "spans_xyz":spans.round(5).tolist(),"hash":sha(dst),
            "vertex_colors":bool(any(hasattr(x.visual,"vertex_colors") for x in ms))}
        R["source_spatial_status"]="NATIVE_TRIANGLE_GLTF_VALIDATED_NOT_ART_APPROVED"
        return dst
    return phase("official_model_cpu_and_marching_cubes",calc)

def seven_cameras(model_path):
    from PIL import Image,ImageDraw
    import vtk, math, numpy as np, trimesh
    from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
    sc=trimesh.load(str(model_path),force="scene")
    ren=vtk.vtkRenderer();ren.SetBackground(.90,.915,.935)
    win=vtk.vtkRenderWindow();win.SetOffScreenRendering(True);win.SetSize(500,500);win.AddRenderer(ren)
    tris=0
    for mesh in sc.geometry.values():
        if not isinstance(mesh,trimesh.Trimesh) or len(mesh.faces)==0:continue
        tris+=len(mesh.faces)
        poly=vtk.vtkPolyData()
        ps=vtk.vtkPoints();ps.SetData(numpy_to_vtk(np.asarray(mesh.vertices,dtype=np.float32),deep=True))
        poly.SetPoints(ps)
        faces=np.column_stack((np.full(len(mesh.faces),3,dtype=np.int64),mesh.faces.astype(np.int64))).ravel()
        cells=vtk.vtkCellArray();cells.SetCells(len(mesh.faces),numpy_to_vtkIdTypeArray(faces,deep=True))
        poly.SetPolys(cells)
        colors=np.asarray(mesh.visual.vertex_colors)
        if len(colors)==len(mesh.vertices):
            uchar=numpy_to_vtk(np.ascontiguousarray(colors[:,:3]),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR)
            uchar.SetNumberOfComponents(3);uchar.SetName("RGB")
            poly.GetPointData().SetScalars(uchar)
        mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
        if len(colors)==len(mesh.vertices):mapper.SetColorModeToDirectScalars()
        actor=vtk.vtkActor();actor.SetMapper(mapper)
        actor.GetProperty().SetInterpolationToPhong()
        if len(colors)!=len(mesh.vertices):actor.GetProperty().SetColor(.9,.86,.76)
        ren.AddActor(actor)
    bounds=ren.ComputeVisiblePropBounds()
    b=np.asarray(bounds,float)
    assert np.isfinite(b).all() and np.all(b[1::2]>b[::2])
    center=(b[::2]+b[1::2])/2
    span=max(b[1::2]-b[::2])
    specs=[("front",(0,0,3)),("back",(0,0,-3)),
           ("left",(-3,0,0)),("right",(3,0,0)),
           ("front_threequarter",(2,.55,2)),("top",(0,3,.2)),
           ("bottom",(0,-3,.5))]
    panel=Image.new("RGB",(4*320,2*350),(244,245,246))
    pen=ImageDraw.Draw(panel); records=[]
    for index,(name,vector) in enumerate(specs):
        cam=ren.GetActiveCamera();cam.ParallelProjectionOn()
        cam.SetFocalPoint(*center)
        cam.SetPosition(*(center+span*np.array(vector)))
        cam.SetViewUp(*( (0,0,1) if name=="top" else (0,1,0) ))
        cam.SetParallelScale(span*.8)
        ren.ResetCameraClippingRange()
        win.Render()
        wti=vtk.vtkWindowToImageFilter();wti.SetInput(win);wti.Update()
        path=OUT/("run227_TRUE_MESH_"+name+"_NOT_APPROVED.png")
        w=vtk.vtkPNGWriter();w.SetFileName(str(path));w.SetInputConnection(wti.GetOutputPort());w.Write()
        arr=np.asarray(Image.open(path).convert("RGB"),int)
        nonbg=int((np.max(abs(arr-np.array([230,233,238])),axis=2)>32).sum())
        assert nonbg>400,"blank GLB scene "+name
        thumb=Image.open(path).convert("RGB").resize((310,310))
        x=index%4*320; y=index//4*350
        panel.paste(thumb,(x,y+25));pen.text((x+6,y+5),name.upper(),fill=(25,28,31))
        records.append(dict(camera=name,foreground_pixels=nonbg,file=path.name))
    panel.save(OUT/"run227_TRIPOSR_SEVEN_TRUE3D_CAMERAS_NOT_APPROVED.png")
    win.Finalize()
    R["seven_camera_evidence"]=records
    R["technical_status"]="REAL_GLTF_IMPORT_AND_SEVEN_NATIVE_CAMERA_RENDER_PASS"
    R["art_gate"]="NOT_APPROVED_UNTIL_VISUAL_COMPARISON"
    R["release"]="NO_RELEASE"

def main():
    t=time.monotonic()
    try:
        image=phase("canonical_two_dimensional_source",preprocess)
        mesh=run_model(image)
        phase("seven_real_three_dimensional_mesh_cameras",lambda:seven_cameras(mesh))
        R["status"]="NATIVE_3D_READY_FOR_VISUAL_REJECTION_OR_REVIEW_NO_RELEASE"
    except BaseException as exc:
        R["status"]="FAILED_OR_PARTIAL_NO_RELEASE"
        R["error"]=repr(exc)
        R["traceback"]=traceback.format_exc()[-6500:]
    finally:
        R["elapsed_seconds"]=round(time.monotonic()-t,2)
        R["ended_utc"]=datetime.now(timezone.utc).isoformat()
        R["files"]={p.name:sha(p) for p in sorted(OUT.iterdir()) if p.is_file() and not p.name.endswith(".json")}
        (OUT/"run227_report.json").write_text(json.dumps(R,ensure_ascii=False,indent=2)+"\n")
        (OUT/"run227_status.md").write_text(
            "# Run227 genuine local CPU TripoSR reconstruction — NO RELEASE\n\n"
            +"Result: "+R["status"]+"\n\n"
            +"No paid APIs/GPU purchases. An exported GLB is not necessarily an acceptable "
            +"young owl, because image-to-3D may produce implausible sides, back, hollow support, "
            +"feathers, eyes and biology. Real mobile GPU WebGL remains untested.\n\n"
            +"Error, if any: "+str(R.get("error","none"))+"\n")
        print(json.dumps({k:v for k,v in R.items() if k not in ("traceback","files")},ensure_ascii=False,default=str),flush=True)
if __name__=="__main__":main()
