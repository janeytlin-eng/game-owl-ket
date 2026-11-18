#!/usr/bin/env python3
"""#172 Run194: independently acquire and inspect a public CC0 owl GLB.
The model is a *source candidate*, not Tyto castanops v3, not an accepted asset.
No geometry fabrication, no texture invention, no integration with the game.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import sys
from datetime import datetime, timezone
from urllib.parse import urlparse
import requests

ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=ROOT/"research-evidence-run194-INNERSCENE-CC0-NATIVE-NO_RELEASE"
OUT.mkdir(parents=True, exist_ok=True)
SOURCE_URL="https://www.innerscene.com/tools/library/3d-parts/owl-d696472a"
DOWNLOAD_URL="https://www.innerscene.com/api/library/owl-d696472a/download"
EXPECTED_REFERENCE_SHA="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
REFERENCE=ROOT/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
REGISTRY=ROOT/"known_rejected_asset_sha256_registry.json"

def sha(data):return hashlib.sha256(data).hexdigest()
def save_json(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False,default=str)+"\n")
def add_error(report, phase, exc):
    report["errors"].append({"phase":phase,"error":str(exc)[:600]})

report={"run":194,"timestamp_utc":datetime.now(timezone.utc).isoformat(),"target":"#172 Tyto castanops v3 rightmost cream mesoptile","source":SOURCE_URL,"download":DOWNLOAD_URL,"release":False,"art_approved":False,"physical_mobile_webgl_tested":False,"errors":[],"preflight":{}}
status="UNSTARTED_NO_RELEASE"
try:
    for path in [REFERENCE,REGISTRY,Path("owl-pet/AGENTS.md"),Path("owl-pet/README.md"),Path("owl-pet/prototype/index.html"),Path("owl-pet/research/species/172-tyto-castanops-v3.md")]:
        if not path.is_file():raise FileNotFoundError(str(path))
        report["preflight"][str(path)]={"sha256":sha(path.read_bytes()),"bytes":path.stat().st_size}
    if report["preflight"][str(REFERENCE)]["sha256"]!=EXPECTED_REFERENCE_SHA:
        raise ValueError("target original image SHA mismatch")
    registry=REGISTRY.read_text()
    report["preflight"]["rejected_registry_bytes"]=len(registry)
    status="PREFLIGHT_OK"
except Exception as e:
    add_error(report,"preflight",e)
    status="PREFLIGHT_BLOCKED_NO_RELEASE"

headers={"User-Agent":"OwlPet172-NonCommercialQA/1.0 (public licensed source verification)"}
if status=="PREFLIGHT_OK":
    try:
        r=requests.get(SOURCE_URL,headers=headers,timeout=(15,35))
        report["page_status"]=r.status_code
        report["page_bytes"]=len(r.content)
        report["page_sha256"]=sha(r.content)
        (OUT/"source_page_http.txt").write_text("status="+str(r.status_code)+"\nfinal_url="+r.url+"\nsha256="+report["page_sha256"]+"\n")
        page=r.text
        license_phrases=["Public domain (CC0)","Free to use, modify and redistribute"]
        report["license_page_assertions"]={p:p.lower() in page.lower() for p in license_phrases}
        if not r.ok or not all(report["license_page_assertions"].values()):
            status="RIGHTS_NOT_VERIFIED_NO_RELEASE"
        else:
            status="CC0_PAGE_VERIFIED"
    except Exception as e:
        add_error(report,"source_page",e)
        status="SOURCE_UNREACHABLE_NO_RELEASE"
    if status=="CC0_PAGE_VERIFIED":
        try:
            response=requests.get(DOWNLOAD_URL,headers=headers,timeout=(20,100),stream=True,allow_redirects=True)
            report["download_http"]={"status":response.status_code,"final_host":urlparse(response.url).netloc,"content_type":response.headers.get("content-type"),"content_length":response.headers.get("content-length")}
            response.raise_for_status()
            chunks=[]
            size=0
            for chunk in response.iter_content(1024*512):
                if chunk:
                    size+=len(chunk)
                    if size>65_000_000:raise ValueError("download exceeds 65MB bound")
                    chunks.append(chunk)
            response.close()
            data=b"".join(chunks)
            report["binary_bytes"]=len(data)
            report["binary_sha256"]=sha(data)
            if len(data)<100000 or data[:4]!=b"glTF":raise ValueError("not a substantial binary glTF")
            version,total=struct.unpack("<II",data[4:12])
            if version!=2 or total!=len(data):raise ValueError("GLB v2 integrity failed")
            jsonlen,jsonmarker=struct.unpack("<I4s",data[12:20])
            if jsonmarker!=b"JSON":raise ValueError("missing GLB JSON chunk")
            gltf=json.loads(data[20:20+jsonlen])
            report["gltf"]={"meshes":len(gltf.get("meshes",[])),"materials":len(gltf.get("materials",[])),"textures":len(gltf.get("textures",[])),"images":len(gltf.get("images",[])),"scenes":len(gltf.get("scenes",[]))}
            report["fingerprint_previously_rejected"]=(report["binary_sha256"] in registry)
            if report["fingerprint_previously_rejected"]:
                status="DUPLICATE_REJECTED_NATIVE_NO_RELEASE"
            else:
                path=OUT/"run194_innerscene_original_QUARANTINED.glb"
                path.write_bytes(data)
                status="ORIGINAL_GLB_DOWNLOADED_NOT_ART_APPROVED"
        except Exception as e:
            add_error(report,"glb_download",e)
            status="NATIVE_DOWNLOAD_FAILED_NO_RELEASE"

if status=="ORIGINAL_GLB_DOWNLOADED_NOT_ART_APPROVED":
    try:
        import numpy as np
        import trimesh
        import vtk
        from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
        from PIL import Image,ImageDraw
        source=OUT/"run194_innerscene_original_QUARANTINED.glb"
        scene=trimesh.load(str(source),force="scene",process=False)
        geometries=[g for g in scene.geometry.values() if isinstance(g,trimesh.Trimesh) and len(g.faces)>0]
        if not geometries:raise ValueError("GLB imported without triangle meshes")
        report["geometry"]={"meshes":len(geometries),"vertices":int(sum(len(g.vertices) for g in geometries)),"triangles":int(sum(len(g.faces) for g in geometries)),"texture_visuals":int(sum(isinstance(g.visual,trimesh.visual.texture.TextureVisuals) for g in geometries))}
        # Trimesh graph geometry transforms are resolved by scene.dump(concatenate=False).
        meshes=scene.dump(concatenate=False)
        if not isinstance(meshes,list):meshes=[meshes]
        meshes=[m for m in meshes if isinstance(m,trimesh.Trimesh) and len(m.faces)]
        bounds=np.array([np.vstack((m.bounds for m in meshes)).min(axis=0),np.vstack((m.bounds for m in meshes)).max(axis=0)])
        center=bounds.mean(axis=0)
        extent=float((bounds[1]-bounds[0]).max())
        report["geometry"]["world_extents"]=(bounds[1]-bounds[0]).tolist()
        report["geometry"]["faces_per_mesh"]=[len(m.faces) for m in meshes][:20]
        renderer=vtk.vtkRenderer()
        renderer.SetBackground(0.94,0.935,0.92)
        renderer.AutomaticLightCreationOff()
        for xyz,intensity in [((3,4,6),1.0),((-3,1,-5),.75),((0,-4,3),.42)]:
            light=vtk.vtkLight()
            light.SetLightTypeToSceneLight()
            light.SetPosition(*xyz);light.SetFocalPoint(*center)
            light.SetIntensity(intensity);renderer.AddLight(light)
        textured_vertex_color_count=0
        for mesh in meshes:
            pts=vtk.vtkPoints()
            pts.SetData(numpy_to_vtk(np.asarray(mesh.vertices,dtype=np.float64),deep=True))
            faces=np.asarray(mesh.faces,dtype=np.int64)
            cells=vtk.vtkCellArray()
            cells.SetCells(len(faces),numpy_to_vtkIdTypeArray(np.column_stack((np.full(len(faces),3,dtype=np.int64),faces)).ravel(),deep=True))
            poly=vtk.vtkPolyData();poly.SetPoints(pts);poly.SetPolys(cells)
            colors=None
            try:
                vis=mesh.visual.to_color()
                vc=np.asarray(vis.vertex_colors)
                if len(vc)==len(mesh.vertices) and vc.shape[1]>=3:
                    colors=np.ascontiguousarray(vc[:,:3],dtype=np.uint8)
            except Exception as e:
                report["errors"].append({"phase":"texture_to_vertex_color","error":str(e)[:100]})
            normals=vtk.vtkPolyDataNormals()
            normals.SetInputData(poly);normals.ComputePointNormalsOn();normals.SplittingOff();normals.Update()
            if colors is not None:
                poly.GetPointData().SetScalars(numpy_to_vtk(colors,deep=True,array_type=vtk.VTK_UNSIGNED_CHAR))
                textured_vertex_color_count+=len(colors)
            mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(normals.GetOutputPort())
            if colors is not None:mapper.ScalarVisibilityOn()
            else:mapper.ScalarVisibilityOff()
            actor=vtk.vtkActor();actor.SetMapper(mapper)
            actor.GetProperty().SetColor(.86,.84,.78)
            actor.GetProperty().SetInterpolationToPhong()
            actor.GetProperty().SetSpecular(.12)
            renderer.AddActor(actor)
        report["geometry"]["vertices_with_color_approximation"]=textured_vertex_color_count
        report["render_qualification"]="Actual GLB mesh with best-effort vertex-color approximation, not exact original PBR texture fidelity"
        window=vtk.vtkRenderWindow()
        window.SetSize(480,480);window.SetMultiSamples(0);window.SetOffScreenRendering(True);window.AddRenderer(renderer)
        views=[("front_posZ",(0,0,1)),("right_posX",(1,0,0)),("back_negZ",(0,0,-1)),("left_negX",(-1,0,0)),("top_posY",(0,1,0)),("bottom_negY",(0,-1,0)),("quarter",(0.8,0.35,1))]
        shots=[]
        for name,v in views:
            direction=np.array(v,dtype=float);direction/=np.linalg.norm(direction)
            camera=renderer.GetActiveCamera()
            camera.SetFocalPoint(*center)
            camera.SetPosition(*(center+direction*max(1,extent)*3.5))
            camera.SetViewUp(*( (0,0,1) if abs(direction[1])>.85 else (0,1,0) ))
            camera.ParallelProjectionOn()
            camera.SetParallelScale(extent*.83)
            renderer.ResetCameraClippingRange()
            window.Render()
            snap=vtk.vtkWindowToImageFilter();snap.SetInput(window);snap.ReadFrontBufferOff();snap.Update()
            namefile="run194_native_"+name+".png"
            writer=vtk.vtkPNGWriter()
            writer.SetInputConnection(snap.GetOutputPort());writer.SetFileName(str(OUT/namefile));writer.Write()
            if (OUT/namefile).stat().st_size<2500:raise ValueError("empty render "+name)
            shots.append(namefile)
        montage=Image.new("RGB",(480*4,480*2),color=(239,238,234))
        for i,name in enumerate(shots):
            image=Image.open(OUT/name).convert("RGB")
            ImageDraw.Draw(image).text((12,14),name.replace("run194_native_",""),fill=(20,20,20))
            montage.paste(image,((i%4)*480,(i//4)*480))
        montage.save(OUT/"run194_NATIVE_SEVENVIEW_CONTACT.png")
        report["actual_views"]=shots
        status="REAL_NATIVE_SOURCE_7VIEW_CREATED_ART_UNREVIEWED_NO_RELEASE"
    except Exception as e:
        add_error(report,"native_import_and_render",e)
        status="NATIVE_RENDER_FAILED_NO_RELEASE"
report["status"]=status
report["no_release_reason"]="Source is an adult/general owl, not verified Tyto castanops age-unknown cream mesoptile. Art, anatomy, license and physical mobile GPU must all pass separately. Do not copy to prototype."
(OUT/"NO_RELEASE.flag").write_text(status+"\nNOT AN APPROVED #172 CHARACTER. No phone-WebGL or sculpt/cream-down validation.\n")
save_json("run194_actual_source_native_metrics.json",report)
manifest={p.name:{"bytes":p.stat().st_size,"sha256":sha(p.read_bytes())} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!="run194_sha256_manifest.json"}
save_json("run194_sha256_manifest.json",manifest)
assert all(sha((OUT/name).read_bytes())==rec["sha256"] for name,rec in manifest.items())
print("RUN194_RESULT "+json.dumps({"status":status,"binary_sha256":report.get("binary_sha256"),"geometry":report.get("geometry"),"views":len(report.get("actual_views",[])),"errors":report["errors"]},default=str),flush=True)
