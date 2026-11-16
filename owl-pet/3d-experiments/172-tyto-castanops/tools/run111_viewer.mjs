import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
window.__qa={loaded:false,errors:[],frames:0,glError:0,source:'real Run111 GLB',physicalMobileGPU:false};
try {
const scene=new THREE.Scene();scene.background=new THREE.Color('#26323a');
const renderer=new THREE.WebGLRenderer({antialias:false,powerPreference:'low-power',preserveDrawingBuffer:true});
renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.25));renderer.setSize(innerWidth,innerHeight);
renderer.outputColorSpace=THREE.SRGBColorSpace;
renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=0.95;
document.body.appendChild(renderer.domElement);
const gl=renderer.getContext();
window.__qa.webgl=gl.getParameter(gl.VERSION);window.__qa.renderer=gl.getParameter(gl.RENDERER);
scene.add(new THREE.HemisphereLight(0xfff8ed,0x8091aa,1.0));
const key=new THREE.DirectionalLight(0xfff1e0,1.7);key.position.set(2,5,7);scene.add(key);
const fill=new THREE.DirectionalLight(0xdde6ff,.7);fill.position.set(-3,1,-3);scene.add(fill);
const cam=new THREE.PerspectiveCamera(34,innerWidth/innerHeight,.01,150);
const ctrl=new OrbitControls(cam,renderer.domElement);ctrl.enablePan=false;ctrl.enableDamping=true;
ctrl.minPolarAngle=.25;ctrl.maxPolarAngle=Math.PI-.25;
let corners=[];
new GLTFLoader().load('/candidate.glb',gltf=>{
const obj=gltf.scene;scene.add(obj);
const bbox=new THREE.Box3().setFromObject(obj);if(bbox.isEmpty())throw Error('Empty actual GLB');
const center=bbox.getCenter(new THREE.Vector3()), dims=bbox.getSize(new THREE.Vector3());
const tv=Math.tan(THREE.MathUtils.degToRad(cam.fov/2)), th=tv*cam.aspect;
const distance=Math.max(dims.y/(2*tv*.60),dims.x/(2*th*.60),dims.z*1.0)+dims.z*.60;
cam.position.copy(center).add(new THREE.Vector3(0,dims.y*.05,distance));
cam.near=Math.max(.005,distance*.003);cam.far=distance*12;cam.updateProjectionMatrix();
ctrl.target.copy(center);ctrl.update();
for (const x of [bbox.min.x,bbox.max.x])for(const y of [bbox.min.y,bbox.max.y])
 for(const z of [bbox.min.z,bbox.max.z])corners.push([x,y,z]);
window.__qa.meshes=0;window.__qa.triangles=0;
obj.traverse(o=>{if(o.isMesh){window.__qa.meshes++;const p=o.geometry.getIndex()?.count||o.geometry.getAttribute('position').count;
window.__qa.triangles+=Math.floor(p/3);}});
window.__qa.bounds=dims.toArray();window.__qa.loaded=true;
},undefined,err=>{window.__qa.errors.push(String(err))});
function render(){
requestAnimationFrame(render);ctrl.update();renderer.render(scene,cam);
window.__qa.frames++;window.__qa.renderCalls=renderer.info.render.calls;
window.__qa.camera=cam.position.toArray();
if(corners.length){
cam.updateMatrixWorld(true);
const proj=corners.map(p=>new THREE.Vector3(...p).project(cam));
const xs=proj.map(v=>v.x),ys=proj.map(v=>v.y);
const range={left:Math.min(...xs),right:Math.max(...xs),bottom:Math.min(...ys),top:Math.max(...ys)};
window.__qa.framing={...range,inFrame:range.left>-.99&&range.right<.99&&range.bottom>-.99&&range.top<.99};
}
if(window.__qa.frames%25===0)window.__qa.glError=gl.getError();
}
render();
addEventListener('resize',()=>{cam.aspect=innerWidth/innerHeight;cam.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight)});
} catch(e){window.__qa.errors.push(String(e));}