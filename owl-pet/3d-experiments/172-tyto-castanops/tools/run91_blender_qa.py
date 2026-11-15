"""Run91 real Blender Cycles 3D render of all 3 genuine GLB variants.
No approval inferred from successful GLB import or rasterization.
"""
import bpy, os, sys, json, pathlib, math, hashlib
from mathutils import Vector
out=pathlib.Path(sys.argv[sys.argv.index("--")+1])
os.makedirs(out,exist_ok=True)
metrics=json.loads((out/"metrics.json").read_text())
assert len(metrics["variants"])==3
scene=bpy.context.scene
scene.render.engine="CYCLES"
scene.cycles.samples=20
scene.cycles.use_denoising=False
bpy.context.view_layer.cycles.use_denoising=False
scene.render.resolution_x=480
scene.render.resolution_y=480
scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
scene.view_settings.view_transform="Standard"
scene.view_settings.exposure=-.42
world=bpy.data.worlds.new("neutral moonstone photographic QA")
scene.world=world;world.use_nodes=True
world.node_tree.nodes["Background"].inputs["Color"].default_value=(.50,.54,.56,1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value=.52
rendered=[]
for variant in metrics["variants"]:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    src=str(out/variant["glb"])
    assert hashlib.sha256(open(src,"rb").read()).hexdigest()==variant["sha256"]
    bpy.ops.import_scene.gltf(filepath=src)
    objects=[o for o in bpy.data.objects if o.type=="MESH"]
    assert len(objects)==variant["mesh_count"],(len(objects),variant["mesh_count"])
    bounds=[o.matrix_world @ Vector(v) for o in objects for v in o.bound_box]
    mn=Vector([min(v[k] for v in bounds) for k in range(3)])
    mx=Vector([max(v[k] for v in bounds) for k in range(3)])
    mid=(mn+mx)/2; extent=max(mx-mn)
    for name,diff,power,size in [
        ("key",Vector((-1.15,-1.5,1.75)),120,2.2),
        ("fill",Vector((1.5,-.60,.7)),70,2.0),
        ("rim",Vector((.40,1.65,1.65)),115,1.65)]:
        bpy.ops.object.light_add(type="AREA",location=mid+diff*extent)
        light=bpy.context.object;light.name=name
        light.data.energy=power
        light.data.shape="DISK";light.data.size=size*extent
        light.rotation_euler=(mid-light.location).to_track_quat("-Z","Y").to_euler()
    bpy.ops.object.camera_add()
    cam=bpy.context.object;scene.camera=cam
    cam.data.type="ORTHO";cam.data.ortho_scale=extent*1.65
    # Blender glTF import: glTF +Z front becomes Blender -Y front.
    for view,d in [
        ("front",(0,-2.5,.16)),("threequarter",(1.65,-1.9,.20)),
        ("strict_side",(2.5,0,.16)),("back",(0,2.5,.16))]:
        cam.location=mid+Vector(d)*extent
        cam.rotation_euler=(mid-cam.location).to_track_quat("-Z","Y").to_euler()
        img=f"run91_{variant['label']}_{view}.png"
        scene.render.filepath=str(out/img)
        bpy.ops.render.render(write_still=True)
        assert os.path.getsize(out/img)>15000
        rendered.append(img)
    print("REAL_CYCLES_MULTI_VIEW_COMPLETED",variant["label"],flush=True)
metrics["cycles_render_count"]=len(rendered)
metrics["cycles_renders"]=rendered
metrics["blender_version"]=bpy.app.version_string
metrics["gpu_render"]="CPU_Cycles_not_phone_GPU"
metrics["visual_gate"]="PENDING_HUMAN_VIEW_INSPECTION_ART_NOT_APPROVED"
(out/"metrics.json").write_text(json.dumps(metrics,indent=2))
assert len(rendered)==12
