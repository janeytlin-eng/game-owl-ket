#!/usr/bin/env node
// Run306 independent actual-browser research; NO RELEASE, NO PAYMENT, NO CAPTCHA BYPASS.
import fs from 'node:fs';
import crypto from 'node:crypto';
import { chromium } from 'playwright-core';
const ROOT='owl172-run306-evidence', SRC='target-owl172-isolated-WHITE.png';
const EXPECT='6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77';
const sleep=(ms)=>new Promise(r=>setTimeout(r,ms));
const sha=(b)=>crypto.createHash('sha256').update(b).digest('hex');
const sites=[{id:'3dai-textured',url:'https://3dai.dev/en',mode:'textured'},
             {id:'image-to-3d-workbench',url:'https://image-to-3d.app/',mode:'free-trial'}];
fs.mkdirSync(ROOT,{recursive:true});
const report={run:'306',date_utc:new Date().toISOString(),input_sha256:null,
  paid_usd:0,authenticated:false,captcha_bypass:false,models:[],sites:[],
  art_approved:false,rights_cleared:false,physical_phone_tested:false,release_allowed:false};
function parseGLB(b) {
 if(b.length<40||b.length>70e6||b.toString('ascii',0,4)!=='glTF'||b.readUInt32LE(4)!==2||b.readUInt32LE(8)!==b.length)throw Error('invalid GLB header');
 const n=b.readUInt32LE(12);if(n<20||n>5e6||n+20>b.length||b.toString('ascii',16,20)!=='JSON')throw Error('invalid JSON GLB chunk');
 const j=JSON.parse(b.toString('utf8',20,20+n));
 const pos=(j.meshes||[]).flatMap(m=>m.primitives||[]).filter(p=>p.attributes?.POSITION!==undefined);
 if(!pos.length)throw Error('GLB has no vertex positions');
 return {meshes:j.meshes?.length||0,primitives:pos.length,images:j.images?.length||0,textures:j.textures?.length||0,materials:j.materials?.length||0};
}
function disallowed(t){return /verify you are human|captcha|turnstile|security verification|cloudflare challenge|payment required|buy credits|purchase credits|credit card|sign in to generate|log in to generate|processing limit reached|quota exceeded|upgrade plan|out of credits/i.test(t)}
async function probe(site) {
 const dir=ROOT+'/'+site.id;fs.mkdirSync(dir,{recursive:true});
 const info={site:site.url,http:null,source_uploaded:false,submissions:0,glb:null,events:[],errors:[],status:'NOT_GENERATED'};
 report.sites.push(info);
 const ev=(phase,extra={})=>info.events.push({utc:new Date().toISOString(),phase,...extra});
 let browser, pending=[];
 const save=(b,where,via)=>{try{const stats=parseGLB(b);if(info.glb)return;const path=dir+'/generated-native-unapproved.glb';fs.writeFileSync(path,b);
   info.glb={path,bytes:b.length,sha256:sha(b),where,via,...stats};report.models.push(info.glb);ev('glb-captured',info.glb);
 }catch(e){ev('non-glb-response',{why:String(e).slice(0,180),where:String(where).slice(0,200)})}};
 try {
   browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--enable-webgl','--ignore-gpu-blocklist','--use-gl=angle','--use-angle=swiftshader']});
   const page=await browser.newPage({viewport:{width:390,height:780},acceptDownloads:true});
   page.setDefaultTimeout(10000);
   page.on('pageerror',e=>ev('page-error',{error:String(e).slice(0,260)}));
   page.on('response',res=>{const u=res.url(),type=res.headers()['content-type']||'';
      if(!/\.glb(?:[?#]|$)/i.test(u)&&!/model\/gltf-binary|application\/octet-stream/i.test(type))return;
      pending.push((async()=>{try{if(res.ok())save(await res.body(),u,'network')}catch(e){ev('capture-error',{error:String(e).slice(0,200)})}})());});
   page.on('download',d=>pending.push((async()=>{try{const p=await d.path();if(p)save(fs.readFileSync(p),d.url(),'download')}catch(e){ev('download-error',{error:String(e).slice(0,200)})}})()));
   async function snapshot(tag) {
     const dom=await page.evaluate(()=>({
       title:document.title,body:document.body.innerText.slice(0,13000),
       inputs:[...document.querySelectorAll('input[type=file]')].map((x,i)=>({i,accept:x.accept,files:[...x.files||[]].map(f=>f.name)})),
       buttons:[...document.querySelectorAll('button')].slice(0,100).map((x,i)=>({i,text:x.innerText.slice(0,180),disabled:x.disabled})),
       selects:[...document.querySelectorAll('select')].map((x,i)=>({i,value:x.value,options:[...x.options].map(o=>({text:o.text,value:o.value}))}))
     }));
     fs.writeFileSync(dir+'/'+tag+'.json',JSON.stringify(dom,null,2));
     await page.screenshot({path:dir+'/'+tag+'.png',fullPage:true}).catch(()=>{});
     ev(tag,{inputs:dom.inputs.length,buttons:dom.buttons.length,bodyTail:dom.body.slice(-420)});
     return dom;
   }
   const nav=await page.goto(site.url,{waitUntil:'domcontentloaded',timeout:60000});
   info.http=nav?.status()??null;await sleep(8500);
   let s=await snapshot('01-hydrated');
   if(info.http!==200)throw Error('HTTP '+info.http);
   if(disallowed(s.body))throw Error('Visible anti-bot/payment/auth/quota gate; respecting it');
   if(site.mode==='textured'){
     // Only run if Textured is explicitly available. GPU online != texture server ready.
     const bad=/texture service (starting|unavailable)|textured mode (is )?unavailable|texture backend (offline|unavailable)/i.test(s.body);
     const textured=s.buttons.filter(b=>/generate textured 3d/i.test(b.text));
     ev('texture-backend-check',{bad,matching_buttons:textured});
     if(bad||!textured.length||textured.every(b=>b.disabled))throw Error('Textured backend not actually ready');
   }
   if(!s.inputs.length)throw Error('No hydrated file upload field');
   for(let i=0;i<Math.min(4,s.inputs.length);i++){
     await page.locator('input[type=file]').nth(i).setInputFiles(SRC);
     await sleep(2200);s=await snapshot('02-upload-'+i);
     const file=s.inputs.some(x=>x.files.includes(SRC));
     const sourcePreview=await page.evaluate(()=>[...document.images].some(x=>x.naturalWidth>100&&x.naturalHeight>100));
     const suitable=s.buttons.some(b=>site.mode==='textured'?(/generate textured 3d/i.test(b.text)&&!b.disabled):(/generate.*(3d|model)/i.test(b.text)&&!b.disabled));
     if(file||(sourcePreview&&suitable)){info.source_uploaded=true;ev('upload-confirmed',{file,sourcePreview,suitable});break;}
   }
   if(!info.source_uploaded)throw Error('No reliable accepted-source evidence');
   if(disallowed(s.body))throw Error('Auth, quota, CAPTCHA or payment gate after source');
   if(site.mode==='textured'&&(/texture service (starting|unavailable)|textured mode (is )?unavailable/i.test(s.body)))throw Error('Texture backend unavailable after upload');
   let chosen=null;
   for(const b of s.buttons){
      const text=b.text.trim();
      const matches=site.mode==='textured'?/^generate textured 3d$/i.test(text):/^(generate 3d model|generate model|generate 3d)$/i.test(text);
      if(!matches||b.disabled||/purchase|subscribe|buy|pro only|pay|sign in|log in/i.test(text))continue;
      chosen=b;break;
   }
   if(!chosen)throw Error('No enabled ordinary FREE generate-submit button (not hero CTA)');
   // A visible credit/payment requirement is a hard stop.
   if(/remaining:\s*0\s*credits|credits:\s*0\b/i.test(s.body)&&site.mode==='free-trial')throw Error('Provider reports zero remaining credits');
   ev('normal-free-submit-selection',{button:chosen});
   const button=page.locator('button').nth(chosen.i);
   if(!await button.isVisible()||!await button.isEnabled())throw Error('Button no longer available');
   await button.click();info.submissions=1;
   await sleep(4200);await snapshot('03-after-click');
   for(let elapsed=5;elapsed<=245&&!info.glb;elapsed+=5){
      await sleep(5000);
      const body=await page.locator('body').innerText().catch(()=>'');
      if(disallowed(body)){ev('provider-gate-after-submit',{bodyTail:body.slice(-800)});break;}
      if(/generation failed|all processing slots are busy|server error|gpu unavailable|service unavailable|high demand right now/i.test(body)){ev('provider-failed',{bodyTail:body.slice(-800)});break;}
      if(elapsed%30===5)ev('poll',{elapsed,bodyTail:body.slice(-250)});
      if(elapsed%20===5){
         const links=page.locator('a[download],a[href*=".glb"]');
         if(await links.count())await links.first().click({timeout:2000}).catch(()=>{});
         const buttons=page.getByRole('button',{name:/download.*(glb|3d model)/i});
         if(await buttons.count())await buttons.first().click({timeout:2000}).catch(()=>{});
      }
   }
   await Promise.allSettled(pending);await snapshot('04-final');
 }catch(e){info.errors.push(String(e).slice(0,1500));}
 finally{
   await Promise.allSettled(pending);await browser?.close().catch(()=>{});
   info.status=info.glb?'ACTUAL_GLB_UNREVIEWED_NO_RELEASE':'NO_NATIVE_GLB_NO_RELEASE';
   fs.writeFileSync(dir+'/diagnostic.json',JSON.stringify(info,null,2));
   console.log(JSON.stringify({site:site.id,http:info.http,uploaded:info.source_uploaded,submissions:info.submissions,status:info.status,errors:info.errors,glb:info.glb},null,2));
 }
}
try{
 if(!fs.existsSync(SRC))throw Error('source missing');
 report.input_sha256=sha(fs.readFileSync(SRC));if(report.input_sha256!==EXPECT)throw Error('source SHA mismatch');
 for(const site of sites)await probe(site);
}catch(e){report.fatal=String(e)}
finally{
 report.status=report.models.length?'NATIVE_GLB_CAPTURED_ART_RIGHTS_MOBILE_HOLD_NO_RELEASE':'NO_NATIVE_GLB_NO_RELEASE';
 fs.writeFileSync(ROOT+'/run306-report.json',JSON.stringify(report,null,2));
 console.log('RUN306_FINAL',report.status);
}