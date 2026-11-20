# #172 Tyto castanops v3 — Run250p real neural screened-Poisson wing relief inpainting

2026-11-21 Shanghai. **RESEARCH ONLY / ART_REJECTED / PHONE_UNTESTED / NO_RELEASE.** No main, 251-species pipeline, kitten prototype, or deployment edits.

## Source, specification, actual previous evidence

Read owl-pet/AGENTS.md, README.md, the science and age boundary in species/172-tyto-castanops-v3.md and Run248/Run249 audits/code. Downloaded Run249 GitHub Actions artifact 14644778185 (ZIP 7,314,754 bytes, SHA256 00984d2f39e86a14fa4b97c3e7de6cde6a6080e449477e6765f3faf5b6213f16, CRC all pass); actually opened its 14 true-browser-view comparison. Downloaded Run248 source artifact 14641598902 (ZIP SHA256 b96c2ba1eb35e4783d38ed900a322993b9607f555e567881fbfa334c54c32a53, CRC all pass). New trial based on actual native Hunyuan Run248 A GLB, independently SHA256 pinned at 247d820538920735783072a204686fcf2f02ddb3ce1958a5472895a3ed7c1845.

Target remains far-right age-unknown cream-down juvenile: a soft heart disc, rounded low body, short buried wing, completely concealed tail, both feet supported on wide weathered eucalyptus hollow, credible side/back, smartphone WebGL rendering. Exact age unsupported.

## Genuine 3D performed; not a geometry-primitives fake

Unlike repeated wing-tip squeezing in Run248/249, implemented sparse screened-Poisson side-relief inpainting on the *actual* 46,856-triangle learned continuous neural owl mesh. Uses triangle-adjacency Laplacian, SciPy sparse factorization and gentle spatial masks that protect face/eyes and toes; preserves 36,651 original down-card triangles by transferring actual mesh-surface displacement, plus six true anatomical eye meshes. Includes a little chest fullness, does not recreate the bird from spheres or SVG. The existing Y-up ledge is retained unchanged.

Generated and re-imported two native GLB models locally with Trimesh. Each has 9 real mesh objects, 131,835 triangle faces, unchanged neural core face indices, 0 inverted core triangles and finite vertex coordinates. Exact local results:

| Model | Actual GLB bytes | SHA256 | Wing mask vertices >0.3 | Maximum actual core movement | Mean active wing movement | Protected face displacement |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| A | 4,946,016 | db71792b805e9d777f7d52d0cc53135a2d5ff2cb96f8b6ac5c76903abccd847e | 6,210 | 0.03988 | 0.01196 | <0.000001 |
| B | 4,946,016 | 347bc9adde7a7caa3ca48072199975bc9a4b1bd2afcdb92a5f6c73fadfe2d0ec | 6,210 | 0.06704 | 0.01818 | <0.000001 |

Local data are not presented as remote evidence until independently verified.

## Actual source/A/B art inspection: REJECTED

Used Xvfb/VTK for 12 genuinely different three-dimensional camera views (source/A/B × front/side/oblique/back), opened and compared the rendered image. Screened-Poisson B softened parts of raised remige surface but retained the obvious adult long-side-wing anatomy. Head/mask and eyes are too rigid, body too tall, lack of dense fine juvenile down, rear too plain and lower part too long; inherited shelf looks like carved beige stone rather than a weathered tree hollow. Front/threequarter scarcely changed. Local back render has poor lighting and is not evidence of a black model. Neither variant meets design; DO NOT PROMOTE B.

This confirms that improved fairing still cannot reconstruct short embedded juvenile wings. The independent technique avoids Run249's rear-wing horizontal flange but does not yield a acceptable chick.

## GitHub remote experiment and source isolation

On branch research/owl172-run250-laplacian-wing-relief-inpainting-art-reject-no-release created the exact native generation script run250_surface_inpaint.py and dedicated workflow owl172-run250-native-neural-relief-inpaint-webgl.yml. Workflow retrieves original Run248 native model by pinned hash, builds two new native GLBs, tests real Chromium Three.js GLTFLoader from seven true 3D camera positions per variant, hashes all raw screenshots, creates 14-view contact, archives raw GLBs/screens in time-limited Actions artifact and commits only research reports/image. Run https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44793056131 . As of audit creation the run was still active; **do not infer remote PASS until completed and independent artifact checked**.

