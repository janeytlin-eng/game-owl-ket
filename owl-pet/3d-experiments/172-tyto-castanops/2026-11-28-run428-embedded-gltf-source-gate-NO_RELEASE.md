# Run428 — Embedded glTF source access and art gate — NO_RELEASE

2026-11-28. Read main AGENTS, README/STATUS opening sections (207/251, latest six-cycle review), exact #172 v3 species dossier, actual v3 mesoptile crop (blob 2915b7c86316359ff2b8cbd26eb174bfa0280613; base64 decoded for visual inspection) and Run427 commit ccd636d5fa184404dc2ecbd17848b48035e18a09. Reference remains #172 v3, not v7. Cream soft down, broad tan-edged heart mask, dark eyes, horn-colored beak, concealed tail, supported substantial feet. Age unspecified.

## Actual source-access experiment

GitHub code searches for filename:barnowl.gltf, barnowl.stl, owlchick.obj, babyowl.obj, barn_owl.obj, tyto.obj, owlet.obj, owl_chick.stl and baby_owl.obj returned no hits. owl.gltf returned a new source: Jeremy Edelblut's 3moji owl. Repository README explicitly declares CC BY-SA 4.0; LICENSE path itself 404. Source pin: https://github.com/jeremytoys/3moji/tree/8ec8bed2988d1b4dbba225eb5c8b8452ab5dc550 . License attribution and share-alike would need preserving for any distributed adaptation.

Both the embedded-data textual glTF (139515 characters, blob 8c16e43079bacf055dddc829698348f09dd41bda) and native GLB (blob fa3dadabbd069e67982dd0124232a21ef6bb0349) were actually fetched and decoded. Native file 103508 bytes; magic 0x46546c67, version 2, declared length equals decoded length, JSON chunk 1520 bytes, BIN chunk 101960 bytes. All 101960 binary bytes were identical to the decoded data URI in the textual glTF; accessor and bufferView JSON arrays also identical. This demonstrates an alternative route to retrieve small self-contained text glTF assets with geometry AND texture when binary retrieval fails, not a model generation success. Embedded PNG 11997 bytes inspected as a color atlas.

Real mesh: 2404 position entries (all referenced), 6516 valid uint16 indices, 2172 triangles, width/height 0.603185 in mesh space. Bounds x[-0.66327655,0.66527283], y[-1.16740716,1.03514814], z[-0.75211954,0.47176144]. One mesh, one material. Four actual geometry-only depth-buffer raster views at quarter turns incorporating the node yaw were inspected, with 19855/19857/19855/19857 covered pixels (220x220 per view). These coarse renders are silhouette evidence only; projected-space face shading is nearly flat and is not PBR. Also actually fetched and viewed publisher's Images/owl.png (blob f1c200d5cd5e7e2456fb57d97fe7d4fa9f82d6db). It is a stylized blocky red-brown adult-type owl with ear tufts, heavy brow, yellow eyes/beak, long upright torso, no heart-shaped disc and no down. Reject outright as a juvenile Tyto base; no redistribution of external geometry.

## Runtime / additional asset exploration

Local check: Chromium installed, torch/trimesh/VTK/scipy/skimage available; blender executable, bpy, moderngl, pyrender, transformers absent. Actual DNS resolution failed for github.com, huggingface.co and cdn.mint.gg (Errno -3). Web search revisited Mint's CC0 adult barn owl (already blocked Run427); Grab3D CC0 great horned owl published 2026-09-28 is wrong genus, yellow eyes and prominent tufts, listed 399999 or 799999 triangles; not retrieved. https://grab3d.com/models/animals/owl/ . Innerscene CC0 owl listed 19.7 MB, no juvenile Tyto evidence; not retrieved. https://www.innerscene.com/tools/library/3d-parts/owl-d696472a . No generation service or paid download invoked.

## Reproducibility: actual binary equivalence and geometry checks

Python equivalent of the executed connector-side JS parsing. Obtain the pinned GLB and glTF first. No third-party file included in this archive.

```python
import base64, json, struct
from pathlib import Path
import numpy as np
g=json.loads(Path('owl.gltf').read_text())
raw=Path('owl.glb').read_bytes()
magic,version,size,n,kind=struct.unpack_from('<5I',raw)
assert magic==0x46546c67 and version==2 and size==len(raw)
j=json.loads(raw[20:20+n])
m,typ=struct.unpack_from('<2I',raw,20+n)
binary=raw[28+n:28+n+m]
embedded=base64.b64decode(g['buffers'][0]['uri'].split(',',1)[1])
assert binary==embedded
assert j['accessors']==g['accessors']
assert j['bufferViews']==g['bufferViews']
v=np.frombuffer(embedded,dtype='<f4',count=2404*3).reshape(-1,3)
f=np.frombuffer(embedded,dtype='<u2',count=6516,offset=76928).reshape(-1,3)
assert f.max()<len(v)
print(len(raw), n, len(binary), len(v), len(f), np.unique(f).size)
print(v.min(0),v.max(0),np.ptp(v,axis=0)[0]/np.ptp(v,axis=0)[1])
Path('atlas.png').write_bytes(embedded[89960:101957])
```

Decision ART_REJECTED / NO_RELEASE. No high-quality character sample; no actual mobile WebGL test. Only source retrieval method improved. Next prioritize genuine juvenile Tyto geometry in self-contained glTF or OBJ, not adult emoji recolor or optimization. No main/production/original concept/deployment changes, no extra payment.
