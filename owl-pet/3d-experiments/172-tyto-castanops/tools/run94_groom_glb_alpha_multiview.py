#!/usr/bin/env python3
"""Run94: proper alpha/PBR check + real 3D GroomLab-card shrink/registration ablation.
Inputs: Run93 genuine GroomLab hair-card GLB and Run92C rejected anatomical GLB.
Neither source nor output is approved; zero production or deployment mutation.
"""
import bpy, sys, math, json, hashlib, pathlib, collections
from mathutils import Vector
from mathutils.bvhtree import BVHTree

OUT=pathlib.Path(sys.argv[sys.argv.index('--')+1]).resolve()
OUT.mkdir(parents=True,exist_ok=True)
BASE=OUT/'baseline_run92C_REJECTED.glb'
HAIR=OUT/'run93_groomlab_export_REJECTED.glb'
assert BASE.is_file() and HAIR.is_file(), (BASE,HAIR)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(BASE)=='6bc98227580d178e5750c6abd8903c31d956172b6afeacf20257dabf661d2d53'
assert sha(HAIR)=='b1aa292c614ad93a819e1985005634433bf24beb02012398aa8f06f922442be6'
S=bpy.context.scene
S.render.engine='CYCLES';S.cycles.samples=20
S.render.resolution_x=420; S.render.resolution_y=420
S.render.resolution_percentage=100;S.render.image_settings.file_format='PNG'
S.render.film_transparent=False
S.view_settings.view_transform='Standard';S.view_settings.exposure=-.35
W=bpy.data.worlds.new('RUN94_KNOWN_LIGHT')
W.use_nodes=True
W.node_tree.nodes['Background'].inputs['Color'].default_value=(.51,.52,.54,1)
W.node_tree.nodes['Background'].inputs['Strength'].default_value=.65
S.world=W
def clear():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
def objs():
    return [o for o in bpy.context.scene.objects if o.type=='MESH']
def tris():
    return sum(len(o.data.polygons) for o in objs())
def worldbounds():
    pts=[o.matrix_world @ Vector(c) for o in objs() for c in o.bound_box]
    low=Vector([min(v[k] for v in pts) for k in range(3)])
    hi=Vector([max(v[k] for v in pts) for k in range(3)])
    return low,hi
def read_scene():
    clear()
    bpy.ops.import_scene.gltf(filepath=str(BASE))
    before=tris()
    removed=[]
    for o in list(objs()):
        if 'soft_alpha_mesoptile_research_groom' in o.name:
            removed.append(o.name);bpy.data.objects.remove(o,do_unlink=True)
    assert removed, [o.name for o in objs()]
    names=[o.name for o in objs()]
    body=next(o for o in objs() if 'ORGANIC_CONNECTED_HEAD_BODY_HEART_RELIEF' in o.name)
    assert len(body.data.polygons)>10000
    # GroomLab cards as glTF texture: preserve alpha-mask, normal maps and PBR.
    base_names=set(o.name for o in objs())
    bpy.ops.import_scene.gltf(filepath=str(HAIR))
    new=[o for o in objs() if o.name not in base_names]
    assert len(new)==1,(len(new),[o.name for o in objs()])
    o=new[0];o.name='Run94_GroomLab_real_3D_cards_PROVISIONAL'
    assert len(o.data.polygons)>200
    mat=o.active_material
    assert mat and mat.use_nodes, 'groom cards PBR did not survive glTF import'
    return body,o,removed,before

def components(o):
    # Every actual connected hair card is separately editable triangle geometry.
    # Partition from mesh edge adjacency rather than guessing a strand count.
    nv=len(o.data.vertices)
    parent=list(range(nv))
    def find(i):
        while parent[i]!=i: parent[i]=parent[parent[i]];i=parent[i]
        return i
    for edge in o.data.edges:
        a,b=edge.vertices
        aa,bb=find(a),find(b)
        if aa!=bb:parent[bb]=aa
    by=collections.defaultdict(list)
    for i in range(nv):by[find(i)].append(i)
    return list(by.values())

