# Run330 — localized layered down grooming A/B/C — NO_RELEASE
2026-11-24 Asia/Shanghai. SWATCH_ONLY / THREE_NATIVE_GLB_REIMPORTED / NINE_VTK_VIEWS / ART_REJECTED_FOR_RELEASE / WEBGL_UNTESTED / NO_RELEASE.

## Preflight
Read main owl-pet/AGENTS.md, README.md, STATUS.md, research/species/172-tyto-castanops-v3.md and research/reviews/172-tyto-castanops-v3-review.md, then prior Run329 audit at f722a1b05ca91eeed1d36f5ab5fd06388311a491. Opened original concept via connector (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b). Rightmost age-unknown mesoptile has cream thick down, brown-rimmed heart disc, dark eyes, short buried wings, concealed tail, two feet supported on hollow lip. No exact age or science=true. Main status 203/251, untouched. Run329 rejected procedural body; no new full-bird attempt in this run.

## Actual experiment
Local CPU NumPy/Trimesh/VTK, no Blender/bpy available. Isolated 5 cm curved chest swatch, not a bird. Compare equal triangle budget A (8 independent tapered radial filaments per root) and B (1 shared stalk plus 7 spatial branching barbs per root), both 650 roots. C uses 676 jittered grid roots and four extra shorter, thicker undercoat fibers per root. Three-sided tapered tubes with true 3D geometry and per-vertex cream colors, not SVG or billboards. Each produced GLB successfully reimported as 2 meshes. Three independent VTK camera views per sample, total 9 final renders, 480x480 each. Local montage was actually opened for art review.
| Sample | Triangles | GLB bytes | SHA256 |
|---|---:|---:|---|
| A | 66098 | 1574728 | f36f28c95390c0e7589096697a38ab29f3fab6d42fa942834fb0858c34e5c5a5 |
| B | 66098 | 1574728 | 4cf9956ae55a197470cacb7328f3886737f020b87a95b7e8d662dc608dd50d21 |
| C | 101042 | 2413388 | 7296824771a846e9a46b27867412002441af0bb11f5b441d1735b17824bf847d |

## Review
A shows stiff fan-shaped bristles and exposed beige backing. B breaks the fan pattern and has more irregular side silhouette at equal triangle count, but front still visibly sparse, like wire fibers. C reduces gaps and has denser side volume, yet looks like tangled mesh rather than soft down, and is already 101k triangles / 2.4MB for a tiny 25 cm² patch. C combines spacing and undercoat changes, so cannot attribute result to undercoat alone. Raw whole-body replication would inflate budget; no actual full-body mobile benchmark claimed. None is approved as a character or as finished down material. No complete face, wing, tail or toes modeled in this experiment. No new WebGL test (prior local navigation restriction noted; no bypass), no physical phone test, no deployment. Next test should isolate strand shading/normals and coverage at fixed budget; professional anatomy remains independent unresolved blocker. No additional spending.

## Independent archive
Exact executed [groom.py](run330-local/groom.py), SHA256 1cf1f2c252948edf9fc2f5bcd5be925add1e3c112264e632314e5ae99d6fd77c, remote Git blob f26650258b027a618881c9b91721169ca2db9808 matches local git hash-object and remote readback. Run python groom.py in a separate local directory with NumPy, Trimesh, VTK and Pillow. Full local montage SHA256 ec9ba3fe804c3564a1169a17bc4238d04febe4178c880f76c848becc553d281d. [Actual nine-view thumbnail](run330-local/actual-ABC-thumbnail.jpg.b64) is 144x144, decoded bytes 1692, SHA256 7f731e581fb2942334d3ad6900d3457bec8ac5c1a4085d6e9d8a1409b976e8aa, verified decoded remote Git blob bd835843491b15f7ab5e1e13d7cc35b2eb7a5f6d matches local; corrected earlier base64 transfer by removing one duplicated 4-character group. Final base64 2256 characters read back exactly. Decode with base64 -d. Full GLBs/full-resolution views generated locally but not uploaded; source, thumbnail and measured hashes archived. No remote CI pass claimed.

Only #172 research branch writes, no changes to main, original concept, 251-species production, kitten prototype or deployment. New research swatches=3, new complete chick models=0, approved=0. NO_RELEASE.
