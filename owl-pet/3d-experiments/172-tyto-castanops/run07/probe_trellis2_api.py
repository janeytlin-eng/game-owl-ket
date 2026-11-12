#!/usr/bin/env python3
"""Read-only, free public TRELLIS.2 Hugging Face Space API availability probe.
No model generation, payment, user credentials or private reference upload.
"""
from __future__ import annotations
import json,traceback
from pathlib import Path

out=Path("owl-pet/3d-experiments/172-tyto-castanops/run07/output")
out.mkdir(parents=True,exist_ok=True)
status={"service":"microsoft/TRELLIS.2 Hugging Face Space",
        "scope":"read-only public API introspection",
        "public_reference":"#172 v3 GitHub original; no input uploaded",
        "paid_usage":False,
        "actual_3d_inference":False}
try:
    from gradio_client import Client
    c=Client("microsoft/TRELLIS.2",verbose=False)
    api=c.view_api(return_format="dict")
    status["status"]="api_accessible"
    status["api_description"]=str(api)[:20000]
except Exception as e:
    status["status"]="api_not_accessible"
    status["error_type"]=type(e).__name__
    status["error"]=str(e)[:1500]
(out/"trellis2_public_api_probe.json").write_text(json.dumps(status,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({k:v for k,v in status.items() if k!="api_description"},indent=2,ensure_ascii=False))
