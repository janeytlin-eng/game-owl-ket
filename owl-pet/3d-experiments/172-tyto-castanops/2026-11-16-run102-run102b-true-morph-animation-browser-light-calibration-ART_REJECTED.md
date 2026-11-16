# Run102 + Run102B — genuine #172 neural 3D animation + calibrated WebGL lighting — **ART_REJECTED**

**Date:** 2026-11-16, Asia/Shanghai. **Status: research-only / no release / no user success notification.**

## Preflight and source audit (completed before edits)

Reopened repository instructions and owl-pet README; verified the prototype is still a small-cat WebGL code snapshot, **not** an owl pet. Checked the actual original design plate \`owl-pet/design/concepts/172-tyto-castanops-v3.png\`, especially the **rightmost** unknown-age creamy second-down chick; examined Run100's genuine front/quarter/side/back Blender Cycles contact and read Run101's failure audit, native mesh edit and Blender camera scripts. The reference has bright symmetrical dark OPEN eyes, a broad softly bounded heart-shaped face, generous cream down with soft silhouette, very short concealed wings, and two feet **resting** on the wide eucalyptus hollow lip. In contrast, Run100/101 neural output remains a hard feathered, elongated, low-visibility-eyed adult-like sculpt with airborne claws and no support. The original image is a front-biased concept and is **not evidence of anatomical correctness from unseen sides**.

An independent Tasmanian masked owl chick field photograph (for anatomical observation only; **do not copy image or texture**) is [Luke O'Brien, Young Masked Owl at the Raptor Refuge](https://www.lukeobrien.com.au/young-masked-owl-raptor-refuge). Photography demonstrates short, irregular soft second-down volume, rather than the hard overlapping plates in the neural mesh. The exact \`Tyto castanops\` taxonomy and chick age remain design/source qualifications, not invented measurements.

## Run102 — actually generated a morph-animated real 3D GLB

Unlike prior simple vertex-color/deformation attempts, this run added two **actual glTF deformable mesh morph targets**, independent Blender shape-key animation curves and a closed motion loop to the *existing real neural-generated 80k-face model*. It did not replace the bird with procedural egg geometry or 2D cards.

- Confirmed SHA256 of input Run100 smoothed Hunyuan GLB: \`60feb7a5e4f4c67a020e3457e7ffbfb52f6fbe3e75f115b970030c00b20cd35d\`.
- On **39,684 real bird mesh vertices**, subtle breathing edited **20,101** actual vertices; upper neck/head tilting edited **10,034**. Measured maximum edit distances were 0.02306 and 0.04458 in source GLB coordinates. Shape deformation was kept continuous and toes reasonably stable.
- Native Blender/glTF binary export and reimport verified **79,988 triangles**, **three shape keys including basis**, **two glTF morph targets**, **one animated weights channel** and **one actual GLB animation clip**. Model size **2,814,060 bytes**; SHA256 \`70805cb82f54d730d1851ef73a787e0e0dcb4531ef149cb45eaca959fc2feaae\`.
- Generated and directly inspected four **native Cycles renderings** (front/quarter/strict side/back) from the reimported true 3D geometry, NOT fake rendered stand-ins. The geometry still has closed/indistinct eyes, an overly small inset heart disc, coarse rigid scaling, an elongated side body, claws without a tree hollow, and no layered cream down.
- Imported the resulting GLB into a genuine Three.js WebGL2 scene in **desktop 1280x720** and **phone-size 390x844 Chromium viewport simulation**. In both cases the animation clip loaded and animated morph weights changed (sample range ~0.99), model rendered, pointer orbit changed the camera, the subject stayed in frame and software WebGL reported \`glError=0\` with no page errors. These tests used Linux **SwiftShader software graphics**, *not a real smartphone GPU*, and synthetic pointer motion, not physical multi-touch/haptics.

[Run102 CI actual execution](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43803093632) and the isolated \`research-evidence-run102-REAL-NEURAL-MORPH-ART_UNAPPROVED/\` repository directory contain the original generated GLB, all four renderings, two actual browser screenshots, native mesh and browser metrics, checksums and run logs. All 14 evidence entries in \`checksum_validation.log\` are OK.

## Run102B — actual browser-image lighting iteration using same real animated GLB

Direct visual inspection of the **actual** Run102 desktop/phone screenshots showed excessive white exposure, washing away what little face/wing sculpt detail the source retains. On a fresh independent research branch, Run102B reused the **byte-for-byte identical SHA-verified** animated 3D GLB, reduced Hemisphere/key/fill intensity and applied ACES Filmic tone mapping with exposure 0.82 in Three.js. It then **re-ran** desktop and emulated phone-size WebGL2, animation, orbit and framing tests and captured two new browser screenshots.

- Both new WebGL2 software cases passed genuine runtime checks: loaded animated GLB, changing morph weights (sample ranges 0.999 and 0.9931), mouse orbit, model framing, zero gl errors or application/page errors.
- Independently checked **actual screenshot pixels**, not theoretical lighting. The threshold-mask mean visible subject RGB shifted from **(213.65, 206.00, 188.82)** to **(161.73, 148.77, 131.22)** on desktop, and **(212.01, 204.56, 187.90)** to **(162.08, 149.38, 132.18)** at simulated phone size. Visual inspection confirms the washed-out near-white mass has become darker, more legible cream/grey sculpt shading.
- **Do not misreport** the near-white-per-subject percentage as a clipping improvement: the threshold subject-mask pixel counts differ substantially between lighting setups, and that fraction increased numerically. The useful verified change is restored shadow contrast and lower mean brightness, **not photorealistic down or an accepted new sculpt**.
- No real iOS/Android hardware, device-power benchmark, animation frame pacing, actual touch gesture or memory budget certification has been done.

[Run102B execution](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43803552555). The separate \`research-evidence-run102B-WEBGL-LIGHT-CALIBRATION-ART_UNAPPROVED/\` directory contains the two new real browser screenshots, measured pixel comparison against Run102, software WebGL runtime metrics, hashes and checksum verification (all entries OK).

## Art, rights and production gates

**ART_REJECTED for both.** The animated bird is still an unacceptable hard-shell/owl statuette compared with the actual v3 **plump, fluffy, awake** juvenile. Animation and PBR calibration are useful *technical* increments only; they do **not** repair eyes, anatomy, wing/down grooming, realistic rooted feet, eucalyptus hollow or trustworthy side/rear features. Never claim a complete owl-pet preview.

The model inherits **Tencent Hunyuan3D-2 Community License** restrictions, not a CC0 grant. [Official Tencent Hunyuan3D-2 LICENSE](https://github.com/Tencent-Hunyuan/Hunyuan3D-2/blob/main/LICENSE) explicitly restricts territory and output uses: global publication cannot be presumed lawful. Do **not** deploy this derivative or substitute a misleading low-quality stand-in.

**Cost charged:** $0. Both experiments used free GitHub Actions, Ubuntu Blender 4.0, local Three.js and software Chromium; no paid services or unapproved spending. Compared research branch to \`main\`: **all 142 changed paths** are restricted to \`owl-pet/3d-experiments/172-tyto-castanops/\` or dedicated \`.github/workflows/owl-pet-172-...\` workflows. Root vocabulary game, 251-species production/manifest process, v3 original concept, old prototype and live site were not modified.

**Next concrete blocker:** a genuine aesthetically approved juvenile sculpt with naturally groomed second-down and independently checked side/back plus a grounded support. Only after visual acceptance should real device GPU/memory/touch/animation quality be certification-gated. This run's evidence conclusively validates morph animation and basic browser playback **only**, not final character quality.

**Disposition:** **NOT RELEASED — SILENT RESEARCH ARCHIVE.**
