#!/usr/bin/env python3
"""Run205: real input matte ablation -> genuine TripoSR CPU meshes; nothing is released."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, platform, subprocess, sys, time, traceback

import numpy as np
from PIL import Image, ImageDraw

R=Path("owl-pet/3d-experiments/172-tyto-castanops")
E=R/"research-evidence-run205-MATTED-TRIPOSR-CPU-NO_RELEASE"
SRC=R/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
SOURCE_SHA="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
PREFLIGHT=[
"owl-pet/AGENTS.md","owl-pet/README.md","owl-pet/STATUS.md",
"owl-pet/prototype/index.html","owl-pet/research/species/172-tyto-castanops-v3.md",
str(R/"known_rejected_asset_sha256_registry.json"),
str(R/"2026-11-19-run204c-independent-native-sevenview-twelve-orbit-ART_REJECTED-NO_RELEASE.md")
]
S={"run":205,"utc":datetime.now(timezone.utc).isoformat(),
   "source_sha256_expected":SOURCE_SHA,"model":"VAST-AI-Research/TripoSR",
   "extra_payment":0,"true_mobile_gpu_test":False,"art_approved":False,
   "release":False,"variants":{}}
def digest(b): return hashlib.sha256(b).hexdigest()
def jsave(p,obj):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n")
def component(binary):
    import cv2
    n,l,stats,cent=cv2.connectedComponentsWithStats(binary.astype(np.uint8),8)
    if n<=1:return np.zeros_like(binary,dtype=bool),0
    j=1+int(np.argmax(stats[1:,cv2.CC_STAT_AREA]))
    return l==j,int(stats[j,cv2.CC_STAT_AREA])
def mattes(image):
    import cv2
    a=np.array(image.convert("RGB"))
    # Source is a real single-view concept crop with two distinct backgrounds:
    # near-white outside and a black rectangle behind the right side.
    w,wa=component((np.min(a,axis=2)>235))
    b,ba=component((np.max(a,axis=2)<45))
    if min(wa,ba)<8000:
        raise RuntimeError("Expected two large connected white/black background components")
    bg=w|b
    # Method A: preserve every interior black eye pixel (only remove the
    # connected black background region), with a narrow antialiased edge.
    foreground=(~bg).astype(np.uint8)*255
    background_dist=cv2.distanceTransform(255-foreground,cv2.DIST_L2,3)
    foreground_dist=cv2.distanceTransform(foreground,cv2.DIST_L2,3)
    soft=np.uint8(np.clip((foreground_dist-background_dist+1.2)*90,0,255))
    # Method B: constrain a real graph-cut optimization with source-aware
    # foreground seeds, while the strong background islands remain immutable.
    h,width=foreground.shape
    gc=np.full((h,width),cv2.GC_PR_FGD,np.uint8)
    gc[bg]=cv2.GC_BGD
    cv2.ellipse(gc,(240,250),(99,145),0,0,360,cv2.GC_FGD,-1)
    cv2.ellipse(gc,(245,132),(92,77),0,0,360,cv2.GC_FGD,-1)
    gc[0:15,:]=cv2.GC_BGD;gc[-8:,:]=cv2.GC_BGD
    gc[:,:12]=cv2.GC_BGD;gc[:,-12:]=cv2.GC_BGD
    bgmodel=np.zeros((1,65),np.float64);fgmodel=np.zeros((1,65),np.float64)
    cv2.grabCut(a,gc,None,bgmodel,fgmodel,4,cv2.GC_INIT_WITH_MASK)
    gc_mask=np.where((gc==cv2.GC_FGD)|(gc==cv2.GC_PR_FGD),255,0).astype(np.uint8)
    # Two-pixel alpha edge; interior eyes are retained by the GC_FGD face seeds.
    refined=cv2.GaussianBlur(gc_mask,(5,5),0.9)
    metrics={"background_white_connected_pixels":wa,"background_black_connected_pixels":ba}
    for name,alpha in [("two_region_flood",soft),("seeded_grabcut",refined)]:
        active=int(np.count_nonzero(alpha>128))
        if not 20000<active<210000:
            raise RuntimeError(name+" mask implausible area: "+str(active))
        rgba=np.dstack((a,alpha))
        Image.fromarray(rgba,"RGBA").save(E/f"{name}_rgba.png")
        m=np.zeros_like(a);m[:]=(230,230,230)
        blended=(a*(alpha[:,:,None]/255.)+m*(1-alpha[:,:,None]/255.)).astype(np.uint8)
        Image.fromarray(blended).save(E/f"{name}_matte_preview.png")
        Image.fromarray(alpha).save(E/f"{name}_mask.png")
        metrics[name]={"pixels_alpha_over_128":active,
             "fraction":round(active/float(h*width),5),
             "alpha_min":int(alpha.min()),"alpha_max":int(alpha.max()),
             "central_eye_protected":bool(alpha[155,237]>128 and alpha[155,309]>128)}
    jsave(E/"matting_metrics.json",metrics)
    return metrics

def render_native(mesh_path,out):
    import vtk
    vtk.vtkObject.GlobalWarningDisplayOff()
    win=vtk.vtkRenderWindow()
    win.SetOffScreenRendering(True)
    win.SetSize(450,450)
    imp=vtk.vtkGLTFImporter()
    imp.SetFileName(str(mesh_path))
    imp.SetRenderWindow(win)
    imp.Update()
    ren=win.GetRenderers().GetFirstRenderer()
    if ren is None:raise RuntimeError("No VTK scene renderer")
    ren.SetBackground(.89,.89,.86)
    bb=ren.ComputeVisiblePropBounds()
    mid=np.array([(bb[0]+bb[1])/2,(bb[2]+bb[3])/2,(bb[4]+bb[5])/2])
    span=max(bb[1]-bb[0],bb[3]-bb[2],bb[5]-bb[4])
    if span<1.e-5 or not np.isfinite(span):raise RuntimeError("Invalid VTK bounds")
    angles={"front":([0,0,1],[0,1,0]),"back":([0,0,-1],[0,1,0]),
        "left":([-1,0,0],[0,1,0]),"right":([1,0,0],[0,1,0]),
        "top":([0,1,0],[0,0,-1]),"bottom":([0,-1,0],[0,0,1]),
        "quarter":([.65,.25,1],[0,1,0])}
    ims=[]
    for name,(direction,up) in angles.items():
        v=np.asarray(direction,float);v/=np.linalg.norm(v)
        cam=ren.GetActiveCamera()
        cam.SetFocalPoint(*mid)
        cam.SetPosition(*(mid+span*2.6*v))
        cam.SetViewUp(*up)
        cam.ParallelProjectionOn()
        cam.SetParallelScale(span*.75)
        ren.ResetCameraClippingRange()
        win.Render()
        capt=vtk.vtkWindowToImageFilter()
        capt.SetInput(win);capt.ReadFrontBufferOff();capt.Update()
        dest=out/f"actual_{name}.png"
        writer=vtk.vtkPNGWriter()
        writer.SetFileName(str(dest));writer.SetInputConnection(capt.GetOutputPort())
        writer.Write()
        if not dest.is_file() or dest.stat().st_size<1500:
            raise RuntimeError("VTK render missing "+name)
        ims.append((name,Image.open(dest).convert("RGB").copy()))
    sheet=Image.new("RGB",(1800,980),(246,245,241))
    draw=ImageDraw.Draw(sheet)
    for i,(name,im) in enumerate(ims):
        x=(i%4)*450;y=(i//4)*490
        sheet.paste(im,(x,y+22));draw.text((x+12,y+5),name,fill=(0,0,0))
    sheet.save(out/"native_sevenview.png")
    return True

def infer_one(name):
    import trimesh
    out=E/name
    out.mkdir(parents=True,exist_ok=True)
    inp=(E/(name+"_rgba.png")).resolve()
    cmd=[sys.executable,"/tmp/TripoSR/run.py",str(inp),
        "--device","cpu","--mc-resolution","128","--chunk-size","1024",
        "--model-save-format","glb","--output-dir",str((out/"raw").resolve())]
    start=time.monotonic()
    try:
        with (out/"inference.log").open("w") as log:
            proc=subprocess.run(cmd,cwd="/tmp/TripoSR",env={**os.environ,
                "OMP_NUM_THREADS":"2","MKL_NUM_THREADS":"2",
                "TOKENIZERS_PARALLELISM":"false"},
                stdout=log,stderr=subprocess.STDOUT,timeout=1250)
        entry={"exit_code":proc.returncode,"seconds":round(time.monotonic()-start,2),
               "image":"real source-conditioned "+name+" alpha"}
        if proc.returncode:
            entry["gate"]="INFERENCE_FAILED"
            return entry
        mesh=out/"raw"/"0"/"mesh.glb"
        raw=mesh.read_bytes()
        sc=trimesh.load(mesh,force="scene",process=False)
        triangles=sum(len(g.faces) for g in sc.geometry.values() if hasattr(g,"faces"))
        entry.update({"real_native_glb":True,"sha256":digest(raw),
            "glb_bytes":len(raw),"triangles":triangles,"mesh_count":len(sc.geometry)})
        if triangles<1000:raise RuntimeError("Unexpected low triangle count")
        entry["seven_native_views"]=render_native(mesh,out)
        entry["gate"]="NATIVE_MULTIVIEW_ART_UNREVIEWED_NO_RELEASE"
        return entry
    except Exception as e:
        (out/"exception_trace.txt").write_text(traceback.format_exc())
        return {"gate":"INFERENCE_OR_NATIVE_QA_ERROR","error":repr(e),
                "seconds":round(time.monotonic()-start,2)}

def archive():
    jsave(E/"status.json",S)
    for p in sorted(E.rglob("*")):
        if p.is_file() and p.name!="manifest.json":
            pass
    inv={}
    for p in sorted(E.rglob("*")):
        if p.is_file() and p.name!="manifest.json":
            buf=p.read_bytes();inv[str(p.relative_to(E))]={"bytes":len(buf),"sha256":digest(buf)}
    jsave(E/"manifest.json",inv)
    summary=[
        "# Run205 — two-background connected alpha and seeded GrabCut TripoSR CPU ablation",
        "Source: pinned #172 v3 rightmost 512×512 conceptual crop; source SHA256 "+SOURCE_SHA,
        "Scope: #172 independent research; no changes to production, pet prototype or live deployment.",
        "This experiment replaces mixed black/off-white source background using (1) connected-component",
        "alpha and (2) protected-face graph-cut alpha, and ACTUALLY runs official TripoSR on CPU.",
        "These images are reference-conditioned neural attempts, not expert-designed multi-view anatomy.",
        "Technology gates are separate from art acceptance. Both require independent human visual review.",
        "No physical phone WebGL/GPU test, no rig, no approved organic cream-down juvenile.",
        "Actual outcome/status JSON and original GLB/render files are in isolated short-lived Actions artifact.",
        "Model checksums, preflight, masks and all unaltered errors are in manifest.json.",
        "**NO_RELEASE / NO_NOTIFICATION.**"
    ]
    (R/"2026-11-19-run205-dual-background-alpha-sourcebound-NO_RELEASE.md").write_text("\n".join(summary)+"\n")

def main():
    E.mkdir(parents=True,exist_ok=True)
    try:
        pre={}
        for path in PREFLIGHT:
            bb=Path(path).read_bytes()
            if len(bb)<50:raise RuntimeError("Preflight file missing "+path)
            pre[path]={"bytes":len(bb),"sha256":digest(bb)}
        bb=SRC.read_bytes()
        if digest(bb)!=SOURCE_SHA:raise RuntimeError("Wrong target concept crop")
        pre[str(SRC)]={"bytes":len(bb),"sha256":digest(bb)}
        pre["runtime"]={"python":sys.version,"platform":platform.platform(),"cpu":os.cpu_count()}
        jsave(E/"preflight.json",pre)
        mattes(Image.open(SRC))
        for name in ("two_region_flood","seeded_grabcut"):
            S["variants"][name]=infer_one(name)
    except Exception as exc:
        S["error"]=repr(exc)
        (E/"exception_trace.txt").write_text(traceback.format_exc())
    finally:
        S["gate"]="NO_RELEASE_ART_UNAPPROVED"
        archive()
        print(json.dumps(S,indent=2,ensure_ascii=False))
if __name__=="__main__":
    main()
