#!/usr/bin/env python3
"""Run91B: preserve ORIGINAL COLOR_0 feather/heart colors, repair glTF default metal=1.
The user's required young Tyto anatomy is still ART_REJECTED. Technical control only.
Must output REAL 3D glTF2 binary, Blender render, browser screenshots and pixel QA.
"""
import json, math, hashlib, struct, argparse, importlib.util
from pathlib import Path
import trimesh
from trimesh.exchange.gltf import export_glb

P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('organic_sculpt',P/'mesoptile_organic_sculpt_trial_v31.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

def chunks(data):
    assert data[:4]==b'glTF' and struct.unpack_from('<I',data,8)[0]==len(data)
    pos=12
    while pos<len(data):
        length,typ=struct.unpack_from('<I4s',data,pos)
        payload=data[pos+8:pos+8+length]
        assert len(payload)==length and length%4==0
        yield typ,payload
        pos+=8+length
    assert pos==len(data)

def read_doc(data):
    return json.loads(next(p for k,p in chunks(data) if k==b'JSON'))

def repair_default_metal_1(data):
    cc=list(chunks(data)); assert cc[0][0]==b'JSON'
    doc=json.loads(cc[0][1])
    materials=doc.setdefault('materials',[])
    idx=len(materials)
    materials.append({
       'name':'RUN91B_REPAIR_COLOR_0_MATTE_PBR_DO_NOT_APPROVE_ART',
       'pbrMetallicRoughness':{
           'baseColorFactor':[1.0,1.0,1.0,1.0],
           'metallicFactor':0.0,'roughnessFactor':0.95},
       'doubleSided':False})
    changed=[]
    for mesh in doc['meshes']:
        for primitive in mesh.get('primitives',[]):
            if 'COLOR_0' in primitive['attributes'] and 'material' not in primitive:
                primitive['material']=idx
                changed.append(mesh['name'])
    assert 'ORGANIC_CONNECTED_HEAD_BODY_HEART_RELIEF' in changed,changed
    raw=json.dumps(doc,separators=(',',':'),ensure_ascii=False).encode('utf-8')
    raw+=b' ' * (-len(raw)%4)
    outchunks=[(b'JSON',raw)]+cc[1:]
    segment=b''.join(struct.pack('<I4s',len(p),typ)+p for typ,p in outchunks)
    output=struct.pack('<4sII',b'glTF',2,len(segment)+12)+segment
    assert read_doc(output)['materials'][idx]['pbrMetallicRoughness']['metallicFactor']==0
    return output,changed

parser=argparse.ArgumentParser();parser.add_argument('out',type=Path);parser.add_argument('--resolution',type=int,default=108)
a=parser.parse_args();a.out.mkdir(parents=True,exist_ok=True)
scene,raw_stats=mod.make_scene(res=a.resolution,n_down=1200)
body=scene.geometry['ORGANIC_CONNECTED_HEAD_BODY_HEART_RELIEF']
assert body.is_watertight and body.volume>0
scene.apply_transform(trimesh.transformations.rotation_matrix(-math.pi/2,[1,0,0]))
original=export_glb(scene,include_normals=True,unitize_normals=True)
fixed,changed=repair_default_metal_1(original)
report={'task':'Run91B explicit rough nonmetal PBR on original vertex COLOR_0',
 'status':'ART_REJECTED_UNCONDITIONALLY',
 'not_user_demo':True,'old_geometry_no_anatomy_fix':True,
 'source_continuous_sculpt':'v31 original from repository',
 'material_repair':{'changed_meshes':changed,'count':len(changed),
    'gltf_default_metallic_factor_if_no_material':1.0,
    'explicit_repaired_metallic_factor':0.0,
    'vertex_COLOR_0_preserved':True,'explicit_NORMAL_preserved':True},
 'no_physical_phone_test':True,'variants':[]}
for label,data in [('default_metal_implicit',original),('vertex_color_matte_pbr_repaired',fixed)]:
    target=a.out/f'owl172_run91b_{label}_REJECTED.glb'
    target.write_bytes(data)
    doc=read_doc(data)
    again=trimesh.load(target,force='scene',process=False)
    ntris=sum(len(m.faces) for m in again.geometry.values())
    bodys=[p for m in doc['meshes'] if m.get('name')=='ORGANIC_CONNECTED_HEAD_BODY_HEART_RELIEF' for p in m['primitives']]
    assert len(bodys)==1 and 'COLOR_0' in bodys[0]['attributes'] and 'NORMAL' in bodys[0]['attributes']
    mat=bodys[0].get('material')
    if label.startswith('vertex_'):assert mat is not None and doc['materials'][mat]['pbrMetallicRoughness']['metallicFactor']==0
    else:assert mat is None
    report['variants'].append({'label':label,'glb':target.name,'bytes':len(data),
        'sha256':hashlib.sha256(data).hexdigest(),'triangle_count':ntris,
        'mesh_count':len(again.geometry),
        'body_material':None if mat is None else doc['materials'][mat]['name'],
        'body_color_0':True,'body_normal':True,'approved':False})
assert report['variants'][0]['triangle_count']==report['variants'][1]['triangle_count']
assert report['variants'][0]['mesh_count']==report['variants'][1]['mesh_count']
(a.out/'metrics.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
