#!/usr/bin/env python3
"""Run240 native GLB featherlet/ocular PBR A/B research on real Hunyuan neural sculpt.
NO_RELEASE: retain the actual learned volume, no procedural primitive owl or 2D substitute.
"""
import argparse, hashlib, io, json, struct
from pathlib import Path
import numpy as np
import trimesh
from PIL import Image, ImageFilter
from run239_neural_silhouette_ab_trial import access

PIN="84348c034e39287fe9a7a9d4054c46951d7543f06f1a304d63a623057de9beee"
def sha(b): return hashlib.sha256(b).hexdigest()
def parse(b):
    assert b[:4]==b"glTF" and struct.unpack_from("<II",b,4)==(2,len(b))
    jl,jtype=struct.unpack_from("<I4s",b,12); assert jtype==b"JSON"
    doc=json.loads(b[20:20+jl]); bl,typ=struct.unpack_from("<I4s",b,20+jl)
    assert typ==b"BIN\x00" and 28+jl+bl==len(b)
    return doc,bytearray(b[28+jl:])
def atlas(v):
    rng=np.random.default_rng(20261120+(0 if v=="A" else 123))
    yy,xx=np.mgrid[0:512,0:512].astype(np.float32)
    u=(xx%128)/128; t=yy/511
    alpha=np.zeros((512,512),np.float32)
    for panel in range(4):
        band=(xx>=panel*128)&(xx<(panel+1)*128)
        for ray in range(7 if v=="A" else 9):
            origin=.29+(ray/9)*.43+rng.uniform(-.035,.035)
            curve=origin+rng.uniform(-.12,.12)*t+rng.uniform(-.035,.035)*np.sin((1.2+rng.random())*np.pi*t)
            thickness=rng.uniform(.016,.028) if v=="A" else rng.uniform(.010,.019)
            width=np.maximum(thickness*(1.05-.77*t),.002)
            strand=np.exp(-.5*((u-curve)/width)**2)*np.sin(np.pi*np.clip(t,0,1))**(.45 if v=="A" else .62)*(1-.23*t)
            alpha=np.maximum(alpha,np.where(band,strand,0))
        root=np.exp(-((t-.19)/.32)**2)*np.exp(-((u-.51)/.24)**2)
        alpha=np.maximum(alpha,np.where(band,root*(.22 if v=="A" else .13),0))
    alpha=np.clip(alpha*(.79 if v=="A" else .65),0,1)
    warm=1.5*np.sin(5*np.pi*t)+1.1*np.sin(29*u+8*t)
    a=np.zeros((512,512,4),np.uint8)
    for k,c in enumerate((242,229,212)):a[:,:,k]=np.uint8(np.clip(c+warm,0,255))
    a[:,:,3]=np.uint8(alpha*255)
    return Image.fromarray(a,"RGBA").filter(ImageFilter.GaussianBlur(.4))
