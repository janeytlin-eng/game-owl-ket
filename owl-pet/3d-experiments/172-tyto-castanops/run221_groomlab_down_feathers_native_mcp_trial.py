#!/usr/bin/env python3
"""Run221: *real* open-source GroomLab groom runtime trial, NON-OWL, NO RELEASE.
Deliberate wolf example under Nick Rutlinh (GroomLab), CC BY 4.0; tech-only.
User #172 juvenile's sculpt and premium feather art are NOT represented here.
"""
import datetime,hashlib,json,os,select,subprocess,shutil,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"owl-pet/3d-experiments/172-tyto-castanops/run221-evidence"
OUT.mkdir(parents=True,exist_ok=True)
SOURCE=Path(os.getenv("RUNNER_TEMP","/tmp"))/"owl172-run221-groomlab"
BUILD=SOURCE/"build/lean-cli"
RUNNER=Path(os.getenv("RUNNER_TEMP","/tmp"))/"owl172-run221-sandbox"
RUNNER.mkdir(parents=True,exist_ok=True)
EXPECTED="881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
PIN="5e81163e3520e14e99f001c41c441f85a186daf9"
report={"experiment":"run221-groomlab-open-source-real-fur-runtime","run":220,
    "subject":"#172 Tyto castanops v3 cream juvenile (technical tool qualification only)",
    "actual_groom_subject":"GroomLab example wolf with down-feather preset (NOT AN OWL)",
    "example_mesh_credit":"Wolf by Nick Rutlinh (GroomLab), CC BY 4.0",
    "source":"https://github.com/thekesslereffect/groomlab","upstream_commit":PIN,
    "additional_paid_spend_usd":0,"production_changed":False,
    "character_sample_accepted":False,"art":"NOT_PASSED","phone_hardware_webgl":"NOT_TESTED",
    "release":"NO_RELEASE","steps":{},"files":{}}
def command(label,args,cwd=ROOT,timeout=200):
    file=OUT/(label+".log")
    t=time.monotonic(); err=None;code=None
    with file.open("wb") as h:
        try:
            c=subprocess.run(args,cwd=cwd,stdout=h,stderr=subprocess.STDOUT,timeout=timeout,check=False)
            code=c.returncode
        except Exception as e:err=repr(e)
    data=file.read_bytes()
    report["steps"][label]={"code":code,"error":err,"seconds":round(time.monotonic()-t,2),
        "bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),
        "tail":data[-2000:].decode("utf-8","replace")}
    return code==0
