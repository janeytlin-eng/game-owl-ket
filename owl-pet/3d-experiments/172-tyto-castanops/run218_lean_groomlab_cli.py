#!/usr/bin/env python3
"""Run218. No-fee reproducible narrow GroomLab CLI compile and smoke; never a pet release."""
from __future__ import annotations
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = ROOT / "owl-pet/3d-experiments/172-tyto-castanops/run218-evidence"
EVIDENCE.mkdir(parents=True, exist_ok=True)
PLATE = ROOT / "owl-pet/design/concepts/172-tyto-castanops-v3.png"
EXPECTED = "881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
SOURCE = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "owl172-run218-groomlab"
BUILD = SOURCE / "build/lean-cli"
UPSTREAM = "https://github.com/thekesslereffect/groomlab.git"
COMMIT = "5e81163e3520e14e99f001c41c441f85a186daf9"
report = {"run":218, "subject":"#172 Tyto castanops v3 rightmost cream mesoptile",
          "scope":"native free groom engine qualification, not character model",
          "upstream":UPSTREAM, "upstream_pin":COMMIT,
          "paid_spend_usd":0, "release":"NO_RELEASE",
          "new_tyto_model":False, "art_gate":"NOT_PASSED",
          "phone_hardware_webgl":"NOT_TESTED",
          "steps":{}, "created_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
def run(label, cmd, cwd=ROOT, timeout=120):
    path = EVIDENCE / (label+".log")
    start=time.monotonic()
    code=None
    error=None
    with path.open("wb") as out:
        try:
            completed = subprocess.run(cmd, cwd=cwd, stdout=out,
                stderr=subprocess.STDOUT, timeout=timeout, check=False)
            code=completed.returncode
        except (subprocess.TimeoutExpired, OSError) as exc:
            error = repr(exc)
    data=path.read_bytes()
    summary={"cmd":list(map(str,cmd)), "cwd":str(cwd), "code":code,
             "error":error, "seconds":round(time.monotonic()-start,2),
             "log_bytes":len(data), "log_sha256":hashlib.sha256(data).hexdigest(),
             "last_3000_bytes":data[-3000:].decode("utf-8","replace")}
    report["steps"][label]=summary
    return code==0
try:
    if not PLATE.exists():
        report["status"]="MISSING_REFERENCE"
    else:
        data=PLATE.read_bytes()
        digest=hashlib.sha256(data).hexdigest()
        report["reference"]={"path":str(PLATE.relative_to(ROOT)),"bytes":len(data),
                             "sha256":digest,"valid":digest==EXPECTED}
        if digest!=EXPECTED:
            report["status"]="REFERENCE_MISMATCH"
        else:
            run("environment",["bash","-lc","cmake --version; ninja --version; c++ --version | head -1; nproc; free -h"],timeout=25)
            shutil.rmtree(SOURCE,ignore_errors=True)
            if not run("clone",["git","clone","--depth","1","--branch","dev",UPSTREAM,str(SOURCE)],timeout=100):
                report["status"]="CLONE_FAILED"
            elif not run("pin_checkout",["git","checkout","--detach",COMMIT],cwd=SOURCE,timeout=20):
                report["status"]="UPSTREAM_HEAD_MOVED_NOT_PINNED"
            elif not (SOURCE/"LICENSE").exists():
                report["status"]="LICENSE_NOT_FOUND"
            elif "Apache License" not in (SOURCE/"LICENSE").read_text(encoding="utf-8",errors="replace"):
                report["status"]="LICENSE_UNVERIFIED"
            else:
                # No Alembic/Python/tests/app; run217's default RelWithDebInfo CLI took >470s.
                flags=["-DCMAKE_BUILD_TYPE=Release",
                       "-DCMAKE_CXX_FLAGS_RELEASE=-O1 -DNDEBUG",
                       "-DCMAKE_C_FLAGS_RELEASE=-O1 -DNDEBUG",
                       "-DGROOMLAB_BUILD_TESTS=OFF",
                       "-DGROOMLAB_BUILD_PYTHON=OFF",
                       "-DGROOMLAB_BUILD_ALEMBIC=OFF",
                       "-DGROOMLAB_BUILD_CAPI=OFF",
                       "-DGROOMLAB_BUILD_BLENDER_HELPER=OFF",
                       "-DGROOMLAB_BUILD_ARNOLD=OFF",
                       "-DGROOMLAB_BUILD_PROCEDURAL=OFF",
                       "-DGROOMLAB_BUILD_RENDERMAN=OFF",
                       "-DGROOMLAB_BUILD_MAYA=OFF"]
                if not run("configure",["cmake","-S",str(SOURCE),"-B",str(BUILD),"-G","Ninja"]+flags,cwd=SOURCE,timeout=210):
                    report["status"]="CONFIGURE_FAILED"
                elif not run("build",["cmake","--build",str(BUILD),"--target","groomlab-cli","--parallel","3"],
                             cwd=SOURCE,timeout=740):
                    report["status"]="LEAN_BUILD_FAILED_OR_TIMED_OUT"
                else:
                    bins=[p for p in BUILD.rglob("groomlab-cli") if p.is_file() and os.access(p,os.X_OK)]
                    report["native_cli_binaries"]=[str(p.relative_to(SOURCE)) for p in bins]
                    if not bins:
                        report["status"]="BUILT_NO_CLI_FOUND"
                    else:
                        cli=str(bins[0])
                        ver=run("cli_version",[cli,"--version"],cwd=SOURCE,timeout=20)
                        ops=run("cli_operators",[cli,"--list-operators"],cwd=SOURCE,timeout=25)
                        # Genuine file reads if an actual .groom is found; never fabricate one.
                        available=[p for p in (SOURCE/"samples").rglob("*.groom") if p.is_file()][:2]
                        report["native_groom_samples"]=[str(p.relative_to(SOURCE)) for p in available]
                        if available:
                            run("cli_groom_info",[cli,"info",str(available[0])],cwd=SOURCE,timeout=40)
                        report["status"]="NATIVE_CLI_SMOKE_PASS_NO_OWL" if (ver and ops) else "CLI_SMOKE_FAILED"
except BaseException as exc:
    report["status"]="PYTHON_INTERNAL_ERROR"
    report["exception"]=repr(exc)
finally:
    report["finished_utc"]=dt.datetime.now(dt.timezone.utc).isoformat()
    p=EVIDENCE/"run218_report.json"
    p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (EVIDENCE/"run218_result.md").write_text("# Run218 real lean GroomLab CLI compile and smoke\n\n"
        +"**"+str(report.get("status","UNKNOWN"))+" / NO_RELEASE**. This is a no-fee tool qualification, not a model or owl-pet.\n"
        +"See run218_report.json, complete command logs and their SHA256s. "
        +"No artwork accepted and no mobile hardware gate.\n",encoding="utf-8")
    print(json.dumps({"status":report.get("status"),"release":"NO_RELEASE","evidence":str(p)},ensure_ascii=False))
