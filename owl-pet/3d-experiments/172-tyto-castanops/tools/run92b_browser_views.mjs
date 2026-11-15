// Render actual new GLB in Chromium SwiftShader. Inspect both before and after orbit.
// Emulated viewport is NOT hardware validation or successful aesthetic approval.
import fs from 'node:fs';
import {chromium,devices} from 'playwright';
const dir=process.argv[2]||'qa92b/browser';
fs.mkdirSync(dir,{recursive:true});
const browser=await chromium.launch({headless:true,args:[
 '--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader',
 '--disable-gpu-sandbox','--enable-webgl','--disable-dev-shm-usage'
]});
const res={hardware_gpu:false,art_approved:false,cases:[]};
for(const setting of [
 {name:'desktop',size:{width:1280,height:720},mobile:false},
 {name:'phone_emulated',size:{width:390,height:844},mobile:true}])
{
 const ctx=await browser.newContext(setting.mobile?{
  viewport:setting.size,isMobile:true,hasTouch:true,deviceScaleFactor:2,
  userAgent:devices['iPhone 13'].userAgent
 }:{viewport:setting.size});
 const page=await ctx.newPage();const errors=[];
 page.on('pageerror',e=>errors.push(String(e)));
 page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
 let info={name:setting.name};
 try{
  await page.goto('http://127.0.0.1:4173',{waitUntil:'networkidle',timeout:60000});
  await page.waitForFunction(()=>window.__qa?.loaded||window.__qa?.errors?.length>0,null,{timeout:60000});
  await page.waitForTimeout(800);
  let initial=await page.evaluate(()=>structuredClone(window.__qa));
  await page.screenshot({path:dir+'/'+setting.name+'_initial.png'});
  await page.mouse.move(setting.size.width*.30,setting.size.height*.45);
  await page.mouse.down();
  await page.mouse.move(setting.size.width*.58,setting.size.height*.49,{steps:14});
  await page.mouse.up();await page.waitForTimeout(450);
  let after=await page.evaluate(()=>structuredClone(window.__qa));
  await page.screenshot({path:dir+'/'+setting.name+'_rotated.png'});
  info={name:setting.name,loaded:after.loaded,frames:after.renderedFrames,
    real_glb_triangles:after.triangles,webgl:after.webglVersion,glError:after.glError,
    framed_initial:initial.framing?.inFrame,
    framed_after:after.framing?.inFrame,
    orbit_changed:JSON.stringify(initial.cameraPosition)!==JSON.stringify(after.cameraPosition),
    page_errors:[...errors,...after.errors],
    automatic_front_eye_node_check_invalid_for_neural_asset:true};
 }catch(e){info={name:setting.name,error:String(e),page_errors:errors};}
 res.cases.push(info);await ctx.close();
}
await browser.close();
fs.writeFileSync(dir+'/qa.json',JSON.stringify(res,null,2));
console.log(JSON.stringify(res,null,2));
if(res.cases.some(c=>!c.loaded||!c.real_glb_triangles||c.page_errors?.length||c.glError))process.exitCode=2;
