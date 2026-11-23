#!/usr/bin/env node
/**
 * #172 Run310: real public, no-payment artist-made juvenile sculpt source access.
 * NEVER use bypass methods, tokens, new accounts, paywalls or false GLB promotions.
 * Nothing here can approve art, rights, or mobile WebGL; all files quarantined.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { chromium } from 'playwright-core';

const out=path.resolve('owl172-run310-evidence');
fs.mkdirSync(out,{recursive:true});
const sources=[
 {id:'cgtrader-baby-owl-sculpt',url:'https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt',kind:'free_artist_native',maxBytes:80000000},
 {id:'cgtrader-barn-owl-kid',url:'https://www.cgtrader.com/free-3d-models/character/man/baby-owl-animated-black',kind:'free_animated_young_tyto',maxBytes:150000000},
 {id:'booth-barn-owl-chick',url:'https://booth.pm/ja/items/6643539',kind:'free_vrchat_native_license_unreviewed',maxBytes:20000000},
 {id:'gaitkit-eaglet',url:'https://gaitkit.com/asset/eaglet',kind:'wrong_taxon_anatomy_only',maxBytes:20000000},
 {id:'tripo-public-owlet',url:'https://studio.tripo3d.ai/3d-model/owl-chick-very-big-eyes-f385f601-4c72-4be8-949a-a4c460451eb8',kind:'public_preview_not_assumed_download',maxBytes:25000000}
];
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const report={
 run:310,utc:new Date().toISOString(),target:'original #172 v3 far-right cream Tyto castanops age-unknown mesoptile',
 user_restrictions:'NO PAYMENT, NO LOGIN CREATION, NO AUTH OR CAPTCHA BYPASS, NO PRODUCTION CHANGES',
 no_release:true,sources:[]
};
let browser;
try{
 browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
 for(const s of sources){
   const item={id:s.id,url:s.url,kind:s.kind,downloaded_native_asset:false,asset_licence_independently_cleared:false,art_approved:false};
   report.sources.push(item);
   let ctx,page;
   try{
     ctx=await browser.newContext({viewport:{width:1100,height:800},acceptDownloads:true});
     page=await ctx.newPage();
     const errors=[];
     page.on('pageerror',e=>errors.push('pageerror:'+String(e).slice(0,180)));
     page.on('console',m=>{if(m.type()==='error'&&errors.length<5)errors.push(m.text().slice(0,180));});
     const response=await page.goto(s.url,{waitUntil:'domcontentloaded',timeout:36000});
     item.http_status=response?.status()??null;
     await page.waitForTimeout(4000);
     item.final_url=page.url();item.title=(await page.title()).slice(0,160);
     const body=(await page.locator('body').innerText({timeout:10000}).catch(()=>''))||'';
     item.visible_text_excerpt=body.replace(/\s+/g,' ').slice(0,1400);
     const lower=body.toLowerCase(),lowerurl=page.url().toLowerCase();
     item.sign_in_gate=/sign in to download|log in to download|login to download|sign in|create account/.test(lower)||/sign_in|login/.test(lowerurl);
     item.pro_gate=(s.id==='gaitkit-eaglet'&&/pro download/i.test(body));
     item.catalogue_free_label=/free|無料|¥\s*0/.test(lower);
     item.claimed_young_stage=/baby|chick|雛|ヒナ|kid|sculpt/.test(lower);
     item.explicit_license_markers=(body.match(/royalty.free|vn3|no ai|commercial use|cc0/ig)||[]).slice(0,10);
     const candidates=await page.locator('a,button').evaluateAll(els=>els.map(el=>({
        tag:el.tagName,txt:(el.innerText||el.getAttribute('aria-label')||'').trim().slice(0,130),
        href:el.tagName==='A'?(el.href||''):null
       })).filter(x=>/download|ダウンロード|free|pro|login|sign in|ログイン/i.test(x.txt)).slice(0,24));
     item.visible_download_controls=candidates;
     await page.screenshot({path:path.join(out,s.id+'-public-page.png'),fullPage:false}).catch(()=>{});
     if(s.id==='gaitkit-eaglet'){
       item.access_status=item.pro_gate?'PRO_PAYWALL_NOT_ATTEMPTED':'COST_NOT_VERIFIED';
       item.anatomical_caveat='GOLDEN EAGLE CHICK with yellow cere, no heart-shaped Tyto face; not a candidate for release';
     } else if(s.id==='tripo-public-owlet'){
       item.access_status='PUBLIC_PREVIEW_ONLY_MODEL_RIGHTS_UNKNOWN';
     } else {
       // Real click through a public FREE download control, never buy/subscribe/login.
       const free=(await page.locator('a,button').all()).filter(()=>true);
       let clicked=false;
       for(const el of free.slice(0,120)){
         const label=(await el.innerText().catch(()=>''))?.trim().replace(/\s+/g,' ').slice(0,90)||'';
         const exact=s.id==='booth-barn-owl-chick'
          ? /無料ダウンロード/i.test(label)
          : /^(?:free\s+download|download\s+free|download)$/i.test(label);
         if(!exact || /subscribe|upgrade|purchase|pro/i.test(label)) continue;
         const href=await el.getAttribute('href').catch(()=>null);
         if(href&&/(?:login|sign.?in|subscribe|checkout)/i.test(href))continue;
         item.clicked_free_control=label;clicked=true;
         try{
           const before=page.url();
           const waitDL=page.waitForEvent('download',{timeout:9000}).catch(()=>null);
           await el.click({timeout:9000});
           const dl=await waitDL;
           if(dl){
             const fn=(dl.suggestedFilename()||'candidate.bin').replace(/[^a-zA-Z0-9._-]/g,'_');
             const f=path.join(out,s.id+'-'+fn);
             await dl.saveAs(f);
             const st=fs.statSync(f);
             if(st.size>s.maxBytes){fs.unlinkSync(f);throw Error('BINARY_EXCEEDS_BOUNDED_RESEARCH_LIMIT');}
             const bytes=fs.readFileSync(f);
             item.download_name=fn;item.download_bytes=bytes.length;item.download_sha256=sha(bytes);
             item.download_magic_first8=bytes.subarray(0,8).toString('hex');
             item.downloaded_native_asset=(bytes.subarray(0,4).toString()==='glTF'||/\.zip$|\.blend$|\.obj$|\.fbx$/i.test(fn))&&st.size>1000;
           } else {
             await page.waitForTimeout(2000);
             item.after_click_url=page.url();
             const text=await page.locator('body').innerText().catch(()=>'');
             item.after_click_sign_in=/sign in|sign up|login|log in|ログイン|アカウント/.test(text.toLowerCase())||/sign_in|login/i.test(page.url());
             item.after_click_preview=text.replace(/\s+/g,' ').slice(0,900);
           }
           if(!item.downloaded_native_asset && page.url()===before && !item.after_click_sign_in)item.free_click_no_download=true;
         }catch(e){item.click_error=String(e).slice(0,350);}
         break;
       }
       item.access_status=item.downloaded_native_asset?'ACTUAL_ASSET_DOWNLOADED_UNREVIEWED':
          item.after_click_sign_in?'SIGN_IN_REQUIRED':
          item.clicked_free_control?'NO_UNAUTHENTICATED_ASSET_AFTER_FREE_CLICK':'NO_FREE_DOWNLOAD_CONTROL';
       if(!clicked)item.notice='No normal free download control; no account/payment/captcha bypass attempted';
       await page.screenshot({path:path.join(out,s.id+'-after-free-click.png'),fullPage:false}).catch(()=>{});
     }
     item.browser_errors=errors;
   }catch(e){item.access_status='BROWSER_ACCESS_ERROR';item.error=String(e).slice(0,500);}
   finally{if(ctx)await ctx.close();}
 }
}finally{
 if(browser)await browser.close();
 const files=fs.readdirSync(out).filter(x=>!x.endsWith('.json')&&!x.endsWith('SHA256SUMS.txt'));
 report.saved_evidence_files=files;
 report.native_asset_count=report.sources.filter(s=>s.downloaded_native_asset).length;
 report.quality_gate='NO NEW MODEL IS ART APPROVED; any actual binary must be inspected separately in native 3D from 3 directions, and rights and mobile WebGL independently tested';
 fs.writeFileSync(path.join(out,'run310-source-access-results-NO_RELEASE.json'),JSON.stringify(report,null,2));
 const sums=fs.readdirSync(out).filter(f=>f!=='SHA256SUMS.txt').sort()
   .map(f=>sha(fs.readFileSync(path.join(out,f)))+'  '+f).join('\n')+'\n';
 fs.writeFileSync(path.join(out,'SHA256SUMS.txt'),sums);
 console.log(JSON.stringify(report,null,2));
}