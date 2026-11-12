#!/usr/bin/env python3
"""Synthetic material round-trip tests, NOT evidence of owl art correctness."""
import tempfile, unittest
from pathlib import Path
import trimesh
from trimesh.visual.material import PBRMaterial
from soft_down_groom_trial import build

class DownGroomTest(unittest.TestCase):
    def test_real_glb_triangle_roundtrip_and_alpha(self):
        with tempfile.TemporaryDirectory() as d:
            base=Path(d)/'base.glb';out=Path(d)/'fur.glb'
            g=trimesh.creation.icosphere(subdivisions=3,radius=.2)
            g.vertices[:,1]+=.3
            g.visual.material=PBRMaterial(name='Authored owl coat',baseColorFactor=[250,200,180,255])
            scene=trimesh.Scene();scene.add_geometry(g);scene.export(base)
            result=build(base,out,300,'MASK')
            self.assertGreater(result['groom_cards'],0)
            self.assertFalse(result['source_is_Tyto_castanops_juvenile'])
            self.assertGreater(result['scene_triangles'],1280)
            copy=trimesh.load(out,force='scene',process=False)
            mats=[getattr(x.visual,'material',None) for x in copy.geometry.values()]
            self.assertTrue(any(getattr(m,'alphaMode',None)=='MASK' for m in mats))
            self.assertTrue(any(getattr(m,'baseColorTexture',None) is not None for m in mats))
    def test_unknown_source_must_reject(self):
        with tempfile.TemporaryDirectory() as d:
            base=Path(d)/'bare.glb';out=Path(d)/'fur.glb'
            scene=trimesh.Scene();scene.add_geometry(trimesh.creation.icosphere(subdivisions=2));scene.export(base)
            with self.assertRaisesRegex(ValueError,'material-qualified'):
                build(base,out,100)
if __name__=='__main__':unittest.main()
