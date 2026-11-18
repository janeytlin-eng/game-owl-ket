#!/usr/bin/env python3
"""Blender only when Run157 acquired real generation-tied GLB; never art-pass by import."""
import bpy, json, math, pathlib, hashlib
from mathutils import Vector
R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run167-SF3D-NATIVE-FOURVIEW-NO_RELEASE"
models=list(O.glob("*_new_ui_generated_3d_UNREVIEWED.glb"))
if not models: raise RuntimeError("No generated model; native QA prohibited")
for no,model in enumerate(models):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(model.resolve()))
    meshes=[ob for ob in bpy.context.scene.objects if ob.type=="MESH"]
    if not meshes:raise RuntimeError("GLB has zero imported mesh objects")
    pts=[ob.matrix_world@Vector(v) for ob in meshes for corner in ob.bound_box for v in [corner]]
    mi=Vector([min(p[i] for p in pts) for i in range(3)])
    ma=Vector([max(p[i] for p in pts) for i in range(3)])
    c=(mi+ma)/2; size=(ma-mi).length; size=max(size,0.01)
    sc=bpy.context.scene;sc.render.engine="BLENDER_EEVEE";sc.render.resolution_x=448;sc.render.resolution_y=448;sc.render.resolution_percentage=100
    sc.render.image_settings.file_format="PNG"
    sc.world = sc.world or bpy.data.worlds.new("Run167_world");sc.world.color=(0.30,0.31,0.34)
    camera_data=bpy.data.cameras.new("uncalibrated_orbit");camera=bpy.data.objects.new("uncalibrated_orbit",camera_data);sc.collection.objects.link(camera);sc.camera=camera
    camera_data.type="ORTHO";camera_data.ortho_scale=size*1.6
    ldata=bpy.data.lights.new("large_area","AREA");light=bpy.data.objects.new("large_area",ldata);sc.collection.objects.link(light)
    light.location=c+Vector((size, size*0.6, size*1.8));ldata.energy=650;ldata.shape="DISK";ldata.size=size*2
    for label,v in [("front_plusY",(0,1,0.12)),("quarter",(0.7,0.7,0.12)),("side_plusX",(1,0,0.12)),("back_minusY",(0,-1,0.12))]:
        camera.location=c+Vector(v).normalized()*size*2.4
        look=c-camera.location;camera.rotation_euler=look.to_track_quat("-Z","Y").to_euler()
        sc.render.filepath=str((O/(model.stem+"_"+label+"_UNREVIEWED.png")).resolve())
        bpy.ops.render.render(write_still=True)
    a={"source":model.name,"sha256":hashlib.sha256(model.read_bytes()).hexdigest(),
       "meshes":len(meshes),"triangles":sum(len(o.data.polygons) for o in meshes),
       "bounds":list(ma-mi),"views":"front+Y,45,side+X,back-Y UNCALIBRATED, four true native camera renders",
       "art_decision":"UNREVIEWED / NO_RELEASE"}
    (O/(model.stem+"_blender_metrics.json")).write_text(json.dumps(a,indent=2))
    print("RUN167_REAL_BLENDER_4_ORBITS_NO_RELEASE",json.dumps(a))
