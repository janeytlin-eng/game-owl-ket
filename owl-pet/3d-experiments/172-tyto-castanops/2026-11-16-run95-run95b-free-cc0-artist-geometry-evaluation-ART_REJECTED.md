# Run95 / Run95B — free CC0 catalog real owl GLB source scouting, Blender neutral-light validation — ART_REJECTED

Date: 2026-11-16 (Asia/Shanghai). **Art verdict: ART_REJECTED. Not a user sample, not for deployment.** This report is research-only on branch `research/owl172-run95-free-juvenile-source-mesh-evaluation`, not production.

## Preflight and actual reference

Re-read `owl-pet/AGENTS.md`, `README.md`, `research/species/172-tyto-castanops-v3.md`, Run92/92C, Run93 and Run94 technical records, and the current prototype listing. Actually opened the original `owl-pet/design/concepts/172-tyto-castanops-v3.png` and all twelve Run94 native Blender four-azimuth comparison frames. The target is specifically the rightmost cream age-unknown second-down owl, with a naturally feathered broad dark-rimmed heart face, recessed dark eyes, dense fluffy cream down, essentially buried wings, concealed tail, plump head/body, and substantial supported feet on the hollow lip. The image only supplies frontal morphology, not proved side or rear dimensions. Prior Run94 was a white egg/pear, pasted heart mask and floating or grey-speckled GroomLab card system; adding more hair cards to that inherited sculpture was not justified.

## No-cost actual new external assets and modeling route

Attempted to discover more anatomically authored genuine three-dimensional source assets rather than looping on the unsuccessful procedural seed body. Tried a no-fee candidate model search with a strict **US$0 budget** through the connected 3D generation catalog; the non-interactive runtime instead returned an explicit user-input-required block, so **no paid generation call was submitted and no money was spent**. Then actually used the public no-login `https://3dassets.dev/api/v1/assets` endpoint with `barn owl`, `masked owl`, `owlet`, `baby owl`, and `owl` searches. Found two candidate owl mesh records and downloaded the real original GLBs; checked the binary `glTF` signature, lengths, hashes and declared CC0 license. **Their listing's CC0 assertion has NOT been independently corroborated with the original creators' license**. Neither claims to be `Tyto castanops` juvenile.

- Catalogued "Barn owl (Birds and Reptiles HD)" adult-like candidate source: `CC0_original_birds-and-reptiles-hd-barn-owl-b51d286f.glb`, 369,708 bytes, SHA256 `044dbcfeaf008deff45ff7f227fb0c0dc7e984177a20745345656e1b4b141bc2`.
- "Snowy owl (Birds and Reptiles HD)" wrong-taxon negative control: `CC0_original_birds-and-reptiles-hd-snowy-owl-257f670d.glb`, 360,464 bytes, SHA256 `b5aefa7f13f271e5f441baade9fe4fcdf53a203e58565ecf9c893030361d3c70`.
- No genuine juvenile *Tyto* mesh emerged from this catalog search. CC0 is a licensing claim, not taxonomic, anatomical or artistic verification.

Ran free Ubuntu GitHub Actions + Blender 4.0.2 Cycles in a *separate isolated research workflow*. Both original GLBs imported as actual editable meshes; produced four original genuine Cycles views per source. Created an actual mesh-preserving cream rough nonmetallic PBR retarget on each, exported two fresh genuine GLBs, re-imported them and rendered four more Cycles views per model. Thus **16 original native 3D four-view PNGs and four explicit contact sheets**, not SVG or 2D pet stand-ins. Each GLB had 16,972 real triangles on re-import.

| Trial | Actual real GLB bytes | GLB SHA256 | Re-import triangles | Status |
| --- | ---: | --- | ---: | --- |
| Barn owl → cream-only PBR | 527,088 | `16e132929c5504b7f30a0e90e06412bffab59e1b3ec2c696b1b0999d5d931eb7` | 16,972 | Rejected |
| Snowy owl → cream-only PBR | 520,332 | `4b730698f53442e678ace86d37ecca3f1d51e29ddae5f4e45ad0e2f0c6b10374` | 16,972 | Rejected |

