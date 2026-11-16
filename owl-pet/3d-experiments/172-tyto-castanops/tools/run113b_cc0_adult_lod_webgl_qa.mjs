// Run113B — actual CC0 adult owl LOD, browser-source QA only (NOT target juvenile).
// Desktop and mobile-viewport Chromium SwiftShader are NOT real phone GPU.
import fs from 'node:fs';
import {chromium,devices} from 'playwright';
const dir=process.argv[2];
fs.mkdirSync(dir,{recursive:true});
const browser=await chromium.launch({headless:true,args:[
 '--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader',
 '--enable-webgl','--disable-gpu-sandbox','--disable-dev-shm-usage']});
const output={run:'113B',asset:'real CC0 adult great horned owl 91999 triangles (wrong species and age; never publish)',
 renderer:'Chromium SwiftShader software WebGL2',physicalPhoneTest:false,artApproved:false,results:[]};
for(const conf of [{name:'desktop',width:1280,height:720,mobile:false},
 {name:'simulated_phone',width:390,height:844,mobile:true}]){
 const ctx=await browser.newContext({
  viewport:{width:conf.width,height:conf.height},
  ...(conf.mobile?{isMobile:true,hasTouch:true,deviceScaleFactor:2,
   userAgent:devices['iPhone 13'].userAgent}:{deviceScaleFactor:1})});
 const page=await ctx.newPage();const errors=[];let result={name:conf.name};
 page.on('pageerror',e=>errors.push(String(e)));
 page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
 try{
  await page.goto('http://127.0.0.1:4173/',{waitUntil:'networkidle',timeout:90000});
  await page.waitForFunction(()=>window.__qa?.loaded||window.__qa?.errors?.length,{timeout:60000});
  await page.waitForTimeout(500);
  const before=await page.evaluate(()=>({...window.__qa}));
  await page.screenshot({path:dir+'/'+conf.name+'_ACTUAL_ADULT_LOD_UNAPPROVED.png'});
  await page.mouse.move(conf.width*.35,conf.height*.5);await page.mouse.down();
  await page.mouse.move(conf.width*.62,conf.height*.48,{steps:19});await page.mouse.up();
  await page.waitForTimeout(460);
  const after=await page.evaluate(()=>({...window.__qa}));
  result={name:conf.name,loaded:after.loaded,webgl:after.webgl,
   renderer:after.renderer,meshes:after.meshes,triangles:after.triangles,
   frames:after.frames,beforeFrame:before.framing,afterFrame:after.framing,
   orbitMoved:JSON.stringify(before.camera)!==JSON.stringify(after.camera),
   glError:after.glError,pageErrors:errors,appErrors:after.errors};
 }catch(e){result={name:conf.name,error:String(e),pageErrors:errors};}
 output.results.push(result);await ctx.close();
}
await browser.close();
output.technicalPass=output.results.length===2 && output.results.every(x=>
 x.loaded && x.meshes>=1 && x.triangles>=80000 && x.triangles<=110000 &&
 x.beforeFrame?.inFrame && x.afterFrame?.inFrame && x.orbitMoved &&
 !x.glError && !x.pageErrors?.length && !x.appErrors?.length);
fs.writeFileSync(dir+'/run113b_real_adult_webgl_qa.json',JSON.stringify(output,null,2));
console.log(JSON.stringify(output,null,2));
if(!output.technicalPass)process.exitCode=2;
