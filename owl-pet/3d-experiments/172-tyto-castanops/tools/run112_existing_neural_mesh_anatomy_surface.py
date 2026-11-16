#!/usr/bin/env python3
"""Run112. Controlled anatomical and posterior microrelief ablation on a REAL
existing neural 3D owl. Never publish: previously failed facial-disc, down,
short-wing, feet-support and global rights gates still apply. No proxy sphere.
"""
import argparse, bpy, hashlib, json, math, pathlib, sys
from collections import defaultdict
from mathutils import Vector, Matrix
from math import radians, sin, cos

p = argparse.ArgumentParser()
p.add_argument('--source', required=True)
p.add_argument('--out', required=True)
args = p.parse_args(sys.argv[sys.argv.index('--')+1:])
source=pathlib.Path(args.source)
dest=pathlib.Path(args.out); dest.mkdir(parents=True,exist_ok=True)
def sha(path): return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
EXPECTED='c755adfdea0d54e8de5588d72593009162d799ec2a97dec2026cc1efe613a886'
assert source.read_bytes()[:4]==b'glTF'
assert sha(source)==EXPECTED, "source content changed, refuse experiment"
def smoothstep(a,b,x):
    t=max(0.0,min(1.0,(x-a)/(b-a)))
    return t*t*(3.0-2.0*t)

bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene
scene.render.engine='CYCLES';scene.cycles.samples=18
scene.cycles.use_denoising=False
scene.render.resolution_x=440;scene.render.resolution_y=440
scene.render.resolution_percentage=100
scene.view_settings.view_transform='Standard'
scene.view_settings.look='Medium High Contrast'
scene.view_settings.exposure=-0.08
scene.world.color=(0.31,0.31,0.31)
def area(name,vec,power,scale):
    l=bpy.data.lights.new(name,'AREA');l.energy=power;l.shape='DISK';l.size=scale
    ob=bpy.data.objects.new(name,l);scene.collection.objects.link(ob)
    ob.location=Vector(vec);return ob
lights=[area('genuine_mesh_soft_key',(-3,-4,3),380,5),
        area('genuine_mesh_fill',(3,2,4),260,4)]
cam=bpy.data.objects.new('actual_3d_orbit_camera',bpy.data.cameras.new('actual_3d_orbit_camera'))
scene.collection.objects.link(cam);scene.camera=cam;cam.data.type='ORTHO'
def bbox(ob):
    pts=[ob.matrix_world@v.co for v in ob.data.vertices]
    lo=Vector([min(q[i] for q in pts) for i in range(3)])
    hi=Vector([max(q[i] for q in pts) for i in range(3)])
    return lo,hi

def build_anatomy(p, lo, hi, rear_amount, face_amount):
    c=(lo+hi)*.5;d=hi-lo
    t=(p.z-lo.z)/d.z
    # Lower body and feet stay untouched. The front face and orbit share a
    # continuous deformation with the native mesh rather than separate decals.
    fy=(c.y-p.y)/d.y
    fw=smoothstep(0.02,0.26,fy)
    fw*=math.exp(-0.5*((t-.71)/.205)**2)
    fw*=math.exp(-0.5*(((p.x-c.x)/d.x)/.43)**2)
    x=c.x+(p.x-c.x)*(1.+face_amount*fw)
    z=p.z+(t-.71)*d.z*(face_amount*.64*fw)
    # Backwards wedge is a major Run111 failure: compress ONLY rear half
    # of original 3D silhouette (never collapse the open frontal mask).
    rw=smoothstep(.23,.40,t)*(1.-.25*smoothstep(.84,1.0,t))
    rear=max(0.,p.y-c.y)
    y=p.y-rear*rear_amount*rw
    return Vector((x,y,z)), fw, rw

def clean_rebuild(o, mutate):
    raw=o.data; transform=o.matrix_world.copy()
    coordinates=[]
    changed=0
    fw_sum=0.
    for vertex in raw.vertices:
        pt=transform@vertex.co
        pt2,fw,rw=mutate(pt)
        coordinates.append(tuple(pt2))
        if (pt2-pt).length>1.e-6:changed+=1
        fw_sum+=fw
    polys=[tuple(poly.vertices) for poly in raw.polygons]
    nm=bpy.data.meshes.new('Run112_real_neural_topology_'+o.name[:30])
    nm.from_pydata(coordinates,[],polys)
    nm.update()
    for mat in raw.materials: nm.materials.append(mat)
    for i,face in enumerate(nm.polygons):
        face.material_index=raw.polygons[i].material_index
        face.use_smooth=raw.polygons[i].use_smooth
    o.parent=None
    o.matrix_world=Matrix.Identity(4)
    o.data=nm
    if raw.users==0: bpy.data.meshes.remove(raw)
    return changed,fw_sum

