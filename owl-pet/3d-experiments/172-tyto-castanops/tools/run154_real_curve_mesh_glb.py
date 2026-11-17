#!/usr/bin/env python3
"""Run154 isolated Blender-native 3D down export test; NEVER a releasable owl pet.
Inputs: previously produced real .blend source from Run153, exact source files checked
by caller. Tests whether actual curved groom geometry can survive glTF/GLB, rather
than presenting a flat image or claiming mature mesh is realistic.
"""
import bpy, json, os, math, hashlib, time, traceback
from mathutils import Vector
OUT = os.environ.get("OWL154_OUT", "/tmp/owl172_run154")
SOURCE = os.environ["OWL154_BLEND"]
os.makedirs(OUT, exist_ok=True)

def digest(path):
    with open(path,"rb") as f:
        h=hashlib.sha256()
        for chunk in iter(lambda:f.read(1<<20),b""):h.update(chunk)
    return {"bytes":os.path.getsize(path),"sha256":h.hexdigest()}

def load_source():
    bpy.ops.wm.open_mainfile(filepath=SOURCE)
    # This is a non-release research source: original front eyes and side remain rejected.
    scene=bpy.context.scene
    curved=[o for o in scene.objects if o.type=="CURVE" and len(o.data.splines)>0]
    return curved

def mesh_triangles(obj):
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)

