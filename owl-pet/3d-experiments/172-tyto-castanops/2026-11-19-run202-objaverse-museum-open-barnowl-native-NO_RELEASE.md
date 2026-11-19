# Run202 actual no-charge Objaverse museum barn owl native QA

Date: 2026-11-19T00:50:22.662297+00:00

Source: https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc (museum-provided CC0) via official Objaverse 1.0 HuggingFace mirror. Adult taxidermy source is only a potential sculpt/anatomy donor, **not** proof of the v3 age-unknown cream second-down juvenile.

Actual results: {
  "run": 202,
  "date_utc": "2026-11-19T00:50:15.438711+00:00",
  "target": "#172 Tyto castanops v3 rightmost age-unknown cream mesoptile",
  "candidate": "Polish Virtual Museums Barn owl CC0 scanned taxidermy, adult Tyto / potential reference donor only",
  "source_uid": "0e65de5934db4f0eae02835ba7227dcc",
  "source_original": "https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc",
  "distribution": "https://huggingface.co/datasets/allenai/objaverse",
  "license_claim": "Original Sketchfab page says CC0; dataset-level ODC-By does not replace per-object license",
  "original_verified": true,
  "source_downloaded": true,
  "new_native_glb": true,
  "geometry_parsed": true,
  "sevenview": false,
  "independent_art_approval": false,
  "actual_physical_phone_gpu": false,
  "no_extra_payment": true,
  "final_status": "NO_NEW_MODEL_NO_RELEASE",
  "sketchfab_metadata": {
    "uid": "0e65de5934db4f0eae02835ba7227dcc",
    "name": "Barn owl",
    "isDownloadable": true,
    "license": {
      "uri": "https://api.sketchfab.com/v3/licenses/7c23a1ba438d4306920229c12afcb5f9",
      "label": "CC0 Public Domain",
      "fullName": "CC0 Public Domain",
      "requirements": "Credit is not mandatory. Commercial use is allowed.",
      "url": "http://creativecommons.org/publicdomain/zero/1.0/",
      "slug": "cc0"
    },
    "faceCount": 261966,
    "vertexCount": 130961
  },
  "native_sha256": "6412ffd575360397bd90d391d3d4c23397f225945cdef3ec5727bfd91504cd44",
  "native_bytes": 43225496,
  "original_path_in_cache": "/home/runner/.objaverse/hf-objaverse-v1/glbs/000-041/0e65de5934db4f0eae02835ba7227dcc.glb",
  "geometry": {
    "unique_meshes": 12,
    "triangles": 261966,
    "vertices": 756317,
    "bounds": [
      [
        -0.21720988916396777,
        -0.0012066762488420564,
        -0.34814716438032167
      ],
      [
        0.2152903544988547,
        0.5628321491639525,
        0.11197058167116936
      ]
    ],
    "material_kinds": [
      "PBRMaterial"
    ]
  }
}

Actual events: ["Validated owl-pet existing cat prototype, v3 design, Run201d, negative SHA register and exact pinned rightmost owl image", "Public Sketchfab metadata HTTP200 read (read-only, no unauthorized download API)", "Official objaverse.load_objects([known_exact_Sketchfab_UID]) started; no auth or paid service", "Downloaded 43225496 bytes valid GLB magic SHA256=6412ffd575360397bd90d391d3d4c23397f225945cdef3ec5727bfd91504cd44", "True native trimesh import passed {\"unique_meshes\": 12, \"triangles\": 261966, \"vertices\": 756317, \"bounds\": [[-0.21720988916396777, -0.0012066762488420564, -0.34814716438032167], [0.2152903544988547, 0.5628321491639525, 0.11197058167116936]], \"material_kinds\": [\"PBRMaterial\"]}"]

Errors: ["RuntimeError: No imported VTK props"]

Real art acceptance is deliberately false: source age/feather tract and tree-hollow anatomy conflict with target; seven views are diagnostic, NOT an accepted figure. Native renderer does not establish physical smartphone GPU performance. Source GLB remains in the private runner artifact, not committed to public Git. No additional payment or main/251-species changes. NO_RELEASE.
