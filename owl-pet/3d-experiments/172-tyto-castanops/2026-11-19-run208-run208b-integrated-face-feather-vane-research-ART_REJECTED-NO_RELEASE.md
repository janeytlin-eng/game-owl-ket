# Run208 / Run208b — actual native 3D feather-vane and integrated-heart experiments — ART_REJECTED / NO_RELEASE

**2026-11-19, #172 `Tyto castanops` v3, rightmost age-unknown cream-down young.** Research only. Extra spend **$0**.

## Mandatory preflight and isolation

Re-read the real `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/research/species/172-tyto-castanops-v3.md`, the existing unsatisfactory cat-only `owl-pet/prototype/index.html`, Run206b failure record and Run207–207b independent seven-view art rejection. The source crop was **not available** in this local run: no pixel-matched reference reconstruction or source-hash recheck is asserted. The canonical Run205b source crop SHA256 is `5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9` (historical record, not revalidated this run). Actual local base GLB was rehashed and matched immutable Run207b fingerprint `c6cead1a89aa9f620b630a2635d046398db86392178145182018f96344bc1812`.

Tested on Python scientific libraries (NumPy/SciPy/Trimesh), native GLB roundtrip and VTK 9.6.2 offscreen rendering under Xvfb. No neural remote job, borrowed third-party art, paid credits, asset licensing claim, source design change or update to production workflows.

## Run208: genuinely different geometry/groom approach

Constructed an actual new GLB by **removing the rigid 8,320-triangle separate face applique**, painting a continuously blended heart region directly onto the already-continuous watertight main head/body mesh by vertex colors and a signed distance to an analytic heart curve, and placing genuine 3D overlapping down vanes (not the previous needle/spine-like groom) onto its front/sides/back in gravity-oriented layers. Replaced the floating tubular bark ring with an actual dark inner / brown outer vertically extending irregular hollow wall, with a top edge. Reused the original native 3D small eyes/bill/feet but flattened eye protrusions. The output is a full native scene with independently measured side, back and underside geometry. Nothing is SVG, a photograph on a plane, or a claimed artist-quality final.

Run208b is an **actual exported and rerendered iteration**: more apparent warm tonal heart-disc rim is painted onto the same organic body without reintroducing a hard overlay; bark lip roughness lowered. It is not a mere plan, recolor without export, or a renamed Run208 file.

| Verified measurement | Run207b (read/rehash baseline) | Run208 | Run208b |
|---|---:|---:|---:|
| Native GLB file bytes | 2,873,788 | 2,114,968 | 2,114,972 |
| Triangles after real Trimesh GLB reimport | 100,922 | 84,102 | 84,102 |
| GLB scene geometry count | 21 | 21 | 21 |
| Groom | 16,338 pointed fiber triangles groups | 9,668 layered 3D curved vane strips + 754 peripheral down ruff triangles | same topology, revised integrated disc/bark |
| VTK seven-view native renders | 7 earlier views, reopened | 7 new camera images | 7 new camera images |
| Reduction vs Run207b | — | 16.67% triangles; 26.40% GLB bytes | 16.67% triangles; 26.40% GLB bytes |

Precise SHA256 of GLBs:
- **Run208** `4c46309e3a920fe1eef957c9575fdd71664eb1de867d67aa72eb59ba46a9df06`
- **Run208b** `c03305892851ceb3a99cfbe60adc4f8ae973116a137f11e8616a4f25b7bcd974`

Images actually created: `run208_view_{front,left,right,back,quarter,top,bottom}.png`, `run208b_view_{front,left,right,back,quarter,top,bottom}.png`, both seven-view contact sheets. I opened the Run207b, Run208, Run208b sheets independently rather than approving from mesh metadata.

## Independent aesthetic verdict

**Run208 failed** the main image-quality gate: although the face is no longer a protruding decorative plate, the heart contour almost vanishes under washed-out diffuse tones, the eyes are still simple glossy black beads, and front, sides and back read as an anatomically oversimplified egg/chick with triangular flecks rather than a high-end cream-down owl. The thick eucalypt trunk is structurally more coherent than a torus but looks like a crude vertical chocolate-brown sleeve.

**Run208b also failed**. A warm facial-rim color change makes the face area slightly more legible, and bark shape is smoother, but it still does not yield the integrated, naturally feathered heart-shaped face, true down softness, believable wing anatomy, sculpt-quality eye sockets or original target's juvenile appearance. Rear coverage is real but superficial: continuous feather-card distribution is **not** artist-grade feather tracts. No valid age/fledging inference, animal-specific anatomy proof, or evidence of agreement with inaccessible reference pixels.

**Decision: ART_REJECTED / NO_RELEASE / NO_NOTIFICATION.** Do not publish these GLBs as owl-pet or make a public viewer claim. These exact file SHA256 values must not be relabeled as accepted in later runs.

## Actual browser feasibility attempt and reproducible blocker

Built a standalone browser test that really parses the binary GLB 2.0 JSON + bufferViews and attempts to create native WebGL2 buffers and draw all mesh primitives, using local Chromium 2026 environment, Playwright and forced SwiftShader. First navigation to the ephemeral loopback server failed `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Retried **without a server** by embedding the real GLB bytes in the page, and Chromium returned `No WebGL2` even with SwiftShader flags. This is an **environment limitation**, not evidence that the GLB cannot load on WebGL2, and not a positive mobile compatibility test. No real smartphone GPU, hardware frame rate, touch/control QA, or actual verified browser GLB rendering result is claimed. The browser attempt's source HTML/Python and status JSON are retained.

A different future optimization route was identified from the MIT-licensed meshoptimizer/gltfpack upstream (https://github.com/zeux/meshoptimizer), but **gltfpack was not installed or executed** and no optimization effect is claimed. Aesthetic failure must be solved before optimizing/publishing a low-quality model.

## Evidence and storage truth

Actual local evidence bundle `owl172_run208_208b_research_evidence_NO_RELEASE.zip`: **8,481,415 bytes**, SHA256 **`1c17f1402808aa2072c239da292b77485127c02b297925275b1331981552ab3d`**. Contains both original Python generation scripts, browser probe script and page, two full native GLBs, 14 new VTK camera PNGs, 2 new contact sheets, Run207b comparator contact, metrics, negative browser probe JSON and `run208_reproducibility_manifest.json`. Audited **26/26 payload SHA256 and byte lengths** against the manifest after opening the ZIP (27 entries including manifest). GLBs verified independently by Trimesh. Source images are rendered evidence, not user-approved art.

**Persistence limitation:** this documentation is committed in the isolated GitHub research branch. The 8.48 MB binary ZIP is a conversation-local output, **not a GitHub artifact**, not uploaded to GitHub or remote branch. A separate persistent Library folder/upload attempt returned `AccessDeny` for both operations; do not imply successful archival or permanent retention of the ZIP.

**Isolation:** only this one `owl-pet/3d-experiments/172-tyto-castanops/` technical audit was added to a new research branch descended from Run207b; `main`, the 251-species source pipeline, `owl-pet/prototype`, root word game, GitHub Pages and deployment are unchanged.

**Next material quality constraint:** requires a genuinely artist-quality young owl base sculpt/reference-compatible multiview anatomy and groomed layered feather material; repeated basic parametric meshes and naive fur patches have been conclusively insufficient. Do not silently turn a WebGL syntactic test or triangular reduction into an art approval.
