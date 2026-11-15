#!/usr/bin/env python3
"""Run93 no-extra-fee ACTUAL artist-mesh CC0-source intake/LOD audit.
Experimental adult/unverified owl reference, never a juvenile Tyto release.
Requires Blender 4.x. Does not touch production or any live deployment.
"""
import bpy, sys, pathlib, json, hashlib, math
from mathutils import Vector

out=pathlib.Path(sys.argv[sys.argv.index('--')+1]).resolve()
out.mkdir(exist_ok=True,parents=True)
source=out/'innerscene_owl_original_CC0_CLAIM_UNVERIFIED.glb'
assert source.is_file() and source.stat().st_size>1_000_000
assert source.read_bytes()[:4]==b'glTF'
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
S=bpy.context.scene
S.render.engine='CYCLES'
S.cycles.samples=14
S.cycles.use_denoising=False
bpy.context.view_layer.cycles.use_denoising=False
S.render.resolution_x=480
S.render.resolution_y=480
S.render.resolution_percentage=100
S.render.image_settings.file_format='PNG'
S.render.film_transparent=False
S.view_settings.view_transform='Standard'
S.view_settings.exposure=-0.28
world=bpy.data.worlds.new('run93-neutral-review-world')
world.use_nodes=True
world.node_tree.nodes['Background'].inputs['Color'].default_value=(0.44,.48,.52,1)
world.node_tree.nodes['Background'].inputs['Strength'].default_value=.6
S.world=world

def clear():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def meshes():
    return [o for o in bpy.context.scene.objects if o.type=='MESH']

def tri(o):
    o.data.calc_loop_triangles()
    return len(o.data.loop_triangles)

def stats(name):
    oo=meshes()
    assert oo
    return {'label':name,'mesh_count':len(oo),
        'triangle_count':sum(tri(o) for o in oo),
        'vertex_count':sum(len(o.data.vertices) for o in oo),
        'material_names':sorted(set(m.name for o in oo for m in o.data.materials if m)),
        'image_names':sorted(set(i.name for i in bpy.data.images if i.source=='FILE'))}

def bounds():
    pts=[o.matrix_world @ Vector(c) for o in meshes() for c in o.bound_box]
    mini=Vector(tuple(min(v[j] for v in pts) for j in range(3)))
    maxi=Vector(tuple(max(v[j] for v in pts) for j in range(3)))
    return mini,maxi

def lights_and_views(label):
    low,high=bounds()
    center=(low+high)*.5
    ext=max(high-low)
    assert ext>0
    lights=[]
    for name,direction,power,scale in (
        ('key',(-1.15,-1.45,1.75),250,2.2),
        ('fill',(1.4,-.55,.7),120,2.6),
        ('rim',(.4,1.3,1.2),190,1.8)):
        pos=center+Vector(direction)*ext
        bpy.ops.object.light_add(type='AREA',location=pos)
        l=bpy.context.object
        l.name='run93_'+name
        l.data.energy=power
        l.data.shape='DISK'
        l.data.size=scale*ext
        l.rotation_euler=(center-pos).to_track_quat('-Z','Y').to_euler()
        lights.append(l)
    bpy.ops.object.camera_add()
    cam=bpy.context.object
    S.camera=cam
    cam.data.type='ORTHO'
    cam.data.ortho_scale=ext*1.65
    files=[]
    for name,v in (
        ('negative_y',(0,-2.55,.18)),
        ('positive_x',(2.55,0,.18)),
        ('positive_y',(0,2.55,.18)),
        ('negative_x',(-2.55,0,.18))):
        cam.location=center+Vector(v)*ext
        cam.rotation_euler=(center-cam.location).to_track_quat('-Z','Y').to_euler()
        p=out/f'run93_{label}_{name}.png'
        S.render.filepath=str(p)
        bpy.ops.render.render(write_still=True)
        assert p.stat().st_size>10000,(p,p.stat().st_size)
        files.append(p.name)
    for o in lights+[cam]:
        bpy.data.objects.remove(o,do_unlink=True)
    return files

def import_glb(path):
    clear()
    bpy.ops.import_scene.gltf(filepath=str(path))
    assert meshes()

def export_glb(path):
    assert meshes()
    bpy.ops.export_scene.gltf(filepath=str(path),export_format='GLB',
       export_normals=True,export_materials='EXPORT',export_yup=True,
       export_apply=True)
    assert path.stat().st_size>200000
    assert path.read_bytes()[:4]==b'glTF'

