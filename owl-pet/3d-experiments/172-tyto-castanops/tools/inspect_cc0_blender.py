"""One-off Blender inspection of a license-checked EXTERNAL adult-owl base.

Source is NOT #172 Tyto castanops chick. This script is an acquisition/QA
experiment only; never promote its output to approved owl-pet production.
Run: blender -b --factory-startup --python inspect_cc0_blender.py -- INPUT.glb OUTDIR
"""
import bpy
import json
import math
import os
import sys
from mathutils import Vector

arg = sys.argv[sys.argv.index('--') + 1:]
src, out = arg[0], os.path.abspath(arg[1])
os.makedirs(out, exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=os.path.abspath(src))

meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH']
if not meshes:
    raise RuntimeError('Imported GLB has no mesh: reject acquisition')
for o in meshes:
    for p in o.data.polygons:
        p.use_smooth = True

bpy.context.view_layer.update()
corners = [o.matrix_world @ Vector(c) for o in meshes for c in o.bound_box]
low = Vector([min(v[i] for v in corners) for i in range(3)])
high = Vector([max(v[i] for v in corners) for i in range(3)])
size = high - low
center = (high + low) / 2
span = max(size)
if span <= 0:
    raise RuntimeError('Zero-size imported mesh')

tris_before = sum(len(p.vertices) - 2 for o in meshes for p in o.data.polygons)
report = {
    'input_file': os.path.basename(src),
    'source_is_juvenile': False,
    'source_license_claim': 'CC0 (independent source-page verification required)',
    'bounds_min': list(low), 'bounds_max': list(high), 'bbox_extent': list(size),
    'mesh_objects': len(meshes), 'original_triangles': tris_before,
    'material_count': len(bpy.data.materials),
    'image_names': [i.name for i in bpy.data.images],
    'blender_version': bpy.app.version_string,
}
# Actual rendered cardinal angles, not a 2D flip. Front orientation is
# provisional until a human looks at the reference asset orientation.
bpy.ops.object.camera_add()
camera = bpy.context.object
camera.name = 'InspectionCamera'
camera.data.type = 'ORTHO'
camera.data.ortho_scale = span * 1.65
camera.data.lens = 45
bpy.context.scene.camera = camera

def area_light(name, pos, power, size):
    bpy.ops.object.light_add(type='AREA', location=pos)
    o = bpy.context.object
    o.name = name
    o.data.energy = power
    o.data.shape = 'DISK'
    o.data.size = size

area_light('Key', center + Vector((span*1.5, -span*2, span*2.1)), 350, span*2)
area_light('Fill', center + Vector((-span*1.5, span*.3, span*1.3)), 200, span*2)
world = bpy.context.scene.world
if world is None:
    world = bpy.data.worlds.new('QA World')
    bpy.context.scene.world = world
world.use_nodes = True
world.node_tree.nodes['Background'].inputs['Color'].default_value = (.68,.71,.73,1)
world.node_tree.nodes['Background'].inputs['Strength'].default_value = .8
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.samples = 24
scene.cycles.use_denoising = False  # distro Blender built without OpenImageDenoiser
scene.render.resolution_x = 640
scene.render.resolution_y = 640
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.film_transparent = True
views = {
    'front': (0,-1,.15), 'threequarter': (.67,-.74,.2),
    'side': (1,0,.15), 'rear': (0,1,.15),
}
for label, direction in views.items():
    d = Vector(direction).normalized()
    camera.location = center + d * span * 3.4
    camera.rotation_euler = (center-camera.location).to_track_quat('-Z','Y').to_euler()
    scene.render.filepath = os.path.join(out, label + '.png')
    bpy.ops.render.render(write_still=True)

# Non-destructive LOD in a separate duplicated mesh-only collection. Original
# stays intact for inspection; export only the duplicates at the end.
for ob in list(bpy.context.scene.objects):
    if ob.type not in ('MESH',):
        bpy.data.objects.remove(ob, do_unlink=True)
orig = [o for o in bpy.context.scene.objects if o.type=='MESH']
for o in orig:
    o.select_set(False)
tri_target = 100000
factor = min(1.0, tri_target/max(1,tris_before))
if factor < 0.995:
    for o in orig:
        bpy.context.view_layer.objects.active=o
        modifier=o.modifiers.new('MobileDecimate','DECIMATE')
        modifier.ratio=max(.04, factor)
        bpy.ops.object.modifier_apply(modifier=modifier.name)

# Reduce source texture resolution without inventing shader data.
for im in bpy.data.images:
    if im.type == 'IMAGE' and im.has_data:
        w,h=im.size
        if max(w,h) > 1024:
            ratio=1024/max(w,h)
            im.scale(max(1,int(w*ratio)),max(1,int(h*ratio)))

bpy.ops.object.select_all(action='DESELECT')
for o in orig:
    o.select_set(True)
bpy.context.view_layer.objects.active=orig[0]
mobile_path=os.path.join(out,'external_owl_adult_lod_UNAPPROVED.glb')
bpy.ops.export_scene.gltf(filepath=mobile_path, export_format='GLB', use_selection=True)
report['mobile_triangles']=sum(len(p.vertices)-2 for o in orig for p in o.data.polygons)
report['mobile_glb_bytes']=os.path.getsize(mobile_path)
report['views_rendered']=list(views)
report['user_visual_gate']='NOT_REVIEWED_OR_APPROVED'
report['actual_mobile_webgl_gate']='NOT_TESTED'
with open(os.path.join(out,'import_inspection.json'),'w') as f:
    json.dump(report,f,indent=2)
print('OWL_INSPECTION_JSON='+json.dumps(report))
