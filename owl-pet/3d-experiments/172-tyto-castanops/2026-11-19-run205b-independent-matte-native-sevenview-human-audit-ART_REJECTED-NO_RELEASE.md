# Run205b — verified dual-background matting, two genuine TripoSR GLBs, independent visual rejection

**2026-11-19 · #172 `Tyto castanops` v3 rightmost age-unknown mesoptile · ART_REJECTED / NO_RELEASE.**

## Existing work and immutable source

Checked `owl-pet/AGENTS.md`, `README.md`, `STATUS.md`, `prototype/index.html` (unsatisfactory cat WebGL snapshot), `research/species/172-tyto-castanops-v3.md`, the Run204c independent TripoSR multi-view rejection and the known rejected asset SHA256 registry before acting. The original, distinct #172 rightmost source crop was verified byte-for-byte: SHA256 `5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9`, 512 × 512 PNG. The target is **cream second-down, continuous integrated heart facial disc, open dark eyes, crouched young proportions, short buried wings, concealed tail, supported feet/belly on a broad eucalypt hollow lip**; chronological age is not established.

## What was actually executed

[GitHub Actions Run205](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44456202860) completed successfully with no paid tool or credits. The official open-source `VAST-AI-Research/TripoSR` model was actually installed and run on a GitHub-hosted **CPU** twice with two differently constructed RGBA inputs, not merely proposed. The original crop had mutually inconsistent off-white and black rectangular background regions. A connected-component two-region matte and a foreground-seeded OpenCV GrabCut matte were both created. Human-opened 512×512 preview images show that the black rectangle is removed and eyes remain visible. Connected white background component: **111,829 pixels**; connected black background component: **42,464 pixels**. Foreground alpha >128: **107,851 pixels (41.142%)** for direct two-region matte versus **105,621 (40.291%)** for GrabCut.

After both actual CPU runs exited with code 0, the extracted models were loaded independently from the original isolation ZIP with **Trimesh**, validated by `glTF` GLB magic and exact SHA256, and both were rendered independently from seven VTK camera positions (front/back/left/right/top/bottom/quarter are **world-axis labels**, not necessarily correct bird anatomical axes).

| Route | Actual CPU inference | Real native GLB | Meshes / vertices / triangles | Original SHA256 |
|---|---:|---:|---:|---|
| Connected two-region alpha | 33.39 s, exit 0 | 499,132 bytes | 1 / 12,481 / 24,868 | `4d3c63444787d1c1544fb10ac3a8f1d2a726c1cc16ff06a02a234d698cad7631` |
| Seeded GrabCut alpha | 27.38 s, exit 0 | 759,100 bytes | 1 / 18,997 / 37,844 | `dd9371f2599bb1ed60f87df711fdb423ac520933d31cb0570c34eb811e8a04ef` |

The original ZIP from [Run205 isolated evidence artifact 14498460615](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44456202860/artifacts/14498460615) was **actually downloaded**; all **32/32** `manifest.json` records were independently checked for exact byte count and SHA256 without mismatch. Both original GLBs were independently loaded again and their triangle/vertex counts and hashes reproduced. The archived 14 native VTK views, both seven-view contact sheets, all alpha mattes, native input files, full inference/install logs and status remain in the expiring Actions artifact (expiry 2026-12-03 04:11 UTC). They are **not** published as character deliverables.

## Direct visual inspection: definitive rejection

Both original native seven-view contact sheets were actually opened. Despite much better source-background consistency, **neither neural mesh has coherent animal anatomy**. In both, the recognizable face appears in a side-on world-axis view; nose/face/eyes distort into collapsed holes and raised crude ridges. The opposite side becomes a **very dark/charcoal heavily corrugated, crusted or scaly shell**, radically unlike airy continuous cream-white down. Off-axis front/back views resemble a flattened or stretched lump rather than a sitting owl; prominent isolated/clumped toe-like protrusions replace naturally supported feet. The eucalypt hollow lip and natural full-body support are absent. The GrabCut result is more voluminous but *not* materially more anatomically believable. **Higher triangle count does not confer artistic acceptability.** Neither is a mobile-grade 3D pet model.

The fact that better RGBA matting improves source pixels but **does not fix single-view neural side/back hallucination** is a measured negative result, not a reason to recolor, smooth or publish these meshes. Both exact hashes are being added to the negative asset fingerprint registry. TripoSR model outputs are real GLBs, not SVGs or manually assembled primitives, but **ART_REJECTED**.

## Quality and isolation gate

**No physical smartphone GPU/WebGL acceptance**, no validated animation/rig or usable cream feather groom, no scientifically established specific juvenile age, no visually passable native 3D sample. **NO_RELEASE / NO_NOTIFICATION**. No payment; no main, 251-species production flow, original pet prototype, design manifest, or deployment modifications. Changes are exclusively to the #172 independent research files and one isolated workflow. Further attempts should use an artist-quality multi-view sculpt/groom or materially different generation representation; repeated single-view TripoSR mask polishing is not a convincing production route.
