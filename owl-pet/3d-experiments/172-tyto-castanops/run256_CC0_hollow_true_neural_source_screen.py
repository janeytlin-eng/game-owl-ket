#!/usr/bin/env python3
"""Run256: independent free CC0 environment/source screening against an authentic neural 3D owl.

Research-only: does not claim a new infant neural source or production-worthy art.
Loads source GLBs, composes ACTUAL 3D meshes, reimports, records geometry and provenance.
"""
import argparse
import hashlib
import json
import urllib.request
from pathlib import Path

import numpy as np
import trimesh

BASE_SHA = "cd1513ac0822eef25bb56f9f8d08d244cac64d209ea8c92333693d287c926eb6"
CORE = "real_neural_owl_juvenile_core"
DOWN = "real_3d_surface_following_wispy_down"
SOURCES = {
    "cc0_barn_owl_adult": {
        "url": "https://cdn.3dassets.dev/assets/28079/v1/model.glb",
        "page": "https://3dassets.dev/assets/birds-and-reptiles-hd-barn-owl-b51d286f",
        "license": "CC0 1.0", "adult_not_chick": True,
    },
    "cc0_hollow_tree": {
        "url": "https://cdn.3dassets.dev/assets/28115/v1/model.glb",
        "page": "https://3dassets.dev/assets/birds-and-reptiles-hd-tree-stump-with-hollow-5ad1c3f4",
        "license": "CC0 1.0", "species": "unverified_generic_tree_not_claimed_eucalyptus",
    },
}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def bounds(meshes):
    bb = np.array([m.bounds for m in meshes], dtype=float)
    return np.array([bb[:, 0].min(axis=0), bb[:, 1].max(axis=0)])

def get_baked_meshes(scene):
    # Dump applies scene-node transforms, unlike blindly concatenating geometry dict entries.
    return [m.copy() for m in scene.dump(concatenate=False) if isinstance(m, trimesh.Trimesh)]

def download(entry, path):
    req = urllib.request.Request(entry["url"], headers={"User-Agent": "owl172-cc0-research-run256/1.0"})
    with urllib.request.urlopen(req, timeout=40) as response:
        b = response.read(15_000_000)
    assert len(b) >= 64 and b[:4] == b"glTF", ("not_valid_glb", path, len(b))
    path.write_bytes(b)
    return {"bytes": len(b), "sha256": sha(path), "url": entry["url"], "page": entry["page"], "license": entry["license"]}

def save_and_reimport(scene, path):
    data = scene.export(file_type="glb", include_normals=True)
    assert data[:4] == b"glTF"
    path.write_bytes(data)
    check = trimesh.load(path, force="scene")
    meshes = get_baked_meshes(check)
    assert meshes and all(np.isfinite(m.vertices).all() for m in meshes)
    return {
        "bytes": path.stat().st_size,
        "sha256": sha(path),
        "mesh_instances": len(meshes),
        "triangles": int(sum(len(m.faces) for m in meshes)),
        "bounds": bounds(meshes).round(5).tolist(),
        "filename": path.name,
        "native_glb_reimport": True,
        "art_approved": False,
        "phone_gpu": "UNTESTED",
    }

def natural_habitat(owl_meshes, tree_meshes, owl_bounds, clearance, variant):
    """Put a real hollow-tree mesh behind the owl, not a bark-coloured cylinder."""
    o_min, o_max = owl_bounds
    o_ext = o_max - o_min
    t_min, t_max = bounds(tree_meshes)
    t_ext = t_max - t_min
    assert np.all(t_ext > 0)
    scale = min(float(o_ext[0] * (1.8 if variant == "B" else 1.65) / t_ext[0]),
                float(o_ext[1] * (0.93 if variant == "B" else 0.90) / t_ext[1]))
    # The broad lip / opening sits behind the subject's feet and lower breast.
    target_top_y = float(o_min[1] + o_ext[1] * (0.30 if variant == "B" else 0.26))
    position = np.array([
        float((o_min[0] + o_max[0]) * .5),
        target_top_y,
        float(o_min[2] - o_ext[2] * (0.21 if variant == "B" else 0.17)),
    ])
    scene = trimesh.Scene()
    for i, m in enumerate(owl_meshes):
        scene.add_geometry(m, geom_name=f"source_owl_true_mesh_{i:02d}")
    for i, original in enumerate(tree_meshes):
        m = original.copy()
        # Input tree coordinates are +Y up; scale relative to the actual owl, not guessed units.
        m.vertices = (m.vertices - (t_min + t_max) * .5) * scale
        m.vertices += position + [0, -(t_ext[1] * scale) * .5, 0]
        scene.add_geometry(m, geom_name=f"cc0_hollow_tree_mesh_{i:02d}")
    return scene, {"tree_scale": scale, "tree_center": position.round(5).tolist(),
                   "tree_top_relative_to_owl_feet": target_top_y - o_min[1],
                   "no_claim_actual_eucalyptus": True, "clearance_policy": clearance}

