#!/usr/bin/env python3
"""Independent TRUE 3D six-axis Blender visual QA of Run175/176 image-bound GLB.

Re-uses the exact verified Run175/176 image-generated 90,618-triangle file.
No generation, no paid service, no primitive substitute. Candidate NO_RELEASE
unless art and real phone WebGL are both independently accepted.
"""
import bpy
import hashlib
import json
import math
import os
import traceback
from pathlib import Path
from mathutils import Vector
import urllib.request

BASE=Path(__file__).resolve().parent.parent
OUT=BASE/"research-evidence-run177-BLENDER-REAL-NEURAL-SIXVIEW-NO_RELEASE"
OUT.mkdir(exist_ok=True,parents=True)
SOURCE_URL="https://three.ws/cdn/forge/anon/083fb94e-8cc3-46c7-8f97-d6f699554654.glb"
EXPECTED_SHA="c56c1a1c0159e11a140f587f12ad4c84b49fdb38b9b3142078f3de9d75f46e99"
REFERENCE_SHA="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
REJECTS=BASE/"known_rejected_asset_sha256_registry.json"
SRC=BASE/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED/rightmost_mesoptile_input.png"
STATE={"run":177,"source":"Run175 image-bound three.ws mesh, Run176 recovered GLB",
       "source_glb_url":SOURCE_URL,"expected_glb_sha256":EXPECTED_SHA,
       "source_ref_sha256":REFERENCE_SHA,"model_provenance":"image-conditioned free MCP, NOT text-only",
       "additional_payments_usd":0,"art":"UNREVIEWED","release":False,
       "mobile_phone_gpu":"NOT_TESTED"}
def save():
    (OUT/"run177_metrics.json").write_text(json.dumps(STATE,ensure_ascii=False,indent=2))
def normalize_faces():
    return [obj for obj in bpy.context.scene.objects if obj.type=="MESH"]