def decimate(target):
    before=sum(tri(o) for o in meshes())
    ratio=min(1.,target/before)
    if ratio < .98:
        for o in meshes():
            n=tri(o)
            if n<200 or not o.data.vertices: continue
            mod=o.modifiers.new('run93_mobile_reference_LOD','DECIMATE')
            mod.ratio=max(.04,ratio)
            bpy.context.view_layer.objects.active=o
            bpy.ops.object.modifier_apply(modifier=mod.name)
    after=sum(tri(o) for o in meshes())
    return {'original_tris':before,'target_tris':target,'result_tris':after,
            'fraction':after/max(before,1)}

def retarget_juvenile_shape_trial():
    """Geometric test, NOT an anatomical sculpt. Head classification unknown."""
    lo,hi=bounds()
    h=max(.001,hi.z-lo.z)
    center=(lo+hi)/2
    moved=0
    for o in meshes():
        world=o.matrix_world.copy()
        inv=world.inverted_safe()
        for v in o.data.vertices:
            w=world @ v.co
            t=max(0.,min(1.,(w.z-lo.z)/h))
            s=t*t*(3-2*t)
            # CRUDE juvenile proportion hypothesis only; no reliable head segmentation
            w.x=center.x+(w.x-center.x)*(1+.19*s)
            w.y=center.y+(w.y-center.y)*(1+.17*s)
            w.z=lo.z+(w.z-lo.z)*(.82+.04*s)
            v.co=inv @ w
            moved+=1
        o.data.update()
    return {'deformed_vertices':moved,
        'method':'world-space tapered head broadening + vertical squash (controlled negative test)',
        'not_anatomy_validated':True}

sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
summary={'experiment':'run93 artist-authored original external owl intake, real four-azimuth Blender view, mobile LOD/juvenile ratio trial',
         'release':'ART_REJECTED','phone_GPU_tested':False,'model_identity':'unnamed owl, NOT confirmed Tyto castanops; adult vs juvenile unverified',
         'source_licensing':'Innerscene web page claims original CC0; not independently audited',
         'source_page':'https://www.innerscene.com/tools/library/3d-parts/owl-d696472a',
         'download_url':'https://www.innerscene.com/api/library/owl-d696472a/download',
         'original_sha256':sha(source),'original_bytes':source.stat().st_size,'variants':[]}
import_glb(source)
d=stats('unmodified_original_reference')
d['glb']=source.name
d['sha256']=sha(source)
d['bytes']=source.stat().st_size
d['renders']=lights_and_views('source')
d['approved']=False
summary['variants'].append(d)
print('RUN93_IMPORTED_SOURCE',d['triangle_count'],d['mesh_count'],flush=True)

lod=out/'owl172_run93_artist_owl_mobile_LOD_RESEARCH_ONLY.glb'
lodstat=decimate(65000)
export_glb(lod)
import_glb(lod) # REAL GLB round-trip proof
d=stats('mobile_LOD_reference')
d.update(lodstat)
d['glb']=lod.name;d['sha256']=sha(lod);d['bytes']=lod.stat().st_size
d['renders']=lights_and_views('lod')
d['approved']=False
summary['variants'].append(d)
print('RUN93_REAL_LOD_ROUNDTRIP',d['triangle_count'],flush=True)

ret=retarget_juvenile_shape_trial()
candidate=out/'owl172_run93_cc0_juvenile_ratio_negative_test.glb'
export_glb(candidate)
import_glb(candidate) # REAL GLB round-trip proof
d=stats('juvenile_ratio_shape_trial')
d.update(ret)
d['glb']=candidate.name;d['sha256']=sha(candidate);d['bytes']=candidate.stat().st_size
d['renders']=lights_and_views('juvenile_ratio')
d['approved']=False
summary['variants'].append(d)
print('RUN93_REAL_JUVENILE_SHAPE_TEST_ROUNDTRIP',d['triangle_count'],flush=True)
summary['blender_version']=bpy.app.version_string
summary['render_count']=sum(len(v['renders']) for v in summary['variants'])
assert summary['render_count']==12
(out/'run93_metrics.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
print('RUN93_REAL_GLBS_RENDERED_ART_NOT_APPROVED',flush=True)
