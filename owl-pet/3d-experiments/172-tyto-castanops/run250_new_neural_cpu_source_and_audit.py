#!/usr/bin/env python3
"""Run250: strict reproducible v3 far-right mesoptile crop + native TripoSR output audit.
Research-only. Never equate a generated GLB with art approval.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import trimesh
from PIL import Image

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def prepare(source, out):
    src=Path(source)
    assert src.is_file(), src
    with Image.open(src) as im:
        image=im.convert("RGB")
    w,h=image.size
    assert (w,h)==(1536,1024), f"Unexpected #172 v3 plate: {w}x{h}; crop needs visual review"
    # Last bird only; visually checked original plate: subject spans approx x956..1360 and y289..842; adult female and bottom captions excluded.
    # No synthetic 2D bird geometry is introduced. Background separation is
    # delegated to an independent free IS-Net segmentation model.
    box=(956,250,1435,880)
    crop=image.crop(box)
    # A modest neutral border avoids touching feathers at the crop boundaries.
    canvas=Image.new("RGB",(crop.width+112,crop.height+112),(127,127,127))
    canvas.paste(crop,(56,56))
    out.mkdir(parents=True,exist_ok=True)
    p=out/"run250_v3_right_mesoptile_input_UNMASKED_RESEARCH.png"
    canvas.save(p)
    report={"run":"Run250","source":str(src),"source_sha256":sha(src),
        "full_plate_px":[w,h],"crop_box_xyxy":list(box),
        "input_file":p.name,"input_sha256":sha(p),
        "input_px":list(canvas.size),
        "selection_note":"v3 far-right owl plus some original scenery; automatic IS-Net background segmentation may leave bark; do not claim isolated subject without visual review",
        "purpose":"new MIT TripoSR neural base, rather than further warping adult remiges",
        "art_approved":False,"physical_phone_gpu":"UNTESTED","release":"NO_RELEASE"}
    (out/"run250_input_provenance.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

def audit(glb,out):
    p=Path(glb)
    assert p.is_file(), f"No actual neural GLB: {p}"
    data=p.read_bytes()
    assert data[:4]==b"glTF", "Not an authentic binary glTF"
    scene=trimesh.load(p,force="scene")
    meshes=list(scene.geometry.values())
    vertices=sum(len(g.vertices) for g in meshes)
    triangles=sum(len(g.faces) for g in meshes)
    bounds=scene.bounds
    spans=np.diff(bounds,axis=0)[0]
    valid=bool(len(meshes)>0 and triangles>2000 and vertices>1000
               and np.isfinite(bounds).all() and np.min(spans)>0.12)
    audit={"run":"Run250","backend":"shapestudio 0.1.7 vendored MIT TripoSR CPU",
           "source_kind":"new neural image-to-3D reconstruction; not inherited adult Hunyuan wing deformation",
           "glb_file":p.name,"bytes":len(data),"sha256":sha(p),"mesh_count":len(meshes),
           "vertices":vertices,"triangles":triangles,"bounds":bounds.round(6).tolist(),
           "spans":spans.round(6).tolist(),"basic_native_geometry_pass":valid,
           "face_disc_correctness":"UNREVIEWED","plumulaceous_down":"UNREVIEWED",
           "anatomical_wing_and_tail":"UNREVIEWED","side_back_consistency":"UNREVIEWED",
           "phone_webgl":"UNTESTED","art_approved":False,"release":"NO_RELEASE"}
    (out/"run250_neural_machine_report.json").write_text(json.dumps(audit,indent=2)+"\n")
    print(json.dumps(audit,indent=2))
    assert valid, "New mesh failed native geometry gate; no release"

if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("stage",choices=["prepare","audit"])
    a.add_argument("--source")
    a.add_argument("--glb")
    a.add_argument("--outdir",required=True)
    args=a.parse_args()
    out=Path(args.outdir);out.mkdir(exist_ok=True,parents=True)
    if args.stage=="prepare":
        assert args.source
        prepare(args.source,out)
    else:
        assert args.glb
        audit(args.glb,out)
