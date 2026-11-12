#!/usr/bin/env python3
"""Repack embedded GLB image bufferViews for a low-memory WebGL candidate.

Keep GLB mesh, UVs and material bindings; resize source textures to 512px
and flat placeholder textures to 32px. Opaque base colour -> JPEG; normals
and alpha -> PNG. This is NOT a mobile runtime or visual-quality approval.
"""
import io
import json
import struct
import sys
from pathlib import Path
from PIL import Image, ImageStat

def pad4(raw, fill=b'\0'):
    return raw + fill * ((-len(raw)) % 4)

def optimize(source, target, dimension=512):
    raw=Path(source).read_bytes()
    if len(raw)<20 or raw[:4]!=b'glTF':
        raise ValueError('not GLB')
    magic, version, declared=struct.unpack_from('<4sII',raw)
    if version!=2 or declared!=len(raw):
        raise ValueError('GLB header invalid')
    n,ctype=struct.unpack_from('<I4s',raw,12)
    if ctype!=b'JSON' or n%4:
        raise ValueError('GLB JSON malformed')
    doc=json.loads(raw[20:20+n])
    pos=20+n
    if pos+8>len(raw):
        raise ValueError('missing BIN header')
    bsize,btype=struct.unpack_from('<I4s',raw,pos)
    if btype!=b'BIN\0':
        raise ValueError('missing BIN chunk')
    old_bin=raw[pos+8:pos+8+bsize]
    if len(old_bin)!=bsize or len(doc['buffers'])!=1 or 'uri' in doc['buffers'][0]:
        raise ValueError('only self-contained one-buffer GLB supported')
    views=doc['bufferViews']
    image_view_to_payload={}
    stats=[]
    for im_no,im in enumerate(doc.get('images',[])):
        if 'bufferView' not in im:
            raise ValueError('external image not supported')
        v_idx=im['bufferView']
        if views[v_idx].get('buffer',0)!=0:
            raise ValueError('unexpected buffer')
        view=views[v_idx]
        payload=old_bin[view.get('byteOffset',0):view.get('byteOffset',0)+view['byteLength']]
        with Image.open(io.BytesIO(payload)) as input_image:
            pic=input_image.copy()
        rgb=pic.convert('RGB')
        reduced=rgb.resize((8,8),Image.Resampling.BOX)
        is_flat=len(payload)<50000 and max(ImageStat.Stat(reduced).stddev)<2.5
        size=32 if is_flat else dimension
        if max(pic.size)>size:
            pic.thumbnail((size,size),Image.Resampling.LANCZOS)
        has_alpha=('A' in pic.getbands()) and pic.getchannel('A').getextrema()[0]<255
        normal='normal' in im.get('name','').lower()
        fmt='PNG' if has_alpha or normal or is_flat else 'JPEG'
        out=io.BytesIO()
        if fmt=='JPEG':
            pic.convert('RGB').save(out,'JPEG',quality=83,optimize=True,subsampling=0)
            im['mimeType']='image/jpeg'
        else:
            pic.save(out,'PNG',optimize=True,compress_level=9)
            im['mimeType']='image/png'
        image_view_to_payload[v_idx]=out.getvalue()
        stats.append(dict(name=im.get('name',str(im_no)),before=len(payload),
                          after=len(out.getvalue()),width=pic.width,
                          height=pic.height,format=fmt))
    new_bin=bytearray()
    for idx,view in enumerate(views):
        start=view.get('byteOffset',0)
        data=image_view_to_payload.get(idx)
        if data is None:
            data=old_bin[start:start+view['byteLength']]
        if not data:
            raise ValueError('empty bufferView '+str(idx))
        new_bin.extend(b'\0'*((-len(new_bin))%4))
        view['byteOffset']=len(new_bin)
        view['byteLength']=len(data)
        new_bin.extend(data)
    new_bin=pad4(bytes(new_bin))
    doc['buffers'][0]['byteLength']=len(new_bin)
    js=pad4(json.dumps(doc,ensure_ascii=False,separators=(',',':')).encode(),b' ')
    data=(struct.pack('<4sII',b'glTF',2,12+8+len(js)+8+len(new_bin))
          +struct.pack('<I4s',len(js),b'JSON')+js
          +struct.pack('<I4s',len(new_bin),b'BIN\0')+new_bin)
    Path(target).write_bytes(data)
    return dict(source_bytes=len(raw),optimized_bytes=len(data),images=stats)

if __name__=='__main__':
    if len(sys.argv) not in (3,4):
        raise SystemExit('usage: optimize_glb_textures.py INPUT.glb OUTPUT.glb [maxdim]')
    print(json.dumps(optimize(sys.argv[1],sys.argv[2],
          int(sys.argv[3]) if len(sys.argv)==4 else 512),indent=2))
