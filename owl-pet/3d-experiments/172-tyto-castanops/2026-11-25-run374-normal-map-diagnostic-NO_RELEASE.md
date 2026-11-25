# Run374 — native normal texture diagnostic / alternate museum asset — ART_REJECTED / NO_RELEASE
2026-11-25; parent Run373 7aafcf42b836fd5adb18e1f00ee959260b6f1a35. Extra spend $0.
Read current main AGENTS, README, STATUS (206/251, 45 remaining), #172 v3 review and Run373. Cream mesoptile, developed heart mask, buried short wings, concealed tail, age unknown, science=false. Recovered GitHub Actions artifact 14795923598 and verified actual original GLB SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be. Viewed reference crop and existing side rendering. No Blender executable; torch CUDA false.

## Actual new alternate asset exploration
- Museum CC0 specimen MP 148, 262k triangles, https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc and https://muzea.malopolska.pl/en/objects-list/2394. Adult/juvenile suitability not established. Actual requests to museum, Sketchfab API and Objaverse object-paths JSON on Hugging Face failed DNS. No binary obtained.
- https://github.com/canopico-world/PhenoVoxel-Archive/blob/main/model-assets.json was fetched and parsed: tyto-alba record has CC BY 4.0 Innovation Studio Common Barn Owl, source https://sketchfab.com/3d-models/common-barn-owl-19c989a6681145bc999c332699eb852e ; exact Objaverse path https://huggingface.co/datasets/allenai/objaverse/resolve/main/glbs/000-081/19c989a6681145bc999c332699eb852e.glb ; expected 1,690,152 bytes SHA256 29531600a1f221f6fbb8dded12cee4ceea4251b28bd678c494d947dc4c3fc3aa. Archive describes taxidermy scan with mounting block. GitHub fetch_file(base64) for model-tyto-alba.glb returned empty content, blob SHA 282ee8520f715eed2aa8c032710641434fd64289; fetch_blob failed UnicodeDecodeError byte 0xca position 9. No geometry acquired or visual pass claimed. This is a useful precise alternate asset lead but no juvenile guarantee.
- https://grab3d.com/models/animals/owl/ CC0 800k triangles great horned owl with ear tufts and yellow eyes; wrong species/age; direct request failed DNS. Paid assets excluded.

## Actual experiment: distinguish normal-map shading from baked seam
Run373 custom WebGL shader did not sample normal texture. Instead of further mesh edits, isolated glTF normalTexture.scale at 0, .55, 1; only material JSON changed, binary mesh and texture chunk preserved. Actual native GLBs all 1,137,120 bytes, independently loaded with trimesh, 27,372 triangles each, 16,971 original indexed vertices:
0: 1c636d8da9bcd4433381d106cee5d4fee058feae926e1f184a6d4cf035eb5693
.55: c5bc73c2c593b870781020ac77f12423a0195e3a4b818067c48894fb6b8e654e
1: a36ff2b62e10fcd76da248d4f8118f2f14209511fd99485918c329ab07873fb1
Direct GLB buffer accessor and both embedded JPEGs loaded in WebGL2 Chromium with Xvfb and SwiftShader; simulated 390x500 mobile canvas, no hardware claim. Fragment shader explicitly reconstructs tangent frame using UV and position derivatives:
```glsl
vec3 n=normalize(N);vec3 px=dFdx(P),py=dFdy(P);
vec2 tx=dFdx(T),ty=dFdy(T);
float det=tx.x*ty.y-tx.y*ty.x;
if(abs(det)>1e-9){
 vec3 t=normalize((px*ty.y-py*tx.y)/det);
 t=normalize(t-n*dot(n,t));
 vec3 b=normalize((py*tx.x-px*ty.x)/det);
 b=normalize(b-n*dot(n,b)-t*dot(t,b));
 vec3 m=texture(normalMap,T).xyz*2.-1.;
 m.xy*=strength;n=normalize(t*m.x+b*m.y+n*m.z);
}
```
Diffuse directional lighting, approximate gamma, NOT complete glTF PBR conformance. Initial test reused page and produced duplicate/blank frames; rejected those outputs and reran on fresh page per variant. Nine distinct actual rendered screenshots, all getError=0, each draws 27,372 triangles. Foreground RGB mean absolute difference from zero strength (8-bit scale), percent pixels any channel difference >2:
| orientation | .55 MAE / changed | 1 MAE / changed |
|---|---:|---:|
| rear | .987 / 10.89% | 1.826 / 33.05% |
| side | 1.164 / 16.03% | 2.115 / 37.08% |
| front | 1.445 / 25.43% | 2.506 / 48.94% |
Foreground approximated by distance from known background color. Actual full contact sheet visually checked: dark side stripe and crown edge remain visible even with normal map disabled; rear wing shoulder anatomy, foot/support fusion, and down volume remain inadequate. Normal map strength alone cannot resolve the defects. Front heart face survives. All rejected. No new high quality foundation, no mobile hardware QA.

