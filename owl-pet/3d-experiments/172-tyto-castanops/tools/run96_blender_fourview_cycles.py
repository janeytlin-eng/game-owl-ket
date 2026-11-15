#!/usr/bin/env python3
"""Native Blender true-mesh 4-azimuth QA; does not approve the art."""
import bpy,sys,pathlib,json,hashlib,math
from mathutils import Vector
out=pathlib.Path(sys.argv[sys.argv.index("--")+1]).resolve()
model=out/"run96_anatomy_directional_down_NOT_APPROVED.glb"
assert model.exists()
bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(model))
S=bpy.context.scene
orig=[o for o in S.objects if o.type=="MESH"]
assert len(orig)>5
for o in orig:o.data.calc_loop_triangles()
tri=sum(len(o.data.loop_triangles) for o in orig)
corners=[o.matrix_world @ Vector(v) for o in orig for v in o.bound_box]
lo=Vector([min(v[i] for v in corners) for i in range(3)])
hi=Vector([max(v[i] for v in corners) for i in range(3)])
center=(lo+hi)*.5; extent=max(hi-lo)
S.render.engine="CYCLES"
S.cycles.samples=24;S.cycles.use_denoising=False
bpy.context.view_layer.cycles.use_denoising=False
S.render.resolution_x=520;S.render.resolution_y=520
S.render.resolution_percentage=100
S.render.image_settings.file_format="PNG"
S.render.film_transparent=False
S.view_settings.view_transform="Standard"
S.view_settings.look="Medium High Contrast"
S.view_settings.exposure=-.35
world=bpy.data.worlds.new("neutral studio for independent evidence")
world.use_nodes=True
world.node_tree.nodes["Background"].inputs["Color"].default_value=(.58,.60,.63,1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value=.7
S.world=world
for name,d,power,size in [
    ("key",(-2.8,-3.7,6.4),420,4.0),
    ("fill",(3.9,-1.9,3.4),180,4.3),
    ("back",(1.5,4.1,5.1),380,3.0)]:
    bpy.ops.object.light_add(type="AREA",location=d)
    light=bpy.context.object;light.name=name
    light.data.energy=power;light.data.size=size
    light.rotation_euler=(center-light.location).to_track_quat("-Z","Y").to_euler()
bpy.ops.object.camera_add()
cam=bpy.context.object;S.camera=cam;cam.data.type="ORTHO"
cam.data.ortho_scale=extent*1.36
renders=[]
for title,pos in [
    ("front",(0,-6,2.12)),
    ("threequarter",(3.8,-5,2.24)),
    ("strict_side",(6,0,2.12)),
    ("rear",(0,6,2.12))]:
    cam.location=Vector(pos)
    cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
    dest=out/("run96_actual_cycles_"+title+".png")
    S.render.filepath=str(dest)
    bpy.ops.render.render(write_still=True)
    assert dest.stat().st_size>5000
    renders.append({"view":title,"file":dest.name,"bytes":dest.stat().st_size,
                    "sha256":hashlib.sha256(dest.read_bytes()).hexdigest()})
    print("RUN96_NATIVE_CYCLES_RENDER",title,dest.stat().st_size,flush=True)
info={"render_engine":"Blender 4.x Cycles CPU true GLB import",
      "imported_mesh_count":len(orig),"triangles":tri,
      "bounds_m":[round(float(v),4) for v in hi-lo],
      "renders":renders,"aesthetic_verdict":"PENDING_MANUAL_IMAGE_INSPECTION",
      "real_phone_gpu":False}
(out/"run96_fourview_metrics.json").write_text(json.dumps(info,indent=2))
print("RUN96_NATIVE_RENDER_COMPLETED",json.dumps(info),flush=True)
