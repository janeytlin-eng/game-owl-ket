#!/usr/bin/env python3
"""Run249: monotone rear-remige contraction on a SHA-pinned native neural owl mesh.
No procedural fake bird / no release. Y-up, +Z-front.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import trimesh
from scipy.spatial import cKDTree

SOURCE_SHA="247d820538920735783072a204686fcf2f02ddb3ce1958a5472895a3ed7c1845"
CORE="real_neural_owl_juvenile_core"
DOWN="real_3d_surface_following_wispy_down"

def ss(a,b,t):
    u=np.clip((t-a)/(b-a),0,1)
    return u*u*(3-2*u)

def warp(p,variant):
    q=p.astype(np.float64).copy()
    x,y,z=q.T
    cfg={"A":(.55,.26,.09),"B":(.35,.34,.16)}[variant]
    factor,lift,side=cfg
    zz=np.minimum(z+.035,0)
    q[:,2]=z+(factor-1)*zz*ss(.03,.11,-z)
    tip=ss(.18,-.42,y)*ss(.04,-.24,z)
    paw_free=ss(.55,.10,z)
    q[:,1]+=lift*tip*paw_free
    q[:,0]=x*(1-side*ss(.02,-.35,z)*ss(.35,-.25,y))
    return q

def inversions(old,new,faces):
    a=np.cross(old[faces[:,1]]-old[faces[:,0]],old[faces[:,2]]-old[faces[:,0]])
    b=np.cross(new[faces[:,1]]-new[faces[:,0]],new[faces[:,2]]-new[faces[:,0]])
    return int(np.sum(np.einsum("ij,ij->i",a,b)<=0))

def trial(src,out,version):
    scene=trimesh.load(src,force="scene")
    assert len(scene.geometry)==9
    core=scene.geometry[CORE]
    down=scene.geometry[DOWN]
    old=core.vertices.copy()
    oldfur=down.vertices.copy()
    faces=core.faces.copy()
    desired=warp(old,version)
    alpha=1.
    new=desired
    inv=inversions(old,new,faces)
    while inv and alpha>1/128:
        alpha/=2
        new=old+alpha*(desired-old)
        inv=inversions(old,new,faces)
    assert not inv
    idx=cKDTree(old).query(oldfur,k=1)[1]
    down.vertices=oldfur+(new-old)[idx]
    core.vertices=new
    path=out/("run249_"+version+"_true_neural_shortwing_remige_ablation_RESEARCH_NO_RELEASE.glb")
    path.write_bytes(scene.export(file_type="glb",include_normals=True))
    reread=trimesh.load(path,force="scene")
    assert len(reread.geometry)==9
    assert len(reread.geometry[CORE].faces)==46856
    assert sum(len(g.faces) for g in reread.geometry.values())==131835
    assert np.isfinite(reread.geometry[CORE].vertices).all()
    assert np.allclose(reread.geometry[CORE].vertices,new,atol=2e-5)
    return {"version":version,"source_sha256":SOURCE_SHA,"blend_factor":alpha,
        "real_neural_core_triangles":46856,"mesh_count":9,"triangles":131835,
        "inverted_core_triangles":inv,
        "changed_core_vertices_gt_0p01":int((np.linalg.norm(new-old,axis=1)>.01).sum()),
        "largest_core_displacement":float(np.linalg.norm(new-old,axis=1).max()),
        "original_bounds":np.vstack((old.min(axis=0),old.max(axis=0))).round(4).tolist(),
        "new_bounds":np.vstack((new.min(axis=0),new.max(axis=0))).round(4).tolist(),
        "glb_file":path.name,"glb_size_bytes":path.stat().st_size,
        "glb_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
        "art_approved":False,"physical_mobile_webgl":"UNTESTED","release":"NO_RELEASE"}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",required=True)
    ap.add_argument("--outdir",required=True)
    a=ap.parse_args()
    assert hashlib.sha256(Path(a.source).read_bytes()).hexdigest()==SOURCE_SHA
    out=Path(a.outdir);out.mkdir(exist_ok=True,parents=True)
    report={"run":"Run249","source_sha256":SOURCE_SHA,"art_approved":False,
        "release":"NO_RELEASE","physical_mobile_webgl":"UNTESTED","variants":{}}
    for v in ("A","B"):
        report["variants"][v]=trial(a.source,out,v)
    (out/"run249_machine_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":
    main()
