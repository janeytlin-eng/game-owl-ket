#!/usr/bin/env python3
"""Run134: non-GPU public API inspection of another no-cost native image->mesh service.
Research only: Tencent Hunyuan license is not a release/distribution clearance."""
import json, pathlib, traceback, time, hashlib
from PIL import Image
from gradio_client import Client
R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run134-HUNYUAN-MINI-TURBO-ACTUAL-PROBE-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
S=R/"research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/rightmost_baby_owl_512_rgba.png"
status={"run":134,"date":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
 "service":"tencent/Hunyuan3D-2mini-Turbo","paid":False,"token_used":False,
 "GPU_inference":False,"GLB_obtained":False,"license":"tencent-hunyuan-community: restricted; NO_RELEASE",
 "stage":"preflight","art":"UNREVIEWED","release":"NO_RELEASE"}
def write(name,object):
 (O/name).write_text(json.dumps(object,indent=2,ensure_ascii=False,default=str)+"\n")
try:
 assert S.is_file(),"Missing genuine rightmost chick input"
 assert hashlib.sha256(S.read_bytes()).hexdigest()=="e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8"
 im=Image.open(S)
 assert im.size==(512,512)
 status["source_sha256"]=hashlib.sha256(S.read_bytes()).hexdigest()
 status["stage"]="live_public_gradio_schema"
 cli=Client(status["service"],verbose=False)
 spec=cli.view_api(return_format="dict")
 public={}
 for kind in ("named_endpoints","unnamed_endpoints"):
  endpoints=spec.get(kind,{})
  for key,fn in endpoints.items():
   public[key]={"kind":kind,"parameters":fn.get("parameters",[]),"returns":fn.get("returns",[])}
 write("run134_exact_live_api_schema.json",public)
 status["endpoints"]=[k for k in public]
 status["candidate_generation_endpoints"]=[k for k in public if any(v in k.lower() for v in ("generate","shape","mesh","predict","3d"))]
 status["stage"]="schema_recorded"
except Exception as ex:
 status["error"]=type(ex).__name__+": "+str(ex)[:2000]
 (O/"run134_traceback.txt").write_text(traceback.format_exc())
finally:
 status["finished"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
 write("run134_status.json",status)
 (O/"NO_RELEASE.flag").write_text("Run134 is schema and license research, not a generated pet or a cleared commercial model.\n")
 print("RUN134",json.dumps(status),flush=True)
