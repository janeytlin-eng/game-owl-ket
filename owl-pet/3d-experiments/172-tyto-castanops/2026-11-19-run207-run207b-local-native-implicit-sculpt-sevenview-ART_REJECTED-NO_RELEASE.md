# Run207–207b — independent free native 3D implicit-sculpt + actual geometry-down experiment: ART_REJECTED / NO_RELEASE

**2026-11-19 · #172 `Tyto castanops` v3 · rightmost cream mesoptile / age unknown**

## Preflight and isolation

Re-read the actual `owl-pet/AGENTS.md`, `README.md`, current independent Run206b record, original species boundary `owl-pet/research/species/172-tyto-castanops-v3.md`, and Run205b TripoSR seven-view reject record before producing a new trial. Existing `prototype/index.html` remains the earlier unsatisfactory cat, not a finished owl. The reference *design specification* is cream second-down, continuous integrated heart disc, dark eyes, crouched juvenile proportions, down-buried short wings, hidden tail and body/feet supported by broad senescent eucalypt hollow lip. The source crop SHA256 reported by Run205b is `5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9`; **the source image bytes were not available to this local test, so no pixel-level photo agreement is claimed**. This is a *new scratch-built* native geometry representation, distinct from neural reconstruction and anonymous web generation.

## Actual trial, not a plan

Executed locally in Python 3.11-compatible scientific libraries using **NumPy, SciPy, scikit-image marching cubes, Trimesh, native GLB and real VTK 9.6 software rendering under Xvfb**. A single watertight organic SDF body/head/cheek/wing-bud form was created by smooth field union and meshed; a curved heart-shaped face, physically curved eyelid/eye/bill forms, supported feet, original irregular tree-hollow lip and tens of thousands of true spatial featherlet faces were constructed. This is true 3D geometry, not SVG or screenshot geometry; the 3D down has measurable posterior surface coverage. Neither run reused a prohibited third-party GLB. Re-imported both exported binary GLBs through Trimesh as scenes and verified `glTF` GLB magic, geometry and triangle totals. Renderer generated **seven real independent VTK camera views** for each version (front, left, right, back, quarter, top, bottom). I opened both contact sheets and compared side/back images directly. No paid service, key, credit, billing or source-license issue.

The first VTK render tried forcing OSMesa, but the local system lacked `libOSMesa` and aborted after GLB export. Re-ran successfully via available **Xvfb/Mesa software OpenGL**, preserving the failed attempt as a real setup limitation. Version b was a real iteration: face depth conforming to a head ellipsoid rather than flat extrusion, smaller/recessed eyes, narrower/shorter down, denser groom and coarser base mesh.

| Real output | Run207 | Run207b |
|---|---:|---:|
| Native GLB byte length | 2,941,880 | 2,873,788 |
| GLB SHA256 | `8dbb64adcf79d390412af2af6ea936f354dd36eb572c2951417f6e1c46ccf92c` | `c6cead1a89aa9f620b630a2635d046398db86392178145182018f96344bc1812` |
| GLB scene geometries after roundtrip | 21 | 21 |
| Triangles | 116,984 | 100,922 |
| Actual tapered native down featherlets | 12,500 | 16,338 |
| Organic body watertight / Euler number | true / 2 | true / 2 |
| Native seven-view VTK stills | 7 | 7 |
| Provenance | original code, research only | modified original code, research only |

Original isolated run files: `run207_native_sdf_down_trial.py`, `run207b_native_sdf_down_trial.py`, `run207_metrics.json`, `run207b_metrics.json`, `run207_reproducibility_audit.json`, 14 actual VTK PNG camera renders, 2 contact sheets, and 2 GLBs. They were packaged in the **run's working-container evidence ZIP**, `owl172_run207_207b_research_evidence_NO_RELEASE.zip`: **9,042,649 bytes; SHA256 `6e6ccfd5ca0c666c2fac114ad85263494fbe756ecae1b817be3fd43c043c73d8`**. This is **not a GitHub-hosted or permanently retained archive**: the binary evidence was not uploaded to this branch; the exact code and images are present only in the run's working-container output. The present audit permanently records discriminating metrics, IDs and failure criteria; do not misrepresent the ZIP as a GitHub Actions artifact.

## Independent visual rejection

**Run207:** front resembles an owl-shaped stylized plush, but the heart is a stiff flat protruding plate and cartoon eyes bulge beyond the head in side profile; surface hairs look like coarse straw/porcupine spines rather than naturally layered neonatal down. Tree lip resembles a detached toroid. Back is at least filled (not the dark neural shell seen in Run205) but lacks anatomical feather tracts and mass complexity.

**Run207b:** nonplanar/closer-fitting mask and smaller eye reduced some protrusion, more delicate high-density fur covers side/back consistently. **Still fails:** the sculpt retains an obvious hard decorative heart applique, expression/eye sockets read as toy rather than premium fluffy juvenile, side outline is a simplified egg-shaped body without convincing buried wings or feather anatomy, lower feet/support are poor. 100,922 triangles is already expensive for a low-detail mobile pet, and mobile WebGL / real phone GPU test **not performed**. Neither has artist-grade groom, PBR feather variation, production rig, approved reference correspondence or natural credible side/back detail. A geometrically watertight body alone does not imply aesthetic quality.

**Decision: ART_REJECTED / NO_RELEASE / NO_NOTIFICATION.** Do not publish, rename, recolor or deploy these GLBs as an acceptable v3 owl. The tested implicit sculpt + simple procedural featherlets does *not* clear the premium aesthetic gate; prioritize genuinely artist-quality base anatomy and physically groomed broad feather structure rather than additional self-confirming geometry-only tweaks.

## Isolation and expense

This is a separate research-branch **documentation-only GitHub mutation**. No modification to `main`, production 251-species code, existing `owl-pet/prototype`, design manifest, GitHub Pages/Sites or deployment. Extra spend **$0**. No real GPU or smartphone validation is claimed.
