#!/usr/bin/env python3
"""Run299: bounded research-only native mesh rear and folded-wing C2 sculpt.
The input is a real neural GLB, not a sphere assembly, SVG, sprite, or released art.
"""
import argparse, json, hashlib
from pathlib import Path
import numpy as np
import trimesh

SOURCE_SHA='bdf58cdcb8b859fbdfd83745bc2d0ee4d842f2fc7b89a8edc91d5215b6e5487f'
def hashfile(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def smooth(a,b,x):
    q=np.clip((x-a)/(b-a),0.,1.)
    return q*q*(3.-2.*q)

def warp(v,version):
    p=np.array(v,dtype=np.float64,copy=True)
    x,y,z=p.T
    strength={'A':1.0,'B':1.45}[version]
    back=1-smooth(-.28,.16,z)
    low=np.exp(-0.5*((y+.64)/.23)**2)
    yguard=smooth(-.91,-.76,y)
    sculpt=back*low*yguard
    p[:,2]+=strength*.205*sculpt
    p[:,1]+=strength*.107*sculpt
    rear=1-smooth(-.43,.02,z)
    volume=np.exp(-0.5*((y+.28)/.34)**2)
    side=np.clip(np.abs(x)/.55,0,1)
    p[:,0]+=np.sign(x)*strength*.042*volume*rear*side
    p[:,2]-=strength*.027*rear*volume
    sx=np.abs(x)
    wingpath=.42-.09*np.clip((-y+.07)/.75,0,1)
    atwing=np.exp(-.5*((sx-wingpath)/.14)**2)
    across=np.exp(-.5*((y+.15)/.29)**2)
    back_side=1-smooth(-.20,.30,z)
    guard=smooth(-.67,-.48,y)*(1-smooth(.27,.46,y))
    fold=atwing*across*back_side*guard
    p[:,0]+=np.sign(x)*strength*.035*fold
    p[:,2]-=strength*.018*fold
    foldlines=np.cos((y+.09)*32.)**2
    weak=fold*foldlines*.0035*strength
    p[:,0]+=np.sign(x)*weak
    return p

def run(src,outdir):
    src=Path(src);outdir=Path(outdir);outdir.mkdir(parents=True,exist_ok=True)
    original_sha=hashfile(src)
    assert original_sha==SOURCE_SHA, f'wrong source {original_sha}'
    old=trimesh.load(src,force='scene')
    names=list(old.geometry)
    assert len(names)==2 and sum(len(m.faces) for m in old.geometry.values())==31000
    assert sum('body' in s for s in names)==1 and sum('down' in s for s in names)==1
    data={'run':'Run299','method':'C2 continuous spatial wing and rear sculpt on real neural 3D mesh (no primitive additions)',
          'input_sha256':original_sha,'reference':'#172 Tyto castanops v3 rightmost downy juvenile',
          'original_names':names,'variants':{},'art_approved':False,'rights_cleared':False,
          'physical_phone_tested':False,'no_release':True,'additional_paid_usd':0}
    for version in ['A','B']:
        obj=trimesh.load(src,force='scene')
        metrics={}
        for name,m in obj.geometry.items():
            prior=m.vertices.copy()
            after=warp(prior,version)
            delta=np.linalg.norm(after-prior,axis=1)
            m.vertices=after
            metrics[name]={'vertex_count':len(after),'face_count':len(m.faces),
                           'moving_gt_0p01':int((delta>.01).sum()),'max_displacement':round(float(delta.max()),5),
                           'rms_displacement':round(float(np.sqrt(np.mean(delta**2))),5),
                           'bounds':np.round(m.bounds,5).tolist(),
                           'uv_preserved':m.visual.kind=='texture' and len(m.visual.uv)==len(m.vertices)}
            assert np.isfinite(after).all() and metrics[name]['uv_preserved']
        fp=outdir/f'run299_{version}_continuous_neural_wing-relief_ART_REJECTED_NO_RELEASE.glb'
        obj.export(fp)
        check=trimesh.load(fp,force='scene')
        assert len(check.geometry)==2 and sum(len(m.faces) for m in check.geometry.values())==31000
        assert all(m.visual.kind=='texture' for m in check.geometry.values())
        data['variants'][version]={'file':fp.name,'sha256':hashfile(fp),'bytes':fp.stat().st_size,
                                   'triangles':sum(len(m.faces) for m in check.geometry.values()),
                                   'mesh_metrics':metrics,'technical_import_pass':True,'art_approved':False}
    (outdir/'run299_geometry_report.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
    print(json.dumps(data,ensure_ascii=False,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--src',required=True);ap.add_argument('--outdir',required=True)
    a=ap.parse_args();run(a.src,a.outdir)
