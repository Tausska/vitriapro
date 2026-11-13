"""Démo plombier : Plomberie Delmas. Site pensé pour ce métier (urgence, triage, prix annoncés, estimation, demande de devis).
Lancer depuis la racine du dépôt : python3 -I tools/demo_plombier.py
"""
import os

OUT = "demo-plombier"
TEL = "01 99 00 12 34"          # numéro fictif réservé aux oeuvres de fiction
TELH = "+33199001234"

CSS = r"""
@font-face{font-family:BC;font-weight:700;font-display:swap;src:url(../fonts/barlow-condensed-latin-700-normal.woff2)}
@font-face{font-family:BC;font-weight:800;font-display:swap;src:url(../fonts/barlow-condensed-latin-800-normal.woff2)}
@font-face{font-family:BW;font-weight:400;font-display:swap;src:url(../fonts/barlow-latin-400-normal.woff2)}
@font-face{font-family:BW;font-weight:600;font-display:swap;src:url(../fonts/barlow-latin-600-normal.woff2)}
:root{--bg:#e9ecef;--ink:#0d1a23;--mut:#52606c;--line:#c3cad1;--wh:#fff;--hot:#d63a2b;--cold:#1b5fe8;--pipe:#8a97a3;--r:2px}
*{box-sizing:border-box;margin:0}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{font:400 17px/1.55 BW,system-ui,sans-serif;background:var(--bg);color:var(--ink);padding-bottom:76px;overflow-x:hidden}
a{color:inherit}
h1,h2,h3{font-family:BC,Impact,sans-serif;font-weight:800;line-height:.95;letter-spacing:-.005em}
.demo{background:var(--ink);color:#cfd6dc;font-size:13px;text-align:center;padding:8px 12px}.demo a{color:#fff}
.hd{position:sticky;top:0;z-index:30;background:var(--bg);border-bottom:2px solid var(--ink);display:flex;align-items:center;justify-content:space-between;padding:10px 18px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none}
.brand svg{width:34px;height:34px}.brand b{font:800 24px/1 BC;letter-spacing:.01em}
.nv{display:flex;gap:22px;align-items:center}
.nv a{text-decoration:none;font-weight:600;font-size:15px;padding:6px 0;border-bottom:2px solid transparent}.nv a:hover,.nv a.on{border-color:var(--cold)}
.nv .tel{background:var(--hot);color:#fff;padding:9px 14px;border:0;border-radius:var(--r);font-weight:600}
.bg{display:none;width:46px;height:46px;border:2px solid var(--ink);background:var(--wh);position:relative;cursor:pointer}
.bg i{position:absolute;left:11px;right:11px;height:2px;background:var(--ink);transition:transform .25s,opacity .2s}
.bg i:nth-child(1){top:15px}.bg i:nth-child(2){top:21px}.bg i:nth-child(3){top:27px}
.op .bg i:nth-child(1){transform:translateY(6px) rotate(45deg)}.op .bg i:nth-child(2){opacity:0}.op .bg i:nth-child(3){transform:translateY(-6px) rotate(-45deg)}
.w{max-width:1040px;margin:0 auto;padding:0 18px}
.hero{padding-top:30px;padding-bottom:10px}
.hero .g{display:grid;grid-template-columns:1.05fr .95fr;gap:30px;align-items:center}
.stat{display:inline-flex;align-items:center;gap:9px;font-weight:600;font-size:14px;background:var(--wh);border:2px solid var(--ink);padding:6px 12px 6px 10px}
.stat:before{content:"";width:10px;height:10px;border-radius:50%;background:#1f9d55;animation:pl 1.8s infinite}
@keyframes pl{50%{box-shadow:0 0 0 6px rgba(31,157,85,0)}0%{box-shadow:0 0 0 0 rgba(31,157,85,.5)}}
.hero h1{font-size:clamp(50px,14vw,104px);text-transform:uppercase;margin:16px 0 14px}
.hero h1 em{font-style:normal;color:var(--hot)}
.lead{font-size:18px;max-width:46ch;color:#2c3a45}
.q{margin-top:22px;font:700 15px BW;color:var(--mut)}
.tri{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
.tri button{font:700 20px/1.05 BC;text-align:left;padding:13px 12px;background:var(--wh);border:2px solid var(--ink);border-radius:var(--r);cursor:pointer;color:var(--ink);transition:transform .15s,background .2s,color .2s;min-height:58px}
.tri button:active{transform:translateY(2px)}
.tri button[aria-pressed=true]{background:var(--ink);color:#fff}
.tri button small{display:block;font:400 13px BW;opacity:.75;margin-top:3px}
.pan{margin-top:12px;background:var(--wh);border:2px solid var(--ink);border-left:8px solid var(--hot);padding:16px 16px 18px;display:none}
.pan.show{display:block;animation:in .35s ease}
@keyframes in{from{opacity:0;transform:translateY(8px)}}
.pan h3{font-size:30px;margin-bottom:8px}
.pan p{margin:6px 0}.pan .do{font-weight:600}
.pan .meta{display:flex;gap:18px;flex-wrap:wrap;margin:12px 0;font-weight:600}
.pan .meta span{border-top:2px solid var(--line);padding-top:6px}
.pan .meta b{display:block;font:800 26px/1 BC}
.btn{display:inline-block;font:700 19px/1 BC;letter-spacing:.02em;text-decoration:none;padding:15px 20px;border-radius:var(--r);border:2px solid var(--ink);cursor:pointer;transition:transform .15s}
.btn:active{transform:translateY(2px)}
.b-h{background:var(--hot);border-color:var(--hot);color:#fff}.b-c{background:var(--cold);border-color:var(--cold);color:#fff}.b-o{background:transparent;color:var(--ink)}
.acts{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.dg{width:100%;height:auto;display:block;background:var(--wh);border:2px solid var(--ink)}
.dg .p{fill:none;stroke-width:10;stroke-linecap:round;stroke-linejoin:round}
.dg .cold{stroke:var(--cold)}.dg .hot{stroke:var(--hot)}.dg .dr{stroke:var(--pipe)}
.dg .dw{stroke-dasharray:1;stroke-dashoffset:1;animation:dw 1.1s cubic-bezier(.6,0,.2,1) forwards}
.dg .dw:nth-of-type(2){animation-delay:.25s}.dg .dw:nth-of-type(3){animation-delay:.5s}.dg .dw:nth-of-type(4){animation-delay:.75s}
@keyframes dw{to{stroke-dashoffset:0}}
.dg .fl{fill:none;stroke:#fff;stroke-width:3;stroke-linecap:round;stroke-dasharray:2 16;opacity:0;animation:fo .6s 1.9s forwards,fm 1.2s 1.9s linear infinite}
@keyframes fo{to{opacity:.8}}@keyframes fm{to{stroke-dashoffset:-18}}
.dg .tank{fill:#dde3e8;stroke:var(--ink);stroke-width:3}
.dg .hs{opacity:0;transition:opacity .3s}.dg .hs circle.rg{fill:none;stroke:var(--hot);stroke-width:3;transform-box:fill-box;transform-origin:center;animation:rg 1.4s infinite}
@keyframes rg{from{transform:scale(.7);opacity:1}to{transform:scale(1.5);opacity:0}}
.dg[data-t=fuite] .hs.f,.dg[data-t=bouchon] .hs.b,.dg[data-t=chaudeau] .hs.c{opacity:1}
.dg text{font:700 15px BW;fill:var(--ink)}
.drip{fill:var(--cold);animation:dp 1.1s infinite}@keyframes dp{0%{transform:translateY(0);opacity:1}100%{transform:translateY(34px);opacity:0}}
.dg .lab{font:800 17px BC;fill:var(--hot)}
.fact{border-top:2px solid var(--ink);border-bottom:2px solid var(--ink);margin-top:34px;display:grid;grid-template-columns:repeat(4,1fr)}
.fact div{padding:14px 14px 14px 0;font-weight:600;line-height:1.25}.fact div+div{border-left:1px solid var(--line);padding-left:14px}
.fact b{display:block;font:800 30px/1 BC;color:var(--cold);margin-bottom:3px}
section{padding:54px 0 6px}
h2{font-size:clamp(36px,8vw,56px);text-transform:uppercase;margin-bottom:16px}
.sub{max-width:56ch;color:#2c3a45;margin-bottom:22px}
.pl{background:var(--wh);border:2px solid var(--ink)}
.pl h3{font-size:26px;padding:12px 16px;background:var(--ink);color:#fff}
.row{display:flex;align-items:baseline;gap:8px;padding:12px 16px;border-top:1px solid var(--line)}
.row:first-of-type{border-top:0}
.row span:first-child{font-weight:600}.row small{display:block;font-weight:400;color:var(--mut);font-size:14px}
.row i{flex:1;border-bottom:2px dotted var(--line);transform:translateY(-4px);min-width:16px}
.row b{font:800 24px/1 BC;white-space:nowrap}
.pls{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.seq{position:relative;margin-left:6px}
.seq:before{content:"";position:absolute;left:19px;top:10px;bottom:10px;width:6px;background:var(--cold);opacity:.25}
.st{position:relative;padding:0 0 22px 62px}
.st b{position:absolute;left:0;top:0;width:44px;height:44px;border-radius:50%;background:var(--wh);border:4px solid var(--cold);display:grid;place-items:center;font:800 20px BC;color:var(--cold)}
.st h3{font-size:26px;margin-bottom:3px}.st p{color:#2c3a45;max-width:52ch}
.zone{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
.cm{display:flex;flex-wrap:wrap;gap:8px}.cm span{border:2px solid var(--ink);background:var(--wh);padding:6px 11px;font-weight:600;font-size:15px}
.rad{aspect-ratio:1;max-width:340px;width:100%;margin:0 auto}
.rev{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.rv{background:var(--wh);border:2px solid var(--ink);padding:16px}
.rv q{display:block;font-size:17px;quotes:none}.rv b{display:block;margin-top:10px;font-weight:600}.rv small{color:var(--mut)}
.rv .s{color:#b8860b;letter-spacing:2px;font-size:17px}
.note{font-size:13px;color:var(--mut);margin-top:10px}
details{background:var(--wh);border:2px solid var(--ink);margin-top:8px}
summary{list-style:none;cursor:pointer;padding:15px 52px 15px 16px;font-weight:600;position:relative}
summary::-webkit-details-marker{display:none}
summary:after{content:"+";position:absolute;right:16px;top:8px;font:700 30px/1 BC;transition:transform .25s}
details[open] summary:after{transform:rotate(45deg)}
details p{padding:0 16px 16px;color:#2c3a45;max-width:60ch}
.vp{margin-top:56px;background:var(--ink);color:#fff;padding:46px 18px}
.vp h2{color:#fff;margin-bottom:10px}.vp p{max-width:52ch;color:#cfd6dc;margin-bottom:18px}.vp .btn{background:#fff;color:var(--ink);border-color:#fff}
.ft{background:#071017;color:#aeb8c0;padding:30px 18px 24px;font-size:14px}
.ft .g{max-width:1040px;margin:0 auto;display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:24px}
.ft b{display:block;color:#fff;font:800 20px BC;margin-bottom:6px}.ft a{display:block;text-decoration:none;margin:3px 0}.ft a:hover{color:#fff}
.ft .c{max-width:1040px;margin:22px auto 0;padding-top:14px;border-top:1px solid #ffffff22;font-size:12px}
.sb{position:fixed;left:0;right:0;bottom:0;z-index:40;display:grid;grid-template-columns:1.25fr 1fr;gap:0;box-shadow:0 -6px 22px rgba(13,26,35,.25)}
.sb a{display:block;text-align:center;text-decoration:none;color:#fff;font:800 20px/1 BC;letter-spacing:.02em;padding:18px 8px 20px}
.sb .h{background:var(--hot)}.sb .c{background:var(--cold)}
.sb a small{display:block;font:400 12px BW;opacity:.85;margin-top:3px;letter-spacing:0}
.ph{padding-top:30px;padding-bottom:8px}.ph h1{font-size:clamp(46px,11vw,84px);text-transform:uppercase;margin-bottom:12px}
.est{background:var(--wh);border:2px solid var(--ink);padding:18px;margin-top:6px}
.est label,.fm label{display:block;font-weight:600;font-size:14px;margin:12px 0 6px}
.est select,.fm input,.fm select,.fm textarea{display:block;width:100%;padding:0 12px;height:52px;font:400 17px BW;border:2px solid var(--ink);border-radius:var(--r);background:var(--wh);color:var(--ink);-webkit-appearance:none;appearance:none}
.fm textarea{height:120px;padding:12px;resize:vertical}
.est select,.fm select{background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='8'%3E%3Cpath d='M1 1l6 6 6-6' fill='none' stroke='%230d1a23' stroke-width='2'/%3E%3C/svg%3E") no-repeat right 14px center}
.est select:focus,.fm input:focus,.fm select:focus,.fm textarea:focus,.btn:focus-visible,summary:focus-visible,.tri button:focus-visible,a:focus-visible{outline:3px solid var(--cold);outline-offset:2px}
.seg{display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:6px}
.seg button{height:50px;font:700 18px BC;border:2px solid var(--ink);background:var(--wh);cursor:pointer;color:var(--ink)}.seg button+button{border-left:0}
.seg button[aria-pressed=true]{background:var(--ink);color:#fff}
.res{margin-top:16px;border-top:2px solid var(--ink);padding-top:12px}.res b{font:800 52px/1 BC;color:var(--cold);display:block}.res span{color:var(--mut);font-size:14px}
.cases{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.cs{background:var(--wh);border:2px solid var(--ink)}
.cs .vis{background:#f3f5f7;border-bottom:2px solid var(--ink);aspect-ratio:16/9;position:relative}
.cs svg{width:100%;height:100%;display:block}
.cs .ap,.cs.is-ap .av{display:none}.cs.is-ap .ap{display:block}
.cs .bd{padding:14px 16px 16px}.cs h3{font-size:28px;margin-bottom:6px}
.cs dl{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;margin-top:10px;font-size:15px}.cs dt{font-weight:600}.cs dd{margin:0;color:#2c3a45}
.cs .seg{margin:0}
.fm{background:var(--wh);border:2px solid var(--ink);padding:18px;max-width:620px}
.stp{display:flex;gap:6px;margin-bottom:6px}.stp i{flex:1;height:6px;background:var(--line)}.stp i.on{background:var(--cold)}
.tp{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
.tp button{font:700 20px/1.05 BC;text-align:left;padding:14px 12px;background:var(--wh);border:2px solid var(--ink);cursor:pointer;color:var(--ink);min-height:56px}
.tp button[aria-pressed=true]{background:var(--ink);color:#fff}
.sl{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-top:6px}
.sl button{height:48px;font:700 18px BC;border:2px solid var(--ink);background:var(--wh);cursor:pointer;color:var(--ink)}.sl button[aria-pressed=true]{background:var(--cold);color:#fff;border-color:var(--cold)}
.er{display:none;color:#a02a1a;font-weight:600;margin-top:12px}.er.show{display:block;animation:in .3s}
.ok{display:none;background:#e8f3ea;border:2px solid #1f7a3a;padding:16px;margin-top:14px;font-weight:600}.ok.show{display:block;animation:in .4s}
.plan{margin-top:24px;aspect-ratio:16/7;border:2px solid var(--ink);background:repeating-linear-gradient(45deg,#dfe4e8 0 14px,#e9ecef 14px 28px);display:grid;place-items:center;text-align:center;padding:18px;font:700 20px BC}
.cols2{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:start}
@media(max-width:820px){
 .bg{display:block}
 .nv{position:absolute;left:0;right:0;top:100%;background:var(--bg);flex-direction:column;align-items:stretch;gap:0;padding:0 18px;max-height:0;overflow:hidden;border-bottom:2px solid var(--ink);transition:max-height .35s}
 .op .nv{max-height:420px;padding-bottom:12px}.nv a{padding:14px 0;border-bottom:1px solid var(--line);font-size:17px}.nv .tel{margin-top:10px;text-align:center}
 .hero .g,.zone,.cols2,.pls,.cases,.rev{grid-template-columns:1fr}
 .fact{grid-template-columns:1fr 1fr}.fact div:nth-child(3){border-left:0;padding-left:0}.fact div:nth-child(n+3){border-top:1px solid var(--line)}
 .ft .g{grid-template-columns:1fr}
}
@media(min-width:821px){body{padding-bottom:0}.sb{display:none}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important}.dg .dw{stroke-dashoffset:0}.dg .fl{opacity:.8}}
"""

