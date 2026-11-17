# #172 *Tyto castanops* v3 Run154 — actual native fur GLB roundtrip, rejected art

**2026-11-18 Asia/Shanghai — FINAL: TECHNICAL_EXPORT_PASS / ART_REJECTED / NO_RELEASE.** No sample meeting quality requirements. No notification, no site deployment, and no physical phone WebGL claim.

## Boundary and preflight

Read `owl-pet/AGENTS.md`, `owl-pet/README.md`, the #172 v3 species design file, Run152's real multi-view rejection and Run153's first native sculpt/groom rejection, plus known rejected GLB fingerprints. The rightmost age-unknown mesoptile requires cream second down, integrated broad heart face, **open dark eyes that stay anatomically embedded in 3D**, hidden short wings/tail, coherent side/back, supported feet and a credible old eucalypt hollow; neither original Run153 art nor any adult donor satisfies that gate. Run154 is **not a new owl sculpture** and must not be mistaken for one.

## Exactly what was executed

On its own branch `research/owl172-run154-hair-native-glb-roundtrip`, the [actual GitHub Actions run 44192763186](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44192763186) downloaded the previous [Run153 unapproved research artifact](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44183510767), and independently verified its genuine 7,042,832-byte Blender source against SHA256 `b448a3f39f49827a7f21e286202e31913caf20f25d0460f7dc4d6dc1fdf27073`. Installed free Blender 4.0.2 and actually ran `tools/run154_real_curve_mesh_glb.py`. The script converted four native curve objects totaling **11,400 real existing Blender spline strands** to triangulated mesh, not SVG, flat photographs, or invented GLB output. It exported two geometry density tiers to GLB, cleared the original scene, then **freshly imported each GLB** and rendered actual face +Y / quarter / strict profile +X / rear -Y views in Blender Cycles. Blender's CLI and the workflow guarded nonzero Python exceptions and mandatory outputs.

| Native geometry metric | Full down | One-in-three guide LOD |
|---|---:|---:|
| Retained individual strands | 11,400 | 3,801 |
| Converted fur triangles | 396,000 | 132,036 |
| Entire reimported GLB triangles | 456,420 | 192,456 |
| GLB byte size | 15,582,880 | 5,468,680 |
| Reimported mesh objects | 28 | 28 |
| Actually rendered directions from reimport | 4 | 4 |

Both fresh-import models retained **all their expected fur triangles**, and all eight true independent 360px views were actually produced. The tested full GLB SHA256 is `c0b7a76eee8d232c56b019bebb45507155a08deced8b63ca7e562f75a3895f56`; the LOD GLB SHA256 is `78c1c7f0a995b7104921a69f9915e0845d35abaca80aa29a9f4276126e639b31`. These fingerprint values distinguish the two internal experiments, not approved assets. Models and original PNG frames remain ONLY in the 30-day [Run154 quarantined action artifact](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44192763186), not committed to the product. The Git branch contains source code, logs, machine measurements, a small rejection contact sheet and a SHA256 evidence manifest, but no GLB.

## Human inspection of real eight-view contact sheet — **REJECTED**

I opened the [actual GLB roundtrip four-view comparison, both LOD tiers](research-evidence-run154-REAL-GLB-HAIR-NO_RELEASE/run154_actual_glb_fourview_pair_UNAPPROVED.jpg) at full resolution rather than relying on file existence or successful import:

- At the front, the face reads as a stylized cartoon with large circular, protruding eye globes, a hard thin beige heart outline and featureless belly; cream point-like strands do not create plush natural second down.
- Both 45-degree views reveal eyes projecting far in front of the facial plane rather than integrated masked-owl sockets.
- At strict profile the entire **eyes and heart-disc assembly is floating visibly detached from the head**, a hard anatomical no-go. The side contour reads as a long narrow white bean, not a compact crouched Tyto juvenile.
- Rear remains a nearly featureless white volume with an unnatural hair halo. The so-called hollow support is a smooth cylindrical platform with a uniform ring and no recognizable senescent eucalypt bark.
- The 1-in-3 LOD makes sparse, spiky strands and empty tuft patches much more conspicuous. Full-density rendering has more soft-looking white coverage, but the underlying face/side/back anatomy remains entirely wrong; no artistic quality pass at either tier.

Converting the **real** native fibres does close one previous *format* gap (Run153's mesh-only GLB lost hair), but this is **not** a usable furry owl pet. It is expensive geometry for a portable static model: 456k/192k triangles, 15.6/5.47 MB and no animation. Those numbers are not physical phone measurements and do **not** prove mobile WebGL performance; therefore no mobile claim is made. This technical success must not be confused with a new high-quality sculpt, rig or approved candidate.

## Rights / cost / integrity / independence

The upstream sculpt and curves are an original locally authored Blender experiment; Run154 fetches only the known original Run153 internal research source, no externally purchased/licensed donor. Extra provider payment: **$0**. The [actual evidence directory](research-evidence-run154-REAL-GLB-HAIR-NO_RELEASE/) contains `run154_summary.json`, the two full GLB roundtrip metrics files, complete `blender_run154.log`, explicit `NO_RELEASE.txt`, a saved comparison image and `sha256_manifest.json` covering six materialized audit files. Any artifact with missing/failed images must not be called a visual pass; here all eight actual render outputs are verified in metrics and the contact sheet was reviewed.

Only the dedicated Run154 workflow and `owl-pet/3d-experiments/172-tyto-castanops/**` have changed from the previous isolated Run153 commit. No changes to main, 251-species production, existing cat WebGL prototype, source concept art or deployment. Neither source nor GLBs are placed in the public product branch. CI green is a **reproducible technical run**, not final art approval.

## Conclusion

**ART_REJECTED / NO_RELEASE.** Practical positive: Blender native strand groom can actually be transported as real glTF mesh without silently disappearing, with truthful full-vs-LOD size and triangle measurements. The result is far too costly and has the same structural facial detachment, weak side/back and non-natural fur as the earlier rejected sculpt. Do **not** pursue mere fibre-count changes to this wrong base; move to a professionally coherent juvenile sculpt or much better multiview geometry with transferable hair and then independently validate side/back and actual mobile WebGL before release.
