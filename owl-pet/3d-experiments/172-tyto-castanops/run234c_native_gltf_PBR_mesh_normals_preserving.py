#!/usr/bin/env python3
"""Run234c: MODIFY actual 30412-triangle museum adult Tyto glTF image bytes in-place.
Preserve ORIGINAL normals/UV/indices/normal map/AO+roughness. NOT approved juvenile.
Only released as isolated, research evidence. No payment, no production change.
"""
import hashlib,io,struct,json,datetime
from pathlib import Path
import numpy as np,trimesh
from PIL import Image,ImageDraw
from skimage.color import rgb2lab,lab2rgb
P=Path(__file__).resolve().parent; OUT=P/"run234c-evidence";OUT.mkdir(exist_ok=True)
SRC=P/"run234-evidence/donor_uncompressed_adult.glb"
HASH="4865f48828adb93cef4f5ec07002adc1a61855a80adb286f781a227fca89430f"
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==HASH
b=SRC.read_bytes();mg,v,total=struct.unpack_from("<III",b,0)
assert (mg,v,total)==(0x46546c67,2,len(b))
jsz,jt=struct.unpack_from("<II",b,12);j=json.loads(b[20:20+jsz])
binlen,bt=struct.unpack_from("<II",b,20+jsz)
assert jt==0x4e4f534a and bt==0x004e4942
data=b[28+jsz:28+jsz+binlen]
assert len(data)==j["buffers"][0]["byteLength"]
assert len(j["images"])==3 and j["textures"][0]["source"]==2
assert "NORMAL" in j["meshes"][0]["primitives"][0]["attributes"]
assert j["materials"][0]["pbrMetallicRoughness"]["baseColorTexture"]["index"]==0
bv=j["bufferViews"][2];start=bv["byteOffset"];end=start+bv["byteLength"]
assert all(x["byteOffset"]+x["byteLength"]<=start for i,x in enumerate(j["bufferViews"]) if i!=2)
original=Image.open(io.BytesIO(data[start:end])).convert("RGB")
assert original.size==(2048,2048)
lab=rgb2lab(np.asarray(original,dtype=np.float32)/255)
lab[:,:,0]=np.clip(90+(lab[:,:,0]-lab[:,:,0].mean())*.25,67,99)
lab[:,:,1]=np.clip((lab[:,:,1]-lab[:,:,1].mean())*.14+1,-4,5)
lab[:,:,2]=np.clip((lab[:,:,2]-lab[:,:,2].mean())*.14+10,1,19)
cream=Image.fromarray(np.uint8(np.round(np.clip(lab2rgb(lab),0,1)*255)))
R={"run":"234c","date_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
"source":"Zenodo 21379215 original adult photogrammetry (not a nestling)",
"zero_additional_paid_usd":0,"art_gate":"ART_REJECTED","release":"NO_RELEASE",
"real_mobile_gpu_tested":False,"cases":{},
"original":{"bytes":len(b),"sha256":HASH,"images":3,"normals":True}}
for size in (2048,1024,512):
 image=cream if size==2048 else cream.resize((size,size),Image.Resampling.LANCZOS)
 buf=io.BytesIO();image.save(buf,"JPEG",quality=90,optimize=True,subsampling=0)
 jpg=buf.getvalue();packed=data[:start]+jpg+bytes((-len(jpg))%4)
 obj=json.loads(json.dumps(j))
 obj["bufferViews"][2]["byteLength"]=len(jpg);obj["buffers"][0]["byteLength"]=len(packed)
 obj["materials"][0]["pbrMetallicRoughness"]["roughnessFactor"]=.95
 obj["materials"][0]["pbrMetallicRoughness"]["metallicFactor"]=0
 jsonbytes=json.dumps(obj,separators=(",",":"),ensure_ascii=False).encode()
 jsonbytes+=b" "*((-len(jsonbytes))%4)
 chunks=struct.pack("<II",len(jsonbytes),0x4e4f534a)+jsonbytes+struct.pack("<II",len(packed),0x004e4942)+packed
 output=struct.pack("<III",0x46546c67,2,len(chunks)+12)+chunks
 p=OUT/f"run234c_NATIVE_mesh_preserved_{size}px_ADULT_ART_REJECTED.glb";p.write_bytes(output)
 loaded=trimesh.load(p,force="scene",process=False);m=next(iter(loaded.geometry.values()))
 assert len(m.faces)==30412 and np.isfinite(m.vertices).all()
 assert min(np.ptp(m.vertices,axis=0))>.1 and m.visual.material.baseColorTexture.size==(size,size)
 R["cases"][str(size)]={"glb_bytes":len(output),"sha256":hashlib.sha256(output).hexdigest(),
 "triangles":len(m.faces),"jpeg_bytes":len(jpg),"normal_attribute_retained":True,
 "other_original_PBR_textures_retained":True,"glTF_images":3}
# Reuse the previously verified VTK native seven-axis camera renderer.
ns={"__file__":str(P/"run234_real_CC0_donor_cream_texture_two_variants.py")}
source=(P/"run234_real_CC0_donor_cream_texture_two_variants.py").read_text()
exec(source.split("try:main()")[0],ns)
ns["OUT"]=OUT;render=ns["render"]
contact=Image.new("RGB",(7*235,2*255),(245,246,247));dr=ImageDraw.Draw(contact)
for row,size in enumerate((2048,512)):
 m=trimesh.load(OUT/f"run234c_NATIVE_mesh_preserved_{size}px_ADULT_ART_REJECTED.glb",force="scene",process=False)
 imgs,records=render(m,f"run234c_{size}px")
 assert len(records)==7 and len({x["sha256"] for x in records})==7
 R["cases"][str(size)]["seven_actual_3d_camera_views"]=records
 for col,(name,p) in enumerate(imgs):
  x=235*col;y=255*row
  dr.text((x+4,y+3),str(size)+"px "+name,fill=(28,29,30))
  contact.paste(Image.open(p).convert("RGB").resize((229,228)),(x+3,y+25))
sheet=OUT/"run234c_NORMALS_PRESERVED_14_REAL_3D_CAMERAS_ART_REJECTED.png";contact.save(sheet)
R["contact_sheet"]={"bytes":sheet.stat().st_size,"sha256":hashlib.sha256(sheet.read_bytes()).hexdigest()}
R["status"]="THREE_REAL_NATIVE_GLB_NORMALS_PRESERVED_TWO_SEVEN_VIEW_TESTS_ART_REJECTED_NO_RELEASE"
(OUT/"run234c_machine_report.json").write_text(json.dumps(R,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"status":R["status"],"bytes":{k:v["glb_bytes"] for k,v in R["cases"].items()}},ensure_ascii=False),flush=True)
