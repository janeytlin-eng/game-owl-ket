#!/usr/bin/env python3
"""Run217: real, no-fee native GroomLab CLI/GLB-groom tool qualification.

This is a technical exploratory test, NOT a Tyto castanops character generator.
Never auto-approve or publish a model from this script.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "owl-pet" / "3d-experiments" / "172-tyto-castanops" / "run217-evidence"
OUTPUT.mkdir(parents=True, exist_ok=True)
UPSTREAM = "https://github.com/thekesslereffect/groomlab.git"
SRC = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "owl172-run217-groomlab-src"
PLATE = ROOT / "owl-pet" / "design" / "concepts" / "172-tyto-castanops-v3.png"
EXPECTED_SHA = "881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d"
report = {"experiment": "run217-free-artist-grade-groom-tool-qualification",
          "date_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "subject": "#172 Tyto castanops v3 rightmost cream mesoptile",
          "release": "NO_RELEASE", "art_gate": "NOT_PASSED",
          "phone_webgl_gate": "NOT_TESTED", "paid_spend_usd": 0,
          "upstream": UPSTREAM, "steps": {}}

def execute(label, argv, cwd=None, timeout=150):
    before = time.monotonic()
    record = {"cmd": argv, "cwd": str(cwd or ROOT), "timeout_s": timeout}
    try:
        cp = subprocess.run(argv, cwd=cwd or ROOT, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            timeout=timeout, check=False)
        log = cp.stdout or ""
        record.update(return_code=cp.returncode, duration_s=round(time.monotonic()-before, 2),
                      log_tail=log[-2500:])
    except Exception as exc:
        log = str(exc)
        record.update(error=repr(exc), duration_s=round(time.monotonic()-before, 2),
                      log_tail=log[-2500:])
    (OUTPUT/(label+".log")).write_text(log, encoding="utf-8", errors="replace")
    report["steps"][label] = record
    return record.get("return_code") == 0

def dump():
    report["date_finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    p = OUTPUT/"run217_report.json"
    p.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    (OUTPUT/"run217_report.md").write_text(
        "# Run217 source-groom feasibility, not a character\n\n"
        + "Native sculpt, natural owl anatomy, photographic down and phone GPU acceptance are **not satisfied**.\n"
        + "Tool status: **"+str(report.get("status","INCOMPLETE"))+"**; **NO_RELEASE**.\n"
        + "No paid services, no production changes. See run217_report.json and command logs.\n", encoding="utf-8")
    return p

try:
    if not PLATE.exists():
        report["status"] = "SOURCE_MISSING"
    else:
        data=PLATE.read_bytes()
        digest=hashlib.sha256(data).hexdigest()
        report["reference"]={"path":str(PLATE.relative_to(ROOT)),
                             "bytes":len(data),"sha256":digest,
                             "matches_expected":digest==EXPECTED_SHA}
        if digest!=EXPECTED_SHA:
            report["status"] = "SOURCE_HASH_MISMATCH"
        else:
            execute("environment", ["bash","-lc","cmake --version; c++ --version | head -1; git --version"],timeout=20)
            if SRC.exists():
                shutil.rmtree(SRC)
            if not execute("clone", ["git","clone","--filter=blob:none","--depth=1","--branch=dev",UPSTREAM,str(SRC)],timeout=180):
                report["status"]="UPSTREAM_CLONE_BLOCKED"
            else:
                execute("upstream_commit", ["git","rev-parse","HEAD"],cwd=SRC,timeout=12)
                license_file=SRC/"LICENSE"
                lic = license_file.read_text(encoding="utf-8",errors="replace") if license_file.exists() else ""
                report["license"]={"license_file_found":license_file.exists(),
                                   "apache_2_string_present":"Apache License" in lic and "Version 2.0" in lic}
                if not report["license"]["apache_2_string_present"]:
                    report["status"]="UNVERIFIED_UPSTREAM_LICENSE"
                elif not execute("cmake_configure",["cmake","--preset","linux-core"],cwd=SRC,timeout=380):
                    report["status"]="GROOMLAB_CONFIGURE_FAILED"
                elif not execute("cli_build",["cmake","--build","--preset","linux-core","--target","groomlab-cli","--parallel","2"],cwd=SRC,timeout=470):
                    report["status"]="GROOMLAB_CLI_BUILD_FAILED"
                else:
                    candidates = [p for p in SRC.glob("build/**/groomlab-cli") if p.is_file()]
                    report["native_cli_binaries"]=[str(p.relative_to(SRC)) for p in candidates]
                    if candidates:
                        execute("cli_help", [str(candidates[0]),"--help"],cwd=SRC,timeout=40)
                        samples = [p for p in SRC.rglob("*.groom") if "build/" not in str(p.relative_to(SRC))][:5]
                        report["upstream_groom_samples"]=[str(p.relative_to(SRC)) for p in samples]
                        if samples:
                            execute("sample_groom_info",[str(candidates[0]),"info",str(samples[0])],cwd=SRC,timeout=60)
                    report["status"]="CLI_BUILT_NO_OWL_GROOM_ART" if candidates else "BUILD_PASSED_CLI_MISSING"
except BaseException as exc:
    report["status"]="INTERNAL_EXCEPTION_NO_RELEASE"
    report["internal_exception"]=repr(exc)
finally:
    dump()
    print(json.dumps({"status":report["status"],"release":"NO_RELEASE",
                      "evidence":str(OUTPUT)},ensure_ascii=False))
