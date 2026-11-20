#!/usr/bin/env python3
"""Run246: correct Y-up orientation and sculpt a naturally fractured horizontal eucalyptus ledge.

Previous Run245/245b implicitly treated Z as the world's vertical axis. However the
verified Three.js viewer uses camera.up=(0,1,0) and front=(0,0,1), so an upright
hollow ring was expected. This independent experiment fixes the axis contract,
derives dimensions from a SHA-pinned learned 3-D owl, creates two genuinely
volumetric marching-cubes ledge alternatives, and records strict NO_RELEASE.
It does not replace the Hunyuan owl, the production line, or its materials.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import scipy.ndimage as ndi
from scipy.spatial import cKDTree
from skimage.measure import marching_cubes
import trimesh

SOURCE_SHA256 = "19274685ed19bb4c61b36a55b09048649a3db5c691aff2d75b1fe33831abf1ee"
CORE = "real_neural_owl_juvenile_core"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def make_ledge(core_vertices, variant, pitch=0.026):
    """No upright ring: carved horizontal XY-height-wise support with true 3D relief.

    The learned owl is left untouched. X=left/right, Y=UP, Z=front/back, exactly
    as configured in the actual Three.js renderer. Variation is only in the
    separate environmental support, not fake procedural bird parts.
    """
    box = np.array([core_vertices.min(axis=0), core_vertices.max(axis=0)])
    spread = box[1] - box[0]
    cx, cy, cz = (box[0] + box[1]) * .5
    low_y = float(np.quantile(core_vertices[:, 1], .004))
    rx = max(.92, spread[0] * (.79 if variant == "A" else .84))
    rz = max(.78, spread[2] * (.68 if variant == "A" else .75))
    depth = max(.38, spread[1] * (.235 if variant == "A" else .25))
    y_top = low_y + .024 * spread[1]
    xx = np.arange(cx - 1.22 * rx, cx + 1.22 * rx, pitch, dtype=np.float32)
    yy = np.arange(y_top - depth - .16, y_top + .15, pitch, dtype=np.float32)
    zz = np.arange(cz - 1.22 * rz, cz + 1.22 * rz, pitch, dtype=np.float32)
    x, y, z = np.meshgrid(xx, yy, zz, indexing="ij", sparse=True)
    u = (x-cx)/rx
    v = (z-cz)/rz
    angle = np.arctan2(v, u)
    rho = (np.abs(u)**4.3 + np.abs(v)**4.3)**(1/4.3)
    rng = np.random.default_rng(246 if variant == "A" else 172246)
    noise_shape = (17, 9, 15)
    coarse = rng.normal(0, 1, noise_shape).astype("float32")
    expanded = ndi.zoom(coarse, tuple(n/k for n,k in zip(
        (len(xx),len(yy),len(zz)),noise_shape)), order=3)
    noise = expanded[:len(xx), :len(yy), :len(zz)]

    # Broken bark, twisting grain, asymmetrical natural edge. No tiled primitives.
    radial_relief = .057 * np.sin(9*angle + 5.5*y) + .033 * np.sin(23*angle-3*y)
    radial_relief += .020 * noise
    side_field = 1.0 - rho + radial_relief

    # A long almost-horizontal lip with subtle hollowed inner wear and raised,
    # fractured rim. No obstructing back wall in the 360-degree view.
    bowl = (.038 if variant == "A" else .060) * spread[1] * np.exp(
        -.5*((u/.67)**2 + (v/.56)**2))
    rim = (.012 if variant == "A" else .018) * spread[1] * np.exp(
        -((rho-.81)/.13)**2)
    grain = .015 * np.sin(11*u+7*v) + .009 * np.cos(23*u-17*v)
    fine = .010 * np.sin(51*u + 17*v)
    top = y_top - bowl + rim + grain + fine
    under = y_top - depth + .026*np.sin(6*u+8*v) + .016*np.cos(20*u-3*v)
    shape_field = np.minimum(0.65 * side_field, np.minimum(
        3.8 * (top-y), 3.5 * (y-under)))
    shape_field = ndi.gaussian_filter(shape_field.astype(np.float32), sigma=.66)
    verts, faces, _, _ = marching_cubes(shape_field, level=0,
                                          spacing=(pitch,pitch,pitch))
    verts += np.array([xx[0],yy[0],zz[0]])
    ledge = trimesh.Trimesh(vertices=verts, faces=faces, process=False)
    ledge.fix_normals()

    vx, vy, vz = verts.T
    vu = (vx-cx)/rx
    vv = (vz-cz)/rz
    rr = (np.abs(vu)**4.3 + np.abs(vv)**4.3)**(1/4.3)
    a = np.arctan2(vv,vu)
    barkgrain = np.clip(.5 + .22*np.sin(20*a+4*vy)
                       + .18*np.cos(41*a-11*vy)
                       + .10*np.sin(8*vx+37*vz), 0, 1)
    # Warm cream sapwood on horizontal worn top; brown-grey bark on edges.
    exposed = np.clip((vy-(y_top-.06*spread[1]))/
                      max(.012,.040*spread[1]),0,1)
    exposed *= np.clip((1.06-rr)/.24,0,1)
    bark = np.stack([72+45*barkgrain, 55+38*barkgrain,
                     42+33*barkgrain], axis=1)
    wood = np.stack([157+33*barkgrain, 131+33*barkgrain,
                     99+27*barkgrain], axis=1)
    rgb = bark*(1-exposed[:,None]) + wood*exposed[:,None]
    colors = np.clip(np.c_[rgb,np.full(len(vx),255)],0,255).astype(np.uint8)
    mat = trimesh.visual.material.PBRMaterial(
        name="run246_weathered_eucalypt_worn_sapwood_nonmetallic",
        metallicFactor=0.0, roughnessFactor=.96,
        baseColorFactor=[255,255,255,255], doubleSided=True)
    vis = trimesh.visual.TextureVisuals(material=mat)
    vis.vertex_attributes["color"] = colors
    ledge.visual = vis

    assert ledge.is_watertight and len(ledge.faces) > 8000
    assert np.all(np.isfinite(ledge.vertices))
    assert len(ledge.vertex_normals) == len(ledge.vertices)
    # Core body above support: unlike Run245, the rear view cannot be occluded
    # by a tall upright 3D ring. In Three.js, Y is the up axis.
    assert ledge.bounds[1,1] < box[0,1] + .20*spread[1], "ledge obstructs body"
    return ledge, {
        "axes":"X=left-right, Y=vertical, Z=front-back",
        "variant":variant,
        "core_bounds":box.round(4).tolist(),
        "core_spread":spread.round(4).tolist(),
        "measured_core_lower_y_quantile_0p004":low_y,
        "support_surface_target_y":float(y_top),
        "grid":[len(xx),len(yy),len(zz)],
        "vertices":int(len(ledge.vertices)),
        "triangles":int(len(ledge.faces)),
        "watertight":bool(ledge.is_watertight),
        "support_bounds":ledge.bounds.round(4).tolist(),
        "support_y_top_minus_core_y_min":float(ledge.bounds[1,1]-box[0,1]),
        "core_height":float(spread[1])
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()
    output = Path(args.outdir)
    output.mkdir(parents=True, exist_ok=True)
    assert digest(args.source) == SOURCE_SHA256, "source learned 3D mesh SHA mismatch"
    pristine = trimesh.load(args.source, force="scene")
    assert len(pristine.geometry) == 8
    assert sum(len(g.faces) for g in pristine.geometry.values()) == 86867
    core = pristine.geometry[CORE]
    original = {n:(len(g.vertices),len(g.faces)) for n,g in pristine.geometry.items()}
    records=[]
    for variant in ("A","B"):
        scene = trimesh.load(args.source, force="scene")
        ledge, stat = make_ledge(core.vertices,variant)
        scene.add_geometry(ledge,geom_name="run246_authentic_Y_UP_horizontal_eucalypt_bark_ledge_"+variant)
        glb = output/("run246_"+variant+"_real_neural_owl_YUP_horizontal_ledge_RESEARCH_ART_UNAPPROVED.glb")
        scene.export(glb, include_normals=True)
        checked = trimesh.load(glb,force="scene")
        assert len(checked.geometry)==9
        assert all((len(checked.geometry[k].vertices),len(checked.geometry[k].faces))==v
                   for k,v in original.items())
        assert all(np.all(np.isfinite(mesh.vertices)) for mesh in checked.geometry.values())
        bird=checked.geometry[CORE]
        feet=bird.vertices[bird.vertices[:,1] <
                            np.quantile(bird.vertices[:,1],.06)]
        dist,_=cKDTree(ledge.vertices).query(feet,k=1)
        stat["low_y_core_points"]=int(len(feet))
        stat["low_y_near_support_fraction_0p1_units"]=float((dist<.1).mean())
        stat["minimum_distance_to_support"]=float(dist.min())
        stat["core_mesh_preserved"]=True
        stat["core_face_count"]=int(len(bird.faces))
        stat["source_hunyuan_true_3d_preserved"]=True
        stat["scene_meshes"]=len(checked.geometry)
        stat["scene_triangles"]=int(sum(len(m.faces) for m in checked.geometry.values()))
        stat["file"]=glb.name
        stat["bytes"]=glb.stat().st_size
        stat["sha256"]=digest(glb)
        stat["art_approved"]=False
        stat["phone_gpu"]="UNTESTED"
        stat["release"]="NO_RELEASE"
        records.append(stat)
    report={"run":"Run246",
            "cause_corrected":"Run245 treated Z as vertical although WebGL viewer uses Y up",
            "source_sha256":SOURCE_SHA256,
            "design_reference":"#172 v3 rightmost age-unknown cream mesoptile",
            "research_only":True,
            "extra_paid_usd":0,
            "tests":records,
            "no_release":True,
            "quality_status":"UNREVIEWED_PENDING_ACTUAL_SEVEN_VIEW_ART_AUDIT"}
    (output/"run246_machine_report.json").write_text(
        json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
