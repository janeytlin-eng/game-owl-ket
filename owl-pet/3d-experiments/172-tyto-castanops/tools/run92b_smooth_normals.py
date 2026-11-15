#!/usr/bin/env python3
"""Run92B controlled real-GLB geometry/normal ablation, research branch only.
Takes true Run92 TripoSR-generated GLB; retains COLOR_0, PBR, topology and vertices
and compares explicit normals vs Taubin-smoothed surface with explicit normals.
Neither output is accepted creature art until visually judged.
"""
import json,sys,struct,hashlib,pathlib
import numpy as np
import trimesh
root=pathlib.Path(sys.argv[1])
source=pathlib.Path(sys.argv[2])
root.mkdir(parents=True,exist_ok=True)
assert source.exists(),source
orig=source.read_bytes()
magic,vers,total=struct.unpack_from("<4sII",orig,0)
assert (magic,vers,total)==(b'glTF',2,len(orig))
jn,typ=struct.unpack_from("<I4s",orig,12)
assert typ==b'JSON'
gltf=json.loads(orig[20:20+jn])
bo=20+jn
bn,bt=struct.unpack_from("<I4s",orig,bo)
assert bt==b'BIN\x00'
binary=orig[bo+8:bo+8+bn]
p=gltf['meshes'][0]['primitives'][0]
a=gltf['accessors'][p['attributes']['POSITION']]
v=gltf['bufferViews'][a['bufferView']]
assert a['componentType']==5126 and a['type']=='VEC3'
ofs=v.get('byteOffset',0)+a.get('byteOffset',0)
positions=np.frombuffer(binary,offset=ofs,count=a['count']*3,dtype='<f4').copy().reshape(-1,3)
s=trimesh.load(source,force='scene',process=False)
mesh=list(s.geometry.values())[0]
assert np.allclose(mesh.vertices,positions)
assert len(mesh.faces)>10000 and len(mesh.vertices)==len(positions)
assert 'COLOR_0' in p['attributes']
assert gltf['materials'][p['material']]['pbrMetallicRoughness']['metallicFactor']==0.0
meta={'original_sha256':hashlib.sha256(orig).hexdigest(),'status':'ART_REJECTED',
      'original_source':'Run92 genuine CPU TripoSR single-image GLB',
      'reference_only_front':True,'retained_COLOR_0':True,'same_faces':True,
      'real_mobile_GPU_tested':False,'variants':[]}
for label,it in [('explicit_normal_control',0),('taubin12_smooth_explicit_normal',12)]:
    m=trimesh.Trimesh(vertices=positions.copy(),faces=mesh.faces.copy(),process=False)
    if it:
        trimesh.smoothing.filter_taubin(m,lamb=.45,nu=.52,iterations=it)
    verts=np.asarray(m.vertices,dtype='<f4')
    nrm=np.asarray(m.vertex_normals,dtype='<f4')
    assert nrm.shape==verts.shape and np.isfinite(nrm).all()
    j=json.loads(json.dumps(gltf))
    b=bytearray(binary)
    b[ofs:ofs+verts.nbytes]=verts.tobytes()
    while len(b)%4:b.append(0)
    norm_start=len(b);b.extend(nrm.tobytes())
    vid=len(j['bufferViews'])
    j['bufferViews'].append({'buffer':0,'byteOffset':norm_start,
                             'byteLength':nrm.nbytes,'target':34962})
    aid=len(j['accessors'])
    j['accessors'].append({'bufferView':vid,'byteOffset':0,'componentType':5126,
                           'count':len(verts),'type':'VEC3'})
    j['meshes'][0]['primitives'][0]['attributes']['NORMAL']=aid
    j['accessors'][p['attributes']['POSITION']]['min']=verts.min(axis=0).astype(float).tolist()
    j['accessors'][p['attributes']['POSITION']]['max']=verts.max(axis=0).astype(float).tolist()
    j['buffers'][0]['byteLength']=len(b)
    jj=json.dumps(j,separators=(',',':')).encode()
    jj+=b' '*((-len(jj))%4)
    packed=struct.pack('<4sII',b'glTF',2,12+8+len(jj)+8+len(b))
    packed+=struct.pack('<I4s',len(jj),b'JSON')+jj
    packed+=struct.pack('<I4s',len(b),b'BIN\x00')+b
    output=root/f'owl172_run92b_{label}_ART_REJECTED.glb'
    output.write_bytes(packed)
    again=trimesh.load(output,force='scene',process=False)
    tris=sum(len(o.faces) for o in again.geometry.values())
    assert tris==len(mesh.faces)
    secondj=json.loads(packed[20:20+len(jj)])
    assert 'NORMAL' in secondj['meshes'][0]['primitives'][0]['attributes']
    assert 'COLOR_0' in secondj['meshes'][0]['primitives'][0]['attributes']
    dist=np.linalg.norm(verts-positions,axis=1)
    meta['variants'].append({'label':label,'file':output.name,'bytes':len(packed),
       'sha256':hashlib.sha256(packed).hexdigest(),'vertices':len(verts),'triangles':tris,
       'max_vertex_displacement':float(dist.max()),'mean_vertex_displacement':float(dist.mean()),
       'explicit_NORMAL':True,'original_COLOR_0_preserved':True,
       'watertight':bool(m.is_watertight),'approved':False})
(root/'metrics.json').write_text(json.dumps(meta,indent=2))
print(json.dumps(meta,indent=2))
