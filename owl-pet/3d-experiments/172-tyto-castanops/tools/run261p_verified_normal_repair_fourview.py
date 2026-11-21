#!/usr/bin/env python3
"""Run261p: repair the missing actual vertex normals in the truly generated 20k-facet GLB.
Reuses EXACT SHA-pinned Run261 provider GLB, never regenerates/replaces owl body.
Returns an isolated research-only GLB with smooth vertex normals, true Blender
four-view render, explicit ART_UNAPPROVED/PHONE_UNTESTED/NO_RELEASE.
"""
import bpy,hashlib,math,pathlib,json
from mathutils import Vector
O=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run261p-ALPHA-FRAMED-NATIVE-REPAIR-NO_RELEASE")
SRC=O/"run261p_original_from_actual_run261_RESEARCH_ONLY.glb"
DST=O/"run261p_REAL_NATIVE_NORMAL_REPAIR_ART_UNAPPROVED.glb"
PIN="318a4c76986aca0f453fd1a07b60a103f0864656e0f60167b42c4995932e31df"
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert SRC.is_file() and digest(SRC)==PIN,"Source is not Run261 actual verified provider geometry"
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(SRC))
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert meshes
counts0=[len(o.data.polygons) for o in meshes]
assert sum(counts0)==20000,"Original unexpected geometry; no shape substitution"
for obj in meshes:
    for poly in obj.data.polygons: poly.use_smooth=True
    obj.data.update()
    for mat in obj.data.materials:
        if mat and mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.type=="BSDF_PRINCIPLED":
                    node.inputs["Base Color"].default_value=(.82,.80,.72,1)
                    node.inputs["Roughness"].default_value=.86
bpy.ops.export_scene.gltf(filepath=str(DST),export_format="GLB",export_apply=True,
    export_normals=True,export_materials="EXPORT")
assert DST.stat().st_size>1024
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(DST))
ms=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert sum(len(o.data.polygons) for o in ms)==20000,"Re-export geometry lost or altered"
pts=[o.matrix_world@Vector(v) for o in ms for v in o.bound_box]
lo=Vector(tuple(min(q[i] for q in pts) for i in range(3)))
hi=Vector(tuple(max(q[i] for q in pts) for i in range(3)))
center=(lo+hi)*.5; ext=max(hi-lo)
scene=bpy.context.scene
scene.world=bpy.data.worlds.new("run261p actual studio")
scene.world.color=(.42,.42,.42)
scene.render.engine="CYCLES";scene.cycles.samples=20
scene.render.resolution_x=500;scene.render.resolution_y=500
scene.view_layers[0].cycles.use_denoising=False
def light(xyz,power):
    data=bpy.data.lights.new("native area","AREA")
    data.energy=power;data.size=ext*3.5
    ob=bpy.data.objects.new("native area",data)
    scene.collection.objects.link(ob)
    ob.location=center+Vector(xyz)*ext
    ob.rotation_euler=(center-ob.location).to_track_quat("-Z","Y").to_euler()
light((-3,-3,3),390);light((3,2,2),230)
cam=bpy.data.objects.new("native orbit",bpy.data.cameras.new("native orbit"))
scene.collection.objects.link(cam);scene.camera=cam
cam.data.type="ORTHO";cam.data.ortho_scale=ext*1.65
views=[]
for name,deg in (("front",0),("quarter",45),("side",90),("back",180)):
    ang=math.radians(deg)
    cam.location=center+Vector((4*math.sin(ang),-4*math.cos(ang),1.25))*ext
    cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
    path=O/("run261p_"+name+"_ACTUAL_BLENDER_ART_UNAPPROVED.png")
    scene.render.filepath=str(path)
    bpy.ops.render.render(write_still=True)
    views.append(dict(name=name,file=path.name,sha256=digest(path)))
result=dict(run="258p",input_glb_sha256=PIN,output_glb_sha256=digest(DST),
 input_triangle_count=sum(counts0),reimport_triangle_count=sum(len(o.data.polygons) for o in ms),
 imported_real_meshes=len(ms),output_bytes=DST.stat().st_size,blender_version=bpy.app.version_string,
 actual_four_blender_views=views,real_geometry_preserved=True,
 skin_down_anatomy_approved=False,art_approved=False,physical_mobile_tested=False,release="NO_RELEASE")
(O/"run261p_native_actual_report.json").write_text(json.dumps(result,indent=2)+"\n")
print("RUN258P_NATIVE_REAL_REPAIR_REPORT",json.dumps(result))
