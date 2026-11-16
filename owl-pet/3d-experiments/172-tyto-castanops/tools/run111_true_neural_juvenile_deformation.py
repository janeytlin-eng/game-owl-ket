#!/usr/bin/env python3
"""Run111: anatomy-ratio deformation of a previously genuine neural owl mesh.
Research only. Warps ALL native input vertices and original fur/eyes coherently.
No 2D overlay, primitive body replacement, distribution approval or paid service.
"""
import argparse, bpy, hashlib, json, math, pathlib, sys
from mathutils import Matrix, Vector
from math import sin, cos, radians

ap=argparse.ArgumentParser()
ap.add_argument('--source',required=True)
ap.add_argument('--out',required=True)
a=ap.parse_args(sys.argv[sys.argv.index('--')+1:])
source=pathlib.Path(a.source); dest=pathlib.Path(a.out);dest.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
assert source.read_bytes()[:4]==b'glTF', 'Only genuine prior GLB permitted'
assert sha(source)=='604217f513c6e04f8f7d29ba17a418836a33fafe6d6e8fe3b5571b21da09a7c6'
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(source))
input_meshes=[o for o in bpy.context.scene.objects if o.type=='MESH']
assert len(input_meshes)>=7, len(input_meshes)
src_stats={ 'sha256':sha(source),'meshes':len(input_meshes),
 'triangles':sum(len(o.data.loop_triangles) for o in input_meshes)}
body=sorted(input_meshes,key=lambda o:len(o.data.polygons),reverse=True)[0]
body_coords=[body.matrix_world@v.co for v in body.data.vertices]
lo=Vector([min(p[i] for p in body_coords) for i in range(3)])
hi=Vector([max(p[i] for p in body_coords) for i in range(3)])
c=(lo+hi)*.5
d=hi-lo
assert all(x>.1 for x in d), tuple(d)
size=max(d)
scene=bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=20
scene.cycles.use_denoising=False
scene.render.resolution_x=440;scene.render.resolution_y=440
scene.render.resolution_percentage=100
scene.view_settings.view_transform='Standard'
scene.view_settings.look='Medium High Contrast'
scene.view_settings.exposure=-.2
scene.world.color=(.27,.27,.27)
for obj in list(bpy.data.objects):
    if obj.type=='LIGHT':bpy.data.objects.remove(obj,do_unlink=True)
def light(name,loc,power,scale):
    l=bpy.data.lights.new(name,'AREA');l.energy=power;l.shape='DISK';l.size=scale*size
    ob=bpy.data.objects.new(name,l);scene.collection.objects.link(ob)
    ob.location=c+Vector(loc)*size
    ob.rotation_euler=(c-ob.location).to_track_quat('-Z','Y').to_euler()
light('large_softbox_key',(-2.5,-3.0,2.8),340,4.3)
light('warm_rim',(2.1,2.5,2.3),210,3.4)
cam=bpy.data.objects.new('true_multiview_camera',bpy.data.cameras.new('true_multiview_camera'))
scene.collection.objects.link(cam);scene.camera=cam;cam.data.type='ORTHO'
base_mats=set()
for o in input_meshes:
    for m in o.data.materials:
        if m:base_mats.add(m.name)

def zmap(t):
    # Compress juvenile underbody without shortening head/facial disc:
    # continuous at both junctions. This is a genuine mesh deformation.
    if t<=.45:return .75*t
    if t<=.70:return .3375+1.20*(t-.45)
    return .6375+.96*(t-.70)

def deform(p, broad):
    t=(p.z-lo.z)/d.z
    crown=math.exp(-.5*((t-.775)/.155)**2)
    upper_chest=math.exp(-.5*((t-.52)/.20)**2)
    xr=(p.x-c.x)/max(d.x*.5,1e-8)
    x=c.x+(p.x-c.x)*(1.+broad*crown+0.06*upper_chest)
    # Scale elongated trunk profile toward squat juvenile; do not erase
    # the genuine folds, feet, or short wing topology.
    chest=math.exp(-.5*((t-.43)/.22)**2)
    y=c.y+(p.y-c.y)*(1.-.18*chest)
    # Subtle true front facial-volume relief (not an added flat decal).
    front=max(0.,min(1.,(c.y-p.y)/max(d.y*.4,1e-8)))
    cheek=math.exp(-.5*((t-.715)/.155)**2)*math.exp(-.5*((abs(xr)-.17)/.37)**2)
    y-=d.y*.021*front*cheek
    z=lo.z+d.z*zmap(t)
    return Vector((x,y,z))

