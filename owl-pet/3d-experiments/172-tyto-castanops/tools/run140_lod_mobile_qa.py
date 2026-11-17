#!/usr/bin/env python3
"""Run140: exact Run139 PBR GLB LOD/replay and Chromium WebGL QA. NO_RELEASE.
No public source GLB distribution, no fake physical mobile GPU. Source SHA locked.
"""
import sys, json, pathlib, hashlib, subprocess, threading, http.server, functools, time, os, traceback
R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run140-PBR-LOD-SIMULATED-MOBILE-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
ORIG=O/"run139_original_RESEARCH_ONLY.glb"
PIN="9a154c9e3aeebb34ebcd6f209760e1d9e21e2f544f2b690dae406d9c8bf878e8"
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def save(p,d):(O/p).write_text(json.dumps(d,ensure_ascii=False,indent=2,default=str)+"\n")
def verify():
    assert ORIG.is_file() and sha(ORIG)==PIN,"Wrong original model; never test substitute"
    assert ORIG.stat().st_size==9983448,"Unexpected byte length"

def lod():
    import bpy
    from mathutils import Vector
    verify()
    outputs={}
    for ratio,tag in ((0.25,"lod25"),(0.12,"lod12")):
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=str(ORIG))
        meshes=[ob for ob in bpy.context.scene.objects if ob.type=="MESH"]
        if len(meshes)!=1: raise RuntimeError("Expected genuine source mesh and only one for reproducibility")
        ob=meshes[0]
        full_tri=len(ob.data.polygons)
        bpy.ops.object.select_all(action="DESELECT")
        ob.select_set(True);bpy.context.view_layer.objects.active=ob
        mod=ob.modifiers.new("run140_quadric_lod","DECIMATE")
        mod.decimate_type="COLLAPSE";mod.ratio=ratio
        bpy.ops.object.modifier_apply(modifier=mod.name)
        tri=len(ob.data.polygons)
        out=O/("run140_"+tag+"_TEXTURED_RESEARCH_ONLY.glb")
        bpy.ops.export_scene.gltf(filepath=str(out),export_format="GLB",export_materials="EXPORT",export_texcoords=True,export_normals=True,export_image_format="AUTO")
        assert out.is_file() and out.stat().st_size>1024
        outputs[tag]=dict(source_triangles=full_tri,ratio_requested=ratio,actual_triangles=tri,bytes=out.stat().st_size,sha256=sha(out),blender=bpy.app.version_string)
        save("run140_blender_lod_report.json",outputs)
    print("REAL_LODS",json.dumps(outputs,indent=2))

HTML=r'''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Run140 #172 Actual Binary GLB Local QA - NO RELEASE</title>
<style>html,body{margin:0;padding:0;width:100%;height:100%;overflow:hidden;background:#bab7b1}canvas{width:100%;height:100%;display:block}#status{position:absolute;top:8px;left:8px;font:12px monospace;background:#fff9;padding:8px;max-width:80%;pointer-events:none}</style>
<canvas id="canvas"></canvas><div id="status">Research only. Not a released character.</div>
<script type="importmap">{"imports":{"three":"/node_modules/three/build/three.module.js","three/addons/":"/node_modules/three/examples/jsm/"}}</script>
<script type="module">
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
const params=new URLSearchParams(location.search), source=params.get('model')||'run139_original_RESEARCH_ONLY.glb';
window.__qa={ready:false,error:null,source:source,draws:0,frameTimes:[]};
try{
const canvas=document.getElementById('canvas');
const renderer=new THREE.WebGLRenderer({canvas:canvas,antialias:false,preserveDrawingBuffer:true,powerPreference:'low-power'});
const mobileWidth=Math.min(innerWidth,900);
renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.5));renderer.setSize(innerWidth,innerHeight);
renderer.setClearColor(0xc9c8c3,1);
renderer.outputColorSpace=THREE.SRGBColorSpace;
const scene=new THREE.Scene();
scene.background=new THREE.Color(0xc9c8c3);
scene.add(new THREE.AmbientLight(0xffffff,1.6));
const light=new THREE.DirectionalLight(0xffffff,2.0);light.position.set(-2,4,6);scene.add(light);
const second=new THREE.DirectionalLight(0xffffff,0.7);second.position.set(3,1,-4);scene.add(second);
const camera=new THREE.PerspectiveCamera(42,innerWidth/innerHeight,.001,100);
window.addEventListener('error',e=>window.__qa.error=String(e.message));
const gl=renderer.getContext(),isGL2=gl instanceof WebGL2RenderingContext;
window.__qa.webgl2=Boolean(isGL2);
window.__qa.renderer=gl.getParameter(gl.RENDERER);
window.__qa.vendor=gl.getParameter(gl.VENDOR);
const gltf=await new GLTFLoader().loadAsync(source);
const obj=gltf.scene;scene.add(obj);
const box=new THREE.Box3().setFromObject(obj);
const size=new THREE.Vector3();box.getSize(size);
const center=new THREE.Vector3();box.getCenter(center);
obj.position.sub(center);
const span=Math.max(size.x,size.y,size.z);
const viewSize=Math.max(span,0.1);
camera.position.set(0,viewSize*.20,viewSize*2.7);
camera.lookAt(0,0,0);
camera.near=viewSize*.01;camera.far=viewSize*30;camera.updateProjectionMatrix();
let materialSet=new Set(),mapSet=new Set(),meshes=0;
obj.traverse(o=>{
 if(o.isMesh){
    meshes+=1;
    const a=Array.isArray(o.material)?o.material:[o.material];
    a.filter(Boolean).forEach(m=>{materialSet.add(m.uuid);if(m.map)mapSet.add(m.map.uuid);});
 }
});
window.__qa.model={meshes:meshes,materials:materialSet.size,colorMaps:mapSet.size,
  animations:gltf.animations.length,bbox:size.toArray()};
let last=performance.now();
function frame(now){
 const delta=now-last;last=now;
 if(window.__qa.frameTimes.length<160)window.__qa.frameTimes.push(delta);
 obj.rotation.y=(params.get('back')==='1'?Math.PI:0);
 renderer.render(scene,camera);
 window.__qa.draws++;
 window.__qa.triangles=renderer.info.render.triangles;
 requestAnimationFrame(frame);
}
window.__qa.ready=true;
document.getElementById('status').innerText='Research-only real 3D · NO_RELEASE · '+source;
requestAnimationFrame(frame);
}catch(e){window.__qa.error=String(e&&e.stack||e);document.getElementById('status').innerText=window.__qa.error;}
</script>'''