JS = r"""
(function(){
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var hd=$('.hd');var b=$('.bg');if(b)b.onclick=function(){hd.classList.toggle('op')};
/* triage */
var T={
fuite:{t:'Fuite d’eau',do:'D’abord, fermez le robinet d’arrêt (sous l’évier ou près du compteur). Épongez, et ne touchez pas aux prises électriques mouillées.',p:'dès 89 €',e:'Sur place sous 45 min en journée'},
bouchon:{t:'Canalisation bouchée',do:'Évitez le débouchant chimique : il abîme les tuyaux et complique le travail. Ne versez rien, appelez-nous.',p:'dès 79 €',e:'Sur place sous 1 h en journée'},
chaudeau:{t:'Plus d’eau chaude',do:'Vérifiez que le disjoncteur du chauffe-eau n’a pas sauté. S’il saute de nouveau, ne le réenclenchez pas et appelez-nous.',p:'49 € le diagnostic',e:'Déduit si vous commandez les travaux'},
autre:{t:'Autre besoin',do:'Salle de bains, robinetterie, installation : décrivez-nous votre projet, vous recevez un devis avant toute intervention.',p:'Devis gratuit',e:'Réponse sous 24 h'}};
var pan=$('#pan'),dg=$('#dg');
$$('.tri button').forEach(function(bt){bt.onclick=function(){
 var k=bt.dataset.k,d=T[k];$$('.tri button').forEach(function(x){x.setAttribute('aria-pressed',x===bt)});
 if(dg)dg.setAttribute('data-t',k);
 pan.innerHTML='<h3>'+d.t+'</h3><p class="do">'+d.do+'</p><div class="meta"><span><b>'+d.p+'</b>Tarif annoncé</span><span><b>'+d.e.split(' ')[0]+(d.e.indexOf('Sur place')==0?'':'')+'</b></span></div><div class="acts"><a class="btn b-h" href="tel:%TELH%">Appeler le %TEL%</a><a class="btn b-o" href="devis.html?type='+k+'">Planifier un créneau</a></div>';
 pan.querySelector('.meta').innerHTML='<span><b>'+d.p+'</b>Tarif annoncé</span><span><b style="font-size:20px;line-height:1.1">'+d.e+'</b></span>';
 pan.classList.add('show');pan.style.animation='none';void pan.offsetWidth;pan.style.animation='';
}});
/* estimation */
var E={fuite:89,bouchon:79,robinet:69,chauffeeau:290,chaudiere:95,sdb:0};
var es=$('#es');
if(es){var sv=es.querySelector('select'),mode='day',out=$('#res');
 function calc(){var base=E[sv.value];var r;
  if(sv.value==='sdb'){r='<b>Sur devis</b><span>Visite gratuite, prix ferme avant les travaux.</span>';}
  else{var v=Math.round(base*(mode==='night'?1.3:1));var lab=sv.value==='chauffeeau'?'Pose seule, hors fourniture du ballon.':'Main d’œuvre et déplacement inclus, pièces en plus.';
   r='<b>dès '+v+' €</b><span>'+lab+(mode==='night'?' Majoré de 30 % le soir et le week-end.':'')+' Estimation indicative.</span>';}
  out.innerHTML=r}
 sv.onchange=calc;$$('.seg button',es).forEach(function(x){x.onclick=function(){mode=x.dataset.m;$$('.seg button',es).forEach(function(y){y.setAttribute('aria-pressed',y===x)});calc()}});calc();}
/* avant / après */
$$('.cs').forEach(function(c){$$('.seg button',c).forEach(function(x){x.onclick=function(){c.classList.toggle('is-ap',x.dataset.s==='ap');$$('.seg button',c).forEach(function(y){y.setAttribute('aria-pressed',y===x)})}})});
/* devis */
var fq=$('#fq');
if(fq){var st=1,data={type:'',slot:''};var steps=$$('.stepbox',fq),bars=$$('.stp i',fq);
 function show(n){st=n;steps.forEach(function(s,i){s.style.display=(i+1===n)?'block':'none'});bars.forEach(function(x,i){x.classList.toggle('on',i<n)});$('#er').className='er'}
 function bad(m){var e=$('#er');e.textContent=m;e.className='er show'}
 $$('.tp button',fq).forEach(function(x){x.onclick=function(){data.type=x.dataset.k;data.label=x.textContent;$$('.tp button',fq).forEach(function(y){y.setAttribute('aria-pressed',y===x)})}});
 $$('.sl button',fq).forEach(function(x){x.onclick=function(){data.slot=x.textContent;$$('.sl button',fq).forEach(function(y){y.setAttribute('aria-pressed',y===x)})}});
 var m=location.search.match(/type=(\w+)/);if(m){var pre=$('.tp button[data-k='+m[1]+']',fq);if(pre)pre.click()}
 var d=$('#d'),t=new Date();d.value=t.toISOString().slice(0,10);d.min=d.value;
 $('#n1').onclick=function(){if(!data.type){bad('Choisissez le type d’intervention.');return}show(2)};
 $('#n2').onclick=function(){if(!data.slot){bad('Choisissez un créneau.');return}show(3)};
 $('#p2').onclick=function(){show(1)};$('#p3').onclick=function(){show(2)};
 $('#send').onclick=function(){var nm=$('#nm').value.trim(),tl=$('#tl').value.trim(),vl=$('#vl').value.trim();
  if(!nm){bad('Indiquez votre nom.');return}if(tl.replace(/\D/g,'').length<9){bad('Indiquez un numéro de téléphone valide.');return}if(!vl){bad('Indiquez votre commune.');return}
  var dt=new Date(d.value+'T12:00:00').toLocaleDateString('fr-FR',{weekday:'long',day:'numeric',month:'long'});
  var ok=$('#ok');ok.textContent='Merci '+nm+'. Demande enregistrée : '+data.label.toLowerCase()+' à '+vl+', le '+dt+', créneau '+data.slot+'. Nous vous rappelons au '+tl+' pour confirmer. (Démonstration : aucune demande réelle.)';
  ok.className='ok show';$('#er').className='er';$$('.stepbox',fq).forEach(function(s){s.style.display='none'});ok.scrollIntoView({behavior:'smooth',block:'center'})};
 show(1)}
/* contact */
var cf=$('#cf');
if(cf){cf.addEventListener('submit',function(e){e.preventDefault();var er=$('#er2'),ok=$('#ok2'),nm=$('#cn').value.trim(),em=$('#ce').value.trim(),ms=$('#cm').value.trim();er.className='er';ok.className='ok';
 function bad(m){er.textContent=m;er.className='er show'}
 if(!nm)return bad('Indiquez votre nom.');if(!/^\S+@\S+\.\S+$/.test(em))return bad('Indiquez une adresse e-mail valide.');if(!ms)return bad('Écrivez votre message.');
 ok.textContent='Merci '+nm+', votre message est envoyé. Nous vous répondons sous 24 h. (Démonstration : aucun message réel.)';ok.className='ok show'})}
})();
""".replace("%TELH%", TELH).replace("%TEL%", TEL)

