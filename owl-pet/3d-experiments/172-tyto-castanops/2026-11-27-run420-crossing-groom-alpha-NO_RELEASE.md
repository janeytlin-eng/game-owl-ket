# Run420 — crossing down-card alpha compositing — ART_REJECTED / NO_RELEASE

2026-11-27. Re-read main owl-pet AGENTS, README, STATUS (207/251, unchanged). Fetched and actually viewed the 1536x1024 #172 v3 concept from main, blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b. Right juvenile has a compact, rounded cream/buff down-covered body, short feathered legs, warm dark outline of a heart-shaped facial disc, dark eyes, pale tapered bill. Do not mistake adjacent adult birds for juvenile references. Re-read Run419 in full (26f082687a67bf5da82a50e0e77a0c88a074d6a7): direct EGL can separate MASK and BLEND for a single artificial texture; browser contexts blocked. This run tests overlapping cards at different views instead of repeating single-card shader or rejected sculpt smoothing.

## Executed test
Python NumPy analytical orthographic ray/plane intersections, 24 crossing planar down-card fixtures in true 3D, 256x256, three azimuths. Varying depths per pixel, procedural feather barbs, deliberately varying colors to expose sorting errors (NOT target palette or animal). Compare exact per-pixel back-to-front source-over with arbitrary fixed and reverse order, plus weighted blended approximation with exact background transmittance and four exponential weight coefficients. This is a CPU numerical reference, not a GPU implementation, glTF asset or owl sample.

| angle | overlapping pixels | max layers | fixed MAE | reverse MAE | w0 | w2 | w4 | w8 | fixed vs reverse MAE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0|15009|7|8.151|4.497|5.616|3.292|4.121|6.828|10.406|
|40|11356|8|7.599|3.023|4.684|2.894|3.320|5.667|9.083|
|80|8801|5|4.625|2.971|3.504|2.427|3.962|6.467|6.679|

MAE is mean absolute RGB difference in 0–255 numerical units over pixels with at least two nonzero alpha fragments. Colors composited in numerical RGB, no sRGB conversion or physical light model. The k=2 approximation had smallest error among tested approximations at every view, but is not exact; larger weights worsen results. Actual 1792x768 rendered comparison PNG was viewed; fixed/reverse change overlapping feather colors, weighted cases visibly soften depth cues; synthetic feather stripes are not natural juvenile down. PNG remained local; full reproducible script below. No phone or GPU benchmark claimed. Potential implementation needs render-target/blend capability probes and mobile cost measurement; not a standard glTF feature. Do not introduce until a suitable sculpt exists.

Reference: McGuire & Bavoil 2013, Weighted Blended Order-Independent Transparency, https://www.jcgt.org/published/0002/02/09/paper.pdf ; abstract and method explanation accessed via https://www.academia.edu/69283111/Weighted_Blended_Order_Independent_Transparency . Our exponential coefficient is a fixture-specific heuristic, not the paper's recommended general-purpose weight.

## No-fee route checks
Actual local requests to github.com, huggingface.co and raw.githubusercontent.com failed DNS resolution. torch.cuda.is_available() False; Blender executable absent. No paid invocation. Public asset search returned previously screened Mint, Innerscene, Embossify; not new assets. Grab3D https://grab3d.com/models/animals/owl/ publisher describes a great horned owl with ear tufts, yellow eyes, adult barred plumage (up to 799999 triangles); wrong morphology, no download or new visual inspection claimed. WildMesh https://sketchfab.com/3d-models/realistic-animated-owl-3d-model-c48c6afb709c4e7dbedda8c88eef35a2 advertises 6.9k triangles and free animated model but no verified juvenile appearance or distribution terms; not accepted, not downloaded. No usable new base.

## Reproduction (Python, NumPy, Pillow)
```python
import numpy as np
from PIL import Image
import time,json
rng=np.random.default_rng(420)
N=256; K=24
centers=rng.uniform([-.55,-.45,-.35],[.55,.45,.35],(K,3))
angles=rng.uniform(-1.1,1.1,K)
widths=rng.uniform(.16,.30,K); heights=rng.uniform(.55,.9,K)
colors=rng.uniform([.62,.48,.32],[.98,.92,.79],(K,3))
Y,X=np.mgrid[0:N,0:N]/(N-1)*2-1
bg=np.array([.08,.10,.13]); result={}; images=[]
for theta in [0,40,80]:
 t=np.deg2rad(theta); right=np.array([np.cos(t),0,-np.sin(t)]); view=np.array([np.sin(t),0,np.cos(t)]); up=np.array([0,1,0]); orig=X[...,None]*right+Y[...,None]*up
 alpha=[];depth=[]
 for i in range(K):
  a=angles[i]; U=np.array([np.cos(a),0,np.sin(a)]); V=np.array([0,1,.20*np.sin(i)]); V/=np.linalg.norm(V); normal=np.cross(U,V); denom=normal@view
  if abs(denom)<1e-5: d=np.zeros_like(X); op=np.zeros_like(X)
  else:
   d=np.sum((centers[i]-orig)*normal,axis=-1)/denom; p=orig+d[...,None]*view-centers[i]; u=np.sum(p*U,axis=-1)/widths[i]; v=np.sum(p*V,axis=-1)/heights[i]+.5
   w=.76*np.maximum(np.sin(np.pi*np.clip(v,0,1)),0)**.7; edge=np.clip((w-np.abs(u))*16,0,1); barb=.22+.78*(.5+.5*np.cos((v-np.abs(u)*.13)*100))**2
   op=edge*barb*.75*((v>0)&(v<1))
  alpha.append(op);depth.append(d)
 A=np.array(alpha); D=np.array(depth); C=np.broadcast_to(colors[:,None,None,:],(K,N,N,3)); idx=np.argsort(D,axis=0)
 def over(order):
  out=np.broadcast_to(bg,(N,N,3)).copy()
  for j in range(K):
   ix=order[j]; a=np.take_along_axis(A,ix[None],axis=0)[0,...,None]; c=np.take_along_axis(C,ix[None,...,None],axis=0)[0];out=c*a+out*(1-a)
  return out
 ref=over(idx); fixed=over(np.broadcast_to(np.arange(K)[:,None,None],A.shape)); rev=over(np.broadcast_to(np.arange(K)[::-1,None,None],A.shape)); R=np.prod(1-A,axis=0)[...,None]; valid=np.sum(A>0,axis=0)>1
 def wblend(k):
  w=np.exp(np.clip(k*D,-8,8)); p=A*w; return np.sum(p[...,None]*C,axis=0)/np.maximum(np.sum(p,axis=0)[...,None],1e-12)*(1-R)+bg*R
 def err(img):return round(float(np.mean(np.abs(img[valid]-ref[valid]))*255),3)
 outs=[ref,fixed,rev]+[wblend(k) for k in [0,2,4,8]]
 result[str(theta)]={'overlap_pixels':int(valid.sum()),'max_layers':int(np.sum(A>0,axis=0).max()),'mae_8bit_overlap':dict(zip(['sorted','fixed','reverse','w0','w2','w4','w8'],map(err,outs))),'fixed_reverse_mae':round(float(np.mean(np.abs(fixed[valid]-rev[valid]))*255),3)}
 images.append(np.concatenate(outs,axis=1))
Image.fromarray(np.uint8(np.clip(np.concatenate(images,axis=0),0,1)*255)).save('run420.png')
print(json.dumps(result,indent=2))
```

Decision: ART_REJECTED / NO_RELEASE. No new accepted character sculpt or actual mobile WebGL acceptance. No additional cost. No changes to main, original concepts, production flow or deployment.
