# Run352 — source-derived down microstructure / PBR normal-map ablation — NO_RELEASE
2026-11-25 Asia/Shanghai. THREE_NATIVE_GLB_REIMPORTED / 12_VTK_PBR_VIEWS / ART_REJECTED / NO_RELEASE.

Read main owl-pet README, STATUS (206/251), knowledge/DESIGN_WORKFLOW.md, prototype/index.html and #172 v3 review; immutable Run351 record and discrepancy at 02dd32f05801baa3afa7489e809c166ca452b93a. Root AGENTS.md returned 404. Historical artifact 14733006902 actually downloaded and unzip-tested. Viewed masked 512px juvenile source and historical six-view render. Donor SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117. No new neural inference. Blender not installed, CUDA unavailable; VTK, SciPy, Trimesh available. No external generation or extra spending.

## Actual experiment
Instead of further smoothing/remeshing or adding feather geometry, test whether source-derived microstructure can give real three-dimensional surface lighting at unchanged triangle count. Largest connected component, reorder axes [1,2,0], center, fix normals. Cylindrical UV atan2(x,z)/(2*pi)+.5 and normalized height; duplicate seam-crossing vertices. Four-neighbor inverse-square UV color interpolation with periodic samples to 1024x1024. Preserve front upper face and feet with sigmoid masks; elsewhere blend toward cream RGB [218,198,170]. Take actual masked source central belly patch rows 262:342 cols 185:265, average RGB, subtract Gaussian sigma3 illumination, normalize, mirror-tile and blur sigma .45. Mask microcontrast out of face and feet. Compare base (flat tangent normal, no microcontrast), fine (normal gradient .26, color amplitude5), strong (.65,10). Normal maps encode [-dx*amp,dy*amp,1] normalized. Export native GLB PBR baseColorTexture and normalTexture, metallic0, roughness .92, explicit NORMAL and TEXCOORD_0. All reimport successfully with normalTexture. Exported GLBs do not include explicit TANGENT; VTK independently generated tangents for rendering, so cross-viewer agreement not established. UV overlap on feet/complex surface is possible; seam duplicate topology not a watertightness claim.

|Model|Triangles|Vertices|Bytes|SHA256|
|---|---:|---:|---:|---|
|base|100534|50398|3491156|4d4d45ca4c9d6a62a7dfd795184c01385dcfe33d5f11e258ed2d7230f7663f96|
|fine|100534|50398|5222384|8c9f76de8b26be3fd483b5c091178de1f97051878c18abe002de8285c815b5c0|
|strong|100534|50398|5900968|afc54ce448f11bcc45dfb00e8d1ffd6089dcaeec3b9a2ee12868cd9bc77c8499|

Rendered actual VTK PBR 0/45/90/180 degrees, 300x350, same camera scale .59, three lights and textures, 12 views. Full contact sheet opened and inspected. Mean absolute RGB difference on non-background pixels vs base, by angle: fine 2.47/2.31/3.16/3.47, strong 5.32/5.18/6.69/7.46 (0–255). This is a combined normal/albedo ablation, not isolated normal-map effect. Fine looks like coarse cracked clay with added grain; strong looks noisy/sandy rather than fluffy. Black flecks, deep eye sockets, flat face profile and feet defects persist. No silhouette improvement by design. All rejected. The maps add 1.73–2.41 MB over baseline without improving anatomy. No new browser/physical phone test. Do not promote. Stop treating donor surface detail as the primary bottleneck; new juvenile base mesh remains necessary.

## Evidence
Actual executed experiment.py SHA256 05c7b6dc3439b0521489bdaa2e35dc5f7c0b730726642d32a849babd39d374e0
Actual full contact.jpg SHA256 d56ffe5a21b8fbb5e575c9a54708ad703332a8d166983f779d09ed8a70f4a430
metrics.json SHA256 e7696b463eb379c37ae2899c6f64b81f534f5e30c8e92339e8bab168d614e0c4
Full GLBs, script, textures and full-size renders local only, not claimed remote. Separate thumbnail base64 evidence can be decoded with base64 -d; local JPEG 96x90, 1348 bytes, SHA256 cf082dd26032893a482b4940252d8901717bee068ecb60b62bf323d9d37ae1ca, Git blob SHA 2a0d6a4b57944f614bc322efedc48798f67ccaab. Thumbnail is for orientation only, not sufficient for art approval.

Independent branch created from main; no changes to main, species production, concept images or deployment. Zero extra spend.
