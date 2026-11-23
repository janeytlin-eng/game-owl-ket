"""Run321 repeatable silhouette comparison against native untouched source.
Usage: python run321_silhouette_diagnostic.py /path/to/run321-evidence
IoU is NOT an art-quality score; this script never approves artwork.
"""
from pathlib import Path
import argparse,json
import numpy as np
from PIL import Image

def silhouette(im,bg,threshold=25):
    return np.max(np.abs(im.astype('float32')-bg.astype('float32')),axis=2)>threshold

def run(folder):
    rows=[]
    for view in ('front','right','rear_oblique','back'):
        base_image=np.array(Image.open(folder/f'run321-baseline-{view}.png').convert('RGB'))
        corners=np.concatenate((base_image[:80,:80].reshape(-1,3),
                                base_image[:80,-80:].reshape(-1,3)),axis=0)
        bg=np.median(corners,axis=0)
        b=silhouette(base_image,bg)
        for label in ('A','B'):
            im=np.array(Image.open(folder/f'run321-{label}-{view}.png').convert('RGB'))
            a=silhouette(im,bg)
            u=int(np.count_nonzero(a|b));i=int(np.count_nonzero(a&b))
            changed=int(np.count_nonzero(a^b))
            assert u>20000, 'Silhouette is unexpectedly small; verify camera and threshold'
            rows.append({'view':view,'variant':label,'silhouette_iou':round(i/u,6),
                         'outline_changed_pixels':changed,'union_pixels':u,
                         'outline_change_percent':round(100*changed/u,3)})
    (folder/'run321-silhouette-diagnostic.json').write_text(json.dumps({
        'method':'true native 3D raster, fixed background median, RGB deviation >25; descriptive only',
        'results':rows},indent=2))
    return rows

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('evidence_dir');args=ap.parse_args()
    print(json.dumps(run(Path(args.evidence_dir)),indent=2))
