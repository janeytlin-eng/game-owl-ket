#!/usr/bin/env python3
"""Run283 RESEARCH ONLY: exact verified Run282c real TripoSR mesh, no primitive substitutions.
Spatially blended vertex colours remove discontinuous front/back UV atlas.
Physical 3D curved feather-tract vanes are attached to the genuine reconstructed surface.
ART_REJECTED / PHONE_UNTESTED / SOURCE_RIGHTS_UNCLEARED / NO_RELEASE.
"""
import sys,json,struct,hashlib,pathlib,math
import numpy as np, trimesh
from PIL import Image
from scipy.ndimage import map_coordinates
from run281_triposr_cpu_juvenile_reference_NO_RELEASE import qa,sha
SOURCE_SHA='5eb3064d07495bfdc120ee6a420671c0bce07c118bdad31123c88d5113e10e88'
REF_SHA='8eee63bf0b8650c390d4c4bba6a07a0c2dd05dd7fc2e90e00a896ec3ab51c641'

def colors(m,photo):
    v=m.vertices;n=m.vertex_normals
    y=np.clip((v[:,1]+.35)/.75,0,1)
    neutral=np.stack([218+18*y,196+24*y,172+29*y],axis=1)
    neutral+=np.clip(6*(v[:,2]+.1),-3,3)[:,None]
    img=np.asarray(photo,dtype=float)
    u=np.clip(250+390*v[:,0],0,511)
    w=np.clip(257-450*v[:,1],0,511)
    sampled=np.stack([map_coordinates(img[:,:,k],[w,u],order=1,mode='nearest') for k in range(3)],axis=1)
    prob=np.clip((np.linalg.norm(sampled-128,axis=1)-9)/19,0,1)
    orient=np.clip((n[:,2]+.18)/.94,0,1);orient*=orient*(3-2*orient)
    front=np.clip((v[:,2]+.17)/.43,0,1);front*=front*(3-2*front)
    mix=(orient*front*.97*prob)[:,None]
    rgb=np.clip(np.round(neutral*(1-mix)+sampled*mix),0,255).astype('uint8')
    return np.column_stack([rgb,np.full(len(v),255,dtype='uint8')])

def feathers(m):
    rng=np.random.default_rng(172283)
    samples,idx=trimesh.sample.sample_surface(m,40000,seed=172283)
    norms=m.face_normals[idx]
    masks={'back':(norms[:,2]<-.15)&(samples[:,1]>-.35)&(samples[:,1]<.37)&(np.abs(samples[:,0])<.34),
           'flank':(np.abs(norms[:,0])>.34)&(samples[:,1]>-.28)&(samples[:,1]<.26)&(np.abs(samples[:,0])>.145)}
    verts=[];rgba=[];faces=[];offset=0;counts={}
    for kind,total in [('back',2800),('flank',800)]:
        ids=np.flatnonzero(masks[kind])
        if len(ids)<total//2:raise ValueError('not enough actual neural surface samples')
        picks=rng.choice(ids,size=total,replace=len(ids)<total)
        counts[kind]=len(picks)
        for k in picks:
            p=samples[k];normal=norms[k];normal/=np.linalg.norm(normal)
            flow=np.array([np.sign(p[0])*.22,-1.,-.28]) if kind=='flank' else np.array([p[0]*.13,-1.,-.14])
            tangent=flow-normal*np.dot(flow,normal);l=np.linalg.norm(tangent)
            if l<1e-5:continue
            tangent/=l
            side=np.cross(normal,tangent);side/=np.linalg.norm(side)
            L=rng.uniform(.025,.057) if kind=='back' else rng.uniform(.048,.093)
            W=rng.uniform(.004,.011) if kind=='back' else rng.uniform(.010,.019)
            twist=rng.normal(0,.15)
            for t,width in [(0.,.46),(.26,1.),(.62,.79),(.9,.32),(1.,.015)]:
                center=p+t*L*tangent+normal*(.003+.006*math.sin(math.pi*t))+side*twist*L*t*t
                for sign in (-1,1):
                    verts.append(center+side*sign*W*width)
                    c=(np.array([235,220,201]) if kind=='back' else np.array([230,207,181]))+rng.uniform(-6,7)-13*t-3*abs(sign)
                    rgba.append([*np.clip(c,0,255).astype('uint8'),255])
            for i in range(4):
                q=offset+2*i
                faces.extend([(q,q+2,q+1),(q+1,q+2,q+3)])
            offset+=10
    m=trimesh.Trimesh(vertices=np.array(verts),faces=np.array(faces),process=False)
    m.vertex_normals=m.vertex_normals
    m.visual=trimesh.visual.ColorVisuals(mesh=m,vertex_colors=np.array(rgba,dtype='uint8'))
    return m,counts