variants=[]
for name, back_compress, face_expansion, smooth_factor, iterations in [
   ('balanced_28', .28,.22,.34,5),
   ('strong_44', .44,.35,.48,11)]:
    for o in list(scene.objects):
        if o.type in {'MESH','EMPTY'}:bpy.data.objects.remove(o,do_unlink=True)
    bpy.ops.import_scene.gltf(filepath=str(source))
    parts=[o for o in scene.objects if o.type=='MESH']
    assert len(parts)==8, ('expected 8 real model mesh pieces',len(parts))
    main=max(parts,key=lambda o:len(o.data.polygons))
    lo,hi=bbox(main);center=(lo+hi)*.5; dims=hi-lo
    assert all(v>.1 for v in dims)
    original_poly_count=sum(len(o.data.polygons) for o in parts)
    assert original_poly_count==127262, original_poly_count
    moved=0
    for ob in parts:
        m,_=clean_rebuild(ob,lambda pt:build_anatomy(pt,lo,hi,back_compress,face_expansion))
        moved+=m

    # Restrict topology-preserving Laplacian smoothing to the posterior
    # existing neural surface, avoiding eyes, beak, frontal face and feet.
    grp=main.vertex_groups.new(name='posterior_original_mesh_only')
    buckets=defaultdict(list)
    for v in main.data.vertices:
        pt=v.co
        t=(pt.z-lo.z)/dims.z
        posterior=(pt.y-center.y)/dims.y
        weight=smoothstep(.03,.22,posterior)*smoothstep(.25,.43,t)
        if weight>.025: buckets[min(20,max(1,int(weight*20)))].append(v.index)
    for b,ids in buckets.items():
        grp.add(ids,b/20.,'REPLACE')
    weighted=sum(map(len,buckets.values()))
    assert weighted>1500,('posterior mask unexpectedly empty',weighted)
    bpy.ops.object.select_all(action='DESELECT')
    main.select_set(True);bpy.context.view_layer.objects.active=main
    mod=main.modifiers.new('Run112_posterior_native_microrelief_reduction','SMOOTH')
    mod.factor=smooth_factor
    mod.iterations=iterations
    mod.vertex_group=grp.name
    bpy.ops.object.modifier_apply(modifier=mod.name)
    # Normalize Blender imported glTF custom-data and exporter state.
    old=main.data
    clean=bpy.data.meshes.new('clean_post_smoothing_REAL_neural_model')
    clean.from_pydata([tuple(v.co) for v in old.vertices],[],
                      [tuple(face.vertices) for face in old.polygons])
    clean.update()
    for mat in old.materials:clean.materials.append(mat)
    for i,f in enumerate(clean.polygons):
        f.material_index=old.polygons[i].material_index
        f.use_smooth=True
    main.data=clean
    if old.users==0:bpy.data.meshes.remove(old)
    polys=sum(len(o.data.polygons) for o in parts)
    assert polys==127262, ('not topology-preserving',polys)
    bpy.context.view_layer.update()
    lo2,hi2=bbox(main)
    out=dest/('run112_'+name+'_real_neural_sculpt_ART_UNAPPROVED.glb')
    bpy.ops.object.select_all(action='DESELECT')
    for ob in parts:ob.select_set(True)
    bpy.context.view_layer.objects.active=main
    main.data.validate(clean_customdata=True)
    bpy.ops.export_scene.gltf(filepath=str(out),export_format='GLB',
        use_selection=True, export_materials='EXPORT')
    assert out.read_bytes()[:4]==b'glTF', 'not an actual glTF binary'
    # No quality assertion from file size; insist on topology through fresh import.
    before=set(scene.objects)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.import_scene.gltf(filepath=str(out))
    fresh=[ob for ob in scene.objects if ob not in before and ob.type=='MESH']
    reimport_faces=sum(len(ob.data.polygons) for ob in fresh)
    assert reimport_faces==polys, ('lost real mesh on glTF export',reimport_faces,polys)
    for ob in fresh:bpy.data.objects.remove(ob,do_unlink=True)
    center2=(lo2+hi2)*.5
    size=max(hi2-lo2)
    cam.data.ortho_scale=size*1.53
    for lamp in lights:
        lamp.location=center2+Vector((-2.7,-3,2.9) if lamp==lights[0] else (2.3,2.5,3.1))*size
        lamp.rotation_euler=(center2-lamp.location).to_track_quat('-Z','Y').to_euler()
        lamp.data.size=size*(4.4 if lamp==lights[0] else 3.5)
    for view,deg in [('front',0),('quarter',45),('side',90),('back',180)]:
        theta=radians(deg)
        cam.location=center2+Vector((4*sin(theta),-4*cos(theta),1.32))*size
        cam.rotation_euler=(center2-cam.location).to_track_quat('-Z','Y').to_euler()
        scene.render.filepath=str(dest/('run112_'+name+'_'+view+'_REAL_CYCLES_UNAPPROVED.png'))
        bpy.ops.render.render(write_still=True)
    variants.append({'name':name,'back_compress':back_compress,
      'face_expansion':face_expansion,'posterior_smooth_factor':smooth_factor,
      'posterior_smooth_iterations':iterations,'weighted_posterior_vertices':weighted,
      'moved_original_mesh_vertices':moved,'source_triangles':original_poly_count,
      'reimported_real_triangles':reimport_faces,'reimported_meshes':len(fresh),
      'bounds_main_before':list(dims),'bounds_main_after':list(hi2-lo2),
      'file_bytes':out.stat().st_size,'file_sha256':sha(out),
      'native_cycles_views':4})
    for ob in parts:bpy.data.objects.remove(ob,do_unlink=True)
report={'experiment':'Run112 actual existing 3D neural anatomy + posterior microrelief ablation',
    'tool':'Blender '+bpy.app.version_string,
    'source_sha256':sha(source),'source_art_approved':False,
    'source_global_rights_cleared':False,'actual_phone_gpu_tested':False,
    'method':'continuous transformations of native neural surface and weighted posterior smoothing, not primitive replacement',
    'automatic_art_acceptance':False,
    'variants':variants}
(dest/'run112_actual_geometry_metrics.json').write_text(json.dumps(report,indent=2))
print('RUN112_ACTUAL_REAL_3D',json.dumps(report),flush=True)
