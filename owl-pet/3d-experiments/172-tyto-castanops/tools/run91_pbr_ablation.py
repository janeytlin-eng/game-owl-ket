#!/usr/bin/env python3
"""Run91 negative-control PBR/normal WebGL diagnostic for #172.
Generates real, roundtrippable GLBs, NOT an art-approved or shippable pet.
This investigates Run90's false positive: geometry draws but looks black.
All edits and binaries remain isolated on research branch.
"""
import argparse, hashlib, importlib.util, json, math, struct
from pathlib import Path
import numpy as np
import trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals
from trimesh.exchange.gltf import export_glb

P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('sculpt',P/'mesoptile_organic_sculpt_trial_v31.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
parser=argparse.ArgumentParser()
parser.add_argument('output',type=Path)
parser.add_argument('--resolution',type=int,default=108)
args=parser.parse_args()
out=args.output;out.mkdir(parents=True,exist_ok=True)
bodyname='ORGANIC_CONNECTED_HEAD_BODY_HEART_RELIEF'
scene,stats=mod.make_scene(res=args.resolution,n_down=1200)
body=scene.geometry[bodyname]
assert body.is_watertight and body.volume>0,('bad body volume',body.volume)
assert body.is_winding_consistent
assert body.visual.kind=='vertex'
source_color=np.array(body.visual.vertex_colors)
source_triangles=sum(len(g.faces) for g in scene.geometry.values())
report={'research_only':True,'release_approved':False,
 'hypothesis':'Run90 Three.js 0-error smoke may be black due to COLOR_0 vs normals/PBR material; compare fixed geometry.',
 'source':'repository v31 continuous organic signed distance sculpt',
 'source_body_triangles':len(body.faces),
 'body_volume_positive':bool(body.volume>0),
 'body_watertight':bool(body.is_watertight),
 'same_mesh_geometry_all_variants':True,
 'variants':[]}

def gltf_json(glb_bytes):
    assert glb_bytes[:4]==b'glTF'
    jslen=struct.unpack_from('<I',glb_bytes,12)[0]
    return json.loads(glb_bytes[20:20+jslen])

for label,explicit_normals,flat_material in [
    ('source_vertex_colors_implicit_normals',False,False),
    ('source_vertex_colors_explicit_normals',True,False),
    ('flat_cream_pbr_explicit_normals',True,True)]:
    sc=scene.copy()
    obj=sc.geometry[bodyname]
    if flat_material:
        # This is a shading-path diagnostic, NOT a feasible final bird:
        # it deliberately erases the elaborate concept disc colour.
        obj.visual=TextureVisuals(material=PBRMaterial(
            name='RUN91_DIAGNOSTIC_CREAM_NO_COLOR_0',
            baseColorFactor=[244,226,200,255],metallicFactor=0.,
            roughnessFactor=.9,doubleSided=False))
    else:
        assert np.array_equal(obj.visual.vertex_colors,source_color)
    sc.apply_transform(trimesh.transformations.rotation_matrix(-math.pi/2,[1,0,0]))
    data=export_glb(sc,include_normals=explicit_normals,unitize_normals=True)
    file=out/f'owl172_run91_{label}_ART_REJECTED.glb'
    file.write_bytes(data)
    again=trimesh.load(file,force='scene',process=False)
    tris=sum(len(m.faces) for m in again.geometry.values())
    assert tris==source_triangles
    gdoc=gltf_json(data)
    entries=[(m,pr) for m in gdoc['meshes'] for pr in m['primitives'] if m.get('name')==bodyname]
    assert entries,[(x.get('name')) for x in gdoc['meshes']]
    body_attrib=entries[0][1]['attributes']
    assert ('NORMAL' in body_attrib)==explicit_normals
    assert ('COLOR_0' in body_attrib)==(not flat_material)
    report['variants'].append({
        'label':label,'glb':file.name,'bytes':len(data),
        'sha256':hashlib.sha256(data).hexdigest(),
        'triangles':tris,'mesh_count':len(again.geometry),
        'body_color_0_in_gltf':('COLOR_0' in body_attrib),
        'body_normal_in_gltf':('NORMAL' in body_attrib),
        'body_visual_kind_on_reimport':again.geometry[bodyname].visual.kind,
        'approved':False,
        'actual_mobile_phone_tested':False})
(out/'metrics.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
