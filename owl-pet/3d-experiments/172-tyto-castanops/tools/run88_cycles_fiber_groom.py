"""Run88: physically meaningful Cycles fiber groom proof-of-technique on Run87
artist-authored CC0 source retarget, NOT a Tyto castanops release.
True Blender hair guides/children, NOT 2D SVG/primitive masquerading.
Blender hair does not export to GLB: reject mobile/deployment until baked.
"""
import bpy, os, sys, math, json, hashlib
from mathutils import Vector
src,out=sys.argv[sys.argv.index('--')+1:sys.argv.index('--')+3]
os.makedirs(out,exist_ok=True)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=src)
meshes=[o for o in bpy.data.objects if o.type=='MESH']
assert len(meshes)>40, "Expected artist-authored GLB and scene"
body_candidates=[o for o in meshes if 'continuous anatomical skin' in o.name.lower()]
if not body_candidates:
    body_candidates=sorted(meshes,key=lambda o:len(o.data.polygons),reverse=True)[:1]
body=body_candidates[0]
assert len(body.data.polygons)>10000, "No detailed organic source surface"
# Pigment changes do not assert corrected baby anatomy. Preserve dark eyes, bill,
# pupils, irises and talons; desaturate other surfaces to a creamy down undercoat.
tinted=[]
skipped=[]
for mat in bpy.data.materials:
    n=mat.name.lower()
    if any(q in n for q in ['iris','eyeball','pupil','sclera','beak','bill','claw','talon','cornea']):
        skipped.append(mat.name)
        continue
    if not mat.use_nodes:
        mat.diffuse_color=(.94,.865,.744,1)
        tinted.append(mat.name)
        continue
    bs=next((node for node in mat.node_tree.nodes if node.type=='BSDF_PRINCIPLED'),None)
    if not bs: continue
    links=list(bs.inputs['Base Color'].links)
    # One unified cream color, retaining an original albedo's luminance at
    # modest opacity if present. This tests groom against a non-brown body.
    mix=mat.node_tree.nodes.new('ShaderNodeMixRGB')
    mix.blend_type='MIX'
    mix.inputs[0].default_value=.90
    mix.inputs[2].default_value=(.966,.894,.786,1)
    if links:
        origin=links[0].from_socket
        mat.node_tree.links.remove(links[0])
        mat.node_tree.links.new(origin,mix.inputs[1])
    else:
        mix.inputs[1].default_value=bs.inputs['Base Color'].default_value
    mat.node_tree.links.new(mix.outputs[0],bs.inputs['Base Color'])
    bs.inputs['Roughness'].default_value=.84
    tinted.append(mat.name)
# Apply a spatially feather-weighted particle field to original real skin.
# Forbid hair across the eye/facial disc and the supporting lower extremity.
group=body.vertex_groups.new(name="Run88AnatomicDownDensity")
values=[]
for v in body.data.vertices:
    p=body.matrix_world@v.co
    x,y,z=p.x,p.y,p.z
    lower=max(0.,min(1.,(z-.080)/.060))
    weight=lower
    if x>.058 and z>.205:
        # open central heart mask; preserve a soft feathered transition on rim
        core=max(0.,min(1.,(abs(y)-.078)/.035))
        cheek=max(0.,min(1.,(.46-z)/.05))
        weight*=max(.02,core,.20*cheek)
    # The back and shoulders receive a longer coat.
    if x<-.035 and z>.17: weight=min(1.,weight*.95)
    values.append(float(weight))
for i,weight in enumerate(values):
    group.add([i],weight,'REPLACE')
hair=bpy.data.materials.new("Run88 natural cream melanin-free down fibers")
hair.use_nodes=True
hair.diffuse_color=(.982,.938,.856,1.)
nt=hair.node_tree
nt.nodes.clear()
output=nt.nodes.new("ShaderNodeOutputMaterial")
try:
    shader=nt.nodes.new("ShaderNodeBsdfHairPrincipled")
    shader.parametrization='COLOR'
    shader.inputs['Color'].default_value=(.982,.925,.812,1)
    shader.inputs['Roughness'].default_value=.52
except Exception:
    shader=nt.nodes.new("ShaderNodeBsdfPrincipled")
    shader.inputs['Base Color'].default_value=(.982,.925,.812,1)
    shader.inputs['Roughness'].default_value=.9
