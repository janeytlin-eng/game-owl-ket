// REAL Three.js + Chromium WebGL2 draw; simulated phone viewport is not physical GPU.
import fs from 'node:fs';
import {chromium,devices} from 'playwright';
const target=process.argv[2]||'qa92/browser';
fs.mkdirSync(target,{recursive:true});
const b=await chromium.launch({headless:true,args:[
 '--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader',
 '--disable-gpu-sandbox','--enable-webgl','--disable-dev-shm-usage'
]});
const report={renderer:'Chromium SwiftShader software, not Android or iOS hardware',cases:[]};
for(const cfg of [
 {name:'desktop',size:{width:1280,height:720},mobile:false},
 {name:'phone_simulated',size:{width:390,height:844},mobile:true}
]){
 const ctx=await b.newContext(cfg.mobile?{
  viewport:cfg.size,isMobile:true,hasTouch:true,deviceScaleFactor:2,
  userAgent:devices['iPhone 13'].userAgent
 }:{viewport:cfg.size});
 const page=await ctx.newPage();
 const problems=[];
 page.on('pageerror',e=>problems.push('pageerror:'+String(e)));
 page.on('console',m=>{if(m.type()==='error')problems.push(m.text())});
 let result={name:cfg.name};
 try{
  await page.goto('http://127.0.0.1:4173',{waitUntil:'networkidle',timeout:45000});
  await page.waitForFunction(()=>window.__qa?.loaded||window.__qa?.errors?.length,null,{timeout:60000});
  await page.waitForTimeout(1700);
  const first=await page.evaluate(()=>structuredClone(window.__qa));
  await page.mouse.move(cfg.size.width*.34,cfg.size.height*.45);
  await page.mouse.down();
  await page.mouse.move(cfg.size.width*.6,cfg.size.height*.48,{steps:10});
  await page.mouse.up();await page.waitForTimeout(600);
  const second=await page.evaluate(()=>structuredClone(window.__qa));
  await page.screenshot({path:target+'/'+cfg.name+'.png'});
  result={name:cfg.name,loaded:second.loaded,meshes:second.modelMeshes,triangles:second.triangles,
          frames:second.renderedFrames,webgl:second.webglVersion,glError:second.glError,
          framing_before:first.framing,framing_after:second.framing,
          orbit_changed:JSON.stringify(first.cameraPosition)!==JSON.stringify(second.cameraPosition),
          errors:[...problems,...second.errors],
          sourceFront:second.sourceFront,
          important_note:'No scientific side/back verification; +Z eye-node heuristic applies only to prior sculpt and must be disregarded for TripoSR'};
 }catch(e){result={name:cfg.name,error:String(e),errors:problems};}
 report.cases.push(result);
 await ctx.close();
}
await b.close();
fs.writeFileSync(target+'/browser_qa.json',JSON.stringify(report,null,2));
console.log(JSON.stringify(report,null,2));
if(report.cases.some(c=>!c.loaded||!c.triangles||c.errors?.length||c.glError))process.exitCode=2;
