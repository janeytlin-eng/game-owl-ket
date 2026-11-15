#!/usr/bin/env python3
"""Native Blender 3D Cycles four-view QA for Run97 and unmodified baseline."""
import bpy,sys,pathlib,json,hashlib,math
from mathutils import Vector
args=sys.argv[sys.argv.index("--")+1:]
model=pathlib.Path(args[0]).resolve()
out=pathlib.Path(args[1]).resolve()
prefix=args[2]
out.mkdir(parents=True,exist_ok=True)
assert model.stat().st_size>100000
bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(model))
S=bpy.context.scene
orig=[o for o in S.objects if o.type=="MESH"]
assert len(orig)>10
for o in orig:o.data.calc_loop_triangles()
tri=sum(len(o.data.loop_triangles) for o in orig)
corners=[o.matrix_world @ Vector(v) for o in orig for v in o.bound_box]
lo=Vector([min(v[i] for v in corners) for i in range(3)])
hi=Vector([max(v[i] for v in corners) for i in range(3)])
center=(lo+hi)*.5
S.render.engine="CYCLES"
S.cycles.samples=24
S.cycles.use_denoising=False
bpy.context.view_layer.cycles.use_denoising=False
S.render.resolution_x=420;S.render.resolution_y=420
S.render.resolution_percentage=100
S.render.image_settings.file_format="PNG"
S.render.film_transparent=False
S.view_settings.view_transform="Standard"
S.view_settings.look="Medium High Contrast"
S.view_settings.exposure=-.55
world=bpy.data.worlds.new("Run97 neutral studio")
world.use_nodes=True
world.node_tree.nodes["Background"].inputs["Color"].default_value=(.58,.60,.63,1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value=.7
S.world=world
for name,d,power,size in [
 ("key",(-2.8,-3.7,6.4),240,4.0),
 ("fill",(3.9,-1.9,3.4),120,4.3),
 ("back",(1.5,4.1,5.1),220,3.0)]:
 bpy.ops.object.light_add(type="AREA",location=d)
 lamp=bpy.context.object;lamp.name=name
 lamp.data.energy=power;lamp.data.size=size
 lamp.rotation_euler=(center-lamp.location).to_track_quat("-Z","Y").to_euler()
bpy.ops.object.camera_add()
cam=bpy.context.object;S.camera=cam;cam.data.type="ORTHO"
cam.data.ortho_scale=4.08 # exactly fixed for comparable body-size ratios
renders=[]
for title,pos in [
 ("front",(0,-6,2.12)),
 ("threequarter",(3.8,-5,2.24)),
 ("strict_side",(6,0,2.12)),
 ("rear",(0,6,2.12))]:
 cam.location=Vector(pos)
 cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
 dest=out/(prefix+"_cycles_"+title+".png")
 S.render.filepath=str(dest)
 bpy.ops.render.render(write_still=True)
 assert dest.stat().st_size>5000,dest
 renders.append({"view":title,"file":dest.name,"bytes":dest.stat().st_size,
                 "sha256":hashlib.sha256(dest.read_bytes()).hexdigest()})
 print("RUN97_CYCLES",prefix,title,dest.stat().st_size,flush=True)
info={"render_engine":"Blender Cycles native true 3D, four independent cameras",
      "source":model.name,"import_meshes":len(orig),"triangles":tri,
      "dimensions_m":[round(float(v),4) for v in hi-lo],
      "camera_ortho_scale_m":4.08,"views":renders,
      "aesthetic_acceptance":False,"phone_gpu_tested":False}
(out/(prefix+"_fourview_metrics.json")).write_text(json.dumps(info,indent=2))
