#!/usr/bin/env python3
"""Run254: honest R&D study, re-proportion an existing authentic Hunyuan
neural owl sculpture by a smooth spatial warp; NOT a new neural model,
NOT an art-approved pet. Target: #172 v3 right chick.
No primitives added, no change to 251-species production or kitty prototype.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np, trimesh

PIN='cd1513ac0822eef25bb56f9f8d08d244cac64d209ea8c92333693d287c926eb6'
CORE='real_neural_owl_juvenile_core'
DOWN='real_3d_surface_following_wispy_down'

def sh(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def sm(a,b,v):
    t=np.clip((v-a)/(b-a),0,1)
    return t*t*(3-2*t)

def deform(v,variant):
    o=np.array(v,dtype=np.float64,copy=True)
    x,y,z=o.T
    # Protect crown/eye zone, fair broad belly/shoulder into learned mesh.
    torso=sm(-.74,-.38,y)*(1-sm(.32,.78,y))
    width={'A':.30,'B':.38}[variant]
    o[:,0] += x*width*torso*(.84+.16*sm(-.35,.1,z))
    # Shorten the overly columnar neck/upper-body silhouette continuously.
    neck=sm(-.60,-.20,y)*(1-sm(.44,.91,y))
    o[:,1] -= {'A':.060,'B':.090}[variant]*neck
    # Draw the adult-derived hanging posterior remiges forward, no planar cut.
    posterior=1-sm(-.48,-.08,z)
    wingzone=sm(-.76,-.35,y)*(1-sm(.22,.75,y))
    o[:,2] += {'A':.13,'B':.19}[variant]*posterior*wingzone
    # Raise distal rear feather tips without moving anterior feet.
    low=1-sm(-.66,-.23,y)
    o[:,1] += {'A':.08,'B':.115}[variant]*posterior*low
    # Plump the anterior chest through a continuous deformation field.
    frontal=sm(.05,.50,z)*sm(-.53,-.22,y)*(1-sm(.16,.62,y))
    o[:,2] += {'A':.045,'B':.075}[variant]*frontal
    return o

def calculate(src,outdir):
    src=Path(src);outdir=Path(outdir);outdir.mkdir(parents=True,exist_ok=True)
    assert sh(src)==PIN, ('BAD_SOURCE',sh(src))
    base=trimesh.load(src,force='scene')
    assert CORE in base.geometry and DOWN in base.geometry
    original=base.geometry[CORE]
    rep={
      'run':'Run254',
      'method':'authentic continuous neural body/mesoptile 3D anatomically targeted smooth deformation, not primitives',
      'source_sha256':PIN,
      'reference':'#172 v3 rightmost original concept',
      'reference_concept_git_blob_sha':'5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b',
      'art_approved':False,'phone_hardware':'UNTESTED',
      'extra_paid_usd':0,'release':'NO_RELEASE','variants':{}
    }
    for variant in 'AB':
        scene=trimesh.load(src,force='scene')
        core=scene.geometry[CORE];fur=scene.geometry[DOWN]
        ov=core.vertices.copy();of=fur.vertices.copy()
        nv=deform(ov,variant);nf=deform(of,variant)
        core.vertices=nv;fur.vertices=nf
        v0=ov[core.faces];v1=nv[core.faces]
        n0=np.cross(v0[:,1]-v0[:,0],v0[:,2]-v0[:,0])
        n1=np.cross(v1[:,1]-v1[:,0],v1[:,2]-v1[:,0])
        flips=int(np.count_nonzero(np.einsum('ij,ij->i',n0,n1)<=0))
        assert flips==0,(variant,flips)
        assert core.is_watertight and core.volume>0
        out=outdir/f'run254_{variant}_authentic_neural_juvenile_proportion_test_ART_UNAPPROVED_NO_RELEASE.glb'
        out.write_bytes(scene.export(file_type='glb',include_normals=True))
        readback=trimesh.load(out,force='scene')
        assert len(readback.geometry)==9
        assert all(np.isfinite(g.vertices).all() for g in readback.geometry.values())
        pupil=readback.geometry['sculpt_anatomical_eye_detail_1'].visual.material
        assert pupil.baseColorFactor[0]<20
        m={
          'file':out.name,'sha256':sh(out),'bytes':out.stat().st_size,
          'meshes':len(readback.geometry),
          'triangle_count':int(sum(len(g.faces) for g in readback.geometry.values())),
          'core_watertight':bool(readback.geometry[CORE].is_watertight),
          'core_volume':float(readback.geometry[CORE].volume),
          'core_original_volume':float(original.volume),
          'core_bounds':np.round(core.bounds,4).tolist(),
          'source_core_bounds':np.round(original.bounds,4).tolist(),
          'core_triangle_flips':flips,
          'displacement_max':float(np.linalg.norm(nv-ov,axis=1).max()),
          'displacement_mean':float(np.linalg.norm(nv-ov,axis=1).mean()),
          'actual_neural_vertices_moved_gt_0.01':int(np.sum(np.linalg.norm(nv-ov,axis=1)>.01)),
          'source_groom_vertices':len(of),
          'core_original_triangles':len(original.faces),
          'dark_eyes':True,
          'art_approved':False
        }
        rep['variants'][variant]=m
        print(json.dumps({variant:m}),flush=True)
    (outdir/'run254_geometry_report.json').write_text(json.dumps(rep,indent=2)+'\n')
    return rep

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--source',required=True)
    p.add_argument('--outdir',required=True)
    a=p.parse_args()
    calculate(a.source,a.outdir)
