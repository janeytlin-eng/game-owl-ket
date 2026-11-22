#!/usr/bin/env node
/** Zero-payment real browser test of a DIFFERENT textured image-to-3D service.
 * No challenge bypass, account, paid plan, access token, fake screenshot or release.
 * Only a true GLB returned by normal free UI is eligible for three-camera QA.
 */
import fs from 'node:fs';import crypto from 'node:crypto';
import {chromium} from 'playwright-core';
const OUT='owl172-run304-evidence';const SRC='target-owl172-isolated-WHITE.png';
const PAGE='https://hi3d.pro/en';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
fs.mkdirSync(OUT,{recursive:true});
const report={run:'304',utc:new Date().toISOString(),provider:PAGE,source_sha256:null,
  native_glb:null,attempts:0,paid_usd:0,captcha_bypassed:false,
  art_approved:false,rights_cleared:false,physical_phone_tested:false,
  release_allowed:false,events:[],issues:[]};
const ev=(phase,data={})=>report.events.push({phase,time:new Date().toISOString(),...data});
function validate(data,url){
 if(data.length<40||data.toString('ascii',0,4)!=='glTF'||data.readUInt32LE(4)!==2||data.readUInt32LE(8)!==data.length)
   throw Error('not a native glTF 2 GLB');
 const n=data.readUInt32LE(12),magic=data.toString('ascii',16,20);
 if(magic!=='JSON'||n>10000000||n+20>data.length)throw Error('bad GLB JSON');
 const j=JSON.parse(data.toString('utf8',20,20+n));
 const actual=(j.meshes||[]).flatMap(m=>m.primitives||[]).filter(p=>p.attributes?.POSITION!==undefined);
 if(!actual.length)throw Error('no geometry POSITION in GLB');
 if(!report.native_glb){
  const file=OUT+'/run304-hi3d-native-real-NOT_APPROVED.glb';fs.writeFileSync(file,data);
  report.native_glb={file,bytes:data.length,sha256:sha(data),url,mesh_count:j.meshes?.length||0,
    primitive_count:actual.length,images:j.images?.length||0,textures:j.textures?.length||0,
    materials:j.materials?.length||0};
 }
}
let browser;const pending=[];
try{
 if(!fs.existsSync(SRC))throw Error('original rightmost chick crop missing');
 report.source_sha256=sha(fs.readFileSync(SRC));
 if(report.source_sha256!=='6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77')
   throw Error('actual target reference checksum mismatch');
 browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',
  headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--enable-webgl',
  '--ignore-gpu-blocklist','--use-gl=angle','--use-angle=swiftshader']});
 const page=await browser.newPage({viewport:{width:390,height:780},deviceScaleFactor:1,acceptDownloads:true});
 page.setDefaultTimeout(12000);
 page.on('pageerror',e=>ev('page-error',{message:String(e).slice(0,350)}));
 page.on('response',res=>{
  const url=res.url(),ctype=res.headers()['content-type']||'';
  if(!(/\.glb([?#]|$)/i.test(url)||/model\/gltf-binary/i.test(ctype)))return;
  pending.push((async()=>{try{if(res.ok())validate(await res.body(),url)}catch(e){ev('glb-rejected',{error:String(e).slice(0,200)})}})());
 });
 page.on('download',d=>pending.push((async()=>{
  try{const p=await d.path();if(p)validate(fs.readFileSync(p),d.url())}
  catch(e){ev('download-rejected',{error:String(e).slice(0,300)})}})()));
 const response=await page.goto(PAGE,{waitUntil:'domcontentloaded',timeout:60000});
 report.http=response?.status();ev('page-http',{http:report.http});
 await sleep(5000);
 const snapshot=async label=>{
  const snap=await page.evaluate(()=>({
    title:document.title,body:document.body.innerText.slice(0,4800),
    inputs:[...document.querySelectorAll('input[type=file]')].map((x,i)=>({
      i,accept:x.accept,files:[...x.files||[]].map(f=>f.name),html:x.outerHTML.slice(0,300)})),
    buttons:[...document.querySelectorAll('button')].slice(0,45).map(x=>({
      text:x.innerText.slice(0,100),disabled:x.disabled,html:x.outerHTML.slice(0,220)}))
  }));
  fs.writeFileSync(OUT+'/'+label+'.json',JSON.stringify(snap,null,2));
  ev(label,{inputs:snap.inputs.length,buttons:snap.buttons.length,body_tail:snap.body.slice(-500)});
  await page.screenshot({path:OUT+'/'+label+'.png',fullPage:true}).catch(()=>{});
  return snap;
 };
 let snap=await snapshot('01-initial');
 if(/turnstile|captcha|verify you are human/i.test(snap.body))throw Error('captcha human challenge; no bypass');
 const inputs=page.locator('input[type=file]');
 if(!await inputs.count())throw Error('no real HTML file input after hydration');
 const n=Math.min(await inputs.count(),3);
 let target=-1;
 for(let i=0;i<n;i++){
   await inputs.nth(i).setInputFiles(SRC);await sleep(1700);
   snap=await snapshot('02-upload-'+i);
   if(snap.inputs.some(x=>x.files.includes(SRC))){target=i;break;}
 }
 if(target<0)throw Error('source never recognized by browser input');
 const body=snap.body.toLowerCase();
 if(/service unavailable|gpu offline|out of credits|no credits|processing limit reached|buy credits|payment required|rate limit|server busy|quota exhausted/i.test(body))
   throw Error('service quota or billing barrier before generating');
 if(/turnstile|captcha|verify you are human/i.test(body))throw Error('captcha human challenge; no bypass');
 const names=[/create 3d for free/i,/generate 3d/i,/generate/i];
 let clicked=false;
 for(const pat of names){
   const btn=page.getByRole('button',{name:pat});
   if(await btn.count()){
    for(let i=0;i<Math.min(await btn.count(),4);i++){
      const b=btn.nth(i);
      if(!(await b.isVisible().catch(()=>false))||!(await b.isEnabled().catch(()=>false)))continue;
      ev('generate-button-found',{text:(await b.innerText()).slice(0,100)});
      await b.click();clicked=true;break;
    }
   }
   if(clicked)break;
 }
 if(!clicked)throw Error('No ENABLED ordinary free 3D generation button after file upload');
 report.attempts=1;
 await sleep(4000);snap=await snapshot('03-after-click');
 for(let t=0;t<55;t++){
  if(report.native_glb)break;
  await sleep(4000);
  const text=await page.locator('body').innerText().catch(()=>'');
  if(/processing limit reached|payment required|buy credits|quota exhausted|captcha|verify you are human|out of credits/i.test(text.toLowerCase())){
   ev('provider-quota-or-challenge',{tail:text.slice(-550)});break;
  }
  if(t%10===0)ev('poll',{elapsed_sec:(t+1)*4,tail:text.slice(-400)});
  const links=page.locator('a[download],a[href*=".glb"],button:has-text("Download GLB")');
  if(await links.count() && !report.native_glb){
   await links.first().click({timeout:2500}).catch(()=>{});
  }
 }
 await Promise.allSettled(pending);
 await snapshot('04-final');
}catch(e){report.issues.push(String(e).slice(0,1000));}
finally{
 await Promise.allSettled(pending);await browser?.close().catch(()=>{});
 report.final=report.native_glb?'ACTUAL_NATIVE_MODEL_PENDING_VISUAL_AND_LICENSE_NO_RELEASE':'NO_REAL_GLTF2_CAPTURED_NO_RELEASE';
 fs.writeFileSync(OUT+'/run304_diagnostic.json',JSON.stringify(report,null,2));
 console.log(JSON.stringify({run:report.run,final:report.final,http:report.http,
  source_sha256:report.source_sha256,attempts:report.attempts,model:report.native_glb,
  issues:report.issues,events:report.events.map(e=>({phase:e.phase,body_tail:e.body_tail?.slice(-180)}))},null,2));
}
