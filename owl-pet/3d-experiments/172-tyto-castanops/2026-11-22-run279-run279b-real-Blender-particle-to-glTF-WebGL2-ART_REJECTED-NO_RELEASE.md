# #172 *Tyto castanops* v3 — Run279 + Run279b genuine Blender hair-groom → native glTF mesh / Chromium WebGL2

**Date**: 2026-11-22 (Asia/Shanghai). **Verdict**: **TRUE_BLENDER_PARTICLE_PATH_TO_REAL_GLTF_MESH_PASS / 390×780_CHROMIUM_SOFTWARE_WEBGL2_PASS / ART_REJECTED / PHYSICAL_PHONE_UNTESTED / HUNYUAN_NONCOMMERCIAL / NO_RELEASE**.

This is an independently archived negative-control/technical research record, **not** a release asset. Target remains the **right-hand cream-white fluffy juvenile in #172 v3 concept**: natural heart-shaped facial disc, dark small eyes, genuinely round juvenile body, folded short wings, soft layered down across side/back, natural two-foot hold on an aged eucalyptus hollow, and viable mobile WebGL.

## Mandatory repo and source postflight

- Re-read `owl-pet/AGENTS.md`, README, STATUS, current old `prototype` description, and **Run278 source grooming audit**. Run278 Blender native hair was real and visible in Cycles, but its exported GLB contained **exactly the original 133,268-triangle body; 12,000 Blender particle hairs entirely absent from glTF**. The adult-proportioned Hunyuan-derived body failed art and has noncommercial source restrictions.
- Started the entirely separate research branch `research/owl172-run279-hair-gltf-surface-transfer-NO_RELEASE` from the Run278 audit commit `82360b81489334e1cd1e44efaf0dd99883174909`; no main, species manifests, production scripts, source concept art, cat prototype or deployment edits.
- Reused **the actual previous editable Blender groom** from GitHub Actions Run278 artifact, checked exact source SHA256 `2bcdadbc65cf197b1f07f52ab9c3406752098abd86a808848f6ed5deecfa1907`; no substitute sphere/SVG/synthetic 2D representation. Source contains 66,596 vertices / 133,268 triangles and 12,000 particle parent paths, with six underlying hair keys per particle. All 12,000 native particle trajectories passed finite-length filters; 100% of their first points are within expected mesh bounds.
- No paid services, quota requests, purchases, authentication bypass, or alteration of protected upstream project files.

## Run279 — actually build glTF *geometry* from actual native Blender particle paths

Genuine Blender 4.0.2, system NumPy and Cycles installed in the isolated Ubuntu 24.04 GitHub Actions environment. New research-only Python code reads `ParticleSystem.particles[*].hair_keys` **from the authenticated editable Blender scene**, decimates that sample into actual 3D curved/tapered ribbon geometry, and exports it as a separate real mesh primitive alongside the original continuous organic body. This **does not** export the original Blender hair shader, child interpolants, or physical soft-fiber scattering. It is a legitimate geometry transmission test, not a claim of realistic final feathers.

Two true GLB variants were actually built, exported, reimported and independently counted:

| Technical variant | Native body triangles | Hair-path triangles | Total glTF triangles | Bytes | SHA256 |
|---|---:|---:|---:|---:|---|
| Full research | 133,268 | 19,200 (3,200 extracted parent paths) | 152,468 | 4,592,816 | `d4c3cb75e747af17d2e2b04bc4b6a7a91ca4bd4d55b9e79dd0573b7420608bb9` |
| Decimated mobile *candidate* | 55,972 | 9,600 (1,600 paths) | 65,572 | 1,663,256 | `8eb64c09a58f673c793c31e348f41854b5d4fb13c649afcef36d1a23129e12db` |

- Each actual GLB includes **two native mesh primitives**, the source-derived anatomical body and the geometric groom; independently parsed binary glTF JSON and reimported via Trimesh. `NORMAL` is present on both; the groom uses physically separate matte-cream PBR material and is double-sided. These are actual, different 3D geometries, not 2D turntable frames.
- The low-detail version actually applies Blender's mesh decimator to the continuous body; its triangle count is smaller in glTF and in independent Trimesh import. It is a **mobile candidate only**; no published budget, real hardware, VRAM or thermal success is implied.
- The actual LOD scene was rendered through Blender Cycles CPU at four spatial azimuths (0,45,90,180°). All images were reopened independently. They are **different 3D views**.

**Run279 real execution**: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44957716797 (all build/inspect/archive steps succeeded).

