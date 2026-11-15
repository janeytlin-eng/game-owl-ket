#!/usr/bin/env python3
"""Run95: evaluate genuinely downloaded CC0 3D owl meshes in Blender.
A colour trial is a real GLB edit, NOT a suitable juvenile. All ART_REJECTED.
"""
import bpy, pathlib, sys, hashlib, json, math
from mathutils import Vector

OUT=pathlib.Path(sys.argv[sys.argv.index('--')+1]).resolve()
cfg=json.loads((OUT/'run95_candidates.json').read_text())
S=bpy.context.scene
S.render.engine='CYCLES';S.cycles.samples=16
S.cycles.use_denoising=False
bpy.context.view_layer.cycles.use_denoising=False
S.render.resolution_x=460; S.render.resolution_y=460
S.render.resolution_percentage=100
S.render.image_settings.file_format='PNG'
S.view_settings.view_transform='Standard';S.view_settings.exposure=-.4
S.world=bpy.data.worlds.new('Run95 neutral PBR check world')
S.world.use_nodes=True
S.world.node_tree.nodes['Background'].inputs['Color'].default_value=(.45,.47,.50,1)
S.world.node_tree.nodes['Background'].inputs['Strength'].default_value=.7

def clean():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
def meshes():
    return [o for o in S.objects if o.type=='MESH']
def count_tris():
    return sum(len(o.data.loop_triangles) for o in meshes())
def bounds():
    corners=[o.matrix_world@Vector(p) for o in meshes() for p in o.bound_box]
    return (Vector(tuple(min(p[i] for p in corners) for i in range(3))),
            Vector(tuple(max(p[i] for p in corners) for i in range(3))))
def scene_assets():
    lo,hi=bounds(); c=(lo+hi)/2; ext=max((hi-lo))
    L=[]
    for name,d,e,sz in [
       ('key',(-1.3,-1.4,1.7),210,1.7),
       ('fill',(1.7,-.4,1.1),100,2.1),
       ('rim',(.4,1.1,1.5),170,1.3)]:
        pos=c+Vector(d)*ext
        bpy.ops.object.light_add(type='AREA',location=pos)
        o=bpy.context.object;o.name='run95_'+name
        o.data.energy=e;o.data.size=sz*ext
        o.rotation_euler=(c-pos).to_track_quat('-Z','Y').to_euler()
        L.append(o)
    bpy.ops.object.camera_add()
    cam=bpy.context.object;S.camera=cam;cam.data.type='ORTHO'
    cam.data.ortho_scale=ext*1.6
    return c,ext,cam,L
def render(model,variant):
    c,ext,cam,ls=scene_assets()
    views=[('front',(0,-2.6,.18)),('threequarter',(1.7,-1.9,.18)),
           ('strict_side',(2.6,0,.18)),('rear',(0,2.6,.18))]
    images=[]
    for name,d in views:
        cam.location=c+Vector(d)*ext
        cam.rotation_euler=(c-cam.location).to_track_quat('-Z','Y').to_euler()
        filename=f'run95_{model}_{variant}_{name}.png'
        S.render.filepath=str(OUT/filename)
        bpy.ops.render.render(write_still=True)
        assert (OUT/filename).stat().st_size>5000
        images.append(filename)
    for obj in ls+[cam]:bpy.data.objects.remove(obj,do_unlink=True)
    return images
def cream_pbr():
    changed=0
    for ob in meshes():
        for i,mat in enumerate(ob.data.materials):
            if not mat:continue
            copy=mat.copy()
            copy.name='run95_EXPERIMENTAL_CREAM_RECOLOUR_NOT_APPROVED'
            copy.use_nodes=True
            nodes=copy.node_tree.nodes
            b=next((n for n in nodes if n.type=='BSDF_PRINCIPLED'),None)
            if not b:continue
            base=b.inputs.get('Base Color')
            if base:
                for link in list(base.links):copy.node_tree.links.remove(link)
                base.default_value=(.90,.84,.70,1)
            metallic=b.inputs.get('Metallic')
            rough=b.inputs.get('Roughness')
            if metallic:metallic.default_value=0.
            if rough:rough.default_value=.96
            ob.data.materials[i]=copy;changed+=1
    return changed

results=[]
for item in cfg.get('downloaded',[])[:2]:
    slug=str(item['slug']).replace('/','_').replace(' ','_')[:70]
    model=OUT/item['file']
    if hashlib.sha256(model.read_bytes()).hexdigest()!=item['sha256']:
        raise ValueError('upstream source bytes changed')
    record={'slug':slug,'source_file':model.name,'source_sha256':item['sha256'],
            'claimed_license':'CC0; provenance independently unverified',
            'is_a_verified_juvenile':False,'source_mesh_count':0,
            'source_triangles':0,'variants':[]}
    clean()
    bpy.ops.import_scene.gltf(filepath=str(model))
    if not meshes():raise RuntimeError('candidate is not real renderable mesh')
    for ob in meshes():ob.data.calc_loop_triangles()
    record['source_mesh_count']=len(meshes())
    record['source_triangles']=count_tris()
    record['bounds_m']=list(bounds()[1]-bounds()[0])
    record['variants'].append({
        'kind':'unaltered_3d_source','renders':render(slug,'original'),
        'art_approved':False})
    # This is a materials-only ablation on genuine source geometry.
    # Do not deform unrelated adult owl anatomy and call it a #172 chick.
    n=cream_pbr()
    if n:
        glb=OUT/f'owl172_run95_{slug}_cream_ONLY_REJECTED.glb'
        bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',
            export_normals=True,export_materials='EXPORT',
            export_cameras=False,export_lights=False,
            export_yup=True)
        exported=count_tris()
        clean();bpy.ops.import_scene.gltf(filepath=str(glb))
        for ob in meshes():ob.data.calc_loop_triangles()
        actual=count_tris()
        assert actual==exported,(actual,exported)
        record['variants'].append({
            'kind':'real_three_dimensional_material_retarget',
            'glb':glb.name,'bytes':glb.stat().st_size,
            'sha256':hashlib.sha256(glb.read_bytes()).hexdigest(),
            'reimport_triangles':actual,'round_trip':True,
            'changed_material_slots':n,
            'renders':render(slug,'cream'),
            'art_approved':False})
    else:record['material_retarget_blocker']='No editable principled PBR'
    results.append(record)
    print('RUN95_ACTUAL_REAL_MESH_FOUR_VIEW',slug,record['source_triangles'],flush=True)
(OUT/'run95_blender_metrics.json').write_text(json.dumps({
    'status':'ART_REJECTED','physical_mobile_GPU_tested':False,
    'render_engine':'Blender Cycles, native 3D, no image faking',
    'results':results},indent=2))
print('RUN95_FINISHED',len(results),flush=True)
