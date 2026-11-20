#!/usr/bin/env python3
"""Run242: nonrigid wing/tail attenuation + forked down on genuine Run241 Hunyuan owl GLB.
Research-only. These outputs are NOT an accepted pet, not a phone performance claim.
Use original learned continuous body; no SVG/2D impostor or primitive owl assembly.
"""
import argparse, hashlib, io, json, struct
from pathlib import Path

import numpy as np
import trimesh
from PIL import Image, ImageFilter
from run239_neural_silhouette_ab_trial import access, set_normals

PIN = "480b69f0ad296cc91ee6fac521d688cb60510065e9b16d005a629878473c1981"
def sha(b): return hashlib.sha256(b).hexdigest()
def parse(raw):
    assert raw[:4] == b"glTF" and struct.unpack_from("<II",raw,4)==(2,len(raw))
    n,t=struct.unpack_from("<I4s",raw,12)
    assert t==b"JSON"
    doc=json.loads(raw[20:20+n])
    bl,typ=struct.unpack_from("<I4s",raw,20+n)
    assert typ==b"BIN\\x00" and 28+n+bl==len(raw)
    return doc,bytearray(raw[28+n:])
def pack(doc,buf):
    doc["buffers"][0]["byteLength"]=len(buf)
    raw=json.dumps(doc,ensure_ascii=False,separators=(",",":")).encode("utf8")
    raw+=b" "*((-len(raw))%4)
    assert len(buf)%4==0
    return (struct.pack("<4sII",b"glTF",2,28+len(raw)+len(buf))
      +struct.pack("<I4s",len(raw),b"JSON")+raw
      +struct.pack("<I4s",len(buf),b"BIN\\x00")+buf)
def smoothstep(a,b,x):
    x=np.clip((x-a)/(b-a),0,1)
    return x*x*(3-2*x)

def resculpt(v,p):
    q=v.astype(np.float64).copy()
    x,y,z=(q[:,i].copy() for i in range(3))
    # The elevated developed heart, eyes and face stay fixed. Work only behind
    # the face and around the long adult-style wing + projected rear taper.
    side=smoothstep(.29,.67,np.abs(x))
    chest_lock=1-smoothstep(.11,.48,z)
    foot_lock=smoothstep(-.72,-.47,y)
    wing=side*chest_lock*foot_lock*np.exp(-((y+.075)/.41)**4)
    q[:,0]-=np.sign(x)*p["foldwing_inward"]*wing
    # Pull the long learned wing/root backwards silhouette forward into the
    # young body, keeping the face and low toes in their learned positions.
    rear=smoothstep(-.05,-.72,z) if False else (1-smoothstep(-.72,-.05,z))
    lower=np.exp(-((y+.26)/.49)**4)
    q[:,2]+=p["rear_retraction"]*rear*lower*foot_lock*chest_lock
    # Make a full soft juvenile rump instead of a rigid pointed wing end.
    rump=np.exp(-((y+.33)/.38)**4)*(1-smoothstep(-.61,.02,z))*foot_lock
    q[:,1]+=p["rump_lift"]*rump
    q[:,0]*=1+p["soft_body_breadth"]*np.exp(-((y+.33)/.4)**4)*(
        1-smoothstep(-.05,.45,z))*foot_lock*(1-side)
    assert np.isfinite(q).all()
    return q.astype(np.float32),{"wing_vertices":int(np.count_nonzero(wing>.15)),
       "rear_vertices":int(np.count_nonzero(rear*lower*foot_lock>.15)),
       "maximum_vertex_displacement":round(float(np.linalg.norm(q-v,axis=1).max()),6)}

def soften_local_crease(v,faces,strength):
    # Several strictly localized Laplace iterations on original continuous
    # learned wing surface, not a polygon replacement of the bird.
    x,y,z=v[:,0],v[:,1],v[:,2]
    w=smoothstep(.26,.57,np.abs(x))*np.exp(-((y+.09)/.43)**4)*(
      1-smoothstep(.10,.46,z))*smoothstep(-.71,-.48,y)
    before=v.copy()
    for _ in range(5):
        summ=np.zeros_like(v,dtype=np.float64)
        degree=np.zeros(len(v),dtype=np.int32)
        for a,b in ((0,1),(1,2),(2,0)):
            aa=faces[:,a];bb=faces[:,b]
            np.add.at(summ,aa,v[bb])
            np.add.at(summ,bb,v[aa])
            np.add.at(degree,aa,1);np.add.at(degree,bb,1)
        avg=summ/np.maximum(degree[:,None],1)
        v=(v+(avg-v)*(strength*w)[:,None]).astype(np.float32)
    return v,float(np.linalg.norm(v-before,axis=1).max())

