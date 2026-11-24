# Run350 — topology-aware LOD ablation — NO_RELEASE
2026-11-25 (Asia/Shanghai). SIX_NATIVE_GLB_REIMPORTED / 24_VTK_VIEWS / ART_REJECTED / WEBGL_CONTEXT_BLOCKED / NO_RELEASE.

Read main owl-pet/AGENTS.md, README.md, STATUS.md (latest reports 206/251), prototype/index.html and #172 v3 review; read immutable Run349 0e54cf28e9f485905b16d87eff33209e5ad701f6. v3 rightmost young remains the design reference; viewed actual masked crop and historical six-view renders recovered from GitHub Actions artifact 14733006902, containing actual pretrained TripoSR GLB SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117. No new inference or paid call. Separate branch from main bcd452e9e483419241dd69602f924d4729295ba7.

## Actual experiment
Avoid another groom-density or global smoothing repetition. Investigate mobile mesh budget and the topology breakage risk of simplifying neural meshes before a future better sculpt. Extract largest connected component of 110, reorder axes [1,2,0], center by vertex mean; preserve original donor vertex colors, without claiming art improvement. VTK QuadricDecimation with volume preservation, compare geometry-only nearest donor vertex RGB against attribute-aware RGB (scalars weight .2). Then actual iteration with vtkDecimatePro PreserveTopologyOn, SplittingOff, BoundaryVertexDeletionOff. Explicit normals on export through Trimesh; each GLB reimported and face count verified.

| Variant | Faces | Bytes | Watertight | nearest donor-to-LOD vertex distance P95 |
|---|---:|---:|---|---:|
| base |100534|2613436|true|0|
| QEM75 |25132|653700|false|.0110564|
| color75 |25133|653964|false|.0115711|
| color90 |10052|262404|false|.0187533|
| topology75 |60706|1577892|true|.0097406|
| topology90 |60706|1577892|true|.0097406|

Distances in normalized donor units, NOT surface Hausdorff or a silhouette error. Topology variants identical bytes: actual reduction 39.61%, despite requested 75% and 90%; no stronger topology-preserving reduction achieved. QEM variants lose watertightness; color90 visibly introduces dark tears at side and back. Attribute preservation does not visibly fix underlying donor. 24 actual VTK orthographic renders at 300x380, four directions per output, viewed both full contact sheets. The donor still resembles cracked dark clay, lacks cream down on back, eyes recessed, face flat from side. All variants art rejected; do not ship as pet. LOD results useful only as technical constraint for future good sculpt.

## Browser check
Actual Playwright Chromium at 390x500 using --use-gl=angle, --use-angle=swiftshader, --enable-unsafe-swiftshader, --disable-dev-shm-usage, --no-sandbox; repeat with --use-angle=swiftshader-webgl. Both getContext('webgl2') returned null. Installed SwiftShader binaries are present but context unavailable. No browser model render, frame timing or physical phone verification. VTK rendering is not WebGL evidence.

## Local execution evidence
GLB SHA256:
- base 595abdf5dabdccb02014006e397df44b1b4cf14b23400aa7ce0cfc9c6a7c41cc
- qem75 dae266899e7364ca07af81c68304d4aefe028717cd1bf4dc7d3c1970e268aabd
- color75 9809b0ba6be23f4954883153ae21c0ecc7a9c15c8028c11ff28d7681fcac16fb
- color90 8a7c7ce73692e351720d95abfaa699dbf44eba0acab285c88e61924477cf0f64
- topology75/90 22888432986fa7ea33e8d8dbcc3e4634c4f9bb112dc2cda78eea2b29063d80df
Executed experiment.py SHA256 a610f7f6db62db974edf45508d0b0815ad9dd4df1196c1a1d992dddcd3b35c34; topology.py 5271806f5a3f0939bc67cac9b5478531f9644f88c9e7997796bed52f38e2986f. Full contact.jpg d81f6b139ae8c5f89caa2d1fbc48ff763aee41c3d1c0f6d81b5811ee606bfcf0; topology-contact.jpg 9f1c20fed36166d7a70b720b92dbb2de18cbc3dda5bb8bcd77caa370f2d5b7a5. Metrics JSON d6358c10a80bf8f693ed67c1a3fc52a9bddb6cb22c3000fc887d8a3e0a2493ef and eb9536e0dea089ec6c1d78ce0d961b7e5e8e94d4dc655a30d3514b42068b8a80. Full GLBs, executed scripts, full contact sheets local only unless separately archived. Future focus better juvenile sculpt/alternative pretrained donor; topology-preserving simplification before groom, test mobile in supported renderer. Zero extra cost. No main, production, concept, deployment modification.