LOGO = '<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M6 8h14a8 8 0 0 1 8 8v16" fill="none" stroke="#1b5fe8" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="28" cy="33" r="3.2" fill="#d63a2b"/></svg>'
NAV = [("index.html", "Accueil"), ("services.html", "Services et prix"), ("realisations.html", "Réalisations"), ("devis.html", "Devis"), ("contact.html", "Contact")]


def page(fn, title, body, desc):
    links = "".join(f'<a href="{h}"{" class=on" if h == fn else ""}>{t}</a>' for h, t in NAV)
    fl = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} · Plomberie Delmas</title><meta name="robots" content="noindex"><meta name="description" content="{desc}">
<link rel="stylesheet" href="style.css"></head><body>
<div class="demo">Site de démonstration réalisé par VITRIA PRO. <a href="../index.html">Voir les offres</a></div>
<header class="hd"><a class="brand" href="index.html">{LOGO}<b>Plomberie Delmas</b></a>
<nav class="nv">{links}<a class="tel" href="tel:{TELH}">Urgence : {TEL}</a></nav>
<button class="bg" aria-label="Menu"><i></i><i></i><i></i></button></header>
{body}
<div class="vp"><div class="w"><h2>Vous êtes plombier ?</h2><p>Ce site est une démonstration. Le vôtre sera fait sur mesure : vos services, vos prix, vos zones, avec demande de devis directement sur votre téléphone.</p><a class="btn" href="../rendez-vous.html">Je veux le même site</a></div></div>
<footer class="ft"><div class="g"><div><b>Plomberie Delmas</b>Dépannage, installation et entretien.<br>Zone d'intervention : 30 km autour de Valmont (ville fictive)</div>
<div><b>Horaires</b>Lundi au samedi, 8h – 19h<br>Urgences 7j/7 par téléphone<br>{TEL}</div><div><b>Le site</b>{fl}<a href="mentions.html">Mentions légales</a></div></div>
<div class="c">Site de démonstration · Les noms, adresses, numéros et prix sont fictifs · Réalisé par VITRIA PRO</div></footer>
<div class="sb"><a class="h" href="tel:{TELH}">Appeler<small>{TEL}</small></a><a class="c" href="devis.html">Devis<small>réponse sous 24 h</small></a></div>
<script src="app.js"></script><script src="../track.js" defer></script></body></html>"""


def row(n, d, p):
    return f'<div class="row"><span>{n}{f"<small>{d}</small>" if d else ""}</span><i></i><b>{p}</b></div>'


DIAGRAM = """<svg class="dg" id="dg" viewBox="0 0 400 330" role="img" aria-label="Schéma d'une installation de plomberie avec les trois pannes les plus fréquentes">
<g class="pp">
<path class="p cold dw" pathLength="1" d="M0 70H200H235V190H272"/>
<path class="p hot dw" pathLength="1" d="M316 44V20H92V132"/>
<path class="p dr dw" pathLength="1" d="M92 172V268H340"/>
</g>
<rect class="tank" x="272" y="44" width="88" height="170" rx="16"/>
<text x="316" y="134" text-anchor="middle">Ballon</text>
<rect x="66" y="132" width="52" height="40" rx="6" fill="#dde3e8" stroke="#0d1a23" stroke-width="3"/>
<text x="92" y="157" text-anchor="middle" style="font-size:13px">Évier</text>
<circle cx="40" cy="70" r="14" fill="#fff" stroke="#0d1a23" stroke-width="3"/><path d="M33 70h14M40 63v14" stroke="#0d1a23" stroke-width="3"/>
<text x="40" y="104" text-anchor="middle" style="font-size:13px">Arrêt</text>
<path class="fl" d="M0 70H200H235V190H272"/><path class="fl" d="M316 44V20H92V132" style="stroke:#fff"/><path class="fl" d="M92 172V268H340"/>
<g class="hs f"><circle class="rg" cx="150" cy="70" r="16"/><rect x="142" y="60" width="16" height="20" fill="#fff" stroke="#d63a2b" stroke-width="3"/><circle class="drip" cx="150" cy="90" r="4"/><text class="lab" x="150" y="46" text-anchor="middle">Fuite</text></g>
<g class="hs b"><circle class="rg" cx="200" cy="268" r="18"/><rect x="190" y="258" width="20" height="20" fill="#d63a2b"/><path d="M194 262l12 12M206 262l-12 12" stroke="#fff" stroke-width="3"/><text class="lab" x="200" y="304" text-anchor="middle">Bouchon</text></g>
<g class="hs c"><circle class="rg" cx="316" cy="190" r="30"/><text class="lab" x="316" y="242" text-anchor="middle">Pas d'eau chaude</text></g>
</svg>"""

pages = {}

# ----------------------------------------------------------------- Accueil
pages["index.html"] = page("index.html", "Plombier, dépannage et installation", f"""
<main class="w hero"><div class="g"><div>
<span class="stat">Disponible maintenant · arrivée sous 45 min</span>
<h1>Fuite ? <em>On arrive.</em></h1>
<p class="lead">Dépannage, installation et entretien. Le prix est annoncé avant de commencer, et vous repartez avec une facture détaillée.</p>
<p class="q">Qu'est-ce qui se passe chez vous ?</p>
<div class="tri"><button data-k="fuite" aria-pressed="false">Une fuite<small>Eau qui coule, plafond humide</small></button><button data-k="bouchon" aria-pressed="false">Un bouchon<small>Évier, WC ou douche</small></button><button data-k="chaudeau" aria-pressed="false">Plus d'eau chaude<small>Chauffe-eau, chaudière</small></button><button data-k="autre" aria-pressed="false">Autre chose<small>Projet, devis</small></button></div>
<div class="pan" id="pan" aria-live="polite"></div>
</div><div>{DIAGRAM}<p class="note">Touchez un problème : on vous montre où ça se passe dans l'installation.</p></div></div>
<div class="fact"><div><b>45 min</b>Arrivée en journée</div><div><b>Prix annoncé</b>Avant de commencer</div><div><b>2 ans</b>Garantie sur la pose</div><div><b>7j/7</b>Urgences par téléphone</div></div></main>

