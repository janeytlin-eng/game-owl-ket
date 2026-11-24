# Run351 — volumetric remeshing ablation — NO_RELEASE
2026-11-25 Asia/Shanghai. THREE_NATIVE_GLB_REIMPORTED / 12_VTK_VIEWS / ART_REJECTED / NO_RELEASE.

Read main AGENTS, README (request returned no visible content), STATUS (206/251), prototype/index.html, #172 v3 review and immutable Run350 record 0fec45fc85f16a7f902901385766091833520883. Main contains #172 v1–v6; v3 remains the specified reference (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b). Read historical artifact 14733006902 ZIP, passed unzip test; inspected actual masked reference and historical six-camera render. Donor SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117, recovered actual pretrained TripoSR output, not new inference.

## Experiment
Test whether rebuilding connectivity through volumetric occupancy convolution eliminates neural mesh's cracked surface without mere vertex smoothing. Largest connected component, reorder axes [1,2,0], center by mean, fix normals. Voxelize at pitch .009 in donor units, fill and pad five cells. Gaussian occupancy sigma .8 and 2.0 voxels. Compare uniform sigma 2.0 versus blend preserving frontal upper face: sigmoid((y-.08)/.045) * sigmoid((z-.13)/.035). Extract iso .5 by skimage marching cubes, retain largest component, fix normals. Inverse-square weighted transfer from eight nearest donor vertices (minimum distance .002). For both remeshes blend rear colors toward [218,201,174] using .82 * sigmoid((.04-z)/.06) * (1-faceWeight), faceWeight sigmoid((y-.08)/.05)*sigmoid((z-.13)/.04). Color correction is an art hypothesis; no inferred back reference. Export normals and reimport all three native GLBs. Render four actual VTK orthographic views each (0,45,90,180), 260x320, ambient/diffuse .5/.5, same camera scale .59.

| Model | Faces | Bytes | Watertight |
|---|---:|---:|---|
| donor | 100534 | 2613540 | true |
| uniform | 79288 | 2062844 | true |
| protected | 80268 | 2088324 | true |

Viewed full 12-view contact sheet. New topology removes most cracks but produces waxy featureless feather mass, rounded feet with lost toe detail, recessed eyes, flat side profile and remaining vertical rear bands. Protected version only marginally preserves the face; neither approaches actual fluffy v3 target. Both rejected. Topology is closed but does not imply acceptable anatomy. No new browser or physical phone test; Run350 WebGL2 context blocked. No paid tool call. Future: avoid more donor smoothing/remeshing, prioritize new juvenile reconstruction and real fine down; no promotion.

## Evidence
- donor GLB SHA256 54feff73b92a77dcce96cb831c07a18ef9fd8c0dee03132dbd55758bb072be39
- uniform GLB 57739a857eb29590644090262454171f6cc2d6eb1b3dd50733a720e2d104742d
- protected GLB 9556781872749cbb0be3e18f962eb50736289e6050f2bcef8272d78917994768
- actually executed experiment.py 4922ef6ecbabea894a3d34d1f0e5abfb647416098e88ff5da15e53f7631207f0
- full contact.jpg 8a04742e0b5156071ab4b680f345fbbcb9621014e6ebbd0cfc2e14b6bd457552
- metrics.json 7a4a8a0b485501b60daf8605e59e5d3b9c2fd112fa09197068b8b010bfd3127e
- actual contact thumbnail in run351-local/evidence.jpg, 104x104, SHA256 c4743630242b5ebcc7351964890b0a76f927d590d881e4d008bb6646578d02b6. Full GLBs, full contact sheet and executed script local only; method recorded above, no claim of remote binary/source archival.
Independent branch from main 823296ea703e70db34157bcb50114737becc7400. No modification to main, species production, original concepts or deployment. Zero extra spend.