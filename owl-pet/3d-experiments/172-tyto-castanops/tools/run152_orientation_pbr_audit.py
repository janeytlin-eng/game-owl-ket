#!/usr/bin/env python3
"""Run152: real Run151 GLB, anatomically corrected camera and PBR-only ablation.
Never synthesize shape, draw SVG, certify art, or publish quarantined third-party binary.
"""
import json,hashlib,sys,math,random
from pathlib import Path
R=Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run152-ORIENTATION-PBR-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
PIN="f05ad553ebf00a495a4f1593ca2a1949a277ad98ecdd334cb4a75d7283bbec76"
GLB=O/"run151_original_RESEARCH_ONLY.glb"
def write(name,data): (O/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n")
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def render():
    import bpy
    from mathutils import Vector
    if not GLB.is_file(): raise RuntimeError("NO_SOURCE_GLB: cannot claim any model")
    actual=sha(GLB)
    if actual!=PIN: raise RuntimeError("SOURCE_HASH_MISMATCH: "+actual)
    negatives=json.loads((R/"known_rejected_asset_sha256_registry.json").read_text())
    known={i["sha256"] for i in negatives["known_rejected_source_glbs"]}
    if actual in known: raise RuntimeError("NEW_SOURCE_ALREADY_REJECTED")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(GLB))
    meshes=[x for x in bpy.context.scene.objects if x.type=="MESH"]
    assert meshes
    world_positions=[obj.matrix_world@Vector(v) for obj in meshes for v in obj.bound_box]
    low=Vector(tuple(min(v[i] for v in world_positions) for i in range(3)))
    high=Vector(tuple(max(v[i] for v in world_positions) for i in range(3)))
    center=(low+high)/2
    extent=max(high-low)
    assert extent>0.2
    stats=dict(run=152,input_sha256=actual,source_run=151,
       scene_meshes=len(meshes),polygons=sum(len(x.data.polygons) for x in meshes),
       bounds=list(high-low),blender=bpy.app.version_string,
       orientation_note="Run151 front photograph showed back at world -Y; corrected anatomical front camera at +Y",
       four_view_angles={"front":"+Y","quarter":"+Y,+X","strict_side":"+X","back":"-Y"},
       experiment="Original PBR versus shader-only cream surface lift: no geometry modification and no assertion GLB export will preserve that shader")
    scene=bpy.context.scene
    scene.render.engine="CYCLES"
    scene.cycles.samples=16
    scene.view_layers[0].cycles.use_denoising=False
    scene.render.resolution_x=480;scene.render.resolution_y=480
    scene.render.resolution_percentage=100
    scene.render.film_transparent=False
    world=bpy.data.worlds.new("Run152 neutral world") if scene.world is None else scene.world
    scene.world=world
    world.use_nodes=True; world.node_tree.nodes.get("Background").inputs["Color"].default_value=(.65,.66,.68,1)
    world.node_tree.nodes.get("Background").inputs["Strength"].default_value=.7
    def area(name,xyz,power,size):
        ob=bpy.data.objects.new(name,bpy.data.lights.new(name,"AREA"));scene.collection.objects.link(ob)
        ob.data.energy=power;ob.data.shape="DISK";ob.data.size=extent*size
        ob.location=center+Vector(xyz)*extent
        ob.rotation_euler=(center-ob.location).to_track_quat("-Z","Y").to_euler()
    area("Run152 key",(2,3,3),330,3)
    area("Run152 rim",(-3,-2,2),220,2)
    cam=bpy.data.objects.new("Run152 anatomical camera",bpy.data.cameras.new("Run152 anatomical camera"))
    scene.collection.objects.link(cam);scene.camera=cam
    cam.data.type="ORTHO";cam.data.ortho_scale=extent*1.52
    # The source looks toward world +Y in verified Run151 actual contact:
    # +Y = face, -Y = back. Run151 had these labels reversed.
    views={"front":(0,4,1.0),"quarter":(2.8,2.8,1.0),
           "side":(4,0,0.8),"back":(0,-4,1.0)}
    def shoot(label):
        files=[]
        for name,d in views.items():
            cam.location=center+Vector(d)*extent
            cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
            p=O/("run152_"+label+"_"+name+"_ACTUAL_CYCLES_UNAPPROVED.png")
            scene.render.filepath=str(p)
            bpy.ops.render.render(write_still=True)
            if not p.exists() or p.stat().st_size<1000:raise RuntimeError("ACTUAL_RENDER_MISSING "+str(p))
            files.append(p.name)
        return files
    stats["baseline_actual_files"]=shoot("original")
    # Actual PBR experiment: modify ONLY material response. It is deliberately
    # not represented as anatomy correction, feather geometry, or distributable GLB.
    touched=[]
    for mat in bpy.data.materials:
        if not mat.use_nodes:continue
        nt=mat.node_tree
        for bsdf in list(nt.nodes):
            if bsdf.type!="BSDF_PRINCIPLED":continue
            sock=bsdf.inputs.get("Base Color")
            if not sock:continue
            oldlink=next((l for l in nt.links if l.to_socket==sock),None)
            if oldlink:
                upstream=oldlink.from_socket
                mix=nt.nodes.new("ShaderNodeMixRGB")
                mix.name="Run152 cream lift test (not model change)"
                mix.blend_type="MIX"
                mix.inputs[0].default_value=.28
                mix.inputs[2].default_value=(.93,.87,.76,1)
                nt.links.new(upstream,mix.inputs[1])
                nt.links.remove(oldlink)
                nt.links.new(mix.outputs[0],sock)
                touched.append(mat.name)
            else:
                v=sock.default_value
                sock.default_value=(v[0]*.72+.93*.28,v[1]*.72+.87*.28,v[2]*.72+.76*.28,v[3])
                touched.append(mat.name)
            rough=bsdf.inputs.get("Roughness")
            if rough and not rough.is_linked: rough.default_value=max(.72,rough.default_value)
    stats["pbr_touched_materials"]=touched
    stats["toned_actual_files"]=shoot("toned")
    stats["all_eight_native_renders_present"]=True
    stats["release_decision"]="ART_UNREVIEWED / NO_RELEASE"
    stats["physical_phone_gpu_test"]=False
    stats["redistribution_rights_cleared"]=False
    write("run152_actual_blender_stats.json",stats)
    print("RUN152_NATIVE_COMPLETED",json.dumps(stats))
if __name__=="__main__":
    if sys.argv[-1]=="render": render()
    else:raise SystemExit("Pass -- render")
