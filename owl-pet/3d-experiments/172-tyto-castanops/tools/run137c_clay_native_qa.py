#!/usr/bin/env python3
"""Run137C: native four-view Blender replay of genuine public Run137 GLB only.
NO new inference; no paid tools; no glTF release or approval.
The archived original Run137 artifact's SHA256 is a hard precondition.
"""
import bpy, json, hashlib, math, pathlib, sys
from mathutils import Vector
R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run137c-NATIVE-REPLAY-ART_REJECTED-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
S=pathlib.Path("/tmp/owl137_original/run137_verified_raw_provider_RESEARCH_ONLY.glb")
PIN="b65fe7ca77aee54806792f473f15282000a5adc1f3798283a83c1b9bc928630d"
if not S.is_file(): raise RuntimeError("Original real Run137 GLB not downloaded; render must fail, not fabricate")
actual=hashlib.sha256(S.read_bytes()).hexdigest()
if actual != PIN:raise RuntimeError(f"Source SHA256 mismatch {actual}")
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(S))
meshes=[obj for obj in bpy.context.scene.objects if obj.type=="MESH"]
assert meshes,"No genuine model mesh after Blender import"
points=[obj.matrix_world@Vector(v) for obj in meshes for v in obj.bound_box]
low=Vector(tuple(min(v[i] for v in points) for i in range(3)))
high=Vector(tuple(max(v[i] for v in points) for i in range(3)))
center=(low+high)*0.5
extent=max(high-low)
scene=bpy.context.scene
# QA-only uniform grey clay material: no attempt to simulate or fake feathers.
# This reveals generated mesh topology and silhouette rather than white blow-out.
clay=bpy.data.materials.new("run137c neutral grey topology QA")
clay.use_nodes=True
clay.node_tree.nodes.get("Principled BSDF").inputs["Base Color"].default_value=(.34,.34,.33,1)
clay.node_tree.nodes.get("Principled BSDF").inputs["Roughness"].default_value=.92
for ob in meshes:
    ob.data.materials.clear()
    ob.data.materials.append(clay)
if not scene.world:scene.world=bpy.data.worlds.new("Run137C grey research studio")
scene.world.color=(.12,.12,.12)
scene.render.engine="CYCLES"
scene.cycles.samples=12
scene.view_layers[0].cycles.use_denoising=False
scene.render.resolution_x=550
scene.render.resolution_y=550
scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
def area(vec,power):
    light=bpy.data.lights.new("research area",type="AREA")
    light.energy=power
    light.size=extent*4
    obj=bpy.data.objects.new("research area",light)
    scene.collection.objects.link(obj)
    obj.location=center+Vector(vec)*extent
    obj.rotation_euler=(center-obj.location).to_track_quat("-Z","Y").to_euler()
area((-3,-3,3),260)
area((3,1,2),120)
cam=bpy.data.objects.new("QA-camera",bpy.data.cameras.new("QA-camera"))
scene.collection.objects.link(cam)
scene.camera=cam
cam.data.type="ORTHO"
cam.data.ortho_scale=extent*1.7
files=[]
for name,deg in (("front",0),("quarter",45),("side",90),("back",180)):
    a=math.radians(deg)
    cam.location=center+Vector((4*math.sin(a),-4*math.cos(a),1.3))*extent
    cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
    p=O/("run137c_native_"+name+"_UNAPPROVED.png")
    scene.render.filepath=str(p)
    bpy.ops.render.render(write_still=True)
    assert p.is_file() and p.stat().st_size>1000, "Actual render not written"
    files.append(str(p))
(O/"run137c_native_qa.json").write_text(json.dumps({
 "source":"Run137 actual openable GLB quarantined in Actions artifact 14316899449",
 "source_sha256":PIN,"source_bytes":S.stat().st_size,
 "blender_version":bpy.app.version_string,
 "mesh_count":len(meshes),
 "polygon_faces":sum(len(x.data.polygons) for x in meshes),
 "bounds_blender_xyz":list(high-low),"images":files,
 "denoising_disabled":True,
 "renderer":"real native Blender Cycles",
 "material_count":len(bpy.data.materials),
 "material_is_qa_only_clay":True,
 "art_approved":False,"license_cleared":False,"physical_mobile_gpu_tested":False,
 "result":"ART_UNREVIEWED_NO_RELEASE"
 },indent=2)+"\n")
print("RUN137C_NATIVE_4_VIEW_REAL_DONE",json.dumps(files))
