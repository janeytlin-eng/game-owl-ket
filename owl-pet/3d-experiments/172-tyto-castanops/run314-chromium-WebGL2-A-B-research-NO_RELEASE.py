#!/usr/bin/env python3
"""Independent 3D WebGL2 QA of Run314 A/B research GLBs. Strictly NOT a release or actual phone test."""
import hashlib,json,os,pathlib,time
from playwright.sync_api import sync_playwright
BASE=pathlib.Path(os.getenv('OWL314_BROWSER_OUT','/tmp/owl172_run314_webgl2'))
BASE.mkdir(parents=True,exist_ok=True)
ROOT=os.getenv('OWL314_HOST','http://127.0.0.1:8765')
HTML='''<!doctype html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<script type="importmap">{"imports":{"three":"/node_modules/three/build/three.module.js","three/addons/":"/node_modules/three/examples/jsm/"}}</script>
</head><body style="padding:0;margin:0;background:#22282f;overflow:hidden">
<script type="module">
import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
let renderer;
window.GATE={status:'WAITING',webgl2:false,triangles:0,meshes:0,textureCount:0,device:'390x780 simulated viewport only'};
try {
renderer=new THREE.WebGLRenderer({antialias:true,alpha:false,powerPreference:'low-power'});
renderer.setSize(innerWidth,innerHeight);renderer.setPixelRatio(1);
renderer.setClearColor(0x22282f);renderer.outputColorSpace=THREE.SRGBColorSpace;
renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.1;
document.body.appendChild(renderer.domElement);
const context=renderer.getContext();
window.GATE.webgl2=(typeof WebGL2RenderingContext!=='undefined' && context instanceof WebGL2RenderingContext);
const scene=new THREE.Scene();
scene.add(new THREE.AmbientLight(0xffffff,1.65));
const key=new THREE.DirectionalLight(0xfff7eb,2.2);key.position.set(4,4,6);scene.add(key);
const rim=new THREE.DirectionalLight(0xd7eaff,1.25);rim.position.set(-4,-3,2);scene.add(rim);
const camera=new THREE.PerspectiveCamera(37,innerWidth/innerHeight,.01,250);
camera.up.set(0,0,1);
let object,dist=5;
window.setAngle=(az)=>{const a=az*Math.PI/180;camera.position.set(Math.sin(a)*dist,Math.cos(a)*dist,dist*.20);camera.lookAt(0,0,0);renderer.render(scene,camera);return {az,triangles:renderer.info.render.triangles,calls:renderer.info.render.calls}};
const params=new URLSearchParams(location.search);
const which=params.get('variant')||'A';
const count=which==='A'?'6500':'14000';
new GLTFLoader().load('/research/'+which+'/run314_curved_down_'+count+'_RESEARCH_ONLY_NO_RELEASE.glb',(g)=>{
  object=g.scene;const b=new THREE.Box3().setFromObject(object),size=b.getSize(new THREE.Vector3()),ctr=b.getCenter(new THREE.Vector3());
  object.position.sub(ctr);scene.add(object);
  dist=Math.max(size.x,size.y,size.z)*2.25;
  object.traverse((x)=>{if(x.isMesh){window.GATE.meshes++;const gg=x.geometry;window.GATE.triangles+=(gg.index?gg.index.count:gg.attributes.position.count)/3;
    if(x.material){for(const m of (Array.isArray(x.material)?x.material:[x.material])){if(m.map)window.GATE.textureCount++;}}
  }});
  window.setAngle(0);window.GATE.status='LOADED';window.GATE.variant=which;
},undefined,(e)=>{window.GATE.status='GLB_LOAD_ERROR';window.GATE.error=String(e)});
}catch(e){window.GATE.status='WEBGL_SETUP_ERROR';window.GATE.error=String(e)}
</script></body></html>'''


def run():
    results={"run":"314_browser","target":"#172 v3 rightmost age-unknown mesoptile","release":False,
             "art":"REJECTED_UNCHANGED","physical_phone":"NOT_TESTED","requested_viewport":[390,780],
             "environment":"Desktop Chromium with SwiftShader software WebGL2, NOT real Android/iPhone"}
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,args=['--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader','--disable-dev-shm-usage'])
        for variant in ('A','B'):
            d=BASE/variant;d.mkdir(exist_ok=True)
            page=browser.new_page(viewport={'width':390,'height':780},device_scale_factor=1)
            errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
            url=ROOT+'/run314_view.html?variant='+variant
            rsp=page.goto(url,timeout=90000,wait_until='domcontentloaded')
            try:
                page.wait_for_function("window.GATE && window.GATE.status!=='WAITING'",timeout=90000)
            except Exception as e:errors.append('wait:'+str(e))
            gate=page.evaluate('window.GATE') or {}
            gate['http']=rsp.status if rsp else None
            gate['page_errors']=errors
            gate['frames']=[]
            if gate.get('status')=='LOADED' and gate.get('webgl2'):
                for az in (0,90,180):
                    stats=page.evaluate(f'window.setAngle({az})')
                    page.wait_for_timeout(600)
                    f=d/f'angle_{az}.png';page.screenshot(path=str(f))
                    gate['frames'].append(dict(angle=az,file=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),bytes=f.stat().st_size,stats=stats))
            results[variant]=gate
            page.close()
        browser.close()
    (BASE/'actual_browser_evidence_NO_RELEASE.json').write_text(json.dumps(results,indent=2)+'\n')
    (BASE/'NO_RELEASE.txt').write_text('Research-only WebGL2 desktop SwiftShader test. Base art rejected, no real phone, no release.\n')
    print(json.dumps(results,indent=2))
    if any(results[x].get('status')!='LOADED' or not results[x].get('webgl2') or len(results[x].get('frames',[]))!=3 for x in ('A','B')):
        raise SystemExit('TECHNICAL_BROWSER_TEST_FAILED_NO_RELEASE')

if __name__=='__main__':run()