def freeze_geometry(o,broad):
    raw=o.data;mat=o.matrix_world.copy()
    # Exporter-safe rebuilt topology; retain source faces and material indices.
    points=[tuple(deform(mat@v.co,broad)) for v in raw.vertices]
    polys=[tuple(f.vertices) for f in raw.polygons]
    new=bpy.data.meshes.new('reindexed_TRUE_input_'+o.name[:28])
    new.from_pydata(points,[],polys)
    new.update()
    for m in raw.materials:new.materials.append(m)
    for j,f in enumerate(new.polygons):
        f.material_index=raw.polygons[j].material_index
        f.use_smooth=raw.polygons[j].use_smooth
    o.parent=None
    o.matrix_world=Matrix.Identity(4)
    o.data=new
    bpy.context.view_layer.objects.active=o
    if raw.users==0:bpy.data.meshes.remove(raw)
    return len(points),len(polys)

variants=[]
for label,spread in [('juvenile_compact_20',.20),('juvenile_broadface_34',.34)]:
    # Reopen untouched prior GLB for each controlled ablation.
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=str(source))
    parts=[o for o in bpy.context.scene.objects if o.type=='MESH']
    assert len(parts)==len(input_meshes)
    counts=[freeze_geometry(o,spread) for o in parts]
    verts=sum(x for x,_ in counts); faces=sum(y for _,y in counts)
    assert faces>115000 and verts>75000,(label,verts,faces)
    bpy.context.view_layer.update()
    # A mesh export is not validated until freshly re-imported and counted.
    out=dest/('run111_'+label+'_ART_UNAPPROVED.glb')
    bpy.ops.object.select_all(action='DESELECT')
    for o in parts:o.select_set(True)
    bpy.context.view_layer.objects.active=parts[0]
    bpy.ops.export_scene.gltf(filepath=str(out),export_format='GLB',
        use_selection=True,export_materials='EXPORT')
    assert out.read_bytes()[:4]==b'glTF'
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.import_scene.gltf(filepath=str(out))
    newly=[o for o in bpy.context.scene.objects if o.type=='MESH' and o not in parts]
    r_faces=sum(len(o.data.polygons) for o in newly)
    assert r_faces>=faces*.995,(faces,r_faces)
    for o in newly:bpy.data.objects.remove(o,do_unlink=True)
    # Object-relative four camera views of the actual mutated 3D surface.
    bound=[o.matrix_world@v.co for o in parts for v in o.data.vertices if o.name==body.name]
    # Imported body may have generic name, so use biggest mesh after reimport.
    largest=max(parts,key=lambda o:len(o.data.polygons))
    pts=[largest.matrix_world@v.co for v in largest.data.vertices]
    low=Vector([min(p[i] for p in pts) for i in range(3)])
    high=Vector([max(p[i] for p in pts) for i in range(3)])
    cc=(low+high)*.5; s=max(high-low)
    cam.data.ortho_scale=s*1.52
    for name,angle in [('front',0),('quarter',45),('side',90),('back',180)]:
        th=radians(angle)
        cam.location=cc+Vector((4*sin(th),-4*cos(th),1.32))*s
        cam.rotation_euler=(cc-cam.location).to_track_quat('-Z','Y').to_euler()
        scene.render.filepath=str(dest/('run111_'+label+'_'+name+'_cycles_UNAPPROVED.png'))
        bpy.ops.render.render(write_still=True)
    variants.append({'variant':label,'width_spread':spread,'vertices':verts,
        'polygons':faces,'reimport_meshes':len(newly),
        'reimport_polygons':r_faces,'bytes':out.stat().st_size,'sha256':sha(out),
        'body_bounds_before':list(d),'body_bounds_after':list(high-low),
        'views':4})
    for o in parts:bpy.data.objects.remove(o,do_unlink=True)
report={'source':src_stats,'blender':bpy.app.version_string,
        'method':'continuous nonrigid deformation of real neural mesh, all attached face-eye-fiber topology preserved',
        'research_only':True,'art_status':'ART_UNAPPROVED_REQUIRES_INDEPENDENT_VISUAL_REVIEW',
        'source_license_global_clearance':False,'real_phone_gpu_tested':False,
        'variants':variants}
(dest/'run111_true_mesh_metrics.json').write_text(json.dumps(report,indent=2))
print('RUN111_TRUE_NATIVE_GEOMETRY',json.dumps(report),flush=True)
