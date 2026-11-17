#!/usr/bin/env python3
"""Render actually imported 3D GLB in 4 directions with native Blender.

This is evidence, not automated art approval. GLB deleted before archival
until source/redistribution rights independently confirmed.
"""
import bpy, json, math, sys
from pathlib import Path
from mathutils import Vector
args=sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else []
if len(args)<2: raise SystemExit("Usage blender -b -P script.py -- input.glb output_directory")
source=Path(args[0]).resolve(); out=Path(args[1]).resolve(); out.mkdir(parents=True,exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(source))
bpy.context.view_layer.update()
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
if not meshes: raise RuntimeError("GLB contains no actual mesh objects")
vertices=[o.matrix_world @ Vector(v) for o in meshes for v in o.bound_box]
lo=Vector((min(v[i] for v in vertices) for i in range(3)))
hi=Vector((max(v[i] for v in vertices) for i in range(3)))
center=(lo+hi)*0.5
scale=max((hi-lo).length,0.01)
scene=bpy.context.scene
scene.render.engine="CYCLES";scene.cycles.samples=18
scene.render.resolution_x=540;scene.render.resolution_y=540
scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
scene.render.film_transparent=False
scene.world.color=(0.28,0.28,0.28)
# Four neutral area-light views; do not alter the imported source geometry.
def area(name,loc,power,size):
    bpy.ops.object.light_add(type="AREA", location=loc)
    lamp=bpy.context.object;lamp.name=name;lamp.data.energy=power;lamp.data.shape="DISK";lamp.data.size=size
    direction=center-lamp.location;lamp.rotation_euler=direction.to_track_quat("-Z","Y").to_euler()
area("neutral_key",center+Vector((scale*1.0,-scale*0.9,scale*1.35)),850,scale*1.8)
area("neutral_fill",center+Vector((-scale*0.8,-scale*0.25,scale*0.7)),480,scale*1.9)
area("neutral_rim",center+Vector((scale*0.2,scale*1.2,scale*0.85)),620,scale*1.5)
bpy.ops.object.camera_add()
camera=bpy.context.object;camera.name="Run129EvidenceCamera";scene.camera=camera
camera.data.type="ORTHO";camera.data.ortho_scale=scale*1.4
metrics={"source_glb":source.name,"object_count":len(meshes),
         "mesh_objects":[{"name":o.name,"vertices":len(o.data.vertices),
                          "faces":len(o.data.polygons)} for o in meshes[:80]],
         "total_faces":sum(len(o.data.polygons) for o in meshes),
         "materials":list({m.name for o in meshes for m in o.data.materials if m}),
         "bounds_min":list(lo),"bounds_max":list(hi),"size":list(hi-lo),
         "render_engine":"CYCLES_CPU","render_samples":18,
         "views":[],"art_gate":"ART_UNREVIEWED","release":"NO_RELEASE",
         "caution":"Angles are nominal rotations and do not prove that the mesh is an anatomic owl chick."}
for name,theta in [("front_nominal",0),("front_45deg",45),("side_90deg",90),("back_180deg",180)]:
    r=math.radians(theta)
    camera.location=center+Vector((math.sin(r)*scale*1.65,-math.cos(r)*scale*1.65,scale*0.18))
    camera.rotation_euler=(center-camera.location).to_track_quat("-Z","Y").to_euler()
    scene.render.filepath=str(out/("run129_"+name+".png"))
    bpy.ops.render.render(write_still=True)
    metrics["views"].append({"angle_degrees":theta,"file":Path(scene.render.filepath).name})
(out/"run129_blender_four_view_metrics.json").write_text(json.dumps(metrics,indent=2)+"\n")
print("RUN129_NATIVE_RENDER_SUCCESS",json.dumps({"total_faces":metrics["total_faces"],"views":metrics["views"]}))
