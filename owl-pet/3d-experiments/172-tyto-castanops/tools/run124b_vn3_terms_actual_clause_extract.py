#!/usr/bin/env python3
"""Extract limited source-license clauses from the actually downloaded EN/ZH VN3 PDFs.

This is an audit, not rights clearance. No model asset or extracted full PDF text
is redistributed as an output. All pdfs remain source evidence only.
"""
import datetime, hashlib, json, re, subprocess, sys, tempfile
from pathlib import Path
out=Path(sys.argv[1]);repo=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
pat=re.compile(r"redistribut|re.?distrib|distribut|modify|modificat|commercial|3d data|copyright|licen[cs]|public|third party|third-party|prohibit|permit|resell|resale|source file|prohibit|使用|转让|转载|再分发|二次分发|商用|商业|修改|改造|许可|禁止|販売|再配布",re.I)
words=["redistribution","modification","commercial use","license","禁止","商业","修改","转让","再分发","分发"]
data=[]
for key in ("ja","en","zh"):
 p=repo/f"booth_vn3_{key}_terms_terms.pdf"
 item={"locale":key,"source_pdf_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"source_bytes":p.stat().st_size}
 with tempfile.TemporaryDirectory() as t:
    target=Path(t)/"terms.txt"
    cmd=subprocess.run(["pdftotext","-layout",str(p),str(target)],capture_output=True,text=True)
    item["pdftotext_exit"]=cmd.returncode
    if cmd.returncode:
        item["error"]=cmd.stderr[:400]
    else:
        txt=target.read_text(errors="replace")
        lines=[x.strip() for x in txt.splitlines() if x.strip()]
        item["extractable_characters"]=len(txt)
        item["extractable_lines"]=len(lines)
        matched=[(n,x) for n,x in enumerate(lines,1) if pat.search(x)]
        item["matched_clause_lines"]=[{"line":n,"snippet":x[:230]} for n,x in matched[:80]]
        item["sample_head"]=lines[:6]
 data.append(item)
 (out/("run124b_vn3_"+key+"_rights_excerpt.json")).write_text(json.dumps(item,ensure_ascii=False,indent=2))
 print(json.dumps({"locale":key,"pdf_bytes":item["source_bytes"],"pdf_sha256":item["source_pdf_sha256"],"text_chars":item.get("extractable_characters"),"clause_hits":len(item.get("matched_clause_lines",[]))},ensure_ascii=False))
audit={
 "date_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "referent":"actual public VN3 terms, author geana booth Menhukurou free 3D juvenile",
 "license_sources":{
  "ja":"https://drive.google.com/file/d/1yPx28jJUy_1Hl9AYd53zKhj-45CtMx9X/view",
  "en":"https://drive.google.com/file/d/1nx3UjuJAnlyRTc5g02Wpxi6UMSqeZSeq/view",
  "zh":"https://drive.google.com/file/d/1BrlF8LW9Cwy9OvRCpiKp5VIcrxEjnEes/view",
 },
 "results":data,
 "decision":"NO_RELEASE; no legitimate anonymous asset download, no actual artist GLB and no rights clearance yet",
 "paid_usd":0
}
(out/"run124b_vn3_rights_extraction_audit.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2))
(out/"run124b_readme_NO_RELEASE.md").write_text(
 "# Run124B public artist VN3 license clause audit (NO_RELEASE)\n\n"
 "Two public English/Chinese VN3 license PDFs downloaded by Run124 were actually passed through pdftotext. "
 "This does NOT grant model redistribution, let alone count as art approval. "
 "Key clauses and PDFs are SHA-identified in JSON. User has not authorized any payment.\n\n"
 "Asset still requires BOOTH login and explicit rights for WebGL application and model redistribution. "
 "No geometry downloaded or published, no phone GPU test performed.\n")
(out/"NO_RELEASE.flag").write_text("Unverified model license / no approved source asset / no release.\n")
files=sorted(f for f in out.iterdir() if f.is_file() and f.name not in ("SHA256SUMS.txt","sha_checked.log"))
(out/"SHA256SUMS.txt").write_text("".join(hashlib.sha256(f.read_bytes()).hexdigest()+"  "+f.name+"\n" for f in files))
