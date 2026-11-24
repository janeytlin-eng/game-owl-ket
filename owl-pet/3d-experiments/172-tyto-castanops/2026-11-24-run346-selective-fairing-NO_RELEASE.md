# Run346 — region-selective fairing ablation — NO_RELEASE
2026-11-24. THREE_NATIVE_GLB_REIMPORTED / TWELVE_VTK_VIEWS / ART_REJECTED / WEBGL_UNTESTED / NO_RELEASE.

Read main owl-pet/AGENTS.md (b9ebde6dc406354b77d4297089a6f8f928f3b878), README.md, STATUS.md (f4ceb0b50ec3284020a6945e1c679ebf8d13c215), prototype/index.html (fb04d85da57b6cb54ec48d455e3fc8570380172d), v3 review (50ab5259987180a6a46a428317440f2436bfce56), Run345 and its executed source. Original rightmost v3 juvenile remains the visual anchor; main species production separate. Downloaded actual historical Actions artifact 14733006902, extracted and checked listed SHA256 sums; directly viewed masked reference and six-view historical reconstruction. Source GLB SHA256 be513cd814ef2255101d05f7688c436ed51b669191bb4e91b2a2621c19b79117. No new neural inference. Free local NumPy, SciPy, Trimesh, VTK and Pillow available; Blender, ONNX Runtime, PyMeshLab, Open3D absent; github.com and huggingface.co did not resolve via getent. No paid calls.

## Controlled experiment
Run345 strong uniform fairing melts anatomical features. Test whether approximate anatomical region masks plus bilateral graph weights preserve actual learned geometry rather than painting over it. Same 100534 triangles, same vertex colors across A/B/C, no added primitives; orientation [1,2,0], head +Y/front +Z. A: 60 iterations uniform Laplacian at .42. B: same but reduced rate by up to 88% in approximate face and feet regions. C: B plus fixed color similarity weights (.08+.92*exp(-(distance/30)^2)). No bbox rescaling. Shared low-pass color outside protected regions; cream rear is an unobserved design hypothesis.

Actual reimported GLBs:
- A 2010700 bytes; SHA256 970c514257d96438c9538aaafc426b2ca0c794833b8143969c6ccd3357cfc257
- B 2010700 bytes; SHA256 b48412b6b7f4ac331e59903b31e5a0a503f6eb2f3c3d7f49a30d8930cfcf5423
- C 2010696 bytes; SHA256 ed40aedab2d5035982faece0636289e95c53b17fcf373ec9089295cb8f9297c8

Mean vertex displacement in normalized source units (face / feet / body):
A .00661993 / .00860715 / .00728570
B .00353790 / .00409362 / .00727436
C .00370129 / .00413668 / .00736856
B reduces displacement ~47% in face and ~52% in feet versus A while body displacement stays approximately unchanged. C does not improve these measures over B. Displacement is a preservation proxy, not proof of anatomical accuracy.

Actual VTK 0/45/90/180 degree views for all three, 1200x954 full contact sheet directly inspected; SHA256 0e93b95b6fc5647a70c3585a21cf4e88f7833fff088d0cc083b22221ac24ba8b. Tiny 96x76 thumbnail encoded at run346-local/evidence.jpg.b64, readback equal at 9bf8f3ef318696cefdda6dbf3a2e23ad988b9c92; decoded local SHA256 ec40623afb03471026cf94513c8498ec7e5402068d0e98b38e1f39e9fea1234b. Executed source run346-local/experiment.py readback exact at 462057d8816609e5c145ad56efa6416157fd5c03; Git blob a7a9ed61ef03865c8f487568b659727f98841fe7 matches local. Full GLBs and full renders local only.

## Art gate
B and C preserve toe contours somewhat better than A; eyes still read as dark holes, bill is indistinct, heart disc is too flat in profile, rear has obvious smooth ridges and dark basal band, no convincing fluffy feather silhouette. C has no compelling visible gain over B. All rejected. Do not repeat another full-mesh smoothing or color noise sweep on this donor; use a materially better base or integrated anatomical replacement and down groom. No browser WebGL or physical phone test this run. No extra spend; no main, original concept, species production or deployment changes.