def explicit_pbr(path):
    raw=path.read_bytes()
    assert raw[:4]==b'glTF' and struct.unpack_from('<I',raw,4)[0]==2
    length=struct.unpack_from('<I',raw,12)[0]
    obj=json.loads(raw[20:20+length])
    tail=raw[20+length:]
    assert tail[4:8]==b'BIN\x00'
    obj['materials']=[{'name':x,'doubleSided':True,'pbrMetallicRoughness':{'baseColorFactor':[1,1,1,1],'metallicFactor':0,'roughnessFactor':1}} for x in ['matte_cream_body','matte_cream_feathers']]
    for k,mesh in enumerate(obj['meshes']):
        for pr in mesh['primitives']:pr['material']=min(k,1)
    jb=json.dumps(obj,separators=(',',':')).encode()
    jb+=b' '*((-len(jb))%4)
    path.write_bytes(struct.pack('<4sII',b'glTF',2,20+len(jb)+len(tail))+struct.pack('<I4s',len(jb),b'JSON')+jb+tail)

def main(source,atlas,out):
    source=pathlib.Path(source);atlas=pathlib.Path(atlas);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
    assert sha(source)==SOURCE_SHA, 'Authentic previous real neural GLB hash REQUIRED'
    img=Image.open(atlas).convert('RGB');assert img.size==(1024,512)
    photo=img.crop((0,0,512,512));ref=out/'reference_512_from_original_atlas_RESEARCH.png';photo.save(ref)
    assert sha(ref)==REF_SHA, 'Wrong juvenile source image'
    m=next(iter(trimesh.load(source,force='scene').geometry.values())).copy()
    assert m.is_watertight and len(m.faces)==129168
    m.visual=trimesh.visual.ColorVisuals(mesh=m,vertex_colors=colors(m,photo))
    other,counts=feathers(m)
    report={'source_glb_sha256':sha(source),'source_image_sha256':sha(ref),
        'real_3d_feather_tract_counts':counts,'variants':{},
        'art':'UNREVIEWED_NO_RELEASE','physical_phone':'NOT_TESTED','commercial_rights':'NOT_CLEARED'}
    for label,feathered in [('seamless_vertex_color',False),('seamless_feather_tracts',True)]:
        scene=trimesh.Scene()
        scene.add_geometry(m,geom_name='verified_true_neural_sculpt_no_uv_seam')
        if feathered:scene.add_geometry(other,geom_name='true_spatial_feather_vanes')
        file=out/('run283_'+label+'_RESEARCH_NO_RELEASE.glb')
        file.write_bytes(trimesh.exchange.gltf.export_glb(scene));explicit_pbr(file)
        reread=trimesh.load(file,force='scene');meshes=list(reread.geometry.values())
        triangles=sum(len(x.faces) for x in meshes)
        expected=129168+(len(other.faces) if feathered else 0)
        assert triangles==expected and len(meshes)==(2 if feathered else 1)
        raw=file.read_bytes();ln=struct.unpack_from('<I',raw,12)[0];g=json.loads(raw[20:20+ln])
        assert all('COLOR_0' in p['attributes'] and 'material' in p for mm in g['meshes'] for p in mm['primitives'])
        qa(file,out/(label+'_six_views'))
        report['variants'][label]={'triangles':triangles,'meshes':len(meshes),'bytes':len(raw),'sha256':sha(file),
            'color0_pass':True,'explicit_matte_PBR_pass':True,'six_true_spatial_views':6,'art':'PENDING_MANUAL_REVIEW'}
    (out/'run283_validation.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
if __name__=='__main__':main(*sys.argv[1:])
