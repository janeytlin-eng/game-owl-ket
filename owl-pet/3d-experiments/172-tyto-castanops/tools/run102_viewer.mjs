import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
window.__qa={loaded:false,frames:0,errors:[],webglVersion:null,morphSamples:[],clipCount:0,renderCalls:0};
let renderer;
try {
  renderer=new THREE.WebGLRenderer({antialias:false,preserveDrawingBuffer:true,powerPreference:'low-power'});
  renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,1.4));
  renderer.setSize(innerWidth,innerHeight);
  renderer.outputColorSpace=THREE.SRGBColorSpace;
  document.body.appendChild(renderer.domElement);
  const gl=renderer.getContext();
  window.__qa.webglVersion=gl.getParameter(gl.VERSION);
  window.__qa.rendererLabel=gl.getParameter(gl.RENDERER);
  const scene=new THREE.Scene(); scene.background=new THREE.Color('#25303b');
  scene.add(new THREE.HemisphereLight(0xfff7e7,0x7f92a9,2.2));
  const key=new THREE.DirectionalLight(0xffedd8,3.1);key.position.set(3,5,6);scene.add(key);
  const fill=new THREE.DirectionalLight(0xe5edff,1.0);fill.position.set(-4,2,-2);scene.add(fill);
  const camera=new THREE.PerspectiveCamera(34,innerWidth/innerHeight,.01,100);
  const controls=new OrbitControls(camera,renderer.domElement);
  controls.enableDamping=true;controls.enablePan=false;
  const clock=new THREE.Clock();
  let mixer=null,root=null,cornerCoords=[];
  new GLTFLoader().load('/candidate.glb',gltf=>{
    root=gltf.scene;scene.add(root);
    window.__qa.clipCount=gltf.animations.length;
    if(!gltf.animations.length)throw Error('No exported glTF animation');
    mixer=new THREE.AnimationMixer(root);
    mixer.clipAction(gltf.animations[0]).play();
    const box=new THREE.Box3().setFromObject(root);
    if(box.isEmpty())throw Error('Empty 3D volume');
    const center=box.getCenter(new THREE.Vector3());
    const dim=box.getSize(new THREE.Vector3());
    const tanV=Math.tan(THREE.MathUtils.degToRad(camera.fov*.5));
    const tanH=tanV*camera.aspect;
    const dist=Math.max(dim.y/(2*tanV*.61),dim.x/(2*tanH*.61))+dim.z*.75;
    camera.position.copy(center).add(new THREE.Vector3(0,dim.y*.07,dist));
    camera.near=Math.max(.001,dist*.003);camera.far=dist*10;camera.updateProjectionMatrix();
    controls.target.copy(center);controls.update();
    window.__qa.bounds=dim.toArray();
    window.__qa.sourceIs3D=true;
    cornerCoords=[];
    for(let x of [box.min.x,box.max.x])for(let y of [box.min.y,box.max.y])
      for(let z of [box.min.z,box.max.z])cornerCoords.push([x,y,z]);
    window.__qa.loaded=true;
  },undefined,e=>window.__qa.errors.push(String(e)));
  function frame(){
    requestAnimationFrame(frame);
    const dt=Math.min(.075,clock.getDelta());
    if(mixer)mixer.update(dt);
    controls.update();
    renderer.render(scene,camera);
    window.__qa.frames++;
    window.__qa.renderCalls=renderer.info.render.calls;
    window.__qa.cameraPosition=camera.position.toArray();
    if(root){
      const morphs=[];
      root.traverse(o=>{if(o.isMesh&&o.morphTargetInfluences?.length)
        morphs.push(...o.morphTargetInfluences);});
      window.__qa.morphValues=morphs.map(v=>+v.toFixed(4));
      camera.updateMatrixWorld(true);
      const projected=cornerCoords.map(p=>new THREE.Vector3(...p).project(camera));
      const range={left:Math.min(...projected.map(x=>x.x)),right:Math.max(...projected.map(x=>x.x)),
                   bottom:Math.min(...projected.map(x=>x.y)),top:Math.max(...projected.map(x=>x.y))};
      window.__qa.framing={...range,inFrame:range.left>=-.98&&range.right<=.98&&range.bottom>=-.98&&range.top<=.98};
    }
    if(window.__qa.frames%25===0)window.__qa.glError=gl.getError();
  }
  frame();
  addEventListener('resize',()=>{camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight);});
}catch(e){window.__qa.errors.push(String(e));}
