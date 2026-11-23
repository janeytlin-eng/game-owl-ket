#!/usr/bin/env python3
"""Run326: fetch and audit a *different* free CC-BY barn owl native GLB.
Research candidate only. NOT a juvenile Tyto castanops. NO_RELEASE.
"""
import hashlib
import json
import struct
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests

URL = "https://vinish-models.pages.dev/birds/barn-owl.glb"
LICENSE_PAGE = "https://vinish.dev/free-3d-models/birds"
CREDIT = '"Barn Owl" by vinish.dev (https://vinish.dev/free-3d-models/), CC BY 4.0'
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "owl172-run326-evidence")
OUT.mkdir(parents=True, exist_ok=True)
FNAME = "vinish_barn_owl_CC_BY_ANATOMY_ONLY_ADULT_NO_RELEASE.glb"
report = dict(run="326", source_url=URL, source_license_page=LICENSE_PAGE,
              required_attribution=CREDIT, domain=urlparse(URL).netloc,
              target="172 Tyto castanops v3 rightmost cream-white mesoptile chick",
              provider_species="generic adult barn owl; NOT Tyto castanops juvenile",
              verified_juvenile=False, art_approved=False, release=False,
              extra_paid_usd=0, technical_source_verified=False)
try:
    response = requests.get(URL, timeout=70, headers={"User-Agent": "Mozilla/5.0 (research; no auth)"}, stream=True)
    report["http_status"] = response.status_code
    report["content_type"] = response.headers.get("content-type")
    response.raise_for_status()
    data = bytearray()
    for chunk in response.iter_content(chunk_size=1024 * 128):
        if chunk:
            data.extend(chunk)
            if len(data) > 18_000_000:
                raise ValueError("Source unexpectedly exceeds 18 MB: abort")
    data = bytes(data)
    report["bytes"] = len(data)
    report["sha256"] = hashlib.sha256(data).hexdigest()
    if len(data) < 100_000 or data[:4] != b"glTF":
        raise ValueError("Not a source-attributable native GLB")
    magic, version, byte_length = struct.unpack_from("<4sII", data, 0)
    if magic != b"glTF" or version != 2 or byte_length != len(data):
        raise ValueError("Invalid native glTF v2 header or length")
    offset = 12
    jl, jt = struct.unpack_from("<I4s", data, offset)
    if jt != b"JSON" or jl > len(data) - 20:
        raise ValueError("No valid GLB JSON chunk")
    gltf = json.loads(data[20:20+jl].decode("utf-8").rstrip(" \x00"))
    meshes = gltf.get("meshes", [])
    accessors = gltf.get("accessors", [])
    triangles = 0
    primitives = 0
    for mesh in meshes:
        for primitive in mesh.get("primitives", []):
            if primitive.get("mode", 4) != 4:
                continue
            ai = primitive.get("indices", primitive.get("attributes", {}).get("POSITION"))
            if not isinstance(ai, int) or ai >= len(accessors):
                continue
            triangles += accessors[ai]["count"] // 3
            primitives += 1
    nodes = gltf.get("nodes", [])
    animations = gltf.get("animations", [])
    report["gltf_metadata"] = dict(
        asset=gltf.get("asset"), meshes=len(meshes),
        triangle_primitives=primitives, triangle_count=triangles,
        nodes=len(nodes), skins=len(gltf.get("skins", [])),
        animations=[a.get("name", "(unnamed)") for a in animations],
        animation_channel_counts=[len(a.get("channels", [])) for a in animations],
        material_count=len(gltf.get("materials", [])),
        embedded_images=len(gltf.get("images", [])),
        texture_count=len(gltf.get("textures", [])),
        node_names_anatomy=[n.get("name", "") for n in nodes if
                            any(w in n.get("name", "").lower() for w in
                                ("wing", "feather", "jaw", "tail", "leg", "toe"))][:65],
    )
    if triangles < 5000 or not meshes:
        raise ValueError("Native GLB lacks substantive triangular bird geometry")
    report["technical_source_verified"] = True
    (OUT / FNAME).write_bytes(data)
    try:
        import trimesh
        scene = trimesh.load(OUT / FNAME, force="scene", process=False)
        report["trimesh_reimport"] = dict(success=True, mesh_count=len(scene.geometry),
            bounds=scene.bounds.tolist() if scene.bounds is not None else None)
    except Exception as e:
        report["trimesh_reimport"] = dict(success=False, error=repr(e))
except Exception as e:
    report["error"] = repr(e)
finally:
    (OUT / "source_and_native_anatomy.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "ATTRIBUTION_AND_RIGHTS_GATE.txt").write_text(
        "SOURCE: " + URL + "\nLICENSE CLAIM PAGE: " + LICENSE_PAGE +
        "\nATTRIBUTION: " + CREDIT +
        "\nNO_RELEASE: adult barn owl base is NOT a Tyto castanops mesoptile chick."
        "\nRights for final work and attribution must be reviewed; source page is not an independent title audit.\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["technical_source_verified"]:
        sys.exit(2)
