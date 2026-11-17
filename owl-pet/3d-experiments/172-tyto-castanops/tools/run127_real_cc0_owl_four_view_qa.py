#!/usr/bin/env python3
"""Run127 actual native Blender inspection of REAL CC0 source owl.
No synthetic meshes, no beautifying proxy, NO_RELEASE. Source toy-owl is not juvenile castanops.
"""
import sys,pathlib,json,hashlib,math
import bpy
from mathutils import Vector
assert "--" in sys.argv, "usage blender -b --python ... -- SRC_GLb OUT"
args=sys.argv[sys.argv.index("--")+1:]
src=pathlib.Path(args[0]); out=pathlib.Path(args[1]);out.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
EXPECTED="a22017221687458f37b76991719cb80243b5f04554ae57f07503139f988add3f"
assert sha(src)==EXPECTED,"Source CC0 GLB hash changed, stop"
assert src.read_bytes()[:4]==b"glTF"
bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(src))
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert meshes,"No actual GLB meshes"
src_data=[]
for o in meshes:
    o.data.calc_loop_triangles()
    src_data.append({"mesh":o.name,"vertices":len(o.data.vertices),"polygons":len(o.data.polygons),
                     "triangles":len(o.data.loop_triangles),"visible_before":not o.hide_render,
                     "material_count":len(o.data.materials)})
armatures=[o.name for o in bpy.context.scene.objects if o.type=="ARMATURE"]
actions=[a.name for a in bpy.data.actions]
# Inspect professional-art silhouette from real detailed LOD0 only; do not visually superimpose both LODs.
lod1=[o for o in meshes if "lod1" in o.name.lower()]
lod0=[o for o in meshes if "lod0" in o.name.lower()]
for o in lod1:o.hide_render=True
main=lod0 if lod0 else meshes
pts=[o.matrix_world@v.co for o in main for v in o.data.vertices]
low=Vector(tuple(min(p[k] for p in pts) for k in range(3)))
high=Vector(tuple(max(p[k] for p in pts) for k in range(3)))
center=(low+high)*.5;extent=high-low;L=max(extent)
assert 0<L<10000,"Invalid bounds"
sc=bpy.context.scene
sc.render.engine="CYCLES";sc.cycles.samples=24;sc.cycles.use_denoising=False
for layer in sc.view_layers:layer.cycles.use_denoising=False
sc.render.resolution_x=520;sc.render.resolution_y=520;sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG";sc.view_settings.view_transform="Standard"
sc.world.color=(.20,.22,.24)
def light(label,pos,energy,size):
    l=bpy.data.lights.new(label,"AREA");l.energy=energy;l.size=size*L
    o=bpy.data.objects.new(label,l);sc.collection.objects.link(o)
    o.location=center+Vector(pos)*L
    o.rotation_euler=(center-o.location).to_track_quat("-Z","Y").to_euler()
light("warm_key",(-2.3,-2.8,2.6),500,3)
light("fill",(2.2,-1.4,1.6),260,2.8)
light("rim",(1.5,2.5,2.1),350,2.6)
camera=bpy.data.cameras.new("technical_orbit")
cam=bpy.data.objects.new("technical_orbit",camera);sc.collection.objects.link(cam);sc.camera=cam
camera.type="ORTHO";camera.ortho_scale=L*1.65
angles=(("front",0),("quarter",45),("side",90),("back",180))
for name,angle in angles:
    t=math.radians(angle)
    cam.location=center+Vector((3.5*math.sin(t),-3.5*math.cos(t),.55))*L
    cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
    sc.render.filepath=str(out/("run127_"+name+"_real_cycles_NOT_ART_APPROVED.png"))
    bpy.ops.render.render(write_still=True)
report={"run":"127","date":"2026-11-17","model":"actual Vuena CC0 owl from itch.io free zip",
        "source_url":"https://vuena.itch.io/blocky-pets-free","source_bytes":src.stat().st_size,
        "source_sha256":EXPECTED,"blender_version":bpy.app.version_string,
        "meshes":src_data,"lod0_names":[o.name for o in lod0],"lod1_names":[o.name for o in lod1],
        "skeleton_objects":armatures,"blender_actions":actions,"source_materials":list(m.name for m in bpy.data.materials),
        "main_view_bounds_unverified_units":list(extent),"rendered_native_views":[name for name,_ in angles],
        "rendering_method":"real GLB import Cycles 24 samples, four true orbital views, LOD1 hidden to prevent duplicate LOD ghosting",
        "art_result":"ART_REJECTED: blocky low-poly toy owl is NOT cream downy age-unknown Tyto castanops; no anatomically faithful heart disc, down, short folded wings or eucalypt hollow",
        "mobile_phone_gpu":"NOT TESTED, SwiftShader software browser only if browser step passes",
        "license":"Official creator listing and free ZIP license claim CC0, upstream originality not independently proven",
        "payment_usd":0,"release":False}
(out/"run127_blender_real_mesh_lod_four_angle_metrics.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
print("RUN127_NATIVE_CYCLES_FOUR_REAL_VIEWS_ART_REJECTED",json.dumps(report,ensure_ascii=False),flush=True)
