#!/usr/bin/env python3
"""Run102: physically deform real Run100 Hunyuan bird mesh with morph targets.
Research-only animatability/phone WebGL probe; NOT artistic certification.
NO fake 2D, SVG or primitive replacement. GLB source is Tencent Hunyuan3D-2
community-licensed and not CC0; no product / global-use approval implied.
"""
import bpy
import sys, json, math, hashlib, struct, pathlib
from mathutils import Vector, Matrix

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
assert len(argv) == 2, "blender --python ... -- SOURCE.glb EVIDENCE_DIR"
source, out = pathlib.Path(argv[0]), pathlib.Path(argv[1])
out.mkdir(parents=True, exist_ok=True)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
EXPECTED_SOURCE_SHA = "60feb7a5e4f4c67a020e3457e7ffbfb52f6fbe3e75f115b970030c00b20cd35d"
assert source.stat().st_size == 1433708 and sha(source) == EXPECTED_SOURCE_SHA, "neural input changed"
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(source))
objs = [x for x in bpy.context.scene.objects if x.type == 'MESH']
assert len(objs) == 1, f"Expected single true sculpt mesh, got {len(objs)}"
obj = objs[0]
assert len(obj.data.polygons) == 79988
verts = obj.data.vertices
assert len(verts) == 39684
coords = [v.co.copy() for v in verts]
lo = Vector((min(v.x for v in coords), min(v.y for v in coords), min(v.z for v in coords)))
hi = Vector((max(v.x for v in coords), max(v.y for v in coords), max(v.z for v in coords)))
mid = (lo + hi) / 2
size = hi - lo
assert min(size) > 0.05 and size.z > 0.25
smooth = lambda x: (max(0.0,min(1.0,x))**2) * (3.0-2.0*max(0.0,min(1.0,x)))
obj.shape_key_add(name="Basis", from_mix=False)
breath = obj.shape_key_add(name="SoftTorsoBreathing", from_mix=False)
head = obj.shape_key_add(name="QuietHeadTilt", from_mix=False)
modified_breath = 0
modified_head = 0
max_breath = 0.
max_head = 0.
pivot = Vector((mid.x, mid.y, lo.z + size.z*.78))
# Weight fields follow the true bird's original sculpt, not a substitute sphere.
# Lower breast rises subtly, head tilts around upper-neck pivot; stable toes.
angle = math.radians(3.2)
rotation = Matrix.Rotation(angle, 3, 'X')
for i, p in enumerate(coords):
    zf = (p.z-lo.z)/size.z
    body_weight = smooth((zf-.14)/.19) * (1.-smooth((zf-.64)/.17))
    # Real existing mesh vertices deform as a continuous surface.
    offset = Vector(((p.x-mid.x)*.025*body_weight,
                     (p.y-mid.y)*.018*body_weight,
                     size.z*.006*body_weight))
    breath.data[i].co = p + offset
    if offset.length > 0.00001: modified_breath += 1
    max_breath = max(max_breath, offset.length)
    tilt_weight = smooth((zf-.58)/.27)
    rotated = pivot + rotation @ (p-pivot)
    delta = (rotated-p)*tilt_weight
    head.data[i].co = p + delta
    if delta.length > .00001: modified_head += 1
    max_head = max(max_head, delta.length)
assert modified_breath > 5000 and modified_head > 2000
assert max_breath < max(size)*0.04 and max_head < max(size)*0.08
# Native Blender shape-key keyframes should export as glTF animation weights.
scene = bpy.context.scene
scene.frame_start, scene.frame_end = 1, 49
scene.render.fps = 24
for f,b,h in ((1,0.,0.),(9,.5,.10),(17,1.,.3),(25,.7,.9),
              (33,.35,.5),(41,.2,.1),(49,0.,0.)):
    breath.value=b
    head.value=h
    breath.keyframe_insert(data_path='value', frame=f)
    head.keyframe_insert(data_path='value', frame=f)
scene.frame_set(1)
if obj.data.shape_keys.animation_data is None or not obj.data.shape_keys.animation_data.action:
    raise RuntimeError("No real Blender morph animation action")
action = obj.data.shape_keys.animation_data.action
action.name = "Run102_SubtleLivingChick_RESEARCH_ONLY"
for poly in obj.data.polygons: poly.use_smooth = True
if not obj.data.materials:
    mat = bpy.data.materials.new("Run102_existing_neural_surface_cream_nonmetal")
    mat.diffuse_color = (.89,.82,.72,1)
    mat.use_nodes = True
    mat.node_tree.nodes.get("Principled BSDF").inputs["Base Color"].default_value=(.89,.82,.72,1)
    obj.data.materials.append(mat)
for mat in obj.data.materials:
    if mat and mat.use_nodes:
        bsdf=next((n for n in mat.node_tree.nodes if n.type=='BSDF_PRINCIPLED'),None)
        if bsdf:
            bsdf.inputs["Metallic"].default_value=0.0
            bsdf.inputs["Roughness"].default_value=.92
bpy.ops.object.select_all(action='DESELECT')
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
outglb=out/"run102_real_neural_morph_loop_ART_UNAPPROVED.glb"
bpy.ops.export_scene.gltf(filepath=str(outglb),export_format="GLB",use_selection=True,
                          export_animations=True,export_morph=True,export_normals=True,
                          export_materials="EXPORT")
