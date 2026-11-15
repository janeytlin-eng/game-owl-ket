#!/usr/bin/env python3
"""Run98: investigate a free CC0-claimed bird rig as *donor research only*.
The asset is NOT Tyto castanops, and neither original nor warm material ablation
may be published as a qualified owl pet. Real Blender geometry and actual 4-view.
"""
import bpy, sys, json, math, hashlib
from pathlib import Path
from mathutils import Vector

args=sys.argv[sys.argv.index("--")+1:]
source=Path(args[0]).resolve()
out=Path(args[1]).resolve()
out.mkdir(parents=True,exist_ok=True)
assert source.exists() and source.stat().st_size>8000
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(source))
s=bpy.context.scene

def geometry_report():
    meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    arms=[o for o in bpy.context.scene.objects if o.type=="ARMATURE"]
    for o in meshes:o.data.calc_loop_triangles()
    triangles=sum(len(o.data.loop_triangles) for o in meshes)
    c=[o.matrix_world@Vector(v) for o in meshes for v in o.bound_box]
    lo=[min(p[i] for p in c) for i in range(3)]
    hi=[max(p[i] for p in c) for i in range(3)]
    acts=[{"name":a.name,"frames":list(map(float,a.frame_range))} for a in bpy.data.actions]
    return {
      "mesh_count":len(meshes),"triangles":triangles,
      "armature_count":len(arms),"bone_count":sum(len(a.data.bones) for a in arms),
      "action_count":len(acts),"actions":acts,
      "bounds_min":lo,"bounds_max":hi,
      "material_count":len(bpy.data.materials),
      "curve_objects":sum(o.type=="CURVE" for o in bpy.context.scene.objects),
      "has_natural_down_groom":False, # Manual visual QA required; no assertion from mesh counts
      "not_target_species":True
    }

original=geometry_report()
assert original["triangles"]>100 and original["mesh_count"]>0,original
print("RUN98_IMPORTED_REAL_GLB",json.dumps(original),flush=True)

def setup_render():
    sc=bpy.context.scene
    sc.render.engine="CYCLES"
    sc.cycles.samples=18
    sc.cycles.use_denoising=False
    bpy.context.view_layer.cycles.use_denoising=False
    sc.render.resolution_x=430;sc.render.resolution_y=430
    sc.render.resolution_percentage=100
    sc.render.image_settings.file_format="PNG"
    sc.render.film_transparent=False
    sc.view_settings.view_transform="Standard"
    sc.view_settings.look="Medium High Contrast"
    sc.view_settings.exposure=-.5
    world=bpy.data.worlds.new("Run98_gray_studio")
    world.use_nodes=True
    world.node_tree.nodes["Background"].inputs["Color"].default_value=(.56,.59,.62,1)
    world.node_tree.nodes["Background"].inputs["Strength"].default_value=.75
    sc.world=world
    cen=Vector([(a+b)/2 for a,b in zip(original["bounds_min"],original["bounds_max"])])
    dims=Vector([b-a for a,b in zip(original["bounds_min"],original["bounds_max"])])
    extent=max(dims.length, .2)
    for name,vec,power in [("key",(-3,-4,5),230),("fill",(4,-1,3),125),("rim",(1,3,5),205)]:
        bpy.ops.object.light_add(type="AREA",location=cen+Vector(vec)*(extent/3))
        lamp=bpy.context.object;lamp.name=name;lamp.data.energy=power;lamp.data.size=extent
        lamp.rotation_euler=(cen-lamp.location).to_track_quat("-Z","Y").to_euler()
    bpy.ops.object.camera_add()
    cam=bpy.context.object;sc.camera=cam;cam.data.type="ORTHO"
    cam.data.ortho_scale=max(1.35*max(dims.x,dims.y,dims.z),.8)
    return cen,extent,cam

cen,extent,cam=setup_render()
images=[]
def render(stage):
    for name,angle in [("azimuth_0",0),("azimuth_90",90),("azimuth_180",180),("azimuth_270",270)]:
        theta=math.radians(angle)
        cam.location=cen+Vector((math.sin(theta)*extent*1.6,-math.cos(theta)*extent*1.6,extent*.28))
        cam.rotation_euler=(cen-cam.location).to_track_quat("-Z","Y").to_euler()
        dst=out/(stage+"_"+name+".png")
        s.render.filepath=str(dst)
        bpy.ops.render.render(write_still=True)
        assert dst.exists() and dst.stat().st_size>4000,dst
        images.append({"stage":stage,"view":name,"bytes":dst.stat().st_size,
                       "sha256":hashlib.sha256(dst.read_bytes()).hexdigest()})
        print("RUN98_CYCLES_RENDER",stage,name,dst.stat().st_size,flush=True)
render("original")

# A/B color-only experiment, not a juvenile transformation. Deliberately leaves
# topology, wing anatomy, animation bindings and age unchanged.
colored=0
for ob in [o for o in s.objects if o.type=="MESH"]:
    for slot in ob.material_slots:
        if not slot.material:continue
        mat=slot.material.copy()
        slot.material=mat
        mat.diffuse_color=(.91,.86,.75,1)
        mat.use_nodes=True
        node=next((n for n in mat.node_tree.nodes if n.type=="BSDF_PRINCIPLED"),None)
        if node:
            inp=node.inputs.get("Base Color")
            if inp:
                for link in list(inp.links):mat.node_tree.links.remove(link)
                inp.default_value=(.91,.86,.75,1)
            metallic=node.inputs.get("Metallic")
            if metallic:metallic.default_value=0
            roughness=node.inputs.get("Roughness")
            if roughness:roughness.default_value=.92
            colored+=1
assert colored>0,colored
render("warm_material_ablation")

# Export actual transformed glTF from Blender. Lighting and camera not exported.
bpy.ops.export_scene.gltf(filepath=str(out/"warm_material_ABLATION_ART_REJECTED.glb"),
                          export_format="GLB",use_selection=False,
                          export_cameras=False,export_lights=False)
export=out/"warm_material_ABLATION_ART_REJECTED.glb"
assert export.stat().st_size>8000
digest=hashlib.sha256(export.read_bytes()).hexdigest()
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(export))
roundtrip=geometry_report()
assert roundtrip["triangles"]==original["triangles"],(original,roundtrip)
metrics={
 "status":"PENDING_MANUAL_ART_REVIEW_NOT_APPROVED",
 "purpose":"Evaluate real CC0-claimed low-poly barn owl as RIG donor only, not as final character",
 "source_url":"https://gobkit.com/freebies/animal013/BarnOwl.glb",
 "license_claim":"Provider API lists CC0 1.0; author chain of title not independently verified",
 "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
 "source_bytes":source.stat().st_size,
 "original_geometry":original,"color_changed_material_slots":colored,
 "reimport_geometry":roundtrip,
 "ablation_glb_sha256":digest,"ablation_glb_bytes":export.stat().st_size,
 "images":images,
 "source_is_not_tyto_castanops":True,
 "real_phone_gpu":False,"mobile_fps":None,
 "no_payment":True,"production_unchanged":True,
 "release_allowed":False
}
(out/"run98_metrics.json").write_text(json.dumps(metrics,indent=2))
print("RUN98_REAL_GLTF_ROUNDTRIP",json.dumps({"triangles":roundtrip["triangles"],"actions":roundtrip["action_count"],"bytes":export.stat().st_size}),flush=True)
