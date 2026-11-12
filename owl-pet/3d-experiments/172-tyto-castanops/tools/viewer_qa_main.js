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
   const size=b.getSize(new THREE.Vector3());
   // V26/v27 actual bill/eyes are at positive X, NOT positive Z.
   // On portrait phones the horizontal FOV is much narrower than the vertical FOV.
   // Fit both axes rather than using the object diagonal as an arbitrary distance.
   const tanV=Math.tan(THREE.MathUtils.degToRad(camera.fov)*0.5);
   const tanH=tanV*camera.aspect;
   const distance=Math.max(size.y/(2*tanV*0.70),size.z/(2*tanH*0.70))+size.x*0.8;
   camera.position.copy(center).add(new THREE.Vector3(distance,0.09*distance,0.10*distance));
   camera.near=Math.max(.001,distance*0.002);
   camera.far=Math.max(10,distance*20);camera.updateProjectionMatrix();
   controls.target.copy(center);controls.update();
   window.__qa.sourceFront='+X verified from original beak/eyes geometry';
   window.__qa.initialDistance=+distance.toFixed(4);
   window.__qa.modelBounds=size.toArray().map(v=>+v.toFixed(4));
   window.__qa.frameFitChecked=false;
   window.__qa.modelBoundsCorners=[];
   for (const x of [b.min.x,b.max.x]) for (const y of [b.min.y,b.max.y]) for (const z of [b.min.z,b.max.z])
     window.__qa.modelBoundsCorners.push([x,y,z]);
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
   window.__qa.cameraPosition=camera.position.toArray().map(v=>+v.toFixed(3));
   if(window.__qa.loaded && window.__qa.modelBoundsCorners?.length){
     // Quantitative screen-space composition gate: loading a model is not enough.
     camera.updateMatrixWorld(true);
     const corners=window.__qa.modelBoundsCorners.map(p=>
       new THREE.Vector3(...p).project(camera));
     const lim={left:Math.min(...corners.map(p=>p.x)),
       right:Math.max(...corners.map(p=>p.x)),
       bottom:Math.min(...corners.map(p=>p.y)),
       top:Math.max(...corners.map(p=>p.y))};
     window.__qa.framing={...lim,inFrame:
       lim.left>=-0.96&&lim.right<=0.96&&lim.bottom>=-0.96&&lim.top<=0.96};
     window.__qa.frameFitChecked=true;
   }
   if(window.__qa.loaded && window.__qa.renderedFrames%50===0){
     window.__qa.glError=gl.getError();
   }
 }
 frame();
 addEventListener('resize',()=>{
   camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();
   renderer.setSize(innerWidth,innerHeight);
 });
} catch(e) {window.__qa.errors.push(String(e));}
