#!/usr/bin/env python3
"""Run238 actual-browser screenshots -> real seven-view contact; not an art approval."""
from pathlib import Path
from PIL import Image, ImageDraw
import json, hashlib
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"owl-pet/3d-experiments/172-tyto-castanops/run238-evidence"
report=json.loads((OUT/"run237_machine_report.json").read_text())
assert report["run"]=="Run238"
assert report["status"]=="NATIVE_WEBGL2_SOFTWARE_SMOKE_PASS_ART_REJECTED_PHONE_UNTESTED_NO_RELEASE"
views=["front","left","threequarter","right","back","top","bottom"]
canvas=Image.new("RGB",(4*366,2*395),(237,238,240))
draw=ImageDraw.Draw(canvas)
for i,name in enumerate(views):
 p=OUT/f"run237_{name}_WEBGL_RESEARCH_NOT_APPROVED.png"
 b=p.read_bytes()
 assert hashlib.sha256(b).hexdigest()==next(
   v["screenshot"]["sha256"] for v in report["views"] if v["name"]==name)
 im=Image.open(p).convert("RGB")
 assert im.width==640 and im.height==640
 im=im.resize((356,356),Image.Resampling.LANCZOS)
 x=(i%4)*366+5;y=(i//4)*395+25
 canvas.paste(im,(x,y))
 draw.text((x+5,y-19),name+" - actual WebGL2",fill=(35,40,48))
dst=OUT/"run238_REAL_CHROMIUM_WEBGL2_sevenview_PBR_ART_REJECTED_NO_RELEASE.png"
canvas.save(dst)
print(json.dumps({"output":str(dst),"bytes":dst.stat().st_size,
"sha256":hashlib.sha256(dst.read_bytes()).hexdigest(),"views":len(views)}))
