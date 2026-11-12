#!/usr/bin/env python3
"""Experimental independent saliency matte comparison for #172 rightmost chick.
Runs u2netp rembg weights (open source, CPU; may require model download).
Never silently substitutes this output as approved 3-D geometry.
"""
import argparse,io,json,hashlib
from pathlib import Path
import numpy as np
from PIL import Image
import cv2
from rembg import remove,new_session

def hsh(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

p=argparse.ArgumentParser()
p.add_argument("--output-dir",type=Path,required=True)
a=p.parse_args();o=a.output_dir
source=Image.open(o/"chick_reference_uncut.png").convert("RGB")
src=np.asarray(source);h,w=src.shape[:2]
print("u2netp saliency model; free open-source model, unapproved output")
session=new_session("u2netp")
raw=remove(source,session=session,only_mask=True)
mask_image=raw if isinstance(raw,Image.Image) else Image.open(io.BytesIO(raw))
mask=np.asarray(mask_image.convert("L"))
if mask.shape!=(h,w): raise RuntimeError(f"Unexpected saliency output {mask.shape}")
grabcut=np.asarray(Image.open(o/"segmentation_mask.png").convert("L"))
# The U2Net output is intentionally not overwritten with GrabCut's mask.
rgba=np.dstack((src,mask))
Image.fromarray(rgba,"RGBA").save(o/"chick_u2netp_rgba_UNAPPROVED.png",optimize=True)
checker=np.empty_like(src);ys,xs=np.indices((h,w))
tile=((xs//20+ys//20)%2)==0
checker[tile]=[220,225,230];checker[~tile]=[175,184,192]
t=mask.astype(np.float32)[...,None]/255
preview=(src*t+checker*(1-t)).astype(np.uint8)
Image.fromarray(preview).save(o/"chick_u2netp_checker_QA.png",optimize=True)
foreground=(mask>128)
prior=(grabcut>128)
intersection=int((foreground&prior).sum())
union=int((foreground|prior).sum())
data={
 "model":"open-source rembg u2netp CPU saliency",
 "status":"UNAPPROVED reference/matte comparison, NOT a 3D model",
 "opaque_area_fraction":round(float(foreground.mean()),5),
 "agreement_iou_with_grabcut":round(intersection/union if union else 0,5),
 "source_crop_sha256":hsh(o/"chick_reference_uncut.png"),
 "outputs":{
  "chick_u2netp_rgba_UNAPPROVED.png":hsh(o/"chick_u2netp_rgba_UNAPPROVED.png"),
  "chick_u2netp_checker_QA.png":hsh(o/"chick_u2netp_checker_QA.png")
 },
 "caveat":"Compare hair edges, facial disc and talons before selecting matte; no single-image result proves 3D side/back anatomy."
}
(o/"rembg_comparison_qa.json").write_text(json.dumps(data,indent=2)+"\n")
print(json.dumps(data,indent=2))