<section><div class="w"><h2>Les prix, à l'avance</h2><p class="sub">Pas de mauvaise surprise : voici ce que coûtent nos interventions les plus courantes. Les pièces sont en plus, le devis est signé avant les travaux.</p>
<div class="pls"><div class="pl"><h3>Urgences</h3>{row("Dépannage fuite d'eau", "Recherche et réparation", "dès 89 €")}{row("Débouchage", "Évier, WC, douche", "dès 79 €")}{row("Déplacement et diagnostic", "Déduit si vous commandez les travaux", "49 €")}</div>
<div class="pl"><h3>Installation et entretien</h3>{row("Robinetterie", "Fourniture et pose", "dès 69 €")}{row("Chauffe-eau", "Pose et mise en service", "sur devis")}{row("Entretien chaudière", "Contrôle annuel", "dès 95 €")}</div></div>
<div class="acts"><a class="btn b-c" href="services.html">Estimer mon budget</a></div></div></section>

<section><div class="w"><h2>Comment ça se passe</h2><p class="sub">Cinq étapes, et vous savez toujours où on en est.</p>
<div class="seq"><div class="st"><b>1</b><h3>Vous appelez ou vous écrivez</h3><p>Au téléphone en urgence, ou par la demande de devis. On vous répond dans l'heure en journée.</p></div>
<div class="st"><b>2</b><h3>Diagnostic sur place</h3><p>On trouve l'origine du problème. Le déplacement de 49 € est déduit si vous commandez les travaux.</p></div>
<div class="st"><b>3</b><h3>Devis signé avant les travaux</h3><p>Le prix est ferme. S'il y a un imprévu, on vous le dit avant, jamais après.</p></div>
<div class="st"><b>4</b><h3>Réparation, puis nettoyage</h3><p>On protège les sols, on répare, on nettoie. Vous retrouvez votre intérieur comme avant.</p></div>
<div class="st"><b>5</b><h3>Facture détaillée et garantie</h3><p>Chaque ligne est expliquée, et la pose est garantie 2 ans.</p></div></div></div></section>

