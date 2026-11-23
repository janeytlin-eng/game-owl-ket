# #172 *Tyto castanops* v3 — Run311 original continuous organic sculpt, two actual local meshes and six-view art rejection

**2026-11-23 Asia/Shanghai | NATIVE_GLTF_GL B_LOCAL_IMPORT_PASS / SIX_REAL_VTK_3D_ANGLES_PASS / ART_REJECTED / BROWSER_WEBGL2_UNTESTED / PHYSICAL_PHONE_UNTESTED / NO_RELEASE**.

## Preflight and isolation
Actually reread `owl-pet/AGENTS.md`, `README.md`, `STATUS.md` and the full Run310 artist-native asset access audit; inspected the Run310 Paint3D alternative and current 3D-tool availability. `main` contains only the original kitten prototype, not an owl model. The animal is #172 v3's **rightmost cream-white downy juvenile**, not an adult Tyto or horned-owl mesh. Young chick's exact age remains unknown. The 251-species production process, concept image, original game, prototype, manifest, main, and deployment have not been touched.

Previous research had rejected adult donor meshes, neural grey hard shells and generative site authentication/availability problems. This attempt instead produced a **new** organic signed-distance-field sculpture in free Python (NumPy, SciPy, scikit-image, Trimesh, VTK, PIL). Marching-cubes iso-surface unifies head, cheeks, body, chest and short buried wings into one watertight contiguous organic shape; it was reduced to 28k core triangles. Real geometry-based swept hooked beak, dark eyes, short legs, curved toes and surface-attached spatial down ribbons were added. Not a single-plane rendering, SVG or photograph, nor a paid asset.

## Exact actual local outputs; independently GLB-reimported and six software views inspected
| Metric | Run311 A original | Run311b revision |
| --- | --- | --- |
| GLB bytes | 1,179,068 | 1,651,976 |
| GLB SHA256 | `b4f2aa621a9741dc5ddaf753cba768e6765c0d632f879cf326ecbe35cb2308fe` | `6c25fc45e10dacc5ba2a50d4dfc9ad3751453b500e2ced5d6396220630f7e199` |
| Real triangles | 49,452 | 61,683 |
| Mesh components | 27 | 27 |
| Explicit 3D surface down segments | 4,552 | 8,629 |
| Watertight organic main body | true | true |
| Camera render | front, 3/4-front, right, 3/4-back, back, left | same six views |
| Art review | **REJECTED** | **REJECTED** |

Revision B actually changed organic head/body proportions and surface roughness; reduced simulated hair spike length, increased its density and fixed unlit hair-render dark flecks; reduced spherical eye and nose protrusion; strengthened lower facial-disc V contour; retained all six spatially distinct views. B has a softer body outline and less prickly down than A. It is still not a professional juvenile barn owl, though: a rigid white collar and overly round cartoon eyes replace the *Tyto* heart-shaped feather-disc geometry. Side/back remain too smooth, without well-sculpted short wing/shoulder feather layers, and the tiny white fur points resemble flecked plastic, not fluffy down. Feet do not naturally grasp a hollow branch. Even at 61k triangles, polygon count is not evidence of artistic realism.

**Never promote either GLB to an approved character.** Free rendering is a negative control, not qualified art. Physical Android/iPhone FPS, memory, thermals and touch untested; local VTK screenshot is **not** browser WebGL2 evidence.

## Evidence preservation and rights
Local standalone ZIP `owl172_run311_evidence_ART_REJECTED.zip` was generated (5,400,870 bytes, SHA256 `958a799e0ac6351e12b2361fc1e166b166fdfd2819356542678558cd8cec6a86`, 21 files, ZIP CRC check passed). Contains both original native GLBs, two actual generating scripts, two proof reports, 12 view PNGs, two six-view contact sheets, and this audit. File-library persistence was **actually attempted** but both `/Research/Owl172/Run311` folder creation and ZIP upload returned `AccessDeny`, so do **not** claim the ZIP is already persistently archived there.

The matched original source of revised B is in the neighboring compressed, hash-identified Python source file (`sculpt_run311b.py`, original 13,008 bytes, SHA256 `9e630af2b50b86709cbbf878a41b6e8a8beb45de97c1453902f98699aa56ecf5`), intentionally retaining full reproducibility without placing unapproved binaries into production. A separate research-only GitHub Actions job can reconstruct source and save remote research evidence if it completes. No commercial donor meshes, no new external API credits and zero external spend. The source uses no proprietary donor.