def build(raw, variant, dest, outdir):
    old, original=parse(raw)
    doc=json.loads(json.dumps(old));buf=bytearray(original)
    assert len(doc["meshes"])==8 and len(doc["buffers"])==1
    fur=doc["meshes"][1]["primitives"][0];atr=fur["attributes"]
    uv=access(doc,buf,atr["TEXCOORD_0"])
    assert uv.dtype==np.float32 and uv.shape[1]==2 and len(uv)%5==0
    n=len(uv)//5;assert n>10000
    before=uv.copy()
    for k in range(n):
        uv[5*k:5*k+5,0]=(k%4+before[5*k:5*k+5,0])/4.
    assert np.all((uv>=0)&(uv<=1))
    mat=doc["materials"][fur["material"]]
    assert mat["alphaMode"]=="MASK"
    image_id=doc["textures"][mat["pbrMetallicRoughness"]["baseColorTexture"]["index"]]["source"]
    img=doc["images"][image_id];assert img["mimeType"]=="image/png" and "bufferView" in img
    image_view=doc["bufferViews"][img["bufferView"]]
    old_png=bytes(buf[image_view.get("byteOffset",0):image_view.get("byteOffset",0)+image_view["byteLength"]])
    Image.open(io.BytesIO(old_png)).verify()
    pic=atlas(variant); b=io.BytesIO();pic.save(b,format="PNG",optimize=True)
    png=b.getvalue(); assert png[:8]==b"\x89PNG\r\n\x1a\n"
    filename=f"run240_{variant}_fourcell_wispy_neural_down_atlas_RESEARCH_ONLY.png"
    pic.save(outdir/filename)
    buf+=b"\x00"*((-len(buf))%4)
    pos=len(buf);buf.extend(png);buf.extend(b"\x00"*((-len(buf))%4))
    img["bufferView"]=len(doc["bufferViews"])
    doc["bufferViews"].append({"buffer":0,"byteOffset":pos,"byteLength":len(png)})
    doc["buffers"][0]["byteLength"]=len(buf)
    mat["alphaMode"]="MASK";mat["alphaCutoff"]=.13 if variant=="A" else .10
    mat["doubleSided"]=True
    mat["pbrMetallicRoughness"]["metallicFactor"]=0
    mat["pbrMetallicRoughness"]["roughnessFactor"]=1
    rough={"iris":.23,"pupil":.16,"glint":.28}
    ids={}
    for key,value in rough.items():
        ids[key]=len(doc["materials"])
        doc["materials"].append({"name":"run240_nonmetallic_organic_"+key,
          "pbrMetallicRoughness":{"baseColorFactor":[1,1,1,1],"metallicFactor":0,"roughnessFactor":value},"doubleSided":True})
    for i in range(2,8):
        doc["meshes"][i]["primitives"][0]["material"]=ids[["iris","pupil","glint"][(i-2)%3]]
    j=json.dumps(doc,ensure_ascii=False,separators=(",",":")).encode()
    j+=b" "*((-len(j))%4)
    glb=struct.pack("<4sII",b"glTF",2,12+8+len(j)+8+len(buf))
    glb+=struct.pack("<I4s",len(j),b"JSON")+j+struct.pack("<I4s",len(buf),b"BIN\x00")+buf
    dest.write_bytes(glb)
    loaded=trimesh.load(str(dest),force="scene")
    faces=sum(len(m.faces) for m in loaded.geometry.values())
    assert len(loaded.geometry)==8 and faces==86867
    updated,after=parse(glb)
    for i in range(8):
        a=old["meshes"][i]["primitives"][0];b=updated["meshes"][i]["primitives"][0]
        assert np.array_equal(access(old,original,a["indices"]),access(updated,after,b["indices"]))
        for key in ("POSITION","NORMAL","COLOR_0"):
            if key in a["attributes"]:
                assert np.array_equal(access(old,original,a["attributes"][key]),access(updated,after,b["attributes"][key])),(i,key)
    return {"file":dest.name,"bytes":len(glb),"sha256":sha(glb),"triangle_count":faces,
      "real_surface_following_tufts":n,"original_alpha_png_bytes":len(old_png),
      "new_alpha_png_bytes":len(png),"four_distinct_wisp_cells":True,
      "ocular_roughness":rough,"alpha_cutoff":mat["alphaCutoff"],"no_neural_geometry_replacement":True}
def main():
    p=argparse.ArgumentParser();p.add_argument("--source",required=True);p.add_argument("--outdir",required=True)
    args=p.parse_args();out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    raw=Path(args.source).read_bytes();assert sha(raw)==PIN
    report={"run":"Run240","release":"NO_RELEASE","art_pass":False,"phone_webgl":"UNTESTED",
     "paid_usd":0,"source_sha256":sha(raw),
     "method":"actual neural GLB, 4-cell distinct fine down atlas and wet-eye nonmetal PBR; no owl geometry fabrication",
     "variants":{}}
    for v in ("A","B"):
        dest=out/f"run240_variant{v}_TRUE_NEURAL_3D_DOWN_EYE_PBR_ART_REJECTED_NO_RELEASE.glb"
        report["variants"][v]=build(raw,v,dest,out)
    report["status"]="NATIVE_GLBS_BUILT_PENDING_ACTUAL_BROWSER_ART_QA_NO_RELEASE"
    (out/"run240_machine_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":main()
