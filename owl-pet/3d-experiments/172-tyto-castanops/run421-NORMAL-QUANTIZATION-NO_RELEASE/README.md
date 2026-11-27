# Run421 — native mesh normal packing — ART_REJECTED / NO_RELEASE

2026-11-27. Re-read main AGENTS, README, STATUS (207/251) and Run420. Viewed #172 v3 concept (blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b) again; target right chick is compact cream down, dark eyes and narrow warm heart-disc rim. Recovered full Run415 native GLB (blob 1d709a7108eedcda3a74009e5fabac2b965a0d23, header length equals actual 779732). Already rejected sculpt; this is an asset transport experiment, not an art iteration. Source uses uint16 indices already. Repacked float32 normals to normalized signed int8 VEC3 with 4-byte stride (one padding byte), declared KHR_mesh_quantization as used and required. Positions and indices copied byte-for-byte. Measured angular error against source normals after normalization. Result:

```json
{
  "input_bytes": 779732,
  "output_bytes": 606860,
  "vertices": 21622,
  "triangles": 43240,
  "normal_mean_deg": 0.1706382671604012,
  "normal_p95_deg": 0.2832676794717765,
  "normal_max_deg": 0.378438301792431,
  "zero_normals": 0,
  "position_bytes_identical": true,
  "index_bytes_identical": true
}
```

Native binary output [diagnostic.glb](diagnostic.glb), blob 9563fd05ad2f42cc2fa9274e4489e5a45a035b4a. No renderer or phone acceptance in this run, no glTF external validator claim; downstream shader should normalize interpolated normals. Reproduction: parse GLB JSON/BIN, for each normal component q=round(clamp(x,-1,1)*127), write signed byte triplet + padding. Set NORMAL accessor componentType 5120, normalized true, bufferView byteStride 4; move index view to after packed normals; preserve original POSITION and index byte sequences, update buffer length and GLB chunk lengths. Error=acos(clamp(dot(v,q)/(norm(v)*norm(q)),-1,1)) in degrees.

Free route: local probe found torch/trimesh/VTK/scipy/skimage available; Blender, Open3D, PyMeshLab, transformers and diffusers absent. GitHub/HuggingFace/raw GitHub DNS resolution failed. Existing fal 3D library read required interactive user input; no jobs submitted and no charges. Web search mostly rediscovered previously rejected assets; new listing https://sketchfab.com/3d-models/barn-owltyto-alba-af3cdd38e029430d9c131370ebf1bb33 reports 760 triangles, CC BY, no description or verified juvenile anatomy. No download or visual inspection of that listing claimed. Not accepted as base. No new juvenile-grade sculpt, realistic down, or mobile WebGL acceptance. No changes to main, species workflow, original concept or deployment; no additional fees.
