#!/usr/bin/env python3
"""Actual Blender Cycles native multi-view QA ONLY if Run258 provider produced a real GLB."""
import bpy, pathlib, math, json, hashlib
from mathutils import Vector
R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run258-HY3D-FREE-ACTUAL-BROWSER-NO_RELEASE"
SRC=O/"run258_original_NATIVE_PROVIDER_RESEARCH_ONLY.glb"
assert SRC.is_file() and SRC.stat().st_size>1024,"No provider GLB; do not fake QA"
info=json.loads((O/"run258_status.json").read_text())
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==info["verified_glb"]["sha256"]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(SRC))
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert meshes
pt=[o.matrix_world@Vector(v) for o in meshes for v in o.bound_box]
low=Vector(tuple(min(p[i] for p in pt) for i in range(3)))
high=Vector(tuple(max(p[i] for p in pt) for i in range(3)))
center=(low+high)/2; extent=max(high-low)
assert math.isfinite(extent) and extent>0
scene=bpy.context.scene
if scene.world is None:scene.world=bpy.data.worlds.new("Run258 actual native studio")
scene.world.color=(0.4,0.4,0.4)
scene.render.engine="CYCLES";scene.cycles.samples=16
scene.render.resolution_x=460;scene.render.resolution_y=460
scene.render.resolution_percentage=100
scene.view_layers[0].cycles.use_denoising=False
def light(offset,power):
    data=bpy.data.lights.new("area","AREA");data.energy=power;data.size=extent*4
    ob=bpy.data.objects.new("area",data);scene.collection.objects.link(ob)
    ob.location=center+Vector(offset)*extent
    ob.rotation_euler=(center-ob.location).to_track_quat("-Z","Y").to_euler()
light((-3,-3,3),380)
light((3,1.5,2),200)
cam=bpy.data.objects.new("actual orbit",bpy.data.cameras.new("actual orbit"))
scene.collection.objects.link(cam);scene.camera=cam;cam.data.type="ORTHO"
cam.data.ortho_scale=extent*1.65
for name,deg in (("front",0),("threequarter",45),("side",90),("back",180)):
    a=math.radians(deg)
    cam.location=center+Vector((4*math.sin(a),-4*math.cos(a),1.25))*extent
    cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
    scene.render.filepath=str(O/("run258_"+name+"_ACTUAL_CYCLES_ART_UNREVIEWED.png"))
    bpy.ops.render.render(write_still=True)
record=dict(original_file=str(SRC),blender=bpy.app.version_string,meshes=len(meshes),
    total_polygons=sum(len(x.data.polygons) for x in meshes),
    bounding_box=list(high-low),actual_native_render_views=4,art_approved=False,
    licence_verified=False,real_mobile_tested=False,release="NO_RELEASE")
(O/"run258_blender_actual_qa.json").write_text(json.dumps(record,indent=2)+"\n")
print("RUN258_NATIVE_FOUR_VIEWS",json.dumps(record))
