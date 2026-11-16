import fs from 'node:fs';
import {chromium, devices} from 'playwright';
const dir=process.argv[2];fs.mkdirSync(dir,{recursive:true});
const browser=await chromium.launch({headless:true,args:[
'--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader',
'--enable-webgl','--disable-gpu-sandbox','--disable-dev-shm-usage']});
const out={engine:'Chromium SwiftShader software WebGL2; not actual phone GPU',
 model:'new genuine Run115 GLB',physicalPhoneTest:false,results:[]};
for(const test of [{name:'desktop',width:1280,height:720,mobile:false},
{name:'simulated_phone',width:390,height:844,mobile:true}]){
const ctx=await browser.newContext({viewport:{width:test.width,height:test.height},
 ...(test.mobile?{isMobile:true,hasTouch:true,deviceScaleFactor:2,
 userAgent:devices['iPhone 13'].userAgent}:{deviceScaleFactor:1})});
const page=await ctx.newPage(),errors=[];
page.on('pageerror',e=>errors.push(String(e)));
page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
let record={name:test.name};
try {
await page.goto('http://127.0.0.1:4173/',{waitUntil:'networkidle',timeout:90000});
await page.waitForFunction(()=>window.__qa?.loaded||window.__qa?.errors?.length,{timeout:60000});
await page.waitForTimeout(550);
const before=await page.evaluate(()=>({...window.__qa}));
await page.screenshot({path:dir+'/'+test.name+'_real_run115.png'});
await page.mouse.move(test.width*.36,test.height*.50);await page.mouse.down();
await page.mouse.move(test.width*.63,test.height*.48,{steps:17});await page.mouse.up();
await page.waitForTimeout(450);
const after=await page.evaluate(()=>({...window.__qa}));
record={name:test.name,loaded:after.loaded,webgl:after.webgl,renderer:after.renderer,
 meshes:after.meshes,triangles:after.triangles,frames:after.frames,
 beforeFrame:before.framing,afterFrame:after.framing,
 orbitMoved:JSON.stringify(before.camera)!==JSON.stringify(after.camera),
 glError:after.glError,pageErrors:errors,appErrors:after.errors};
} catch(e){record={name:test.name,error:String(e),pageErrors:errors};}
out.results.push(record);await ctx.close();
}
await browser.close();
fs.writeFileSync(dir+'/run115_software_webgl_qa.json',JSON.stringify(out,null,2));
console.log(JSON.stringify(out,null,2));
if(out.results.some(r=>!r.loaded||r.meshes<7||r.triangles<115000||
 !r.beforeFrame?.inFrame||!r.afterFrame?.inFrame||!r.orbitMoved||
 r.glError||r.pageErrors?.length||r.appErrors?.length))process.exitCode=2;