#!/usr/bin/env python3
"""Static GLB preflight for owl-pet. NOT a mobile/WebGL or art-quality certification.
Usage: python audit_glb_mobile.py candidate.glb [report.json]
"""
from __future__ import annotations
import io, json, struct, sys
from pathlib import Path
import numpy as np
import trimesh
from PIL import Image

TARGET_BYTES = 5 * 1024 * 1024
TARGET_TRIANGLES = 120_000
TARGET_TEXTURE_PIXELS = 2 * 1024 * 1024
MAX_TEXTURE_DIM = 2048


def read_glb(path: Path):
    data = path.read_bytes()
    if len(data) < 20 or data[:4] != b'glTF':
        raise ValueError('not a binary glTF (.glb)')
    magic, version, length = struct.unpack_from('<4sII', data)
    if version != 2 or length != len(data):
        raise ValueError('invalid GLB version or declared byte length')
    pos, js, bins = 12, None, []
    while pos < len(data):
        if pos + 8 > len(data):
            raise ValueError('truncated GLB chunk header')
        size, kind = struct.unpack_from('<I4s', data, pos)
        pos += 8
        if size % 4 or pos + size > len(data):
            raise ValueError('invalid GLB chunk size')
        chunk = data[pos:pos+size]
        pos += size
        if kind == b'JSON':
            if js is not None:
                raise ValueError('multiple JSON chunks')
            js = json.loads(chunk.decode('utf-8').rstrip(' \x00'))
        elif kind == b'BIN\x00':
            bins.append(chunk)
    if js is None or js.get('asset', {}).get('version') != '2.0':
        raise ValueError('missing glTF 2.0 JSON')
    return js, bins


