#!/usr/bin/env python3
"""Ablate real glTF groom material against same unmodified v30 sculpt.
Diagnostic, NOT a pet model or new artistic approval."""
import hashlib, json, sys
from pathlib import Path
import trimesh

source=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
variants={}
for label in ["BLEND_original","MASK_alpha","NO_GROOM"]:
    scene=trimesh.load(source,force="scene",process=False)
    name="soft_alpha_mesoptile_research_groom"
    assert name in scene.geometry, "Groom geometry absent; ablation invalid"
    if label=="NO_GROOM":
        scene.delete_geometry(name)
    elif label=="MASK_alpha":
        groom=scene.geometry[name]
        assert groom.visual.kind=="texture"
        groom.visual.material.alphaMode="MASK"
        groom.visual.material.alphaCutoff=0.19
        groom.visual.material.doubleSided=True
    target=out/(label+".glb")
    scene.export(target)
    check=trimesh.load(target,force="scene",process=False)
    assert ("soft_alpha_mesoptile_research_groom" in check.geometry)==(label!="NO_GROOM")
    variants[label]={"path":str(target),"bytes":target.stat().st_size,
                     "sha256":hashlib.sha256(target.read_bytes()).hexdigest(),
                     "triangles":sum(len(g.faces) for g in check.geometry.values()),
                     "groom_material":check.geometry[name].visual.material.alphaMode if label!="NO_GROOM" else "REMOVED",
                     "meshes":len(check.geometry)}
(out/"ablation_manifest.json").write_text(json.dumps(variants,indent=2))
print(json.dumps(variants,indent=2))
