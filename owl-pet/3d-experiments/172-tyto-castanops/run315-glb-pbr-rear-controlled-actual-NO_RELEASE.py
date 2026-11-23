#!/usr/bin/env python3
"""Run315: technically isolate the Run314 rear-black WebGL artifact.
Research-only PBR controls. No change to #172 art or 251-species production.
Requires exact rebuilt Run314 A native GLB; does not create/release a new owl.
"""
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, struct, threading, time
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import numpy as np
from PIL import Image
import trimesh
from playwright.sync_api import sync_playwright

INPUT = pathlib.Path("research/A/run314_curved_down_6500_RESEARCH_ONLY_NO_RELEASE.glb")
OUT = pathlib.Path(os.getenv("OWL315_OUT", "/tmp/owl172_run315"))
OUT.mkdir(parents=True, exist_ok=True)
VARIANTS = ("baseline", "matte", "unlit")
BG = (36, 39, 45)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def parse_glb(binary):
    assert binary[:4] == b"glTF" and struct.unpack_from("<I", binary, 4)[0] == 2
    version, total = struct.unpack_from("<II", binary, 4)
    assert total == len(binary), (total, len(binary))
    off, parts = 12, []
    while off < len(binary):
        length, kind = struct.unpack_from("<II", binary, off)
        off += 8
        parts.append((kind, binary[off:off+length]))
        off += length
    assert off == len(binary) and parts[0][0] == 0x4E4F534A
    data = json.loads(parts[0][1])
    return data, parts[1:]

def put_glb(data, tail):
    raw = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode()
    raw += b" " * ((-len(raw)) % 4)
    chunks = [(0x4E4F534A, raw)] + tail
    body = b"".join(struct.pack("<II", len(b), typ)+b for typ,b in chunks)
    return b"glTF"+struct.pack("<II", 2, 12+len(body))+body

def patch(data, variant):
    import copy
    d = copy.deepcopy(data)
    d.setdefault("materials", [])
    missing = 0
    default = None
    for mesh in d.get("meshes", []):
        for p in mesh.get("primitives", []):
            if "material" not in p:
                if default is None:
                    default=len(d["materials"])
                    d["materials"].append({"name":"Run315 COLOR_0 matte fallback",
                       "pbrMetallicRoughness":{"baseColorFactor":[1,1,1,1],
                       "metallicFactor":0.0,"roughnessFactor":0.96}})
                p["material"] = default
                missing += 1
    if variant == "baseline":
        return data, 0
    for m in d["materials"]:
        p=m.setdefault("pbrMetallicRoughness", {})
        p["metallicFactor"] = 0.0
        p["roughnessFactor"] = 0.97
        m["doubleSided"] = True
        if variant == "unlit":
            m.setdefault("extensions", {})["KHR_materials_unlit"] = {}
    if variant == "unlit":
        d["extensionsUsed"] = sorted(set(d.get("extensionsUsed", [])) | {"KHR_materials_unlit"})
    return d, missing

