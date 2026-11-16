import fs from 'node:fs';
import {chromium,devices} from 'playwright';
const output=process.argv[2] || 'browser_qa';
fs.mkdirSync(output,{recursive:true});
const browser=await chromium.launch({headless:true,args:[
  '--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader',
  '--enable-webgl','--disable-gpu-sandbox','--disable-dev-shm-usage'
]});
const result={source:'GitHub Actions Chromium software SwiftShader',physical_phone_gpu_test:false,
  actual_touch_test:false,art_gate:'UNAPPROVED',cases:[]};
for(const config of [
  {name:'desktop_1280x720',width:1280,height:720,mobile:false},
  {name:'simulated_phone_390x844',width:390,height:844,mobile:true}
]){
  const ctx=await browser.newContext({
    viewport:{width:config.width,height:config.height},
    ...(config.mobile?{isMobile:true,hasTouch:true,deviceScaleFactor:2,
      userAgent:devices['iPhone 13'].userAgent}:{deviceScaleFactor:1})
  });
  const page=await ctx.newPage();
  const errors=[];
  page.on('pageerror',e=>errors.push(String(e)));
  page.on('console',msg=>{if(msg.type()==='error')errors.push(msg.text())});
  let info={name:config.name};
  try {
    await page.goto('http://127.0.0.1:4173/',{waitUntil:'networkidle',timeout:90000});
    await page.waitForFunction(()=>window.__qa?.loaded || window.__qa?.errors?.length,{timeout:60000});
    if(!(await page.evaluate(()=>window.__qa.loaded)))throw Error('Failed to load glTF: '+JSON.stringify(await page.evaluate(()=>window.__qa.errors)));
    const history=[];
    for(let i=0;i<10;i++){
      await page.waitForTimeout(220);
      history.push(await page.evaluate(()=>window.__qa.morphValues||[]));
    }
    const first=await page.evaluate(()=>structuredClone(window.__qa));
    await page.screenshot({path:output+'/'+config.name+'_native_animated_glb.png'});
    await page.mouse.move(config.width*.30,config.height*.45);
    await page.mouse.down();
    await page.mouse.move(config.width*.58,config.height*.44,{steps:15});
    await page.mouse.up();
    await page.waitForTimeout(350);
    const after=await page.evaluate(()=>structuredClone(window.__qa));
    const values=history.flat();
    const range=values.length?Math.max(...values)-Math.min(...values):0;
    info={name:config.name,loaded:after.loaded,webglVersion:after.webglVersion,
      renderer:after.rendererLabel,clipCount:after.clipCount,
      morphValues:after.morphValues,morphAnimationDynamic:range>.20,
      morphChangeRange:range,renderedFrames:after.frames,
      renderingCalls:after.renderCalls,initialFraming:first.framing,
      afterOrbitFraming:after.framing,
      orbitCameraChanged:JSON.stringify(first.cameraPosition)!==JSON.stringify(after.cameraPosition),
      glError:after.glError||0,pageErrors:errors,applicationErrors:after.errors};
  } catch(e) {
    info={name:config.name,error:String(e),pageErrors:errors};
  }
  result.cases.push(info);
  await ctx.close();
}
await browser.close();
fs.writeFileSync(output+'/run102_software_webgl_metrics.json',JSON.stringify(result,null,2));
console.log(JSON.stringify(result,null,2));
if(result.cases.some(c=>!c.loaded||c.clipCount<1||!c.morphAnimationDynamic||
  !c.initialFraming?.inFrame||!c.afterOrbitFraming?.inFrame||
  !c.orbitCameraChanged||c.glError||c.pageErrors?.length||c.applicationErrors?.length))
  process.exitCode=2;
