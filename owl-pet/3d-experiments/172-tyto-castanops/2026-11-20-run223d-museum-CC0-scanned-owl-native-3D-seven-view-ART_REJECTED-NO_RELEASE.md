# Run223–223d — authentic CC0 museum-scanned Barn Owl native GLB and actual seven-view QA: TECH PASS / ART REJECTED / NO RELEASE

**2026-11-19 18:24–18:40 UTC / 2026-11-20 02:24–02:40 Asia/Shanghai.** Subject is the right-hand cream **age-unknown mesoptile** in `#172 Tyto castanops v3`. No new accepted pet, no release, extra paid spend **$0**.

## Preflight and unchanged production boundary

Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/STATUS.md`, `owl-pet/research/species/172-tyto-castanops-v3.md`, existing cat-only WebGL prototype description, and preceding Run221 native `feathers_down` trial and Run222 failed adult 3D donor. Verified full v3 original concept `owl-pet/design/concepts/172-tyto-castanops-v3.png` at **737545 bytes**, SHA256 `881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d`. Actual target: **cream down, seamlessly developed heart face, dark open eyes, squat juvenile body, down-buried short wings, hidden tail, full secure eucalypt hollow-lip support**. No exact castanops juvenile age is claimed. This research branch branches from Run222; main production's 176/251 unique species, existing prototype, root game, owl-pet manifest and deployment are untouched.

## New genuine source acquisition (not simulated)

Searched actual public Zenodo `/api/records` and the Smithsonian Open Access metadata repository. Run223 initially received HTTP 400 from Zenodo because its anonymous search limit is **25 records/page** (we requested 30) and initially hit a 60 MB metadata cap on Smithsonian. Run223b corrected Zenodo to 20 records/page and observed real HTTP 200 results; however the API identifies valid CC0 license as **`cc-zero`**, not the string `cc0`, so the exact record was initially excluded. Run223c verified 1500 Smithsonian metadata rows (out of 3451 listed) using 189630086 transfer bytes before an intentionally capped scan; **zero owl matches in the checked subset**, not a claim about the entire collection. Run223d corrected this license mapping and focused on exact museum record rather than re-downloading huge unrelated metadata.

Found [Zenodo archival Barn owl scan, record 21379215](https://zenodo.org/records/21379215), with original Sketchfab UID `0e65de5934db4f0eae02835ba7227dcc`, from Virtual Museums of Małopolska. **Archive-reported `cc-zero` (CC0) license**; this remains a source metadata assertion rather than an independent legal certification. This is an authentic **adult Barn Owl / Tyto alba taxidermy exhibit** photographed/scanned with its original tree-branch/stump mount, **NOT a young Tasmanian masked owl**.

Actually downloaded the original full-resolution native glTF binary from:
`https://zenodo.org/api/records/21379215/files/0e65de5934db4f0eae02835ba7227dcc.glb/content`

- Actual HTTP **200**, original GLB **43,225,496 bytes**, SHA256 `6412ffd575360397bd90d391d3d4c23397f225945cdef3ec5727bfd91504cd44`. Verified first four bytes as `glTF` and independent re-import with Trimesh.
- Native **12 triangle geometries / 261,966 triangles / 756,317 listed vertices**. Global bound roughly `0.4325 × 0.5640 × 0.4601` in scene units, though exact real-world sizing must be verified.
- Independently submitted all original triangle geometry to **VTK true 3D** renderer (not generated side images, not a 2D impostor) with **seven distinct azimuthal camera directions 0°, 50°, 100°, 150°, 200°, 250°, 300°**, each saved as genuine PNG; also created one contact sheet. The material viewer counted zero dedicated image-textured actors; preview appearance uses vertex-colour fallbacks and **cannot be asserted to reproduce original PBR texture/normal maps**.
- [Actual seven-view contact sheet: **research negative, NOT approved**](run223-evidence/run223_museum_7views_NOT_APPROVED.png); [exact measured Run223d execution JSON](run223-evidence/run223_report.json); [reproducible download/scene/render program](run223_museum_cc0_barn_owl_scan_probe.py); [independent workflow](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run223-museum-tyto-scan-free-model-forensics-no-release/.github/workflows/owl172-run223-museum-tyto-scan-research.yml).

## Actually opened seven views — strict visual gate

Unlike Run222's mechanical/CAD-looking donor, the true scanned specimen has **credible natural adult Tyto head/face and real feather surface** seen across the original multiple-camera views. However **reject as an owl-pet juvenile**: the silhouette is adult and narrow, strongly developed long remiges and tail are plainly visible, adult perch-gripping feet are not a compact crouch, there is **no soft cream second-down**, no short down-buried wing, no hidden tail and **no broad hollow support**. The exhibit's thin diagonal branch and stump mount are part of the scan and not a natural nest hollow lip. Despite a recognisable heart-shaped adult disc, this is not the user's rightmost mesoptile design. It can inform future artist-grade anatomy only. No recolour-only or geometry-scale-only edit is accepted as a juvenile.

**Decision:** REAL_PHOTOGRAMMETRIC_TYTO_ADULT_GLB_261966_TRI_TECH_PASS / SEVEN_NATIVE_VIEWS / AUTHENTIC_ADULT_ANATOMY / JUVENILE_ART_REJECTED / NO_NEW_JUVENILE / NO_PHONE_WEBGL / NO_RELEASE / NO_NOTIFICATION. Smartphone GPU, LOD, fill rate, memory and real WebGL behaviour were **not** tested; the current original 43 MB high-poly scan must not be described as mobile-ready.

## Independent primary binary evidence and readback

[Actual research-only GitHub Actions run 44589767752](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44589767752) finished successfully. Its [30-day evidence artifact #14563087610](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44589767752/artifacts/14563087610) contains original GLB, seven original view PNGs, contact sheet and machine report. I independently **downloaded**, reopened, and checked all **9/9** reported data-payload SHA256 + byte sizes successfully. ZIP length **24,192,586 bytes**, SHA256 `7a2835fffb4a8da63fcd7f8cfd2bf9377bf42466eebcc8dbfcac76d40468fe65`. This artifact is temporary (~30 days, subject to GitHub retention), not a permanent released model. Committed text, measured JSON and contact sheet are persisted on **this separate research branch**, not in `main` or the pet viewer.

### Distinct outcome and next technical constraint

This is a clear **real artistic-source improvement** over the preceding fake-looking owl donor, but **not yet a character**. The remaining hard problem is creation of a true 360-degree **young Tyto mesoptile sculpt**, including remodeled down-covered wings/tail/feet and hollow support, then GroomLab-authored feather-region guides, source-aware materials, GLB LOD and only after beauty acceptance actual phone WebGL testing. Merely whitening the adult scan would be misleading. No external paid quota or paid service was invoked.
