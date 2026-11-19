#!/usr/bin/env python3
"""Run212c: repair data-derived transparent eye holes in the #172 reference crop.

Reads the immutable Run211 or Run212 GitHub Actions evidence archive locally,
preserves original RGB untouched, and fills small enclosed holes in its alpha.
Evidence prep only; NOT a 3D model or art acceptance.
Usage: python run212c_repair_reference_alpha_forensic.py <evidence.zip> <outdir>
Requires: pillow opencv-python-headless numpy
"""
import sys, zipfile, io, hashlib, json
from pathlib import Path
from PIL import Image, ImageDraw
import cv2
import numpy as np

EXPECTED_MASK_SHA256="fcb3527dae6fa9aee4428d9c76ee803106a4be313a9f2ae40047465e84fa8819"
def sha256(data): return hashlib.sha256(data).hexdigest()
def main():
    if len(sys.argv)!=3: raise SystemExit("usage: SCRIPT evidence.zip outdir")
    source=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(source) as z:
        raw=z.read("source_rightmost_grabcut_rgba.png")
    assert sha256(raw)==EXPECTED_MASK_SHA256, "Unsupported original crop: source hash mismatch"
    rgba=np.array(Image.open(io.BytesIO(raw)).convert("RGBA"))
    assert rgba.shape==(595,490,4), rgba.shape
    orig_alpha=rgba[:,:,3]
    inverted=cv2.bitwise_not(orig_alpha)
    n,labels,stats,centers=cv2.connectedComponentsWithStats(inverted)
    corrected=rgba.copy(); repairs=[]
    for i in range(1,n):
        x,y,w,h,area=map(int,stats[i])
        enclosed=x>0 and y>0 and x+w<rgba.shape[1] and y+h<rgba.shape[0]
        if not enclosed or area>=.02*orig_alpha.size: continue
        corrected[labels==i,3]=255
        repairs.append({"bbox_xywh":[x,y,w,h],"pixels":area,
                        "mean_rgb":[round(float(v),2) for v in rgba[labels==i,:3].mean(axis=0)]})
    count=int(np.count_nonzero(corrected[:,:,3]>orig_alpha))
    assert len(repairs)==2 and count==1215,(repairs,count)
    assert np.array_equal(corrected[:,:,:3],rgba[:,:,:3]),"Source RGB must not change"
    fixed_path=out/"source_rightmost_GRABCUT_eyes_filled_UNAPPROVED.png"
    Image.fromarray(corrected,"RGBA").save(fixed_path)
    preview=Image.new("RGB",(1000,625),(239,237,229))
    for idx,frame in enumerate([rgba,corrected]):
        panel=Image.new("RGBA",(490,595),(212,232,240,255))
        panel.alpha_composite(Image.fromarray(frame,"RGBA"))
        preview.paste(panel.convert("RGB"),(idx*500,30))
    ImageDraw.Draw(preview).text((10,8),"ORIGINAL: pupils transparent",(30,30,30))
    ImageDraw.Draw(preview).text((510,8),"FIXED: original RGB pupils preserved",(30,30,30))
    contact_path=out/"matte_BEFORE_AFTER_QA_UNAPPROVED.png"
    preview.save(contact_path)
    report={"status":"REFERENCE_ALPHA_FIXED_NO_3D","source_archive_sha256":sha256(source.read_bytes()),
      "source_mask_sha256":sha256(raw),"filled_interior_regions":repairs,"restored_alpha_pixels":count,
      "foreground_coverage_before":float(np.count_nonzero(orig_alpha))/orig_alpha.size,
      "foreground_coverage_after":float(np.count_nonzero(corrected[:,:,3]))/orig_alpha.size,
      "output_fixed_png_sha256":sha256(fixed_path.read_bytes()),
      "contact_sha256":sha256(contact_path.read_bytes()),"release":"NO_RELEASE"}
    (out/"run212c_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