def down_atlas():
    # Full-res feather card texture with airy branching filaments rather than
    # the previous repetitive seven straight hairlines. No fractional power of
    # floating point negatives; math boundaries are explicitly clamped.
    rng=np.random.default_rng(172242)
    h,w=512,512
    yy,xx=np.mgrid[0:h,0:w].astype(np.float32)
    t=yy/(h-1)
    envelope=np.maximum(np.sin(np.pi*np.clip(t,0,1)),0)**.65
    alpha=np.zeros((h,w),dtype=np.float32)
    base_u=(xx%128+.5)/128
    for panel in range(4):
        seed_center=.45+rng.uniform(-.075,.075)
        band=(xx>=panel*128)&(xx<(panel+1)*128)
        card=np.zeros_like(alpha)
        roots=12+(panel%3)*3
        for k in range(roots):
            root=seed_center+rng.uniform(-.16,.16)
            lean=rng.uniform(-.19,.19)
            curl=rng.uniform(-.075,.075)
            spine=root+lean*t+curl*np.sin((.85+panel*.1)*np.pi*t)
            width=(.016+rng.uniform(0,.014))*(1-.50*t)
            halo=np.exp(-.5*((base_u-spine)/np.maximum(width,.003))**2)
            strand=halo*envelope*(.55+.40*rng.random())*(1-.27*t)
            card=np.maximum(card,strand)
            # Subtle feather barb branches fork from the spine at staggered
            # y values. This reads more like disordered down, not stiff needles.
            for fork in range(2):
                t0=.25+.25*fork+rng.uniform(-.045,.045)
                end=t0+.26+rng.uniform(0,.08)
                progress=np.clip((t-t0)/(end-t0),0,1)
                d=(.055+rng.uniform(0,.035))*progress * (1 if ((k+fork)%2) else -1)
                center=spine+d
                feather=(np.exp(-.5*((base_u-center)/(.009+.008*(1-progress)))**2)
                       *np.maximum(1-np.abs((t-(t0+end)*.5)/((end-t0)*.52)),0))
                card=np.maximum(card,.45*feather)
        root_cloud=(np.exp(-((t-.18)/.27)**2)
                    *np.exp(-((base_u-seed_center)/.31)**2))*.32
        card=np.maximum(card,root_cloud)
        alpha=np.where(band,card,alpha)
    alpha=np.clip(alpha*.78,0,1)
    rgba=np.zeros((h,w,4),dtype=np.uint8)
    # Subtle irregular tonal variation remains cream; no hard white sticker.
    tone=(2.1*np.sin(2*np.pi*t+xx*.011)+1.7*np.sin(xx*.033+yy*.023))
    for i,base in enumerate([243,230,214]):
        rgba[:,:,i]=np.clip(base+tone+(i-1)*1.1,0,255).astype(np.uint8)
    rgba[:,:,3]=np.rint(alpha*255).astype(np.uint8)
    assert np.isfinite(alpha).all() and np.count_nonzero(rgba[:,:,3])>40000
    return Image.fromarray(rgba,"RGBA").filter(ImageFilter.GaussianBlur(.45))

def replace_fur_png(doc,buf,pic):
    fur=doc["meshes"][1]["primitives"][0]
    mat=doc["materials"][fur["material"]]
    assert mat["alphaMode"]=="MASK"
    tex=mat["pbrMetallicRoughness"]["baseColorTexture"]
    image=doc["images"][doc["textures"][tex["index"]]["source"]]
    assert image.get("mimeType")=="image/png" and "bufferView" in image
    data=io.BytesIO();pic.save(data,format="PNG",optimize=True)
    blob=data.getvalue()
    buf+=b"\\x00"*((-len(buf))%4)
    start=len(buf);buf.extend(blob)
    buf+=b"\\x00"*((-len(buf))%4)
    viewid=len(doc["bufferViews"])
    doc["bufferViews"].append({"buffer":0,"byteOffset":start,"byteLength":len(blob)})
    image["bufferView"]=viewid
    mat["alphaCutoff"]=.075
    mat["doubleSided"]=True
    mat["pbrMetallicRoughness"]["metallicFactor"]=0.0
    mat["pbrMetallicRoughness"]["roughnessFactor"]=1.0
    return len(blob)

