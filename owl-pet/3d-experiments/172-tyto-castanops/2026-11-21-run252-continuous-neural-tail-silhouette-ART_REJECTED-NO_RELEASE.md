# #172 Tyto castanops v3 — Run252: learned mesh continuous posterior cage / inversion boundary

**2026-11-21 (Asia/Shanghai). 3D research only. ART_REJECTED / PHONE_UNTESTED / NO_RELEASE.**

## Pre-flight / source of truth

Read `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, the Run251 audit, Run251 exporter and seven-camera workflow, and used the *actual binary Run251 A* from completed GitHub Actions 44798375236 artifact 14658854894. ZIP 7,144,988 bytes, SHA256 `f0f078c6a1b08f96f19ce6f9abb7df6990a48c274a919ffcb1a8e9f1c8da8b73`. Extracted the **native 4,035,000-byte Run251 A dark-eye repair GLB**, whose SHA256 is pinned by Run252 at `cd1513ac0822eef25bb56f9f8d08d244cac64d209ea8c92333693d287c926eb6`. This has **9 original scene meshes, 85,009 real triangles**, a single watertight learned body surface (34,000 triangles), six explicit eye meshes, actual surface down and horizontal tree support. This is not SVG / camera-rotated sprite / basic primitive owl.

Target remains the rightmost #172 v3 concept's soft cream down juvenile, natural heart face, short down-hidden wings, tail not exposed, credible 360-degree anatomy and natural eucalypt hollow supporting both feet. This study **does not** certify those qualities. Earlier Run248–251 had rejected simple wing/volume cuts; Run251 B particularly creates a pointed posterior stump.

## Actual local experiment and independent mesh-level checks

Used local free NumPy 2.3.5, Trimesh 4.11.1, VTK 9.6 offscreen renderer and Pillow 12.3.0; the authentic GLB was loaded, its learned **continuous 3D vertices were moved**, and its existing 3D down vertices followed the **same continuous deformation field**. The eye meshes, PBR dark irises and pupils, original topology, feet/front protection and wood stayed in place. Source vs new versions were actually rendered from front, left, back and right (12 true VTK camera views across source, C, D). No new owl assembled from spheres.

The rear-only deformation combines a smooth posterior mask with a head/disc protection field, a genuine X-width silhouette adjustment and Z-direction shortened posterior. Height remains untouched to avoid Run249's unsupported floating tail and preserve foot contact. `C`: 0.23 back shift, 0.08 width parameter. `D`: 0.30 back shift, 0.10 width parameter. Aggressive variant `E_REJECT_FLIP` (0.37/0.13) is a **hard geometry reject**, not an exported release candidate: introduced **2 inverted core triangles** on the original learned mesh. Earlier local raised-rear exploratory variant A caused a floating tail, and variant B had flipped triangles; neither was promoted.

Real exported local `C`: **4,035,000 bytes**, SHA256 `65446c4c93da72c51e3fe69e6a652fadaab4ea4d556e8ba23ad1c2678a87c01f`, 9 meshes, 85,009 triangles, 11,142 moved core vertices (threshold >0.01), max displacement 0.23189, **0 inverted core triangles**, watertight; learned-body volume **-14.439%** from source.

Real exported local `D`: **4,034,984 bytes**, SHA256 `d4e39ae4243fe9bbef4e34659959fbd2a07e60dc8f376d7ccfa2c1e43aa5b2ef`, 9 meshes, 85,009 triangles, 11,486 moved core vertices (threshold >0.01), max displacement 0.30226, **0 inverted core triangles**, watertight; learned-body volume **-19.093%**.

Source and both versions were re-imported as GLB. The updated back silhouette is a **real 3D geometry change**, but side renders reveal an unattractive **upper rear hump and still unmistakably adult long folded wing**. Both variants also retain sparse/flat back down, a too-firm face and a boxy carved ledge. **C and D are both ART_REJECTED; no visual progress claim.** The invert-free limit is important: pushing this specific field harder introduces triangle flips before creating the desired juvenile anatomy. Do not incrementally keep squeezing the adult-derived shape.

## External no-additional-charge source research (not adopted)

Additional live checks on 2026-11-21 located a royalty-free `Free Baby Owl Sculpt` page with a **no-AI restriction**, so it was not ingested as a generator/reference/derivative donor. An explicit CC0 `Grab3D owl` high-detail download is a **great horned adult** with ear tufts, ~400–800k triangles, not *Tyto castanops* juvenile; not fit for this character/mobile target. The Sketchfab `kenchoo Owl` advertises **CC BY-NC** and is not treated as a general commercial-safe donor. No external money spent or provider credits invoked. Sources:
- https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt
- https://grab3d.com/models/animals/owl/
- https://sketchfab.com/3d-models/owl-86ec461ab6404628b10fcdc26ac004dd

## Remote and mobile restrictions

Dedicated Run252 workflow reproduces the pinned native GLB on free GitHub Actions, should generate C/D, independently reject E on triangle inversion, and run Chromium/Three.js **seven genuine 3D cameras each**. The artifact should carry the real GLBs, raw browser images, full integrity reports; research branch should retain only machine report and 14-view **ART_UNAPPROVED** evidence contact. **Remote status must be checked against the actual run/artifact after completion**; do not treat script submission as execution proof. Local VTK is not real Android/iPhone WebGL GPU. No FPS, memory, heat, touch or phone deployment claims.

**Release gate: NO_RELEASE. No main merge, no 251-species production flow changes, no prior cat prototype edits, no new paid services.** Further credible progress calls for genuinely infant-specific authored/neural sculpt with buried short wings and multilayer fine down, not additional smooth rear deformation.

