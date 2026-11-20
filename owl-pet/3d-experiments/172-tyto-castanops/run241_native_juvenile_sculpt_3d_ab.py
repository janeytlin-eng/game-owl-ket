#!/usr/bin/env python3
"""Run241 authentic neural-mesh compact juvenile and wing-surface sculpt A/B.
Edits the native Hunyuan learned mesh, never assembles an owl from geometric primitives.
All outputs are RESEARCH ONLY and MUST NOT be deployed before independent art review.
"""
import argparse, hashlib, json, struct
from pathlib import Path
import numpy as np
import trimesh
from run239_neural_silhouette_ab_trial import access, set_normals

SOURCE="71cc6ad479479008d79f7eaa0dd375aedd46d691ae1c493d949f9fcb5a9bb121"
def sha(b):return hashlib.sha256(b).hexdigest()
def unpack(b):
    assert b[:4]==b"glTF" and struct.unpack_from("<II",b,4)==(2,len(b))
    jl,kind=struct.unpack_from("<I4s",b,12);assert kind==b"JSON"
    doc=json.loads(b[20:20+jl]);bl,typ=struct.unpack_from("<I4s",b,20+jl)
    assert typ==b"BIN\x00" and 28+jl+bl==len(b)
    return doc,bytearray(b[28+jl:])
def juvenile_warp(v,p):
    q=v.astype(np.float64).copy()
    x,y,z=q[:,0].copy(),q[:,1].copy(),q[:,2].copy()
    # Keep the developed heart mask and eye points anchored; compact the bulky young torso.
    below=np.clip((.33-y)/1.25,0,1)
    q[:,1]+=p["compact_y"]*below
    torso=np.exp(-((y+.17)/.45)**4)*np.clip((.42-z)/.42,0,1)
    q[:,0]*=1+p["body_breadth"]*torso
    # Bring the long rear taper toward a short concealed mesoptile tail.
    tail=np.clip((-z-.10)/.65,0,1)**1.5 * np.exp(-((y+.4)/.65)**2)
    q[:,2]+=p["hide_tail"]*tail
    assert np.isfinite(q).all()
    return q.astype(np.float32)
def soften_wing_ridges(v,faces,strength):
    # Only soften fold-wing ridges of the learned sculpt, not eyes/head/feet or body silhouette.
    original=v.copy()
    av=np.abs(v[:,0]);y=v[:,1];z=v[:,2]
    envelope=np.clip((av-.32)/.25,0,1)*np.exp(-((y+.09)/.39)**4)*np.clip((.59-z)/.65,0,1)
    for iteration in range(3):
        sums=np.zeros_like(v,dtype=np.float64)
        degree=np.zeros(len(v),dtype=np.int32)
        triangles=faces
        for a,b in ((0,1),(1,2),(2,0)):
            u=triangles[:,a];w=triangles[:,b]
            np.add.at(sums,u,v[w]);np.add.at(sums,w,v[u])
            np.add.at(degree,u,1);np.add.at(degree,w,1)
        avg=sums/np.maximum(degree[:,None],1)
        v=v + (avg-v)*np.clip(strength*envelope,0,.5)[:,None]
    maxmove=np.max(np.linalg.norm(v-original,axis=1))
    return v.astype(np.float32),float(maxmove)
def run(raw, out, variant, p):
    doc,buf=unpack(raw)
    original_doc,original_buf=unpack(raw)
    assert len(doc["meshes"])==8
    maxmoves={}
    for i in (0,1):
        prim=doc["meshes"][i]["primitives"][0]
        pos=access(doc,buf,prim["attributes"]["POSITION"])
        before=pos.copy()
        pos[:]=juvenile_warp(before,p)
        if i==0:
            faces=access(doc,buf,prim["indices"]).reshape(-1,3)
            modified,smove=soften_wing_ridges(pos.copy(),faces,p["wing_soften"])
            pos[:]=modified
            maxmoves["actual_core_foldwing_softening"]=round(smove,5)
        maxmoves["actual_mesh_"+str(i)+"_warp"]=round(float(np.linalg.norm(pos-before,axis=1).max()),5)
        set_normals(doc,buf,i)
    for i in range(8):
        a=original_doc["meshes"][i]["primitives"][0]
        b=doc["meshes"][i]["primitives"][0]
        assert np.array_equal(access(original_doc,original_buf,a["indices"]),access(doc,buf,b["indices"]))
        for name in ("COLOR_0","TEXCOORD_0"):
            if name in a["attributes"]:
                assert np.array_equal(access(original_doc,original_buf,a["attributes"][name]),access(doc,buf,b["attributes"][name])),(i,name)
        if i>=2:
            for name in ("POSITION","NORMAL"):
                assert np.array_equal(access(original_doc,original_buf,a["attributes"][name]),access(doc,buf,b["attributes"][name])),(i,name)
    encoded=json.dumps(doc,separators=(",",":"),ensure_ascii=False).encode()
    encoded+=b" "*((-len(encoded))%4)
    glb=struct.pack("<4sII",b"glTF",2,12+8+len(encoded)+8+len(buf))
    glb+=struct.pack("<I4s",len(encoded),b"JSON")+encoded+struct.pack("<I4s",len(buf),b"BIN\x00")+buf
    target=out/f"run241_variant{variant}_true_neural_squat_mesoptile_ART_REJECTED_NO_RELEASE.glb"
    target.write_bytes(glb)
    scene=trimesh.load(str(target),force="scene")
    assert len(scene.geometry)==8 and sum(len(m.faces) for m in scene.geometry.values())==86867
    assert all(np.isfinite(m.vertices).all() and m.bounds is not None for m in scene.geometry.values())
    return {"file":target.name,"bytes":len(glb),"sha256":sha(glb),"parameters":p,
      "native_learned_meshes":8,"real_3d_triangles":86867,"nonrigid_real_3d_changes":maxmoves,
      "learned_owl_eyes_unchanged":True,"true_alpha_down_uv_and_png_unchanged":True}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--source",required=True);ap.add_argument("--outdir",required=True)
    a=ap.parse_args();raw=Path(a.source).read_bytes();assert sha(raw)==SOURCE
    out=Path(a.outdir);out.mkdir(parents=True,exist_ok=True)
    params={"A":{"compact_y":.12,"body_breadth":.17,"hide_tail":.13,"wing_soften":.25},
            "B":{"compact_y":.19,"body_breadth":.26,"hide_tail":.23,"wing_soften":.40}}
    summary={"run":"Run241","release":"NO_RELEASE","art_pass":False,"physical_phone_webgl":"UNTESTED",
      "extra_paid_usd":0,"source_sha256":sha(raw),
      "method":"real neural sculpt body compression, local foldwing smoothing and concealed tail on native POSITION/NORMAL, preserve learned mesh and textured fur","variants":{}}
    for variant,p in params.items():
        summary["variants"][variant]=run(raw,out,variant,p)
    summary["status"]="TWO_NATIVE_3D_SCULPT_VARIANTS_GENERATED_ART_PENDING_NO_RELEASE"
    (out/"run241_machine_report.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps(summary,indent=2))
if __name__=="__main__":main()