def run(raw,variant,p,output,pic):
    doc,buf=parse(raw)
    orig,origbuf=parse(raw)
    assert len(doc["meshes"])==8
    changes={}
    for idx in (0,1):
        prim=doc["meshes"][idx]["primitives"][0]
        pos=access(doc,buf,prim["attributes"]["POSITION"])
        before=pos.copy()
        edited,detail=resculpt(before,p)
        pos[:]=edited
        if idx==0:
            triangles=access(doc,buf,prim["indices"]).reshape(-1,3)
            smoothed,shift=soften_local_crease(pos.copy(),triangles,p["surface_softening"])
            pos[:]=smoothed
            detail["local_surface_crease_smoothing_max"]=round(shift,6)
        changes[f"learned_mesh_{idx}"]=detail
        set_normals(doc,buf,idx)
    texture_bytes=replace_fur_png(doc,buf,pic)
    # These independent checks protect the native neurogeometry, all six
    # learned eye/catchlight meshes and the actual fur UV/colours.
    for i in range(8):
        a=orig["meshes"][i]["primitives"][0]
        b=doc["meshes"][i]["primitives"][0]
        assert np.array_equal(access(orig,origbuf,a["indices"]),access(doc,buf,b["indices"]))
        for prop in ("COLOR_0","TEXCOORD_0"):
            if prop in a["attributes"]:
                assert np.array_equal(access(orig,origbuf,a["attributes"][prop]),
                                      access(doc,buf,b["attributes"][prop]))
        if i>=2:
            for prop in ("POSITION","NORMAL"):
                assert np.array_equal(access(orig,origbuf,a["attributes"][prop]),
                                      access(doc,buf,b["attributes"][prop]))
    glb=pack(doc,buf)
    path=output/f"run242_variant{variant}_native_neural_juvenile_down_ART_UNAPPROVED_NO_RELEASE.glb"
    path.write_bytes(glb)
    scene=trimesh.load(path,force="scene")
    assert len(scene.geometry)==8
    triangles=sum(len(g.faces) for g in scene.geometry.values())
    assert triangles==86867
    assert all(np.isfinite(g.vertices).all() for g in scene.geometry.values())
    return {"file":path.name,"bytes":len(glb),"sha256":sha(glb),
      "actual_neural_source":True,"neural_meshes":8,
      "real_triangles":triangles,"surface_down_tufts":12217,
      "new_real_fur_png_bytes":texture_bytes,
      "native_eye_6_meshes_unchanged":True,"native_topology_and_UV_unchanged":True,
      "nonrigid_xyz_changes":changes,"parameters":p}

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--source",required=True);a.add_argument("--outdir",required=True)
    args=a.parse_args()
    raw=Path(args.source).read_bytes();assert sha(raw)==PIN
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    pic=down_atlas();pic.save(out/"run242_soft_organic_plumulaceous_fourcell_rgba.png")
    variants={
      "A":{"foldwing_inward":.15,"rear_retraction":.17,
           "rump_lift":.055,"soft_body_breadth":.08,"surface_softening":.26},
      "B":{"foldwing_inward":.25,"rear_retraction":.27,
           "rump_lift":.075,"soft_body_breadth":.12,"surface_softening":.39},
    }
    report={"run":"Run242","release":"NO_RELEASE","art_pass":False,
      "phone_webgl":"UNTESTED","cost_usd":0,"source_sha256":sha(raw),
      "method":"actual Hunyuan native continuous neural learned mesh wing/rump resculpt and forked organically soft second-down atlas, no geometric primitive owl",
      "variants":{}}
    for name,p in variants.items():report["variants"][name]=run(raw,name,p,out,pic)
    report["status"]="TRUE_NEURAL_AB_GLBS_CREATED_PENDING_REAL_WEBGL_ART_REVIEW_NO_RELEASE"
    (out/"run242_machine_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":main()
