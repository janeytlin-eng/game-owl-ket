# #172 `Tyto castanops` v3 rightmost juvenile — Run286 high-detail native donor test

**Date:** 2026-11-22 (Asia/Shanghai). **Verdict: REAL_NATIVE_3D_PASS / SIX_TRUE_VIEWS_PASS / ART_REJECTED / MOBILE_PHONE_UNTESTED / NO_RELEASE.**

## Read-first scope and previous attempt

Before running, re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/STATUS.md`, the existing WebGL kitten `owl-pet/prototype/index.html` and the [Run285 beak-contact research audit](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run285-native-beak-contact-diagnostic-NO_RELEASE/owl-pet/3d-experiments/172-tyto-castanops/2026-11-22-run285-native-beak-contact-ART_REJECTED-NO_RELEASE.md). This project is separate from the 251-species image production flow; `main`, the kitten, deployed site, original `#172` reference and production manifests must remain untouched.

Independent retrospective clarification: [Run285 remote attempt 44986810312](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44986810312) **did succeed** and produced [artifact 14740152588](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44986810312/artifacts/14740152588). The artifact was independently downloaded in this run: 4,650,345-byte ZIP SHA256 `63ad741e9ddab38ed68a90ef10c8a4e87b6e66dd91b313afd0e320c00e58af69`, archive CRC passed, its embedded `SHA256SUMS.txt` matched all listed entries. Actual six-camera beak comparison was opened. The prior report's "remote unverified" status should be treated as superseded for technical execution, **not** as art approval.

## Different route: actual externally made detailed owl, not another primitive sculpt

After repeated failures to achieve realistic layered plumage by modifying prior single-image neural and procedural sculpt bases, tested a free downloadable professional-grade native 3D donor to establish a more truthful geometry/texture quality baseline:

- Public source: [Grab3D owl listing](https://grab3d.com/models/animals/owl/); actual [source manifest](https://grab3d.com/dl/owl/manifest.json), [license](https://grab3d.com/dl/owl/LICENSE.txt) and [native light GLB](https://grab3d.com/dl/owl/owl-light.glb) were downloaded **without account creation or payment** on GitHub Actions. HTTP 200 and actual GLB `glTF` magic independently checked.
- Source GLB: **13,356,032 bytes**; SHA256 `fdcd83d53a5346eac8259a861614f5adae46ce7ad11e33919d05dd1bcd52aaba`. Independent Trimesh reload: **256,172 vertices, 399,999 genuine triangles, 1 actual mesh, real PBR material, embedded 1024×1024 texture**. Mesh is true 3D, no SVG/image impostor, not simple spheroid assembly.
- Geometry bounds approx. X -0.1442 to +0.1442, Y 0 to 0.5500, Z -0.1605 to +0.1605 in its native coordinates.
- Actual VTK GLTF importer software rendering produced six independent camera views at front, oblique, right, back, left and above, each 420×420; an assembled 1260×880 contact sheet was opened and inspected. **Visible geometry and patterns genuinely change in 3D across camera views.** Not just 2D rotation.
- Source's license file claims **CC0 1.0** but also discloses **AI-assisted Meshy generation with Blender cleanup**. This is a supplier claim; creator's rights and provenance are **not independently certified**, so do not treat it as product-ready licensed source.

### Real execution errors and resolutions

Initial workflow `44990538374` tried full repository checkout and failed. A second workflow `44990598317` used narrow sparse checkout and successfully fetched the native GLB, but Linux VTK could not open a rendering context (`Failed to load EGL`, `libOSMesa not found`); the shell pipeline originally masked the Python error. Its failed evidence artifact `14742205023` preserved the **actual** GLB and source records, not false success.

Updated workflow to install no-fee `libegl1`, `libgl1`, `xvfb`, invoke `xvfb-run` and use shell `set -euo pipefail`. [Run286 final GitHub Actions run 44990682353](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44990682353) then **completed successfully**; its real acquisition, six-view rendering, report and fail-closed steps passed. Independently downloaded [artifact 14741239442](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44990682353/artifacts/14741239442): ZIP **9,880,588 bytes**, SHA256 `513dabc038c9c6a6acf5121c123aaeb9fe01111a76d6ba7ea3c4066eb8b67db4`, matched GitHub's published digest; **16/16 ZIP entries pass CRC; 13/13 embedded source/output file hashes pass**. The actual GLB was again independently reimported and six-view image opened. Evidence artifact expected to expire on **2026-12-06**, so this is temporary research evidence, **not a release**.

## Actual art rejection

**ART_REJECTED without exception.** This candidate is a **dark brown, ear-tufted adult great horned owl**, not a heart-faced `Tyto castanops` nestling. Actual front view has conspicuous erect ear tufts and large yellow irises; real sides and back show adult long flight feathers and long tail, strongly articulated adult feet and mature proportions. Nothing like a cream-white soft-down ball, dark little eyes, natural heart-shaped facial disc, short down-covered folded wings and correct juvenile volume. The 3D side/back topology is more believable than previous primitive experiments, **but its species and age are fundamentally wrong**; it cannot be relabeled as the desired owlet. No old eucalyptus hollow grasp, behavioral rig, or animation was produced. **No user-ready demonstration should be published.**

A 399,999-triangle original mesh, though visually better textured, **has not been mobile-optimized**. This pass only used VTK software offscreen camera renders. It **does not establish Chromium WebGL2, Android/iPhone GPU, frame rate, memory, controls, thermal stability or physical phone performance**. These stay untested. No fee spent, no external subscription or account setup.

## Durable research scope and decision

Only Run286-specific Python acquisition/inspection source, isolated GitHub Actions workflow and this audit were added on `research/owl172-run286-free-highdetail-donor-native-qa-NO_RELEASE`. Generated GLB, source license/manifest, native six-view PNGs, machine report and checksums live solely in the rejected research Actions artifact. They have **not** been staged as a consumer character; there is no merge to `main`, change to the 251 species production, kitten prototype, original #172 image, or deployment.

**Technical outcome:** high-detail, legitimately downloadable native mesh and real multiview display path work without additional paid tools. **Product outcome:** failed artist gate. This particular adult donor would need a wholly new juvenile species-correct sculpt/groom and real phone optimization; unmodified or mildly recolored use is categorically disallowed. Continue searching for professional juvenile `Tyto` form, layered cream-white down, independently clean rights and actual mobile QA. **NO_RELEASE.**
