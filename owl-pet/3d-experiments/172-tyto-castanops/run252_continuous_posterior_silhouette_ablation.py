#!/usr/bin/env python3
"""Run252 negative-control research: invert-safe continuous posterior warp of an
existing Hunyuan native neural owl GLB with corrected real 3D eye materials.
This is NOT an authored juvenile. No release or main/production edits.
Y up; +Z front; original learned surface, PBR eyes, 3D down and tree retained.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import trimesh

PIN = "cd1513ac0822eef25bb56f9f8d08d244cac64d209ea8c92333693d287c926eb6"
CORE = "real_neural_owl_juvenile_core"
DOWN = "real_3d_surface_following_wispy_down"
EYE = "sculpt_anatomical_eye_detail_1"

def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def smooth(a, b, x):
    u = np.clip((x - a) / (b - a), 0, 1)
    return u*u*(3-2*u)

def deform(v, variant):
    """True nonrigid 3D cage field; cannot fabricate missing juvenile anatomy."""
    x, y, z = np.asarray(v).T.copy()
    lower = 1 - smooth(0.22, 0.58, y)
    rear = 1 - smooth(-0.50, 0.38, z)
    tail = lower*rear
    if variant == "C":
        dz, widen = 0.23*tail, 0.08
    elif variant == "D":
        dz, widen = 0.30*tail, 0.10
    elif variant == "E_REJECT_FLIP":
        dz, widen = 0.37*tail, 0.13
    else:
        raise ValueError(variant)
    # Protect the expensive learned front disc rather than reconstructing it.
    face = smooth(0.25, 0.48, y)*smooth(0.31, 0.55, z)
    dx = widen*lower*x*(1-smooth(0.36, 0.68, np.abs(x)))
    weight = 1-face
    return np.column_stack((x+dx*weight, y, z+dz*weight))

def check_scene(sc, original):
    assert len(sc.geometry) == len(original.geometry) == 9
    c, old = sc.geometry[CORE], original.geometry[CORE]
    assert c.is_watertight and c.volume > 1.0
    assert len(c.vertices) == len(old.vertices) and np.array_equal(c.faces, old.faces)
    assert all(np.isfinite(g.vertices).all() for g in sc.geometry.values())
    n, _ = trimesh.triangles.normals(c.triangles)
    n0, _ = trimesh.triangles.normals(old.triangles)
    flip = int(np.count_nonzero(np.sum(n*n0, axis=1) < 0))
    pbr = sc.geometry[EYE].visual.material
    assert pbr.baseColorFactor[0] < 20
    return dict(meshes=len(sc.geometry),
                triangles=int(sum(len(g.faces) for g in sc.geometry.values())),
                learned_core_triangles=len(c.faces),
                learned_core_volume=float(c.volume),
                core_inverted_triangles=flip,
                eye_pupil_dark_material=True,
                posterior_z_min=float(c.bounds[0,2]),
                max_learned_vertex_delta=float(np.linalg.norm(c.vertices-old.vertices, axis=1).max()),
                altered_core_vertex_count=int(np.count_nonzero(np.linalg.norm(c.vertices-old.vertices, axis=1) > 0.01)))

def main(src, outdir):
    src, outdir = Path(src), Path(outdir)
    assert sha256(src) == PIN, ("wrong true 3D source", sha256(src))
    outdir.mkdir(parents=True, exist_ok=True)
    original=trimesh.load(src, force="scene")
    report=dict(run="Run252", source_sha256=PIN, source_licence="original research mesh; no external donor",
        source_kind="actual native Hunyuan learned 3D GLB", y_up=True,
        objective="nonrigid silhouette control; reject when new hump or adult wing persists",
        physical_phone_gpu="UNTESTED", extra_paid_usd=0, art_approved=False,
        release="NO_RELEASE", variants={})
    for variant in ["C", "D", "E_REJECT_FLIP"]:
        scene=trimesh.load(src,force="scene")
        scene.geometry[CORE].vertices=deform(scene.geometry[CORE].vertices.copy(), variant)
        scene.geometry[DOWN].vertices=deform(scene.geometry[DOWN].vertices.copy(), variant)
        facts=check_scene(scene,original)
        if facts["core_inverted_triangles"] != 0:
            facts.update(status="GEOMETRY_REJECTED", art_approved=False)
            report["variants"][variant]=facts
            print(variant, "REJECT core inversion",facts["core_inverted_triangles"],flush=True)
            continue
        assert facts["max_learned_vertex_delta"] > 0.05
        out=outdir/f"run252_{variant}_real_neural_silhouette_GLb_ART_UNAPPROVED_NO_RELEASE.glb"
        out.write_bytes(scene.export(file_type="glb",include_normals=True))
        reloaded=trimesh.load(out,force="scene")
        assert check_scene(reloaded,original)["core_inverted_triangles"] == 0
        facts.update(file=out.name, bytes=out.stat().st_size, sha256=sha256(out),
                     status="TRUE_NATIVE_MESH_PASS_ART_PENDING",art_approved=False,
                     renderer="browser QA required; not validated here")
        report["variants"][variant]=facts
        print(variant, json.dumps(facts), flush=True)
    assert set(report["variants"])=={"C","D","E_REJECT_FLIP"}
    assert report["variants"]["E_REJECT_FLIP"]["status"]=="GEOMETRY_REJECTED"
    (outdir/"run252_geometry_report.json").write_text(json.dumps(report,indent=2)+"\n")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--source",required=True)
    p.add_argument("--outdir",required=True)
    a=p.parse_args()
    main(a.source,a.outdir)