<section><div class="w zone"><div><h2>On intervient près de chez vous</h2><p class="sub">Dans un rayon de 30 km autour de Valmont. Hors zone, appelez-nous : on regarde ensemble.</p>
<div class="cm"><span>Valmont</span><span>Saint-Clair</span><span>Les Roches</span><span>Bellevue</span><span>Pont-Neuf</span><span>La Garenne</span><span>Montclar</span><span>Ravel</span></div></div>
<svg class="rad" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="92" fill="#fff" stroke="#0d1a23" stroke-width="3"/><circle cx="100" cy="100" r="60" fill="none" stroke="#c3cad1" stroke-width="2" stroke-dasharray="4 6"/><circle cx="100" cy="100" r="30" fill="none" stroke="#c3cad1" stroke-width="2" stroke-dasharray="4 6"/><path d="M100 8v184M8 100h184" stroke="#c3cad1" stroke-width="1.5"/><circle cx="100" cy="100" r="7" fill="#d63a2b"/><text x="100" y="126" text-anchor="middle" style="font:800 13px BC">Atelier</text><text x="106" y="44" style="font:600 12px BW">15 km</text><text x="106" y="17" style="font:600 12px BW">30 km</text></svg></div></section>

<section><div class="w"><h2>Ce que disent les clients</h2><div class="rev">
<div class="rv"><span class="s">★★★★★</span><q>Fuite sous l'évier un dimanche soir. Quelqu'un est arrivé en 40 minutes, prix annoncé avant de toucher à quoi que ce soit.</q><b>Nadia</b><small>Valmont</small></div>
<div class="rv"><span class="s">★★★★★</span><q>Chauffe-eau remplacé dans la matinée. Le devis a été respecté au centime et le sol était propre en partant.</q><b>Pascal</b><small>Saint-Clair</small></div>
<div class="rv"><span class="s">★★★★★</span><q>Ils m'ont expliqué la panne au lieu de me vendre une pièce. Je les rappellerai pour la salle de bains.</q><b>Élodie</b><small>Les Roches</small></div></div>
<p class="note">Exemples d'avis fictifs, pour la démonstration. Sur votre site, ce sont vos vrais avis clients.</p></div></section>

