#!/usr/bin/env python3
"""Run197 independent true WebGL LOD ablation of rejected CC0 animation donor. Never ship."""
import argparse, importlib.util, json, os, sys, traceback
from pathlib import Path

ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
BASE=ROOT/"tools"/"run196_real_threejs_mobile_emulation_skinning.py"
PREF="gltf.scene.traverse(o=>{if(o.isMesh)meshes.push(o);if(o.isSkinnedMesh)skinned.push(o);});"
SKIN="for(const o of skinned.slice(0,3)){"
FLAGS={
"low":"const selected=candidates.slice().sort((a,b)=>a.tris-b.tris)[0];",
"high":"const selected=candidates.slice().sort((a,b)=>b.tris-a.tris)[0];"}
def call_one(lod,src,modules,out):
    spec=importlib.util.spec_from_file_location("run196_lod_"+lod,BASE)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    assert mod.HTML.count(PREF)==1
    js=(
       'const candidates=skinned.map(o=>({o:o,tris:o.geometry.index?o.geometry.index.count/3:o.geometry.attributes.position.count/3}));'
       +FLAGS[lod]+
       'if(candidates.length!==2)throw new Error("Expected exactly 2 skinned donor LOD meshes");'
       'for(const c of candidates){c.o.visible=c.o===selected.o;}'
       'window.OWL_LOD_CHOICE={mode:"'+lod+'",visibleTriangles:selected.tris,allTriangles:candidates.reduce((n,c)=>n+c.tris,0),'
       'sourceMeshNames:candidates.map(c=>c.o.name),selectedMeshName:selected.o.name,drawnMeshes:1};'
    )
    mod.HTML=mod.HTML.replace(PREF,PREF+"\n "+js)
    assert mod.HTML.count(SKIN)==1
    mod.HTML=mod.HTML.replace(SKIN,"for(const o of skinned.filter(o=>o.visible).slice(0,3)){")
    mod.HTML=mod.HTML.replace("skinnedMeshCount:skinned.length,","skinnedMeshCount:skinned.length, visibleSkinnedMeshCount:skinned.filter(o=>o.visible).length, lodChoice:window.OWL_LOD_CHOICE,")
    mod.HTML=mod.HTML.replace("RUN196 TECHNICAL DONOR","RUN197 "+lod.upper()+" LOD TECHNICAL DONOR")
    out.mkdir(parents=True,exist_ok=True)
    prior_argv=sys.argv
    try:
        sys.argv=[str(BASE),"--input",str(src),"--modules",str(modules),"--out",str(out)]
        mod.main()
    finally:sys.argv=prior_argv
    p=out/"run196_result.json"
    result=json.loads(p.read_text())
    result["run"]=197
    result["variant"]=lod
    result["baseline_run"]=196
    result["does_not_modify_glb_or_prove_phone_performance"]=True
    p.rename(out/"run197_result.json")
    (out/"run197_result.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
    for old in sorted(out.glob("run196_TRUE_WEBGL_*.png")):
        old.rename(old.with_name(old.name.replace("run196_","run197_")))
    (out/"NO_RELEASE.flag").write_text("RUN197 "+lod+" LOD; TECHNICAL DONOR ONLY; ART REJECTED; PHONE GPU UNTESTED; NO RELEASE\n")
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True)
    ap.add_argument("--modules",required=True)
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    summary={"run":197,"source_run":195,"baseline_run":196,"art_rejected":True,
             "no_release":True,"extra_payment_usd":0,"real_phone_test":False}
    try:
        for lod in ("low","high"):
            result=call_one(lod,args.input,args.modules,dest/lod)
            summary[lod]={"status":result["status"],"lod":result["browser"]["lodChoice"],
               "drawcalls":result["animation_samples"]["idle"]["per_phase_render_stats"][0]["drawcalls"],
               "triangles":result["animation_samples"]["idle"]["per_phase_render_stats"][0]["triangles"],
               "skinned_motion":result["skinning_verified"],
               "webgl":result["browser"]["webglVersion"],
               "renderer":result["browser"]["renderer"],
               "screenshot_count":len(list((dest/lod).glob("run197_TRUE_WEBGL_*.png")))}
        previous=ROOT/"research-evidence-run196-REAL-WEBGL-RIG-ART_REJECTED-NO_RELEASE"/"run196_result.json"
        if previous.is_file():
            b=json.loads(previous.read_text())
            bs=b["animation_samples"]["idle"]["per_phase_render_stats"][0]
            summary["run196_baseline"]={"drawcalls":bs["drawcalls"],"triangles":bs["triangles"]}
        summary["all_tests_pass"]=(summary["low"]["skinned_motion"] and summary["high"]["skinned_motion"]
             and summary["low"]["drawcalls"]==1 and summary["high"]["drawcalls"]==1
             and summary["low"]["triangles"]<summary["high"]["triangles"])
        summary["status"]="NATIVE_WEBGL_LOD_SWITCH_VERIFIED_STILL_ART_REJECTED" if summary["all_tests_pass"] else "LOD_ABLATION_PARTIAL_OR_FAILED"
        summary["limitation"]="Only the visible Three.js skinned mesh was switched; GLB still stores both LOD meshes and has NOT been size-optimized; SwiftShader is not real phone hardware"
    except Exception:
        summary["status"]="RUN197_FAILED_OR_PARTIAL_NO_RELEASE"
        summary["traceback"]=traceback.format_exc()
        raise
    finally:
        (dest/"NO_RELEASE.flag").write_text("Technical-only animation donor; still wrong species/age/face/feathers/feet; no app release\n")
        (dest/"run197_summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n")
        print(json.dumps({"status":summary["status"],"low":summary.get("low"),"high":summary.get("high"),"NO_RELEASE":True}))
if __name__=="__main__": main()