def run():
    # Local reference & rejected asset registry revalidated
    assert SRC.is_file() and REJECTS.is_file()
    assert hashlib.sha256(SRC.read_bytes()).hexdigest()==REFERENCE_SHA
    previous=REJECTS.read_text()
    assert EXPECTED_SHA not in previous, "Previously rejected mesh must not be repeated"
    STATE["preflight"]="PASS"
    save()
    request=urllib.request.Request(SOURCE_URL,headers={
        "User-Agent":"Mozilla/5.0 (compatible; Owl172Run177Audit)",
        "Accept":"application/octet-stream"})
    glb=OUT/"run177_neural_image_bound_UNREVIEWED.glb"
    n=0
    with urllib.request.urlopen(request,timeout=180) as response, glb.open("wb") as f:
        STATE["source_get_http"]=response.status
        assert response.status==200
        while True:
            chunk=response.read(1048576)
            if not chunk:break
            n+=len(chunk)
            assert n<32*1024*1024,"excessive_glb_size"
            f.write(chunk)
    sha=hashlib.sha256(glb.read_bytes()).hexdigest()
    STATE["glb"]={"sha256":sha,"bytes":glb.stat().st_size}
    assert sha==EXPECTED_SHA and glb.read_bytes()[:4]==b"glTF","source_model_changed"
    STATE["verified_glb"]=True
    save()

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(glb))
    meshes=normalize_faces()
    assert meshes,"Blender glTF import yielded no real mesh"
    STATE["mesh_count"]=len(meshes)
    STATE["triangle_count"]=sum(sum(len(poly.vertices)-2 for poly in m.data.polygons) for m in meshes)
    STATE["vertices_count"]=sum(len(m.data.vertices) for m in meshes)
    STATE["materials"]=sorted({material.name for obj in meshes for material in obj.data.materials if material})
    STATE["images"]=[{"name":image.name,"size":list(image.size)} for image in bpy.data.images]
    STATE["import"]="REAL_GLTF_IMPORT_PASS"
    assert STATE["triangle_count"]>=1000 and STATE["triangle_count"]<=2000000
    # Use WORLD bounds after import to capture transforms and scale.
    coords=[o.matrix_world @ Vector(v) for o in meshes for v in o.bound_box]
    mins=Vector(tuple(min(p[j] for p in coords) for j in range(3)))
    maxs=Vector(tuple(max(p[j] for p in coords) for j in range(3)))
    center=(mins+maxs)/2
    dims=maxs-mins
    extent=max(dims)
    assert extent>0.001 and extent<1e6
    STATE["bbox_world"]={"min":list(mins),"max":list(maxs),"span":list(dims)}
    save()

    scene=bpy.context.scene
    scene.render.engine="CYCLES"
    scene.cycles.samples=16
    try: scene.cycles.use_denoising=True
    except AttributeError: pass
    scene.render.resolution_x=440
    scene.render.resolution_y=440
    scene.render.resolution_percentage=100
    scene.render.image_settings.file_format="PNG"
    scene.render.film_transparent=False
    # Neutral stage, no additional 3D shapes (no invented anatomy).
    scene.world=bpy.data.worlds.new("Neutral QA light world")
    scene.world.use_nodes=True
    background=scene.world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value=(0.22,0.24,0.28,1)
    background.inputs["Strength"].default_value=.75
    scene.view_settings.view_transform="Standard"
    try: scene.view_settings.look="Medium High Contrast"
    except TypeError: scene.view_settings.look="Medium High Contrast"

    def area(name, vector, power, size):
        data=bpy.data.lights.new(name=name,type="AREA")
        data.energy=power
        data.shape="DISK"
        data.size=size
        ob=bpy.data.objects.new(name,data)
        bpy.context.collection.objects.link(ob)
        ob.location=center+Vector(vector)*extent
        ob.rotation_euler=(center-ob.location).to_track_quat("-Z","Y").to_euler()
        return ob
    area("Key",(-1.5,-1.7,2.8),720,4.5*extent)
    area("Fill",(1.6,-0.6,1.3),440,4.0*extent)
    area("Back",(0,2.2,1.7),640,3.7*extent)
    camera_data=bpy.data.cameras.new("orthographic_qa_camera")
    camera=bpy.data.objects.new("orthographic_qa_camera",camera_data)
    bpy.context.collection.objects.link(camera)
    scene.camera=camera
    camera_data.type="ORTHO"
    camera_data.ortho_scale=extent*1.45

    views=[
        ("axis_negY",(0,-1,.08)),
        ("axis_negY_oblique",(0.7,-1,.1)),
        ("axis_posX",(1,0,.1)),
        ("axis_posY",(0,1,.08)),
        ("axis_negX",(-1,0,.1)),
        ("axis_posZ",(0,.1,1)),
        ("axis_negZ",(0,.1,-1)),
    ]
    images=[]
    for label,direction in views:
        offset=Vector(direction).normalized()*extent*3
        camera.location=center+offset
        camera.rotation_euler=(center-camera.location).to_track_quat("-Z","Y").to_euler()
        bpy.context.view_layer.update()
        scene.camera=camera
        scene.render.filepath=str(OUT/("run177_"+label+"_UNREVIEWED.png"))
        bpy.ops.render.render(write_still=True)
        p=Path(scene.render.filepath)
        assert p.stat().st_size>3000, "empty_render"
        images.append((label,p))
    for label,p in images:
        assert p.exists() and p.stat().st_size>3000
    STATE["render_images_without_contact_sheet"]=[p.name for _,p in images]
    STATE["native_qa"]={"render_engine":"Blender "+bpy.app.version_string+" Cycles",
        "views":len(images),"resolution":"440x440","image_files":[p.name for _,p in images],
        "technical":"PASS","art":"UNREVIEWED"}
    STATE["status"]="BLENDER_REAL_MESH_SEVEN_AXIS_RENDERED_NO_RELEASE"
    STATE["art"]="UNREVIEWED"
    save()
try:
    run()
except Exception as e:
    STATE["status"]="BLENDER_NATIVE_QA_ERROR"
    STATE["exception"]=repr(e)
    (OUT/"run177_exception_traceback.txt").write_text(traceback.format_exc())
    save()
    raise
finally:
    (OUT/"NO_RELEASE.flag").write_text("NO_RELEASE: GLB and image render, if present, are unreviewed; NO real mobile hardware verification; no payment.\n")
    manifest={p.name:{"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
              for p in OUT.iterdir() if p.is_file() and not p.name.endswith("sha256_manifest.json")}
    (OUT/"run177_sha256_manifest.json").write_text(json.dumps(manifest,indent=2))
    print("RUN177_FINAL",STATE.get("status"),"TRIANGLES",STATE.get("triangle_count",0),
          "FILES",len(manifest),flush=True)
