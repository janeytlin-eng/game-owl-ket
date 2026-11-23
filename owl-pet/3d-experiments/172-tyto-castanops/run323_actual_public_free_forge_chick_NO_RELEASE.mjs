#!/usr/bin/env node
/** Run323: normal public UI of three.ws/forge; no auth, money, captcha, or hidden API use.
 * Target: exact #172 v3 rightmost mesoptile source. Research ONLY / NO_RELEASE.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {chromium} from 'playwright-core';
const OUT=path.resolve('owl172-run323-evidence');
const SRC=path.resolve('owl172-run295-evidence/young-isolated-white-background-input-NO_3D.png');
const EXPECT='6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77';
const URL='https://three.ws/forge';
fs.mkdirSync(OUT,{recursive:true});
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const report={run:323,date:new Date().toISOString(),target:'#172 Tyto castanops v3 rightmost cream mesoptile',
 source:null,provider:URL,kind:'actual public browser with ordinary UI',paid_usd:0,
 account_created:false,privacy_bypass:false,third_party_rights_verified:false,
 real_phone_tested:false,art_approved:false,release_allowed:false,
 generated_native_glb:null,steps:[],errors:[]};
const step=(action,more={})=>report.steps.push({at:new Date().toISOString(),action,...more});
const blocking=/sign in to (upload|generate)|login required|sign-in required|authentication required|no 3d engine|generator not configured|not connected|all processing slots are busy|out of credits|insufficient credits|payment required|upgrade (?:your|to)|captcha|verify you are human|zeroGPU quota|queue is full/i;
const failMsg=e=>report.errors.push(String(e).slice(0,1200));
let browser;let glbQueue=[];
function checkNative(buf){
 if(!Buffer.isBuffer(buf))buf=Buffer.from(buf);
 if(buf.length<1000||buf.length>65000000||buf.toString('ascii',0,4)!=='glTF'||buf.readUInt32LE(4)!==2
     ||buf.readUInt32LE(8)!==buf.length)throw Error('Native GLB header/version/length invalid');
 const len=buf.readUInt32LE(12);
 if(len<20||len+20>buf.length||buf.toString('ascii',16,20)!=='JSON')throw Error('Missing GLB JSON');
 const j=JSON.parse(buf.toString('utf8',20,20+len));
 const valid=(j.meshes||[]).flatMap(m=>m.primitives||[]).filter(p=>p.attributes?.POSITION!==undefined);
 if(!valid.length)throw Error('No actual mesh POSITION attributes');
 return {mesh_count:j.meshes.length,primitive_count:valid.length,texture_count:j.textures?.length||0,
  material_count:j.materials?.length||0,image_count:j.images?.length||0};
}
function saveGLB(buf,url,source){
 // A legitimate GLB from the website's marketing/demo is NOT a requested
 // juvenile generation. Gate capture on real normal-form submission.
 if(report.generation_attempts!==1 ||
    /robotexpressive|demo|samples?|examples?|landing|avatars?\//i.test(String(url))){
   step('passive-site-GLB-ignored-NOT-a-generated-chick',{url:String(url).slice(0,200),source});
   return;
 }
 if(report.generated_native_glb)return;
 try {
  const meta=checkNative(buf),p=path.join(OUT,'run323-public-free-NATIVE-RESEARCH-ART_UNAPPROVED.glb');
  fs.writeFileSync(p,buf);
  report.generated_native_glb={file:p,url,method:source,sha256:sha(buf),bytes:buf.length,...meta};
  step('native-glb-downloaded-and-header-verified',report.generated_native_glb);
 }catch(e){step('nonvalid-glb-candidate',{url:String(url).slice(0,200),why:String(e).slice(0,240)});}
}
async function snap(page,name){
 const s=await page.evaluate(()=>({
  title:document.title,url:location.href,text:(document.body?.innerText||'').slice(0,12000),
  buttons:[...document.querySelectorAll('button')].slice(0,120).map((e,i)=>({i,text:(e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,120),disabled:e.disabled})),
  selects:[...document.querySelectorAll('select')].map((e,i)=>({i,selected:e.value,options:[...e.options].map(o=>o.text).slice(0,30)})),
  files:[...document.querySelectorAll('input[type=file]')].map((e,i)=>({i,accept:e.accept,count:e.files.length,names:[...e.files].map(f=>f.name)})),
  pictures:[...document.querySelectorAll('img')].filter(e=>e.width>40&&e.height>40).slice(0,20).map(e=>({alt:e.alt,src:e.currentSrc.slice(0,140)}))
 }));
 fs.writeFileSync(path.join(OUT,name+'.json'),JSON.stringify(s,null,2));
 await page.screenshot({path:path.join(OUT,name+'.png'),fullPage:true,timeout:15000}).catch(e=>step('screenshot-error',{why:String(e).slice(0,180)}));
 step(name,{buttons:s.buttons.slice(0,20),files:s.files,tail:s.text.slice(-500)});
 return s;
}
try{
 if(!fs.existsSync(SRC)||sha(fs.readFileSync(SRC))!==EXPECT)throw Error('Exact reference SHA256 mismatch; stop');
 report.source={path:SRC,sha256:EXPECT,bytes:fs.statSync(SRC).size};
 browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',
  headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--enable-webgl','--ignore-gpu-blocklist',
    '--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader']});
 const page=await browser.newPage({viewport:{width:390,height:780},acceptDownloads:true,deviceScaleFactor:1});
 page.setDefaultTimeout(10000);
 page.on('pageerror',e=>step('pageerror',{message:String(e).slice(0,250)}));
 page.on('response',r=>{
  const u=r.url(),ct=r.headers()['content-type']||'';
  if(/\.glb(?:[?#]|$)|model\/gltf-binary/i.test(u+' '+ct)){
   glbQueue.push((async()=>{try{if(r.ok()){const b=await r.body();saveGLB(b,u,'normal-browser-response')}}catch(e){step('capture-error',{error:String(e).slice(0,250)})}})());
  }
 });
 page.on('download',d=>glbQueue.push((async()=>{
  try{const p=await d.path();if(p)saveGLB(fs.readFileSync(p),d.url(),'normal-browser-download')}
  catch(e){step('download-error',{error:String(e).slice(0,200)})}
 })()));
 const resp=await page.goto(URL,{waitUntil:'domcontentloaded',timeout:60000});
 report.http=resp?.status()||null;
 await page.waitForTimeout(7500);
 let s=await snap(page,'01-loaded');
 if(report.http>=400)throw Error('Free Forge HTTP '+report.http);
 if(/generator not configured|no 3d engine is reachable/i.test(s.text))throw Error('Provider explicitly says generator unconfigured');
 // Activate the normal "From photos" UI. Never open protected URLs or private APIs.
 let toggle=page.getByRole('button',{name:/From photos/i});
 if(await toggle.count()){
   step('photo-tab-before',{markup:(await toggle.first().evaluate(e=>e.outerHTML).catch(()=>'' )).slice(0,900)});
   await toggle.first().click();
   await page.waitForTimeout(1600);
   step('photo-tab-after',{markup:(await toggle.first().evaluate(e=>e.outerHTML).catch(()=>'' )).slice(0,900)});
 }
 s=await snap(page,'02-photo-ui');
 report.visible_form_state=s.text.slice(0,1300);
 if(/Describe the object to generate[\s\S]{0,200}Name one object/.test(s.text)){
   step('photo-tab-failed-to-switch',{visible_text:s.text.slice(0,900)});
   // do not set hidden photo inputs belonging to inactive components.
   throw Error('Public UI remained in DESCRIBE IT mode after From photos tab click');
 }
 if(!s.files.length)throw Error('No public normal image input in hydrated photo UI');
 // Select a free engine in normal public UI, if it has one.
 if(/TripoSG/i.test(s.text)){
  const option=page.getByText('TripoSG',{exact:true});
  if(await option.count() && await option.first().isVisible().catch(()=>false)){
   await option.first().click({timeout:3000}).catch(()=>{});
   step('tried-select-public-free-triposg');
  }
 }
 // Upload original approved source only, via ordinary visible file-input control.
 let put=false;
 for(let i=0;i<Math.min(s.files.length,3);i++){
  try{await page.locator('input[type=file]').nth(i).setInputFiles(SRC);put=true;step('ordinary-file-input-selected',{index:i});break}
  catch(e){step('file-input-failure',{index:i,why:String(e).slice(0,150)})}
 }
 if(!put)throw Error('Ordinary image file selection was not possible');
 await page.waitForTimeout(7000);
 s=await snap(page,'03-after-source-upload');
 step('upload-observed-state',{visible_text:s.text.slice(0,1800),trailing_buttons:s.buttons.slice(-15)});
 const hasPreview=s.files.some(x=>x.count>0)||s.pictures.some(x=>/blob:|data:image/i.test(x.src))||
  /\b1 of 1 views\b|\b1 of \d views\b|photo.*added|image.*uploaded|remove image/i.test(s.text);
 if(!hasPreview)throw Error('Upload not established: no accepted preview or retained filename; stop before generation');
 report.preview_verified=true;
 if(blocking.test(s.text)&&!/sign in.*your creations/i.test(s.text))throw Error('Visible free-provider auth/quota/payment gate; stop');
 // Ensure free provider is selected; do not click a paid/API-key generation lane.
 if(!/FREE no API key|Free to generate|Free\s*·\s*no sign-up/i.test(s.text))throw Error('No visible declaration of a selected free generation route');
 const candidates=s.buttons.filter(x=>/^(Generate|Forge)(?:\s|$)/i.test(x.text) &&!x.disabled
  &&!/credit|buy|pay|pro|subscription|upgrade|api key|retopo/i.test(x.text));
 if(!candidates.length)throw Error('No enabled safe free form-generation control found');
 let clicked=false;
 for(const c of candidates){
  const b=page.locator('button').nth(c.i);
  if(!await b.isVisible().catch(()=>false))continue;
  if(/hold \$THREE|billing|requires .*key/i.test(s.text.slice(Math.max(0,s.text.indexOf(c.text)-120),s.text.indexOf(c.text)+120)))continue;
  await b.click({timeout:7000});step('clicked-visible-free-generate-form',{button:c});clicked=true;report.generation_attempts=1;break;
 }
 if(!clicked)throw Error('No safe visible free action; generation not submitted');
 await page.waitForTimeout(4000);
 s=await snap(page,'04-after-submit');
 for(let elapsed=0;elapsed<250&&!report.generated_native_glb;elapsed+=10){
  await page.waitForTimeout(10000);
  const t=await page.locator('body').innerText().catch(()=>'');
  if(/generation failed|processing slots are busy|out of credits|payment required|sign in to generate|generator not configured/i.test(t)){
   step('provider-failure-or-auth-stopped',{elapsed,tail:t.slice(-900)});break;
  }
  if(elapsed%30===0)step('polling',{elapsed,tail:t.slice(-400)});
  // Public download controls only, not undocumented API endpoints.
  const a=page.locator('a[download],a[href*=".glb"]');
  if(await a.count())await a.first().click({timeout:2000}).catch(()=>{});
  const download=page.getByRole('button',{name:/download GLB|download.*model/i});
  if(await download.count())await download.first().click({timeout:1800}).catch(()=>{});
 }
 await Promise.allSettled(glbQueue);
 await snap(page,'05-final');
}catch(e){failMsg(e)}
finally{
 await Promise.allSettled(glbQueue);
 await browser?.close().catch(()=>{});
 report.status=report.generated_native_glb?'REAL_NATIVE_CAPTURED_PENDING_ALL_ART_AND_RIGHTS_APPROVAL':
 'NO_NEW_NATIVE_GLB_NO_RELEASE';
 fs.writeFileSync(path.join(OUT,'run323-browser-report.json'),JSON.stringify(report,null,2));
 fs.writeFileSync(path.join(OUT,'STRICT_NO_RELEASE.txt'),
  'Run323 is a research-only provider trial. NO product release: art/rights/physical-phone unverified, 251-species production untouched. No extra paid spend.\n');
 console.log(JSON.stringify(report,null,2));
}
