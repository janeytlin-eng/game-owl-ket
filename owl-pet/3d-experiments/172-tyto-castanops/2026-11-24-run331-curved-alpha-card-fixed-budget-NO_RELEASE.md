# Run331 — curved alpha-card down swatch at fixed mesh budget — NO_RELEASE
2026-11-24 Asia/Shanghai. THREE_LOCAL_GLB_REIMPORTED / NINE_VTK_VIEWS / SWATCH_ONLY / ART_REJECTED / WEBGL_UNTESTED / NO_RELEASE.

## Preflight
Read main owl-pet/AGENTS.md, README.md, STATUS.md, #172 v3 species and review files, and Run330 audit at 440778780ab6e1ea4bb0631e7bd815759647111b. Actually opened full original v3 concept (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b): rightmost cream mesoptile, dark eyes, developed brown-rimmed heart disc, concealed short wings/tail, both feet on eucalypt hollow lip; exact age unknown, science=false. Main status 205/251, not touched. Run330 C had 101042 triangles on a 5cm square; wire-like appearance. No Blender/bpy installed. This run tests a lower-budget fur material only, not a full bird.

## Actual local experiment
NumPy, Pillow, Trimesh, VTK, xvfb-run. Created a 5cm curved backing with 484 world-space curved ribbons (5 cross-sections each; not camera-facing sprites). Generated original procedural 256x256 RGBA strand texture; 180 painted wisps, no borrowed image. A opaque control and B alpha variant share identical geometry; C lowers ribbon length and increases tilt to improve coverage, so C is not a single-variable change. Native GLBs reimported with two meshes each. Parsed actual binary glTF JSON: all have embedded image, doubleSided=true; A OPAQUE, B/C MASK alphaCutoff=0.4. VTK previews use RGBA blending and requested depth peeling, **not a verified glTF MASK rendering**. Rendered three distinct camera angles each (nine 400x400 views), actually opened the A/B and C montages.
| Variant | Triangles | GLB bytes | SHA256 |
|---|---:|---:|---|
| A opaque | 5554 | 192852 | 3b6e1563a5223e801218940c9c4261c6f8609b6b1d2fafff7ced023ee1bfde16 |
| B alpha | 5554 | 197624 | 9af71f3f1356a1561ad603799ccc157439e60ddfdec31aede5c4cb922b0b2fad |
| C alpha lean | 5554 | 197624 | b909ededbf8557592d07dabc24b8f7d0f81d5871d84074610ea73822befda965 |

## Visual decision
A looks like confetti, fails. B removes the rectangular ribbon silhouettes in side view but its front shows large areas of exposed beige backing and sparse grey speckling. C improves frontal coverage through lean/length changes, but visible crossed straight strand patterns, protruding wisps, exposed backing and artificial pale wire appearance remain. All rejected. C is about 5.5% of prior Run330 C's triangle count on nominally equal 25cm² patch, but different material and geometry; not equivalent quality and no performance claim (alpha overdraw may be expensive). No whole-bird anatomy, eyes, face, wing or feet produced. VTK images are not WebGL screenshots; no browser or physical phone validation this run. Next technical test: non-repeating soft clump texture atlas and normal-directed coverage, then real GLTFLoader alpha-cutoff/overdraw check. Independent professional chick sculpt remains unresolved. No payment, no fal generation submission.

## Archive and reproducibility
- [A/B executed source](run331-local/swatch.py), SHA256 40d31810495d982a84030e0fad20a61f2aab6ab962d063e56ad6ad2d214599dd; local Git blob and remote readback 7cda436e19003ee7f72458e6f6960f81697ba3c4.
- [C executed source](run331-local/swatch_c.py), SHA256 fa1e4f83c82b26654cf8e0999720e57707363b4337c015f08def92cd6d0ad4d9; local and remote Git blob b664055f3d46a2adbb4219b2d6e63300e3cfa9ef.
- Run xvfb-run -a python swatch.py and swatch_c.py in an isolated directory with installed dependencies. C montage crop from 1200x800 to 1200x400 removes unused black row. Local A/B montage SHA256 216b96b5cf25dee7e245866675e84e091c9d00296ab263e182d83e54152026dc; cropped C montage e24db6cc306e369cae53a095318b91b39dbcf773bb311891d0c6d343e425b383.
- [Actual nine-view tiny thumbnail](run331-local/actual-nine-view-tiny.jpg.b64) is 90x90 JPEG, 1696 decoded bytes, SHA256 807a2f3cad39ea759179023e044a0a59c601859f9c00285a0a561a134a266634. Encoded text local and remote blob b2ce5785171912e942e333eab75ca565fc8a3a79, 2264 characters, exact readback. Decode with base64 -d. Rows A/B/C, columns top/oblique/near-side. Full-size renders and GLBs generated locally but not uploaded; reproducible source, measurements and tiny actual image archived.
- Research branch only. No main, concept, production, kitten prototype, or deployment modifications. New research swatches=3, new whole chick models=0, approved=0. NO_RELEASE.