def browser():
    from playwright.sync_api import sync_playwright
    verify()
    html=O/"run140_webgl_qa.html"
    html.write_text(HTML)
    cwd=pathlib.Path.cwd()
    rel=O.relative_to(cwd) if O.is_absolute() else O
    handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(cwd))
    server=http.server.ThreadingHTTPServer(("127.0.0.1",8765),handler)
    thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
    results=dict(source_sha256=PIN,source_bytes=ORIG.stat().st_size,QA_NOT_ART_APPROVAL=True,
      physical_mobile_tested=False,simulated_mobile_only=True,third_party_rights_unverified=True,variants=[])
    with sync_playwright() as p:
      browser=p.chromium.launch(headless=True,args=[
         "--enable-webgl","--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader",
         "--disable-web-security"])
      for variant in ("run139_original_RESEARCH_ONLY.glb","run140_lod25_TEXTURED_RESEARCH_ONLY.glb","run140_lod12_TEXTURED_RESEARCH_ONLY.glb"):
       if not (O/variant).is_file():continue
       for profile,kwargs in (("mobile390",dict(viewport={"width":390,"height":844},device_scale_factor=2,is_mobile=True,has_touch=True)),
          ("desktop1280",dict(viewport={"width":1280,"height":720},device_scale_factor=1))):
        ctx=browser.new_context(**kwargs)
        page=ctx.new_page();errs=[]
        page.on("pageerror",lambda e:errs.append(str(e)))
        suffix="&back=1" if profile=="mobile390" else ""
        url="http://127.0.0.1:8765/"+str(rel/"run140_webgl_qa.html")+"?model="+variant+suffix
        item=dict(variant=variant,profile=profile,source_hash=sha(O/variant))
        try:
          page.goto(url,wait_until="domcontentloaded",timeout=30000)
          page.wait_for_function("window.__qa && (window.__qa.ready || window.__qa.error)",timeout=60000)
          page.wait_for_timeout(4000)
          item.update(page.evaluate("window.__qa"))
          item["console_page_errors"]=errs
          item["screenshot"]="run140_"+variant.replace(".glb","")+"_"+profile+"_ACTUAL_WEBGL.png"
          page.screenshot(path=str(O/item["screenshot"]),timeout=25000)
          frame_times=item.pop("frameTimes",[])
          if frame_times:
            ft=sorted(frame_times)
            item["frame_ms_median_software"]=ft[len(ft)//2]
            item["frame_ms_p95_software"]=ft[int(len(ft)*.95)]
          item["passed_software_gl_render"]=bool(item.get("ready") and item.get("draws",0)>10 and
             item.get("triangles",0)>1000 and not item.get("error") and not errs)
        except Exception as e:
          item["script_or_browser_error"]=traceback.format_exc(limit=4)[-1700:]
          item["passed_software_gl_render"]=False
        finally:
          results["variants"].append(item)
          save("run140_actual_webgl_browser_qa.json",results)
          ctx.close()
      browser.close()
    server.shutdown()
    print("ACTUAL_SOFTWARE_WEBGL_QA",json.dumps(results,ensure_ascii=False)[:12000])

if __name__=="__main__":
    if sys.argv[-1]=="lod":lod()
    elif sys.argv[-1]=="browser":browser()
    else:raise SystemExit("usage: lod | browser")