data=outglb.read_bytes()
assert data[:4]==b'glTF' and struct.unpack_from('<I',data,8)[0]==len(data)
json_size,chunk=struct.unpack_from('<I4s',data,12)
assert chunk==b'JSON'
doc=json.loads(data[20:20+json_size].decode().rstrip(' \x00'))
morphs=[len(p.get('targets',[])) for m in doc.get('meshes',[]) for p in m.get('primitives',[])]
weights=[c for a in doc.get('animations',[]) for c in a.get('channels',[])
         if c.get('target',{}).get('path')=='weights']
assert max(morphs or [0])>=2, "Missing true 3D mesh morph target attributes"
assert weights, "Missing glTF animation of morph-target weights"
assert doc.get("animations"), "Missing glTF animation clips"
print("RUN102_REAL_GLB_ANIMATED",len(data),len(weights),flush=True)
# Independent Blender re-import validates file exists, topology and shapekeys.
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(outglb))
roundobj=[o for o in bpy.context.scene.objects if o.type=='MESH']
assert roundobj and sum(len(o.data.polygons) for o in roundobj)>79000
assert any(o.data.shape_keys and len(o.data.shape_keys.key_blocks)>=3 for o in roundobj)
assert bpy.data.actions, "No Blender animation action after glTF roundtrip"
obj=roundobj[0]
for mat in obj.data.materials:
    if mat and mat.use_nodes:
        shader=next((n for n in mat.node_tree.nodes if n.type=='BSDF_PRINCIPLED'),None)
        if shader:
            shader.inputs["Metallic"].default_value=0.
            shader.inputs["Roughness"].default_value=.92
# Render same reimported real mesh from four camera locations; keyframe 1 vs 17
# are later independently animated in Chromium and checked for morph movement.
bounds=[obj.matrix_world@Vector(c) for c in obj.bound_box]
center=Vector(tuple((min(p[i] for p in bounds)+max(p[i] for p in bounds))*.5 for i in range(3)))
scale=max(max(p[i] for p in bounds)-min(p[i] for p in bounds) for i in range(3))
scene=bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=16
scene.cycles.use_denoising=False
scene.render.resolution_x=448
scene.render.resolution_y=448
scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.render.film_transparent=False
scene.world.color=(.45,.45,.45)
scene.view_settings.view_transform="Standard"
def area(name,xyz,power,width):
    ld=bpy.data.lights.new(name,'AREA')
    ld.energy=power
    ld.size=width*scale
    o=bpy.data.objects.new(name,ld)
    scene.collection.objects.link(o)
    o.location=center+Vector(xyz)*scale
    o.rotation_euler=(center-o.location).to_track_quat('-Z','Y').to_euler()
area('soft_key',(-2.5,-3,3.1),360,4)
area('soft_fill',(2,-2,1.5),120,3.5)
area('rear_rim',(1.5,2,3),170,3)
camdata=bpy.data.cameras.new('run102_camera')
camera=bpy.data.objects.new('run102_camera',camdata)
scene.collection.objects.link(camera)
scene.camera=camera
camdata.type='ORTHO'
camdata.ortho_scale=1.68*scale
for name,angle in (("front",0),("quarter",45),("side",90),("back",180)):
    a=math.radians(angle)
    camera.location=center+Vector((4*math.sin(a),-4*math.cos(a),1.3))*scale
    camera.rotation_euler=(center-camera.location).to_track_quat('-Z','Y').to_euler()
    scene.frame_set(1)
    scene.render.filepath=str(out/(f"run102_{name}_frame01_cycles.png"))
    bpy.ops.render.render(write_still=True)
    print("RUN102_REAL_RENDER",name,flush=True)
# Save the Blender keyframe state check even when glTF exporter changes action.
report={
 "source_sha256":sha(source),"source_license":"Tencent Hunyuan3D-2 Community License; NOT CC0",
 "source_faces":79988,"source_vertices":39684,
 "breath_modified_real_vertices":modified_breath,"head_modified_real_vertices":modified_head,
 "max_breath_geometry_delta":max_breath,"max_head_geometry_delta":max_head,
 "blender_animation":action.name,"glb":outglb.name,
 "glb_bytes":outglb.stat().st_size,"sha256":sha(outglb),
 "glb_morph_target_counts":morphs,
 "glb_weight_animation_channels":len(weights),
 "glb_animation_clips":len(doc.get('animations',[])),
 "reimport_real_tris":sum(len(o.data.polygons) for o in roundobj),
 "reimport_shape_key_counts":[len(o.data.shape_keys.key_blocks) if o.data.shape_keys else 0 for o in roundobj],
 "real_phone_gpu_tested":False,"visual_art_approved":False,"unrestricted_licensed":False,"cost_usd":0
}
(out/"run102_native_metrics.json").write_text(json.dumps(report,indent=2))
(out/"ART_GATE_NOT_PASSED.md").write_text(
 "# Run102 — REAL neural source bird morph animation, ART_UNAPPROVED\n\n"
 "Actual Blender 3D vertex shape keys for breathing and tiny head motion; exported "
 "glTF morph targets and animation, reimported and rendered natively. This is an "
 "animation/WebGL research probe, NOT an approved juvenile mesh. Existing source "
 "still has hard/scaled feather detail, closed eyes, unresolved independent side/back "
 "anatomy, missing supported feet/eucalyptus hollow, no real phone GPU test, "
 "and unresolved Tencent license. Do not publish. Do not modify 251 species pipeline.\n")
print("RUN102_METRICS",json.dumps(report),flush=True)
