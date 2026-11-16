#!/usr/bin/env python3
"""Run100: independently quarantined high-poly neural-mesh surface topology repair trial.

Starts with *actual* Run99 Hunyuan GLB, not an SVG, a rendered billboard, or
new geometric primitives. Runs in free Blender 4.x on Actions; no released pet.
Variants test whether removing severe shell microtopology before polygon
decimation improves the juvenile silhouette/heart face while retaining 3D volume.
The source's public research-only Hunyuan Community License is NOT CC0.
"""
import sys, json, pathlib, hashlib, struct, time, traceback
import bpy
from mathutils import Vector
from math import radians, sin, cos

args=sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else []
if len(args)!=2:
    raise SystemExit("blender -b --python script.py -- SOURCE.glb EVIDENCE_DIRECTORY")
source,out=pathlib.Path(args[0]),pathlib.Path(args[1])
out.mkdir(parents=True,exist_ok=True)
def digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
def tria(obj):
    return sum(len(p.vertices)-2 for p in obj.data.polygons)
def choose(obj):
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active=obj
    obj.select_set(True)
def apply_mod(obj,name):
    choose(obj)
    bpy.ops.object.modifier_apply(modifier=name)
def metrics_mesh(obj):
    pts=[obj.matrix_world @ Vector(c) for c in obj.bound_box]
    return {
        "triangles":tria(obj),"vertices":len(obj.data.vertices),
        "dimensions":[round(max(p[i] for p in pts)-min(p[i] for p in pts),6) for i in range(3)]
    }
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(source))
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
if len(meshes)!=1: raise RuntimeError("Expected one real neural source mesh; found "+str(len(meshes)))
original=meshes[0]
scene=bpy.context.scene
bounds=[original.matrix_world @ Vector(c) for c in original.bound_box]
lo=Vector(tuple(min(p[i] for p in bounds) for i in range(3)))
hi=Vector(tuple(max(p[i] for p in bounds) for i in range(3)))
center=(lo+hi)*0.5
size=max(hi-lo)
if size<=0.01: raise RuntimeError("Degenerate input")
scene.render.engine="CYCLES"
scene.cycles.samples=18
scene.cycles.use_denoising=False
scene.render.resolution_x=448
scene.render.resolution_y=448
scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
scene.render.film_transparent=False
scene.world.color=(0.45,0.45,0.45)
scene.view_settings.view_transform="Standard"
scene.view_settings.look="Medium High Contrast"
scene.view_settings.exposure=0
for o in list(bpy.data.objects):
    if o.type=="LIGHT": bpy.data.objects.remove(o,do_unlink=True)
def area(name,xyz,power,width):
    d=bpy.data.lights.new(name,"AREA")
    d.energy=power;d.shape="DISK";d.size=width*size
    o=bpy.data.objects.new(name,d);scene.collection.objects.link(o)
    o.location=center+Vector(xyz)*size
    o.rotation_euler=(center-o.location).to_track_quat("-Z","Y").to_euler()
area("cream_softbox",(-2.5,-3,3.1),460,4.2)
area("cream_fill",(2,-1.8,1.2),150,3.5)
area("rear_rim",(1.8,2,2.8),250,3.0)
camera_data=bpy.data.cameras.new("Run100_Camera")
camera=bpy.data.objects.new("Run100_Camera",camera_data)
scene.collection.objects.link(camera);scene.camera=camera
camera.data.type="ORTHO";camera.data.ortho_scale=1.6*size
def render_views(prefix):
    for name,degree in (("front",0),("quarter",45),("side",90),("back",180)):
        a=radians(degree)
        camera.location=center+Vector((4*sin(a),-4*cos(a),1.3))*size
        camera.rotation_euler=(center-camera.location).to_track_quat("-Z","Y").to_euler()
        path=out/(prefix+"_"+name+"_cycles.png")
        scene.render.filepath=str(path)
        bpy.ops.render.render(write_still=True)
        print("RUN100_NATIVE_RENDER",path.name,path.stat().st_size,flush=True)
def cream_material():
    m=bpy.data.materials.new("run100_cream_nonmetal_roughness_093")
    m.use_nodes=True
    bsdf=m.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value=(0.9,0.815,0.702,1)
    bsdf.inputs["Metallic"].default_value=0
    bsdf.inputs["Roughness"].default_value=0.93
    bsdf.inputs["Specular IOR Level"].default_value=0.16
    return m
cream=cream_material()
report={
    "experiment":"Run100/neutral neural-source topology ablation",
    "source_sha256":digest(source),
    "source_geometry":metrics_mesh(original),
    "source_type":"real Hunyuan3D-2 ZeroGPU single-view generated GLB",
    "not_a_released_asset":True,
    "target_reference":"#172 Tyto castanops v3 rightmost cream owl mesoptile",
    "art_gate":"ART_UNAPPROVED",
    "source_license":"Tencent Hunyuan3D-2 Community License (review required; territory restrictions)",
    "phone_webgl_verified":False,
    "surface_repair_variants":[]
}
original.hide_render=False
print("RUN100_SOURCE",json.dumps(report["source_geometry"]),flush=True)
render_views("source_raw")
original.hide_render=True

