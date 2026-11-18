#!/usr/bin/env python3
"""Separate native GLB 7-view render QA. Geometry is never synthesized."""
from pathlib import Path
import hashlib,json,os,traceback,math
ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
O=ROOT/"research-evidence-run195-CC0-RIGGED-DONOR-ART_UNAPPROVED-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
paths=sorted(O.glob("run195_OWL_*.glb"))
q={"run":195,"source_glbs":[p.name for p in paths],"seven_native_views_success":False,
   "render_kind":"vtkGLTFImporter actual binary material rendering",
   "art_pass":False,"physical_mobile_gpu_verified":False}
if paths:
    try:
        import vtk
        from PIL import Image,ImageOps,ImageDraw
        p=paths[0]
        h=hashlib.sha256(p.read_bytes()).hexdigest()
        win=vtk.vtkRenderWindow()
        win.SetOffScreenRendering(1)
        win.SetSize(640,640)
        importer=vtk.vtkGLTFImporter()
        importer.SetFileName(str(p))
        importer.SetRenderWindow(win)
        importer.Update()
        renderer=win.GetRenderers().GetFirstRenderer()
        if renderer is None: raise RuntimeError("GLTFImporter provided no native renderer")
        renderer.SetBackground(0.19,0.21,0.23)
        renderer.SetBackground2(0.29,0.32,0.34)
        renderer.GradientBackgroundOn()
        bounds=renderer.ComputeVisiblePropBounds()
        if not bounds or bounds[0]>bounds[1]:raise RuntimeError("No visible mesh in imported GLB")
        cx,cy,cz=[(bounds[i]+bounds[i+1])/2 for i in (0,2,4)]
        radius=max((bounds[1]-bounds[0]),(bounds[3]-bounds[2]),(bounds[5]-bounds[4]),0.05)
        offsets={"front":(0,0,1),"side_right":(1,0,0),"back":(0,0,-1),
                 "side_left":(-1,0,0),"top":(0,1,0),"bottom":(0,-1,0),"quarter":(0.72,0.25,0.72)}
        files=[]
        for name,vec in offsets.items():
            camera=renderer.GetActiveCamera()
            camera.SetFocalPoint(cx,cy,cz)
            camera.SetPosition(cx+vec[0]*radius*2.8,cy+vec[1]*radius*2.8,cz+vec[2]*radius*2.8)
            camera.SetViewUp(0,0,-1) if name in ("top","bottom") else camera.SetViewUp(0,1,0)
            camera.ParallelProjectionOn()
            camera.SetParallelScale(radius*0.75)
            renderer.ResetCameraClippingRange()
            win.Render()
            w=vtk.vtkWindowToImageFilter()
            w.SetInput(win)
            w.SetInputBufferTypeToRGB()
            w.ReadFrontBufferOff()
            w.Update()
            dest=O/("run195_TRUE_NATIVE_"+name+".png")
            writer=vtk.vtkPNGWriter()
            writer.SetFileName(str(dest))
            writer.SetInputConnection(w.GetOutputPort())
            writer.Write()
            if not dest.is_file() or dest.stat().st_size<6000:raise RuntimeError("PNG missing/empty "+name)
            files.append(dest)
        contact=Image.new("RGB",(4*360,2*390),(30,34,38))
        draw=ImageDraw.Draw(contact)
        for i,png in enumerate(files):
            img=Image.open(png).convert("RGB")
            img.thumbnail((355,350))
            x=(i%4)*360+(360-img.width)//2
            y=(i//4)*390
            contact.paste(img,(x,y))
            draw.text(((i%4)*360+10,y+352),png.stem.split("NATIVE_")[-1],fill=(244,244,244))
        contact.save(O/"run195_TRUE_NATIVE_SEVENVIEW_CONTACT.png")
        q.update({"seven_native_views_success":True,"native_source_sha256":h,"bounds":list(bounds),
                  "imported_props":renderer.GetViewProps().GetNumberOfItems(),
                  "views":[p.name for p in files],"vtk_version":vtk.vtkVersion.GetVTKVersion()})
    except Exception as e:
        q["native_failure"]=repr(e)
        (O/"run195_native_traceback.txt").write_text(traceback.format_exc())
else:
    q["native_skip"]="NO_NEW_VALID_GLB_TO_RENDER"
(O/"run195_native_sevenview_audit.json").write_text(json.dumps(q,indent=2,ensure_ascii=False)+"\n")
print(json.dumps(q,ensure_ascii=False))
