#!/usr/bin/env python3
"""Run92 strictly ART_REJECTED: new implicit juvenile anatomy vs Run91B baseline.
Experimental genuine connected marching-cubes sculpt + short alpha-down cards.
No image-only fake, no adult mesh, no claims of art acceptance or phone GPU test.
"""
import argparse, hashlib, json, importlib.util, math, struct
from pathlib import Path
import numpy as np
from scipy.ndimage import gaussian_filter
from trimesh.exchange.gltf import export_glb
import trimesh
from PIL import Image
from trimesh.visual.material import PBRMaterial

P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('previous_v31',P/'mesoptile_organic_sculpt_trial_v31.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
clip=lambda x: np.clip(x,0,1)
def ell(X,Y,Z,c,r):
    return (np.sqrt(((X-c[0])/r[0])**2+((Y-c[1])/r[1])**2+((Z-c[2])/r[2])**2)-1)*min(r)
def smin(a,b,k):
    h=clip(.5+.5*(b-a)/k)
    return b*(1-h)+a*h-k*h*(1-h)
def field(X,Y,Z):
    # Completely new unified crouching juvenile volume: skull, cheeks, shoulders,
    # breast and two tiny down-buried wing bulges voxel-meshed into one skin.
    # No adult asset transfer and no independent visible sphere stack.
    d=ell(X,Y,Z,(0,.047,.47),(.465,.414,.423))
    d=smin(d,ell(X,Y,Z,(0,-.045,.84),(.398,.367,.367)),.32)
    d=smin(d,ell(X,Y,Z,(0,-.14,.50),(.364,.309,.315)),.23)
    for side in (-1,1):
        d=smin(d,ell(X,Y,Z,(side*.403,.073,.513),(.115,.251,.20)),.155)
        d=smin(d,ell(X,Y,Z,(side*.232,-.155,.246),(.100,.13,.159)),.08)
    # Smooth low-amplitude sculpt asymmetry, not the old horizontal rib/pillow noise.
    noise=(.0032*np.sin(14*X+6*Z)*np.sin(12*Y-8*X)
         +.0027*np.sin(26*Y+17*Z+12*X)
         +.0016*np.cos(47*X-19*Z))
    d+=noise
    heart=old.heart_field(X,Z)
    front=clip((-Y-.216)/.135)
    # Physiological facial disc: broad, shallow concavity, no cartoon raised mask.
    fade=clip((Z-.655)/.15)*clip((1.225-Z)/.11)
    inside=clip(-heart/.083)
    rim=np.exp(-((heart+.019)/.10)**2)
    d+=front*fade*(.014*inside-.0017*rim)
    for side in (-1,1):
        depression=np.exp(-((X-side*.139)/.099)**2-((Z-.956)/.091)**2)
        d+=.022*front*depression
    return d

# Surgical replacement of the SDF while retaining v31's verified
# marching cubes, shading, 3D anatomy export and PBR card implementation.
old.body_sdf=field

def rounded_tuft_texture():
    W,H=128,192
    x,y=np.meshgrid(np.linspace(-1,1,W),np.linspace(0,1,H))
    # broad, feathered translucent tufts, not long straight needle silhouettes
    w=.82*(1-.32*y)
    signed=np.abs(x-.045*np.sin(3*np.pi*y))
    feather=clip((w-signed)/.32)
    fade=clip((y-.015)/.105)*clip((1-y)/.21)
    f=.82+.14*np.cos(11*x+9*y)**2
    rgba=np.zeros((H,W,4),dtype=np.uint8)
    rgba[:,:,:3]=[251,244,227]
    rgba[:,:,3]=(148*feather*fade*f).astype(np.uint8)
    return Image.fromarray(rgba,'RGBA')
old.down_texture=rounded_tuft_texture

def pbr_repair(data):
    assert data[:4]==b'glTF'
    pos=12;chunks=[]
    while pos<len(data):
        n,kind=struct.unpack_from('<I4s',data,pos)
        chunks.append((kind,data[pos+8:pos+8+n]))
        pos+=8+n
    assert pos==len(data) and chunks[0][0]==b'JSON'
    doc=json.loads(chunks[0][1])
    materials=doc.setdefault('materials',[])
    idx=len(materials)
    materials.append({'name':'Run92_NONMETALLIC_VERTEX_COLOR_SKIN_MATTE_ART_REJECTED',
      'pbrMetallicRoughness':{'baseColorFactor':[1,1,1,1],
                            'metallicFactor':0,'roughnessFactor':.97}})
    patched=0
    for mesh in doc['meshes']:
        for prim in mesh['primitives']:
            if 'COLOR_0' in prim['attributes'] and 'material' not in prim:
                prim['material']=idx;patched+=1
    assert patched>=20,patched
    j=json.dumps(doc,separators=(',',':')).encode('utf8')
    j+=b' '*(-len(j)%4)
    block=b''.join(struct.pack('<I4s',len(payload),kind)+payload
      for kind,payload in [(b'JSON',j)]+chunks[1:])
    result=struct.pack('<4sII',b'glTF',2,len(block)+12)+block
    assert result[:4]==b'glTF'
    return result,patched

def main():
    a=argparse.ArgumentParser()
    a.add_argument('out',type=Path)
    a.add_argument('--resolution',type=int,default=116)
    cfg=a.parse_args();cfg.out.mkdir(parents=True,exist_ok=True)
    baseline=cfg.out/'owl172_run91b_vertex_color_matte_pbr_repaired_REJECTED.glb'
    assert baseline.is_file() and baseline.stat().st_size>1_000_000
    baseline_sha=hashlib.sha256(baseline.read_bytes()).hexdigest()
    assert baseline_sha=='47088e4e5a3c6267bdb01d0cf9e5bdd344e1a6ba4f9d4955cb17a22ed61870c6'
    metrics={'date':'2026-11-16', 'model':'#172 Tyto castanops v3 right cream juvenile',
      'verdict':'ART_REJECTED_UNTIL_MULTIVIEW_HUMAN_REVIEW','user_demo':False,
      'fresh_implicit_sculpt':True,'previous_pear_sculpt_deformed':False,
      'physical_phone_tested':False,'previous_reference_side_back_unknown':True,
      'glTF_COLOR_0_nonmetal_PBR_repair':True,'variants':[]}
    base=trimesh.load(baseline,force='scene',process=False)
    metrics['variants'].append({'label':'prior_run91b_repaired_control',
      'glb':baseline.name,'bytes':baseline.stat().st_size,'sha256':baseline_sha,
      'triangle_count':sum(len(g.faces) for g in base.geometry.values()),
      'mesh_count':len(base.geometry),'approved':False,'provenance':'Run91B existing rejected GLB'})
    for label,hairs in [('new_sculpt_smooth',1200),('new_sculpt_soft_tuft',4500)]:
        scene,info=old.make_scene(res=cfg.resolution,n_down=hairs)
        body=scene.geometry['ORGANIC_CONNECTED_HEAD_BODY_HEART_RELIEF']
        assert body.is_watertight and body.volume>0
        # Inset eye bulbs toward the newly sculpted face surface
        for name,mesh in scene.geometry.items():
            if name.startswith('eye_'):
                mesh.vertices[:,1]-=.026
        scene.apply_transform(trimesh.transformations.rotation_matrix(-math.pi/2,[1,0,0]))
        raw=export_glb(scene,include_normals=True,unitize_normals=True)
        data,n_patched=pbr_repair(raw)
        path=cfg.out/f'owl172_run92_{label}_REJECTED.glb'
        path.write_bytes(data)
        fresh=trimesh.load(path,force='scene',process=False)
        variant={'label':label,'glb':path.name,'bytes':path.stat().st_size,
            'sha256':hashlib.sha256(data).hexdigest(),
            'triangle_count':sum(len(m.faces) for m in fresh.geometry.values()),
            'mesh_count':len(fresh.geometry),'down_cards':hairs,
            'connected_body_watertight':bool(body.is_watertight),
            'gltf_nonmetal_skin_material_meshes':n_patched,
            'physical_phone_test':False,'approved':False}
        metrics['variants'].append(variant)
    assert len(metrics['variants'])==3
    (cfg.out/'metrics.json').write_text(json.dumps(metrics,indent=2))
    print(json.dumps(metrics,indent=2))
if __name__=='__main__':main()
