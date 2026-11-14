#!/usr/bin/env python3
"""Run67 independent anatomy transplant study (ART_REJECTED, never production).
Requires Run65's baseline_P.glb and Run10's optimized original CC0-claimed adult source GLB
in ./run65 and ./run10 respectively. It produces two standalone actual GLBs.
The source owl is an adult great horned owl, NOT a Tyto castanops chick.
"""
from pathlib import Path
import numpy as np
import trimesh, hashlib, json

P=Path(__file__).parent
baseline=P/'run65/baseline_P.glb'
source=P/'run10/source_adult_textures_optimized_REFERENCE_ONLY.glb'
root=trimesh.load(baseline,force='scene',process=False)
cc0=trimesh.load(source,force='scene',process=False)
BODY='nonparametric_reference_conditioned_continuous_mesh'
body_xf=root.graph[BODY][0]

def selected(n):
    return n.startswith(('Articulated bird toe','Curved tapered bird claw',
                         'Bare raptor tarsus','Sphere.012','Sphere.025'))
feet=[n for n in cc0.geometry if selected(n)]
source_bill='Closed descending upper hook and seated cere'

def mapped_mesh(mesh,name,bill=False):
    m=mesh.copy()
    nodes=[n for n in cc0.graph.nodes_geometry if cc0.graph[n][1]==name]
    v=trimesh.transform_points(m.vertices.copy(),cc0.graph[nodes[0]][0])
    if bill:
        new=np.column_stack((.078+1.25*v[:,2],
                             -.314-1.25*(v[:,0]-.115),
                             .757+1.25*(v[:,1]-.35)))
    else:
        new=np.column_stack((2.68*v[:,2],
                             -.18-2.68*v[:,0],
                             .073+2.68*v[:,1]))
    m.vertices=new
    m.fix_normals()
    return m

def run(version):
    s=trimesh.load(baseline,force='scene',process=False)
    for g in list(s.geometry):
        if g.startswith(('supported_toe','curved_natural_claw','buried_down_shank')) or (version=='Z' and g=='curved_horn_bill'):
            s.delete_geometry(g)
    for name in feet:
        m=mapped_mesh(cc0.geometry[name],name)
        s.add_geometry(m,geom_name='cc0_retargeted_'+name,
                       node_name='cc0_retargeted_'+name,transform=body_xf)
    if version=='Z':
        m=mapped_mesh(cc0.geometry[source_bill],source_bill,bill=True)
        s.add_geometry(m,geom_name='cc0_retargeted_curved_bill',
                       node_name='cc0_retargeted_curved_bill',transform=body_xf)
    p=P/f'owl172_run67_{version}_ANATOMY_TRIAL_ART_UNREVIEWED.glb'
    s.export(p)
    r=trimesh.load(p,force='scene',process=False)
    assert BODY in r.geometry
    assert np.array_equal(r.geometry[BODY].vertices,root.geometry[BODY].vertices)
    assert len([g for g in r.geometry if g.startswith('cc0_retargeted')])==len(feet)+(version=='Z')
    qa=dict(version=version,file=p.name,bytes=p.stat().st_size,
            sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
            meshes=len(r.geometry),
            triangles=sum(len(m.faces) for m in r.geometry.values()),
            foot_source_meshes=len(feet),hook_bill_source=(version=='Z'),
            art_status='ART_REJECTED',phone_hardware_test=False,
            source_limited='CC0-claimed adult horned owl, not juvenile Tyto')
    (P/f'run67_{version}_structural.json').write_text(json.dumps(qa,indent=2))
    return qa

if __name__=='__main__':
    print(json.dumps([run('Y'),run('Z')],indent=2))
