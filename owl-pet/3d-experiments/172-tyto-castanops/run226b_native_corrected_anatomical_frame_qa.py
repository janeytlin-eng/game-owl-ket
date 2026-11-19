#!/usr/bin/env python3
"""Run226: genuine scanned Tyto alba surface, two continuous non-rigid juvenile-shape trials.

IMPORTANT: This is NOT an approved #172 Tyto castanops young pet.
Do not conflate authentic scanned adult surface, a geometry morph, and biological
juvenile anatomy. No donor model is deployed or credited to species production.
No synthetic 2-D view rotation: seven independent native 3-D camera renders per trial.
"""
import datetime as dt
import hashlib
import io
import json
import math
import pathlib
import subprocess
import traceback

import numpy as np
import requests
import trimesh
import vtk
from PIL import Image, ImageDraw, ImageFont
from vtk.util.numpy_support import numpy_to_vtk, numpy_to_vtkIdTypeArray

ROOT=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=ROOT/"run226b-evidence"
OUT.mkdir(parents=True,exist_ok=True)
UID="0e65de5934db4f0eae02835ba7227dcc"
DESIGN=pathlib.Path("owl-pet/design/concepts/172-tyto-castanops-v3.png")
KNOWN="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
MODEL=UID+"_normalized_optimized-0.250.glb"
URL="https://zenodo.org/api/records/21379215/files/"+MODEL+"/content"
DATA={"run":"226b","created_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
      "source":{"archive":"Zenodo 21379215 / Virtual Museums of Malopolska",
                "filename":MODEL,"license_claim":"CC0 on Zenodo archive (adult Barn Owl Tyto alba)",
                "expected_bytes":2185576,"url":URL},
      "subject":"#172 Tyto castanops v3 rightmost cream mesoptile",
      "methods":"Adult genuine 3D scan followed by two novel continuous spatial deformation fields, no primitive replacement",
      "license_note":"Source is museum adult Tyto alba, not species-correct or age-correct character",
      "release":"NO_RELEASE","art_review":"PENDING_MANUAL_REJECT_BY_DEFAULT",
      "real_phone_webgl":"NOT_TESTED","paid_usd":0,"variants":{},"errors":[],"files":{}}
