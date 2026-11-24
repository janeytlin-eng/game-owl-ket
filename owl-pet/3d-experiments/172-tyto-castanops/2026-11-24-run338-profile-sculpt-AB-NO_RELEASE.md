# Run338 — full continuous profile sculpt A/B — NO_RELEASE
2026-11-24. TWO_NATIVE_GLB_REIMPORTED / TWELVE_VTK_VIEWS / ART_REJECTED / WEBGL_UNTESTED / NO_RELEASE.

Read main owl-pet/AGENTS.md, README.md, STATUS.md, prototype/index.html, #172 v3 review, and Run337 record at 88822ecaec546c629191fa48cfa5a5b74fa3f1fd. Retrieved and visually inspected the actual main #172 v3 PNG (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b). Right-hand age-unknown mesoptile only. Front proportions estimated from the image; side/back depth inferred, not scientifically verified.

## Actual experiment
After repeated failed isolated grooming swatches, returned to full-body anatomy. Free local Python/NumPy/SciPy/Trimesh/VTK 9.6.2. Continuous interpolated cross-sectional head/trunk surface (241 longitudinal rings x 256 azimuth samples), heart-outline signed distance facial sculpt, paired recessed orbital bowls, small nasal ridge, subtle continuous shoulder transitions, vertex pigmentation. Separate eyeballs, tapered hooked bill, feather-leg placeholders and swept toes/claws; no claim of accurate feet or a finished groom. Exported two real GLBs, independently reimported and rendered actual meshes at 420x480 for six angles (0,45,90,135,180,315 degrees). Viewed both full 1260x960 montages. No browser performance or physical-phone test.

A: 20 meshes, 126932 triangles, 2522156 bytes, SHA256 59beedd2f5e43503fac7b8a2b7b21d434269065f9b3d43f25553bf9b2ef319e3.
B: 20 meshes, 126932 triangles, 2522164 bytes, SHA256 1d6aa1271c0ff933efe6e5052f8a16ec8e6e8e9aa9c95adf2cdf5d60d322cb37.
A montage SHA256 1fb176029a8f5761e49868ba1fb941b2a4e266822726b413fb2fc374a3b53ffe.
B montage SHA256 aa28c529412fe2257c6c54d2aa9616ec0e62083db0b9b70acb1447572070d32b.

A had excessive stony ripples, protruding bead-like eyes, pear-shaped trunk and stiff feet. B reduced displacement amplitude from .0028 to .0010, lightened base pigment, narrowed belly, widened lower head, recessed eyes (y=.207 to .188), pulled bill toward face, increased leg root radius and reduced specular in VTK. B improved eye seating and surface softness, but still resembles a stylized clay/plush figurine, not a realistic feathered owlet. Heart rim unnaturally rigid, orbital texture absent, crown pointed, side silhouette and wing shoulder underdescribed, legs and toes artificial, no individual down silhouette or supported tree hollow. Both ART_REJECTED. Do not present as completed pet. B changes are simultaneous, not isolated causal tests. No scientific approval or user approval.

## Durable evidence
- [Executed B source gzip/base64](run338-local/study-B.py.gz.b64), commit 4d3d007ed9707ce89684824153601c12390b75cd. Exact readback, Git blob 294c14aeb0feea3619cee524629d2ca8e2c71f4a matches local encoded text, 4460 characters. Decoded gzip SHA256 3b9244204b1f6b0b6695302442631e3034f6222c3bab3722ded8bda8ca206b44; uncompressed script SHA256 f8be9de14457bb0fb0eb16663eee71af5a9b8d817b25856d4e4e65afc7444091. Decode with base64 -d then gunzip. A script SHA256 418acc3df07dce1271dd7eae6049d10a93c5f9ff82d8c1ef3bf3e3d6d08242b0; A full source not uploaded.
- [Actual twelve-view diagnostic thumbnail](run338-local/montage-tiny.jpg.b64), commit 5d4b6983a1c2585cf0b52704841c6b8f1485c718, exact readback, Git blob 09bf916d8900086f8ea8c7d74c60bacbb3e57e64 matches local. Decoded 180x69 grayscale JPEG, SHA256 7bb128f0d394dac7cbf3b899008adc8fbdc5690b2aed7783bc0c4c763189ed4e. A left, B right. Tiny thumbnail for audit only; full-resolution images and GLBs generated locally but not uploaded.
- Next prioritize eye socket/feather disc and accurate tarsus/foot anatomy, then realistic groom on a better sculpt. Avoid treating increased triangle count or procedural ripples as feather quality. Run338 has no WebGL or physical-device results.

Zero extra paid services. Research branch based on Run337 only. No changes to main, species production, source concept, existing prototype or live deployment. NO_RELEASE.
