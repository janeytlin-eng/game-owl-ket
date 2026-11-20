#!/usr/bin/env python3
"""Run248 true neural owl anatomical test: wing fairing and juvenile body mass.

Runs on the existing SHA-pinned actual learned 3D mesh; no procedural primitive
owl, 2D billboarding, fake turntables or new paid service. Research NO_RELEASE.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
import trimesh

SOURCE_SHA="7864afc8a220c7edfa069f4d5bf2498db0fe0810c7e917a0451fc8201f22312b"
CORE="real_neural_owl_juvenile_core"
DOWN="real_3d_surface_following_wispy_down"

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ss(a,b,x):
    t=np.clip((x-a)/(b-a),0.,1.)
    return t*t*(3-2*t)
def bounds(m): return np.round(m.bounds,5).tolist()

def sculpt(v,faces,variant):
    """Local limb/back sculpt; protect the forward eye-disc and both eyes."""
    p=v.astype(np.float64).copy()
    x,y,z=p.T
    # Note: Y is UP, and +Z is FRONT in the tested Three.js viewer.
    protect=ss(.28,.55,y)*ss(.30,.62,z)
    wing_lat=ss(.30,.50,np.abs(x))*(1-protect)
    wing_low=ss(.28,-.48,y) * ss(-.8,-.20,y)
    wing_rear=ss(.30,-.15,z)
    wing=np.clip(wing_lat*wing_low*(.68+.32*wing_rear),0,1)
    rump=ss(.28,-.25,z)*ss(-.68,-.30,y)*(1-ss(.20,.48,y))
    belly=np.exp(-((y+.15)/.35)**2)*np.exp(-((z-.27)/.53)**2)*(1-protect)
    if variant=="A": cfg=dict(tuck_x=.065,wing_lift=.11,rear_in=.105,belly_x=.070)
    else: cfg=dict(tuck_x=.10,wing_lift=.17,rear_in=.155,belly_x=.105)
    new=p.copy()
    # Distinct from prior global squash: wing-only medial tuck, upper folded tip,
    # rump move toward chest and volumetric chest widening, mask-protected.
    new[:,0] += np.sign(x)*(cfg["belly_x"]*belly - cfg["tuck_x"]*wing)
    new[:,1] += cfg["wing_lift"]*wing*ss(-.10,-.65,y)
    new[:,2] += cfg["rear_in"]*(.74*wing*wing_rear+.42*rump)
    # Varying surface fairing in wing region only: cotangent-free mesh adjacency
    # Laplacian/Taubin smoothing attenuates hard adult feather relief.
    a,b,c=faces[:,0],faces[:,1],faces[:,2]
    ids=np.concatenate([a,b,b,c,c,a]); nbr=np.concatenate([b,a,c,b,a,c])
    degree=np.bincount(ids,minlength=len(v)).astype(np.float64)
    mask=np.clip(wing*.85 + rump*.27,0,1)*(1-protect)
    sm=new.copy()
    for _ in range(5 if variant=="A" else 8):
        for alpha in (.42,-.435):
            val=np.zeros_like(sm)
            np.add.at(val,ids,sm[nbr])
            val/=np.maximum(degree[:,None],1.)
            sm+=alpha*mask[:,None]*(val-sm)
    # Prevent local surface inversions; reduce deformation if original triangles
    # reverse orientation. This is stricter than simply re-importing a GLB.
    src=np.cross(p[faces[:,1]]-p[faces[:,0]],p[faces[:,2]]-p[faces[:,0]])
    def inverted(q):
        f=np.cross(q[faces[:,1]]-q[faces[:,0]],q[faces[:,2]]-q[faces[:,0]])
        m=np.linalg.norm(src,axis=1)>1e-9
        return int(np.sum(((f*src).sum(axis=1)<=0)&m))
    correction=1.
    while inverted(p+correction*(sm-p))>0 and correction>1/64:
        correction*=.5
    new=p+correction*(sm-p)
    result=dict(version=variant,params=cfg,correction=correction,
                inverted_triangles=inverted(new),
                max_vertex_change=float(np.linalg.norm(new-p,axis=1).max()),
                changed_vertices_gt_0p01=int((np.linalg.norm(new-p,axis=1)>.01).sum()),
                face_protected_max_shift=float(np.linalg.norm(new[protect>.95]-p[protect>.95],axis=1).max(initial=0.)),
                core_bounds_before=np.round(np.array([p.min(axis=0),p.max(axis=0)]),4).tolist(),
                core_bounds_after=np.round(np.array([new.min(axis=0),new.max(axis=0)]),4).tolist())
    return new, result

def trial(src, out, variant):
    scene=trimesh.load(src,force="scene")
    assert len(scene.geometry)==9
    core=scene.geometry[CORE]
    fur=scene.geometry[DOWN]
    original=core.vertices.copy()
    neural_faces=core.faces.copy()
    revised, report=sculpt(original,neural_faces,variant)
    disp=revised-original
    # Move inherited 3D tufts with their true neural surface, not detached hair.
    _,index=cKDTree(original).query(fur.vertices,k=1)
    fur.vertices=fur.vertices+disp[index]
    core.vertices=revised
    assert np.array_equal(core.faces,neural_faces)
    assert report["inverted_triangles"]==0
    assert len(scene.geometry)==9
    target=out/f"run248_{variant}_true_neural_juvenile_selective_wing_sculpt_RESEARCH_NO_RELEASE.glb"
    target.write_bytes(scene.export(file_type="glb",include_normals=True))
    check=trimesh.load(target,force="scene")
    assert len(check.geometry)==9
    assert len(check.geometry[CORE].faces)==46856
    assert sum(len(m.faces) for m in check.geometry.values())==131835
    assert all(np.isfinite(m.vertices).all() and len(m.vertex_normals)==len(m.vertices) for m in check.geometry.values())
    assert np.allclose(check.geometry[CORE].vertices,revised,atol=1e-5)
    report.update(glb=target.name,glb_bytes=target.stat().st_size,glb_sha256=sha(target),
                  scene_meshes=len(check.geometry),scene_triangles=131835,
                  source_owl_true_neural=True,old_fur_root_transferred=True,
                  art_approved=False,phone_gpu="UNTESTED",release="NO_RELEASE")
    return report

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--source",required=True);ap.add_argument("--outdir",required=True)
    args=ap.parse_args()
    assert sha(args.source)==SOURCE_SHA,"unverified source not allowed"
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    record=dict(run="Run248",source_sha256=SOURCE_SHA,
                purpose="anatomical selective wing tuck + real mesh local fairing",
                status="TECH_RESEARCH_NOT_ART_VERIFIED",art_approved=False,
                release="NO_RELEASE",phone_gpu="UNTESTED",extra_paid_usd=0,variants={})
    for v in ("A","B"):
        record["variants"][v]=trial(args.source,out,v)
    (out/"run248_machine_report.json").write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps(record,indent=2))
if __name__=="__main__": main()
