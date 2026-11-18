#!/usr/bin/env python3
"""Run198: only genuinely downloaded glTF binary may be rendered. No placeholder objects."""
from pathlib import Path
import hashlib,json,traceback
R=Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run198-HYPER3D-REAL-NATIVE-NO_RELEASE"
P=O/"run198_NEW_UNREVIEWED_NATIVE.glb"
q={"input_file":P.name,"rendered_actual_GLTF":False,"art_approved":False,
   "physical_phone_GPU_tested":False,"NO_RELEASE":True,"views":[]}
if not P.is_file():
    q["skip"]="NO_VALID_NEW_NATIVE_GLB_ACQUIRED"
else:
    try:
        import vtk
        from PIL import Image,ImageDraw
        win=vtk.vtkRenderWindow()
        win.SetSize(640,640)
        win.SetOffScreenRendering(True)
        imp=vtk.vtkGLTFImporter()
        imp.SetFileName(str(P))
        imp.SetRenderWindow(win)
        imp.Update()
        renderer=win.GetRenderers().GetFirstRenderer()
        if not renderer: raise ValueError("No GLTF scene")
        bounds=renderer.ComputeVisiblePropBounds()
        if bounds[0]>bounds[1]:raise ValueError("Invalid mesh bounds")
        cx,cy,cz=[(bounds[i]+bounds[i+1])/2 for i in (0,2,4)]
        span=max(bounds[1]-bounds[0],bounds[3]-bounds[2],bounds[5]-bounds[4],0.001)
        renderer.SetBackground(0.17,0.19,0.22)
        vectors={
          "front":(0,0,1),"right":(1,0,0),"rear":(0,0,-1),
          "left":(-1,0,0),"above":(0,1,0),"below":(0,-1,0),
          "quarter":(0.7,0.3,0.7)}
        pngs=[]
        for name,v in vectors.items():
            cam=renderer.GetActiveCamera()
            cam.SetFocalPoint(cx,cy,cz)
            cam.SetPosition(cx+span*2.5*v[0],cy+span*2.5*v[1],cz+span*2.5*v[2])
            cam.SetViewUp(0,0,-1) if name in ["above","below"] else cam.SetViewUp(0,1,0)
            cam.ParallelProjectionOn()
            cam.SetParallelScale(span*0.78)
            renderer.ResetCameraClippingRange()
            win.Render()
            f=vtk.vtkWindowToImageFilter()
            f.SetInput(win);f.SetInputBufferTypeToRGB();f.ReadFrontBufferOff();f.Update()
            p=O/("run198_TRUE_NATIVE_"+name+".png")
            w=vtk.vtkPNGWriter()
            w.SetInputConnection(f.GetOutputPort());w.SetFileName(str(p));w.Write()
            if not p.exists() or p.stat().st_size<1500:raise ValueError("No rendered PNG "+name)
            pngs.append(p)
            q["views"].append(p.name)
        canvas=Image.new("RGB",(1360,720),(29,33,37))
        draw=ImageDraw.Draw(canvas)
        for i,p in enumerate(pngs):
            im=Image.open(p).convert("RGB")
            im.thumbnail((330,320))
            x=(i%4)*340+(340-im.width)//2
            y=(i//4)*360
            canvas.paste(im,(x,y))
            draw.text((x+5,y+323),p.stem.split("NATIVE_")[-1],fill="white")
        canvas.save(O/"run198_TRUE_NATIVE_SEVENVIEW_CONTACT.png")
        q.update({"rendered_actual_GLTF":True,"source_sha256":hashlib.sha256(P.read_bytes()).hexdigest(),
          "original_glb_bytes":P.stat().st_size,"bounds":list(bounds),
          "vtk_version":vtk.vtkVersion.GetVTKVersion()})
    except Exception as ex:
        q["exception"]=repr(ex)
        (O/"run198_vtk_traceback.txt").write_text(traceback.format_exc())
(O/"run198_native_sevenview.json").write_text(json.dumps(q,indent=2)+"\n")
print(json.dumps(q,ensure_ascii=False),flush=True)