Also discovered separate concurrently completed Run250 true volumetric remesh research run 44790702174 and downloaded its original ZIP (SHA256 ab0e7c3d6a380bffa31167d6b634cef4c8d9830b43b8a9169f471dc802635081). Its neural-core topology replacement lowers scene to 85,009 triangles and experimentally improves bark PBR, but the true browser front/side/back still shows too-tall adult silhouette with long posterior; it is also ART_REJECTED. Our inpainting negative control is distinct, not a replacement baseline.

Phone Android/iPhone GPU FPS/thermal/touch/memory are UNTESTED. Additional paid spend $0. Main, the 251-species species/design production, kitten prototype and deployment remain untouched.

## Next necessary work

Stop pretending repeated local fairing, remige shortening, extra hedgehog cards or indiscriminate voxel smoothing will pass the art gate. Need a genuine professionally designed child-specific short-wing anatomy source, soft multi-layer cream down, softer developed heart-disc, credible rear and realistic tree hollow. Then test mobile LOD/performance on physical hardware; **NO_RELEASE** until verified.


## Completed remote QA and final independent visual rejection (2026-11-21 Shanghai)

The initial GitHub Actions run [44793056131](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44793056131) **failed in browser step**, not in native geometry generation: Bash expanded an unquoted label suffix as unbound variable V_real_mesh_RESEARCH_ONLY. This failure is preserved. Corrected the dedicated workflow variable interpolation in commit fe4c765eabadbde214ba5dbe880441d920f14cbe and ran the [fixed remote workflow 44793675946](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44793675946) to completion: **SUCCESS**. Both real GLB regenerations and 14 real Three.js Chromium WebGL2 screenshots succeeded.

Independently downloaded actual [original successful Run250p artifact 14657392183](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44793675946/artifacts/14657392183) and verified ZIP **7,326,398 bytes**, **SHA256 69df3ead77b3b59e5bb587b1fa94a82ed31e76f562a71d8ee99b91c316c19850**, matching GitHub artifact digest. All **22 ZIP entries** passed CRC checks. Actual binary GLBs were separately reloaded in an independent Python/Trimesh environment: A/B both **4,946,016 bytes**, SHA256 exactly matching the local table, **9 real meshes**, **131,835 native 3D triangles**, 46,856 learned neural core triangles, finite normals, and PBR materials. For each variant, the browser machine report independently verified **10/10 software WebGL2 QA gates**, all **7 unique camera views**, no blank/failed screens and **all 14 screenshot SHA256** values matching original PNG bytes. Original 14-view contact SHA256: **345ae53519cfc221303300642fcd65dc798cbf377f9e942b62ac152a6c9336d4**. Source originals and screenshots are in the 30-day Actions evidence artifact; script, audit, machine reports and contact are committed on research branch.

I actually opened the remote 14-view contact, not just checking metadata. Compared it directly against the real #172 v3 repo concept image path owl-pet/design/concepts/172-tyto-castanops-v3.png (far-right age-unknown mesoptile). **Art still unambiguously fails.** In concept, the young has a truly wide fluffy cream body, high-fidelity brown-rimmed soft heart disc, large black eyes, very short entirely down-covered wings, concealed tail and two firmly supported feet within a real rugged tree hollow. Run250p A/B instead have a narrow tall torso, an obvious elongated embossed wing down the side, plain flat white rear and lower tail-like projection, hard and smaller-looking eye-disc, almost no long fine fluffy wisps, and a scalloped pale biscuit/stone stand. B's slight inpainting is not a new art baseline. Rear and side are coherent **as 3D objects**, not adequate as the desired **juvenile anatomy**.

Browser driver: **ANGLE SwiftShader software Vulkan/WebGL2**, not physical Android or iOS. Thus technical WebGL2 smoke PASS must **not** be called phone GPU PASS. Phone FPS, RAM, touch, overdraw and thermal are untested. Final verdict **NATIVE_3D_TECH_PASS / SOFTWARE_WEBGL2_PASS / ART_REJECTED / PHONE_UNTESTED / NO_RELEASE**. No user preview should be sent.

Verified comparison between this isolated branch and Run249: **exactly six research-scoped files added** (one dedicated workflow, one true neural code script, this audit, two JSON reports and 14-view research PNG). No changes to main, 251-species manifests/ledger/automation, kitten prototype, root vocabulary game or live deployment. No extra paid spend.
