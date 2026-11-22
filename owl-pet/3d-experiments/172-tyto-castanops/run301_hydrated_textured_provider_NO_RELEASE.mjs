#!/usr/bin/env node
/**
 * Run301: diagnose React hydration/upload UI from Run300 before trying ONE ordinary
 * no-extra-pay textured image-to-GLB generation using the actual #172 v3 crop.
 * Research only. No rights/art/phone approval and absolutely no release.
 */
import fs from 'node:fs';
import crypto from 'node:crypto';
import {chromium} from 'playwright-core';
const OUT='owl172-run301-evidence',INPUT='target-owl172-isolated-WHITE.png';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
fs.mkdirSync(OUT,{recursive:true});
const report={run:'301',provider:'https://3dai.dev/en',source:'actual #172 v3 rightmost mesoptile Run295 exact crop',
 source_sha256:fs.existsSync(INPUT)?sha(fs.readFileSync(INPUT)):null,
 date:new Date().toISOString(),normal_free_submissions:0,provider_ready:false,
 native_glb:null,art_approved:false,rights_cleared:false,physical_phone_verified:false,
 paid_usd:0,release_allowed:false,events:[],issues:[]};
let browser;const pending=[];
function event(phase,data){report.events.push({phase,utc:new Date().toISOString(),...data});}
function inspect(buffer,url,origin){
 try {
  if(buffer.length<32 || buffer.toString('ascii',0,4)!=='glTF'||buffer.readUInt32LE(4)!==2||buffer.readUInt32LE(8)!==buffer.length)return;
  const n=buffer.readUInt32LE(12);
  if(buffer.toString('ascii',16,20)!=='JSON'||n<10||n>10000000||n+20>buffer.length)return;
  const j=JSON.parse(buffer.toString('utf8',20,20+n));
  const positionPrimitives=(j.meshes||[]).flatMap(m=>m.primitives||[]).filter(p=>p.attributes?.POSITION!==undefined).length;
  if(!positionPrimitives)return;
  const f=OUT+'/run301-real-generated-NOT_APPROVED.glb';
  if(!report.native_glb)fs.writeFileSync(f,buffer);
  report.native_glb={origin,url,bytes:buffer.length,sha256:sha(buffer),meshes:j.meshes?.length||0,
   positionPrimitives,embeddedImages:j.images?.length||0,textures:j.textures?.length||0,
   materials:j.materials?.length||0,extensions:j.extensionsUsed||[]};
  event('native-glb-captured',report.native_glb);
 }catch(err){event('glb-parse-rejected',{error:String(err).slice(0,200)});}
}
try{
 if(!fs.existsSync(INPUT))throw Error('Original v3 isolated white input missing');
 browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',headless:true,
  args:['--no-sandbox','--disable-dev-shm-usage','--use-gl=angle','--use-angle=swiftshader']});
 const page=await browser.newPage({viewport:{width:390,height:780},acceptDownloads:true});
 page.setDefaultTimeout(12000);
 page.on('pageerror',e=>event('page-error',{message:String(e).slice(0,300)}));
 page.on('response',res=>{
  const url=res.url(),type=res.headers()['content-type']||'';
  if(!(/\.glb([?#]|$)/i.test(url)||/model\/gltf-binary/i.test(type)||/\/download\/.*glb/i.test(url)))return;
  pending.push((async()=>{try{if(res.ok())inspect(await res.body(),url,'network')}catch(e){event('response-error',{message:String(e).slice(0,250)})}})());
 });
 page.on('download',dl=>pending.push((async()=>{try{const file=await dl.path();if(file)inspect(fs.readFileSync(file),dl.url(),'download')}catch(e){event('download-error',{message:String(e).slice(0,250)})}})()));
 const res=await page.goto(report.provider,{waitUntil:'domcontentloaded',timeout:60000});
 report.provider_http=res?.status();
 if(report.provider_http!==200)throw Error('provider HTTP '+report.provider_http);
 await page.waitForLoadState('networkidle',{timeout:12000}).catch(()=>{});
 await sleep(6000); // Run300 likely uploaded during initial React shell hydration.
 const snap=async label=>{
  const data=await page.evaluate(()=>({
   text:document.body.innerText.slice(-1400),
   file_inputs:[...document.querySelectorAll('input[type=file]')].map((x,i)=>({index:i,html:x.outerHTML.slice(0,350),
     parent:x.parentElement?.parentElement?.innerText.slice(0,130),files:[...x.files||[]].map(f=>f.name)})),
   buttons:[...document.querySelectorAll('button')].filter(x=>/generate|single image|textured/i.test(x.innerText||''))
    .map(x=>({text:x.innerText.slice(0,90),disabled:x.disabled,html:x.outerHTML.slice(0,250)})),
   status:(document.body.innerText.match(/(?:Connecting|Ready|Disconnected|queued|GPU busy|offline)/gi)||[]).slice(0,8)
  }));
  event(label,data);return data;
 };
 await snap('hydrated-initial');
 const tab=page.getByRole('button',{name:/single image/i});
 if(await tab.count())await tab.first().click().catch(()=>{});
 const inputs=page.locator('input[type="file"]');
 const count=await inputs.count();event('input-count',{count});
 if(count===0)throw Error('no real image upload control');
 let recognized=false;
 for(let i=0;i<Math.min(count,6);i++){
  await inputs.nth(i).setInputFiles(INPUT);
  await sleep(1800);
  await snap('after-input-'+i);
  await page.screenshot({path:`${OUT}/01-file-input-${i}.png`,fullPage:true}).catch(()=>{});
  const generate=page.getByRole('button',{name:/generate textured 3d/i});
  if(await generate.count()&&await generate.first().isEnabled()){
   recognized=true;event('recognized-upload',{input_index:i});break;
  }
  await sleep(4500);
  if(await generate.count()&&await generate.first().isEnabled()){
   recognized=true;event('recognized-upload-delayed',{input_index:i});break;
  }
 }
 if(!recognized)throw Error('Upload did not hydrate into enabled Generate button; collected per-input DOM/screenshots');
 report.provider_ready=true;
 const go=page.getByRole('button',{name:/generate textured 3d/i}).first();
 const buttonText=await go.innerText();
 if(!/textured/i.test(buttonText))throw Error('not textured output mode');
 const bodyBefore=(await page.locator('body').innerText()).toLowerCase();
 if(/payment required|not enough credits|buy credits|quota exceeded/i.test(bodyBefore))throw Error('payment or quota barrier');
 await page.screenshot({path:OUT+'/02-before-generation.png',fullPage:true});
 await go.click();report.normal_free_submissions=1;
 event('normal-free-textured-generation-clicked',{buttonText});
 for(let step=0;step<90;step++){
  await sleep(4000);
  if(report.native_glb)break;
  const t=await page.locator('body').innerText().catch(()=>''),tl=t.toLowerCase();
  if(/processing limit reached|not enough credits|payment required|quota exceeded|rate limit|gpu unavailable/i.test(tl)){
   event('provider-quota-or-backend-block',{tail:t.slice(-700)});break;
  }
  if(step%10===0)event('generation-poll',{elapsed_seconds:(step+1)*4,tail:t.slice(-350)});
  if(/download glb/i.test(t)){
   const dl=page.getByRole('button',{name:/download.*glb/i}).first();
   if(await dl.count()&&await dl.isVisible())await dl.click({timeout:2000}).catch(()=>{});
  }
 }
 await Promise.allSettled(pending);
 await page.screenshot({path:OUT+'/03-result.png',fullPage:true}).catch(()=>{});
 event('final-body',{tail:(await page.locator('body').innerText().catch(()=>'')).slice(-1800)});
}catch(e){report.issues.push(String(e).slice(0,1000));}
finally{
 try{await Promise.allSettled(pending)}catch{}
 try{await browser?.close()}catch{}
 report.final=report.native_glb?'REAL_NATIVE_3D_CAPTURED_PENDING_ART_RIGHTS_PHONE_NO_RELEASE':
  'NO_NATIVE_3D_CAPTURED_ART_RIGHTS_PHONE_HOLD_NO_RELEASE';
 fs.writeFileSync(OUT+'/run301_diagnostic.json',JSON.stringify(report,null,2));
 console.log(JSON.stringify({final:report.final,source_sha256:report.source_sha256,
  submissions:report.normal_free_submissions,model:report.native_glb,
  issues:report.issues,events:report.events.map(e=>({phase:e.phase,status:e.status,tail:e.text?.slice(-160)}))},null,2));
}
