#!/usr/bin/env python3
"""Run256 evidence gate: verifies 21 browser screenshots and builds unapproved review contacts."""
from pathlib import Path
from PIL import Image, ImageDraw
import json, hashlib

root=Path("owl-pet/3d-experiments/172-tyto-castanops/run256-evidence")
cameras=["front","left","threequarter","right","back","top","bottom"]
summary={"run":256,"art_approved":False,"release":"NO_RELEASE","phone_gpu":"UNTESTED","variants":{}}
frames=[]
for v in ("A","B","C"):
    p=root/f"browser_{v}/run256_browser_report.json"
    if not p.exists():
        summary["variants"][v]={"status":"MISSING_REPORT"};continue
    r=json.loads(p.read_text())
    gates=r.get("gates",{})
    summary["variants"][v]={"status":r.get("status"),"gates":gates,"model":r.get("browser",{}).get("stats",{})}
    assert len(gates)==10 and all(gates.values()),(v,gates)
    hashes=set()
    for view in cameras:
        img=p.parent/f"{view}_ACTUAL_THREEJS_WEBGL2_ART_REJECTED.png"
        rec=next(x for x in r["views"] if x["view"]==view)
        actual=hashlib.sha256(img.read_bytes()).hexdigest()
        assert actual==rec["file"]["sha256"],(v,view)
        hashes.add(actual)
        frames.append((v,view,Image.open(img).convert("RGB")))
    assert len(hashes)==7,(v,"duplicate_views")
assert len(frames)==21,("evidence_incomplete",len(frames))
grid=Image.new("RGB",(1280,2100),(230,232,236));d=ImageDraw.Draw(grid)
for i,(v,view,img) in enumerate(frames):
    x=(i%4)*320;y=(i//4)*350
    grid.paste(img.resize((310,310)),(x+4,y+27))
    d.text((x+5,y+6),f"Run256 {v} / {view} / NO RELEASE",fill=(15,15,15))
dst=root/"run256_ABC_21_ACTUAL_WEBGL2_VIEWS_ART_UNAPPROVED.png"
grid.save(dst)
target=Image.open("owl-pet/design/concepts/172-tyto-castanops-v3.png").convert("RGB").crop((950,280,1430,820))
front={v:im for v,view,im in frames if view=="front"}
comp=Image.new("RGB",(1460,435),(238,238,238));c=ImageDraw.Draw(comp)
for j,(label,img) in enumerate([
 ("TARGET rightmost chick: 2D only",target),
 ("A original neural 3D",front["A"]),
 ("B neural owl + CC0 tree hollow",front["B"]),
 ("C CC0 ADULT negative control",front["C"]),
]):
    comp.paste(img.resize((348,391)),(j*365+6,34))
    c.text((j*365+6,8),label,fill=(10,10,10))
comp.save(root/"run256_TARGET_AND_NATIVE_SOURCE_HABITAT_COMPARISON_ART_UNAPPROVED.png")
summary["software_webgl2"]="PASS_21_SPATIAL_VIEWS"
summary["montage_sha256"]=hashlib.sha256(dst.read_bytes()).hexdigest()
(root/"run256_webgl_report.json").write_text(json.dumps(summary,indent=2)+"\n")
print(json.dumps(summary,indent=2))
