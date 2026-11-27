# Run407 — independent native PLY source gate — NO_RELEASE

2026-11-27. Read current main owl-pet AGENTS, README/STATUS opening sections (207/251, six recent concept revisions), design tree and #172 v3 species/review records. Original v3 blob remains 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b. Run406 record and its GLB and comparison directory checked at 16045db5e461b2b524b238c44aba742734c36b74. No change to the target: cream thick mesoptile, developed heart disc, dark eyes, pale bill, short down-buried wings, concealed tail, supported feet. Exact age and side/back morphology are not established by v3.

## Actual independent source test

New route: retrieve an ASCII vertex-coloured PLY directly via the GitHub connector rather than relying on external binary download or editing the rejected historical neural mesh.

- Source: https://github.com/mrbid/SeriousShooter/blob/main/assets/ply/ply_low/owl.ply
- Exact immutable blob d9465f2f0a5f1c3343dbca4dd22f31b1c4167295. Both base64 (98,723 characters including whitespace) and complete UTF-8 source returned. Parsed actual ASCII PLY header and all rows: 676 vertices, 1,347 triangular faces, positions, normals and RGBA vertex colours. Blender 4.0.1 header. Bounds X [-0.6068716,0.6105152], Y [-0.60855186,0.6126806], Z [-0.0077822558,1.7108613]; Z up. Two edges with single incidence, one edge with >2 incidence. Not a watertight manifold.
- Actual four-view indexed triangle rasterization on a 720×250 RGB canvas, orthographic Z-up, yaw 0/90/180/270 degrees, depth buffer, barycentric vertex colour/normal interpolation. Common scale 175 px / largest bounds extent. Covered pixels per view: 14283,12050,14283,12050. PNG encoded and visually inspected in this execution (540,358 bytes). It shows a squat brown adult horned owl, pointed ear tufts, pronounced folded adult wing/feather relief, yellow beak and thin exposed yellow legs, small projecting tail, angular low-poly face, no cream down and no Tyto heart mask. Front is the 180° view. This is NOT a suitable juvenile mesh.
- Higher LODs are present in the same repository: ply_med/owl.ply (848,847 bytes, blob 660c8b0fefbc05e27d1bbe62409d41a61fc41cb0) and ply_high/owl.ply (2,929,690 bytes, blob 8916c0d0bc7e7cb3a533ebe815c9189324057d0f). Directory metadata only; not downloaded or visually assessed. No reason to spend more effort increasing detail of the rejected low-LOD silhouette unless independent evidence indicates these are different characters.
- Repository LICENSE is MIT, but README.MD explicitly attributes all assets to Luma Genie and Meshy.AI. Asset-specific generation and redistribution terms not established; do not equate software MIT license to verified model rights. Third-party source and rendered derivative not redistributed in this repository; reproduction metadata retained here. No production asset generated.

## Reproduction method

Fetch the exact blob above or the UTF-8 PLY file and split on end_header newline. Read first 676 lines as float arrays (x,y,z,nx,ny,nz,r,g,b,a) and remaining 1347 lines as three face indices after the leading 3. Center using midpoint of each coordinate bound, scale by 175/max extent. For yaw a and view k, project (x,y,z) to screen ((k+.5)*180+s*((x-cx)*cos(a)-(y-cy)*sin(a)), 125-s*(z-cz)); depth=(x-cx)*sin(a)+(y-cy)*cos(a). For each triangle, fill bounding-box pixels using barycentric coordinates at pixel centers and retain greater depth; interpolate vertex RGB and multiply by .6+.4*max(0,(nx*sin(a)+ny*cos(a))*.7+nz*.5). Background RGB 225. This is a diagnostic renderer, not a WebGL or production PBR test.

## Other zero-cost source checks

GitHub code search: filename:owlet.stl, filename:owl-chick.obj, filename:baby_owl.stl, filename:owl_baby.obj, filename:owlet.glb, filename:barnowl.ply each returned 0. Narrowed owl STL results mostly SuperTux level files (not 3D models); one low-poly owl in research dataset not pursued. PLY search excluding bowl/cowl/plymouth produced two mirrors of the same source blob above. These counts are search observations, not proof of absence.

New print-sculpt route checked:
- https://pinshape.com/items/7324-3d-printed-owl lists a CC0 19.7 MB STL, login required; original geometry and identity not verified, no download.
- https://cults3d.com/en/3d-model/art/baby-owl-kissoon free STL, creator says commercial licence is through subscription, chibi tag; excluded.
- https://cults3d.com/en/3d-model/art/3d-bas-relief-of-a-barn-owl explicitly a relief, not a full orbit model; excluded.
- https://sketchfab.com/3d-models/barn-owltyto-alba-af3cdd38e029430d9c131370ebf1bb33 CC BY, 760 triangles; not downloaded, insufficient evidence of juvenile form.
- https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt explicitly no AI license; excluded again.

Local checks: /mnt/data empty at start, no Blender executable, no bpy, transformers, diffusers, objaverse, pymeshlab, open3d, pyrender, moderngl; torch/trimesh/vtk/skimage/cv2 available. DNS lookup for github.com, api.github.com and huggingface.co returned errno -3 Temporary failure in name resolution. No model cache observed at ~/.cache/huggingface/hub. No paid tools called, no extra spend.

Decision ART_REJECTED / NO_RELEASE. PLY is now a demonstrated additional native mesh transport route but the candidate is the wrong owl and rights are unresolved. No mobile QA, no newly accepted model. Continue seeking independently authored or rights-cleared juvenile sculpt/mesh, preferably actual Tyto chick, not polishing rejected adult or primitive meshes. No changes to main, original concept images, species production process or deployment.
