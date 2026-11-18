#!/usr/bin/env python3
"""Run196: actual GLB skinning + animation in Three.js WebGL on headless Chromium, not a phone, no release."""
import argparse, hashlib, json, os, shutil, statistics, tempfile, threading, traceback
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright

EXPECTED_GLB="a22017221687458f37b76991719cb80243b5f04554ae57f07503139f988add3f"
EXPECTED_REFERENCE="5a52dfcb228a5048a66679d0d09c1b48e191d54cebbd9291bf99b18df03155d9"
ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
HTML=r"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<style>html,body{width:100%;height:100%;margin:0;overflow:hidden;background:#201d21;}
canvas{display:block;width:100vw;height:100vh;}
#notice{position:fixed;top:12px;left:12px;color:#fff;background:#201d21c9;padding:8px;font:11px sans-serif;max-width:80%;pointer-events:none}</style>
<script type="importmap">{"imports":{"three":"/node_modules/three/build/three.module.js","three/addons/":"/node_modules/three/examples/jsm/"}}</script>
</head><body><canvas id="canvas"></canvas><div id="notice">RUN196 TECHNICAL DONOR ONLY · ART REJECTED · NO RELEASE</div>
<script type="module">
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
window.OWL_GATE_STATE="initializing";
try {
 const renderer=new THREE.WebGLRenderer({canvas:document.getElementById("canvas"),antialias:true,powerPreference:"low-power",preserveDrawingBuffer:true});
 renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));
 renderer.setSize(window.innerWidth,window.innerHeight);
 renderer.outputColorSpace=THREE.SRGBColorSpace;
 const scene=new THREE.Scene();scene.background=new THREE.Color(0x33343a);
 scene.add(new THREE.HemisphereLight(0xffffff,0x6c6272,2.2));
 const key=new THREE.DirectionalLight(0xffefd9,2.7);key.position.set(2,4,6);scene.add(key);
 const fill=new THREE.DirectionalLight(0xacc1dd,1.7);fill.position.set(-5,1,-3);scene.add(fill);
 const loader=new GLTFLoader();
 const gltf=await loader.loadAsync("/source.glb");
 scene.add(gltf.scene);
 const box=new THREE.Box3().setFromObject(gltf.scene);
 const center=box.getCenter(new THREE.Vector3()),size=box.getSize(new THREE.Vector3());
 const radius=Math.max(size.x,size.y,size.z,0.1);
 const camera=new THREE.PerspectiveCamera(40,window.innerWidth/window.innerHeight,0.001,1000);
 const mixer=new THREE.AnimationMixer(gltf.scene);
 const clips=gltf.animations;
 const meshes=[],skinned=[];
 gltf.scene.traverse(o=>{if(o.isMesh)meshes.push(o);if(o.isSkinnedMesh)skinned.push(o);});
 function orbit(yaw=0,pitch=0.08) {
   const d=radius*2.75;
   camera.position.set(center.x+d*Math.sin(yaw)*Math.cos(pitch),center.y+d*Math.sin(pitch),center.z+d*Math.cos(yaw)*Math.cos(pitch));
   camera.lookAt(center);camera.updateProjectionMatrix();renderer.render(scene,camera);
 }
 function vertices(){
   const arr=[];
   for(const o of skinned.slice(0,3)){
     const pos=o.geometry.attributes.position;if(!pos)continue;
     for(const f of [0,0.03,0.11,0.28,0.48,0.65,0.84,0.99]){
       const i=Math.min(pos.count-1,Math.floor(pos.count*f));
       const v=new THREE.Vector3().fromBufferAttribute(pos,i);
       if(typeof o.applyBoneTransform==="function")o.applyBoneTransform(i,v);
       o.localToWorld(v);arr.push(v.toArray().map(n=>Math.round(n*100000)/100000));
     }
   }
   return arr;
 }
 function sample(clipName,phase=0.25,yaw=0){
   mixer.stopAllAction();
   const clip=clips.find(c=>c.name===clipName);
   if(!clip)throw new Error("clip not found: "+clipName);
   mixer.clipAction(clip).reset().play();
   mixer.setTime(Math.max(0,Math.min(0.999,phase))*clip.duration);
   gltf.scene.updateMatrixWorld(true);
   orbit(yaw);
   return {clip:clip.name,duration:clip.duration,tracks:clip.tracks.length,phase,vertices:vertices(),
       frame:{triangles:renderer.info.render.triangles,drawcalls:renderer.info.render.calls},
       memory:{geometries:renderer.info.memory.geometries,textures:renderer.info.memory.textures}};
 }
 function status(){
   const gl=renderer.getContext();
   const dbg=gl.getExtension("WEBGL_debug_renderer_info");
   return {ready:true,viewport:[window.innerWidth,window.innerHeight],
    dpr:renderer.getPixelRatio(),userAgent:navigator.userAgent,
    webglVersion:gl.getParameter(gl.VERSION),renderer:dbg?gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL):gl.getParameter(gl.RENDERER),
    clips:clips.map(c=>({name:c.name,duration:c.duration,tracks:c.tracks.length})),
    meshCount:meshes.length,skinnedMeshCount:skinned.length,
    boneCounts:skinned.map(s=>s.skeleton.bones.length),
    bbox:{center:center.toArray(),size:size.toArray()},gpu:renderer.info.memory,
    isMobileEmulation:("ontouchstart" in window)};
 }
 async function benchmark(n=32){
   let ts=[],last=0;
   for(let i=0;i<n;i++)await new Promise(resolve=>requestAnimationFrame(t=>{
     if(last)ts.push(t-last);last=t;mixer.update(1/60);renderer.render(scene,camera);resolve();
   }));
   return {frameIntervalMs:ts,frames:ts.length,rendererCalls:renderer.info.render.calls,
      warning:"Chromium SwiftShader software GPU and emulated viewport; NOT phone GPU performance"};
 }
 orbit();
 window.OwlGate={status,sample,orbit,benchmark};
 window.OWL_GATE_STATE="ready";
} catch(e) {window.OWL_GATE_ERROR=String(e&&e.stack||e);window.OWL_GATE_STATE="failed";console.error("RUN196_FATAL",e);}
</script></body></html>"""

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--modules",required=True)
    a=ap.parse_args()
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    result={"run":196,"status":"STARTED","actual_physical_phone":False,"source_run":195,
      "artist_accepted":False,"production_change":False,"no_release":True,"extra_payment_usd":0,
      "reference_sha256_expected":EXPECTED_REFERENCE,"donor_sha256_expected":EXPECTED_GLB}
    (out/"NO_RELEASE.flag").write_text("RUN196 ART_REJECTED_AS_TARGET / CHROMIUM_ONLY / NOT A PHONE / DO NOT SHIP\n")
    assert sha(a.input)==EXPECTED_GLB, "Incorrect donor GLB: stop before testing"
    ref=ROOT/"research-evidence-run114C-RGB-BOUNDED-NATIVE-ART_REJECTED"/"rightmost_mesoptile_input.png"
    assert ref.is_file() and sha(ref)==EXPECTED_REFERENCE, "Target design reference mismatch"
    assert (ROOT/"known_rejected_asset_sha256_registry.json").is_file()
    assert (ROOT/"2026-11-19-run195-real-free-cc0-rigged-owl-native-sevenview-ART_REJECTED-NO_RELEASE.md").is_file()
    result["preflight"]={"source_glb_bytes":Path(a.input).stat().st_size,
      "source_glb_sha256":sha(a.input),"target_reference_sha256":sha(ref)}
    with tempfile.TemporaryDirectory(prefix="owl196_") as temporary:
      site=Path(temporary)
      (site/"index.html").write_text(HTML)
      shutil.copy2(a.input,site/"source.glb")
      modules=Path(a.modules).resolve()
      assert (modules/"three"/"build"/"three.module.js").is_file(),"Pinned Three.js not installed"
      (site/"node_modules").symlink_to(modules,target_is_directory=True)
      class Handler(SimpleHTTPRequestHandler):
        def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(site),**kwargs)
        def log_message(self,*args): pass
      srv=ThreadingHTTPServer(("127.0.0.1",0),Handler)
      t=threading.Thread(target=srv.serve_forever,daemon=True);t.start()
      url="http://127.0.0.1:"+str(srv.server_port)+"/index.html"
      errors=[];console=[]
      try:
        with sync_playwright() as pw:
          browser=pw.chromium.launch(headless=True,args=[
            "--no-sandbox","--disable-dev-shm-usage","--use-gl=angle","--use-angle=swiftshader",
            "--enable-unsafe-swiftshader","--disable-web-security"])
          context=browser.new_context(viewport={"width":390,"height":844},device_scale_factor=2,
                is_mobile=True,has_touch=True,service_workers="block")
          page=context.new_page()
          page.on("pageerror",lambda e:errors.append(str(e)))
          page.on("console",lambda m:console.append(m.type+": "+m.text[:600]))
          page.goto(url,wait_until="domcontentloaded",timeout=45000)
          page.wait_for_function("window.OWL_GATE_STATE==='ready'||window.OWL_GATE_STATE==='failed'",timeout=75000)
          state=page.evaluate("window.OWL_GATE_STATE")
          if state!="ready":raise RuntimeError("Three.js GLTF failed: "+str(page.evaluate("window.OWL_GATE_ERROR")))
          stat=page.evaluate("window.OwlGate.status()")
          result["browser"]=stat
          names=[q["name"] for q in stat["clips"]]
          views={"front":0,"right":1.5707963,"back":3.1415926,"left":-1.5707963,"quarter":0.7853981}
          for label,yaw in views.items():
            if names:
              page.evaluate("([n,y])=>window.OwlGate.sample(n,0.2,y)",[names[0],yaw])
            else:
              page.evaluate("(y)=>window.OwlGate.orbit(y)",yaw)
            page.screenshot(path=str(out/("run196_TRUE_WEBGL_"+label+".png")),animations="disabled",timeout=20000)
          samples={}
          for name in ["idle","walk","fly","sleep","call","sit"]:
            if name not in names:continue
            snapshots=[]
            for phase in [0,0.25,0.5,0.75]:
              snapshots.append(page.evaluate("([n,p])=>window.OwlGate.sample(n,p,0.7853981)",[name,phase]))
            deltas=[]
            v0=snapshots[0]["vertices"]
            for x in snapshots[1:]:
              for p,q in zip(v0,x["vertices"]):
                if len(p)==3 and len(q)==3:
                  deltas.append(sum((p[i]-q[i])**2 for i in range(3))**.5)
            samples[name]={"duration":snapshots[0]["duration"],"tracks":snapshots[0]["tracks"],
              "sampled_vertices":len(v0),"max_vertex_motion_world_units":max(deltas or [0]),
              "mean_vertex_motion_world_units":statistics.mean(deltas) if deltas else 0,
              "per_phase_render_stats":[x["frame"] for x in snapshots]}
            page.screenshot(path=str(out/("run196_TRUE_WEBGL_POSE_"+name+".png")),animations="disabled",timeout=20000)
          result["animation_samples"]=samples
          result["benchmark"]=page.evaluate("window.OwlGate.benchmark(28)")
          result["glb_loaded_in_real_webgl"]=stat["meshCount"]>0 and bool(stat["webglVersion"])
          result["skinning_verified"]=(stat["skinnedMeshCount"]>0 and any(x["max_vertex_motion_world_units"]>0.00001 for x in samples.values()))
          result["status"]="CHROMIUM_WEBGL_RIG_MOTION_VERIFIED_DONOR_ART_REJECTED" if result["skinning_verified"] else "WEBGL_LOADED_BUT_SKIN_MOTION_UNPROVEN"
          result["not_phone_validation"]="Emulated 390x844 touch Chromium via SwiftShader CPU renderer, not Android/iOS real GPU"
          browser.close()
      except Exception:
        result["status"]="WEBGL_BROWSER_ERROR_OR_UNPROVEN"
        result["traceback"]=traceback.format_exc()
        raise
      finally:
        srv.shutdown()
        (out/"run196_browser_console.json").write_text(json.dumps({"errors":errors,"console":console},indent=2)+"\n")
        (out/"run196_result.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":result["status"],"skinning_verified":result.get("skinning_verified"),
      "browser_renderer":result.get("browser",{}).get("renderer"),"no_release":True}))

if __name__=="__main__": main()
