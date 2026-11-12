#!/usr/bin/env python3
"""Run10 v25 rejected recolour experiment on a real adult-mesh refit.

Maps current feather detail into pale cream, darkens irises and lightens bill.
Does not create a Tyto heart disc, physical down or correct chick support;
REJECT on visual QA. Kept for reversible A/B comparison, not user preview.
"""
import sys
from pathlib import Path
import trimesh
import numpy as np
from PIL import Image

palette={
    'Authored owl coat':((232,221,204),.17),
    'Original overlapping avian coverts':((227,217,196),.20),
    'Original closed folded remiges':((224,211,190),.22),
    'Great horned owl golden iris':((25,21,19),0),
    'Strongly decurved raptorial upper bill':((235,213,183),0),
}

def recolor(source,destination):
    scene=trimesh.load(str(source),force='scene',process=False)
    seen=set()
    for geom in scene.geometry.values():
        material=getattr(geom.visual,'material',None)
        if material is None or material.name not in palette or id(material) in seen:
            continue
        seen.add(id(material))
        original=material.baseColorTexture
        if original is None:
            continue
        base,strength=palette[material.name]
        pixels=np.asarray(original.convert('RGB'),dtype=np.float32)
        luma=pixels[:,:,0]*.2126+pixels[:,:,1]*.7152+pixels[:,:,2]*.0722
        delta=(luma-luma.mean())*strength
        output=np.stack([np.clip(base[channel]+delta,0,255)
                         for channel in range(3)],axis=-1).astype('uint8')
        material.baseColorTexture=Image.fromarray(output,'RGB')
        material.baseColorFactor=[255,255,255,255]
    scene.export(str(destination))
    return dict(recolored_materials=len(seen),art_gate='FAIL_STILL_NO_TYTO_DISC_OR_DOWN')

if __name__=='__main__':
    if len(sys.argv)!=3:
        raise SystemExit('usage: recolor_reference_trial.py INPUT.glb OUTPUT.glb')
    print(recolor(Path(sys.argv[1]),Path(sys.argv[2])))
