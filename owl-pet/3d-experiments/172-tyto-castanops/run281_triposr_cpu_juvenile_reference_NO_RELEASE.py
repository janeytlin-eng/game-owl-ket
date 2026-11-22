#!/usr/bin/env python3
"""Run281. Source-image-specific, real MIT TripoSR CPU reconstruction feasibility.

Only source is the rightmost juvenile in the archived #172 v3 concept.
No crude primitive/owl stand-in. All outputs are research-only and fail closed.
The target view is a front *concept*, not measured biological anatomy.
"""
import argparse, json, hashlib, os, pathlib, sys, time
import numpy as np
from PIL import Image

def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def prepare(source, output):
    import cv2
    im=Image.open(source).convert("RGB")
    assert im.size == (1536,1024), "Unexpected v3 reference dimensions"
    # Right-hand owlet, without adults, title or bottom caption.
    # Coordinates are defined relative to ORIGINAL 1536x1024 reference.
    box=(956,271,1407,811)
    crop=np.array(im.crop(box))
    h,w=crop.shape[:2]
    # GrabCut is a true content-dependent segmentation attempt, not an
    # invented 3D shape. Exclude the bark/branch using conservative seeds.
    m=np.full((h,w),cv2.GC_PR_BGD,np.uint8)
    y,x=np.mgrid[:h,:w]
    cx,cy=244,265
    ellipse=((x-cx)/203)**2+((y-cy)/272)**2
    m[ellipse<1]=cv2.GC_PR_FGD
    m[ellipse<.46]=cv2.GC_FGD
    # Top, side and lower bark as definite background
    m[:10,:]=cv2.GC_BGD
    m[:,:14]=cv2.GC_BGD
    m[:,-12:]=cv2.GC_BGD
    m[-5:,:]=cv2.GC_BGD
    # Keep face, both eyes, beak and chest surely within foreground.
    m[120:340,118:355]=cv2.GC_FGD
    bg=np.zeros((1,65),np.float64);fg=np.zeros((1,65),np.float64)
    try:
        cv2.grabCut(crop,m,None,bg,fg,6,cv2.GC_INIT_WITH_MASK)
        a=np.where((m==cv2.GC_FGD)|(m==cv2.GC_PR_FGD),255,0).astype(np.uint8)
        seg="cv2-grabcut-seeded"
    except Exception as e:
        # A failed grabcut MUST be exposed; fallback is a soft silhouette and
        # this run may never count as a high-quality aesthetic pass.
        a=(ellipse<1).astype(np.uint8)*255
        seg=f"fallback-ellipse:{str(e)[:180]}"
    a=cv2.GaussianBlur(a,(5,5),.8)
    bounds=cv2.findNonZero((a>20).astype(np.uint8))
    assert bounds is not None,"No owl foreground"
    xx,yy,ww,hh=cv2.boundingRect(bounds)
    rgb=crop[yy:yy+hh,xx:xx+ww]
    aa=a[yy:yy+hh,xx:xx+ww]
    scale=440/max(ww,hh)
    nx=max(1,int(ww*scale));ny=max(1,int(hh*scale))
    rgb=cv2.resize(rgb,(nx,ny),interpolation=cv2.INTER_AREA if scale<1 else cv2.INTER_LINEAR)
    aa=cv2.resize(aa,(nx,ny),interpolation=cv2.INTER_LINEAR)
    fg=np.array(Image.new("RGB",(512,512),(128,128,128)),dtype=np.uint8)
    ox=(512-nx)//2;oy=(512-ny)//2
    f=aa.astype(np.float32)[...,None]/255
    fg[oy:oy+ny,ox:ox+nx]=np.rint(f*rgb+(1-f)*128).astype(np.uint8)
    p=pathlib.Path(output);p.parent.mkdir(parents=True,exist_ok=True)
    Image.fromarray(fg).save(p)
    debug=Image.fromarray(np.dstack([crop,a]))
    debug.save(p.with_name("source_crop_and_alpha_RESEARCH.png"))
    info={"reference_sha256":sha(source),"prepared_sha256":sha(p),
          "crop_source_xyxy":box,"segmentation":seg,"foreground_bbox":[int(xx),int(yy),int(ww),int(hh)],
          "source_dimensions":list(im.size),"input_dimensions":[512,512],
          "model":"TripoSR, MIT, CPU, verified only after actual checkpoint and inference",
          "status":"INPUT_PREPARED_ONLY / NO_RELEASE"}
    p.with_name("input_provenance_RESEARCH.json").write_text(json.dumps(info,indent=2))
    print(json.dumps(info,indent=2))