<section><div class="w"><h2>Questions fréquentes</h2>
<details><summary>Combien coûte un déplacement ?</summary><p>49 € pour le déplacement et le diagnostic. Cette somme est déduite si vous nous confiez les travaux.</p></details>
<details><summary>Intervenez-vous le week-end et le soir ?</summary><p>Oui, pour les urgences, 7j/7 par téléphone. Les interventions le soir et le week-end sont majorées de 30 %, annoncées avant que nous venions.</p></details>
<details><summary>Le devis est-il gratuit ?</summary><p>Oui, et sans engagement. Pour un projet (salle de bains, chauffe-eau), la visite est gratuite et le prix est ferme.</p></details>
<details><summary>Comment puis-je payer ?</summary><p>Par carte, chèque ou virement, à la fin de l'intervention, sur facture détaillée.</p></details></div></section>""",
    "Démonstration d'un site de plombier réalisé par VITRIA PRO.")

# ----------------------------------------------------------------- Services
pages["services.html"] = page("services.html", "Services et prix", f"""
<main class="w ph"><h1>Services et prix</h1><p class="lead">Chaque intervention commence par un diagnostic et un devis clair. Voici nos tarifs, et un moyen d'estimer votre budget.</p></main>
<section style="padding-top:20px"><div class="w cols2"><div>
<div class="pl"><h3>Urgences</h3>{row("Dépannage fuite d'eau", "Recherche et réparation", "dès 89 €")}{row("Débouchage canalisation", "Évier, WC, douche", "dès 79 €")}{row("Recherche de fuite", "Caméra et détection", "dès 150 €")}{row("Déplacement et diagnostic", "Déduit si vous commandez les travaux", "49 €")}</div>
<div class="pl" style="margin-top:18px"><h3>Installation</h3>{row("Remplacement robinetterie", "Fourniture et pose", "dès 69 €")}{row("Chauffe-eau", "Pose et mise en service", "sur devis")}{row("Salle de bains", "Rénovation complète", "sur devis")}{row("WC", "Remplacement", "dès 190 €")}</div>
<div class="pl" style="margin-top:18px"><h3>Entretien</h3>{row("Entretien chaudière", "Contrôle annuel", "dès 95 €")}{row("Détartrage", "Chauffe-eau et circuits", "dès 85 €")}</div>
<p class="note">Prix indicatifs de démonstration, pièces en plus. Le devis est signé avant les travaux.</p></div>
<div><h2 style="font-size:40px">Estimer mon budget</h2><div class="est" id="es"><label for="sv">Que faut-il faire ?</label><select id="sv"><option value="fuite">Fuite d'eau</option><option value="bouchon">Débouchage</option><option value="robinet">Robinetterie</option><option value="chauffeeau">Chauffe-eau</option><option value="chaudiere">Entretien chaudière</option><option value="sdb">Salle de bains</option></select>
<label>Quand ?</label><div class="seg"><button data-m="day" aria-pressed="true">En journée</button><button data-m="night" aria-pressed="false">Soir ou week-end</button></div>
<div class="res" id="res"></div><div class="acts"><a class="btn b-c" href="devis.html">Demander un devis précis</a></div></div></div></div></section>""",
    "Services et tarifs de la plomberie Delmas (démonstration).")


