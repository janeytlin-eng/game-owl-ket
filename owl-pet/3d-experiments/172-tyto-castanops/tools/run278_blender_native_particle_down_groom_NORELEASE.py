"""Run278: real Blender hair on a genuine neural 3D donor. Research only; never a deliverable.
This tests whether Blender-native soft down rendering survives glTF export.
Requires Blender, a verified GLB path, and no paid service. No species pipeline writes.
"""
import bpy, math, os, sys, json, hashlib, traceback
from pathlib import Path
from mathutils import Vector

out=Path(os.environ.get("OWL172_OUT","/tmp/owl172-run278"))
src=Path(os.environ["OWL172_GLB_INPUT"])
out.mkdir(parents=True, exist_ok=True)
report={"experiment":"run278_real_blender_particle_hair",
        "source":str(src),"source_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),
        "status":"NO_RELEASE", "art_grade":"UNREVIEWED",
        "source_rights":"HUNYUAN_NONCOMMERCIAL_RESEARCH_ONLY",
        "gltf_hair_export":"UNVERIFIED",
        "phone_gpu":"UNTESTED"}
try:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=str(src))
    meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    assert meshes, "No native meshes in source"
    primary=max(meshes,key=lambda o:len(o.data.polygons))
    for o in meshes: o.select_set(False)
    primary.select_set(True)
    bpy.context.view_layer.objects.active=primary
    bbox=[primary.matrix_world @ Vector(corner) for corner in primary.bound_box]
    lo=Vector([min(v[i] for v in bbox) for i in range(3)])
    hi=Vector([max(v[i] for v in bbox) for i in range(3)])
    center=(lo+hi)*0.5
    diagonal=(hi-lo).length
    assert diagonal>0, "No genuine spatial extent"
    report["native_glb"]={"mesh_objects":len(meshes),
      "largest_mesh_faces":len(primary.data.polygons),"largest_mesh_vertices":len(primary.data.vertices),
      "bounds_min":list(lo),"bounds_max":list(hi), "diagonal":diagonal}
    # Blender true hair curve/child grooming, not old mesh spikes or UV texture fake fur.
    bpy.ops.object.particle_system_add()
    ps=primary.particle_systems[-1]
    settings=ps.settings
    settings.type="HAIR"
    settings.count=12000
    settings.hair_length=diagonal*0.042
    settings.hair_step=5
    settings.use_emit_random=True
    settings.distribution="JIT"
    settings.child_type="INTERPOLATED"
    settings.rendered_child_count=7
    settings.clump_factor=0.10
    settings.roughness_1=diagonal*0.008
    settings.roughness_2=diagonal*0.004
    settings.roughness_endpoint=diagonal*0.009
    # Shader for down, distinct from a procedural mesh / simple ribbon substitute.
    mat=bpy.data.materials.new("Warm_cream_semimat_DOWN_HAIR_research")
    mat.diffuse_color=(0.93,0.878,0.774,1)
    mat.use_nodes=True
    bsdf=mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
      bsdf.inputs["Base Color"].default_value=(0.94,0.892,0.80,1)
      bsdf.inputs["Roughness"].default_value=0.87
    primary.data.materials.append(mat)
    settings.material=len(primary.data.materials)
    report["groom"]={"type":"Blender real particle hair",
                     "parents":settings.count,
                     "render_children":settings.rendered_child_count,
                     "length_world":settings.hair_length,
                     "child_type":settings.child_type}
    # True Cycles CPU renders. Four cameras are spatially different; front not
    # asserted without a documented original axis.
    scene=bpy.context.scene
    scene.render.engine="CYCLES"
    scene.cycles.device="CPU"
    scene.cycles.samples=6
    # Ubuntu Blender package ships Cycles without OpenImageDenoiser; disable explicitly.
    scene.cycles.use_denoising=False
    for layer in scene.view_layers:
      if hasattr(layer,'cycles'):
        layer.cycles.use_denoising=False
    scene.render.resolution_x=440
    scene.render.resolution_y=440
    scene.render.resolution_percentage=100
    scene.render.image_settings.file_format="PNG"
    scene.render.film_transparent=True
    scene.world.color=(0.24,0.24,0.24)
    world=bpy.data.worlds.new("Studio_world")
    world.use_nodes=True
    world.node_tree.nodes["Background"].inputs["Color"].default_value=(0.55,0.58,0.65,1)
    world.node_tree.nodes["Background"].inputs["Strength"].default_value=0.7
    scene.world=world
    def area(name, xyz, energy, size):
      d=bpy.data.lights.new(name,"AREA")
      obj=bpy.data.objects.new(name,d)
      scene.collection.objects.link(obj)
      obj.location=center+Vector(xyz)*diagonal
      direction=center-obj.location
      obj.rotation_euler=direction.to_track_quat("-Z","Y").to_euler()
      d.energy=energy; d.shape="DISK"; d.size=diagonal*size
    area("warm_studio_key",(-1.4,-1.7,1.9),640,2.5)
    area("cool_back_rim",(1.2,1.0,1.2),420,1.9)
    cam_data=bpy.data.cameras.new("research_camera")
    cam=bpy.data.objects.new("research_camera",cam_data)
    scene.collection.objects.link(cam)
    scene.camera=cam
    cam_data.type="ORTHO"; cam_data.ortho_scale=diagonal*1.08
    angles=[0,45,90,180]
    report["rendered"]=[]
    for degrees in angles:
      a=math.radians(degrees)
      cam.location=center+Vector((math.sin(a)*2.15,-math.cos(a)*2.15,0.48))*diagonal
      cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
      p=out/("blender_cycles_hair_azimuth_%03d.png"%degrees)
      scene.render.filepath=str(p)
      bpy.ops.render.render(write_still=True)
      report["rendered"].append({"azimuth_degrees":degrees,"name":p.name,
                                  "bytes":p.stat().st_size,
                                  "sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
    bpy.ops.wm.save_as_mainfile(filepath=str(out/"run278_real_blender_hair_groom_research_NORELEASE.blend"))
    # Scientific negative/positive glTF transmission gate: mesh-only export.
    # Particle hair is Blender renderer data and may not survive glTF.
    bpy.ops.object.select_all(action="DESELECT")
    for o in meshes: o.select_set(True)
    bpy.context.view_layer.objects.active=primary
    export=out/"run278_glb_export_from_real_hair_scene_UNVALIDATED_NORELEASE.glb"
    bpy.ops.export_scene.gltf(filepath=str(export),export_format="GLB",use_selection=True)
    report["export_glb_bytes"]=export.stat().st_size
    report["export_glb_sha256"]=hashlib.sha256(export.read_bytes()).hexdigest()
    report["runtime_observation"]="Blender true hair preview is not by itself evidence of WebGL2 export; inspect exported glTF primitives and source visual mismatch."
    report["status"]="RENDER_AND_EXPORT_COMPLETED_REVIEW_REQUIRED_NO_RELEASE"
except Exception as e:
    report["status"]="EXECUTION_FAILED_NO_RELEASE"
    report["error"]=str(e)
    report["traceback"]=traceback.format_exc()
    raise
finally:
    (out/"machine-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2,default=str)+"\n")
    print("RUN278_MACHINE_REPORT",json.dumps(report,ensure_ascii=False,default=str),flush=True)
