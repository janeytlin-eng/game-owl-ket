#!/usr/bin/env node
/** Run310 independently attempts one normal, free, unauthenticated, non-CAPTCHA
 * image-to-textured-3D flow on Paint3D. No payment, account, credit bypass, or release.
 * Source: #172 v3 repository original rightmost age-unknown cream mesoptile.
 * This script treats browser response, 3D decoding and visual art as SEPARATE gates.
 */
import fs from 'node:fs';
import crypto from 'node:crypto';
import {chromium} from 'playwright-core';

const ROOT='owl172-run310-evidence';
const SRC='owl172-rightmost-mesoptile-source.png';
const EXPECT='6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77';
const URL='https://paint-3d.dev/';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const d=ROOT+'/paint-3d-dev';
fs.mkdirSync(d,{recursive:true});
const report={run:310,utc_start:new Date().toISOString(),site:URL,
  true_reference_sha:null,loaded_http:null,provider_input_accepted:false,
  normal_free_generate_clicked:false,submitted_at:null,
  native_glb:null,webgl2_tech_test:false,art_approved:false,rights_cleared:false,
  physical_phone_verified:false,additional_paid_usd:0,account_created:false,
  captcha_bypassed:false,release_allowed:false,events:[],errors:[]};
const log=(kind,data={})=>{
  const item={utc:new Date().toISOString(),kind,...data};
  report.events.push(item);console.log(JSON.stringify(item));
};
const STOP=/captcha|turnstile|verify you are human|cloudflare challenge|security verification|buy credits|purchase credits|payment required|credit card|subscribe|upgrade|sign in to generate|log in to generate|quota exhausted|insufficient credits/i;
let browser;const jobs=[];let generationSubmitted=false;
function inspectGLB(b){
 if(b.length<80||b.length>70000000||b.toString('ascii',0,4)!=='glTF')throw Error('No glTF magic');
 const ver=b.readUInt32LE(4),len=b.readUInt32LE(8),jsonLen=b.readUInt32LE(12);
 if(ver!==2||len!==b.length||jsonLen>2000000||b.toString('ascii',16,20)!=='JSON')throw Error('Invalid GLB header or JSON');
 const doc=JSON.parse(b.toString('utf8',20,20+jsonLen));
 const prims=(doc.meshes||[]).flatMap(m=>m.primitives||[]).filter(p=>p.attributes?.POSITION!==undefined);
 if(!prims.length)throw Error('No position-bearing native geometry');
 return {mesh_count:doc.meshes?.length||0,primitives:prims.length,
    images:doc.images?.length||0,textures:doc.textures?.length||0,
    materials:doc.materials?.length||0,buffer_views:doc.bufferViews?.length||0};
}
function captureGLB(b,url,how){
 if(!generationSubmitted||report.native_glb)return;
 try{
  const stats=inspectGLB(b);
  const path=d+'/native-UNAPPROVED-source.glb';
  fs.writeFileSync(path,b);
  report.native_glb={path,bytes:b.length,sha256:sha(b),source_url:String(url).slice(0,300),how,...stats};
  log('REAL_NATIVE_GLB_CAPTURED_BUT_ART_AND_RIGHTS_PENDING',report.native_glb);
 }catch(e){log('rejected_candidate_binary',{url:String(url).slice(0,180),reason:String(e).slice(0,200)})}
}
async function snapshot(page,name){
 const out={date:new Date().toISOString(),url:page.url(),title:await page.title().catch(()=>''),
    frames:[]};
 for(const [idx,frame] of page.frames().entries()){
  try{
   out.frames.push(await frame.evaluate((idx)=>({
    idx,url:location.href,title:document.title,body:document.body?.innerText?.slice(0,8000)||'',
    file_inputs:[...document.querySelectorAll('input[type=file]')].map((e,i)=>({
      i,accept:e.accept,files:[...e.files||[]].map(f=>f.name),outer:e.outerHTML.slice(0,400)})),
    buttons:[...document.querySelectorAll('button,[role=button]')].slice(0,100)
      .map((e,i)=>({i,text:(e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,160),
        disabled:e.disabled||e.getAttribute('aria-disabled')==='true',outer:e.outerHTML.slice(0,250)})),
    image_count:document.querySelectorAll('img').length,
    canvas_count:document.querySelectorAll('canvas').length,
    links:[...document.querySelectorAll('a[download],a[href*=glb]')].slice(0,12).map(a=>({href:a.href,text:a.innerText.slice(0,90)}))
   }),idx));
  }catch(e){out.frames.push({idx,url:frame.url(),error:String(e).slice(0,200)})}
 }
 fs.writeFileSync(d+'/'+name+'.json',JSON.stringify(out,null,2));
 await page.screenshot({path:d+'/'+name+'.png',fullPage:true,timeout:15000}).catch(e=>log('screenshot_error',{reason:String(e).slice(0,150)}));
 log('snapshot',{name,frames:out.frames.map(f=>({url:f.url,input_count:f.file_inputs?.length||0,
  button_count:f.buttons?.length||0,body_tail:f.body?.slice(-180)||''}))});
 return out;
}
async function main(){
 const b=fs.readFileSync(SRC);report.true_reference_sha=sha(b);
 if(report.true_reference_sha!==EXPECT)throw Error('Reference integrity mismatch; refusing a substituted owl');
 browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',
  headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--enable-webgl',
   '--ignore-gpu-blocklist','--use-gl=angle','--use-angle=swiftshader']});
 const page=await browser.newPage({viewport:{width:390,height:780},acceptDownloads:true});
 page.setDefaultTimeout(10000);
 page.on('pageerror',e=>log('javascript_exception',{message:String(e).slice(0,350)}));
 page.on('response',resp=>{
  const url=resp.url(),ct=resp.headers()['content-type']||'';
  if(!/\.glb(?:[?#]|$)|model\/gltf-binary|application\/octet-stream/i.test(url+' '+ct))return;
  jobs.push((async()=>{try{if(resp.ok())captureGLB(await resp.body(),url,'network-response')}
   catch(e){log('binary_response_error',{url:url.slice(0,200),error:String(e).slice(0,200)})}})());
 });
 page.on('download',download=>jobs.push((async()=>{
   try{const p=await download.path();if(p)captureGLB(fs.readFileSync(p),download.url(),'browser-download')}
   catch(e){log('binary_download_error',{error:String(e).slice(0,200)})}
 })()));
 const r=await page.goto(URL,{waitUntil:'domcontentloaded',timeout:65000});
 report.loaded_http=r?.status();log('navigation',{http:report.loaded_http,url:page.url()});
 await sleep(9500);
 let s=await snapshot(page,'01-hydrated');
 if(report.loaded_http!==200)throw Error('Provider HTTP '+report.loaded_http);
 if(s.frames.some(f=>STOP.test(f.body||'')))throw Error('Login, payment, CAPTCHA or quota gate; no bypass');
 const locations=[];
 for(const frame of page.frames()){
  const fsCount=await frame.locator('input[type=file]').count().catch(()=>0);
  for(let i=0;i<Math.min(fsCount,4);i++)locations.push({frame,i});
 }
 if(!locations.length)throw Error('No usable native upload input found after hydration, including subframes');
 let submittedFile=false;
 for(const loc of locations){
  try{
   await loc.frame.locator('input[type=file]').nth(loc.i).setInputFiles(SRC,{timeout:10000});
   await sleep(3500);
   s=await snapshot(page,'02-upload-frame-'+locations.indexOf(loc));
   const hasFilename=s.frames.some(f=>f.file_inputs?.some(v=>v.files.includes(SRC)));
   const generationButtonEnabled=s.frames.some(f=>f.buttons?.some(x=>
      /^(?:generate|create|start|make|convert|extract 3d)/i.test(x.text)&&!x.disabled&&!/pricing|credit|purchase|buy|subscription/i.test(x.text)));
   // React components sometimes clear their file input after parsing the image.
   if(hasFilename||generationButtonEnabled){
     submittedFile=true;report.provider_input_accepted=true;
     log('input_accepted',{filename_persists:hasFilename,generation_button_enabled:generationButtonEnabled});
     break;
   }
  }catch(e){log('upload_attempt_failed',{frame:loc.frame.url(),error:String(e).slice(0,300)})}
 }
 if(!submittedFile)throw Error('File selected but there is no evidence the provider accepted it');
 if(s.frames.some(f=>STOP.test(f.body||'')))throw Error('Provider authentication/payment/CAPTCHA shown after upload');
 // Choose only the actual form's FREE action and never a marketing or paid-action button.
 let candidate=null;
 for(const frame of page.frames()){
  const buttons=frame.locator('button');
  const n=Math.min(await buttons.count().catch(()=>0),100);
  for(let i=0;i<n;i++){
   const el=buttons.nth(i);
   const title=(await el.innerText().catch(()=>''))?.trim()||'';
   if(!/^(generate|create 3d|generate 3d model|generate my 3d model|convert image|extract 3d)/i.test(title))continue;
   if(/buy|pricing|credit|pay|premium|subscribe|upgrade|login|sign in/i.test(title))continue;
   if(!await el.isEnabled().catch(()=>false)||!await el.isVisible().catch(()=>false))continue;
   candidate={frame,index:i,title};break;
  }
  if(candidate)break;
 }
 if(!candidate)throw Error('No enabled genuinely free generation button visible, no submission');
 log('free_generate_action_found',{title:candidate.title,frame:candidate.frame.url()});
 generationSubmitted=true;
 await candidate.frame.locator('button').nth(candidate.index).click({timeout:10000});
 report.normal_free_generate_clicked=true;report.submitted_at=new Date().toISOString();
 await sleep(3000);await snapshot(page,'03-after-real-submit');
 for(let t=0;t<240&&!report.native_glb;t+=6){
  await sleep(6000);
  const bodies=await Promise.all(page.frames().map(f=>f.locator('body').innerText().catch(()=>'')));
  if(bodies.some(x=>STOP.test(x))){log('explicit_stop_gate',{tail:bodies.join(' ').slice(-700)});break}
  if(t%30===0)log('generation_observation',{seconds:t+6,tail:bodies.join(' ').slice(-380)});
  // Download only generated model; never consent to paid or account UI.
  if(t%18===0){
   for(const frame of page.frames()){
    const links=frame.locator('a[download],a[href*=".glb"]');
    if(await links.count().catch(()=>0))await links.first().click({timeout:2500}).catch(()=>{});
    const btn=frame.getByRole('button',{name:/download.*(glb|model)|extract glb/i});
    if(await btn.count().catch(()=>0))await btn.first().click({timeout:2500}).catch(()=>{});
   }
  }
 }
 await Promise.allSettled(jobs);
 await snapshot(page,'04-final');
}
try{await main()}
catch(e){report.errors.push(String(e).slice(0,1000));log('RUN310_BLOCKED_OR_FAILED',{error:String(e).slice(0,1000)})}
finally{
 await Promise.allSettled(jobs);
 await browser?.close().catch(()=>{});
 report.final=report.native_glb?'TRUE_GLTF_CAPTURED_ART_RIGHTS_UNTESTED_NO_RELEASE':
  'NO_NEW_NATIVE_MODEL_NO_RELEASE';
 report.utc_end=new Date().toISOString();
 fs.writeFileSync(d+'/report-NO_RELEASE.json',JSON.stringify(report,null,2));
 console.log('RUN310_FINAL',report.final);
}