def audit(path: Path):
    issues, unknowns = [], []
    if not path.is_file():
        raise FileNotFoundError(path)
    doc, chunks = read_glb(path)
    info = {'file': path.name, 'bytes': path.stat().st_size,
            'asset_version': doc['asset']['version'],
            'extensions_required': doc.get('extensionsRequired', []),
            'extensions_used': doc.get('extensionsUsed', [])}
    if info['bytes'] > TARGET_BYTES:
        issues.append('asset_size_exceeds_5MiB_target')
    required = set(info['extensions_required'])
    for extension in sorted(required & {'KHR_draco_mesh_compression',
                                          'EXT_meshopt_compression',
                                          'KHR_texture_basisu'}):
        issues.append('decoder_needed:' + extension)
    if any(uri for b in doc.get('buffers', []) if (uri := b.get('uri'))):
        issues.append('external_buffer_dependency')
    if any(uri for i in doc.get('images', []) if (uri := i.get('uri'))):
        issues.append('external_image_dependency')

    mats = doc.get('materials', [])
    alpha = [m.get('alphaMode', 'OPAQUE') for m in mats]
    info['materials'] = len(mats)
    info['alpha_mode_counts'] = {m: alpha.count(m) for m in sorted(set(alpha))}
    info['animations'] = len(doc.get('animations', []))
    info['skins'] = len(doc.get('skins', []))
    info['nodes'] = len(doc.get('nodes', []))
    info['morph_target_meshes'] = sum(
        1 for mesh in doc.get('meshes', [])
        if any('targets' in p for p in mesh.get('primitives', [])))
    if 'BLEND' in alpha:
        unknowns.append('transparent_card_depth_order_and_mobile_overdraw_not_tested')
    if not info['animations']:
        issues.append('no_animations_for_interactive_pet')
    if not info['skins'] and not info['morph_target_meshes']:
        issues.append('no_skin_or_morph_target_for_bird_deformation')

    images = []
    views = doc.get('bufferViews', [])
    for ix, im in enumerate(doc.get('images', [])):
        src = None
        if 'bufferView' in im:
            view = views[im['bufferView']]
            bi = view.get('buffer', 0)
            if bi < len(chunks):
                start = view.get('byteOffset', 0)
                src = chunks[bi][start:start + view['byteLength']]
        elif im.get('uri', '').startswith('data:'):
            import base64
            src = base64.b64decode(im['uri'].split(',', 1)[1])
        record = {'index': ix, 'mimeType': im.get('mimeType', ''), 'decoded': False}
        if src is not None:
            try:
                with Image.open(io.BytesIO(src)) as picture:
                    w, h = picture.size
                    record.update({'decoded': True, 'width': w, 'height': h,
                                   'approx_rgba_vram_bytes': w*h*4})
                    if max(w, h) > MAX_TEXTURE_DIM:
                        issues.append('image_' + str(ix) + '_over_2048px')
            except Exception as exc:
                record['decode_error'] = str(exc)[:90]
                issues.append('image_' + str(ix) + '_cannot_decode')
        else:
            unknowns.append('image_' + str(ix) + '_bytes_unavailable')
        images.append(record)
    info['images'] = images
    pixels = sum(i.get('width', 0)*i.get('height', 0) for i in images)
    info['approx_texture_rgba_vram_bytes_no_mips'] = pixels*4
    if pixels > TARGET_TEXTURE_PIXELS:
        issues.append('total_texture_pixels_exceed_2MP_target')

    try:
        scene = trimesh.load(path, force='scene', process=False)
        triangles, degenerates, meshes, all_bounds = 0, 0, 0, []
        for node in scene.graph.nodes_geometry:
            matrix, name = scene.graph.get(node)
            mesh = scene.geometry[name]
            if not isinstance(mesh, trimesh.Trimesh) or not len(mesh.faces):
                continue
            verts = trimesh.transform_points(mesh.vertices, matrix)
            all_bounds.append(np.array([verts.min(axis=0), verts.max(axis=0)]))
            faces = verts[mesh.faces]
            doubles = np.cross(faces[:, 1] - faces[:, 0],
                               faces[:, 2] - faces[:, 0])
            degenerates += int(np.count_nonzero(
                np.einsum('ij,ij->i', doubles, doubles) < 1e-18))
            triangles += len(mesh.faces)
            meshes += 1
        info['triangle_count'] = triangles
        info['mesh_instances'] = meshes
        info['degenerate_triangles'] = degenerates
        if triangles > TARGET_TRIANGLES:
            issues.append('triangle_count_exceeds_120k_target')
        if degenerates:
            issues.append('degenerate_faces_present')
        if all_bounds:
            b = np.array(all_bounds)
            lo, hi = b[:, 0].min(axis=0), b[:, 1].max(axis=0)
            info['aabb_min'] = lo.round(6).tolist()
            info['aabb_max'] = hi.round(6).tolist()
            info['aabb_extent'] = (hi-lo).round(6).tolist()
        else:
            issues.append('no_renderable_triangles')
    except Exception as exc:
        issues.append('mesh_import_failed:' + str(exc)[:130])
    unknowns.extend(['visual_similarity_to_172_v3_unverified',
                     'true_face_disc_feather_anatomy_unverified',
                     'feet_contact_with_eucalyptus_hollow_unverified',
                     'real_phone_webgl_gpu_and_touch_unverified',
                     'actual_fps_memory_and_shader_support_unverified'])
    return {'static_preflight': 'WARN_OR_FAIL' if issues else 'PASS_STATIC_ONLY',
            'not_a_visual_or_device_approval': True,
            'info': info, 'issues': sorted(set(issues)),
            'unverified': sorted(set(unknowns)),
            'targets': {'max_glb_bytes': TARGET_BYTES,
                        'max_triangles': TARGET_TRIANGLES,
                        'max_texture_dimension': MAX_TEXTURE_DIM,
                        'max_total_texture_pixels': TARGET_TEXTURE_PIXELS}}


def main():
    if len(sys.argv) not in (2, 3):
        raise SystemExit('Usage: audit_glb_mobile.py MODEL.glb [RESULT.json]')
    try:
        result = audit(Path(sys.argv[1]))
    except Exception as exc:
        result = {'static_preflight': 'INVALID',
                  'error': type(exc).__name__ + ': ' + str(exc)}
    report = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if len(sys.argv) == 3:
        Path(sys.argv[2]).write_text(report, encoding='utf-8')
    print(report)
    if result['static_preflight'] == 'INVALID':
        raise SystemExit(2)


if __name__ == '__main__':
    main()