def sha(p):
    return {"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def trace(stage,e):
    DATA["errors"].append({"stage":stage,"error":repr(e),
                           "trace":traceback.format_exc()[-1300:]})
def native_mesh(p):
    s=trimesh.load(str(p),force="scene",process=False)
    geos=[g for g in s.dump() if isinstance(g,trimesh.Trimesh) and len(g.faces)]
    if not geos: raise ValueError("no 3-D mesh")
    xyz=np.concatenate([g.vertices for g in geos],axis=0)
    spans=np.ptp(xyz,axis=0)
    if not np.all(np.isfinite(xyz)) or max(spans)<0.05 or np.sum(spans>0.001)<2:
        raise ValueError("invalid or Draco-undecoded spatial vertices "+str(spans))
    return geos,{"mesh_count":len(geos),"triangles":sum(len(g.faces) for g in geos),
                 "vertex_count":len(xyz),"bounds":np.vstack((xyz.min(axis=0),xyz.max(axis=0))).round(5).tolist(),
                 "span":spans.round(5).tolist()}
def model_morph(geos,kind):
    coords=np.concatenate([g.vertices for g in geos],axis=0)
    lo=np.min(coords,axis=0);hi=np.max(coords,axis=0);dims=hi-lo
    up=int(np.argmax(dims));lateral=[i for i in range(3) if i!=up]
    ctr=(lo+hi)*0.5
    # Only the scanner's spatial geometry supplies details. Geometry remains a
    # single warped native scan, retaining folds/eyes/face relief where present.
    # An adult can still fail biologically after a visually successful transform.
    params={"compact":{"height":0.84,"head_bulge":0.17,"body_bulge":0.13,"foot_lift":0.05},
            "crouched":{"height":0.72,"head_bulge":0.27,"body_bulge":0.18,"foot_lift":0.085}}[kind]
    new=[]
    for g in geos:
        h=g.copy()
        v=np.array(g.vertices,copy=True,dtype=np.float64)
        t=np.clip((v[:,up]-lo[up])/dims[up],0,1)
        head=np.exp(-0.5*((t-.785)/.155)**2)
        belly=np.exp(-0.5*((t-.41)/.23)**2)
        lower=np.exp(-0.5*((t-.12)/.1)**2)
        # Preserve facial mesh topology and texture coordinates. The head
        # expands in both horizontal directions in contrast to merely scaling
        # the entire adult GLB. Smoothly compress the long lower adult form.
        for j,axis in enumerate(lateral):
            radial=(v[:,axis]-ctr[axis])
            fac=1+params["head_bulge"]*head+params["body_bulge"]*belly-0.08*lower
            if j==1: fac=1+(fac-1)*0.83
            v[:,axis]=ctr[axis]+radial*fac
        v[:,up]=lo[up]+dims[up]*(params["height"]*t+
                              params["foot_lift"]*np.sin(math.pi*t)**2)
        h.vertices=v
        new.append(h)
    sc=trimesh.Scene()
    for i,g in enumerate(new): sc.add_geometry(g,node_name=kind+"_"+str(i),
                                               geom_name=kind+"_"+str(i))
    return sc,params
def vtk_render(name,geos,view_size=380):
    ren=vtk.vtkRenderer();win=vtk.vtkRenderWindow()
    win.SetOffScreenRendering(1);win.SetSize(view_size,view_size)
    ren.SetBackground(.91,.915,.925);win.AddRenderer(ren)
    tex_used=0
    texture_paths=[]
    for i,g in enumerate(geos):
        poly=vtk.vtkPolyData()
        pts=vtk.vtkPoints()
        pts.SetData(numpy_to_vtk(np.asarray(g.vertices,dtype=np.float64),deep=True))
        poly.SetPoints(pts)
        faces=np.column_stack((np.full(len(g.faces),3,dtype=np.int64),
                               np.asarray(g.faces,dtype=np.int64))).ravel()
        cells=vtk.vtkCellArray()
        cells.SetCells(len(g.faces),numpy_to_vtkIdTypeArray(faces,deep=True))
        poly.SetPolys(cells)
        mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
        actor=vtk.vtkActor();actor.SetMapper(mapper)
        actor.GetProperty().SetColor(.76,.69,.59)
        actor.GetProperty().SetInterpolationToPhong()
        material=getattr(g.visual,"material",None)
        tex=getattr(material,"baseColorTexture",None)
        if tex is None: tex=getattr(material,"image",None)
        uv=getattr(g.visual,"uv",None)
        if tex is not None and uv is not None and len(uv)==len(g.vertices):
            try:
                im=Image.fromarray(np.asarray(tex)).convert("RGB")
                q=OUT/("run226b_"+name+"_native_tex_"+str(i)+".png")
                im.save(q);texture_paths.append(q.name)
                tc=numpy_to_vtk(np.asarray(uv,dtype=np.float32),deep=True)
                tc.SetName("uv");poly.GetPointData().SetTCoords(tc)
                reader=vtk.vtkPNGReader();reader.SetFileName(str(q));reader.Update()
                tx=vtk.vtkTexture();tx.SetInputConnection(reader.GetOutputPort())
                tx.InterpolateOn();actor.SetTexture(tx);tex_used+=1
            except Exception as e: DATA["variants"].setdefault(name,{}).setdefault("texture_errors",[]).append(repr(e))
        ren.AddActor(actor)
    bounds=ren.ComputeVisiblePropBounds()
    lo=np.array([bounds[2*i] for i in range(3)])
    hi=np.array([bounds[2*i+1] for i in range(3)])
    dims=hi-lo
    up=2;lat=[0,1] # Explicit Z-up diagnosis: source 0.25 LOD has longest Y span due to museum display branch
    center=(lo+hi)/2;diameter=float(dims.max())
    views=[]
    for angle in (0,45,90,135,180,225,270):
        vec=np.zeros(3);a=math.radians(angle)
        vec[lat[0]]=math.cos(a);vec[lat[1]]=math.sin(a)
        camera=ren.GetActiveCamera();camera.ParallelProjectionOn()
        camera.SetFocalPoint(*center)
        camera.SetPosition(*(center+3*diameter*vec))
        camera.SetViewUp(*np.eye(3)[up])
        camera.SetParallelScale(.72*diameter)
        ren.ResetCameraClippingRange();win.Render()
        q=OUT/("run226b_"+name+"_azimuth"+str(angle)+".png")
        filt=vtk.vtkWindowToImageFilter();filt.SetInput(win);filt.Update()
        wr=vtk.vtkPNGWriter();wr.SetFileName(str(q))
        wr.SetInputConnection(filt.GetOutputPort());wr.Write()
        ar=np.array(Image.open(q).convert("RGB")).astype(np.int16)
        fg=int((np.max(np.abs(ar-np.array([232,233,236])),axis=2)>27).sum())
        if fg<400: raise ValueError("EMPTY_NATIVE_RENDER "+name+" "+str(angle)+" "+str(fg))
        views.append((angle,q,fg))
    return views,{"native_triangles":sum(len(g.faces) for g in geos),
                  "native_textures_used":tex_used,"native_texture_paths":texture_paths,
                  "camera_up_axis_inferred":up,"rendered_views":len(views),
                  "foreground_pixels":[x[2] for x in views],
                  "render_PBR_caveat":"VTK does not reproduce glTF full PBR or normal map"}
def montage(sets):
    wh=380
    im=Image.new("RGB",(4*wh,3*(wh+36)+80),(244,244,244))
    draw=ImageDraw.Draw(im)
    for k,(name,views) in enumerate(sets.items()):
        for i,(deg,q,_) in enumerate(views):
            x=(i%4)*wh;y=k*(wh+36)+(i//4)*(wh+36)
            im.paste(Image.open(q).convert("RGB"),(x,y+25))
            draw.text((x+12,y+5),name+": true mesh camera "+str(deg)+" deg",fill=(30,30,30))
    # If 2 variants, an independent label clearly distinguishes 2-D original.
    draw.text((10,im.height-58),"ADULT ARCHIVAL SCAN AND SCULPT RESEARCH ONLY. NOT A YOUNG TYTO MODEL.",fill=(140,30,30))
    draw.text((10,im.height-34),"NO_RELEASE / no down material / no real phone WebGL test",fill=(140,30,30))
    im.save(OUT/"run226b_true3d_nonrigid_donor_7view_comparison_NOT_APPROVED.png")
try:
    DATA["reference"]=sha(DESIGN)
    assert DATA["reference"]["sha256"]==KNOWN,"Original species reference changed"
    # Immutable 2-D guide, never shown as 3-D evidence:
    crop=Image.open(DESIGN).convert("RGB").crop((950,255,1440,850))
    crop.save(OUT/"run226b_reference_CROP_ONLY_2D.png")
    r=requests.get(URL,timeout=(25,110))
    DATA["source"]["http"]=r.status_code
    r.raise_for_status()
    orig=OUT/"run226b_museum_adult_draco_original_ONLY.glb"
    orig.write_bytes(r.content)
    DATA["source"]["downloaded"]=sha(orig)
    if orig.stat().st_size!=2185576: raise ValueError("museum source byte mismatch")
    decomp=OUT/"run226b_museum_adult_native_decoded_ONLY.glb"
    run=subprocess.run(["gltf-transform","copy",str(orig),str(decomp)],
                       capture_output=True,text=True,timeout=240)
    DATA["source"]["draco_decoder"]={"rc":run.returncode,"log":(run.stdout+run.stderr)[-1500:]}
    if run.returncode: raise RuntimeError("Draco decode failed")
    DATA["source"]["decoded_sha"]=sha(decomp)
    geos,base_stats=native_mesh(decomp)
    DATA["source"]["actual_native_geometry"]=base_stats
    comp=trimesh.util.concatenate(geos).split(only_watertight=False)
    DATA["source"]["connected_component_analysis"]=[
        {"triangles":int(len(p.faces)),"bounds":np.asarray(p.bounds).round(4).tolist()}
        for p in sorted(comp,key=lambda p:len(p.faces),reverse=True)[:15]]
    DATA["source"]["component_count"]=len(comp)
    rendered={}
    baseline_views,baseline_rs=vtk_render("original_adult",geos)
    rendered["original_adult"]=baseline_views
    DATA["source"]["adult_original_native_views"]=baseline_rs
    for name in ("compact","crouched"):
        try:
            sc,params=model_morph(geos,name)
            out=OUT/("run226b_"+name+"_REAL_SCAN_DEFORMED_ART_UNAPPROVED.glb")
            sc.export(str(out))
            checked,stats=native_mesh(out)
            v,rs=vtk_render(name,checked)
            rendered[name]=v
            DATA["variants"].setdefault(name,{}).update({"params":params,"file":out.name,
                                          "sha256":sha(out),"geometry":stats,"renders":rs,
                                          "art":"NOT_APPROVED"})
        except Exception as e: trace("variant_"+name,e)
    if len(rendered)==3:
        # Composite row length of four cameras, two rows per variant.
        panel=Image.new("RGB",(4*380,6*415+70),(243,244,246))
        pen=ImageDraw.Draw(panel)
        for j,(name,views) in enumerate(rendered.items()):
            for i,(deg,q,fg) in enumerate(views):
                x=(i%4)*380;y=j*830+(i//4)*415
                panel.paste(Image.open(q).convert("RGB"),(x,y+26))
                pen.text((x+8,y+5),name+" real 3-D "+str(deg)+" deg",fill=(33,33,33))
        pen.text((12,2490),"SCANNED ADULT DONOR MORPHS ONLY — NOT NATURAL CREAM DOWN YOUNG",fill=(150,20,20))
        pen.text((12,2515),"ART_REVIEW_REQUIRED / NO_PHONE_WEBGL / NO_RELEASE",fill=(150,20,20))
        panel.save(OUT/"run226b_true3d_nonrigid_donor_21views_NOT_APPROVED.png")
        DATA["result"]="TWO_NATIVE_SCAN_MORPHS_GLBS_AND_TWENTY_ONE_VIEWS_ART_UNAPPROVED_NO_RELEASE"
    else: DATA["result"]="PARTIAL_MORPH_GENERATION_NO_RELEASE"
except Exception as e:
    trace("fatal",e)
    DATA["result"]="FAILED_NO_RELEASE"
finally:
    DATA["finished_utc"]=dt.datetime.now(dt.timezone.utc).isoformat()
    for p in OUT.iterdir():
        if p.is_file() and p.name!="run226b_report.json": DATA["files"][p.name]=sha(p)
    (OUT/"run226b_report.json").write_text(json.dumps(DATA,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"result":DATA["result"],"variants":list(DATA["variants"]),
                      "errors":[x["error"] for x in DATA["errors"]],
                      "release":"NO_RELEASE"},ensure_ascii=False),flush=True)
