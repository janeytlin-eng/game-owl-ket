"""Run92 locked-lights native Blender 4-way independent GLB import render.
Cycles screenshots are EVIDENCE not approval; no actual phone GPU.
"""
import bpy, os, sys, json, pathlib, hashlib
from mathutils import Vector
out=pathlib.Path(sys.argv[sys.argv.index('--')+1])
metrics=json.loads((out/'metrics.json').read_text())
assert len(metrics['variants'])==3
scene=bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=18
scene.cycles.use_denoising=False
bpy.context.view_layer.cycles.use_denoising=False
scene.render.resolution_x=440
scene.render.resolution_y=440
scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.view_settings.view_transform='Standard'
scene.view_settings.exposure=-.42
world=bpy.data.worlds.new('shared-photo-studio-world')
scene.world=world
world.use_nodes=True
world.node_tree.nodes['Background'].inputs['Color'].default_value=(.50,.54,.56,1)
world.node_tree.nodes['Background'].inputs['Strength'].default_value=.52
images=[]
for variant in metrics['variants']:
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    filename=out/variant['glb']
    assert hashlib.sha256(filename.read_bytes()).hexdigest()==variant['sha256']
    bpy.ops.import_scene.gltf(filepath=str(filename))
    objs=[o for o in bpy.data.objects if o.type=='MESH']
    assert len(objs)==variant['mesh_count'],(len(objs),variant['mesh_count'])
    tris=sum(len(o.data.polygons) for o in objs)
    assert tris==variant['triangle_count'],(tris,variant['triangle_count'])
    bounds=[o.matrix_world @ Vector(v) for o in objs for v in o.bound_box]
    mn=Vector([min(v[k] for v in bounds) for k in range(3)])
    mx=Vector([max(v[k] for v in bounds) for k in range(3)])
    mid=(mn+mx)/2
    extent=max(mx-mn)
    for name,diff,power,size in [
        ('key',Vector((-1.15,-1.5,1.75)),120,2.2),
        ('fill',Vector((1.5,-.60,.7)),70,2.0),
        ('rim',Vector((.40,1.65,1.65)),115,1.65)]:
        bpy.ops.object.light_add(type='AREA',location=mid+diff*extent)
        light=bpy.context.object;light.name=name
        light.data.energy=power
        light.data.shape='DISK';light.data.size=size*extent
        light.rotation_euler=(mid-light.location).to_track_quat('-Z','Y').to_euler()
    bpy.ops.object.camera_add()
    cam=bpy.context.object;scene.camera=cam
    cam.data.type='ORTHO';cam.data.ortho_scale=extent*1.65
    for view,d in [
       ('front',(0,-2.5,.16)),
       ('threequarter',(1.65,-1.9,.20)),
       ('strict_side',(2.5,0,.16)),
       ('back',(0,2.5,.16))]:
        cam.location=mid+Vector(d)*extent
        cam.rotation_euler=(mid-cam.location).to_track_quat('-Z','Y').to_euler()
        image_name='run92_'+variant['label']+'_'+view+'.png'
        scene.render.filepath=str(out/image_name)
        bpy.ops.render.render(write_still=True)
        assert (out/image_name).stat().st_size>10000
        images.append(image_name)
    print('RUN92_GENUINE_BLENDER_GLTF_VIEW',variant['label'],flush=True)
metrics['cycles_renders']=images
metrics['cycles_render_count']=len(images)
metrics['blender_version']=bpy.app.version_string
metrics['visual_verdict']='UNREVIEWED_NOT_APPROVED'
(out/'metrics.json').write_text(json.dumps(metrics,indent=2))
assert len(images)==12
