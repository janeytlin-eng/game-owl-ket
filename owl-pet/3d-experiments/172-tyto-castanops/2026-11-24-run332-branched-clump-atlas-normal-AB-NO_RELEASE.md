# Run332 — branched down clump atlas / normal alignment A/B — NO_RELEASE
2026-11-24 Asia/Shanghai. TWO_NATIVE_GLB_REIMPORTED / SIX_VTK_VIEWS / ART_REJECTED / WEBGL_CONTEXT_BLOCKED / NO_RELEASE.

## Preflight
Read main owl-pet/AGENTS.md, README.md, STATUS.md and #172 v3 review; main STATUS reported 205/251 and active production. Read Run331 audit and executed C source at ae82b0ecdc355565d1683bda1acf5d0fa58f02d1. Fetched and actually viewed original full #172 v3 concept (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b). Target rightmost bird: cream thick mesoptile, broad brown-rimmed heart disc, dark eyes, short buried wings and hidden tail, supported toes at eucalypt hollow lip, precise age unknown. Review PASS_WITH_LIMITATIONS, science=false. Guessed species file path returned 404, so no claim of rereading that file. No Blender/bpy installed. 

## Actual experiment
Run331 C had 5554 triangles and straight crossed strands with bare spots. This run made two 5cm curved local swatches using NumPy, Pillow, Trimesh and VTK with xvfb-run. Four original 256x256 atlas tiles (512x512 RGBA total) each contain 65 curved branched strand paths with soft edges. 484 world-space curved ribbons; wider clump shapes, seeded atlas choice, warm cream solid backing (not actual backing microtexture despite source comment). A vertical growth axis; B surface-normal growth axis; all other parameters and seeds held fixed. Both native GLBs reimported successfully with two geometries each. Actual binary GLB JSON confirms embedded texture, MASK alphaCutoff=0.4 and doubleSided=true.
| Variant | Triangles | Bytes | SHA256 |
|---|---:|---:|---|
| atlas-vertical A | 5554 | 433512 | c152bc6aeafa3a2300dc3420bc5cfce09de4d7ca612341bc91202954e6326f6b |
| atlas-normal B | 5554 | 433516 | 6193f650aa22d6647050090ed3bada497dc0f7eec25da9005bf490b220864369 |

Rendered six real 400x400 VTK views (top, oblique, near-side for each) and actually inspected 1200x800 montage. VTK uses pre-thresholded alpha pixels and interpolation/blending, not proof of a glTF MASK shader. A/B still have patchy exposed backing, granular overly dense white speckle and hard rectangular substrate silhouette. Normal alignment yields only subtle side/oblique differences; no convincing soft depth or natural clump shading. Both rejected. Larger texture more than doubles Run331 C GLB size at same mesh count. No performance or visual equivalence claim. New full chick models=0, art-approved=0. 

## Browser test
Actually launched local Chromium via Playwright with 390x780 viewport. Canvas WebGL2 context creation returned false/null in initial test and three configurations: --use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader; --use-gl=angle --use-angle=swiftshader-webgl --enable-unsafe-swiftshader; --disable-gpu-sandbox --enable-unsafe-swiftshader (all --no-sandbox). Browser process launched but no valid GPU context, so no GLTFLoader, alpha overdraw benchmark, or physical phone test. No paid service invoked. 

## Archive
- [Executed source](run332-local/swatch.py), SHA256 c5b693b5269c7677bd49bb92b98c7f3d1ceae86c8266b4c5cf37be7b231a5c86. Local git hash-object and exact remote readback blob 236d921d6e04e30d15ca02e74abd7ec5557e765e. Run xvfb-run -a python swatch.py in isolated directory with NumPy/Pillow/Trimesh/VTK.
- Actual full montage SHA256 55f7e731491b86742d11c36e881ca2e79f44fb8fad4317ab9c5214c3cff38aa3. [Actual six-view tiny JPEG](run332-local/actual-six-view-tiny.jpg.b64) 120x80, 1581 decoded bytes, local SHA256 4cfcaf96c27e4f3af79fcea1649b9f79355750426cdd1033d816356294cbee84; remote encoded content exact readback, blob d016f87043654e3e97a171f90ef1892707f72738. Decode with base64 -d. Full GLBs/full images locally generated, not uploaded.
- Research branch only. No main, original concept, 251-species production, kitten prototype or deployment writes. Next test should prioritize low-frequency clump shading and dense short base coverage before increasing strand complexity; professional whole-chick sculpt remains unresolved. NO_RELEASE.
