#!/usr/bin/env python3
"""Combine original owl-preserving GrabCut head with feet-cleaning u2netp lower silhouette.
The rembg-only mask incorrectly punches out both dark eyes: do NOT use it alone.
Output is still a reference matte, not a 3D model.
"""
from pathlib import Path
import argparse,hashlib,json
import numpy as np
from PIL import Image

p=argparse.ArgumentParser();p.add_argument("--output-dir",type=Path,required=True)
a=p.parse_args();o=a.output_dir
a0=np.asarray(Image.open(o/"chick_reference_rgba.png").convert("RGBA"))
a1=np.asarray(Image.open(o/"chick_u2netp_rgba_UNAPPROVED.png").convert("RGBA"))
if a0.shape!=a1.shape:raise RuntimeError("Mask source mismatch")
h,w=a0.shape[:2]
yy=np.arange(h,dtype=np.float32)[:,None]
# Only feet/ledge area borrows saliency: original face, eyes, and down contour stay intact.
t=np.clip((yy-399)/88,0,1)
t=t*t*(3-2*t)
alpha=np.clip(np.round(a0[:,:,3]*(1-t)+a1[:,:,3]*t),0,255).astype(np.uint8)
rgba=np.dstack((a0[:,:,:3],alpha))
Image.fromarray(rgba,"RGBA").save(o/"chick_hybrid_reference_rgba_UNAPPROVED.png",optimize=True)
y,x=np.indices((h,w))
chk=np.empty((h,w,3),dtype=np.uint8)
tile=(x//20+y//20)%2==0
chk[tile]=[220,225,230];chk[~tile]=[175,184,192]
af=alpha.astype(np.float32)[...,None]/255
preview=(a0[:,:,:3]*af+chk*(1-af)).astype(np.uint8)
Image.fromarray(preview,"RGB").save(o/"chick_hybrid_checker_QA.png",optimize=True)
def hash_file(f):return hashlib.sha256((o/f).read_bytes()).hexdigest()
# Report, do not assert face geometry correctness or pixel-perfect cutout.
# Check dark eyes remain opaque; approximate ellipse boxes for robust QA.
eye_boxes=[(192,118,253,197),(285,118,354,198)]
eye_means=[round(float(alpha[y0:y1,x0:x1].mean()),2) for x0,y0,x1,y1 in eye_boxes]
if min(eye_means)<180:raise RuntimeError(f"hybrid punched out an eye: {eye_means}")
stats={
 "status":"UNAPPROVED 2D single-chick reference, not 3D or a live mobile model",
 "source":"#172 v3 rightmost bird 1536x1024 repo original",
 "method":"GrabCut through y=399; smoothstep blend to u2netp by y=487 to remove bark near feet; both eyes retained",
 "opaque_coverage":round(float((alpha>127).mean()),5),
 "eye_box_alpha_means":eye_means,
 "inputs":{"grabcut":hash_file("chick_reference_rgba.png"),"u2netp":hash_file("chick_u2netp_rgba_UNAPPROVED.png")},
 "outputs":{"hybrid_rgba":hash_file("chick_hybrid_reference_rgba_UNAPPROVED.png"),"hybrid_QA":hash_file("chick_hybrid_checker_QA.png")},
 "limit":"Sides/back are not observed. Do not project frontal details onto unseen rear or treat photo as 3D."
}
(o/"hybrid_reference_qa.json").write_text(json.dumps(stats,indent=2)+"\n")
print(json.dumps(stats,indent=2))
