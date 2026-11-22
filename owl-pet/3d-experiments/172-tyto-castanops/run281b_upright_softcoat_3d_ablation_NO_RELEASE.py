#!/usr/bin/env python3
"""#172 Run281b: true TripoSR mesh axis normalization and cream-coat Taubin ablation.
Research-only. Never create surrogate geometry or claim art or phone pass.
Both variants are genuine transforms of the exact original Run281 real MIT TripoSR GLB.
"""
import pathlib,hashlib,json,sys
import numpy as np
import trimesh
from run281_triposr_cpu_juvenile_reference_NO_RELEASE import qa,sha

SOURCE_SHA="be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117"
def main(src,dest):
    src=pathlib.Path(src);dest=pathlib.Path(dest);dest.mkdir(parents=True,exist_ok=True)
    assert sha(src)==SOURCE_SHA, "Wrong source: no substitute mesh is allowed"
    base=trimesh.load(src,force="scene")
    meshes=list(base.geometry.values())
    assert len(meshes)==1 and len(meshes[0].faces)==103084
    T=np.eye(4)
    # TripoSR raw owlet is lying on its side under glTF Y-up conventions.
    # Map original x,y,z -> new y,z,x; proper (det=+1) spatial rotation.
    T[:3,:3]=[[0,1,0],[0,0,1],[1,0,0]]
    assert round(np.linalg.det(T[:3,:3]))==1
    base.apply_transform(T)
    p1=dest/"upright_raw_TRUE3D_NO_RELEASE.glb"
    p1.write_bytes(trimesh.exchange.gltf.export_glb(base))
    qa(p1,dest/"raw_upright_six_views")
    # Alternate treatment: preserve facial disc/eyes, smooth ONLY existing geometry
    # under graded field and paint torso warm cream; no invented 3D primitives.
    alt=trimesh.load(p1,force="scene")
    m=next(iter(alt.geometry.values()))
    v0=m.vertices.copy();c0=m.visual.vertex_colors.copy()
    trimesh.smoothing.filter_taubin(m,lamb=.5,nu=.53,iterations=10)
    filtered=m.vertices.copy()
    x,y,z=v0.T
    sigmoid=lambda t:1/(1+np.exp(-np.clip(t,-25,25)))
    protected=sigmoid(22*(z-.07))*sigmoid(15*(y+.025))*sigmoid(18*(.285-np.abs(x)))
    weight=1-.98*protected
    m.vertices=v0+(filtered-v0)*weight[:,None]
    luma=.2126*c0[:,0]+.7152*c0[:,1]+.0722*c0[:,2]
    light=np.clip((luma-110)*.10,-12,12)
    cream=np.stack([241+light,228+light,211+light],axis=-1)
    feet=sigmoid(45*(-.365-y))
    retain=np.maximum(protected,feet*.78)
    outcols=np.clip(np.rint(cream*(1-retain[:,None])+c0[:,:3]*retain[:,None]),0,255).astype(np.uint8)
    m.visual.vertex_colors=np.column_stack([outcols,np.full(len(outcols),255,np.uint8)])
    p2=dest/"upright_taubin10_cream_TRUE3D_NO_RELEASE.glb"
    p2.write_bytes(trimesh.exchange.gltf.export_glb(alt))
    qa(p2,dest/"cream_taubin10_six_views")
    r={"source_sha256":sha(src),"source_triangles":len(meshes[0].faces),
       "source_vertices":len(meshes[0].vertices),
       "transform":"[x,y,z] -> [y,z,x]; correct handedness det +1",
       "smoothing":"Taubin 10 iterations, face/eye protected graded blend",
       "source_genuine_TripoSR_mesh_not_primitives":True,
       "mean_unblended_smooth_displacement":float(np.linalg.norm(filtered-v0,axis=1).mean()),
       "variant_files":{p.stem:{"bytes":p.stat().st_size,"sha256":sha(p),
       "faces":sum(len(m.faces) for m in trimesh.load(p,force="scene").geometry.values())}
       for p in [p1,p2]},
       "six_different_camera_angles_each":True,
       "art_review":"PENDING_REAL_IMAGE_REVIEW / NO_RELEASE",
       "phone_webgl":"NOT_TESTED",
       "rights":"MIT TripoSR; original concept source rights must still be evaluated",
       "release":False}
    assert all(x["faces"]==103084 for x in r["variant_files"].values())
    (dest/"run281b_native_transform_ablation_QA.json").write_text(json.dumps(r,indent=2))
    print(json.dumps(r,indent=2))
if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])