**Original research artifact (temporary)**: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44957716797/artifacts/14728237949 . Independently downloaded ZIP size **6,240,862 bytes**; GitHub digest / local SHA256 both `959943917988d445739b9c1148ea8829e52980ddb2e32edef67eadac8518f9e4`; **13/13 ZIP files CRC valid, 11/11 manifest SHA256 entries passed**. Contains actual editable `.blend`, two true GLBs, four 3D images, full real execution log, source-path report, binary structural audit and `NO_RELEASE` marker. GitHub currently reports expiration **2026-12-12 22:38 UTC**, not permanent publication.

## Run279b — actual Three.js Chromium browser test of the *same* mobile GLB

Separately recovered the exact exported LOD from Run279's GitHub artifact; SHA256-checked it against the previous real Blender output. Used genuine headless Chromium, Three.js `GLTFLoader`, actual WebGL2 context with SwiftShader launch options and a **390×780 canvas**. Captured front, front-quarter, right, back, left, top and bottom snapshots from distinct camera transforms. All seven viewport images had different SHA256; the bounding-box projections fit inside 90% of normalized screen, without accidental crop. WebGL reports **65,572 triangles, two actual mesh objects, zero missing-normal mesh objects, no page errors**. **10/10 declared browser technical checks passed.** The `gl.RENDERER` string is generic `WebKit WebGL`; launch requested ANGLE SwiftShader but is **not** an independent physical GPU identity attestation. This is software-browser loadability only.

**Run279b actual execution**: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44957944731 (all stages succeeded).

**Original browser research artifact (temporary)**: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44957944731/artifacts/14728601270 . Independently downloaded ZIP size **6,739,326 bytes**, digest/local SHA256 `5dd6f84e31ec8449417678fa31f0812ea3a301b61044deabcc265a6af4782415`. **23/23 ZIP files CRC valid, 21/21 manifest SHA256 checks passed**. Contains **seven actual Chromium screenshots**, WebGL report, the same two source-derived native GLBs and source render images, logs, `.blend`, checksums and `NO_RELEASE` status. GitHub currently reports expiration **2026-12-12 22:41 UTC**.

## Independent visual acceptance: explicitly REJECTED

I independently opened the four Run279 Cycles views and the seven actual 390×780 Chromium screenshots. The positive finding is **GLB now genuinely contains converted hair geometry**; the visual result, however, has **hard, thin, disconnected porcupine-like bristles**, not thick soft down. Browser view makes this very conspicuous on the head and shoulders. The face appears too hard and pale, without naturally integrated dark juvenile eyes and an appealing soft heart disc. Side view is an adult-like inclined wedge with long hard folded wings; back is a featureless rough shell plus bristles. Claws are exaggerated and appear to float without a credible old eucalyptus hollow. No rig, idle/blink animation or actual pet interaction is present in this new model.

The four Cycles frames and seven WebGL2 frames agree that this still fails the requested reference, even though GLB transfer now works. **Do not publish or embed it in a consumer-facing pet experience.** Merely achieving mobile viewport rendering is NOT mobile quality or artistic acceptance.

## Gate discipline / next engineering choice

- **YES**: open-source Blender edited scene; original hair trajectory extraction; GLB contains actual nontrivial feather-path triangles; independent native GLB parse/import; full/LOD pair; four distinct actual Cycles 3D renders; seven distinct actual software WebGL2 camera captures; source and integrity hashes; branch-scoped research archive; zero external spend.
- **NO**: dense creamy *soft* down; rounded juvenile anatomy; dark expressive eyes; short soft wings; coherent side/back feathers; eucalyptus hollow two-foot contact; physically measured Android/iPhone GPU FPS, memory, touch, battery/thermal performance; verified commercial license; animation/interaction.
- Technical lesson: direct particle-path-to-mesh conversion fixes Run278's **hair-absent glTF** failure, but visibly loses the particle system's soft shading and child-density effect. The resulting sparse ribbon spikes are **not a usable solution to the character art problem**; do not spend successive runs simply raising strand count on the same adult donor. A properly sculpted, legally usable juvenile artist mesh, with carefully authored soft feather textures/geometry and real mobile verification, remains prerequisite.

**Final: TRUE_HAIR_GEOMETRY_GLTF_PASS / SOFTWARE_WEBGL2_390x780_PASS / ART_REJECTED / SOURCE_RIGHTS_NONCOMMERCIAL / PHONE_UNTESTED / NO_RELEASE.**
