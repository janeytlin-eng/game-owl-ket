# #172 *Tyto castanops* v3 — Run288 independent adult reference / glTF binary compaction / UV quantization QA

**2026-11-22 Asia/Shanghai. Final: GENUINE_NATIVE_TEXTURED_3D_PASS / 35%_BYTES_SMALLER / GEOMETRIC_LOD_FAIL / SIX_REAL_CAMERA_VIEWS_PASS / ART_REJECTED / CHICK_SCULPT_NOT_MADE / PHONE_WEBGL_UNTESTED / SOURCE_RIGHTS_UNCERTAIN / NO_RELEASE.**

## Scope / read-first evidence

Before doing work, re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/STATUS.md`, original `owl-pet/prototype/index.html`, Run286 and [Run287–287b audit](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run287-cc0-real-barnowl-museum-scan-NO_RELEASE/owl-pet/3d-experiments/172-tyto-castanops/2026-11-22-run287-run287b-museum-barnowl-native-ART_REJECTED-NO_RELEASE.md), and the Run279b genuine Chromium/ThreeJS GLTFLoader test. Prior iterations rejected distorted single-image neural reconstruction, simplified procedural owl anatomy, 2D-like feathers, and adult owl stand-ins. **No changes to the 251-species concept production line, main, manifests, source #172 picture, kitten prototype, or deployment.** New independent branch only.

The #172 target remains the **rightmost cream-white fluffy masked owl juvenile**: round infant silhouette, genuine anatomical heart-shaped face, dark expressive eyes, soft and directional down, natural baby-sized short folding wings, believable side/back and feet on old eucalyptus hollow, and eventual physically tested phone WebGL. An adult museum reference remains **categorically not a releasable chick** even if the mesh technically works.

## Actual external asset / rights scope (not a new product asset)

Reused previously independently pinned source: [Virtual Museums of Małopolska adult Tyto alba specimen](https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc), also linked to the public [museum inventory](https://muzea.malopolska.pl/en/objects-list/2394). Original author declares **CC0** on the Sketchfab page; a third-party downloadable [mirror GLB](https://doc.ayootech.com/galeri/model/0e65de5934db4f0eae02835ba7227dcc.glb) is not independently authenticated against original provider bytes; rights provenance therefore **NOT CERTIFIED for product reuse**. No account login bypass and no payment. Original actual native GLB **43,225,496 bytes**, SHA256 `6412ffd575360397bd90d391d3d4c23397f225945cdef3ec5727bfd91504cd44`, **12 meshes / 261,966 triangles / 756,317 vertices / real 1024² PBR texture**.

**Technical experiment only:** unlike another primitive owl sculpt, use free `@gltf-transform/cli` to optimize original native glTF, retain real mesh, UV, source PBR texture, and run actual six camera spatial rendering with Trimesh and VTK, with foreground occupancy / unique images / hashes all fail-closed. Do **not** call byte compaction a good juvenile model.

## Actual sequence, including preserved failure evidence

- **Run288a** [Actions 45002802387](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45002802387): workflow green, native GLB output verified, actual six distinct nonblank spatial renders. However, opening the generated **six-view contact sheet** revealed a uniform brown clay-like model instead of the source's true feather colors. Although `baseColorTexture` was present, *our QA renderer was wrong*; this is not evidence of valid visual preservation. Independently inspected true glTF binary attributes.
- Diagnosis: `KHR_mesh_quantization` stores `TEXCOORD_0` as **normalized UNSIGNED_SHORT** with integers from 0 to 65,535. Trimesh in this context exposed raw integer-valued UVs without auto-normalization. Our VTK sampling used `coords % 1`, mapping all these integer UVs to a **single texel** (RGB std = 0). This is a **renderer false-negative / false-color**, not necessarily missing original model texture.
- **Run288b** [Actions 45002976079](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45002976079): increased simplification error and required substantial triangle reduction (at least 25%). **Failed properly** because glTF-Transform simplification remained negligible — larger error did not produce mobile game LOD. Actual failure and GLB artifact were archived; did not call the workflow a success.
- **Run288c** [Actions 45003185157](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45003185157): initial color-collapse self-check purposely **failed closed** before six-camera QA, confirming renderer could not pass with collapsed UV colors.
- **Run288d (final technical reference)** [Actions 45003202031](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45003202031): restored realistic PBR base pattern during native VTK rendering by dividing the exact quantized `TEXCOORD_0` by **65535.0** before sampling, and enforced sampled RGB variation. This completed successfully. Independently opened final six-view contact sheet and compared with original Run287b's actual six-view image — adult source mottled facial disk, wings, and branch texture returned. It is *not a new visually acceptable baby*.

## Verified final binary measurements / no deceptive mobile readiness

| Metric | Pinned original adult museum GLB | Run288d compact native GLB |
| --- | ---: | ---: |
| True GLB bytes | 43,225,496 | **28,079,256** |
| Real triangles | 261,966 | **261,794** |
| Vertices | 756,317 | **756,146** |
| Re-imported mesh parts | 12 | 1 (merged) |
| Embedded real PBR texture present | Yes | Yes |
| UV encoding | FLOAT TEXCOORD | NORMALIZED 16-bit unsigned / KHR_mesh_quantization |
| File size change | — | **-35.0401%** |
| Geometry count change | — | **-0.06566%** |

**Critical limit:** Even though output is ~35% smaller in bytes, the mesh has almost the same number of triangles and vertices. This **is not effective mesh LOD** and cannot be honestly called phone GPU-ready. File compaction affects transfer/footprint but does not reduce most geometry/render costs. The test is static, not rigged and not animated; no physical iPhone/Android hardware, WebGL2 context, FPS, GPU memory, touch, thermal or power tests. `glTF` parse/re-import and software VTK camera rendering do not establish any of these. Older Run279b's browser PASS applied to another GLB, **not this donor**.

Six final real 3D camera renderings (440×440) each produced unique SHA and measurable foreground occupancy: **front 11.15%; front45 10.38%; right 10.19%; back 9.65%; left 9.68%; top 8.97%**. Real PBR sampled per-channel RGB standard deviations ~**52.5 / 49.8 / 45.9**, i.e., no brown single-texel collapse; `KHR_mesh_quantization` UV normalization was detected on exactly one merged mesh. No 2D fake rotation or SVG silhouette substituted.

## Independent evidence / human art review

[Run288d final source and actual six-view research artifact 14746518569](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45003202031/artifacts/14746518569). Independently downloaded ZIP: **17,578,845 bytes**, SHA256 `ff4af440251e8be737881e285201dd3082493e7f5688a5ac380c0959cdcf47ae`, exactly matching GitHub artifact digest. **14/14 ZIP CRC entries pass**, **12/12 in-archive SHA256 file checks pass**. Reopened native optimized GLB, confirmed `glTF` magic, matching **28,079,256 bytes**, model SHA256 `646c0d6aef9c329f83dd7fbb4843654d75763d4666e2ab2edd1a63a4a73913d3`, real **1 mesh / 261,794 triangles / PBR texture / KHR_mesh_quantization NORMALIZED uint16 TEXCOORD_0**. Opened actual final six-view contact sheet and compared with original Run287b as human art check. Artifact expected expiration **2026-12-13**, not permanent product hosting. Run288a earlier evidence is retained at [45002802387](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45002802387) and its brown false-render is **not accepted evidence of texture fidelity**.

**Final art: ART_REJECTED / NO_RELEASE.** The picture is visibly an adult grey-brown *Tyto alba* perched on a taxidermy branch with long developed wing and tail and hard adult face; NOT the target rightmost fluffy cream-white *Tyto castanops* juvenile. No artist-reviewed baby sculpt, no soft down groom, no short folded baby wings, no natural eucalypt hollow, no interactive pet, and full licensing provenance unresolved. Fancier compression cannot resolve wrong juvenile anatomy. It would be misleading to give a consumer demo link. All third-party commercial image-to-3D tools requiring money remain unrun; connected zero-budget model search required interactive input not available in this scheduled environment. Free alternatives surveyed but did not acquire a suitable licensed high-quality juvenile asset. **External extra spending: $0.**

## Next attempts

Prioritize **correct juvenile sculpt/groom and verified source rights** over additional repurposing of adult references. A potential free “Baby Owl Sculpt” at CGTrader is not yet physically acquired and carries a **no-AI** license; BlendKit's animated baby owl requires a plan; do not treat links as usable assets. Test Blender/GN feather grooming with explicit export bake to GLB only with a correct young-bird base. *Then* measure Chromium WebGL2 load at 390×780 and actual Android/iPhone GPU, memory, control and thermal behavior. Continue isolated experiments; main and 251-species pipeline untouched. No release.
