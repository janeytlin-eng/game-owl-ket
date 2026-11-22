#!/usr/bin/env node
/** Isolated two-provider, no-login, no-payment, no-CAPTCHA-bypass browser experiment.
 * Only original #172 v3 rightmost mesoptile from repository; GLB is NOT product art.
 * Site names are not evidence of official foundation-model ownership or license.
 */
import fs from 'node:fs';import crypto from 'node:crypto';
import {chromium} from 'playwright-core';
const ROOT='owl172-run305-evidence',SRC='target-owl172-isolated-WHITE.png';
const EXPECT='6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77';
const SITES=[{slug:'trellis2-dev',url:'https://trellis2.dev/'},
             {slug:'hunyuan3d-dev',url:'https://hunyuan3d.dev/'}];
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const gate=t=>/verify you are human|security verification|cloudflare challenge|captcha|turnstile|processing limit reached|quota exhausted|out of credits|buy credits|payment required|paid plan|sign in to generate|log in to generate|upgrade to pro|subscribe to generate/i.test(t);
fs.mkdirSync(ROOT,{recursive:true});
const report={run:305,utc:new Date().toISOString(),source:null,paid_usd:0,
 account_created:false,captcha_bypassed:false,art_approved:false,
 rights_cleared:false,physical_phone_tested:false,release_allowed:false,sites:[]};
