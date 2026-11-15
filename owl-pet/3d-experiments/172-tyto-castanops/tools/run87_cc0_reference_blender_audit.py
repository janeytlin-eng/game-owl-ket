"""Run87: inspect a verifiable third-party CC0 owl GLB as an anatomy/mesh BASE
for #172, never present as an approved juvenile. The source is an adult/general
owl and MUST NOT be represented as a Tyto castanops hatchling. It is only a
zero-payment asset transfer experiment. No edits to production assets.
"""
import bpy, bmesh, json, math, os, sys, hashlib, collections
from mathutils import Vector
from math import sin, cos, pi

src=sys.argv[sys.argv.index('--')+1]
out=sys.argv[sys.argv.index('--')+2]
os.makedirs(out,exist_ok=True)
assert open(src,'rb').read(4)==b'glTF','Source is not a genuine GLB'
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=src)
model=[o for o in bpy.context.scene.objects if o.type=='MESH']
assert model,'No 3D mesh objects in source'
raw_bounds=[o.matrix_world@Vector(q) for o in model for q in o.bound_box]
mins=[min(v[i] for v in raw_bounds) for i in range(3)]
maxs=[max(v[i] for v in raw_bounds) for i in range(3)]
center=Vector([(a+b)*.5 for a,b in zip(mins,maxs)])
extents=[b-a for a,b in zip(mins,maxs)]
diagonal=sum(v*v for v in extents)**.5
print('MODEL_SOURCE_REAL_GLTF',len(model),extents,diagonal)
objects=[]
tottri=0
for ob in model:
    me=ob.data
    me.calc_loop_triangles()
    tric=len(me.loop_triangles);tottri+=tric
    # topology belongs to mesh and not necessarily to union or visual model.
    bm=bmesh.new();bm.from_mesh(me)
    bd=sum(1 for e in bm.edges if e.is_boundary)
    nm=sum(1 for e in bm.edges if not e.is_manifold)
    bm.free()
    objects.append({'name':ob.name,'vertices':len(me.vertices),'triangles':tric,
                    'boundary_edges':bd,'nonmanifold_edges':nm,'material_count':len(me.materials)})
materials=[]
for m in bpy.data.materials:
    tex=[]
    if m.use_nodes:
        for n in m.node_tree.nodes:
            if n.type=='TEX_IMAGE' and n.image is not None:
                tex.append({'name':n.image.name,'size':list(n.image.size),'packed':bool(n.image.packed_file)})
    materials.append({'name':m.name,'uses_nodes':bool(m.use_nodes),'image_textures':tex,'blend_method':m.blend_method})
actions=[a.name for a in bpy.data.actions]
stats={'verdict':'SOURCE_ASSET_ANATOMY_AUDIT_ONLY_NOT_APP_APPROVED',
       'source_url':'https://www.innerscene.com/tools/library/3d-parts/owl-d696472a',
       'source_license_claim':'CC0 published on source page; keep provenance, do not infer taxon',
       'download_sha256':hashlib.sha256(open(src,'rb').read()).hexdigest(),
       'download_bytes':os.path.getsize(src),'blender_version':bpy.app.version_string,
       'objects':objects,'materials':materials,'actions':actions,
       'source_bounds':{'min':mins,'max':maxs,'extents':extents},
       'source_total_triangles':tottri,'actual_phone_test':False,
       'source_as_juvenile_approved':False}
with open(os.path.join(out,'source_mesh_audit.json'),'w') as f:json.dump(stats,f,indent=2)
# Renders of the *original unmodified imported asset*, to judge if its
# lateral/back silhouette is a better mesh foundation than Run86.
world=bpy.context.scene.world
if not world:
    world=bpy.data.worlds.new('Studio World');bpy.context.scene.world=world
world.use_nodes=True
world.node_tree.nodes.get('Background').inputs['Color'].default_value=(.28,.30,.33,1)
world.node_tree.nodes.get('Background').inputs['Strength'].default_value=.65
for o in list(bpy.data.objects):
    if o.type in {'LIGHT','CAMERA'}:bpy.data.objects.remove(o,do_unlink=True)
for name,angle,energy,size in [('key',-2.3,550,3),('fill',1.8,290,3.5),('rim',3.9,450,3)]:
    bpy.ops.object.light_add(type='AREA',location=(center.x+diagonal*cos(angle)*1.4,
        center.y+diagonal*sin(angle)*1.4, center.z+diagonal*1.7))
    o=bpy.context.object;o.name=name;o.data.energy=energy;o.data.shape='DISK';o.data.size=diagonal*1.7
    o.rotation_euler=(center-o.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add()
cam=bpy.context.object;cam.name='8-view unedited asset inspection';bpy.context.scene.camera=cam
cam.data.type='ORTHO';cam.data.ortho_scale=diagonal*1.36
sc=bpy.context.scene;sc.render.engine='CYCLES';sc.cycles.samples=12
bpy.context.view_layer.cycles.use_denoising=False
sc.render.resolution_x=540;sc.render.resolution_y=540;sc.render.resolution_percentage=100
sc.render.image_settings.file_format='PNG'
sc.view_settings.view_transform='Standard';sc.view_settings.exposure=-.2
for i in range(8):
    angle=2*pi*i/8
    cam.location=center+Vector((diagonal*1.75*sin(angle),-diagonal*1.75*cos(angle),diagonal*.27))
    cam.rotation_euler=(center-cam.location).to_track_quat('-Z','Y').to_euler()
    path=os.path.join(out,'source_view_%02d.png'%i)
    sc.render.filepath=path
    bpy.ops.render.render(write_still=True)
    print('ACTUAL_NATIVE_BLENDER_RENDER',i,os.path.getsize(path))
# A copy as GLB, proving the externally sourced 3D asset is usable by the
# Blender -> glTF 2.0 pipeline, but NO juvenile model has been created here.
dest=os.path.join(out,'owl172_run87_cc0_import_roundtrip_NOT_A_PET.glb')
bpy.ops.export_scene.gltf(filepath=dest,export_format='GLB',
                          export_cameras=False,export_lights=False)
assert open(dest,'rb').read(4)==b'glTF'
stats['reexport_bytes']=os.path.getsize(dest)
stats['reexport_sha256']=hashlib.sha256(open(dest,'rb').read()).hexdigest()
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=dest)
stats['roundtrip_mesh_count']=sum(o.type=='MESH' for o in bpy.data.objects)
assert stats['roundtrip_mesh_count']>0
with open(os.path.join(out,'source_mesh_audit.json'),'w') as f:json.dump(stats,f,indent=2)
print('RUN87_REAL_GLTF_REFERENCE_EXPLORATION_ONLY',json.dumps({k:stats[k] for k in ['download_bytes','source_total_triangles','roundtrip_mesh_count','reexport_bytes']}))