def qa(glb,out):
    import trimesh
    from PIL import Image,ImageDraw
    p=pathlib.Path(glb);o=pathlib.Path(out);o.mkdir(parents=True,exist_ok=True)
    if not p.exists():raise RuntimeError("Actual AI 3D mesh is absent; NEVER substitute synthetic geometry")
    s=trimesh.load(p,force="scene")
    meshes=[m for m in s.geometry.values() if isinstance(m,trimesh.Trimesh)]
    faces=sum(len(m.faces) for m in meshes)
    verts=sum(len(m.vertices) for m in meshes)
    if faces<2000 or verts<1000:raise RuntimeError(f"TripoSR output too small ({faces} faces)")
    bounds=s.bounds
    if not np.all(np.isfinite(bounds)):raise RuntimeError("Nonfinite 3D bounds")
    import vtk
    rw=vtk.vtkRenderWindow();rw.SetSize(540,540);rw.SetOffScreenRendering(1)
    renderer=vtk.vtkRenderer();rw.AddRenderer(renderer)
    imp=vtk.vtkGLTFImporter();imp.SetFileName(str(p));imp.SetRenderWindow(rw);imp.Update()
    renderer.SetBackground(.91,.89,.85)
    # Camera labels are axis directions, not an unverified claim of front/rear!
    directions={"+Z":(0,0,1),"+X":(1,0,0),"-Z":(0,0,-1),"-X":(-1,0,0),
                "+Y":(0,1,0),"-Y":(0,-1,0)}
    bmin,bmax=bounds;center=(bmin+bmax)/2
    diagonal=float(np.linalg.norm(bmax-bmin))
    assert diagonal>1e-6
    outputs=[]
    for name,d in directions.items():
        cam=renderer.GetActiveCamera()
        cam.ParallelProjectionOn()
        cam.SetFocalPoint(*center)
        cam.SetPosition(*(center+np.asarray(d)*diagonal*2.2))
        up=(0,0,-1) if name=="+Y" else ((0,0,1) if name=="-Y" else (0,1,0))
        cam.SetViewUp(*up)
        cam.SetParallelScale(diagonal*.69)
        renderer.ResetCameraClippingRange();rw.Render()
        window=vtk.vtkWindowToImageFilter();window.SetInput(rw);window.Update()
        fn=o/("axis_"+name.replace("+","pos").replace("-","neg")+".png")
        writer=vtk.vtkPNGWriter();writer.SetFileName(str(fn));writer.SetInputConnection(window.GetOutputPort());writer.Write()
        if fn.stat().st_size<4000:raise RuntimeError("Empty 3D camera frame")
        outputs.append(fn)
    cols=3;rows=2;tile=380
    montage=Image.new("RGB",(cols*tile,rows*(tile+25)),(244,242,238))
    draw=ImageDraw.Draw(montage)
    for i,file in enumerate(outputs):
        im=Image.open(file).convert("RGB");im.thumbnail((tile,tile))
        x=(i%cols)*tile;y=(i//cols)*(tile+25)
        montage.paste(im,(x,y));draw.text((x+6,y+tile+3),file.stem,fill=(20,20,20))
    montage.save(o/"six_true_camera_directions_REVIEW.png")
    info={"input_glb_sha256":sha(p),"vertices":verts,"triangles":faces,
          "meshes":len(meshes),"bounds":bounds.tolist(),
          "six_actual_camera_views":[x.name for x in outputs],
          "model_is_true_3d":True,
          "art_review":"PENDING_VISUAL_REVIEW_NO_RELEASE",
          "physical_phone_test":False,
          "commercial_rights":"CHECK_TRIPOSR_WEIGHT_MIT_AND_REFERENCE_OWNERSHIP",
          "status":"TRUE_NATIVE_3D_EXPORT_TESTED / ART_UNREVIEWED / NO_RELEASE"}
    (o/"native_model_qa_RESEARCH.json").write_text(json.dumps(info,indent=2))
    print(json.dumps(info,indent=2))

if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("task",choices=["prep","qa"])
    a.add_argument("source");a.add_argument("output")
    x=a.parse_args()
    prepare(x.source,x.output) if x.task=="prep" else qa(x.source,x.output)