for kind,target in (("smooth_80k",80000),("voxel_55k",55000)):
    entry={"variant":kind,"goal":target}
    obj=None
    try:
        obj=original.copy()
        obj.data=original.data.copy()
        scene.collection.objects.link(obj)
        obj.name="run100_"+kind+"_REAL_NEURAL_SOURCE"
        choose(obj)
        obj.hide_render=False
        if kind=="smooth_80k":
            sm=obj.modifiers.new("smooth_6pass",type="SMOOTH")
            sm.factor=0.43
            sm.iterations=6
            apply_mod(obj,sm.name)
            entry["operation"]="six gentle mesh smoothing passes before true decimation"
        elif kind=="voxel_55k":
            voxel_size=size*0.014
            obj.data.remesh_voxel_size=voxel_size
            bpy.ops.object.voxel_remesh()
            entry["voxel_size_units"]=voxel_size
            entry["operation"]="physical voxel topology consolidation + 3 smooth passes before decimation"
            sm=obj.modifiers.new("soft_voxel_relax_3pass",type="SMOOTH")
            sm.factor=0.5
            sm.iterations=3
            apply_mod(obj,sm.name)
        entry["after_topology_repair"]=metrics_mesh(obj)
        dec=obj.modifiers.new("genuine_polygon_budget",type="DECIMATE")
        dec.decimate_type="COLLAPSE"
        dec.ratio=min(1,target/max(1,tria(obj)))
        dec.use_collapse_triangulate=True
        apply_mod(obj,dec.name)
        obj.data.materials.clear()
        obj.data.materials.append(cream)
        for p in obj.data.polygons:
            p.material_index=0
            p.use_smooth=True
        entry["before_export"]=metrics_mesh(obj)
        choose(obj)
        target_glb=out/("run100_"+kind+"_ART_UNAPPROVED.glb")
        bpy.ops.export_scene.gltf(filepath=str(target_glb),export_format="GLB",
            use_selection=True, export_materials="EXPORT", export_normals=True)
        binary=target_glb.read_bytes()
        if binary[:4]!=b"glTF" or struct.unpack_from("<I",binary,8)[0]!=len(binary):
            raise RuntimeError("Invalid GLB file signature/length")
        entry["file_bytes"]=len(binary)
        entry["sha256"]=digest(target_glb)
        bpy.data.objects.remove(obj,do_unlink=True);obj=None
        before=set(o.name for o in bpy.data.objects)
        bpy.ops.import_scene.gltf(filepath=str(target_glb))
        newcomers=[o for o in bpy.context.scene.objects if o.name not in before and o.type=="MESH"]
        if not newcomers: raise RuntimeError("No meshes in actual Blender GLB roundtrip")
        entry["roundtrip_tris"]=sum(tria(o) for o in newcomers)
        entry["roundtrip_meshes"]=len(newcomers)
        entry["roundtrip_materials"]=[m.name for o in newcomers for m in o.data.materials if m]
        if entry["roundtrip_tris"] < target*0.75 or not entry["roundtrip_materials"]:
            raise RuntimeError("Low 3D geometry/materials after GLB reimport")
        for o in newcomers:o.hide_render=False
        render_views(kind+"_roundtrip")
        for o in newcomers:bpy.data.objects.remove(o,do_unlink=True)
        entry["status"]="REAL_GLB_AND_4_VIEWS_REVIEW_NEEDED"
    except Exception as exc:
        entry["status"]="FAILED_NOT_PUBLISHED"
        entry["error"]=type(exc).__name__+": "+str(exc)[:900]
        (out/(kind+"_traceback.txt")).write_text(traceback.format_exc())
        print("RUN100_VARIANT_FAILURE",kind,entry["error"],flush=True)
        if obj is not None and obj.name in bpy.data.objects:
            bpy.data.objects.remove(obj,do_unlink=True)
        # Return to reference-only state even when a candidate fails.
        original.hide_render=True
    finally:
        report["surface_repair_variants"].append(entry)
        (out/"run100_mesh_metrics.json").write_text(json.dumps(report,indent=2))
        print("RUN100_VARIANT_REPORT",json.dumps(entry),flush=True)

(out/"ART_GATE_NOT_PASSED.md").write_text(
    "# RUN100 RESEARCH ONLY — ART_UNAPPROVED\n\n"
    "Real single-image generated neural source; smoothed or voxel-remeshed actual 3D topology, "
    "never SVG, fake 2D or primitive geometry. Rig, real mobile GPU, animation, artist-approved "
    "feather grooming, source rights, independent side/back anatomy, broad tree-hollow support and "
    "full adult-to-juvenile anatomical validation are NOT passed. The baseline and both variants "
    "require manual multi-view inspection. Zero spend. NEVER publish or merge into species production.\n")
print("RUN100_COMPLETED_ART_UNAPPROVED",json.dumps(report),flush=True)
