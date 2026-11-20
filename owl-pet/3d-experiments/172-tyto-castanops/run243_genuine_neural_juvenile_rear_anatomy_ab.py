#!/usr/bin/env python3
"""Run243 research: true continuous neural 3D rump/wing/tail morphology, not a primitive owl.
All outputs ART_UNAPPROVED/NO_RELEASE; real phone validation is not inferred.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import trimesh
from run242_real_neural_wing_tuck_plumulaceous_atlas_ab import parse,pack,smoothstep
from run239_neural_silhouette_ab_trial import access,set_normals
PIN="ef60639bbba95a0e876ac427b277fa500063b9ce05d9b9c8bae5811a5c0518d1"
def sha(b):return hashlib.sha256(b).hexdigest()

def sculpt(v,p):
    q=v.astype(np.float64).copy()
    x,y,z=q[:,0],q[:,1],q[:,2]
    rear=smoothstep(-.03,-.49,z)
    low=1-smoothstep(-.40,.28,y)
    lock=smoothstep(-.70,-.43,y)
    face=1-smoothstep(.30,.57,z)
    wing=(smoothstep(.23,.52,np.abs(x))*smoothstep(-.49,-.19,y)
         *(1-smoothstep(.15,.47,y)))
    q[:,1]+=p["tail_lift"]*rear*low*lock*face+p["wing_fold_up"]*wing*rear*lock
    q[:,2]+=p["tail_retract"]*rear*low*lock*face+p["wing_fold_forward"]*wing*rear*lock
    rump=(smoothstep(-.72,-.40,y)*(1-smoothstep(.02,.25,y))
          *smoothstep(.1,-.42,z))
    q[:,0]+=np.sign(x)*p["rump_fullness"]*rump*(1-smoothstep(.48,.74,np.abs(x)))
    cheek=(np.exp(-((y-.31)/.18)**2)*np.exp(-((np.abs(x)-.34)/.17)**2)
           *np.exp(-((z-.44)/.23)**2))
    q[:,0]+=np.sign(x)*p["cheek_volume"]*cheek
    dist=np.linalg.norm(q-v,axis=1)
    return q.astype(np.float32),{
        "max_change_scene_units":float(dist.max()),
        "moved_vertices_gt_0p02":int((dist>.02).sum()),
        "rear_mask_vertices_gt_0p45":int((rear*low*lock>.45).sum())}

def local_taubin(v,faces,amount):
    x,y,z=v[:,0],v[:,1],v[:,2]
    w=(smoothstep(.35,.56,np.abs(x))*smoothstep(-.46,-.22,y)
       *(1-smoothstep(.26,.57,y))*(1-smoothstep(.32,.55,z))
       *smoothstep(-.68,-.45,y))
    a,b,c=faces[:,0],faces[:,1],faces[:,2]
    ids=np.concatenate([a,b,b,c,c,a])
    neighbors=np.concatenate([b,a,c,b,a,c])
    degree=np.bincount(ids,minlength=len(v)).astype(float)
    before=v.astype(np.float64)
    moved=before.copy()
    for _ in range(8):
        for alpha in (.48,-.50):
            avg=np.zeros_like(moved)
            np.add.at(avg,ids,moved[neighbors])
            avg/=np.maximum(degree[:,None],1)
            moved+=alpha*amount*w[:,None]*(avg-moved)
    return moved.astype(np.float32),float(np.linalg.norm(moved-before,axis=1).max())

def variant(raw,p,out,label):
    doc,buf=parse(raw);original,origbuf=parse(raw)
    assert len(doc["meshes"])==8
    changes={}
    for idx in (0,1):
        prim=doc["meshes"][idx]["primitives"][0]
        pos=access(doc,buf,prim["attributes"]["POSITION"])
        v,info=sculpt(pos.copy(),p)
        if idx==0:
            faces=access(doc,buf,prim["indices"]).reshape(-1,3)
            v,shift=local_taubin(v,faces,p["wing_smoothing"])
            info["local_taubin_max_change"]=shift
        pos[:]=v
        set_normals(doc,buf,idx)
        changes[str(idx)]=info
    for idx in range(8):
        a=original["meshes"][idx]["primitives"][0]
        b=doc["meshes"][idx]["primitives"][0]
        assert np.array_equal(access(original,origbuf,a["indices"]),
                              access(doc,buf,b["indices"]))
        for prop in ("COLOR_0","TEXCOORD_0"):
            if prop in a["attributes"]:
                assert np.array_equal(access(original,origbuf,a["attributes"][prop]),
                                      access(doc,buf,b["attributes"][prop]))
        if idx>=2:
            for prop in ("POSITION","NORMAL"):
                assert np.array_equal(access(original,origbuf,a["attributes"][prop]),
                                      access(doc,buf,b["attributes"][prop]))
    new=pack(doc,buf)
    name=f"run243_variant{label}_genuine_neural_rump_tail_ART_REJECTED_NO_RELEASE.glb"
    target=out/name;target.write_bytes(new)
    scene=trimesh.load(target,force="scene")
    assert len(scene.geometry)==8
    faces=sum(len(g.faces) for g in scene.geometry.values())
    assert faces==86867
    assert all(np.isfinite(g.vertices).all() for g in scene.geometry.values())
    return {"file":name,"sha256":sha(new),"bytes":len(new),
            "genuine_neural_mesh_count":8,"real_triangles":faces,
            "all_original_eye_geometry_and_UVs_preserved":True,
            "parameters":p,"deformation":changes}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",required=True)
    ap.add_argument("--outdir",required=True)
    args=ap.parse_args()
    raw=Path(args.source).read_bytes()
    assert sha(raw)==PIN,"Pinned real neural source mismatch"
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    parameters={
      "C":{"tail_lift":.18,"tail_retract":.20,"wing_fold_up":.10,
           "wing_fold_forward":.10,"rump_fullness":.035,
           "cheek_volume":.022,"wing_smoothing":.72},
      "D":{"tail_lift":.31,"tail_retract":.28,"wing_fold_up":.16,
           "wing_fold_forward":.16,"rump_fullness":.05,
           "cheek_volume":.03,"wing_smoothing":1.0}}
    report={"run":"Run243","status":"TWO_TRUE_NEURAL_GLBS_CREATED_PENDING_BROWSER_ART_REVIEW",
        "source_sha256":PIN,"art_approved":False,"release":"NO_RELEASE",
        "phone_webgl":"NOT_TESTED","external_paid_usd":0,"variants":{}}
    for name,p in parameters.items():report["variants"][name]=variant(raw,p,out,name)
    (out/"run243_machine_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":main()