function checkGLB(b){
 if(b.length<40||b.length>65000000||b.toString('ascii',0,4)!=='glTF'||
    b.readUInt32LE(4)!==2||b.readUInt32LE(8)!==b.length)throw Error('Not a valid native GLB header');
 const n=b.readUInt32LE(12);
 if(n<20||n>3000000||b.toString('ascii',16,20)!=='JSON'||n+20>b.length)
   throw Error('GLB JSON invalid');
 const j=JSON.parse(b.toString('utf8',20,20+n));
 const p=(j.meshes||[]).flatMap(m=>m.primitives||[]).filter(x=>x.attributes?.POSITION!==undefined);
 if(!p.length)throw Error('No actual mesh vertex POSITION');
 return {mesh_count:j.meshes?.length||0,primitives:p.length,textures:j.textures?.length||0,
         images:j.images?.length||0,materials:j.materials?.length||0};
}
async function test(site){
 const dir=ROOT+'/'+site.slug;fs.mkdirSync(dir,{recursive:true});
 const out={site:site.url,source_uploaded:false,generation_attempts:0,glb:null,
  http:null,events:[],errors:[],release_allowed:false};
 report.sites.push(out);
 const ev=(event,data={})=>out.events.push({event,utc:new Date().toISOString(),...data});
 let browser;const tasks=[];
 const save=(b,url,via)=>{try{
   const valid=checkGLB(b);if(out.glb)return;
   const f=dir+'/native-real-ART_NOT_APPROVED.glb';fs.writeFileSync(f,b);
   out.glb={file:f,sha256:sha(b),bytes:b.length,url,via,...valid};ev('native-glb-captured',out.glb);
  }catch(e){ev('invalid-glb-candidate',{url:String(url).slice(0,150),why:String(e).slice(0,160)})}};
 try{
  browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',
    headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--enable-webgl',
                      '--ignore-gpu-blocklist','--use-gl=angle','--use-angle=swiftshader']});
  const page=await browser.newPage({viewport:{width:390,height:780},acceptDownloads:true});
  page.setDefaultTimeout(11000);
  page.on('pageerror',e=>ev('pageerror',{message:String(e).slice(0,260)}));
  page.on('response',r=>{const u=r.url(),ct=r.headers()['content-type']||'';
    if(!/\.glb(?:[?#]|$)/i.test(u)&&!/model\/gltf-binary|application\/octet-stream/.test(ct))return;
    tasks.push((async()=>{try{if(r.ok())save(await r.body(),u,'network')}catch(e){ev('network-capture-error',{error:String(e).slice(0,240)})}})());
  });
  page.on('download',d=>tasks.push((async()=>{try{
    const p=await d.path();if(p)save(fs.readFileSync(p),d.url(),'download');
   }catch(e){ev('download-capture-error',{error:String(e).slice(0,240)})}})()));
  const snap=async(name)=>{
    const s=await page.evaluate(()=>({title:document.title,body:document.body.innerText.slice(0,6500),
      inputs:[...document.querySelectorAll('input[type=file]')].map((x,i)=>({i,names:[...x.files||[]].map(f=>f.name),accept:x.accept})),
      buttons:[...document.querySelectorAll('button')].slice(0,80).map((x,i)=>({i,text:x.innerText.slice(0,110),disabled:x.disabled})),
      links:[...document.querySelectorAll('a[download],a[href*=".glb"]')].slice(0,15).map(x=>({url:x.href,text:x.innerText.slice(0,50)}))}));
    fs.writeFileSync(dir+'/'+name+'.json',JSON.stringify(s,null,2));
    await page.screenshot({path:dir+'/'+name+'.png',fullPage:true}).catch(()=>{});
    ev(name,{inputs:s.inputs.length,buttons:s.buttons.length,tail:s.body.slice(-300)});
    return s;
  };
  const resp=await page.goto(site.url,{waitUntil:'domcontentloaded',timeout:60000});
  out.http=resp?.status();ev('http',{status:out.http});
  await sleep(6000);let s=await snap('01-loaded');
  if(out.http>=400)throw Error('Provider HTTP '+out.http);
  if(gate(s.body))throw Error('Captcha, quota, login or paywall; respected without bypass');
  if(!s.inputs.length)throw Error('No normal input[type=file] found after hydration');
  for(let i=0;i<Math.min(3,s.inputs.length);i++){
    await page.locator('input[type=file]').nth(i).setInputFiles(SRC);
    await sleep(2600);s=await snap('02-input-'+i);
    // React recreates/clears its hidden native input after reading the image.
    // The enabled live generation control AND rendered image preview are evidence.
    const persistent=s.inputs.some(f=>f.names.includes(SRC));
    const formEnabled=s.buttons.some(b=>/^GENERATE\s*Fast/i.test(b.text)&&!b.disabled);
    if(persistent||formEnabled){out.source_uploaded=true;
      ev('source-preview-accepted',{persistent_native_filename:persistent,form_enabled:formEnabled});break}
  }
  if(!out.source_uploaded)throw Error('Image not actually accepted in file input');
  if(gate(s.body))throw Error('Quota/login/challenge shown after actual file upload');
  let chosen=null;const buttons=page.locator('button');
  for(let i=0;i<Math.min(await buttons.count(),80);i++){
    const b=buttons.nth(i);const t=(await b.innerText().catch(()=>''))?.trim()||'';
    // Avoid the enabled hero navigation "Generate 3D Free"; choose actual submit button.
    if(!/^(GENERATE\s*Fast|Generate My 3D Model|Generate 3D Model)$/i.test(t))continue;
    if(/buy|credit|pay|premium|subscribe|pro/i.test(t))continue;
    if(!await b.isVisible().catch(()=>false)||!await b.isEnabled().catch(()=>false))continue;
    chosen={i,text:t.slice(0,110)};break;
  }
  if(!chosen)throw Error('No enabled free-generation button in live DOM');
  ev('free-button',{chosen});await buttons.nth(chosen.i).click();out.generation_attempts=1;
  await sleep(4000);s=await snap('03-after-click');
  for(let seconds=0;seconds<225&&!out.glb;seconds+=5){
    await sleep(5000);
    const text=await page.locator('body').innerText().catch(()=>'');
    if(gate(text)){ev('provider-quota-or-challenge',{tail:text.slice(-700)});break}
    if(seconds%30===0)ev('poll',{seconds:seconds+5,tail:text.slice(-300)});
    if(seconds%20===0){
      const a=page.locator('a[download],a[href*=".glb"]');
      if(await a.count())await a.first().click({timeout:2500}).catch(()=>{});
      const b=page.getByRole('button',{name:/download.*(glb|model)/i});
      if(await b.count())await b.first().click({timeout:2500}).catch(()=>{});
    }
  }
  await Promise.allSettled(tasks);await snap('04-final');
 }catch(e){out.errors.push(String(e).slice(0,1200))}
 finally{
   await Promise.allSettled(tasks);await browser?.close().catch(()=>{});
   out.final=out.glb?'REAL_NATIVE_GLB_BUT_NO_ART_OR_RIGHTS_APPROVAL':
    'NO_NEW_VERIFIED_NATIVE_GLB_NO_RELEASE';
   fs.writeFileSync(dir+'/diagnostic.json',JSON.stringify(out,null,2));
   console.log(JSON.stringify({site:site.slug,http:out.http,attempts:out.generation_attempts,
    uploaded:out.source_uploaded,glb:out.glb,errors:out.errors,final:out.final},null,2));
 }
}
try{
 if(!fs.existsSync(SRC))throw Error('Original target crop missing');
 report.source=sha(fs.readFileSync(SRC));
 if(report.source!==EXPECT)throw Error('Source image SHA mismatch: refusing substituted bird');
 for(const s of SITES)await test(s);
}catch(e){report.fatal=String(e)}
finally{
 report.final=report.sites.some(x=>x.glb)?'NATIVE_CAPTURED_ART_AND_RIGHTS_UNCLEARED_NO_RELEASE':'NO_NATIVE_GLB_NO_RELEASE';
 fs.writeFileSync(ROOT+'/run305-report.json',JSON.stringify(report,null,2));
 console.log('RUN305_FINAL',report.final);
}