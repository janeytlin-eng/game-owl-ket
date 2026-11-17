"""Blender-only four-angle inspection for legitimately acquired external GLB; not an art approval."""
import bpy,sys,math,json
from mathutils import Vector
from pathlib import Path
args=sys.argv[sys.argv.index("--")+1:]
source=Path(args[0]).resolve(); output=Path(args[1]).resolve()
bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(source))
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
if not meshes:raise RuntimeError("asset has no importable 3D mesh")
worldpts=[o.matrix_world@Vector(p) for o in meshes for p in o.bound_box]
mi=Vector([min(p[i] for p in worldpts) for i in range(3)])
ma=Vector([max(p[i] for p in worldpts) for i in range(3)])
center=(mi+ma)/2
extent=max((ma-mi)[:])
if extent<=0:raise RuntimeError("degenerate mesh")
scene=bpy.context.scene
scene.render.engine="CYCLES";scene.cycles.samples=24
scene.render.resolution_x=520;scene.render.resolution_y=520;scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
scene.world.color=(0.22,0.22,0.22)
bpy.ops.object.camera_add();cam=bpy.context.object;scene.camera=cam
cam.data.type="ORTHO";cam.data.ortho_scale=extent*1.85
for loc,power,size in [((2,3,5),650,5),((-3,2,2),480,4)]:
    bpy.ops.object.light_add(type="AREA", location=tuple(center[i]+loc[i]*extent for i in range(3)))
    light=bpy.context.object;light.data.energy=power;light.data.shape="DISK";light.data.size=size
for name,az in [("front",0),("quarter",45),("side",90),("back",180)]:
    a=math.radians(az)
    cam.location=center+Vector((math.sin(a)*extent*2.7,-math.cos(a)*extent*2.7,extent*0.6))
    target=center+Vector((0,0,extent*0.02))
    cam.rotation_euler=(target-cam.location).to_track_quat("-Z","Y").to_euler()
    scene.render.filepath=str(output/("run123_"+name+"_actual_blender_inspection.png"))
    bpy.ops.render.render(write_still=True)
(output/"run123_candidate_mesh_metrics.json").write_text(json.dumps({
 "source_file":source.name,
 "blender_version":bpy.app.version_string,
 "mesh_objects":len(meshes),
 "total_triangles":sum(sum(len(p.vertices)-2 for p in o.data.polygons) for o in meshes),
 "world_extent":list(ma-mi),
 "note":"camera-up assumed +Z; display only for manual art review; NO_RELEASE"
},indent=2))