Source credits/provenance remain inconclusive; these are explicitly negative research candidates and cannot be reused in a public commercial product without creator-level license verification.

## Real failures, corrections, and visual evaluation

- First Run95 Actions execution [43760555912](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43760555912) successfully downloaded both actual source GLBs and permanently archived the failure, but glTF Blender import failed due to **missing NumPy**; fixed by installing `python3-numpy` explicitly.
- Second actual full [Run95 Actions 43760736486](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43760736486) completed all original and cream-only multi-view renders, two real GLB round trips, 16 images and archive. Opened the original **pixel contact sheets**, found gross clipping: the initial light levels blew most materials white, so those images were not trusted for color/material acceptance.
- Changed studio area-light energies from 210/100/170 to 12/6/10, world strength from 0.70 to 0.45, exposure from -0.4 to -1.5. Third actual [Run95B neutral-light Actions 43760975549](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/43760975549) succeeded, re-rendered all real views and permanently re-archived SHA evidence. Explicitly opened actual source and cream four-view contact sheets again, including snowy negative control, **not just read JSON metrics**.
- Under corrected neutral lighting, the models are small stylized **mature, long-tailed/long-winged bird shapes**, some with protruding pointed structures around head; particularly striking side view shows massive mature wing/tail plane, extended standing legs, no plump chick silhouette. They have no broad naturally feathered heart disc, dense cream second-down plumage, compact buried wings or supported hollow-lip pose. Simply painting entire geometry cream masks detail and makes a beige toy, does not transform the shape into the reference juvenile. The “barn owl” source is not the species/age required; snowy owl is biologically the wrong genus. This catalog route did not yield an artistically acceptable anatomical base. **Do not reuse either as finished #172**.
- There was no independent creator-rights check or physical mobile WebGL GPU/real FPS, thermal, animation or touch gesture validation. A GLB load or Cycles render cannot pass those later acceptance checks.

## Evidence / integrity / isolation

Scripts:
`owl-pet/3d-experiments/172-tyto-castanops/tools/run95_free_cc0_owl_asset_scout.py`;
`tools/run95_real_mesh_fourviews.py`;
`.github/workflows/owl-pet-172-run95-free-cc0-anatomy-mesh-qa.yml`.
Files (2 original authentic downloaded source GLBs, 2 new trial GLBs, 16 PNGs, 4 contact sheets, 31 SHA256 manifest entries, metrics, free-tool logs, rejection marker) are permanently retained under:
`owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run95-FREE-CC0-MESH-ART-REJECTED/`.
The original earlier overexposed attempt is also preserved in immutable prior Git commits and an Actions artifact; the final neutral-light evidence is on the current research branch and independently checked via GitHub readback. Both experimental GLB SHA256 values from metrics are present in the archived `SHA256SUMS.txt`; outputs re-import at 16,972 triangles each. Successful final workflow artifact ID `14179954008` (the previous successful workflow also has artifact `14180126656`).

GitHub main-vs-research comparison shows **zero changes outside `.github/workflows/owl-pet-172-*` and `owl-pet/3d-experiments/172-tyto-castanops/**`**. No modifications to 251-species production, original concept plate, earlier pet prototype, science ledger, main branch, or live application; no paid credits or billed API.

**Hard release gate: ART_REJECTED. No user-facing 3D sample or success notification.** The valuable result is negative: these off-the-shelf catalog GLBs, even with accurate source import, true round-trip, native multi-view rendering and cream PBR, have substantially wrong mesoptile anatomy and do not remedy the visual blocker. Future art success needs a genuinely high-quality juvenile barn/masked owl 3D sculpt with natural sculpted feather tracts and then realistic phone GPU testing, not another cream recolor of an incorrect adult model.
