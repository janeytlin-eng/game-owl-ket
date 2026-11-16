#!/usr/bin/env python3
"""Run120: independent purported-CC0 real owl GLB import, native 4-view and mobile LOD audit.
This script does NOT approve the asset as #172's age-unknown Tyto castanops chick.
No synthetic primitive owl, SVG, mock GLB, or release output.
"""
import sys, pathlib, json, hashlib, math
import bpy
from mathutils import Vector

assert "--" in sys.argv
src=pathlib.Path(sys.argv[sys.argv.index("--")+1])
out=pathlib.Path(sys.argv[sys.argv.index("--")+2]);out.mkdir(parents=True,exist_ok=True)
digest=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
assert src.is_file() and src.stat().st_size>200000 and src.open("rb").read(4)==b"glTF"
bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(src))
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert meshes,"No imported 3D meshes, reject"
original_triangles=sum(len(o.data.loop_triangles) for o in meshes)
assert original_triangles>10000,"Too little organic anatomical topology to claim high-detail source"
world_pts=[o.matrix_world@v.co for o in meshes for v in o.data.vertices]
low=Vector(tuple(min(p[k] for p in world_pts) for k in range(3)))
high=Vector(tuple(max(p[k] for p in world_pts) for k in range(3)))
center=(low+high)*.5; size=high-low; longest=max(size)
assert 0<longest<10000,"Invalid source units"
scene=bpy.context.scene
scene.render.engine="CYCLES";scene.cycles.samples=20;scene.cycles.use_denoising=False
for layer in scene.view_layers:layer.cycles.use_denoising=False
scene.render.resolution_x=480;scene.render.resolution_y=480;scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
scene.view_settings.view_transform="Standard"
scene.world.color=(.22,.22,.22)
def area(name,offset,power,width):
    data=bpy.data.lights.new(name,"AREA");data.energy=power;data.size=width*longest
    ob=bpy.data.objects.new(name,data);scene.collection.objects.link(ob)
    ob.location=center+Vector(offset)*longest
    ob.rotation_euler=(center-ob.location).to_track_quat("-Z","Y").to_euler()
area("key",(-2.4,-3,2.3),450,3.5)
area("fill",(2,-1.5,1.3),270,3)
area("rim",(1.5,2.3,2.2),330,3)
camdata=bpy.data.cameras.new("true_orbit_camera")
cam=bpy.data.objects.new("true_orbit_camera",camdata);scene.collection.objects.link(cam);scene.camera=cam
camdata.type="ORTHO";camdata.ortho_scale=longest*1.65
# Disable display of rig armatures or miscellaneous clutter if imported.
for o in bpy.context.scene.objects:
    if o.type not in {"MESH","CAMERA","LIGHT"}:o.hide_render=True
for name,deg in [("front",0),("quarter",45),("side",90),("back",180)]:
    phi=math.radians(deg)
    cam.location=center+Vector((3.6*math.sin(phi),-3.6*math.cos(phi),.70))*longest
    cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
    scene.render.filepath=str(out/("run120_source_"+name+"_real_cycles_RESEARCH_ONLY.png"))
    bpy.ops.render.render(write_still=True)
# Non-destructive, independent mobile geometry derivative of a real textured source.
for o in meshes:
    if o.type=="MESH" and len(o.data.polygons)>1000:
        frac=min(1., max(.01, 95000/original_triangles))
        if frac<.98:
            bpy.context.view_layer.objects.active=o
            bpy.ops.object.select_all(action="DESELECT");o.select_set(True)
            m=o.modifiers.new("mobile_lod_real_mesh_decimate","DECIMATE")
            m.ratio=frac;bpy.ops.object.modifier_apply(modifier=m.name)
bpy.ops.object.select_all(action="DESELECT")
for o in meshes:o.select_set(True)
bpy.context.view_layer.objects.active=meshes[0]
lod=out/"run120_independent_CC0_claim_source_LOD_ART_UNAPPROVED.glb"
bpy.ops.export_scene.gltf(filepath=str(lod),export_format="GLB",use_selection=True,export_materials="EXPORT")
assert lod.read_bytes()[:4]==b"glTF" and lod.stat().st_size>150000
before=set(bpy.context.scene.objects)
bpy.ops.import_scene.gltf(filepath=str(lod))
reimport=[o for o in bpy.context.scene.objects if o not in before and o.type=="MESH"]
assert reimport,"Exported GLB did not load"
lod_triangles=sum(len(o.data.loop_triangles) for o in reimport)
assert lod_triangles>1000
for o in reimport:bpy.data.objects.remove(o,do_unlink=True)
report={"run":120,"purpose":"Independent purported CC0 real owl 3D suitability benchmark",
        "source":str(src),"source_bytes":src.stat().st_size,"source_sha256":digest(src),
        "source_meshes":len(meshes),"source_triangles":original_triangles,
        "source_bounds_xyz_m_not_verified":list(size),"lod_triangles":lod_triangles,
        "lod_bytes":lod.stat().st_size,"lod_sha256":digest(lod),
        "blender_version":bpy.app.version_string,"real_4_views":4,
        "source_license":"Source website claims CC0; upstream rights NOT independently cleared",
        "art_review":"ART_REJECTED until confirmed juvenile Tyto anatomy, heart face, soft cream down, 4-side support and physical mobile QA",
        "release":"NO_RELEASE"}
(out/"run120_real_3d_mesh_import_lod_metrics.json").write_text(json.dumps(report,indent=2),encoding="utf8")
print("RUN120_REAL_MESH_AND_LOD_DONE_NOT_ART_APPROVAL",json.dumps(report))
