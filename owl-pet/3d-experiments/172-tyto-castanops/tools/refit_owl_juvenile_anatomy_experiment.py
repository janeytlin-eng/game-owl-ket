#!/usr/bin/env python3
"""Unapproved anatomical transfer trial on a CC0 adult great horned owl.

The source's real sculpted body and feather meshes are preserved. This removes
ear-like tufts and visible tail rectrices, increases crouching torso mass, and
reduces adult-looking folded remiges. Missing Tyto heart disc, down groom,
realistic expression and crouch/support mean NOT a qualified #172 juvenile.
"""
import sys
from pathlib import Path
import numpy as np
import trimesh

def transfer(source, target):
    scene=trimesh.load(str(source),force='scene',process=False)
    result=trimesh.Scene()
    for node in scene.graph.nodes_geometry:
        transform,gi=scene.graph.get(node)
        label=node.lower()
        if 'tuft' in label or 'rectrix' in label:
            continue
        geom=scene.geometry[gi].copy()
        geom.apply_transform(transform)
        verts=np.asarray(geom.vertices).copy()
        adult_height=verts[:,1].copy()
        t=np.clip(adult_height/.47,0,1)
        belly=1+.20*np.exp(-((t-.36)/.26)**2)
        verts[:,0]=(verts[:,0]-.01)*belly+.01
        verts[:,2]*=1.09+.16*np.exp(-((t-.45)/.30)**2)
        verts[:,1]=.012+.76*adult_height
        if any(x in label for x in ('wing','flight feather','covert')):
            side=np.sign(np.median(verts[:,2])) or 1
            anchor=np.array([-.016,.188,.09*side])
            verts=anchor+.47*(verts-anchor)
        geom.vertices=verts
        result.add_geometry(geom,geom_name=node)
    result.export(str(target))
    return {'meshes':len(result.geometry),
            'triangles':sum(len(g.faces) for g in result.geometry.values()),
            'artifact_quality':'REJECTED_UNAPPROVED_NOT_A_TYTO_CHICK'}

if __name__=='__main__':
    if len(sys.argv)!=3:
        raise SystemExit('usage: refit_owl_juvenile_anatomy_experiment.py SOURCE.glb OUT.glb')
    print(transfer(Path(sys.argv[1]),Path(sys.argv[2])))