## Evidence
Local full assets and source only; no remote full binary claim. SHA256 test.py 59e1574d312226ced14e734945865c2d0ab0906a17a178a6c2290b923f39f7c3; viewer.html 5424c72b9a315a7ae4928061afe945a8df4ac578185baf701a6ccf712b1b6a81; report.json c1f3c25e9712b3ef493c1525d04511e6a99b2a11e6232140727ba809dda54c53; contact.jpg 208d09ecb209451977c37ea07415750b43935fb938de1475c707446617976f21.
| strength | rear screenshot SHA256 | side | front |
|---|---|---|---|
| 0 | 5de3e459685009a6346c84bfb880d1c56cc4fb1ad1d9f9c21a29c3b76dda6df6 | fac438a6ea4558f9ba36b17a8556645946b71fdc722424d93fba2318f5e92857 | 476e1ded64a7b336da24e9491e6ec0c56735cd478e607e8c9f7baed3280a07e8 |
| .55 | ee33e035267a54b16c72bfbbae1e4a52e41c6f3120ecda0ac9ad73b455adf540 | 534dea944b55d0f8fa46557e4528cb119220d7731ca6510bbcd7e19423a1dd16 | 4743d0b6f341d6ee65ad721461cf00f311a7d5500ef51bd51095004069cdde04 |
| 1 | b512f0d1805f7d3c1d75dbae59cdb2089e44aa7c015543e050d2ba87865ff958 | b3b67171a827e79666aa0e00cb3accae66a91d98d8792b6b1c31ebf7599d90ee | 0ce7421b9c8e7cad085209cc312a4fb41e197b922032e416f826ce1ac8c35c07 |
Tiny contact sheet, 90x104 actual screenshot thumbnail (rows 0/.55/1; rear/side/front columns), SHA256 ac24e23d670af6bef5c1c7d8a65cda788346215d67ab8eb7e3bffa7f7bb5a37f; base64 JPEG:
```base64
/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAA4KCw0LCQ4NDA0QDw4RFiQXFhQUFiwgIRokNC43NjMuMjI6QVNGOj1OPjIySGJJTlZYXV5dOEVmbWVabFNbXVn/2wBDAQ8QEBYTFioXFypZOzI7WVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVn/wAARCABoAFoDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDuPKjXnB455Y1Xa8bJ2xgr7tgmprpsQH34qgxGKxlKxtCF9TRhmWZNy8diD2qxtDWzg9CexxWRp7f6SyjutbC/6hvrVRd1ciSs7FcIicge3Wqi37CRlli2qCRuDZpuptLut1jbYN+4nGc+1RSkfPnrmpc7OxcYXVzUBDAEHIPQ1JcIrpHuzwOxIqlpzbrNfYkfrV+X7ifSrWqM2rMqswiwsaFnbtn9aZ50iMPORAvqrZx+lV78FtwVtpPUjrWbiUhC8yllXB2rjzGzwfYY/nWbnrY1UNLnSJ99frVus6yfzIYW7kDNaNbIxZiapJ5ccZOdpbBNUGnXHWte7gFzayRHHzDgnsfWsJ9EvguFlhPvkj+lYyjd3NoTSViawnH9oIoP3sj9K6Jf9Q31rnbHRZ4byOaeVCsZztXJya6Jf9Q31q4KyIm7sp3kfmW7YHK/MPwrBnvFEpU/3RW7c/ayQLbyQCOTITkfQCsOfQLqRwwliHGO9TKN3cqMrI1NFcSWRI7Oa1ZfuR/Ss3S7I2Fp5TPvYtuJ7VpS/cj+lWtEZt3ZjSzCSV8YwpIJ96osyBi3y8+1Tz6TcnzRG8bBmJUklWWqsWhX3kNHNLA5b+PJyP0rBwdzoU1Y2NEkMtorkEBnO36VtVRt41iWKNQAqgAAdKvV0R2OZ6szv33rH+RpDcRIdryKG70szFImI69qzyMDFRKVi4xuagIIyDkHuKk5+zPtxnPGelZmnyEO0WcrjI9q1F/1DfWqi7kyVnYrjzM/MU/AGmpcwSOUSVWYcYBqG+ujbeSFUsZHwQOw7k1UlRSWYcHPWpcrOxahdXNan3G/ZHs29Od1VbOQy2ys3J5BPrirkv3E+lUtiHuVtxQbpWQKO/SkjuIpG2pIC3pVe9laIhlTzGHCrj9frVFtQlmCMI32lS5yuPLwcYPPXOahzSdi1BtXN1Pvr9at1Rt38xY3/vAGr1aozZj38myNB/eNUWcY61d1SAzWblc+YnzLgZz7Vzb3MqL8yOD7g1hOLbN6bVjY0+QC+C/3gRW6v+ob61yOlm4l1KAiNtoOWYqcAYrrl/1DfWrhsZ1NzPv4g0YlA+ZD+YrNmnXewz1GT9a1Lu6hgHly7iXU4VVJJ/KuUuhP5wYRyYK/3T1qZLUuD0On0lt1n9GNaUv3E+lY+gJKlgfOQoWckA9ccVsS/cj+laR2M5bmVcsGkZc/hVA7t5+Y4znp1Pv61FPNNAZ9ysHDnhlPzfQ1Rjupp4HYJIknZChOa5mnc6E1Y6jSZBJbrg5CttFa9Zem2y2ltDCDkjlie5PWtSuqOxyy3M8Sqegbrj7pp9Nd9iFj2FZ7SSMSxkcH2OAKlySKUWzSqTcFtnJzgHsM1Rs7gygo/wB9e/qKvr/qG+tNO4mrECuGOBu6Z5BFOqOaZYQpc43HaPrWcXnhlZhK7DJ+VjkUnJIai2atPncIkWc8+gJqGGQTRK44z29KsS/cT6VRJCrbumfxGKWq1zME4ZzGg6sOp9hVY3UcLgpJKc9nbIYVDkk7FqLauaiffX61bqnEQxRh0OCKuVoiGZV44WIDuxqi7cVPq4cWwlTnyzlh7Vjm9UrnNc807m9O1jT09/8ASyPVTWyv+ob61yun3YOpwAH7xI/SuqX/AFDfWtIbEVNzL1OASGF2G5Y2zj0PrVeWQAsPXkVpzp5kLr6iuTubtlmI7Fc1ElqXB6HS6Y26zH+8a0JfuJ9KxtAk82wY+khH6CtmX7kf0rWOxlLcy71RJlSoYZ79Ky1hijwiwgbF2Kf7ik5IFTPervlkkztViM9l+tUzeo0byqNyDqRXM27nSkrHR6c++CL1U7T+FadY2ixSRWcXnZDud5B7Z7Vs11R2OWW5QkRZEZHGVYYIrPbQ7FuNjgezmiikFyW20u0tZRLFF+8HRmYnFaS/6hvrRRTQMpXFpFcspl3naMYDkD8cVXbRbFzkxH/vo0UUrBcuQQRW0QjhQIg7CrMv3E+lFFMRmy6XaysxKMpc5ba5GT9Khi0HT4l2pG4X08xsfzooqbIq7NSMYZQOgxVyiirRLP/Z
```
No main, production, concept, deployment modifications. Continue alternate high-quality foundation search, no further normal-strength iteration. ART_REJECTED / NO_RELEASE; no notification.
