# Run418 — native alpha renderer fidelity gate — ART_REJECTED / NO_RELEASE

2026-11-27. Re-read main owl-pet AGENTS, README, STATUS (207/251), original concept path (v3 PNG blob 5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b, base64 response incomplete; no new visual inspection claim), Run415 report and Run417 commit bf51b8b81dbfb4f7efa4e46ed0f3e09d3e4bf1a4. Reference remains the right juvenile, compact cream-white down, heart facial disc, dark eyes. No main or species workflow changes.

## New actual experiment: renderer qualification for textured down
Run417 proved geometry import, not material fidelity. Instead of polishing its deliberately coarse fixture or rejected base, generated three native GLBs with the exact same 120 curved feather cards, shared procedural RGBA barbed atlas (128x256, 138 distinct alpha levels), 960 vertices, 720 triangles, and OPAQUE/MASK/BLEND material variants. This is a material test coupon, NOT a character. Actual VTK 9.6.2 EGL import and six 360x360 renders (front and 60-degree views), all inspected as a combined JPEG. Foreground counted as max RGB difference from corner background >12.

| Mode | Bytes | SHA256 | 0° foreground | 60° foreground | depth peeling |
|---|---:|---|---:|---:|---|
| OPAQUE | 38784 | beca1cd38b9816431300608e1bf1ca080e5fc3dc87d48865c5015c5bb49fba0d | 42623 | 20329 | false |
| MASK (cutoff .4) | 38800 | 62c27c1f869de9e72cd58e1c183e89440ccf16f6c059a180271065166261e9e1 | 44755 | 21950 | true |
| BLEND | 38780 | e6212e77da3c52a09f5051bda2d81d85d3dd8008cb16194cd7526c5b4c59edca | 44755 | 21950 | true |

Actual pixel-array comparison: MASK and BLEND identical at both angles; OPAQUE differs from MASK at 32768 and 16209 pixels respectively. OPAQUE itself unexpectedly still shows transparent feather silhouettes. Visual: isolated grey-buff feather fronds rather than soft fluffy down; MASK and BLEND visually identical. This importer/renderer configuration cannot establish faithful glTF alpha-mode behavior; do not use it alone to approve textured groom. Not an actual browser/device test. No accepted character asset.

## Independent candidate and local route check
- https://grab3d.com/models/animals/owl/ — publisher describes adult great horned owl, ear tufts, yellow eyes, 800k triangles (light 400k), static. CC0 claimed; rejected on description, not downloaded.
- https://sketchfab.com/3d-models/barn-owltyto-alba-af3cdd38e029430d9c131370ebf1bb33 — publisher reports 760 triangles and CC BY. No juvenile claim, no inspected native geometry, not a qualified sculpt.
- https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt — clay sculpt, 236060 polygons, no AI license restriction; not downloaded, no new visual claim. Prior juvenile sculpt gate also rejected simplified shape.
- Local DNS api.github.com, raw.githubusercontent.com, huggingface.co each errno -3 again. No Blender/bpy, model cache, open3d or pytorch3d; VTK, torch, trimesh, skimage, playwright present. No paid service submitted.

## Reproduction
Save the following executed script as probe.py in an isolated directory, then run python probe.py with numpy, Pillow and VTK. Produces actual native material coupon GLBs, atlas, six PNGs and comparison.jpg, not an owl model. Source script SHA256 in runtime: 754fc08964cd927879c946b7683254de73b5f59a3052aa931b25638b42111641.

