#!/usr/bin/env python3
"""Run250 fix: preserve REAL source neural vertex RGB after volumetric remeshing.
Do not substitute flat-color primitive material or discard COLOR_0 learned data.
"""
import json, struct
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree

CORE="real_neural_owl_juvenile_core"

def parts(blob):
    magic,ver,total=struct.unpack_from("<III",blob,0)
    assert (magic,ver,total)==(0x46546c67,2,len(blob))
    jl,jt=struct.unpack_from("<II",blob,12)
    assert jt==0x4e4f534a
    obj=json.loads(blob[20:20+jl])
    bo=20+jl
    bl,bt=struct.unpack_from("<II",blob,bo)
    assert bt==0x004e4942
    binary=blob[bo+8:bo+8+bl]
    return obj,binary

def attr(obj,binary,mesh_name,attribute):
    m=next(m for m in obj["meshes"] if m.get("name")==mesh_name)
    prim=m["primitives"][0]
    a=obj["accessors"][prim["attributes"][attribute]]
    bv=obj["bufferViews"][a["bufferView"]]
    off=bv.get("byteOffset",0)+a.get("byteOffset",0)
    count=a["count"]
    n={"VEC3":3,"VEC4":4}[a["type"]]
    typ={5121:np.uint8,5126:"<f4"}[a["componentType"]]
    return np.frombuffer(binary,dtype=typ,count=count*n,offset=off).reshape(count,n).copy()

def pin_neural_colors(source,outfile,old_vertices,new_vertices):
    src_obj,src_bin=parts(Path(source).read_bytes())
    src_colors=attr(src_obj,src_bin,CORE,"COLOR_0")
    assert src_colors.shape==(len(old_vertices),4) and src_colors.dtype==np.uint8
    dest_obj,dest_bin=parts(Path(outfile).read_bytes())
    positions=attr(dest_obj,dest_bin,CORE,"POSITION")
    assert positions.shape==(len(new_vertices),3)
    assert np.allclose(positions,new_vertices,atol=2e-6)
    nearest=cKDTree(old_vertices).query(new_vertices)[1]
    rgba=src_colors[nearest]
    raw=rgba.tobytes()
    offset=len(dest_bin)
    viewid=len(dest_obj["bufferViews"])
    accessorid=len(dest_obj["accessors"])
    dest_obj["bufferViews"].append({"buffer":0,"byteOffset":offset,"byteLength":len(raw)})
    dest_obj["accessors"].append({
        "componentType":5121,"normalized":True,"type":"VEC4",
        "count":len(rgba),"bufferView":viewid,"byteOffset":0,
        "min":rgba.min(axis=0).tolist(),"max":rgba.max(axis=0).tolist()
    })
    m=next(m for m in dest_obj["meshes"] if m.get("name")==CORE)
    m["primitives"][0]["attributes"]["COLOR_0"]=accessorid
    payload=dest_bin+raw
    dest_obj["buffers"][0]["byteLength"]=len(payload)
    encoded=json.dumps(dest_obj,separators=(",",":")).encode("utf-8")
    encoded+=b" "*((-len(encoded))%4)
    payload+=b"\0"*((-len(payload))%4)
    result=struct.pack("<III",0x46546c67,2,12+8+len(encoded)+8+len(payload))
    result+=struct.pack("<II",len(encoded),0x4e4f534a)+encoded
    result+=struct.pack("<II",len(payload),0x004e4942)+payload
    Path(outfile).write_bytes(result)
    reread_obj,reread_bin=parts(result)
    assert np.array_equal(attr(reread_obj,reread_bin,CORE,"COLOR_0"),rgba)
    return {"source_neural_colors_preserved":len(rgba),
            "color_min":rgba.min(axis=0).tolist(),
            "color_max":rgba.max(axis=0).tolist()}
