#!/usr/bin/env python3
"""Run91 visible-foreground material check: WebGL no-error is NOT enough.
Reads actual captured RGB screenshots from the real GLB, not placeholder metadata.
Returns diagnostic result in JSON; never signs off art or physical-phone quality.
"""
from PIL import Image
from pathlib import Path
import json,sys,numpy as np
folder=Path(sys.argv[1])
results={'tool':'Pillow screenshot-centre material luminance, not ART or phone QA',
         'bright_target_required':'rightmost cream downy chick, not black',
         'physical_mobile_tested':False,'cases':[]}
for file in sorted(folder.glob('*/*.png')):
    im=np.array(Image.open(file).convert('RGB'),dtype=np.float32)
    h,w=im.shape[:2]
    # Foreground should fill much of the central view under the existing framing QA.
    roi=im[int(h*.24):int(h*.76),int(w*.24):int(w*.76)]
    luma=.2126*roi[:,:,0]+.7152*roi[:,:,1]+.0722*roi[:,:,2]
    # Background Three.js #25303b; ensure samples aren't mistaken for model.
    dist=np.sqrt(((roi-[37,48,59])**2).sum(axis=-1))
    nonbg=dist>36
    bright=(luma>118)&nonbg
    # A grayscale dark owl is not falsely "valid" just because a mesh loaded.
    r={'file':str(file),'size':[w,h],
       'roi_luminance_median':float(np.median(luma)),
       'roi_luminance_p95':float(np.percentile(luma,95)),
       'roi_nonbg_fraction':float(nonbg.mean()),
       'roi_bright_fraction':float(bright.mean()),
       'roi_nonbg_median_luma':float(np.median(luma[nonbg])) if nonbg.any() else None,
       'material_readable':bool(bright.mean()>=.055 and
                               np.percentile(luma,95)>145),
       'note':'rough automatic visibility metric; human view still mandatory'}
    results['cases'].append(r)
results['evaluated_screenshots']=len(results['cases'])
results['all_readable']=bool(results['cases']) and all(c['material_readable'] for c in results['cases'])
(folder.parent/'pixel_material_gate.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
