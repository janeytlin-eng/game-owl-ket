#!/usr/bin/env python3
"""RESEARCH ONLY Run90: photographically registered 2D concept pigment on REAL
three-dimensional continuous sculpt. This is NOT image-to-3D, NOT a compliant
pet, NOT proof of side/back texture, and never a user-facing release.

Use same source sculpt, locked cameras and lighting for baseline / color-
projection / color+real geometric alpha down controls. Difference is measured.
"""
import sys, os, json, hashlib, importlib.util, pathlib, math
import numpy as np
from PIL import Image
import trimesh

root=pathlib.Path(__file__).resolve().parent
src_script=root/"mesoptile_organic_sculpt_trial_v31.py"
spec=importlib.util.spec_from_file_location("mesoptile_v31",src_script)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
if len(sys.argv)<4: raise SystemExit("Usage: run90.py source_concept_png output_dir resolution")
concept=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2]); res=int(sys.argv[3])
out.mkdir(parents=True,exist_ok=True)
assert concept.is_file() and src_script.is_file()
photo=np.array(Image.open(concept).convert("RGB"),dtype=np.uint8)
assert photo.shape[:2]==(1024,1536), "Exact v3 original image dimensions needed"
source_sha=hashlib.sha256(concept.read_bytes()).hexdigest()
assert source_sha and photo[445,1220].mean()>45

def photo_pigment(mesh,strength):
    xyz=np.asarray(mesh.vertices)
    xyz_n=np.asarray(mesh.vertex_normals)
    x,y,z=xyz.T
    # Registration measured approximately from rightmost bird in exact v3
    # concept: face centered to bird's right due to asymmetry; front-only sample.
    head_factor=np.clip((z-.68)/.24,0,1)
    u=1186+35*head_factor+x*366
    v=795-(z-.14)*430
    ui=np.rint(u).astype("int64")
    vi=np.rint(v).astype("int64")
    bounds=(ui>=972)&(ui<=1410)&(vi>=285)&(vi<=800)
    ui=np.clip(ui,0,1535); vi=np.clip(vi,0,1023)
    color=photo[vi,ui].astype(np.float32)
    # Do NOT paste 2D background on rear, cheek sides, or unsupported regions.
    frontal=np.clip((-xyz_n[:,1]-.18)/.57,0,1)
    depth=np.clip((-.025-y)/.24,0,1)
    w=(strength*frontal*depth*bounds).astype(np.float32)
    bad=(color[:,0]<75)&(z<.82)
    w[bad]*=.05
    base=mesh.visual.vertex_colors.copy()
    base[:,:3]=np.uint8(np.clip(base[:,:3]*(1-w[:,None])+color*w[:,None],0,255))
    mesh.visual.vertex_colors=base
    return {
      "affected_vertex_count":int(np.count_nonzero(w>.05)),
      "weight_over_0_5":int(np.count_nonzero(w>.5)),
      "max_weight":float(np.max(w)),
      "image_projection_uv_rule":{"u":"1186 + 35*clip((Z-.68)/.24) + X*366","v":"795-(Z-.14)*430"},
      "color_source":"same source user's v3 three-bird concept; rightmost chick only",
      "underlying_base_shape_unchanged":True,
      "side_back_texture_authored":False,
      "photogrammetric_depth_inferred":False,
    }

summary={"status":"ART_UNREVIEWED_NOT_APPROVED",
         "reference_sha256":source_sha,
         "base_sculpt":"repository v31 organic SDF head/body",
         "not_a_photogrammetry_scan":True, "not_approved":True,
         "hardware_mobile_tested":False, "variants":[]}
for label,photo_weight,down in [
 ("baseline_v31_no_down",0.0,False),
 ("reference_projection_no_down",.87,False),
 ("reference_projection_alpha_down",.87,True)]:
    scene,raw_stats=mod.make_scene(res=res,n_down=3500)
    body=scene.geometry["ORGANIC_CONNECTED_HEAD_BODY_HEART_RELIEF"]
    assert isinstance(body,trimesh.Trimesh)
    m=photo_pigment(body,photo_weight) if photo_weight else {"affected_vertex_count":0,"max_weight":0}
    assert len(body.faces)>8000
    if not down: scene.delete_geometry("soft_alpha_mesoptile_research_groom")
    # v31's same explicit Y-up GLB boundary as original; front = +Z.
    scene.apply_transform(trimesh.transformations.rotation_matrix(-math.pi/2,[1,0,0]))
    filename=f"owl172_run90_{label}_ART_UNREVIEWED.glb"
    target=out/filename
    scene.export(str(target))
    chk=trimesh.load(str(target),force="scene",process=False)
    triangles=sum(len(g.faces) for g in chk.geometry.values() if hasattr(g,"faces"))
    sha=hashlib.sha256(target.read_bytes()).hexdigest()
    assert target.stat().st_size>100000 and triangles>10000
    # Verify an actual vertex colour attribute in reimported PBR glTF mesh.
    vcol_meshes=sum(1 for g in chk.geometry.values() if g.visual.kind=="vertex")
    assert vcol_meshes>0
    summary["variants"].append({
       "label":label,"glb":filename,"sha256":sha,"bytes":target.stat().st_size,
       "triangles":triangles,"mesh_count":len(chk.geometry),
       "vertex_color_meshes":vcol_meshes,
       "base_watertight":bool(body.is_watertight),
       "photo_projection":m,"alpha_down":down,
       "release_approved":False
    })
(out/"metrics.json").write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
