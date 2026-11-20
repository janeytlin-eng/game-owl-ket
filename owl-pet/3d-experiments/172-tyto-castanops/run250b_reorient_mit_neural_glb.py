#!/usr/bin/env python3
"""Run250b: exact native glTF reorientation preserving neural vertices, colors and topology.
ShapeStudio/TripoSR Z-up, Y-front => project Three.js Y-up, Z-front.
Not a new art generation, not a release. No primitive assembly.
"""
import argparse
import hashlib
import json
import struct
from pathlib import Path
import numpy as np

SOURCE_SHA='4cfa289e44bf12453442143113d1574f30b0b7445c98b2ac7a2c408aca770098'
MATRIX=[[-1,0,0],[0,0,1],[0,1,0]]

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def pad4(b,fill):
    return b+fill*((-len(b))%4)

def rotate(src,dst,outdir):
    src=Path(src);dst=Path(dst);outdir=Path(outdir)
    assert sha(src)==SOURCE_SHA, 'Run250 corrected neural GLB SHA mismatch'
    b=src.read_bytes()
    assert b[:4]==b'glTF'
    magic,ver,tot=struct.unpack_from('<III',b,0)
    assert (ver,tot)==(2,len(b))
    jsonlen,jsontype=struct.unpack_from('<II',b,12)
    assert jsontype==0x4E4F534A
    j=json.loads(b[20:20+jsonlen].decode())
    binloc=20+jsonlen
    binlen,bintype=struct.unpack_from('<II',b,binloc)
    assert bintype==0x004E4942
    buf=bytearray(b[binloc+8:binloc+8+binlen])
    assert len(buf)==j['buffers'][0]['byteLength']
    assert len(j['meshes'])==1 and len(j['meshes'][0]['primitives'])==1
    attrs=j['meshes'][0]['primitives'][0]['attributes']
    assert {'POSITION','NORMAL','COLOR_0'}.issubset(attrs)
    def accessor(name):
        a=j['accessors'][attrs[name]]
        v=j['bufferViews'][a['bufferView']]
        assert a['componentType']==5126 and a['type']=='VEC3'
        assert v.get('byteStride',12)==12
        off=v.get('byteOffset',0)+a.get('byteOffset',0)
        n=a['count']
        return a,off,np.frombuffer(buf,dtype='<f4',count=n*3,offset=off).reshape((n,3)).copy()
    a_pos,off_p,p=accessor('POSITION')
    a_norm,off_n,n=accessor('NORMAL')
    a_col,off_c,c=accessor('COLOR_0')
    assert len(p)==len(n)==len(c)==22594
    m=np.asarray(MATRIX,dtype=np.float64)
    assert np.linalg.det(m)>0.999999
    q=(p@m.T).astype('<f4')
    nn=(n@m.T).astype('<f4')
    assert np.isfinite(q).all() and np.isfinite(nn).all()
    assert np.allclose(q@m,p,atol=2e-7)
    colorbytes=bytes(buf[off_c:off_c+len(c)*12])
    buf[off_p:off_p+len(q)*12]=q.tobytes()
    buf[off_n:off_n+len(nn)*12]=nn.tobytes()
    assert bytes(buf[off_c:off_c+len(c)*12])==colorbytes
    a_pos['min']=q.min(axis=0).astype(float).tolist()
    a_pos['max']=q.max(axis=0).astype(float).tolist()
    j['asset'].setdefault('extras',{})['owl172Run250bOrientation']='Native neural GLB, transform (-x,z,y) for Y-up, Z-front; research-only'
    js=pad4(json.dumps(j,separators=(',',':')).encode(),b' ')
    binary=pad4(bytes(buf),b'\x00')
    result=struct.pack('<III',0x46546c67,2,12+8+len(js)+8+len(binary))
    result+=struct.pack('<II',len(js),0x4e4f534a)+js
    result+=struct.pack('<II',len(binary),0x004e4942)+binary
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_bytes(result)
    import trimesh
    original=trimesh.load(src,force='scene')
    check=trimesh.load(dst,force='scene')
    assert len(check.geometry)==len(original.geometry)==1
    old_mesh=next(iter(original.geometry.values()));new_mesh=next(iter(check.geometry.values()))
    assert len(new_mesh.faces)==len(old_mesh.faces)==45100
    assert len(new_mesh.vertices)==len(old_mesh.vertices)==22594
    assert np.array_equal(old_mesh.faces,new_mesh.faces)
    assert np.allclose(new_mesh.vertices,q,atol=1e-6)
    assert (new_mesh.bounds[1]-new_mesh.bounds[0])[1]>.5
    outdir.mkdir(parents=True,exist_ok=True)
    report={'run':'Run250b','model':'MIT TripoSR from Run250 visually corrected v3 crop',
      'original_source_sha256':SOURCE_SHA,'source_bytes':len(b),'oriented_sha256':sha(dst),
      'oriented_bytes':len(result),'oriented_glb':dst.name,'matrix':MATRIX,
      'mesh_count':len(check.geometry),'vertices':len(q),'triangles':len(new_mesh.faces),
      'preserved_triangle_indices':True,'preserved_original_color_bytes':True,
      'native_3d':True,'z_up_to_y_up':True,
      'source_axis':'TripoSR Z up +Y front','project_axis':'Three.js Y up +Z front',
      'original_bounds':original.bounds.round(5).tolist(),
      'oriented_bounds':check.bounds.round(5).tolist(),
      'plumulaceous_feather_quality':'UNREVIEWED',
      'heart_mask_and_eyes':'UNREVIEWED',
      'side_back_anatomy':'UNREVIEWED',
      'physical_mobile_webgl':'UNTESTED','art_approved':False,'release':'NO_RELEASE'}
    (outdir/'run250b_native_orientation_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',required=True)
    ap.add_argument('--target',required=True)
    ap.add_argument('--outdir',required=True)
    args=ap.parse_args()
    rotate(args.source,args.target,args.outdir)