# ----------------------------------------------------------------- Réalisations
def case(title, prob, sol, dur, price, kind):
    if kind == "tank":
        av = '<rect x="150" y="30" width="100" height="140" rx="16" fill="#dde3e8" stroke="#0d1a23" stroke-width="4"/><path d="M200 70l-10 24 14 10-8 26" fill="none" stroke="#d63a2b" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="200" cy="184" r="6" fill="#1b5fe8"><animate attributeName="cy" values="176;196" dur="1.1s" repeatCount="indefinite"/></circle>'
        ap = '<rect x="150" y="30" width="100" height="140" rx="16" fill="#dde3e8" stroke="#0d1a23" stroke-width="4"/><path d="M180 100l14 14 28-30" fill="none" stroke="#1b5fe8" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
    else:
        av = '<path d="M30 100H170M230 100H370" stroke="#8a97a3" stroke-width="14" stroke-linecap="round"/><path d="M170 100l12-22 14 22 12-22 12 22" fill="none" stroke="#d63a2b" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="200" cy="130" r="6" fill="#1b5fe8"><animate attributeName="cy" values="120;160" dur="1.1s" repeatCount="indefinite"/></circle>'
        ap = '<path d="M30 100H370" stroke="#1b5fe8" stroke-width="14" stroke-linecap="round"/><rect x="186" y="90" width="28" height="20" fill="#fff" stroke="#0d1a23" stroke-width="3"/><path d="M180 140l14 14 28-30" fill="none" stroke="#1b5fe8" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    return f"""<article class="cs"><div class="vis"><svg viewBox="0 0 400 225" role="img" aria-label="{title}"><g class="av">{av}</g><g class="ap">{ap}</g></svg></div>
