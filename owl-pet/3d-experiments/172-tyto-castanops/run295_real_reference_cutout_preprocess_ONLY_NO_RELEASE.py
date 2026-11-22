#!/usr/bin/env python3
"""#172 true-image 3D input prep ONLY; GrabCut isolates actual rightmost fluffy chick.
Not a GLB, never a 3D deliverable; do not infer anatomy from segmentation.
Input: unchanged repository-original 1536x1024 three-bird v3 plate.
Output: transparent original pixels, plus a white-background flattened guide for 3D inference.
"""
from pathlib import Path
from PIL import Image, ImageDraw
import cv2, numpy as np, hashlib, json
P=Path('owl-pet/design/concepts/172-tyto-castanops-v3.png')
O=Path('owl172-run295-evidence');O.mkdir(exist_ok=True)
if not P.exists():raise RuntimeError('Missing repository original v3 concept')
full=Image.open(P).convert('RGB')
w,h=full.size
if (w,h)!=(1536,1024):raise RuntimeError('Unexpected original dimensions; do not silently reuse fixed mask')
im=np.asarray(full.crop((w*2//3,0,w,h)))
H,W=im.shape[:2]
mask=np.full((H,W),cv2.GC_BGD,dtype=np.uint8)
# Probable silhouette traced once against ORIGINAL project reference, not an invented bird.
poly=np.array([(131,282),(214,281),(282,299),(326,338),(355,402),(354,466),
 (344,519),(362,571),(376,629),(375,699),(349,748),(359,778),(345,816),
 (291,833),(257,824),(222,822),(178,833),(137,839),(105,830),(65,835),
 (25,831),(4,780),(0,709),(7,650),(16,585),(31,521),(30,446),(45,365),(84,308)],np.int32)
cv2.fillPoly(mask,[poly],cv2.GC_PR_FGD)
cv2.ellipse(mask,(189,420),(75,93),0,0,360,cv2.GC_FGD,-1)
cv2.ellipse(mask,(179,614),(109,125),0,0,360,cv2.GC_FGD,-1)
cv2.ellipse(mask,(187,733),(82,37),0,0,360,cv2.GC_FGD,-1)
mask[:265,:]=cv2.GC_BGD;mask[850:,:]=cv2.GC_BGD
bg=np.zeros((1,65),np.float64);fg=np.zeros((1,65),np.float64)
cv2.grabCut(cv2.cvtColor(im,cv2.COLOR_RGB2BGR),mask,None,bg,fg,12,cv2.GC_INIT_WITH_MASK)
binary=np.isin(mask,[cv2.GC_FGD,cv2.GC_PR_FGD]).astype(np.uint8)*255
binary=cv2.morphologyEx(binary,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)))
alpha=cv2.GaussianBlur(binary,(0,0),1.2)
rgba=np.dstack((im,alpha));rgba[alpha==0,:3]=255
original=Image.fromarray(im,'RGB')
young=Image.fromarray(rgba,'RGBA').crop((0,265,392,845))
young.save(O/'young-REAL-PHOTO-PIXELS-transparent-input-NO_3D.png')
for bg_color,label in [((255,255,255,255),'white'),((205,212,222,255),'gray')]:
 layer=Image.new('RGBA',young.size,bg_color);layer.alpha_composite(young)
 if label=='white':
  layer.convert('RGB').save(O/'young-isolated-white-background-input-NO_3D.png')
 else:
  layer.convert('RGB').save(O/'young-isolated-review-ONLY.jpg',quality=95)
# Preserve context for exactly attributable comparison
original.save(O/'reference-rightmost-unaltered.png')
qa={'subject':'#172 Tyto castanops v3 original rightmost age-unknown mesoptile',
    'original_reference_source':str(P),'original_full_dims':list(full.size),
    'crop_source_dims':[W,H],'output_dims':list(young.size),
    'original_full_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
    'nontransparent_matte_pixels':int(np.count_nonzero(alpha)),
    'matte_soft_edge_pixels':int(np.count_nonzero((alpha>0)&(alpha<255))),
    'input_preprocessing':'GrabCut with human inspected subject seeds, preserves source RGB pixels',
    'quality_limitations':['retains a small patch of wood beneath the feet','one image only; unseen 3D side/back not solved',
    'model must generate and undergo true multi-angle QA','no mobile browser GLB proven'],
    'real_native_3d':False,'art_approved':False,'release_allowed':False}
(O/'run295_matte_QA.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2))
lines=[]
for p in sorted(O.iterdir()):
 if p.is_file() and p.name!='SHA256SUMS.txt':
  lines.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name)
(O/'SHA256SUMS.txt').write_text('\n'.join(lines)+'\n')
print(json.dumps(qa,ensure_ascii=False,indent=2))
