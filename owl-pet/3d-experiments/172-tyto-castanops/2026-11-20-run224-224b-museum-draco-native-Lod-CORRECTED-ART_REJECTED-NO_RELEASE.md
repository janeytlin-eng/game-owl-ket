# #172 Run224–224b: museum Tyto adult LOD study, Draco decoder correction, 12 real 3D views — ART_REJECTED / NO_RELEASE

Date: 2026-11-20 (Asia/Shanghai). Separate isolated research branch: research/owl172-run224-museum-3d-lod-material-qualification-no-release. Extra paid costs: $0.

## Re-read before executing

Verified owl-pet/AGENTS.md, README.md, the #172 v3 species research design, original v3 concept image and the Run223/223d rejected museum photogrammetry. Original design PNG is 737,545 bytes, SHA256 881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d. Target is the rightmost *Tyto castanops* age-unknown mesoptile: creamy real down, naturally joined heart face, dark eyes, compact crouch, down-buried short wings, hidden tail, two supported feet, broad eucalyptus hollow lip.

The archive donor [Zenodo record 21379215](https://zenodo.org/records/21379215) states cc-zero (CC0) in metadata. This is the archival license claim, not an independent legal review. The animal is an ADULT *Tyto alba* taxidermy with long wings/tail on a mounted thin branch and stump, not a young *Tyto castanops*. No source image or object should be passed off as the target young character.

## Run224: actual GLB downloads revealed a critical false-positive

[Actual Run224 workflow 44592266178](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44592266178) downloaded and parsed the full 43,225,496-byte scan (261,966 real triangles) and three archived low-resolution GLBs (5.60MB, 2.19MB, 1.63MB). Original genuinely rendered and was visually inspected. Crucially, the three smaller archives require KHR_draco_mesh_compression. Trimesh returned nonempty triangle arrays but **all positions were (0,0,0)**, causing blank camera frames. Run224's first-pass “TRUE_3D_RENDERED” label for those three is WRONG; its zero silhouette-IoU values are **invalid**, not geometry similarity measurements. The original raw measurements and visibly blank 16-frame sheet are preserved without concealment: [Run224 first-pass report](run224-evidence/run224_report.json) and [bad 16-frame diagnostic](run224-evidence/run224_four_LoDs_16view_ADULT_NOT_APPROVED.png).

## Run224b: actual free Draco decoding and strict nonzero geometry gate

[Actual Run224b workflow 44593286911](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44593286911) installed @gltf-transform/cli 4.5.1 without fee, downloaded the three original low-resolution archives again (HTTP 200, exact byte lengths and SHA256), ran gltf-transform copy and independently re-imported the resulting uncompressed native GLBs. Output headers no longer require Draco, and the program now explicitly rejects all-zero / nonfinite / tiny 3D bounds and empty camera shots. All three passed and generated 12 actual spatial 3D views with mapped colour textures.

| Archive variant | Source bytes | Decoded bytes | Actual triangles | Nondegenerate bounds X × Y × Z |
| --- | ---: | ---: | ---: | --- |
| normalized_optimized | 5,603,344 | 6,380,156 | 30,412 | 0.43080 × 0.56346 × 0.45928 |
| normalized_optimized-0.250 | 2,185,576 | 2,486,016 | 9,096 | 0.43009 × 0.56284 × 0.45871 |
| normalized-0.100 | 1,634,244 | 2,350,412 | 26,192 | 0.43183 × 0.56390 × 0.45985 |

Archive SHA256:
- optimized: 3fff5130cfad17cc1fcf312819019bad75782f4f01708d18696e100d643691cb
- optimized-0.250: 97b886248ea11483094a7290f27a97e373752f92f73f6ff585190e3d612d743a
- normalized-0.100: 8d5b2c0baa5dc3be8471bbedbd2ca0fe86feb0d26fc546a378b0b9dc04377b3c

Decoded SHA256:
- optimized: 4865f48828adb93cef4f5ec07002adc1a61855a80adb286f781a227fca89430f
- optimized-0.250: c9a62d8bbac9631f7f56315319592db06fe75ec5b23b40e5c027e8a0d2690026
- normalized-0.100: 42223dac3d4d69b88176f20246cecde2c158dea6445880e52635a0237560dd7e

Independent evidence: [Run224b numeric report](run224b-evidence/run224b_report.json), [12 true camera views — adult donor ONLY, NOT APPROVED](run224b-evidence/run224b_draco_decoded_12views_ADULT_NOT_APPROVED.png), [Run224b reusable decoder and strict checks](run224b_draco_decode_corrected_3d_qa.py).

The actual 12-view sheet was opened and reviewed: each lower-poly adult donor is now nonblank, recognisably three-dimensional from all four azimuths, with genuine feathered adult morphology; the 9,096-triangle variant looks more faceted. ALL remain visually rejected: brown adult plumage, full mature flight wings and tail, prominent exposed legs, thin twig and pedestal; no cream baby down, naturally fluffy body, nestled wide hollow support or juvenile articulation. These models cannot pass an artistic juvenile gate through recolouring.

## Archives, boundaries, and limitations

Run224 and Run224b separately uploaded real binary GLBs and camera PNG to GitHub Actions 30-day **research-only temporary artifacts**, not a permanent published character. Run224b artifact is attached to [workflow 44593286911](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44593286911) with artifact id 14563799633 and measured compressed size 33,280,317 bytes. Run224b machine report and 12-camera negative view sheet have also been durably committed to this isolated research branch. The machine report individually records file lengths and SHA256. Do not call the artifact permanent storage.

These free pre-optimized native donor GLBs are 1.63–5.60 MB rather than 43.23 MB, but Draco requires a compatible renderer decoder. No real phone hardware or phone WebGL performance test has been done. VTK render materials only approximate glTF PBR. The technical success pertains to a legitimate ADULT donor and file decoding, not the actual design.

Important permanent process correction: **a nonempty triangle count and successful PNG write do not prove a rendered 3D object**. Mandatory extension/codec check, independently decoded real nonzero vertex bounds, finite coordinates, and actual foreground pixels are required before claiming true native 3D QA.

No modifications to main, 251-species production, root vocabulary game, cat prototype or deployment; only #172 dedicated scripts, independent workflows, machine reports and negative visual evidence on research branch.

Final: NATIVE_GLTF_DECODER_TECHNICAL_PASS / 3 VALID ADULT DONOR LoDs / 12 TRUE_3D_VIEWS / NO_ACCEPTABLE_JUVENILE / NO_PHONE_WEBGL / ART_REJECTED / NO_RELEASE / NO_NOTIFICATION.
