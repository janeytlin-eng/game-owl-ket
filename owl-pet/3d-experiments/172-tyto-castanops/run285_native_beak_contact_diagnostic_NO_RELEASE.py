#!/usr/bin/env python3
"""#172 Run285: repair only beak/front-surface contact on a true 3D native mesh.
This is geometry/visual research, not a release candidate or new primitive owl.
Inputs are the actual Run284 GLB, never an SVG/sprite/stand-in.
"""
import sys, hashlib, json
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
import trimesh

src=Path(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
assert src.read_bytes()[:4]==b'glTF', "Must begin with authentic binary glTF"
expected='6bb3dce65140483cf88d5499b3dcb7334d06338976216c03a498b60bdee593af'
actual=hashlib.sha256(src.read_bytes()).hexdigest()
assert actual==expected, f'Wrong upstream artifact hash: {actual}'
scene=trimesh.load(src,force='scene',process=False)
def name_match(prefix):
    ks=[k for k in scene.geometry if prefix in k]
    assert len(ks)==1, (prefix,ks,list(scene.geometry))
    return ks[0]
body_key=name_match('one_continuous_organic_owl_body')
beak_key=name_match('curved_beak')
body=scene.geometry[body_key]
beak=scene.geometry[beak_key]
assert len(body.faces)>100000 and len(beak.faces)>400
bv=np.asarray(body.vertices)
beakv=np.asarray(beak.vertices)
assert float(bv[:,2].max())>0 and float(beakv[:,2].max())>0
# Build a 2D spatial acceleration structure over the positively-facing surface.
# Allow XY radius 0.022-0.055; maximize Z to target front shell.
front=bv[(bv[:,2]>0.08)&(bv[:,1]>0.025)&(bv[:,1]<0.35)]
assert len(front)>3000, len(front)
tree=cKDTree(front[:,:2])
# Beak root uses high-Y end; do not rely on glTF vertex ordering.
max_y=float(beakv[:,1].max())
root=beakv[beakv[:,1]>max_y-.013]
assert len(root)>=6, (len(root),max_y)
xy=root[:,:2].mean(axis=0)
indices=tree.query_ball_point(xy, r=.035)
assert len(indices)>40, ('No front-face neighbors',len(indices))
front_z=float(np.percentile(front[indices,2],96))
before_root_z=float(np.median(root[:,2]))
before_gap=before_root_z-front_z
# Embed the beak root by 0.008m: overlaps body rather than floating.
shift=front_z-0.008-before_root_z
assert -.20<shift<.08, shift
revised=beakv.copy(); revised[:,2]+=shift
beak.vertices=revised
after_root_z=float(np.median(revised[beakv[:,1]>max_y-.013,2]))
after_gap=after_root_z-front_z
assert abs(after_gap+.008)<.002
# Full meshes are preserved; no toy objects are constructed or added.
# The slight overlap is NOT topological fusion; do not claim a watertight beak.
control=trimesh.load(src,force='scene',process=False)
control_path=out/'run285_original_control_RESEARCH_NO_RELEASE.glb'
control_path.write_bytes(trimesh.exchange.gltf.export_glb(control,include_normals=True))
revised_path=out/'run285_beak_embedded_RESEARCH_NO_RELEASE.glb'
revised_path.write_bytes(trimesh.exchange.gltf.export_glb(scene,include_normals=True))
checks={}
for label,p in [('control',control_path),('beak_embedded',revised_path)]:
    re=trimesh.load(p,force='scene',process=False)
    tri=sum(len(g.faces) for g in re.geometry.values())
    assert tri>150000 and len(re.geometry)>=26
    checks[label]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                   'bytes':p.stat().st_size,'triangles':int(tri),
                   'meshes':len(re.geometry),'actual_binary_GLTF':True}
report={
 'source_artifact':'Run284 44982798516 #14737544875',
 'source_glb_sha256':actual,
 'root_front_before_m':round(before_gap,6),
 'root_front_after_m':round(after_gap,6),
 'beak_z_translation_m':round(float(shift),6),
 'root_projection_neighbor_count':len(indices),
 'true_mesh_contact':'overlap only, not welded or watertight at beak',
 'variants':checks,
 'limitation':'This repair does not fix facial disc, fluffy down, wings, feet, rear anatomy, old eucalyptus perch or rights',
 'art':'UNREVIEWED_NOT_APPROVED','real_phone_gpu':'UNTESTED','release':False,
}
(out/'run285_machine_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
