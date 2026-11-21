#!/usr/bin/env python3
"""Run265b test: remove accidental opaque rectangular BLACK BACKGROUND on #172 original, not owl.
No external segmentation model and no retouching of the owl body or eyes.
Original/pinned RGBA is kept separately for provenance. Research-only, never a release.
"""
from PIL import Image
from collections import deque
import numpy as np,hashlib,json,pathlib,sys
source=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8'
original=np.array(Image.open(source).convert('RGBA'))
h,w=original.shape[:2]; assert (w,h)==(512,512)
black=(original[:,:,:3].max(axis=2)<=35) & (original[:,:,3]>150)
# Flood fill only from one known rectangular BACKGROUND pixel, not dark irises.
sx,sy=410,150;assert black[sy,sx]
mask=np.zeros((h,w),dtype=bool); mask[sy,sx]=True
queue=deque([(sx,sy)])
while queue:
 x,y=queue.popleft()
 for yy in range(max(0,y-1),min(h,y+2)):
  for xx in range(max(0,x-1),min(w,x+2)):
   if black[yy,xx] and not mask[yy,xx]:
    mask[yy,xx]=True;queue.append((xx,yy))
assert 38000<np.count_nonzero(mask)<47000, np.count_nonzero(mask)
# Remove anti-aliased near-black border up to two pixels to prevent a black rectangular seam.
fringe=np.zeros((h,w),dtype=bool); seed=mask.copy()
for _ in range(2):
 neighbors=seed.copy()
 for dx,dy in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
  yy0=max(0,-dy);yy1=min(h,h-dy);xx0=max(0,-dx);xx1=min(w,w-dx)
  neighbors[yy0:yy1,xx0:xx1]|=seed[yy0+dy:yy1+dy,xx0+dx:xx1+dx]
 seed=neighbors
fringe=seed&~mask&(original[:,:,:3].max(axis=2)<=70)&(original[:,:,3]>60)
clean=original.copy()
clean[mask|fringe,3]=0
# Keep the original owl's opaque pixels, save full transparent source + gray composited model input.
path=out/'run265b_black_rectangle_MASKED_rgba.png'
Image.fromarray(clean,'RGBA').save(path)
bg=Image.new('RGBA',(w,h),(128,128,128,255))
bg.alpha_composite(Image.fromarray(clean,'RGBA'))
rgb=out/'run265b_reference_gray_rgb.png';bg.convert('RGB').save(rgb)
report={
 'source_original_sha256':hashlib.sha256(raw).hexdigest(),
 'removed_connected_black_background_pixels':int(mask.sum()),
 'removed_antialias_fringe_pixels':int(fringe.sum()),
 'source_original_alpha_nonzero':int(np.count_nonzero(original[:,:,3])),
 'cleaned_alpha_nonzero':int(np.count_nonzero(clean[:,:,3])),
 'cleanup':'bounded 8-connected near-black background flood fill from rectangle only; no owl geometry primitive',
 'model_input_sha256':hashlib.sha256(rgb.read_bytes()).hexdigest(),
 'model_input_rgb_path':str(rgb),'release':'NO_RELEASE'}
(out/'run265b_segmentation_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2),flush=True)
