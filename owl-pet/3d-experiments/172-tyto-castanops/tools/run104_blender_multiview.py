# Run104: native Blender Cycles rendering of actual independently created neural GLB.
# NOT a representation of verified side/back anatomy, nor approved character art.
import bpy,sys,math,os,json
from mathutils import Vector
args=sys.argv[sys.argv.index('--')+1:]
folder=args[0]
candidate=os.path.join(folder,'owl172_run104_neural_SINGLEVIEW_ART_UNREVIEWED.glb')
assert os.path.isfile(candidate),candidate
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=os.path.abspath(candidate))
meshes=[o for o in bpy.context.scene.objects if o.type=='MESH']
assert meshes,"No real mesh in GLB"
def bounds(obj):
    return [obj.matrix_world@Vector(c) for c in obj.bound_box]
vertices=[v for o in meshes for v in bounds(o)]
lo=Vector([min(v[i] for v in vertices) for i in range(3)])
hi=Vector([max(v[i] for v in vertices) for i in range(3)])
center=(lo+hi)*.5
radius=max((hi-lo))*1.5
if radius<=0:raise RuntimeError("Zero-size mesh")
w=bpy.data.worlds.new('neutral world') if not bpy.data.worlds else bpy.data.worlds[0]
bpy.context.scene.world=w;w.use_nodes=True
w.node_tree.nodes.get('Background').inputs['Color'].default_value=(.72,.77,.84,1)
w.node_tree.nodes.get('Background').inputs['Strength'].default_value=.6
def area(name,pos,power,size):
    bpy.ops.object.light_add(type='AREA',location=center+Vector(pos)*radius)
    l=bpy.context.object;l.name=name;l.data.energy=power;l.data.shape='DISK';l.data.size=size*radius
    direction=center-l.location;l.rotation_euler=direction.to_track_quat('-Z','Y').to_euler()
area('key',(2,-3,4),650,3.2)
area('fill',(-3,-2,2),450,3.5)
area('rim',(0,3,3),550,2.4)
bpy.ops.object.camera_add()
cam=bpy.context.object;bpy.context.scene.camera=cam;cam.data.type='ORTHO';cam.data.ortho_scale=radius*2.25
scene=bpy.context.scene;scene.render.engine='CYCLES'
scene.cycles.samples=18
scene.render.resolution_x=640;scene.render.resolution_y=640;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.render.film_transparent=False
# Four honest different camera directions; front orientation is an unverified hypothesis.
views={'front_assumed':(0,-2,0.35),'threequarter_assumed':(1.5,-1.4,0.4),
       'strict_side_assumed':(2,0,0.3),'back_assumed':(0,2,0.3)}
for name,vec in views.items():
    cam.location=center+Vector(vec).normalized()*radius*2.5
    direction=center-cam.location;cam.rotation_euler=direction.to_track_quat('-Z','Y').to_euler()
    scene.render.filepath=os.path.abspath(os.path.join(folder,f'run104_neural_{name}.png'))
    bpy.ops.render.render(write_still=True)
    assert os.path.getsize(scene.render.filepath)>5000
print('RUN92_REAL_CYCLES_FOUR_VIEW_COMPLETE_ART_UNREVIEWED',[(o.name,len(o.data.polygons)) for o in meshes])
