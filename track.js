(function(){try{
var q=new URLSearchParams(location.search),H=location.hostname;
var rh='';try{rh=document.referrer?new URL(document.referrer).hostname.replace(/^www\./,''):''}catch(_){}
if(rh===H.replace(/^www\./,''))rh='';
var st=null;try{st=JSON.parse(sessionStorage.getItem('vp_s')||'null')}catch(_){}
if(!st){
 var s=q.get('utm_source')||(q.get('gclid')||q.get('gbraid')||q.get('wbraid')?'google-ads':q.get('fbclid')?'meta':q.get('e')?'email':rh||'direct');
 st={s:s.toLowerCase(),m:(q.get('utm_medium')||'').toLowerCase(),c:q.get('utm_campaign')||'',r:rh,i:Math.random().toString(36).slice(2,10)};
 try{sessionStorage.setItem('vp_s',JSON.stringify(st))}catch(_){}
}
function t(ev,p){try{navigator.sendBeacon('/t',JSON.stringify({ev:ev,p:p||location.pathname,s:st.s,m:st.m,c:st.c,r:st.r,i:st.i}))}catch(_){}}
t('view');
document.addEventListener('click',function(x){var a=x.target.closest&&x.target.closest('a');if(!a)return;var h=a.getAttribute('href')||'';if(/rendez-vous|cal\.com|wa\.me|mailto:|tel:/.test(h))t('cta',h.slice(0,80))},true);
}catch(_){}})();
(function(){try{
var q=new URLSearchParams(location.search),e=q.get('e');if(!e)return;
var U='https://vitria-machine.tausska.workers.dev/v';
function s(ev,p){try{navigator.sendBeacon(U,JSON.stringify({e:e,p:p||location.pathname,ev:ev}))}catch(_){}}
s('view');
document.addEventListener('click',function(x){
var a=x.target.closest&&x.target.closest('a');if(!a)return;
var h=a.getAttribute('href')||'';
if(/rendez-vous|cal\.com|wa\.me|mailto:|tel:/.test(h))s('cta',h);
if(h&&!/^(https?:|mailto:|tel:|#|javascript:)/.test(h)&&h.indexOf('e=')<0){a.href=h+(h.indexOf('?')<0?'?':'&')+'e='+encodeURIComponent(e)}
},true);
document.addEventListener('submit',function(){s('form')},true);
}catch(_){}})();
