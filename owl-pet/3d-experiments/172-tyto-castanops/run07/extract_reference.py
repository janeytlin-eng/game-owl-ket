#!/usr/bin/env python3
"""Isolated, unapproved #172 chick source image crop and GrabCut reference extraction.
No 3D model, rig, multi-view back geometry, or WebGL claim is produced here.
Run: python extract_reference.py --source <full_v3.png> --out <output_dir>
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import cv2
import numpy as np
from PIL import Image

EXPECTED_SIZE=(1536,1024)
BBOX=(956,268,1424,848)

def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def ellipse(im, point, axes, value):
    cv2.ellipse(im,point,axes,0,0,360,value,-1)

def process(src,out):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=True)
    with Image.open(src) as original:
        if original.size!=EXPECTED_SIZE:
            raise ValueError(f"Wrong original dimensions {original.size}; refusing to crop")
        rgb=np.asarray(original.convert("RGB"))
    x0,y0,x1,y1=BBOX
    crop=rgb[y0:y1,x0:x1].copy()
    h,w=crop.shape[:2]
    def local(x,y):return (int(x-x0),int(y-y0))
    probable=np.zeros((h,w),np.uint8)
    for x,y,ax,ay in [(1190,564,200,229),(1195,426,165,139),(1179,682,183,119),(1104,774,93,65),(1300,777,89,63)]:
        ellipse(probable,local(x,y),(ax,ay),255)
    seed=np.full((h,w),cv2.GC_BGD,np.uint8)
    seed[probable>0]=cv2.GC_PR_FGD
    for x,y,ax,ay in [(1188,584,133,179),(1189,427,117,100),(1117,770,55,24),(1283,768,47,24)]:
        ellipse(seed,local(x,y),(ax,ay),cv2.GC_FGD)
    seed[:9,:]=cv2.GC_BGD;seed[-9:,:]=cv2.GC_BGD
    seed[:,:8]=cv2.GC_BGD;seed[:,-8:]=cv2.GC_BGD
    bgr=cv2.cvtColor(crop,cv2.COLOR_RGB2BGR)
    bg=np.zeros((1,65),np.float64);fg=np.zeros((1,65),np.float64)
    cv2.grabCut(bgr,seed,None,bg,fg,7,cv2.GC_INIT_WITH_MASK)
    mask=np.where((seed==cv2.GC_FGD)|(seed==cv2.GC_PR_FGD),255,0).astype(np.uint8)
    n,lab,stats,_=cv2.connectedComponentsWithStats(mask,8)
    keep=np.zeros_like(mask)
    for i in range(1,n):
        if stats[i,cv2.CC_STAT_AREA]>240 and np.any((lab==i)&(seed==cv2.GC_FGD)):
            keep[lab==i]=255
    keep=cv2.morphologyEx(keep,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
    alpha=cv2.GaussianBlur(keep,(0,0),1.4)
    rgba=np.dstack((crop,alpha))
    Image.fromarray(rgba,"RGBA").save(out/"chick_reference_rgba.png",optimize=True)
    Image.fromarray(keep,"L").save(out/"segmentation_mask.png",optimize=True)
    Image.fromarray(crop,"RGB").save(out/"chick_reference_uncut.png",optimize=True)
    yy,xx=np.indices((h,w))
    checker=np.empty_like(crop)
    tile=((xx//20+yy//20)%2)==0
    checker[tile]=[220,225,230];checker[~tile]=[175,184,192]
    t=alpha.astype(np.float32)[...,None]/255
    preview=(crop*t+checker*(1-t)).astype(np.uint8)
    Image.fromarray(preview,"RGB").save(out/"chick_matte_checker_QA.png",optimize=True)
    dark=np.full_like(crop,[52,62,73])
    Image.fromarray((crop*t+dark*(1-t)).astype(np.uint8),"RGB").save(out/"chick_matte_dark_QA.png",optimize=True)
    occupancy=float((keep>0).mean())
    if not 0.25<occupancy<0.8:raise RuntimeError(f"Foreground occupancy {occupancy:.3f}: QA abort")
    meta={
      "source":"owl-pet/design/concepts/172-tyto-castanops-v3.png",
      "source_sha256":sha256_file(src),
      "original_size":list(EXPECTED_SIZE),
      "target":"rightmost cream AGE-UNKNOWN MESOPTILE; no adults",
      "crop_bbox_xyxy":list(BBOX),
      "crop_dimensions":[w,h],
      "foreground_occupancy":round(occupancy,5),
      "feather_edge_alpha_band_pixels":int(((alpha>0)&(alpha<255)).sum()),
      "rough_source_landmarks_crop_xy":{
        "left_eye":[1159-x0,422-y0],"right_eye":[1270-x0,426-y0],
        "beak_tip":[1201-x0,535-y0],
        "left_foot":[1115-x0,774-y0],"right_foot":[1281-x0,781-y0]},
      "limitations":"Automatic GrabCut matte requires visual acceptance; does not reconstruct side/back, age or feather chronology.",
      "status":"UNAPPROVED REFERENCE ONLY; NOT 3D; NOT MOBILE/WEBGL PASS",
      "outputs":{}
    }
    for p in sorted(out.glob("*.png")):
        meta["outputs"][p.name]={"bytes":p.stat().st_size,"sha256":sha256_file(p)}
    (out/"reference_qa.json").write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps(meta,indent=2,ensure_ascii=False))
    return meta

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    process(args.source,args.out)