HTML = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<script type="importmap">{"imports":{"three":"/node_modules/three/build/three.module.js",
"three/addons/":"/node_modules/three/examples/jsm/"}}</script></head>
<body style="margin:0;background:#24272d;overflow:hidden">
<script type="module">
import * as THREE from "three";
import {GLTFLoader} from "three/addons/loaders/GLTFLoader.js";
window.GATE={state:"START",webgl2:false,meshes:0,triangles:0,materials:[],noRelease:true};
let r,scene,camera,object,dist;
try {
r=new THREE.WebGLRenderer({antialias:true,powerPreference:"low-power"});
r.setSize(innerWidth,innerHeight);r.setPixelRatio(1);
r.setClearColor(0x24272d);
r.outputColorSpace=THREE.SRGBColorSpace;
r.toneMapping=THREE.ACESFilmicToneMapping;
r.toneMappingExposure=1.1;document.body.appendChild(r.domElement);
window.GATE.webgl2 = r.getContext() instanceof WebGL2RenderingContext;
scene=new THREE.Scene();
scene.add(new THREE.AmbientLight(0xffffff,1.65));
const key=new THREE.DirectionalLight(0xfff5e8,2.1);key.position.set(4,5,7);scene.add(key);
const back=new THREE.DirectionalLight(0xe7ecff,2.1);back.position.set(-2,3,-6);
scene.add(back);back.visible=false;
camera=new THREE.PerspectiveCamera(37,innerWidth/innerHeight,.01,250);
camera.up.set(0,1,0);
window.setAngle = (az, rear=false) => {
 back.visible=rear;
 const a=az*Math.PI/180;
 camera.position.set(Math.sin(a)*dist,dist*.20,Math.cos(a)*dist);
 camera.lookAt(0,0,0);
 r.render(scene,camera);
 return {angle:az,rearLight:rear,trianglesRendered:r.info.render.triangles,calls:r.info.render.calls};
};
const variant=new URLSearchParams(location.search).get("variant") || "baseline";
new GLTFLoader().load("/models/"+variant+".glb",g=>{
 object=g.scene;
 const bbox=new THREE.Box3().setFromObject(object);
 const s=bbox.getSize(new THREE.Vector3()),center=bbox.getCenter(new THREE.Vector3());
 object.position.sub(center);scene.add(object);
 dist=Math.max(s.x,s.y,s.z)*2.25;
 object.traverse(x=>{
  if(!x.isMesh)return;
  window.GATE.meshes++;
  window.GATE.triangles+=(x.geometry.index?x.geometry.index.count:x.geometry.attributes.position.count)/3;
  for(const m of (Array.isArray(x.material)?x.material:[x.material])){
   window.GATE.materials.push({type:m.type,color:m.color?.getHexString(),metalness:m.metalness??null,
    doubleSided:m.side===THREE.DoubleSide,transparent:m.transparent,alphaTest:m.alphaTest});
  }
 });
 window.setAngle(0);
 window.GATE.state="LOADED";
},undefined,e=>{window.GATE.state="FAILED";window.GATE.error=String(e)});
} catch(e) {window.GATE.state="SETUP_FAILED";window.GATE.error=String(e);}
</script></body></html>"""

def produce():
    data = INPUT.read_bytes()
    scene = trimesh.load(INPUT, force="scene", process=False)
    base, tail = parse_glb(data)
    (OUT/"models").mkdir(exist_ok=True)
    metrics = {"run":315,"input_sha256":digest(data),"input_bytes":len(data),
               "real_input_geometry":len(scene.geometry),
               "real_input_triangles":sum(len(g.faces) for g in scene.geometry.values()),
               "original_material_count":len(base.get("materials", [])),
               "original_unassigned_primitives":sum("material" not in p for m in base["meshes"] for p in m["primitives"]),
               "research_only":True,"release":False,"art_approved":False,
               "source_owl":"run314 A / previously art rejected"}
    for variant in VARIANTS:
        modified, missing = patch(base, variant)
        built = data if variant == "baseline" else put_glb(modified,tail)
        q=OUT/"models"/(variant+".glb")
        q.write_bytes(built)
        check,_=parse_glb(built)
        assert len(check["meshes"])==len(base["meshes"])
        assert [x["attributes"] for m in check["meshes"] for x in m["primitives"]] == [
            x["attributes"] for m in base["meshes"] for x in m["primitives"]]
        assert [x["indices"] for m in check["meshes"] for x in m["primitives"]] == [
            x["indices"] for m in base["meshes"] for x in m["primitives"]]
        reopened=trimesh.load(q,force="scene",process=False)
        tri=sum(len(g.faces) for g in reopened.geometry.values())
        assert tri == metrics["real_input_triangles"], (variant,tri)
        metrics[variant]={"bytes":len(built),"sha256":digest(built),"triangles":tri,
                          "geometry_count":len(reopened.geometry),
                          "original_unassigned_assigned":missing,
                          "material_count":len(check.get("materials",[]))}
    (OUT/"evidence_mesh.json").write_text(json.dumps(metrics,indent=2)+"\n")
    pathlib.Path("run315_view.html").write_text(HTML)
    print(json.dumps(metrics,indent=2))

def image_stats(path):
    arr=np.asarray(Image.open(path).convert("RGB")).astype(np.float32)
    region=arr[int(arr.shape[0]*.16):int(arr.shape[0]*.85),
               int(arr.shape[1]*.17):int(arr.shape[1]*.84)]
    m=np.any(np.abs(region-np.asarray(BG)[None,None,:])>13,axis=-1)
    lum=(region[...,0]*.2126+region[...,1]*.7152+region[...,2]*.0722)
    return {"non_background_fraction":float(m.mean()),
            "non_background_median_luma":float(np.median(lum[m])) if m.any() else None,
            "bright_area_fraction":float(np.logical_and(m, lum>92).mean()),
            "dark_area_fraction":float(np.logical_and(m, lum<45).mean())}

def browser():
    class Handler(SimpleHTTPRequestHandler):
        def log_message(self, *args): pass
    http=ThreadingHTTPServer(("127.0.0.1",8765),Handler)
    threading.Thread(target=http.serve_forever, daemon=True).start()
    report={"run":315,"research_only":True,"release":False,"art_approved":False,
            "real_phone":False,"viewport":[390,780],"environment":"desktop Chromium SwiftShader WebGL2","variants":{}}
    with sync_playwright() as p:
        b=p.chromium.launch(headless=True,args=["--enable-unsafe-swiftshader","--use-gl=angle",
            "--use-angle=swiftshader","--disable-dev-shm-usage"])
        for v in VARIANTS:
            page=b.new_page(viewport={"width":390,"height":780},device_scale_factor=1)
            errors=[];page.on("pageerror",lambda e:errors.append(str(e)))
            resp=page.goto("http://127.0.0.1:8765/run315_view.html?variant="+v,
                           timeout=90000,wait_until="domcontentloaded")
            page.wait_for_function("window.GATE && !['START'].includes(window.GATE.state)",timeout=90000)
            status=page.evaluate("window.GATE")
            status["http_status"]=resp.status if resp else None
            status["errors"]=errors
            status["frames"]=[]
            if status["state"]=="LOADED" and status["webgl2"]:
                for az,rear in [(0,False),(90,False),(180,False),(180,True)]:
                    stats=page.evaluate("([a,r])=>window.setAngle(a,r)",[az,rear])
                    page.wait_for_timeout(280)
                    path=OUT/(v+"_angle_"+str(az)+("_rearLight" if rear else "")+".png")
                    page.screenshot(path=str(path))
                    status["frames"].append({"angle":az,"rear_light":rear,
                       "sha256":digest(path.read_bytes()),"pixel":image_stats(path),
                       "render":stats})
            report["variants"][v]=status
            page.close()
        b.close()
    http.shutdown()
    (OUT/"actual_browser_evidence.json").write_text(json.dumps(report,indent=2)+"\n")
    (OUT/"NO_RELEASE.txt").write_text(
      "Controlled PBR and unlit technical diagnostics only. Original organic chick anatomy and down art rejected. "
      "No actual phone; never deploy or present GLBs as a usable pet.\n")
    print(json.dumps(report,indent=2))
    assert all(report["variants"][v]["state"]=="LOADED" and report["variants"][v]["webgl2"]
               and len(report["variants"][v]["frames"])==4 for v in VARIANTS)
if __name__ == "__main__":
    a=argparse.ArgumentParser();a.add_argument("phase",choices=["produce","browser"]);x=a.parse_args()
    if x.phase=="produce":produce()
    else:browser()
