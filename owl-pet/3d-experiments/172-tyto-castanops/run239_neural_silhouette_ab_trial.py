#!/usr/bin/env python3
"""Run239: non-rigid A/B mesoptile geometry study on REAL Run238 Hunyuan 3D owl.
Never publish these research-only GLBs; native glTF buffers remain genuine 3D.
"""
import argparse, hashlib, json, struct
from pathlib import Path
import numpy as np
import trimesh

PIN = "8a16b6b664fd6280372e85d4aba7429a659097363cd582269fc861cc825bdc7d"
def sha(b): return hashlib.sha256(b).hexdigest()

def access(doc, buf, idx):
    a=doc["accessors"][idx]; view=doc["bufferViews"][a["bufferView"]]
    assert a["componentType"] in (5121,5125,5126)
    dt={5121:np.uint8,5125:np.uint32,5126:np.float32}[a["componentType"]]
    n={"SCALAR":1,"VEC2":2,"VEC3":3,"VEC4":4}[a["type"]]
    assert view.get("byteStride",np.dtype(dt).itemsize*n)==np.dtype(dt).itemsize*n
    offset=view.get("byteOffset",0)+a.get("byteOffset",0)
    return np.ndarray((a["count"],n),dtype=dt,buffer=buf,offset=offset)

def morph(v,p):
    x,y,z=v[:,0],v[:,1],v[:,2]
    torso=np.exp(-((y+.10)/.64)**4)
    face_lock=np.clip((.59-z)/.49,0,1)
    foot_lock=np.clip((y+.72)/.34,0,1)
    moving=torso*face_lock*foot_lock
    rear=np.clip((-z+.06)/.77,0,1)**1.35
    delta=np.zeros_like(v)
    delta[:,2]+=p["rear_shift"]*rear*moving
    wing=np.clip((np.abs(x)-.38)/.32,0,1)*np.exp(-((y+.12)/.52)**4)
    delta[:,0]-=np.sign(x)*p["wing_tuck"]*wing*face_lock*foot_lock
    belly=np.exp(-((y+.32)/.45)**2)*np.clip((.48-z)/.40,0,1)*foot_lock
    delta[:,0]-=p["belly_narrow"]*x*belly
    slope=np.clip((.42-y)/1.05,0,1)*np.clip((y+.73)/.35,0,1)*face_lock
    delta[:,1]+=.055*p["squat"]*slope
    return v+delta

def set_normals(doc,buf,mesh_idx):
    primitive=doc["meshes"][mesh_idx]["primitives"][0]
    atr=primitive["attributes"]
    v=access(doc,buf,atr["POSITION"])
    triangles=access(doc,buf,primitive["indices"]).reshape(-1,3)
    f=v[triangles]; nface=np.cross(f[:,1]-f[:,0],f[:,2]-f[:,0])
    n=np.zeros_like(v)
    for j in range(3):np.add.at(n,triangles[:,j],nface)
    n/=np.maximum(np.linalg.norm(n,axis=1,keepdims=True),1e-10)
    access(doc,buf,atr["NORMAL"])[:]=n
    for attribute in ("POSITION","NORMAL"):
        idx=atr[attribute]; a=doc["accessors"][idx]; q=access(doc,buf,idx)
        a["min"]=q.min(axis=0).astype(float).tolist()
        a["max"]=q.max(axis=0).astype(float).tolist()

def run(src,outdir):
    raw=Path(src).read_bytes()
    assert raw[:4]==b"glTF" and sha(raw)==PIN
    assert struct.unpack_from("<II",raw,4)==(2,len(raw))
    jl,jtype=struct.unpack_from("<I4s",raw,12); assert jtype==b"JSON"
    original=json.loads(raw[20:20+jl])
    binlen,btype=struct.unpack_from("<I4s",raw,20+jl)
    assert btype==b"BIN\x00" and 28+jl+binlen==len(raw)
    sourcebin=raw[28+jl:]
    assert len(original["meshes"])==8
    outdir=Path(outdir);outdir.mkdir(parents=True,exist_ok=True)
    report={"run":"Run239","release":"NO_RELEASE","art_pass":False,
     "phone_webgl":"UNTESTED","cost_usd":0,
     "method":"real native learned neural owl mesh & fur buffer nonrigid retarget; no geometrical owl primitive or SVG",
     "source":{"bytes":len(raw),"sha256":sha(raw)},"variants":{}}
    variants={"A":{"rear_shift":.16,"wing_tuck":.06,"belly_narrow":.05,"squat":.65},
              "B":{"rear_shift":.28,"wing_tuck":.105,"belly_narrow":.085,"squat":1.}}
    for name,parameters in variants.items():
        doc=json.loads(json.dumps(original)); buffer=bytearray(sourcebin)
        shifts=[]
        for i in (0,1):
            idx=doc["meshes"][i]["primitives"][0]["attributes"]["POSITION"]
            p=access(doc,buffer,idx); before=p.copy()
            p[:]=morph(before,parameters)
            shifts.append(float(np.max(np.linalg.norm(before-p,axis=1))))
            set_normals(doc,buffer,i)
        # Preserve the original real mesh topology, alpha-down UV/color and all eye geometry.
        for i in range(8):
            prim=doc["meshes"][i]["primitives"][0]
            oldprim=original["meshes"][i]["primitives"][0]
            assert prim==oldprim
            for field in ["indices","COLOR_0","TEXCOORD_0"]:
                idx=prim["indices"] if field=="indices" else prim["attributes"].get(field)
                if idx is not None:
                    old=access(original,bytearray(sourcebin),idx).copy()
                    assert np.array_equal(access(doc,buffer,idx),old),(i,field)
            if i>=2:
                for field in ["POSITION","NORMAL"]:
                    idx=prim["attributes"][field]
                    assert np.array_equal(access(doc,buffer,idx),access(original,bytearray(sourcebin),idx))
        j=json.dumps(doc,separators=(",",":"),ensure_ascii=False).encode("utf8")
        j+=b" "*((-len(j))%4)
        glb=struct.pack("<4sII",b"glTF",2,12+8+len(j)+8+len(buffer))
        glb+=struct.pack("<I4s",len(j),b"JSON")+j+struct.pack("<I4s",len(buffer),b"BIN\x00")+buffer
        path=outdir/f"run239_variant{name}_true_neural_mesoptile_ART_REJECTED_NO_RELEASE.glb"
        path.write_bytes(glb)
        scene=trimesh.load(str(path),force="scene")
        assert len(scene.geometry)==8 and all(np.isfinite(g.vertices).all() for g in scene.geometry.values())
        faces=sum(len(g.faces) for g in scene.geometry.values())
        assert faces==86867
        report["variants"][name]={"parameters":parameters,"file":path.name,"bytes":len(glb),
          "sha256":sha(glb),"real_meshes":8,"real_triangles":faces,
          "max_true_core_xyz_shift":round(shifts[0],5),
          "max_true_3d_down_shift":round(shifts[1],5)}
    report["status"]="TWO_REIMPORTED_NATIVE_DIFFUSION_3D_AB_VARIANTS_NO_ART_APPROVAL_NO_RELEASE"
    (outdir/"run239_machine_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("--source",required=True);a.add_argument("--outdir",required=True)
    o=a.parse_args();run(o.source,o.outdir)
