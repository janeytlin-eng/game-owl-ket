#!/usr/bin/env python3
"""Read-only, source-verified GLB Blender inspection. NO_RELEASE, not a model-generation claim."""
import bpy, json, math, pathlib, sys, hashlib
from mathutils import Vector

if "--" not in sys.argv:
    raise SystemExit("requires '-- MODEL.glb OUTPUT_DIR'")
model_arg, out_arg = sys.argv[sys.argv.index("--") + 1:][:2]
model = pathlib.Path(model_arg).resolve()
out = pathlib.Path(out_arg).resolve()
out.mkdir(parents=True, exist_ok=True)
if not model.is_file() or model.stat().st_size < 100:
    raise RuntimeError("Missing genuine native GLB")
expected = "8ff7341725e4fc27caf3ff4dbb3b07fe9231a96d216de31317bddf2aa07a7b8b"
digest = hashlib.sha256(model.read_bytes()).hexdigest()
if digest != expected:
    raise RuntimeError("Source SHA mismatch; refuse to render unverified download " + digest)
assert model.read_bytes()[:4] == b"glTF"
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(model))
meshes = [ob for ob in bpy.context.scene.objects if ob.type == "MESH"]
if not meshes: raise RuntimeError("No mesh objects imported from actual GLB")

pts = [ob.matrix_world @ Vector(v) for ob in meshes for v in ob.bound_box]
mi = Vector([min(p[i] for p in pts) for i in range(3)])
ma = Vector([max(p[i] for p in pts) for i in range(3)])
center = (mi + ma) / 2
extents = ma-mi
span = max(extents.length,0.001)
sc = bpy.context.scene
sc.render.engine = "BLENDER_EEVEE"
sc.render.resolution_x=544
sc.render.resolution_y=544
sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG"
sc.render.film_transparent=False
sc.render.filepath = str(out / "test.png")
sc.view_settings.view_transform="Standard"
if sc.world is None:
    sc.world = bpy.data.worlds.new("run166-neutral-background")
sc.world.use_nodes=True
bg=sc.world.node_tree.nodes.get("Background")
if bg:
    bg.inputs["Color"].default_value=(0.24,0.27,0.30,1.0)
    bg.inputs["Strength"].default_value=0.7
camd=bpy.data.cameras.new("uncalibrated-orbit")
cam=bpy.data.objects.new("uncalibrated-orbit",camd)
sc.collection.objects.link(cam)
sc.camera=cam
camd.type="ORTHO"
camd.ortho_scale=span*1.55

for i,(position,power) in enumerate([((1,1,1.7),730),((-1,0.5,0.8),390),((0,-1,1.2),260)]):
    ld=bpy.data.lights.new("softbox-"+str(i),"AREA")
    lo=bpy.data.objects.new("softbox-"+str(i),ld)
    sc.collection.objects.link(lo)
    lo.location=center+Vector(position)*span
    ld.energy=power
    ld.shape="DISK"
    ld.size=span*1.7
    lo.rotation_euler=(center-lo.location).to_track_quat("-Z","Y").to_euler()

# Explicitly mark model-local axes: source orientation has not been calibrated against
# source image, so these are objective viewing directions, NOT asserted anatomical front/back.
directions=[
    ("axis_plusY", (0,1,0.12)),
    ("axis_plusY_plusX_45",(1,1,0.12)),
    ("axis_plusX",(1,0,0.12)),
    ("axis_minusY",(0,-1,0.12)),
    ("axis_minusX",(-1,0,0.12))
]
rendered=[]
for label, vec in directions:
    cam.location=center+Vector(vec).normalized()*span*2.1
    cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
    sc.render.filepath=str(out/("run166_sf3d_"+label+"_UNREVIEWED.png"))
    bpy.ops.render.render(write_still=True)
    img=pathlib.Path(sc.render.filepath)
    if not img.is_file() or img.stat().st_size<10000:
        raise RuntimeError("Failed native render "+str(img))
    rendered.append({"camera_axis":label,"path":img.name,"bytes":img.stat().st_size,
                     "sha256":hashlib.sha256(img.read_bytes()).hexdigest()})

meta={
 "source_file":model.name,"source_sha256":digest,"source_bytes":model.stat().st_size,
 "blender_version":bpy.app.version_string,"mesh_count":len(meshes),
 "vertex_count":sum(len(x.data.vertices) for x in meshes),
 "face_count":sum(len(x.data.polygons) for x in meshes),
 "triangulated_face_estimate":sum(sum(max(len(p.vertices)-2,1) for p in x.data.polygons) for x in meshes),
 "materials_count":len([m for m in bpy.data.materials if m.users]),
 "texture_images":[{"name":im.name,"w":im.size[0],"h":im.size[1]}
                   for im in bpy.data.images if im.size[0]>1 and im.size[1]>1],
 "bounds":[round(float(v),5) for v in extents],
 "source_orientation":"uncalibrated; +Y/+X/-Y/-X are local model axes, not anatomical labels",
 "views":rendered,"art_decision":"UNREVIEWED","mobile_physical_gpu":"NOT_TESTED",
 "release":False
}
(out/"run166_blender_native_metrics.json").write_text(json.dumps(meta,indent=2,ensure_ascii=False))
print("RUN166_NATIVE_FOUR_AXIS_RENDER_COMPLETE",json.dumps({k:v for k,v in meta.items() if k!="views"}))