def calibrate(body,card,scale):
    # Work in imported Blender world coordinates; both GLBs Y-up converted to Z-up.
    coords=[body.matrix_world @ v.co for v in body.data.vertices]
    faces=[[int(i) for i in p.vertices] for p in body.data.polygons]
    bvh=BVHTree.FromPolygons(coords,faces,all_triangles=True)
    groups=components(card)
    original_lengths=[];new_lengths=[];distances=[];facial_clipped=0
    M=card.matrix_world.copy();INV=M.inverted_safe()
    for group in groups:
        pts=[M @ card.data.vertices[i].co for i in group]
        cent=sum(pts,Vector((0,0,0)))/len(pts)
        nearest,normal,idx,dist=bvh.find_nearest(cent)
        assert nearest is not None
        # Face is the -Y side of Run92C sculpt after Blender import; keep eye/disc legible.
        protect=(cent.y<-.17 and cent.z>.71 and abs(cent.x)<.34)
        actual_scale=.018 if protect else scale
        if protect: facial_clipped+=1
        length=max((p-cent).length for p in pts)
        for i,p in zip(group,pts):
            target=nearest+normal*.007+(p-cent)*actual_scale
            card.data.vertices[i].co=INV@target
        original_lengths.append(length)
        new_lengths.append(length*actual_scale)
        distances.append(dist)
    card.data.update()
    return {'component_count':len(groups),'vertices':len(card.data.vertices),
            'card_faces':len(card.data.polygons),'scale':scale,
            'facial_cards_minimized':facial_clipped,
            'original_radius_max':max(original_lengths),
            'new_radius_max':max(new_lengths),
            'distance_to_surface_median':sorted(distances)[len(distances)//2],
            'genuine_mesh_repositioned':True}

def render(label):
    lo,hi=worldbounds();mid=(lo+hi)*.5;ext=max(hi-lo)
    created=[]
    for nm,direction,energy,width in [
        ('key',(-1.1,-1.5,1.7),170,2.0),('fill',(1.4,-.6,.9),90,2.4),
        ('rim',(.4,1.4,1.7),145,1.6)]:
        pos=mid+Vector(direction)*ext
        bpy.ops.object.light_add(type='AREA',location=pos)
        l=bpy.context.object;l.data.energy=energy;l.data.shape='DISK';l.data.size=width*ext
        l.rotation_euler=(mid-pos).to_track_quat('-Z','Y').to_euler()
        created.append(l)
    bpy.ops.object.camera_add();cam=bpy.context.object;S.camera=cam
    cam.data.type='ORTHO';cam.data.ortho_scale=ext*1.7
    views=[('front',(0,-2.55,.15)),('threequarter',(1.75,-1.85,.18)),
           ('side',(2.55,0,.15)),('rear',(0,2.55,.15))]
    outputs=[]
    for nm,dir in views:
        cam.location=mid+Vector(dir)*ext
        cam.rotation_euler=(mid-cam.location).to_track_quat('-Z','Y').to_euler()
        fname='run94_'+label+'_'+nm+'.png'
        S.render.filepath=str(OUT/fname)
        bpy.ops.render.render(write_still=True)
        assert (OUT/fname).stat().st_size>12000
        outputs.append(fname)
    for o in created+[cam]: bpy.data.objects.remove(o,do_unlink=True)
    return outputs
result={'name':'Run94 genuine GroomLab glTF alpha-mask and calibrated short down PBR',
        'status':'ART_REJECTED','accepted':False,'physical_phone_GPU_tested':False,
        'native_GLTF_PBR':True,'original_reference_side_back_verified':False,
        'source':{'base_hash':sha(BASE),'hair_hash':sha(HAIR)},
        'variants':[]}
for label,scale in [('raw_cards_alpha',None),('short_cards_0p22',.22),
                     ('micro_cards_0p08',.08)]:
    body,o,removed,original=read_scene()
    before={'source_tris':original,'removed_existing_bad_down':removed,
            'groom_triangle_count':len(o.data.polygons),
            'alpha_mode':o.active_material.blend_method if hasattr(o.active_material,'blend_method') else 'Blender4 material',
            'card_material':o.active_material.name,
            'material_uses_nodes':bool(o.active_material.use_nodes)}
    if scale is not None:
        before['calibration']=calibrate(body,o,scale)
    glb=OUT/('owl172_run94_'+label+'_UNAPPROVED.glb')
    bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',
        export_normals=True,export_materials='EXPORT',export_yup=True,
        export_apply=True)
    assert glb.is_file() and glb.stat().st_size>100000
    # Enforce true GLB round trip with native Blender; do not trust a file name.
    exported_tris=tris()
    bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=str(glb))
    assert abs(tris()-exported_tris)<20,(tris(),exported_tris)
    before.update({'label':label,'bytes':glb.stat().st_size,'sha256':sha(glb),
                   'real_glb_roundtrip':True,'triangles':tris(),
                   'renders':render(label),'approved':False})
    result['variants'].append(before)
    print('RUN94_REAL_GLTF_ALPHA_RENDERED',label,before['bytes'],before['sha256'],flush=True)
assert len(result['variants'])==3 and sum(len(v['renders']) for v in result['variants'])==12
(OUT/'run94_metrics.json').write_text(json.dumps(result,indent=2,ensure_ascii=False))
(OUT/'ART_REJECTED_DO_NOT_PUBLISH.txt').write_text(
    'This is real imported GroomLab feather geometry and Blender glTF PBR render.\n'
    'No artistic approval. No real mobile GPU, rig or animation validation.\n'
    'Never publish as a usable #172 juvenile owl or alter species production.\n')
