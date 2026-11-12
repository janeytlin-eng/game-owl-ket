#!/usr/bin/env python3
"""Offline regression tests. Fixtures are only parser probes, NOT owl candidates."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

import trimesh
from PIL import Image
from trimesh.visual.material import PBRMaterial

SCRIPT = Path(__file__).with_name('audit_glb_mobile.py')
spec = importlib.util.spec_from_file_location('owl_glb_audit', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class MobileStaticPreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)

    def test_simple_valid_mesh_does_not_equal_pet(self):
        fixture = self.path / 'geometry_probe.glb'
        trimesh.creation.icosphere(subdivisions=2).export(fixture)
        result = module.audit(fixture)
        self.assertEqual(result['info']['triangle_count'], 320)
        self.assertIn('no_animations_for_interactive_pet', result['issues'])
        self.assertTrue(result['not_a_visual_or_device_approval'])
        self.assertIn('visual_similarity_to_172_v3_unverified', result['unverified'])

    def test_alpha_material_detected_without_claiming_correct_blend(self):
        fixture = self.path / 'transparent_probe.glb'
        image = Image.new('RGBA', (256, 128), (250, 242, 222, 160))
        mesh = trimesh.creation.icosphere(subdivisions=1)
        mesh.visual = trimesh.visual.TextureVisuals(
            material=PBRMaterial(baseColorTexture=image, alphaMode='BLEND'))
        trimesh.Scene(mesh).export(fixture)
        result = module.audit(fixture)
        self.assertEqual(result['info']['alpha_mode_counts']['BLEND'], 1)
        self.assertEqual(result['info']['images'][0]['width'], 256)
        self.assertIn('transparent_card_depth_order_and_mobile_overdraw_not_tested',
                      result['unverified'])

    def test_invalid_glb_fails(self):
        fixture = self.path / 'invalid.glb'
        fixture.write_bytes(b'fake')
        with self.assertRaises(ValueError):
            module.audit(fixture)


if __name__ == '__main__':
    unittest.main(verbosity=2)