<div class="bd"><div class="seg"><button data-s="av" aria-pressed="true">Avant</button><button data-s="ap" aria-pressed="false">Après</button></div><h3 style="margin-top:12px">{title}</h3>
<dl><dt>Problème</dt><dd>{prob}</dd><dt>Réalisé</dt><dd>{sol}</dd><dt>Durée</dt><dd>{dur}</dd><dt>Prix</dt><dd>{price}</dd></dl></div></article>"""


pages["realisations.html"] = page("realisations.html", "Réalisations", f"""
<main class="w ph"><h1>Réalisations</h1><p class="lead">Quatre interventions récentes, avec le problème, ce qui a été fait, le temps passé et le prix payé. Touchez « Après » pour voir le résultat.</p></main>
<section style="padding-top:20px"><div class="w"><div class="cases">
{case("Chauffe-eau percé, remplacé", "Ballon de 200 L qui fuyait, plus d'eau chaude depuis la veille.", "Dépose, pose d'un ballon neuf, groupe de sécurité remplacé.", "3 h, le jour même", "890 € TTC, devis respecté", "tank")}
{case("Fuite sur canalisation encastrée", "Tache d'humidité au plafond du voisin du dessous.", "Localisation, remplacement du tronçon, test en pression.", "2 h 30", "310 € TTC", "pipe")}
{case("Évier bouché depuis une semaine", "Écoulement lent puis bouchon complet, odeurs.", "Débouchage mécanique, nettoyage du siphon.", "1 h", "119 € TTC", "pipe")}
{case("Ballon d'eau chaude entartré", "Eau tiède, consommation électrique en hausse.", "Détartrage, remplacement de l'anode et du groupe de sécurité.", "2 h", "185 € TTC", "tank")}
</div><p class="note">Exemples fictifs, pour la démonstration. Sur votre site, ce sont vos vrais chantiers, avec vos photos.</p></div></section>""",
    "Réalisations de la plomberie Delmas (démonstration).")

# ----------------------------------------------------------------- Devis
pages["devis.html"] = page("devis.html", "Demande de devis", f"""
<main class="w ph"><h1>Demander un devis</h1><p class="lead">Trois étapes, une minute. Pour une fuite importante, ne remplissez pas ce formulaire : appelez le <a href="tel:{TELH}"><b>{TEL}</b></a>.</p></main>
<section style="padding-top:18px"><div class="w"><div class="fm" id="fq"><div class="stp"><i></i><i></i><i></i></div>
<div class="stepbox"><label>1. Quel est le besoin ?</label><div class="tp"><button data-k="fuite" aria-pressed="false">Fuite d'eau</button><button data-k="bouchon" aria-pressed="false">Débouchage</button><button data-k="chaudeau" aria-pressed="false">Chauffe-eau</button><button data-k="autre" aria-pressed="false">Autre projet</button></div>
<div class="acts"><button class="btn b-c" id="n1" type="button">Continuer</button></div></div>
<div class="stepbox" style="display:none"><label for="d">2. Quel jour ?</label><input type="date" id="d"><label>Créneau souhaité</label><div class="sl"><button type="button" aria-pressed="false">8h – 10h</button><button type="button" aria-pressed="false">10h – 12h</button><button type="button" aria-pressed="false">14h – 16h</button><button type="button" aria-pressed="false">16h – 18h</button></div>
<div class="acts"><button class="btn b-o" id="p2" type="button">Retour</button><button class="btn b-c" id="n2" type="button">Continuer</button></div></div>
<div class="stepbox" style="display:none"><label for="nm">3. Vos coordonnées</label><input id="nm" placeholder="Nom" autocomplete="name"><label for="tl">Téléphone</label><input id="tl" type="tel" placeholder="Pour vous rappeler" autocomplete="tel"><label for="vl">Commune</label><input id="vl" placeholder="Où intervenir ?">
<div class="acts"><button class="btn b-o" id="p3" type="button">Retour</button><button class="btn b-h" id="send" type="button">Envoyer ma demande</button></div></div>
<div class="er" id="er" role="alert"></div><div class="ok" id="ok" role="status"></div></div></div></section>""",
    "Demande de devis plomberie (démonstration).")

# ----------------------------------------------------------------- Contact
pages["contact.html"] = page("contact.html", "Contact", f"""
<main class="w ph"><h1>Contact</h1><p class="lead">Une urgence ? Appelez. Une question ou un projet ? Écrivez, on répond sous 24 h.</p></main>
<section style="padding-top:20px"><div class="w cols2"><div><div class="pl"><h3>Nous joindre</h3>{row("Urgences 7j/7", "Par téléphone", f'<a href="tel:{TELH}" style="text-decoration:none">{TEL}</a>')}{row("Horaires", "Lundi au samedi", "8h – 19h")}{row("Zone", "Autour de Valmont", "30 km")}</div>
<div class="plan">Plan d'accès et zone d'intervention<br>(carte intégrée sur votre vrai site)</div></div>
<form class="fm" id="cf" novalidate><label for="cn">Nom</label><input id="cn" autocomplete="name"><label for="ce">E-mail</label><input id="ce" type="email" autocomplete="email"><label for="cm">Message</label><textarea id="cm"></textarea>
<div class="er" id="er2" role="alert"></div><div class="acts"><button class="btn b-c" type="submit">Envoyer le message</button></div><div class="ok" id="ok2" role="status"></div></form></div></section>""",
    "Contacter la plomberie Delmas (démonstration).")

# ----------------------------------------------------------------- Mentions
pages["mentions.html"] = page("mentions.html", "Mentions légales", """
<main class="w ph"><h1>Mentions légales</h1><p class="lead">Ce site est une démonstration réalisée par VITRIA PRO. Plomberie Delmas est une entreprise fictive : les noms, adresses, numéros, prestations, prix, avis et réalisations sont fictifs. Sur votre site, cette page contient vos informations légales réelles (raison sociale, SIRET, adresse, contact, hébergeur, données personnelles).</p></main>""",
    "Mentions légales (démonstration).")

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "style.css"), "w", encoding="utf-8").write(CSS)
open(os.path.join(OUT, "app.js"), "w", encoding="utf-8").write(JS)
for fn, html in pages.items():
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
print(len(pages), "pages")
