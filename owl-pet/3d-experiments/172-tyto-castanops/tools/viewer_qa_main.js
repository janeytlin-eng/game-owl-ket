import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';

window.__qa={loaded:false,renderedFrames:0,errors:[],source:'/candidate.glb'};
let renderer;
try {
 renderer=new THREE.WebGLRenderer({antialias:false,alpha:true,powerPreference:'low-power',preserveDrawingBuffer:true});
 document.body.appendChild(renderer.domElement);
 renderer.setSize(innerWidth,innerHeight);
 renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));
 renderer.outputColorSpace=THREE.SRGBColorSpace;
 const gl=renderer.getContext();
 window.__qa.webglVersion=gl.getParameter(gl.VERSION);
 window.__qa.renderer=String(gl.getParameter(gl.RENDERER));
 const scene=new THREE.Scene();
 scene.background=new THREE.Color(0x25303b);
 scene.add(new THREE.HemisphereLight(0xfff2e8,0x8895ac,2.1));
 const key=new THREE.DirectionalLight(0xffecd9,3.4);key.position.set(3,4,5);scene.add(key);
 const camera=new THREE.PerspectiveCamera(34,innerWidth/innerHeight,.01,100);
 const controls=new OrbitControls(camera,renderer.domElement);
 controls.enableDamping=true;
 controls.enablePan=false;
 const loader=new GLTFLoader();
 loader.load('/candidate.glb',gltf=>{
   const root=gltf.scene;
   scene.add(root);
   const b=new THREE.Box3().setFromObject(root);
   if(b.isEmpty())throw new Error('Empty model bounding box');
   const center=b.getCenter(new THREE.Vector3());
   const r=b.getSize(new THREE.Vector3()).length();
   camera.position.copy(center).add(new THREE.Vector3(0.5*r,.22*r,1.25*r));
   camera.near=Math.max(.001,r*.005);camera.far=r*20;camera.updateProjectionMatrix();
   controls.target.copy(center);controls.update();
   window.__qa.modelMeshes=0;window.__qa.triangles=0;
   root.traverse(x=>{
    if(x.isMesh){
      window.__qa.modelMeshes++;
      const geo=x.geometry;
      window.__qa.triangles+=(geo.index?geo.index.count:geo.attributes.position.count)/3;
    }
   });
   window.__qa.loaded=true;
 },undefined,err=>window.__qa.errors.push(String(err)));
 function frame(){
   requestAnimationFrame(frame);
   controls.update();
   renderer.render(scene,camera);
   window.__qa.renderedFrames++;
   if(window.__qa.loaded && window.__qa.renderedFrames%50===0){
     window.__qa.cameraPosition=camera.position.toArray().map(v=>+v.toFixed(3));
     window.__qa.glError=gl.getError();
   }
 }
 frame();
 addEventListener('resize',()=>{
   camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();
   renderer.setSize(innerWidth,innerHeight);
 });
} catch(e) {window.__qa.errors.push(String(e));}
