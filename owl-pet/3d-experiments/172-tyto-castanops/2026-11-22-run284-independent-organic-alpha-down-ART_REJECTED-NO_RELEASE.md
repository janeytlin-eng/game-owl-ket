# #172 *Tyto castanops* v3 rightmost owlet — Run284 independent organic SDF and true alpha-down cards

**2026-11-22 (Asia/Shanghai). Research only. ART_REJECTED / PHONE_UNTESTED / NO_RELEASE.**

## Read-first provenance and non-interference

Re-read owl-pet/AGENTS.md, README.md, STATUS.md, the existing WebGL kitten prototype description and [Run283's exact rejection audit](https://github.com/janeytlin-eng/game-owl-ket/blob/research/owl172-run283-surface-tracts-native-pbr-NO_RELEASE/owl-pet/3d-experiments/172-tyto-castanops/2026-11-22-run283-spatial-cream-PBR-curved-feather-tracts-ART_REJECTED-NO_RELEASE.md). Independently downloaded original Run283 GitHub Actions artifact #14736523128; byte size **5,445,510**, ZIP SHA256 **61c0f6465701936805167828f9924818ac74c9aca59dca55d828417817169d7e** matches the previous recorded digest. Opened the original 512×512 rightmost juvenile crop; its SHA256 is **8eee63bf0b8650c390d4c4bba6a07a0c2dd05dd7fc2e90e00a896ec3ab51c641**. Inspected previous neural sculpt six-axis views. **Do not mistake a real model for acceptable art.**

For external juvenile anatomy context, Australian Museum states young Masked Owls are white to cream when first fledged: https://australian.museum/learn/animals/birds/masked-owl/ (updated July 23, 2024). No third-party owl photos/models were copied into this experiment.

## Actual independent local model experiment

Abandoned the now repeatedly rejected single-view neural shell as the primary sculpt. Installed-code route uses existing free Python NumPy, SciPy, scikit-image, Trimesh, PIL, and VTK; no GPU, paid generation service or purchased credits. Created a **new watertight continuous SDF surface** with organ-shaped chest, rounder head and anatomically placed short folded wings, surfaced using marching cubes; this is a complete physical volumetric mesh, not an SVG or 2D camera turn.

Added genuine curved 3D beak and toes, inset/gloss eyes, sculpted heart-border relief, original reference-derived *front-only* colors blended with neutral rear colors, plus **3,600** surface-root locations for two crossing groups of spatially curved tapered fin cards, genuine vertex positions/UV/alpha cutoff texture and glTF PBR material. Explicitly exported GLB **with POSITION and NORMAL** via Trimesh `include_normals=True`. There are two distinct native GLBs: the no-down anatomical control and the alpha-down variant. Both were really reimported and rendered in VTK from +Z, 45°, +X, -Z, -X and +Y (six spatial cameras each, not a sprite rotation).

Local validated metrics:

| Variant | GLB bytes | Triangles | Meshes | Notes |
| --- | ---: | ---: | ---: | --- |
| new organic SDF no-fur control | 3,714,928 | 145,120 | 26 | full watertight organic body and true separate anatomical details |
| new organic SDF + alpha fin down | 6,082,604 | 188,272 | 27 | includes real UV alpha-cutout fin primitive, with MASK mode |

Both 640-pixel VTK six-axis contact sheets were actually opened and manually compared to the 512-pixel rightmost original juvenile. Exact GLB SHA256 and glTF mesh/material evidence are in the ZIP machine-validation file; both model files actually exist and were independently reloaded. The new base is not the previously used TripoSR mesh. This is an actual implementation and physical 3D output, **not** a written-only plan.

Local evidence ZIP `owl172_run284_rejected_research_evidence.zip`: **7,800,667 bytes**, SHA256 **58b8fb56ffb9caeea4a088fc28877cdc466dc1dbb1da5a3361bbcb3d17a029e3**, **26/26 ZIP members CRC-pass**. Includes both GLBs, source scripts, original target crop, 12 VTK views, QA JSON, manifest and Chromium diagnostics. This ZIP exists in the local working sandbox only. **Persistent Library upload was actually attempted but both folder creation and upload returned AccessDeny**, so do not describe it as permanently stored or directly downloadable from the repo.

## Manual visual verdict: ART_REJECTED

The broad compact body and native front/side/back silhouette are cleaner than the malformed adult-like single-view neural shell. However the actual render is still a stylized toy lacking fine professional sculpture: the face is poorly integrated, the eye cavities and curved beak do not meet correctly from the side, and there is no convincing heart-disc anatomy. The UV/alpha cards render as **distinct gray flakes or mottled marks**, not fluffy cream-white down. The folded wing remains a swelling of the body instead of a naturally layered short wing. Feet float without a real old-eucalyptus hollow/grasp. At **188,272 triangles**, the furry variant is also not yet mobile-budget qualified. Both controls therefore failed the supplied character art standard. DO NOT SHOW AS AN APPROVED OWLET, PUBLISH, DEPLOY OR RELEASE.

Local Chromium actually attempted WebGL2 context creation in a 390×780 mobile viewport using normal headless mode and two SwiftShader configurations; all yielded null WebGL2 contexts. No credible mobile browser render, actual Android/iPhone GPU FPS/memory, gestures or thermal measurement can be claimed. No separate phone certification. The project reference art's downstream commercial usage rights also need verification.

## Independent GitHub reproduction / separation

This branch **research/owl172-run284-independent-organic-alpha-down-ART_REJECTED-NO_RELEASE** extends only the isolated Run283 research branch. It contains a separate native 3D source file and an independent fail-closed GitHub Actions workflow, which downloads the exact original 512-pixel reference from the pinned Run283 artifact, generates two real GLBs again in Linux, reimports them, renders six VTK camera views each, and saves their actual files/sha256 manifests to a separately named 14-day **RESEARCH NO RELEASE** artifact. The runner may produce different exact byte SHA256 values from local due to version/runtime differences; compare *its own* machine manifest, and never claim byte identity without checking.

Execution: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44982710242 . Technical completion and remote art review must be verified before claiming any remote pass. No modifications to main, 251-species concept generation, original image, existing kitten prototype, or deployment. Additional external payment **zero**.

## Decision

**ART_REJECTED / PHYSICAL_PHONE_UNTESTED / RIGHTS_UNCLEARED / NO_RELEASE.** The independent organic SDF and mobile-compatible alpha-masked geometry path provides a new native-GLB technique and a useful failure observation, but still does not yield soft down or acceptable face/beak/feet. Character art needs a professional juvenile-specific sculpt and multiview sculpt supervision, not more unilateral procedural furry decoration. Only re-open the public sample gate after real visual acceptance and physical mobile QA.


## Independent remote execution completed and artistically rejected (not a usable model)

First [GitHub Actions run #44982710242](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44982710242) **failed closed**: the remote source constructed a NumPy array combining scalar camera-position indices and a 181-long depth vector, triggering a coordinate-shape ValueError in front-surface lookup. Its 5,702-byte diagnostic ZIP artifact #14738670884 was downloaded; no model was claimed from that failure. Corrected source using `np.vstack` of equally-sized coordinate vectors and committed the actual fix `516b499276a735e58e50cbd906baaf5f9cdfb1df`.

Second [independent Actions run #44982798516](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44982798516) **fully succeeded**, including pinned input reference retrieval, actual two-model construction, original-model reread, 12 VTK true-space directions, fail-closed check and independent upload. This indicates engineering reproducibility, **not** acceptable art. Its original [Run284 research artifact #14737544875](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44982798516/artifacts/14737544875) is **6,140,724 bytes**, SHA256 `bf158b9a6cff06facdec0079e527e07c7200a72e7f13a3d729aadeadff288edb` as independently downloaded and matched to the GitHub digest. **27/27 ZIP CRC entries pass; 25/25 SHA256SUMS entries pass.** GitHub lists expiration **2026-12-06 03:56:53 UTC**, so it is *temporary research storage*, not a permanent released pet. Both original remote GLBs were again parsed and loaded by Trimesh; all have native `POSITION`, `NORMAL`, `COLOR_0`, and the feathered variant additionally has `TEXCOORD_0`, real embedded alpha texture and `alphaMode=MASK` with double-sided glTF PBR.

| Remotely regenerated (not byte-identical to local variants) | Bytes | Genuine triangles | Meshes | SHA256 |
| --- | ---: | ---: | ---: | --- |
| New organic base | 3,769,652 | 152,520 | 26 | `6bb3dce65140483cf88d5499b3dcb7334d06338976216c03a498b60bdee593af` |
| Base + 3,600 UV down roots/two crossed fans | 6,139,932 | 195,720 | 27 | `5b737ffc3539e752395c0ccc949f00d5da7e4495286791bac66e9377904fb00d` |

**I explicitly reopened the successful remote +Z/+X/-Z/-X/+Y/-Y six-camera composite for both versions. Both are ART_REJECTED.** The front is a smooth, stylized rounded owl with tiny dark bead-like eyes and shallow mask, far from the rightmost soft cream owlet target. More critically, at both +X and -X the separate curved beak is **visibly suspended in mid-air ahead of the head**, and the exposed toe/claw shapes appear to dangle without a perch. The back is a regular corrugated shell/chevron sculpture, not fine feather anatomy. The alpha fur produces **dark gray short hatch/flake markings over the entire body**, creating worse dirty/mottled down appearance, not soft dimensional creamy down. The 195,720-triangle variant has no justified physical-phone GPU performance margin. **Stop and reject this technique as a plausible publishable character in its present form.** A green CI run absolutely does not mean art or mobile release readiness.

The separate research branch still never changes main or the original 251-species workflow. Additional external payment: zero; artwork usage rights remain uncleared. Final status **ART_REJECTED / SOFTWARE PHONE WEBGL2 UNVERIFIED / PHYSICAL PHONE UNTESTED / RIGHTS_UNCLEARED / NO_RELEASE**.