nt.links.new(shader.outputs['BSDF'],output.inputs['Surface'])
body.data.materials.append(hair)
bpy.ops.object.select_all(action='DESELECT')
body.select_set(True)
bpy.context.view_layer.objects.active=body
bpy.ops.object.particle_system_add()
ps=body.particle_systems[-1]
ps.settings.type='HAIR'
ps.settings.count=5600
ps.settings.hair_length=.013
ps.settings.hair_step=5
ps.settings.use_advanced_hair=True
ps.settings.emit_from='FACE'
ps.settings.distribution='RAND'
ps.settings.child_type='INTERPOLATED'
ps.settings.child_nbr=8
ps.settings.rendered_child_count=10
ps.settings.clump_factor=.035
ps.settings.clump_shape=-.45
ps.settings.roughness_1=.005
ps.settings.roughness_2=.004
ps.settings.roughness_2_size=.028
ps.settings.kink='NO'
ps.settings.material=len(body.data.materials)
ps.vertex_group_density=group.name
# Render reliable 3D views, common scale and camera lighting for a fair
# paired raw-source versus hair comparison.
allverts=[o.matrix_world@v.co for o in meshes for v in o.data.vertices]
mn=Vector([min(q[i] for q in allverts) for i in range(3)])
mx=Vector([max(q[i] for q in allverts) for i in range(3)])
center=(mn+mx)/2
extent=max(mx-mn)
scene=bpy.context.scene
world=scene.world or bpy.data.worlds.new('Run88 softbox')
scene.world=world
world.use_nodes=True
world.node_tree.nodes['Background'].inputs['Color'].default_value=(.30,.32,.34,1)
world.node_tree.nodes['Background'].inputs['Strength'].default_value=.65
for ob in list(bpy.data.objects):
    if ob.type in {'CAMERA','LIGHT'}:
        bpy.data.objects.remove(ob,do_unlink=True)
for name,pos,power,size in [
    ('key',(1.,-1.4,1.3),230,2.2),
    ('fill',(1.0,1.4,1.0),180,1.8),
    ('rim',(-.75,.65,1.0),180,1.7)]:
    bpy.ops.object.light_add(type='AREA', location=pos)
    l=bpy.context.object
    l.name=name
    l.data.energy=power
    l.data.shape='DISK'
    l.data.size=size
    l.rotation_euler=(center-l.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add()
camera=bpy.context.object
scene.camera=camera
camera.data.type='ORTHO'
camera.data.ortho_scale=extent*1.60
scene.render.engine='CYCLES'
scene.cycles.samples=20
scene.cycles.use_denoising=True
scene.render.resolution_x=540
scene.render.resolution_y=540
scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.view_settings.view_transform='Standard'
scene.view_settings.exposure=-.3
views=[
    ('front',(2.0,0,.40)),
    ('threequarter',(1.65,-1.5,.43)),
    ('side',(0,-2.0,.37)),
    ('back',(-2,0,.37))
]
results=[]
for with_hair in [False,True]:
    # Particle renderer switch DOES NOT remove underlying original glTF mesh.
    for mod in body.modifiers:
        if mod.type=='PARTICLE_SYSTEM':
            mod.show_render=with_hair
            mod.show_viewport=with_hair
    for name,pos in views:
        camera.location=center+Vector(pos)
        camera.rotation_euler=(center-camera.location).to_track_quat('-Z','Y').to_euler()
        fn=f"run88_{'hair' if with_hair else 'base'}_{name}.png"
        scene.render.filepath=os.path.join(out,fn)
        bpy.ops.render.render(write_still=True)
        assert os.path.getsize(scene.render.filepath)>10000
        results.append(fn)
    print("ABLAT",with_hair,"RENDERED",len(results),flush=True)
# Save actual native .blend with all hair children and complete PBR scene.
for mod in body.modifiers:
    if mod.type=='PARTICLE_SYSTEM':
        mod.show_render=True
        mod.show_viewport=True
blend=os.path.join(out,'owl172_run88_true_cycles_fiber_groom_NOT_WEBGL_APPROVED.blend')
bpy.ops.wm.save_as_mainfile(filepath=blend)
assert os.path.getsize(blend)>200000
metrics={
'decision':'PENDING_INDEPENDENT_ART_QA_NOT_APPROVED',
'original_model':'Run87B adult horned owl CC0 retarget, wrong taxon/stage',
'current_technique':'Blender 4 native hair strand/path fibers with child hairs on genuine authored detailed body mesh',
'blender_version':bpy.app.version_string,'source_meshes':len(meshes),
'detailed_body_faces':len(body.data.polygons),'hair_parent_guides':ps.settings.count,
'hair_rendered_children_per_parent':ps.settings.rendered_child_count,
'hair_length_m':ps.settings.hair_length,'density_weight_min':min(values),
'density_weight_max':max(values),'albedo_materials_tinted':tinted,
'albedo_materials_skipped':skipped,'renders':results,
'blend_file_bytes':os.path.getsize(blend),
'blend_sha256':hashlib.sha256(open(blend,'rb').read()).hexdigest(),
'real_mobile_gpu_pass':False,'glb_hair_portable':False,
'visual_qa_pending':True,'no_251_species_changes':True,
'asset_source_license_claim':'Innerscene CC0 original, not independently audited',
'no_payment':True}
with open(os.path.join(out,'metrics.json'),'w') as f:
    json.dump(metrics,f,indent=2)
print('RUN88_NATIVE_HAIR_GROOM_NOT_MOBILE_CANDIDATE',json.dumps(metrics),flush=True)
