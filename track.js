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