def attempt_tier(tier, keep_modulus):
    start=time.monotonic()
    curved=load_source()
    before=sum(len(o.data.splines) for o in curved)
    stats={"tier":tier,"before_strands":before,"input_curve_objects":[o.name for o in curved],
           "keep_modulus":keep_modulus,"input":{"blend":digest(SOURCE)}}
    if before<10000:raise RuntimeError("Expected original native groom missing: "+str(before))
    converted=[]
    for o in curved:
        n=len(o.data.splines)
        # For the LOD keep one in every three original guides, not a polygon
        # decimator that destroys the fragile cross section of down strands.
        if keep_modulus>1:
            sp=o.data.splines
            for i in range(n-1,-1,-1):
                if i%keep_modulus:sp.remove(sp[i])
        kept=len(o.data.splines)
        if not kept:continue
        bpy.ops.object.select_all(action="DESELECT")
        o.select_set(True);bpy.context.view_layer.objects.active=o
        bpy.ops.object.convert(target="MESH")
        mo=bpy.context.object
        mo.name="Run154 TRUE CURVE TO MESH "+o.name
        converted.append({"name":mo.name,"strands":kept,"triangles":mesh_triangles(mo)})
    stats["curve_conversions"]=converted
    stats["retained_strands"]=sum(x["strands"] for x in converted)
    stats["converted_hair_triangles"]=sum(x["triangles"] for x in converted)
    if stats["converted_hair_triangles"]<=0:raise RuntimeError("hair conversion empty")
    path=os.path.join(OUT,"run154_"+tier+"_FUR_IN_GLB_UNAPPROVED.glb")
    # Export material-bearing original actual mesh surfaces + actual converted hair.
    bpy.ops.object.select_all(action="DESELECT")
    selected=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    if not selected:raise RuntimeError("No owl mesh left for export")
    for o in selected:o.select_set(True)
    bpy.context.view_layer.objects.active=selected[0]
    bpy.ops.export_scene.gltf(filepath=path,export_format="GLB",
          use_selection=True,export_apply=True)
    if not os.path.isfile(path) or os.path.getsize(path)<100000:
        raise RuntimeError("GLB export unexpectedly missing/small")
    stats["glb"]=digest(path)
    stats["source_mesh_objects"]=len(selected)
    stats["source_triangles"]=sum(mesh_triangles(o) for o in selected)
    # Fresh reload, never mistake source .blend curves for transported geometry.
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=path)
    reload_meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    stats["roundtrip_meshes"]=len(reload_meshes)
    stats["roundtrip_triangles"]=sum(mesh_triangles(o) for o in reload_meshes)
    stats["roundtrip_hair_meshes"]=[
        {"name":o.name,"triangles":mesh_triangles(o)} for o in reload_meshes
        if "TRUE CURVE TO MESH" in o.name
    ]
    stats["roundtrip_hair_triangles"]=sum(m["triangles"] for m in stats["roundtrip_hair_meshes"])
    if stats["roundtrip_hair_triangles"]!=stats["converted_hair_triangles"]:
        raise RuntimeError("hair triangles lost on GLB roundtrip: "+str(stats["roundtrip_hair_triangles"]))
    # Independent real four-view rendered FROM REIMPORTED GLB, never from native curves.
    scene=bpy.context.scene
    scene.render.engine="CYCLES";scene.cycles.samples=8;scene.cycles.use_denoising=False
    scene.render.resolution_x=360;scene.render.resolution_y=360;scene.render.resolution_percentage=100
    scene.render.image_settings.file_format="PNG"
    world=bpy.data.worlds.new("Run154 inspection environment");world.use_nodes=True
    world.node_tree.nodes["Background"].inputs["Color"].default_value=(.65,.69,.73,1)
    world.node_tree.nodes["Background"].inputs["Strength"].default_value=.6
    scene.world=world
    def light(name,xyz,energy,size):
        bpy.ops.object.light_add(type="AREA",location=xyz);o=bpy.context.object
        o.name=name;o.data.energy=energy;o.data.shape="DISK";o.data.size=size
        o.rotation_euler=(Vector((0,0,1.24))-o.location).to_track_quat("-Z","Y").to_euler()
    light("key",(2,3.7,4.3),650,4.5);light("fill",(-3,0.9,3.2),450,4)
    light("back rim",(-1,-3.5,3.7),700,3.5)
    target=Vector((0,0,1.2))
    views={"front":(0,4.8,2.35),"quarter":(3.4,3.4,2.35),
           "side":(4.8,0,2.35),"back":(0,-4.8,2.35)}
    rendered=[]
    for name,loc in views.items():
        bpy.ops.object.camera_add(location=loc);cam=bpy.context.object
        cam.name="run154_"+tier+"_"+name
        cam.rotation_euler=(target-cam.location).to_track_quat("-Z","Y").to_euler()
        cam.data.type="ORTHO";cam.data.ortho_scale=2.85;scene.camera=cam
        outfile=os.path.join(OUT,tier+"_"+name+"_ACTUAL_REIMPORT_NO_RELEASE.png")
        scene.render.filepath=outfile
        bpy.ops.render.render(write_still=True)
        if not os.path.isfile(outfile) or os.path.getsize(outfile)<1000:
            raise RuntimeError("Rendering failed for "+name)
        rendered.append({"view":name,"image":digest(outfile),"name":os.path.basename(outfile)})
    stats["actual_render_from_reimport"]=rendered
    stats["seconds"]=round(time.monotonic()-start,2)
    outstat=os.path.join(OUT,tier+"_measured.json")
    with open(outstat,"w") as f:json.dump(stats,f,indent=2)
    print("RUN154_TIER_OK",json.dumps(stats),flush=True)
    return stats

try:
    tiers=[]
    tiers.append(attempt_tier("full",1))
    tiers.append(attempt_tier("lod3",3))
    summary={"experiment":"run154 actual GLB transported native Blender mesoptile groom",
             "source_run":153,"new_external_cost_usd":0,
             "art_acceptance":"UNREVIEWED_NO_RELEASE",
             "source_art_already_rejected":True,
             "glb_portable_hair":True,"mobile_webgl_tested":False,
             "production_files_modified":False,"results":tiers}
    with open(os.path.join(OUT,"run154_summary.json"),"w") as f:json.dump(summary,f,indent=2)
    with open(os.path.join(OUT,"NO_RELEASE.txt"),"w") as f:
        f.write("Run154 technical portability test on art-rejected Run153 sculpt. Do NOT publish or present as a successful juvenile pet. Real mobile GPU test not performed.\n")
    print("RUN154_COMPLETE_NO_RELEASE",flush=True)
except Exception:
    with open(os.path.join(OUT,"RUN154_ERROR.txt"),"w") as f:f.write(traceback.format_exc())
    print("RUN154_FAILED",traceback.format_exc(),flush=True)
    raise
