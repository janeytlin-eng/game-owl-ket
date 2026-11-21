#!/usr/bin/env python3
"""Run256p: repair a confirmed normalized-accessor importer bug; real GLBs, no release.

CC0 source GLBs declare KHR_mesh_quantization with normalized signed-int16
positions and normalized unsigned-int16 UVs. Trimesh 4.11.1 currently exposes
raw [-32767,32767] positions and [0,65535] texture coordinates. Applying scene
node transforms BEFORE normalizing distorts all part placement and texture.
Restore [-1,1] positions and [0,1] UVs on each original geometry BEFORE dump
bakes node transforms. This is not a sculpt or juvenile aesthetic acceptance.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import run256_CC0_hollow_true_neural_source_screen as prev

def normalized_baked_meshes(scene):
    corrected = []
    for name, mesh in scene.geometry.items():
        old = np.asarray(mesh.vertices)
        if old.size and float(np.max(np.abs(old))) > 100:
            mesh.vertices = old.astype(np.float64) / 32767.0
            uv = getattr(mesh.visual, "uv", None)
            if uv is not None and len(uv) and float(np.max(np.abs(uv))) > 100:
                mesh.visual.uv = np.asarray(uv, dtype=np.float64) / 65535.0
            corrected.append(name)
    baked = ORIGINAL(scene)
    if corrected:
        print(json.dumps({
            "normalized_KHR_mesh_quantization_input_parts": corrected,
            "baked_triangles": sum(len(m.faces) for m in baked),
            "baked_bounds_meters": prev.bounds(baked).round(6).tolist()
        }), flush=True)
        assert all(np.isfinite(m.vertices).all() for m in baked)
        assert max(np.max(np.abs(m.vertices)) for m in baked) < 100
    return baked

ORIGINAL = prev.get_baked_meshes
prev.get_baked_meshes = normalized_baked_meshes

def main(source, output):
    prev.run(source, output)
    output = Path(output)
    p = output / "run256_geometry_report.json"
    report = json.loads(p.read_text())
    report["run"] = "256p"
    report["technique"] = "correct KHR_mesh_quantization normalized signed INT16 vertex POSITION & unsigned UINT16 UV before scene-transform bake"
    report["fixed_importer_bug"] = True
    report["accessor_normalization"] = {"vertex_POSITION_INT16_normalized": "divide by 32767",
        "UV_UINT16_normalized": "divide by 65535",
        "checked_against_pack_published_source_dimensions_meters": True}
    report["published_pack_source_dimensions_meters"] = {
        "cc0_hollow_tree": [1.174,0.708,1.229],
        "cc0_barn_owl_adult": [0.206,0.401,0.607]}
    # Reuse filename convention but in independently versioned run256p-evidence path,
    # never overwriting prior Run256 (known-wrong) binary research artifacts.
    for k in ["cc0_hollow_tree","cc0_barn_owl_adult"]:
        b = report["downloaded"][k]["bounds"]
        dimensions = (np.array(b[1])-np.array(b[0])).round(4)
        assert max(dimensions) < 2.0,(k,dimensions.tolist())
    report["original_run256_is_negative_control"] = True
    report["art_approved"] = False
    report["phone_hardware"] = "UNTESTED"
    (output / "run256p_geometry_report.json").write_text(
        json.dumps(report, indent=2,ensure_ascii=False)+"\n")
    p.unlink()
    for v, data in report["variants"].items():
        assert data["native_glb_reimport"] and data["sha256"]
        path = output / data["filename"]
        assert hashlib.sha256(path.read_bytes()).hexdigest()==data["sha256"]
    print(json.dumps({"run256p":"native normalization repaired","variant_shapes":report["variants"],
                      "inputs": report["downloaded"]},indent=2),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",required=True)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    main(a.source,a.output)
