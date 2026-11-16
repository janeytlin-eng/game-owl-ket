#!/usr/bin/env python3
"""Run100B: true high-poly -> decimated neural surface tangent normal bake.

Non-release #172 rightmost cream nestling test. Input is REAL Run99 Hunyuan
neural 3D and REAL Run100 smoothed 80k 3D, not SVG/2D/primitive assembly.
Blender Cycles Selected-to-Active baking; tests if displacement-like plumage
etching can be transferred without reintroducing harsh geometry.
"""
import pathlib, sys, json, hashlib, struct, traceback
import bpy
from mathutils import Vector
from math import radians,sin,cos
args=sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else []
if len(args)!=3: raise SystemExit("usage: blender -b --python script.py -- HI.glb LO.glb OUTDIR")
hi_path,lo_path,out=[pathlib.Path(a) for a in args]
out.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def tri(ob):return sum(len(p.vertices)-2 for p in ob.data.polygons)
def select_active(o,source=None):
    bpy.ops.object.select_all(action="DESELECT")
    if source:source.select_set(True)
    o.select_set(True)
    bpy.context.view_layer.objects.active=o
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(hi_path))
high=[o for o in bpy.context.scene.objects if o.type=="MESH"]
if len(high)!=1: raise RuntimeError("Run99 expected one neural high mesh")
high=high[0]
before=set(o.name for o in bpy.data.objects)
bpy.ops.import_scene.gltf(filepath=str(lo_path))
low=[o for o in bpy.context.scene.objects if o.type=="MESH" and o.name not in before]
if len(low)!=1:raise RuntimeError("Run100 smooth GLB expected one low mesh")
low=low[0]
report={"experiment":"run100B_true_normal_map_bake",
        "high_sha256":sha(hi_path),"low_sha256":sha(lo_path),
        "high_faces":tri(high),"low_faces":tri(low),
        "license_review_pending":True,"real_mobile_device_unverified":True,
        "source":"neural generated in Run99, polished lower geometry from Run100",
        "art_gate":"UNAPPROVED","outcome":"IN_PROGRESS"}
scene=bpy.context.scene
scene.render.engine="CYCLES"
scene.cycles.samples=18
scene.cycles.use_denoising=False
scene.render.resolution_x=448
scene.render.resolution_y=448
scene.render.resolution_percentage=100
scene.world.color=(.43,.43,.43)
scene.view_settings.view_transform="Standard"
scene.view_settings.look="Medium High Contrast"

select_active(low)
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.uv.smart_project(island_margin=0.025)
bpy.ops.object.mode_set(mode="OBJECT")
report["low_uv_layers"]=len(low.data.uv_layers)
if report["low_uv_layers"]<1:raise RuntimeError("No actual UV coordinates created")

if len(low.data.materials)<1:raise RuntimeError("No PBR material on source low mesh")
material=low.data.materials[0].copy()
material.name="run100b_cream_pbr_with_real_highpoly_baked_tangent_normals"
low.data.materials.clear()
low.data.materials.append(material)
nodes=material.node_tree.nodes
links=material.node_tree.links
for n in nodes:n.select=False
texture=nodes.new("ShaderNodeTexImage")
texture.name="Actual Cycles normal bake 1024"
texture.label="Run99 high-mesh normals"
image=bpy.data.images.new("run100b_high_detail_normal_bake",width=1024,height=1024,alpha=False,float_buffer=False)
image.colorspace_settings.name="Non-Color"
texture.image=image
nodes.active=texture
texture.select=True
normal_node=nodes.new("ShaderNodeNormalMap")
normal_node.space="TANGENT"
normal_node.uv_map=low.data.uv_layers.active.name
bsdf=nodes.get("Principled BSDF")
if not bsdf: raise RuntimeError("No PBR Principled BSDF shader")
# Keep bake image target active; link baked texture as a normal map only after bake.
scene.render.bake.use_selected_to_active=True
scene.render.bake.max_ray_distance=0.065
scene.render.bake.cage_extrusion=0.015
scene.render.bake.margin=8
select_active(low,high)
print("RUN100B_BAKING_STARTED",report["high_faces"],report["low_faces"],flush=True)
try:
    bpy.ops.object.bake(type="NORMAL")
except Exception as e:
    report["outcome"]="BAKE_FAILED_ART_UNAPPROVED"
    report["error"]=repr(e)
    (out/"run100b_bake_error.txt").write_text(traceback.format_exc())
    (out/"run100b_metrics.json").write_text(json.dumps(report,indent=2))
    raise
