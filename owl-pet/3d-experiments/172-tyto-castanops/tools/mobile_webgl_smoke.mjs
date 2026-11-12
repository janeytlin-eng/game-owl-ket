import fs from 'node:fs';
import {chromium,devices} from 'playwright';
const address='http://127.0.0.1:4173';
const output=process.argv[2]||'browser-qa';
fs.mkdirSync(output,{recursive:true});
const browser=await chromium.launch({headless:true,args:[
 '--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader',
 '--disable-gpu-sandbox','--enable-webgl','--disable-dev-shm-usage'
]});
const res={runner:'GitHub Linux Chromium, software SwiftShader, NOT a physical phone',
           checkedAt:new Date().toISOString(),cases:[]};
for(const setting of [
 {name:'desktop_1280x720',viewport:{width:1280,height:720},isMobile:false},
 {name:'emulated_phone_390x844',...devices['iPhone 13'],viewport:{width:390,height:844}}
]){
 const ctx=await browser.newContext(setting.isMobile?{
  viewport:setting.viewport,isMobile:true,hasTouch:true,deviceScaleFactor:2,
  userAgent:devices['iPhone 13'].userAgent
 }:{viewport:setting.viewport});
 const page=await ctx.newPage();
 const errors=[];
 page.on('pageerror',e=>errors.push(String(e)));
 page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
 let state;
 try{
   await page.goto(address,{waitUntil:'networkidle',timeout:55000});
   await page.waitForFunction(()=>window.__qa?.loaded||window.__qa?.errors?.length>0,null,{timeout:55000});
   await page.waitForTimeout(1200);
   const before=await page.evaluate(()=>structuredClone(window.__qa));
   await page.mouse.move(setting.viewport.width*.35,setting.viewport.height*.45);
   await page.mouse.down();await page.mouse.move(setting.viewport.width*.62,setting.viewport.height*.47,{steps:10});
   await page.mouse.up();await page.waitForTimeout(450);
   const after=await page.evaluate(()=>structuredClone(window.__qa));
   await page.screenshot({path:`${output}/${setting.name}.png`});
   state={name:setting.name,before,after,pageErrors:errors,
       orbit_camera_changed:JSON.stringify(before.cameraPosition)!==JSON.stringify(after.cameraPosition),
       loaded:after.loaded,frames:after.renderedFrames,glError:after.glError};
 }catch(e){state={name:setting.name,error:String(e),pageErrors:errors};}
 res.cases.push(state);
 await ctx.close();
}
await browser.close();
fs.writeFileSync(`${output}/browser_qa.json`,JSON.stringify(res,null,2));
console.log(JSON.stringify(res,null,2));
if(res.cases.some(c=>!c.loaded||c.pageErrors?.length||c.after?.glError)) process.exitCode=2;
