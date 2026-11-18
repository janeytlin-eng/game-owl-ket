#!/usr/bin/env python3
"""Run155: genuine, roundtrip-loaded GLB 4-azimuth native render if NEW public model exists.
Not orientation-calibrated. These four image files never imply art acceptance or phone WebGL.
"""
import os, json, math, hashlib, pathlib
import bpy
from mathutils import Vector
OUT=pathlib.Path('owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run155-MESHY-CC0-JUVENILE-NO_RELEASE')
candidates=sorted(OUT.glob('*_genuine_3d_SOURCE_UNAPPROVED.glb'))
if not candidates:
    raise SystemExit('RUN155: no authentic newly-downloaded GLB; do not invent renders')
f=candidates[0]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(f.resolve()))
meshes=[o for o in bpy.context.scene.objects if o.type=='MESH']
assert meshes,'No MESH after true GLB reimport'
verts=[m.matrix_world@Vector(corner) for m in meshes for corner in m.bound_box]
low=Vector([min(v[i] for v in verts) for i in range(3)])
high=Vector([max(v[i] for v in verts) for i in range(3)])
center=(low+high)*0.5
radius=max((high-low))*1.3
scene=bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=12
scene.cycles.use_denoising=False
scene.render.resolution_x=480;scene.render.resolution_y=480
scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.world.color=(.72,.72,.72)
def point(o):
    o.rotation_euler=(center-o.location).to_track_quat('-Z','Y').to_euler()
for delta,power,size in [((2,-3,4),650,5),((-4,2,3),450,5)]:
    bpy.ops.object.light_add(type='AREA',location=center+Vector(delta)*radius)
    l=bpy.context.object;l.data.energy=power;l.data.size=radius*size;point(l)
bpy.ops.object.camera_add()
cam=bpy.context.object
cam.data.type='ORTHO';cam.data.ortho_scale=radius*2.4
scene.camera=cam
frames=[]
for degrees in [0,45,90,180]:
    rad=math.radians(degrees)
    cam.location=center+Vector((math.sin(rad)*radius*2.5,-math.cos(rad)*radius*2.5,radius*.40))
    point(cam)
    path=OUT/f'run155_true_glb_orbit_{degrees:03d}_NO_RELEASE.png'
    scene.render.filepath=str(path.resolve())
    bpy.ops.render.render(write_still=True)
    assert path.stat().st_size>1000
    frames.append({'angle_deg_unoriented':degrees,'path':path.name,
                  'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
triangles=sum(sum(len(poly.vertices)-2 for poly in ob.data.polygons) for ob in meshes)
(OUT/'run155_native_glb_reimport_render.json').write_text(json.dumps({
    'source':f.name,'mesh_objects':len(meshes),'triangles':triangles,
    'bounds':[list(low),list(high)],'true_blender_render':True,
    'anatomical_orientation_verified':False,'visual_review':'PENDING',
    'mobile_webgl_verified':False,'art_release':False,'frames':frames
},indent=2))
print('RUN155_NATIVE_REAL_ORBITS_NO_RELEASE',len(frames))
