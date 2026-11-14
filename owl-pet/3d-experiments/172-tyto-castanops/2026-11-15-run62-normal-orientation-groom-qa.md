# Run62 — #172 Tyto castanops v3 rightmost mesoptile — 2026-11-15

**ART_REJECTED. Research-only true-3D experiments, not a releaseable/showable owl pet.**

## Preflight
Read owl-pet README/AGENTS/STATUS, #172 species v3 and review, previous Run61 failure audit; recovered Run60 J binary GLB, all Run60 source and visual evidence from independent Drive ZIP, also checked Run41 fallback. The owner's approved chick is a single front view, with no reliable lateral/rear anatomy; age remains unknown; science=false.

## Actual experiments and new finding
The Run60 J continuous trunk was inward-facing, signed volume -0.5726019679 even though UV-welded mesh was watertight/winding-consistent. All 15 separate watertight feet/toes/claws/beak meshes also had inconsistent winding. Rebuilt M with corrected normals/winding: welded body +0.5726019679 signed volume, watertight true, winding-consistent true, all 15 accessories repaired. M: 17 meshes, 69,764 triangles, 3,703,872 bytes. N: M plus 3,200 curved, tapered, genuine 3D down microtufts and correct inherited scene graph transform; 18 meshes, 127,364 triangles, 5,010,408 bytes. Both independent GLB models successfully exported and reimported. An initial tuft rotation/position failure was caught by multiview rendering and fixed before this QA.

Rendered actual VTK front, 3/4, strict side and back views for M and N (8 images, 2 contact sheets). Chromium ANGLE/SwiftShader WebGL2 loaded both GLBs and drew four angles each at emulated 390x600 and 800x800 viewports (16 tests); all graphics error codes 0, one embedded texture loaded, no page errors. These tests are desktop software GPU and browser canvas: no phone hardware, PBR GLTFLoader, FPS or touch pass.

## Rejection
Both M and N ART_REJECTED. M remains a pear-like toy with photo-mapped face and inaccurate short wings/feet and unsupported sides/back. N adds small silhouette fuzz but creates sparse bright hard needles/scratches, not natural rich cream mesoptile. Correct orientation is a legitimate technical fix but does not establish aesthetic quality or realistic anatomy. No user demo, deployment, or character release.

## Free tools and independent archival proof
Used installed trimesh, VTK, scipy, PIL, Chromium, Xvfb. Local Blender/bpy absent; trial access to Blender download and other open-source hosts failed due to DNS. Free CC0 adult owl assets found on the web do not qualify as an age-unknown castanops chick. No paid tools invoked.

45-file Run62 QA ZIP includes two GLBs, original Run60 J, reference crop, code, VTK/browser screenshots, QA reports and SHA256 manifest. It was saved to the pre-existing Google Drive independent research folder, remotely re-downloaded and checked byte-for-byte, ZIP integrity and 44 internal file hashes. Size 17,300,431 bytes; SHA256 ef1a3f396b61b79bdce612210ac73692630dcb066852d1a2226d083556459871.

Drive ZIP: https://drive.google.com/file/d/17LYDmJ50oHg1VOT8jldwwYMe755G_WTx/view

Drive full QA: https://drive.google.com/file/d/1E6bBBKYBD2ocHvRw3pkqStcx8XdT6co8/view

No modification to the main 251-species production pipeline, old concept drawings, active prototype or root game. Next requirements: professional juvenile multiview sculpt, natural layered down, anatomically coherent wings/feet, real phone GLTF/PBR hardware QA.
