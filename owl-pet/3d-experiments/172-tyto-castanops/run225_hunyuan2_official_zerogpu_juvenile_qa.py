#!/usr/bin/env python3
"""Run225: a SINGLE no-token public official Hunyuan3D-2 ZeroGPU image->textured-native-GLB trial.
Research-only. Green CI != usable art. Never deploy, never mark aesthetically accepted.
Do not retry within the same run, switch to paid API, or send tokens.
"""
import hashlib, json, os, shutil, time, traceback
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
from PIL import Image, ImageDraw
import cv2

ROOT = Path(__file__).resolve().parents[3]
EXP = ROOT / "owl-pet/3d-experiments/172-tyto-castanops"
OUT = EXP / "run225-evidence"
OUT.mkdir(parents=True,exist_ok=True)
SRC = ROOT / "owl-pet/design/concepts/172-tyto-castanops-v3.png"
SOURCE_SHA = "881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
R = dict(run="Run225", date_utc=datetime.now(timezone.utc).isoformat(),
    target="#172 Tyto castanops v3 RIGHTMOST cream down age-unknown mesoptile",
    model="tencent/Hunyuan3D-2", upstream="https://huggingface.co/spaces/tencent/Hunyuan3D-2",
    reference_crop_xyxy=[950,255,1440,850],
    status="PREFLIGHT", output_release="NO_RELEASE",
    paid_requests=0, hf_token_used=False, actual_mobile_gpu_test=False,
    art_review="PENDING_HUMAN_VISUAL_INSPECTION_NEVER_AUTO_ACCEPT",
    constraints=["true spatial 3D","heart face integrated into head","cream second down",
       "young crouched proportions","short down buried wings","hidden tail",
       "both feet on broad hollow lip","consistent back and sides","phone WebGL budget"])
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def prep():
    assert SRC.is_file() and h(SRC)==SOURCE_SHA, "Canonical source missing or changed"
    im=Image.open(SRC).convert("RGB")
    assert im.size==(1536,1024)
    crop=im.crop(tuple(R["reference_crop_xyxy"]))
    crop.save(OUT/"run225_exact_young_crop.png")
    rgb=np.asarray(crop).copy()
    bgr=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR)
    height,width=bgr.shape[:2]
    gc=np.zeros((height,width),np.uint8)
    cv2.grabCut(bgr,gc,(round(width*.09),round(height*.035),
             round(width*.82),round(height*.89)),
             np.zeros((1,65),np.float64),np.zeros((1,65),np.float64),
             7,cv2.GC_INIT_WITH_RECT)
    a=np.where((gc==cv2.GC_FGD)|(gc==cv2.GC_PR_FGD),255,0).astype(np.uint8)
    n,l,stats,_=cv2.connectedComponentsWithStats(a)
    assert n>1
    idx=max(range(1,n),key=lambda j:stats[j,cv2.CC_STAT_AREA])
    a=(l==idx).astype(np.uint8)*255
    a=cv2.morphologyEx(a,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
    n,l,stats,_=cv2.connectedComponentsWithStats(cv2.bitwise_not(a))
    restored=[]
    for j in range(1,n):
        x,y,w,ht,area=map(int,stats[j])
        if x>0 and y>0 and x+w<width and y+ht<height and area<.02*(height*width):
            a[l==j]=255
            restored.append(dict(bbox=[x,y,w,ht],pixels=area))
    ratio=float(np.count_nonzero(a))/a.size
    assert .15<ratio<.94, ratio
    R.update(source_sha=h(SRC), restored_eye_holes=restored, alpha_ratio=ratio)
    rgba=np.dstack((rgb,a))
    p=OUT/"run225_canonical_young_RGBA_restored_eyes.png"
    Image.fromarray(rgba,"RGBA").save(p)
    R["input_sha"]=h(p)
    return p

def walk_file(obj):
    files=[]
    def go(o):
        if isinstance(o,str) and ".glb" in o.lower():
            files.append(o)
        elif isinstance(o,dict):
            for k,v in o.items():
                if k in ("url","path","name","value") and isinstance(v,str) and ".glb" in v.lower():files.append(v)
                elif isinstance(v,(dict,list,tuple)):go(v)
        elif isinstance(o,(list,tuple)):
            for v in o:go(v)
    go(obj)
    return files

def persist_glb(candidate):
    dest=OUT/"run225_hunyuan2_unapproved_textured.glb"
    from urllib.parse import urlparse
    if candidate.startswith(("https://","http://")):
        host=urlparse(candidate).hostname or ""
        assert host.endswith((".hf.space",".huggingface.co")) or host in ("huggingface.co","cdn-lfs.hf.co"),host
        import requests
        with requests.get(candidate,timeout=90,stream=True) as resp:
            resp.raise_for_status()
            with dest.open("wb") as f:
                for b in resp.iter_content(1024*1024):f.write(b)
    else:
        assert Path(candidate).is_file(), candidate
        shutil.copyfile(candidate,dest)
    assert dest.stat().st_size>4096 and dest.open("rb").read(4)==b"glTF", "No valid GLB magic"
    R["glb_bytes"]=dest.stat().st_size
    R["glb_sha256"]=h(dest)
    return dest

def actual_validate_and_render(p):
    import trimesh, vtk
    s=trimesh.load(str(p),force="scene")
    real=[m for m in s.geometry.values() if isinstance(m,trimesh.Trimesh) and len(m.faces)>0]
    assert real, "No triangle mesh"
    pts=np.vstack([m.vertices for m in real])
    dims=np.ptp(pts,axis=0)
    assert np.isfinite(pts).all() and np.isfinite(dims).all() and min(dims)>1e-5, "Zero or invalid spatial coordinates"
    faces=int(sum(len(m.faces) for m in real))
    assert faces>1000, "Not a credible mesh"
    R["geometry"]={"meshes":len(real),"triangles":faces,"bounds_xyz":dims.tolist(),"vertices":len(pts)}
    imp=vtk.vtkGLTFImporter()
    imp.SetFileName(str(p))
    ren=vtk.vtkRenderer();ren.SetBackground(.11,.14,.18)
    window=vtk.vtkRenderWindow();window.SetSize(560,560);window.SetOffScreenRendering(True)
    window.AddRenderer(ren);imp.SetRenderWindow(window);imp.Update()
    bounds=ren.ComputeVisiblePropBounds()
    b=np.array(bounds,dtype=float)
    assert np.isfinite(b).all() and b[1]>b[0] and b[3]>b[2] and b[5]>b[4], "Importer has no spatial scene"
    c=np.array([(b[0]+b[1])/2,(b[2]+b[3])/2,(b[4]+b[5])/2])
    radius=max(b[1]-b[0],b[3]-b[2],b[5]-b[4])
    positions=[("front",(0,-3,0)),("back",(0,3,0)),
          ("left",(-3,0,0)),("right",(3,0,0)),
          ("threequarter",(2,-2,.5)),("top",(0,0,3)),
          ("bottom",(0,-1,-3))]
    outputs=[]
    for name,d in positions:
        v=np.array(d,dtype=float)
        cam=ren.GetActiveCamera()
        cam.SetPosition(*(c+radius*v))
        cam.SetFocalPoint(*c)
        cam.SetViewUp(*( (0,1,0) if name in ("top","bottom") else (0,0,1) ))
        cam.ParallelProjectionOn();cam.SetParallelScale(radius*.8)
        ren.ResetCameraClippingRange();window.Render()
        f=vtk.vtkWindowToImageFilter();f.SetInput(window);f.Update()
        pth=OUT/("run225_native_"+name+".png")
        wr=vtk.vtkPNGWriter();wr.SetFileName(str(pth));wr.SetInputConnection(f.GetOutputPort());wr.Write()
        a=np.asarray(Image.open(pth).convert("RGB"))
        bg=np.array([.11,.14,.18])*255
        fg=int((np.max(np.abs(a-bg),axis=2)>35).sum())
        assert fg>700,"Blank render "+name
        outputs.append(dict(camera=name,file=pth.name,non_bg_pixels=fg))
    window.Finalize()
    composite=Image.new("RGB",(4*290,2*310),(238,236,231))
    draw=ImageDraw.Draw(composite)
    for i,item in enumerate(outputs):
        img=Image.open(OUT/item["file"]).convert("RGB")
        img.thumbnail((285,280))
        x=i%4*290;y=i//4*310
        composite.paste(img,(x,y+26))
        draw.text((x+7,y+5),item["camera"].upper(),fill=(20,20,20))
    composite.save(OUT/"run225_seven_3d_views_UNREVIEWED_NO_RELEASE.png")
    R["camera_evidence"]=outputs
    R["status"]="NATIVE_TEXTURED_GLB_7_VIEWS_TECHNICAL_QA_ART_UNREVIEWED_NO_RELEASE"

def main():
    start=time.monotonic()
    try:
        source=prep()
        # Public ZeroGPU, no token. Never silently fall back to a paid endpoint.
        from gradio_client import Client,handle_file
        os.environ["HF_HOME"]="/tmp/owl172_run225_anonymous_zero_gpu"
        os.environ.pop("HF_TOKEN",None)
        cli=Client("tencent/Hunyuan3D-2",verbose=False,token=None)
        api={str(k):str(v.api_name) for k,v in cli.endpoints.items()}
        R["api_endpoints"]=api
        R["status"]="API_DISCOVERED_NOT_YET_GENERATED"
        names=list(api.values())
        match=next((n for n in names if n and ("generation_all" in n or "gen_textured" in n)),None)
        if not match:
            # Inspect documented signatures only; do not call a wrong or undocumented endpoint.
            info=cli.view_api(return_format="dict")
            R["view_api_excerpt"]=str(info)[:11000]
            raise RuntimeError("Official textured single-call endpoint not exposed; no paid/no guessing")
        # App source 2026-11-20 btn_all.click generation_all has precisely these 13 inputs;
        # the GPU decorator requests 90 seconds. One trial ONLY, no retry if quota-limited.
        # RGBA already has correct pupils and transparent background.
        values=[None,handle_file(str(source)),None,None,None,None,30,5.0,172225,256,False,8000,False]
        job=cli.submit(*values,api_name=match)
        R["submitted"]=True
        R["remote_endpoint"]=match
        result=job.result(timeout=500)
        R["result_preview"]=str(result)[:3500]
        candidates=walk_file(result)
        R["glb_candidates"]=candidates[:8]
        if not candidates:raise RuntimeError("Official generation returned no download-path GLB")
        # Prefer textured GLB over white shape: 2nd of generation_all outputs.
        candidate=next((x for x in candidates if "textured" in x.lower()),candidates[-1])
        dest=persist_glb(candidate)
        R["status"]="NATIVE_GLB_UNREVIEWED_NO_RELEASE"
        actual_validate_and_render(dest)
    except Exception as e:
        R["error"]=str(e)
        R["traceback"]=traceback.format_exc()[-6000:]
        R["status"]="NO_NEW_VERIFIED_GLB_NO_RELEASE"
    finally:
        R["runtime_seconds"]=round(time.monotonic()-start,2)
        R["evidence_files"]={x.name:dict(bytes=x.stat().st_size,sha256=h(x))
          for x in sorted(OUT.iterdir()) if x.is_file() and not x.name.startswith("run225_report")}
        (OUT/"run225_report.json").write_text(json.dumps(R,ensure_ascii=False,indent=2,default=str))
        (OUT/"run225_report.md").write_text(
          "# #172 Run225 official Tencent Hunyuan3D-2 ZeroGPU trial — NO RELEASE\\n\\n"
          "Native 3D is necessary but insufficient. Output never automatically accepted.\\n\\n"
          "Status: "+R["status"]+"\\n\\n"
          "Error: "+str(R.get("error","none"))+"\\n\\n"
          "No costs, no credentials, no changes to production or prototype.\\n".replace("\\n","\n"))
        print(json.dumps({k:v for k,v in R.items() if k not in ("traceback","result_preview","view_api_excerpt")},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