```python
import json, struct, base64, io, math, hashlib
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
import vtk
P=Path(__file__).parent
# Material coupon only: 120 curved feather cards; not owl geometry.
rng=np.random.default_rng(172)
v=[];uv=[];idx=[]
for k in range(120):
 x=rng.uniform(-.85,.85); z=rng.uniform(-.1,.1); y=rng.uniform(-.7,.45)
 tilt=rng.uniform(-.35,.35); w=rng.uniform(.045,.09); l=rng.uniform(.16,.32)
 n=len(v)
 for j in range(4):
  t=j/3; cx=x+tilt*t; cy=y+l*t; cz=z+.10*t*t
  for s in [-1,1]:
   v.append([cx+s*w,cy,cz]);uv.append([(s+1)/2,1-t])
 for j in range(3):
  a=n+2*j;idx.extend([a,a+1,a+2,a+1,a+3,a+2])
# Feather alpha atlas: tapered core and stochastic tapered barbs, no opaque card background.
W,H=128,256
im=Image.new('RGBA',(W,H),(250,236,211,0));d=ImageDraw.Draw(im)
for j in range(160):
 t=rng.uniform(.06,.97); yc=(1-t)*H; reach=math.sin(math.pi*t)**.65*rng.uniform(22,60)
 for sign in [-1,1]:
  col=(250,238,215,int(rng.integers(100,250)))
  d.line([(64,yc),(64+sign*reach,yc-rng.uniform(6,28))],fill=col,width=int(rng.integers(1,3)))
d.line([(64,245),(64,8)],fill=(247,232,207,245),width=2)
buf=io.BytesIO();im.save(buf,format='PNG');tex=buf.getvalue();im.save(P/'feather-atlas.png')
v=np.asarray(v,'<f4');uv=np.asarray(uv,'<f4');idx=np.asarray(idx,'<u2')
# Actual glTF with the same mesh/texture and three alpha modes.
for mode in ['OPAQUE','MASK','BLEND']:
 parts=[];views=[];offset=0
 for b,target in [(v.tobytes(),34962),(uv.tobytes(),34962),(idx.tobytes(),34963),(tex,None)]:
  view={'buffer':0,'byteOffset':offset,'byteLength':len(b)}
  if target:view['target']=target
  views.append(view); pad=b+b'\0'*((-len(b))%4);parts.append(pad);offset+=len(pad)
 binary=b''.join(parts)
 material={'doubleSided':True,'alphaMode':mode,'pbrMetallicRoughness':{'baseColorTexture':{'index':0},'metallicFactor':0,'roughnessFactor':1}}
 if mode=='MASK':material['alphaCutoff']=.4
 g={'asset':{'version':'2.0'},'scene':0,'scenes':[{'nodes':[0]}],'nodes':[{'mesh':0}],'meshes':[{'primitives':[{'attributes':{'POSITION':0,'TEXCOORD_0':1},'indices':2,'material':0}]}],'materials':[material],'textures':[{'source':0}],'images':[{'bufferView':3,'mimeType':'image/png'}],'buffers':[{'byteLength':len(binary)}],'bufferViews':views,'accessors':[{'bufferView':0,'componentType':5126,'count':len(v),'type':'VEC3','min':v.min(0).tolist(),'max':v.max(0).tolist()},{'bufferView':1,'componentType':5126,'count':len(uv),'type':'VEC2'},{'bufferView':2,'componentType':5123,'count':len(idx),'type':'SCALAR'}]}
 js=json.dumps(g,separators=(',',':')).encode();js+=b' '*((-len(js))%4)
 raw=struct.pack('<4sII',b'glTF',2,12+8+len(js)+8+len(binary))+struct.pack('<I4s',len(js),b'JSON')+js+struct.pack('<I4s',len(binary),b'BIN\0')+binary
 file=P/(mode+'.glb');file.write_bytes(raw)
 w=vtk.vtkEGLRenderWindow();w.SetOffScreenRendering(1);w.SetSize(360,360)
 r=vtk.vtkRenderer();w.AddRenderer(r)
 imp=vtk.vtkGLTFImporter();imp.SetFileName(str(file));imp.SetRenderWindow(w);imp.Update()
 r=w.GetRenderers().GetFirstRenderer();r.SetBackground(.10,.14,.18)
 r.UseDepthPeelingOn();r.SetMaximumNumberOfPeels(16);w.SetAlphaBitPlanes(1);w.SetMultiSamples(0)
 cam=r.GetActiveCamera();cam.ParallelProjectionOn();cam.SetParallelScale(1);cam.SetFocalPoint(0,0,0);cam.SetPosition(0,0,4);cam.SetViewUp(0,1,0);r.ResetCameraClippingRange()
 metrics=[]
 for angle in [0,60]:
  cam.SetPosition(4*math.sin(math.radians(angle)),0,4*math.cos(math.radians(angle)));r.ResetCameraClippingRange();w.Render()
  cap=vtk.vtkWindowToImageFilter();cap.SetInput(w);cap.Update();writer=vtk.vtkPNGWriter();writer.SetInputConnection(cap.GetOutputPort());writer.SetFileName(str(P/f'{mode}-{angle}.png'));writer.Write()
  a=np.asarray(Image.open(P/f'{mode}-{angle}.png').convert('RGB'));bg=a[0,0];n=int((np.abs(a.astype(int)-bg).max(2)>12).sum());metrics.append({'angle':angle,'foreground_pixels':n,'depth_peeling':bool(r.GetLastRenderingUsedDepthPeeling())})
 print(json.dumps({'mode':mode,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'vertices':len(v),'triangles':len(idx)//3,'views':metrics}))
 w.Finalize()
canvas=Image.new('RGB',(1080,750),(25,32,42));d=ImageDraw.Draw(canvas)
for i,mode in enumerate(['OPAQUE','MASK','BLEND']):
 d.text((i*360+8,7),mode,fill='white')
 for j,ang in enumerate([0,60]):canvas.paste(Image.open(P/f'{mode}-{ang}.png'),(i*360,25+j*360))
canvas.save(P/'comparison.jpg',quality=86)
```

Raw generated coupons and images exist in the run-local workspace; this archive preserves reproducible code and measured evidence rather than claiming remote binary archival. Decision: ART_REJECTED / NO_RELEASE. Further progress requires a new high-quality juvenile sculpt and a renderer that distinguishes alpha modes; no more polishing the rejected coarse mesh. Extra external cost zero; no main, original concept, 251 species workflow or deployment mutation.