image.filepath_raw=str(out/"run100b_1024_native_normal_bake_UNAPPROVED.png")
image.file_format="PNG"
image.save()
texsize=pathlib.Path(image.filepath_raw).stat().st_size
report["normal_map_bytes"]=texsize
report["normal_map_sha256"]=sha(image.filepath_raw)
print("RUN100B_CYCLES_BAKED_TEXTURE",texsize,flush=True)
links.new(texture.outputs["Color"],normal_node.inputs["Color"])
links.new(normal_node.outputs["Normal"],bsdf.inputs["Normal"])
for poly in low.data.polygons:poly.use_smooth=True
high.hide_render=True
select_active(low)
model=out/"run100b_80k_uv_real_baked_normals_ART_UNAPPROVED.glb"
bpy.ops.export_scene.gltf(filepath=str(model),export_format="GLB",
    use_selection=True,export_materials="EXPORT",export_normals=True)
binary=model.read_bytes()
if binary[:4]!=b"glTF" or struct.unpack_from("<I",binary,8)[0]!=len(binary):
    raise RuntimeError("Invalid binary glTF after normal baking export")
report["output_bytes"]=len(binary)
report["output_sha256"]=sha(model)
low.hide_render=True
before=set(o.name for o in bpy.data.objects)
bpy.ops.import_scene.gltf(filepath=str(model))
imported=[o for o in bpy.data.objects if o.name not in before and o.type=="MESH"]
if not imported:raise RuntimeError("Exported normal map GLB did not reimport")
report["roundtrip_triangles"]=sum(tri(o) for o in imported)
report["roundtrip_material_count"]=sum(len(o.data.materials) for o in imported)
report["roundtrip_image_count"]=len(bpy.data.images)
for obj in imported:obj.hide_render=False
if report["roundtrip_triangles"]<70000:raise RuntimeError("Exported geometry incomplete")
bounds=[o.matrix_world@Vector(c) for o in imported for c in o.bound_box]
lo=Vector(tuple(min(v[i] for v in bounds) for i in range(3)))
hi=Vector(tuple(max(v[i] for v in bounds) for i in range(3)))
center=(lo+hi)*0.5
size=max(hi-lo)
for o in list(bpy.data.objects):
    if o.type=="LIGHT":bpy.data.objects.remove(o,do_unlink=True)
def area(name,xyz,power,width):
    d=bpy.data.lights.new(name,type="AREA");d.energy=power;d.shape="DISK";d.size=width*size
    o=bpy.data.objects.new(name,d);scene.collection.objects.link(o)
    o.location=center+Vector(xyz)*size
    o.rotation_euler=(center-o.location).to_track_quat("-Z","Y").to_euler()
area("softbox",(-2.5,-3,3.1),460,4.2)
area("fill",(2,-1.8,1.2),150,3.5)
area("rim",(1.8,2,2.8),250,3)
camdata=bpy.data.cameras.new("run100b_cam")
cam=bpy.data.objects.new("run100b_cam",camdata);scene.collection.objects.link(cam)
scene.camera=cam;cam.data.type="ORTHO";cam.data.ortho_scale=size*1.6
for name,deg in (("front",0),("quarter",45),("side",90),("back",180)):
    rad=radians(deg)
    cam.location=center+Vector((4*sin(rad),-4*cos(rad),1.3))*size
    cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
    scene.render.filepath=str(out/("run100b_"+name+"_native_cycles_UNAPPROVED.png"))
    bpy.ops.render.render(write_still=True)
    print("RUN100B_RENDERED",name,flush=True)
report["outcome"]="REAL_BAKE_GLTF_REIMPORT_4_VIEWS_COMPLETE_ART_UNAPPROVED"
(out/"run100b_metrics.json").write_text(json.dumps(report,indent=2))
(out/"ART_GATE_NOT_PASSED.md").write_text(
    "# Run100B art gate NOT passed\n\n"
    "Actual high-to-low Cycles tangent normal-map bake and real PBR GLB.\n"
    "Unverified: cream down layering, heart-disc sculpt, side/back independent anatomy, "
    "broad tree-hollow footing, animation and physical phone GPU testing. "
    "No production deploy. Public-research-only Tencent Hunyuan license review required.\n")
print("RUN100B_SUCCESSFUL_TECHNICAL_BAKE_NO_ART_APPROVAL",json.dumps(report),flush=True)