## Gate and next priority
`AUTHENTIC_NATIVE_GEOMETRY_PASS / LOCAL_6_VIEW_PASS / TRUE_DOWN_QUALITY_FAIL / HEART_DISC_REALISM_FAIL / SIDE_BACK_FEATHER_LAYERS_FAIL / NATURAL_FOOT_GRIP_FAIL / REAL_WEBGL2_UNTESTED / ART_REJECTED / NO_RELEASE`.

**Stop iterative procedural hard-plastic refinement as a product candidate.** Need expert organic sculpt, physically believable short fine down grooming, careful reference-matched facial sculpt and real phone renderer validation. Avoid repeating user-rejected geometric assembly. This is a small reproducible negative-control in independent `research/` only; the 251-species production pipeline remains unchanged.

## Final independent GitHub Actions execution and actual ZIP/open-image audit (2026-11-23)

A first wide-checkout attempt ([Run #45096802999](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45096802999)) became obstructed by the oversized repository checkout; it was replaced with a narrowly sparse-checkout job. The next [Run #45096867637](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45096867637) **failed** with VTK `Failed to load EGL`, `libOSMesa not found`, then process `Segmentation fault (139)`. The GLB generation stage did not count as a full run because the real six-view render had crashed. Fixed runner by installing `libosmesa6 libegl1 libgl1-mesa-dri xvfb` and executing under `xvfb-run` with a real X screen, while preserving `pipefail` and an exact sparse checkout.

The corrected [Run311b GitHub Actions **#45096949795**](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45096949795) **completed successfully**, including real source reconstruction and SHA, native 3D generation, six offscreen rendered views, independent Trimesh GLB import, 6-view uniqueness and research artifact upload. The remote exact original source was **13,008 bytes, SHA256 `9e630af2b50b86709cbbf878a41b6e8a8beb45de97c1453902f98699aa56ecf5`**. The regenerated remote GLB was **1,651,940 bytes, SHA256 `557fa0ff2f95251f0da2c8ab20dd63a35803f60d6a975ec07f84550f91274225`**, with **27 geometric components and 61,683 triangles**. A 36-byte difference from the local B GLB is consistent with differing package/environment serialization, and is not silently claimed to be byte-identical; geometry and six-view technical gates matched.

The real remote [Run311b NO_RELEASE research artifact #14782983757](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/45096949795/artifacts/14782983757) was **actually downloaded** back from GitHub, not merely inferred from job success: 2,734,987 bytes, exact GitHub digest **SHA256 `fcee624060abd99d16fe42c4c0019d6b7c033445d858bc392d0ace74e5e1314a`**. Independently opened ZIP: **12 entries, 12/12 CRC valid**, including native GLB, source, model proof, execution log, six individual PNG views, six-view montage, and remote evidence gate. The gate JSON explicitly records `NATIVE_GLB_PASS_SIX_3D_VIEWS_PASS_ART_REJECTED_NO_RELEASE`, `browser_webgl2: NOT_TESTED`, `physical_phone: NOT_TESTED`, and `release: false`. Artifact expires **2026-12-07 01:52:38 UTC**; do not confuse temporary Actions storage with a permanent user-library upload.

**Manually opened the ACTUAL remote montage (1200×2100)** and inspected front, quarter, true right, quarter back, back and left. It is physically three-dimensional but still aesthetically unsuitable: front has large round plastic eyes rather than natural Tyto heart mask; projecting beak and huge round head evoke a stylized toy; right view shows protruding disconnected-looking eyes and beak, and mostly featureless soft-plastic side; rear has weak sculpted short wing/shoulder layering and sparkle-like fake down; feet don't grip a hollow eucalypt limb. **Actual remote art gate = REJECT**, not approved or released. No actual Chromium WebGL2 or physical smartphone test of this generated asset; those gates cannot be awarded from VTK software rendering alone.

**Isolation rechecked:** GitHub compare with previous Run310 branch found exactly three added research-only files (this audit, exact compressed source, and dedicated no-release workflow). No 251-species production edit, no main change, no deployment, no purchase. Persistent user Library remains blocked by real `AccessDeny`, as previously documented. Source and audit archived on separate GitHub branch; remote binary remains available only as an expiring NO_RELEASE research artifact.
