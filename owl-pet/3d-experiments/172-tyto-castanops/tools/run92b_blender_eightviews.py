import bpy,sys,os,math,json
from mathutils import Vector
folder=sys.argv[sys.argv.index('--')+1]
files=[('control','owl172_run92b_explicit_normal_control_ART_REJECTED.glb'),
       ('smooth','owl172_run92b_taubin12_smooth_explicit_normal_ART_REJECTED.glb')]
for variant,filename in files:
    bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
    path=os.path.abspath(os.path.join(folder,filename))
    assert os.path.isfile(path)
    bpy.ops.import_scene.gltf(filepath=path)
    geo=[o for o in bpy.context.scene.objects if o.type=='MESH']
    assert len(geo)>=1
    pts=[obj.matrix_world@Vector(c) for obj in geo for c in obj.bound_box]
    lo=Vector([min(v[i] for v in pts) for i in range(3)])
    hi=Vector([max(v[i] for v in pts) for i in range(3)])
    center=(lo+hi)*.5
    radius=max(hi-lo)
    assert radius>.05
    scene=bpy.context.scene
    world=bpy.data.worlds.new('world_'+variant)
    scene.world=world;world.use_nodes=True
    world.node_tree.nodes.get('Background').inputs['Color'].default_value=(.73,.77,.82,1)
    world.node_tree.nodes.get('Background').inputs['Strength'].default_value=.7
    for name,d,power in [
       ('soft_key',(3,-4,4),500),('soft_fill',(-4,-2,2),350),('back_rim',(0,3,3),350)]:
        bpy.ops.object.light_add(type='AREA',location=center+Vector(d)*radius)
        l=bpy.context.object;l.name=name;l.data.energy=power
        l.data.shape='DISK';l.data.size=3*radius
        l.rotation_euler=(center-l.location).to_track_quat('-Z','Y').to_euler()
    bpy.ops.object.camera_add();cam=bpy.context.object;scene.camera=cam
    cam.data.type='ORTHO';cam.data.ortho_scale=radius*2.15
    scene.render.engine='CYCLES';scene.cycles.samples=16
    # Explicitly avoid unsupported OpenImageDenoiser in Ubuntu Blender 4.0.2.
    scene.cycles.use_denoising=False
    for view_layer in scene.view_layers:
        view_layer.cycles.use_denoising=False
    scene.render.resolution_x=600;scene.render.resolution_y=600
    scene.render.resolution_percentage=100;scene.render.image_settings.file_format='PNG'
    # Front is a hypothesis for source TripoSR; scientific true orientation unverified.
    for name,vec in [
        ('front_assumed',(0,-2,.3)),
        ('threequarter_assumed',(1.4,-1.4,.35)),
        ('strict_side_assumed',(2,0,.3)),
        ('back_assumed',(0,2,.3))]:
        cam.location=center+Vector(vec).normalized()*radius*3.0
        cam.rotation_euler=(center-cam.location).to_track_quat('-Z','Y').to_euler()
        scene.render.filepath=os.path.abspath(os.path.join(folder,f'run92b_{variant}_{name}.png'))
        bpy.ops.render.render(write_still=True)
        assert os.path.isfile(scene.render.filepath) and os.path.getsize(scene.render.filepath)>10000
    print('REAL_BLENDER_CYCLES_4VIEW',variant,[(o.name,len(o.data.polygons)) for o in geo])