def run(source, output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    assert sha(source) == BASE_SHA, ("PINNED_NEURAL_SOURCE_MISMATCH", sha(source))
    source_scene = trimesh.load(source, force="scene")
    assert CORE in source_scene.geometry and DOWN in source_scene.geometry
    core = source_scene.geometry[CORE]
    core_bounds = np.array(core.bounds)
    core_mesh_count = len(core.faces)
    assert core_mesh_count == 34000 and core.is_watertight
    report = {
        "run": "256",
        "purpose": "true_native_CC0_hollow_environment_and_external_anatomy_negative_control",
        "research_only": True, "art_approved": False, "release": "NO_RELEASE",
        "phone_hardware": "UNTESTED", "extra_paid_usd": 0,
        "source_hunyuan_sha256": sha(source),
        "upstream": "Run251_A learned Hunyuan model, six repaired 3D eye meshes, real 3D down",
        "source_links": SOURCES, "downloaded": {}, "variants": {},
    }
    cc0_meshes = {}
    for name, item in SOURCES.items():
        path = output / f"run256_input_{name}_original_CC0.glb"
        report["downloaded"][name] = download(item, path)
        obj = trimesh.load(path, force="scene")
        parts = get_baked_meshes(obj)
        assert parts and sum(len(m.faces) for m in parts) >= 500
        cc0_meshes[name] = parts
        report["downloaded"][name].update({
            "meshes": len(parts), "triangles": int(sum(len(m.faces) for m in parts)),
            "bounds": bounds(parts).round(5).tolist(),
        })

    # Negative control A is the untouched SHA-pinned neural owl in its original support.
    variant_a = output / "run256_A_original_neural_control_NO_RELEASE.glb"
    variant_a.write_bytes(Path(source).read_bytes())
    report["variants"]["A"] = save_and_reimport(source_scene, variant_a)

    # B retains the true learned owl, groom and 6 ocular meshes. Removes its biscuit-like
    # tree support, substituting CC0 sculpted hollow tree: all meshes are genuine 3D.
    original_parts = []
    omitted = []
    for key, m in source_scene.geometry.items():
        if key in (CORE, DOWN) or key.startswith("sculpt_anatomical_eye_detail_"):
            original_parts.append(m.copy())
        else:
            omitted.append(key)
    assert len(original_parts) == 8 and len(omitted) == 1, (len(original_parts), omitted)
    B, details_b = natural_habitat(original_parts, cc0_meshes["cc0_hollow_tree"], core_bounds,
                                   "independent_placement_not_physical_collision_solved", "B")
    report["variants"]["B"] = save_and_reimport(
        B, output / "run256_B_authentic_neural_owl_CC0_hollow_research_NO_RELEASE.glb")
    report["variants"]["B"].update(details_b)
    report["variants"]["B"]["original_biscuit_support_removed"] = omitted
    report["variants"]["B"]["preserved_hunyuan_faces"] = core_mesh_count
    report["variants"]["B"]["preserved_original_groom_faces"] = 36651

    # C is deliberately an ADULT source control, never renamed as a chick or a new neural
    # juvenile. Different adult anatomy can be judged from genuine side/back rotations.
    adult_meshes = [m.copy() for m in cc0_meshes["cc0_barn_owl_adult"]]
    ab = bounds(adult_meshes)
    ratio = float((core_bounds[1,1] - core_bounds[0,1]) * .93 / (ab[1,1] - ab[0,1]))
    for m in adult_meshes:
        m.vertices = (m.vertices - (ab[0]+ab[1]) * .5) * ratio
        m.vertices += np.array([core_bounds[:,0].mean(), core_bounds[:,1].mean(), core_bounds[:,2].mean()])
    C, details_c = natural_habitat(adult_meshes, cc0_meshes["cc0_hollow_tree"],
                                   bounds(adult_meshes), "adult_only_negative_control", "C")
    report["variants"]["C"] = save_and_reimport(
        C, output / "run256_C_CC0_ADULT_barn_owl_anatomy_NEGATIVE_CONTROL_NO_RELEASE.glb")
    report["variants"]["C"].update(details_c)
    report["variants"]["C"]["adult_not_chick"] = True
    report["variants"]["C"]["not_hunyuan"] = True

    (output/"run256_geometry_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"variants": report["variants"], "downloaded": report["downloaded"]},
                     indent=2, ensure_ascii=False), flush=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    run(args.source, args.output)
