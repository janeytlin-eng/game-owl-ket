#!/usr/bin/env python3
"""Independent official MIT TRELLIS.2 ZeroGPU anonymous image-to-native-3D trial.
No accounts, tokens, fees, proxy bypass, or app publication. At most ONE generation.
Reports no-GLB and preserves original #172 rightmost chick crop hash and evidence.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,shutil,traceback
OUT=Path("owl172-run303-evidence");OUT.mkdir(exist_ok=True)
SRC=Path("target-owl172-isolated-WHITE.png")
EXPECTED="6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77"
SPACE="microsoft/TRELLIS.2"
report={"run":"303","date":datetime.now(timezone.utc).isoformat(),
 "space":SPACE,"source":str(SRC),"source_sha256":None,
 "api_discovered":False,"generation_submitted":False,"generation_count":0,
 "anonymous":True,"payment_usd":0,"native_glb":None,"art_approved":False,
 "rights_reviewed":False,"real_phone_tested":False,"release_allowed":False,
 "events":[],"errors":[]}
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ev(x,**kw):report["events"].append({"event":x,**kw})
def dump(): (OUT/"run303_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2,default=str))
def file_candidates(o):
    if isinstance(o,str):
        if o.lower().split("?")[0].endswith(".glb"):
            yield o
    elif isinstance(o,dict):
        for k,v in o.items():yield from file_candidates(v)
    elif isinstance(o,(tuple,list)):
        for v in o:yield from file_candidates(v)
def field_info(p):
    return (p.get("parameter_name") or p.get("name") or ""),p.get("parameter_default")
def fill_params(parameters,source,gen_state=None):
    from gradio_client import handle_file
    vals=[];used_image=False
    for i,p in enumerate(parameters):
        name,default=field_info(p);low=name.lower().replace("-","_")
        typ=str(p.get("type","")).lower()
        if not used_image and ("image" in low or (i==0 and ("image" in typ or "file" in typ))):
            vals.append(handle_file(str(source)));used_image=True
        elif low=="resolution":
            vals.append("512" if isinstance(default,str) else 512)
        elif low in ("decimation_target","target_face_count","target_faces","num_faces"):
            vals.append(20000)
        elif low in ("texture_size","texture_resolution"):
            vals.append(1024)
        elif low in ("randomize_seed","random_seed","use_random_seed"):
            vals.append(False)
        elif low=="seed":vals.append(42)
        elif default is not None:
            vals.append(default)
        elif gen_state is not None and ("state" in low or "mesh" in low or "generated" in low):
            vals.append(gen_state)
        else:
            return None,used_image,"missing required param "+str(name)
    return vals,used_image,None
try:
    if not SRC.exists():raise RuntimeError("missing original rightmost target crop")
    report["source_sha256"]=digest(SRC)
    if report["source_sha256"]!=EXPECTED:raise RuntimeError("reference crop sha mismatch")
    from gradio_client import Client
    # no hf_token, no sign-in. Stops on permission/quota errors.
    c=Client(SPACE,verbose=False,download_files=str(OUT/"gradio_downloads"))
    schema=c.view_api(return_format="dict")
    (OUT/"zeroGPU_api_schema.json").write_text(json.dumps(schema,ensure_ascii=False,indent=2,default=str)[:250000])
    report["api_discovered"]=True
    named=schema.get("named_endpoints",{}) or {}
    ev("api_endpoints",names=list(named))
    options=[]
    for key,v in named.items():
        params=v.get("parameters",[]) or []
        names=[field_info(p)[0] for p in params]
        if any("image" in n.lower() for n in names) and any(w in key.lower() for w in ("generate","image_to_3d","reconstruct")):
            options.append((key,params))
    if not options:raise RuntimeError("No documented generation endpoint with image input; no speculative invocation")
    endpoint,ps=options[0]
    inputs,used,err=fill_params(ps,SRC)
    if err:raise RuntimeError("API parameter mismatch: "+err)
    if not used:raise RuntimeError("image not mapped; refusing text-only fallback")
    ev("generated_request_preflight",api_name=endpoint,num_fields=len(ps),
       params=[field_info(p)[0] for p in ps])
    # Exactly one normal demo request; ZeroGPU quota/auth are enforced upstream.
    report["generation_submitted"]=True;report["generation_count"]=1
    output=c.predict(*inputs,api_name=endpoint)
    preview=json.dumps(output,ensure_ascii=False,default=str)
    (OUT/"generation_output_summary.json").write_text(preview[:30000])
    ev("generation_returned",result_type=type(output).__name__,preview=preview[:500])
    candidates=list(file_candidates(output))
    # Depending on app, generation creates an internal asset; extraction is a distinct
    # non-generation action that packages that output as GLB.
    if not candidates:
        ex=[(k,v.get("parameters",[])) for k,v in named.items()
            if "extract" in k.lower() and "glb" in k.lower()]
        if ex:
            key,params=ex[0]
            required=[field_info(p)[0] for p in params]
            values=[]
            for p in params:
                n,default=field_info(p);low=n.lower()
                if default is not None:values.append(default)
                elif "state" in low or "mesh" in low or "generated" in low:
                    values.append(output[-1] if isinstance(output,(tuple,list)) else output)
                elif "decimation" in low:values.append(20000)
                elif "texture" in low:values.append(1024)
                else:values=None;break
            if values is not None:
                ev("extract_glb",api_name=key,params=required)
                extracted=c.predict(*values,api_name=key)
                (OUT/"extract_output_summary.json").write_text(json.dumps(extracted,default=str)[:30000])
                candidates=list(file_candidates(extracted))
    for item in candidates:
        p=Path(item)
        if p.exists() and p.is_file():
            body=p.read_bytes()
            if len(body)>28 and body[:4]==b"glTF":
                target=OUT/"run303-TRELLIS2-native-NOT_APPROVED.glb"
                shutil.copyfile(p,target)
                report["native_glb"]={"file":str(target),"bytes":len(body),"sha256":digest(target)}
                break
    if not report["native_glb"]:
        raise RuntimeError("generation/extract returned no local native GLB; not a verified model")
except Exception as e:
    report["errors"].append(type(e).__name__+": "+str(e)[:1600])
finally:
    report["final"]="NATIVE_GLB_NEEDS_ART_RIGHTS_PHONE_VALIDATION_NO_RELEASE" if report["native_glb"] else "NO_VERIFIED_NATIVE_MODEL_NO_RELEASE"
    dump()
    print(json.dumps({k:v for k,v in report.items() if k!="events"},ensure_ascii=False,indent=2))