def sha(path):
    data=Path(path).read_bytes()
    return {"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
def decode_result(message):
    if message.get("error"):return {"error":message["error"]}
    res=message.get("result",{})
    out={"isError":res.get("isError",False)}
    for item in res.get("content",[]):
        if item.get("type")=="text":
            try:return dict(out,parsed=json.loads(item.get("text","")))
            except Exception:return dict(out,text=item.get("text","")[:3000])
    return dict(out,other_keys=list(res.keys()))
def transact(p, name, args={}, timeout=75):
    rid=len(report["mcp"])+1
    req={"jsonrpc":"2.0","id":rid,"method":"tools/call","params":{"name":name,"arguments":args}}
    t=time.monotonic(); out=None
    try:
        p.stdin.write(json.dumps(req,ensure_ascii=False)+"\n");p.stdin.flush()
        ready,_,_=select.select([p.stdout],[],[],timeout)
        if not ready:raise TimeoutError(name+" no MCP response within "+str(timeout))
        line=p.stdout.readline()
        if not line:raise RuntimeError("MCP ended: "+str(p.poll()))
        message=json.loads(line)
        if message.get("id")!=rid:raise ValueError("MCP wrong response id")
        out=decode_result(message)
    except Exception as exc:
        out={"error":repr(exc)}
    result={"tool":name,"arguments":args,"seconds":round(time.monotonic()-t,2),
        "result":out}
    report["mcp"].append(result)
    (OUT/("mcp_"+str(rid).zfill(2)+"_"+name+".json")).write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return out
def good(result):
    return "error" not in result and not result.get("isError",False)
try:
    plate=ROOT/"owl-pet/design/concepts/172-tyto-castanops-v3.png"
    report["reference"]=sha(plate) if plate.exists() else {"error":"missing"}
    if report["reference"].get("sha256")!=EXPECTED:raise RuntimeError("reference mismatch")
    if not command("clone",["git","clone","--depth","1","--branch","dev",
           "https://github.com/thekesslereffect/groomlab.git",str(SOURCE)],timeout=130):
        raise RuntimeError("clone blocked")
    if not command("pin",["git","checkout","--detach",PIN],cwd=SOURCE,timeout=30):
        raise RuntimeError("upstream pin unavailable")
    license=(SOURCE/"LICENSE").read_text(encoding="utf-8")
    if "Apache License" not in license:raise RuntimeError("license not verified")
    flags=["-DCMAKE_BUILD_TYPE=Release","-DCMAKE_CXX_FLAGS_RELEASE=-O1 -DNDEBUG",
           "-DGROOMLAB_BUILD_TESTS=OFF","-DGROOMLAB_BUILD_PYTHON=OFF",
           "-DGROOMLAB_BUILD_ALEMBIC=ON","-DGROOMLAB_BUILD_CAPI=OFF",
           "-DGROOMLAB_BUILD_BLENDER_HELPER=OFF","-DGROOMLAB_BUILD_ARNOLD=OFF",
           "-DGROOMLAB_BUILD_PROCEDURAL=OFF","-DGROOMLAB_BUILD_RENDERMAN=OFF",
           "-DGROOMLAB_BUILD_MAYA=OFF"]
    if not command("configure",["cmake","-S",str(SOURCE),"-B",str(BUILD),"-G","Ninja"]+flags,
            cwd=SOURCE,timeout=190):raise RuntimeError("configure failed")
    if not command("build",["cmake","--build",str(BUILD),"--target","groomlab-cli","--parallel","3"],
            cwd=SOURCE,timeout=840):raise RuntimeError("native build failed")
    cli=BUILD/"engine/cli/groomlab-cli"
    if not cli.exists():raise RuntimeError("native exe not found")
    if not command("version",[str(cli),"--version"],cwd=SOURCE,timeout=15):
        raise RuntimeError("CLI not runnable")
    report["mcp"]=[]
    p=subprocess.Popen([str(cli),"mcp","--root",str(RUNNER)],cwd=SOURCE,
      stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,
      text=True,encoding="utf-8",bufsize=1)
    try:
        sample=transact(p,"list_sample_meshes",{},timeout=30)
        presets=transact(p,"list_presets",{},timeout=30)
        mesh_entries=sample.get("parsed",{}).get("meshes",[])
        wolf=next((m for m in mesh_entries if m.get("name")=="wolf"),None)
        if wolf is None:raise RuntimeError("GroomLab own CC BY 4.0 sample wolf unavailable")
        names=presets.get("parsed",{}).get("presets",[])
        candidates=[x for x in names if "fur" in (x.get("name","")+" "+x.get("title","")).lower()]
        chosen=None
        if candidates:
            candidates.sort(key=lambda x:("short" not in (x.get("name","")+" "+x.get("title","")).lower(),
                                    len(x.get("name",""))))
            chosen=candidates[0].get("name")
        chosen="feathers_down"
        report["chosen_preset"]=chosen
        report["preset_target_note"]="Real native down-feather preset test on donor wolf; no Tyto mesh, no pet art approval"
        params={"name":"real_wolf_downfeathers_tech_only","mesh":"wolf"}
        if chosen:params["preset"]=chosen
        created=transact(p,"new_groom",params,timeout=100)
        if not good(created):raise RuntimeError("real groom creation rejected")
        groom="real_wolf_downfeathers_tech_only"
        ev=transact(p,"evaluate",{"groom":groom,"density":0.05},timeout=140)
        report["native_groom_evaluation_success"]=good(ev)
        report["down_feather_strands"]=ev.get("parsed",{}).get("strands",0)
        if not good(ev) or not isinstance(report["down_feather_strands"],int) or report["down_feather_strands"]<=0:
            raise RuntimeError("Native down-feather preset produced zero verified strands")
        saved=transact(p,"save_groom",{"groom":groom,"path":"run221_real_wolf_downfeathers_tech_ONLY.groom"},timeout=90)
        report["saved_native_groom_success"]=good(saved)
        preview=transact(p,"render_preview",
            {"groom":groom,"views":["front","side","back","three_quarter","top"],
             "size":1024,"max_strands":10000,"density":0.04,
             "save_to":"run221_downfeathers_fiveview_technical_ONLY.png"},timeout=200)
        report["fiveview_technical_preview_success"]=good(preview)
        report["fiveview_strands_drawn"]=preview.get("parsed",{}).get("strandsDrawn",0)
        ex=transact(p,"export",{"groom":groom,"path":"run221_wolf_technical_downfeathers.usda",
            "density":0.04},timeout=180)
        report["native_usd_curves_export_success"]=good(ex)
        for candidate in ("run221_real_wolf_downfeathers_tech_ONLY.groom",
                          "run221_downfeathers_fiveview_technical_ONLY.png",
                          "run221_wolf_technical_downfeathers.usda"):
            source=RUNNER/candidate
            if source.is_file() and source.stat().st_size>0:
                report["files"][candidate]=sha(source)
                shutil.copyfile(source,OUT/candidate)
        if report.get("down_feather_strands",0)>0 and any(p.endswith(".png") for p in report["files"]):
            report["status"]="REAL_GROOM_WITH_TECHNICAL_PREVIEW_NO_OWL"
        elif report.get("saved_native_groom_success"):
            report["status"]="REAL_GROOM_SAVE_ONLY_NO_OWL"
        else:report["status"]="MCP_SESSION_NO_GROOM_DELIVERABLE"
    finally:
        p.stdin.close()
        try:p.wait(timeout=20)
        except subprocess.TimeoutExpired:p.kill()
except BaseException as exc:
    report["status"]="FAILED_NO_RELEASE"
    report["exception"]=repr(exc)
finally:
    report["finished_utc"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
    (OUT/"run221_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (OUT/"LICENSE_CREDIT.txt").write_text(
      "This technical groom uses a non-owl example from GroomLab. Wolf by Nick Rutlinh (GroomLab), CC BY 4.0.\n"
      "Source: https://github.com/thekesslereffect/groomlab\n"
      "Not an accepted owl or public character model. Never claim the actual wolf screenshot is #172.\n",encoding="utf-8")
    print(json.dumps({"status":report["status"],"release":"NO_RELEASE",
       "files":report["files"],"log":str(OUT/"run221_report.json")},ensure_ascii=False))
