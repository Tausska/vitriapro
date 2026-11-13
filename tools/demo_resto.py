"""Génère la démo complète de site de restaurant (Maison Aubépine) dans demo-restaurant/.
Lancer depuis la racine du dépôt : python3 -I tools/demo_resto.py
"""
import os

OUT = "demo-restaurant"
U = lambda i, w=900: f"https://images.unsplash.com/photo-{i}?auto=format&fit=crop&w={w}&q=80"
IMG = {
    "salle": "1517248135467-4c7edcad34c4", "plat": "1414235077428-338989a2e8c0", "grill": "1555939594-58d7cb561ad1",
    "salade": "1546069901-ba9599a7e63c", "salle2": "1559339352-11d035aa65de",
    "assiette": "1551218808-94e220e084d2", "viande": "1600891964092-4316c288032e", "marche": "1504674900247-0877df9cc836",
}
NAV = [("index.html", "Accueil"), ("carte.html", "La carte"), ("galerie.html", "Galerie"), ("histoire.html", "Notre histoire"), ("contact.html", "Contact")]

CSS = """
@font-face{font-family:PF;font-weight:700;src:url(../fonts/playfair-display-latin-700-normal.woff2)}
@font-face{font-family:PF;font-weight:700;font-style:italic;src:url(../fonts/playfair-display-latin-700-italic.woff2)}
:root{--ink:#241a16;--cream:#f7f0e6;--clay:#b4532a;--moss:#2f3a2c;--sand:#efe3cf;--ease:cubic-bezier(.2,.7,.2,1)}
*{box-sizing:border-box;margin:0}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}body{overflow-x:clip}
body{font-family:Inter,system-ui,sans-serif;background:var(--cream);color:var(--ink);line-height:1.6}
a{color:inherit}
.demo{background:#111;color:#fff;font-size:13px;text-align:center;padding:9px 12px}.demo a{color:#f0c27a}
.nav{--p:0;display:flex;justify-content:space-between;align-items:center;padding:16px 22px;background:var(--cream);position:sticky;top:0;z-index:20;border-bottom:1px solid #e3d5bd;transition:padding .4s var(--ease),box-shadow .4s}
.nav.sc{padding:10px 22px;box-shadow:0 10px 30px -18px rgba(36,26,22,.45)}
.nav:after{content:"";position:absolute;left:0;bottom:-1px;height:2px;width:100%;background:var(--clay);transform-origin:left;transform:scaleX(var(--p))}
.logo{font-family:PF,Georgia,serif;font-weight:700;font-size:21px;color:var(--moss);text-decoration:none}
.menu-l{display:flex;align-items:center;gap:26px}
.menu-l a{text-decoration:none;font-size:14px;color:var(--moss);position:relative;padding:4px 0}
.menu-l a:after{content:"";position:absolute;left:0;bottom:0;height:1px;width:100%;background:var(--clay);transform:scaleX(0);transform-origin:left;transition:transform .4s var(--ease)}
.menu-l a:hover:after,.menu-l a.on:after{transform:scaleX(1)}
.burger{display:none;width:44px;height:44px;border:1px solid #d9c9ad;background:#fff;cursor:pointer;position:relative}
.burger i{position:absolute;left:12px;right:12px;height:2px;background:var(--moss);transition:transform .4s var(--ease),opacity .3s}
.burger i:nth-child(1){top:15px}.burger i:nth-child(2){top:21px}.burger i:nth-child(3){top:27px}
.open .burger i:nth-child(1){transform:translateY(6px) rotate(45deg)}.open .burger i:nth-child(2){opacity:0}.open .burger i:nth-child(3){transform:translateY(-6px) rotate(-45deg)}
.btn{position:relative;overflow:hidden;display:inline-block;transition:transform .35s var(--ease),box-shadow .35s var(--ease)}
.btn:hover{transform:translateY(-2px);box-shadow:0 16px 30px -14px rgba(180,83,42,.8)}.btn:active{transform:scale(.98)}
.btn:after{content:"";position:absolute;top:0;left:-70%;width:45%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.45),transparent);transform:skewX(-20deg);animation:shine 5s ease-in-out infinite}
@keyframes shine{0%,60%{left:-70%}100%{left:130%}}
.b1{background:var(--clay);color:#fff;text-decoration:none;padding:12px 18px;font-size:14px;font-weight:600;border:0;cursor:pointer;font-family:inherit}
.cta{margin-top:24px;background:var(--clay);color:#fff;padding:16px 26px;font-weight:600;text-decoration:none;font-size:15px}
.cta.alt{background:transparent;border:1px solid #ffffffb0;margin-left:10px}
.hero{position:relative;overflow:hidden;overflow:clip;contain:paint;min-height:82vh;display:flex;align-items:flex-end;color:#fff;background:#3a2a22}
.hero.s{min-height:42vh}
.hero .bg{position:absolute;inset:-8%;background:#3a2a22 var(--im) center/cover;animation:kb 24s ease-in-out infinite alternate}
@keyframes kb{from{transform:scale(1)}to{transform:scale(1.12) translate(-2%,-1.5%)}}
.hero:before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,#00000022 0,#000000a6 100%)}
.hero .in{position:relative;z-index:2;max-width:1000px;margin:0 auto;padding:0 22px 56px;width:100%}
.hero small{display:block;letter-spacing:.28em;font-size:12px;color:#f0c27a;opacity:0;animation:fade 1s var(--ease) .2s forwards}
.hero h1{font-family:PF,Georgia,serif;font-size:clamp(38px,9vw,78px);line-height:1.05;margin:14px 0;max-width:13ch}
.hero.s h1{font-size:clamp(34px,7vw,56px);max-width:none}
.hero h1 em{color:#f0c27a}
.w{display:inline-block;overflow:hidden;vertical-align:top;padding-bottom:.08em}
.w>span{display:inline-block;transform:translateY(115%);animation:up 1.1s var(--ease) forwards;animation-delay:calc(.35s + .09s*var(--i))}
@keyframes up{to{transform:none}}@keyframes fade{to{opacity:1}}
.hero p{max-width:44ch;font-size:18px;color:#f5eadb;opacity:0;transform:translateY(16px);animation:rise 1s var(--ease) 1.1s forwards}
.hero .acts{opacity:0;transform:translateY(16px);animation:rise 1s var(--ease) 1.35s forwards}
@keyframes rise{to{opacity:1;transform:none}}
.wrap{max-width:1000px;margin:0 auto;padding:0 22px}
section{padding:64px 0}
h2{font-family:PF,Georgia,serif;font-size:clamp(28px,5vw,40px);line-height:1.12;margin-bottom:12px;color:var(--moss);position:relative;padding-bottom:16px}
h2:after{content:"";position:absolute;left:0;bottom:0;height:2px;width:56px;background:var(--clay);transform-origin:left;transform:scaleX(0);transition:transform 1s var(--ease) .3s}
.in h2:after{transform:scaleX(1)}
.tc{text-align:center}.tc h2:after{left:50%;margin-left:-28px}
.lead{font-size:18px;max-width:56ch;color:#5d4c43}.tc .lead{margin:0 auto}
.rv{transition:opacity 1s var(--ease),transform 1s var(--ease);transition-delay:var(--d,0s)}
.js .rv{opacity:0;transform:translateY(30px)}.js .rv.in{opacity:1;transform:none}
.split{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.ph{position:relative;overflow:hidden;aspect-ratio:4/5;background:#7a5a46}
.ph:before,.gal div:before,.card .ph2:before{content:"";position:absolute;inset:0;background:var(--im) center/cover;transition:transform 1.6s var(--ease)}
.js .ph:before{transform:scale(1.18)}.js .ph.in:before{transform:scale(1)}
.dark{background:var(--moss);color:#f3ead8}.dark h2{color:#fff}.dark .lead{color:#d9cdb6}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:34px}
.card{background:#fff;border:1px solid #e6d8c0;transition:transform .5s var(--ease),box-shadow .5s var(--ease)}
.card:hover{transform:translateY(-6px);box-shadow:0 26px 40px -26px rgba(36,26,22,.55)}
.card .ph2{position:relative;overflow:hidden;aspect-ratio:4/3;background:#7a5a46}.card:hover .ph2:before{transform:scale(1.08)}
.card div.t{padding:18px}.card b{font-family:PF,Georgia,serif;font-size:20px;color:var(--moss);display:block}.card span{font-size:14px;color:#5d4c43}
.why{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:30px}.why b{display:block;font-family:PF,Georgia,serif;font-size:21px;color:#f0c27a;margin-bottom:6px}.why p{color:#d9cdb6;font-size:15px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:0 48px;margin-top:24px}
.it{display:flex;justify-content:space-between;gap:16px;padding:14px 0;border-bottom:1px solid #d9c9ad;transition:padding .45s var(--ease),border-color .45s}
.it:hover{padding-left:10px;border-color:var(--clay)}
.it b{display:block;font-weight:600;font-size:17px}.it span{font-size:14px;color:#6b5a50}.it em{font-style:normal;font-family:PF,Georgia,serif;font-size:19px;color:var(--clay)}
.cat{grid-column:1/-1;margin-top:26px;letter-spacing:.22em;font-size:12px;color:var(--clay);text-transform:uppercase;font-weight:600}
.note{font-size:13px;color:#7a6a60;margin-top:26px}
.gal{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:30px}
.gal div{position:relative;overflow:hidden;aspect-ratio:1;background:#7a5a46;cursor:zoom-in}.gal div:hover:before{transform:scale(1.1)}
.lb{position:fixed;inset:0;background:rgba(15,10,8,.92);display:none;align-items:center;justify-content:center;z-index:50;cursor:zoom-out}
.lb.show{display:flex;animation:fade2 .35s}.lb div{width:min(92vw,900px);height:80vh;background:var(--im) center/contain no-repeat}
@keyframes fade2{from{opacity:0}}
.book,.cform{background:#fff;border:1px solid #e0d2ba;box-shadow:0 24px 50px -26px rgba(36,26,22,.5);padding:24px;width:100%;max-width:560px;margin:30px auto 0;overflow:hidden;text-align:left}
label{display:block;font-size:13px;font-weight:600;margin:12px 0 6px;color:var(--moss)}
input,select,textarea{display:block;width:100%;max-width:100%;min-width:0;padding:0 13px;border:1px solid #d9c9ad;border-radius:0;font:inherit;font-size:16px;background:#fff;color:var(--ink);-webkit-appearance:none;appearance:none;transition:border-color .3s,box-shadow .3s}
input,select{height:50px}textarea{padding:13px;height:130px;resize:vertical}
input:focus,select:focus,textarea:focus{outline:0;border-color:var(--clay);box-shadow:0 0 0 3px rgba(180,83,42,.18)}
input[type=date]{min-height:50px;line-height:50px;text-align:left}input[type=date]::-webkit-date-and-time-value{text-align:left;min-width:0}
select{background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='8'%3E%3Cpath d='M1 1l6 6 6-6' fill='none' stroke='%232f3a2c' stroke-width='2'/%3E%3C/svg%3E") no-repeat right 14px center}
.slots{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.slot{padding:12px 0;border:1px solid #d9c9ad;background:#fff;font:inherit;font-weight:600;cursor:pointer;color:var(--moss);transition:background .3s,color .3s,border-color .3s}
.slot:hover{border-color:var(--moss)}.slot.on{background:var(--moss);color:#fff;border-color:var(--moss);animation:pop .45s var(--ease)}
@keyframes pop{0%{transform:scale(.9)}60%{transform:scale(1.06)}100%{transform:scale(1)}}
.go{width:100%;margin-top:18px;padding:16px;font-size:15px}
.ok{display:none;margin-top:16px;padding:18px;background:#e9f1e4;border:1px solid #b8d2ab;font-size:15px;align-items:center;gap:14px}.ok.show{display:flex;animation:rise .8s var(--ease)}
.ok svg{flex:none;width:44px;height:44px}.ok circle,.ok path{fill:none;stroke:#2f6b3a;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:140;stroke-dashoffset:140;animation:draw .9s var(--ease) .15s forwards}
.ok path{stroke-dasharray:40;stroke-dashoffset:40;animation-delay:.6s}@keyframes draw{to{stroke-dashoffset:0}}
.err{display:none;margin-top:12px;color:#a02a1a;font-size:14px}.err.show{display:block;animation:shake .4s}@keyframes shake{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.info{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:30px}.info b{display:block;font-family:PF,Georgia,serif;font-size:20px;margin-bottom:6px;color:var(--moss)}.info p{font-size:15px;color:#5d4c43}
.plan{margin-top:28px;aspect-ratio:16/7;background:linear-gradient(135deg,#e8dcc6,#d9c9ad);display:flex;align-items:center;justify-content:center;color:var(--moss);font-family:PF,Georgia,serif;font-size:20px;text-align:center;padding:20px;border:1px solid #d9c9ad}
.team{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:30px}.team b{display:block;font-family:PF,Georgia,serif;font-size:20px;color:var(--moss)}.team span{font-size:14px;color:#6b5a50}
.vp{background:#111;color:#fff;text-align:center;padding:60px 22px}.vp h2{color:#fff;display:inline-block}.vp p{max-width:48ch;margin:0 auto;color:#d9d3c8;font-size:17px}
.vp a{margin-top:22px;background:#f0c27a;color:#111;padding:16px 26px;font-weight:700;text-decoration:none}
footer.f{background:var(--moss);color:#e7dcc6;padding:44px 22px 24px}footer.f .g{max-width:1000px;margin:0 auto;display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:30px}
footer.f b{display:block;font-family:PF,Georgia,serif;font-size:19px;color:#fff;margin-bottom:8px}footer.f p,footer.f a{font-size:14px;color:#cfc3ac;display:block;text-decoration:none;margin:2px 0}footer.f a:hover{color:#fff}
footer.f .c{max-width:1000px;margin:26px auto 0;padding-top:16px;border-top:1px solid #ffffff26;font-size:12px;color:#a99d86}
@media(max-width:760px){
 .burger{display:block}
 .menu-l{position:absolute;left:0;right:0;top:100%;background:var(--cream);flex-direction:column;align-items:stretch;gap:0;padding:6px 22px 18px;border-bottom:1px solid #e3d5bd;max-height:0;overflow:hidden;opacity:0;transition:max-height .5s var(--ease),opacity .3s,padding .4s}
 .open .menu-l{max-height:420px;opacity:1}.menu-l a{padding:13px 0;border-bottom:1px solid #eadfcc;font-size:16px}.menu-l a:after{display:none}
 .split,.cols,.info,.cards,.why,.team,footer.f .g{grid-template-columns:1fr}.ph{aspect-ratio:4/3}.slots{grid-template-columns:repeat(3,1fr)}.gal{grid-template-columns:repeat(2,1fr)}.cta.alt{margin-left:0;margin-top:12px}
}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important}.js .rv{opacity:1;transform:none}.w>span{transform:none}.hero small,.hero p,.hero .acts{opacity:1;transform:none}.js .ph:before{transform:none}h2:after{transform:scaleX(1)}}
"""

JS = """
(function(){
var nav=document.getElementById('nav'),bg=document.getElementById('bg');
document.getElementById('bu').onclick=function(){nav.classList.toggle('open')};
var rv=document.querySelectorAll('.rv');
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});[].forEach.call(rv,function(e){io.observe(e)})}else{[].forEach.call(rv,function(e){e.classList.add('in')})}
setTimeout(function(){[].forEach.call(rv,function(e){e.classList.add('in')})},6000);
var tk=false;function on(){var y=pageYOffset||0,h=document.documentElement.scrollHeight-innerHeight;nav.classList.toggle('sc',y>30);nav.style.setProperty('--p',h>0?Math.min(1,y/h):0);tk=false}
addEventListener('scroll',function(){if(!tk){tk=true;requestAnimationFrame(on)}},{passive:true});on();
[].forEach.call(document.querySelectorAll('.cols .it'),function(e,i){e.style.setProperty('--d',(i%5)*0.07+'s')});
var lb=document.getElementById('lb');
if(lb){[].forEach.call(document.querySelectorAll('.gal div'),function(g){g.onclick=function(){lb.firstChild.style.setProperty('--im',g.style.getPropertyValue('--im'));lb.classList.add('show')}});lb.onclick=function(){lb.classList.remove('show')}}
var sl=document.getElementById('sl');
if(sl){var sel='',d=document.getElementById('d'),t=new Date();t.setDate(t.getDate()+1);d.value=t.toISOString().slice(0,10);d.min=new Date().toISOString().slice(0,10);
['12:00','12:30','13:00','13:30','19:00','19:30','20:00','20:30','21:00','21:30'].forEach(function(h){var b=document.createElement('button');b.type='button';b.className='slot';b.textContent=h;b.onclick=function(){sel=h;[].forEach.call(sl.children,function(x){x.classList.toggle('on',x===b)})};sl.appendChild(b)});
document.getElementById('f').addEventListener('submit',function(e){e.preventDefault();var er=document.getElementById('er'),ok=document.getElementById('ok'),nm=document.getElementById('nm').value.trim();er.className='err';ok.className='ok';
function bad(m){er.textContent=m;void er.offsetWidth;er.className='err show'}
if(!sel){bad('Choisissez une heure.');return}if(!nm){bad('Indiquez votre nom.');return}
var dt=new Date(d.value+'T12:00:00').toLocaleDateString('fr-FR',{weekday:'long',day:'numeric',month:'long'});
ok.innerHTML='<svg viewBox="0 0 52 52"><circle cx="26" cy="26" r="22"/><path d="M16 27l7 7 14-15"/></svg><div></div>';
ok.lastChild.textContent='Merci '+nm+', votre table pour '+document.getElementById('n').value+' personne(s) est réservée le '+dt+' à '+sel+'. (Démonstration : aucune réservation réelle.)';ok.className='ok show';ok.scrollIntoView({behavior:'smooth',block:'center'})})}
var cf=document.getElementById('cf');
if(cf){cf.addEventListener('submit',function(e){e.preventDefault();var er=document.getElementById('er2'),ok=document.getElementById('ok2'),nm=document.getElementById('cn').value.trim(),em=document.getElementById('ce').value.trim(),ms=document.getElementById('cm').value.trim();er.className='err';ok.className='ok';
function bad(m){er.textContent=m;void er.offsetWidth;er.className='err show'}
if(!nm){bad('Indiquez votre nom.');return}if(!/^\\S+@\\S+\\.\\S+$/.test(em)){bad('Indiquez une adresse e-mail valide.');return}if(!ms){bad('Écrivez votre message.');return}
ok.innerHTML='<svg viewBox="0 0 52 52"><circle cx="26" cy="26" r="22"/><path d="M16 27l7 7 14-15"/></svg><div></div>';ok.lastChild.textContent='Merci '+nm+', votre message est bien envoyé. Nous vous répondons sous 24 h. (Démonstration : aucun message réel.)';ok.className='ok show'})}
})();
"""


def words(text, em=None):
    em = em or []
    out, i = [], 0
    for wd in text.split():
        s = f'<span class="w" style="--i:{i}"><span>{wd}</span></span>'
        out.append(f"<em>{s}</em>" if wd in em else s)
        i += 1
    return " ".join(out)


def page(fn, title, body, active, desc, hero=None):
    nav = "".join(f'<a href="{h}"{" class=on" if h == active else ""}>{t}</a>' for h, t in NAV)
    return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} · Maison Aubépine</title><meta name="robots" content="noindex"><meta name="description" content="{desc}">
<script>document.documentElement.className='js'</script><style>{CSS}</style></head><body>
<div class="demo">Site de démonstration réalisé par VITRIA PRO. <a href="../index.html">Voir les offres</a></div>
<div class="nav" id="nav"><a class="logo" href="index.html">Maison Aubépine</a>
<div class="menu-l">{nav}<a class="b1 btn" href="reserver.html">Réserver</a></div>
<button class="burger" id="bu" aria-label="Menu"><i></i><i></i><i></i></button></div>
{body}
<div class="vp"><div class="rv"><h2>Vous avez un restaurant ?</h2><p>Ce site est une démonstration. Le vôtre sera fait sur mesure : votre carte, vos photos, votre ambiance, avec réservation en ligne.</p><a class="btn" href="../rendez-vous.html">Je veux le même site</a></div></div>
<footer class="f"><div class="g"><div><b>Maison Aubépine</b><p>Cuisine de saison, au feu de bois.<br>12 rue des Halles (adresse fictive)</p></div>
<div><b>Horaires</b><p>Mardi au samedi<br>12h – 14h · 19h – 22h<br>Fermé dimanche et lundi</p></div>
<div><b>Le site</b>{"".join(f'<a href="{h}">{t}</a>' for h, t in NAV)}<a href="reserver.html">Réserver</a><a href="mentions.html">Mentions légales</a></div></div>
<div class="c">Site de démonstration · Les noms, adresses et photographies sont fictifs ou illustratifs · Réalisé par VITRIA PRO</div></footer>
<div class="lb" id="lb"><div></div></div>
<script>{JS}</script><script src="../track.js" defer></script></body></html>"""


def hero(img, small, h1, p="", acts="", em=None, small_hero=False):
    cls = "hero s" if small_hero else "hero"
    return f"""<header class="{cls}"><div class="bg" id="bg" style="--im:url({U(IMG[img],1800)})"></div><div class="in"><small>{small}</small><h1>{words(h1, em)}</h1>{f'<p>{p}</p>' if p else ''}{f'<div class="acts">{acts}</div>' if acts else ''}</div></header>"""


pages = {}

# ---- Accueil
pages["index.html"] = page("index.html", "Restaurant, cuisine de saison", hero("salle", "RESTAURANT · CUISINE DE SAISON", "Une table qui sent bon la saison", "Produits du marché, cuisine au feu de bois, vins de petits producteurs.", '<a class="cta btn" href="reserver.html">Réserver une table</a><a class="cta alt btn" href="carte.html">Voir la carte</a>', em=["sent", "bon"]) + f"""
<section><div class="wrap split"><div class="rv"><h2>Une cuisine simple, faite avec ceux qui cultivent</h2><p class="lead">Chaque semaine, la carte change avec ce que nos producteurs nous apportent. Peu de plats, bien faits, servis dans une salle chaleureuse de trente couverts.</p><p style="margin-top:18px"><a href="histoire.html" style="color:var(--clay);font-weight:600">Notre histoire →</a></p></div>
<div class="ph rv" style="--im:url({U(IMG['grill'],1100)});--d:.15s"></div></div></section>
<section class="dark"><div class="wrap"><div class="rv"><h2>Pourquoi on vous attend</h2></div><div class="why">
<div class="rv"><b>Le marché d'abord</b><p>Légumes, viandes et poissons choisis chaque semaine auprès de producteurs voisins.</p></div>
<div class="rv" style="--d:.12s"><b>Le feu de bois</b><p>Les grillades et les cuissons lentes se font sur braise, devant vous.</p></div>
<div class="rv" style="--d:.24s"><b>Une carte courte</b><p>Moins de plats, mieux faits, et des suggestions qui changent au fil des jours.</p></div></div></div></section>
<section><div class="wrap"><div class="rv tc"><h2>Les incontournables</h2><p class="lead">Trois plats que nos clients redemandent.</p></div><div class="cards">
<a class="card rv" href="carte.html" style="text-decoration:none"><div class="ph2" style="--im:url({U(IMG['viande'])})"></div><div class="t"><b>Entrecôte au feu de bois</b><span>Frites maison, sauce au poivre</span></div></a>
<a class="card rv" href="carte.html" style="text-decoration:none;--d:.12s"><div class="ph2" style="--im:url({U(IMG['salade'])})"></div><div class="t"><b>Burrata, tomates anciennes</b><span>Huile d'olive, basilic du jardin</span></div></a>
<a class="card rv" href="carte.html" style="text-decoration:none;--d:.24s"><div class="ph2" style="--im:url({U(IMG['assiette'])})"></div><div class="t"><b>Pêche du jour</b><span>Légumes rôtis, beurre blanc</span></div></a></div></div></section>
<section style="background:var(--sand)"><div class="wrap tc"><div class="rv"><h2>Réservez votre table</h2><p class="lead">En quelques secondes, à toute heure, depuis votre téléphone.</p><a class="cta btn" href="reserver.html" style="display:inline-block">Réserver</a></div>
<div class="info"><div class="rv" style="text-align:left"><b>Horaires</b><p>Mardi au samedi<br>12h – 14h et 19h – 22h</p></div><div class="rv" style="--d:.12s;text-align:left"><b>Adresse</b><p>12 rue des Halles<br>Adresse fictive de démonstration</p></div><div class="rv" style="--d:.24s;text-align:left"><b>Contact</b><p><a href="contact.html" style="color:var(--clay);font-weight:600">Nous écrire →</a></p></div></div></div></section>""", "index.html", "Démonstration d'un site de restaurant réalisé par VITRIA PRO.")

# ---- Carte
def item(n, d, p):
    return f'<div class="it rv"><div><b>{n}</b><span>{d}</span></div><em>{p}</em></div>'

carte = (
    ("Entrées", [("Burrata, tomates anciennes", "Huile d'olive, basilic du jardin", "13"), ("Velouté de potimarron", "Châtaignes, crème fumée", "11"), ("Œuf parfait, champignons", "Crème de persil, noisettes", "12"), ("Terrine de campagne", "Pickles maison, pain grillé", "11")]),
    ("Plats", [("Pluma de porc, jus corsé", "Purée au beurre noisette", "24"), ("Pêche du jour", "Légumes rôtis, beurre blanc", "26"), ("Risotto aux cèpes", "Parmesan, huile de sauge", "21"), ("Entrecôte au feu de bois", "Frites maison, sauce au poivre", "28"), ("Légumes du marché grillés", "Houmous, graines torréfiées", "19"), ("Souris d'agneau confite", "Polenta crémeuse, jus au thym", "27")]),
    ("Desserts", [("Tarte fine aux pommes", "Glace vanille", "9"), ("Mousse au chocolat", "Fleur de sel", "9"), ("Crème brûlée à la verveine", "", "9"), ("Fromages affinés", "Sélection du moment", "11")]),
    ("Boissons", [("Vins au verre", "Sélection de petits producteurs, à partir de", "5"), ("Bières artisanales", "Pression et bouteilles, à partir de", "5"), ("Cocktails sans alcool", "Fruits et herbes du jardin", "7")]),
)
cb = "".join(f'<div class="cat rv">{c}</div>' + "".join(item(*i) for i in its) for c, its in carte)
pages["carte.html"] = page("carte.html", "La carte", hero("plat", "LA CARTE DU MOMENT", "Ce que le marché nous a apporté", "Renouvelée chaque semaine. Prix en euros, service compris.", small_hero=True) + f"""
<section><div class="wrap"><div class="rv"><h2>Menu du midi</h2><p class="lead">Du mardi au vendredi : plat du jour et dessert, <b>19 €</b>. Entrée, plat et dessert, <b>25 €</b>.</p></div>
<div class="cols">{cb}</div><p class="note rv">Merci de nous signaler toute allergie ou intolérance. Carte indicative de démonstration : plats et prix fictifs.</p></div></section>
<section style="background:var(--sand)"><div class="wrap tc"><div class="rv"><h2>Une envie ? Réservez</h2><a class="cta btn" href="reserver.html" style="display:inline-block">Réserver une table</a></div></div></section>""", "carte.html", "La carte du restaurant Maison Aubépine (démonstration).")

# ---- Galerie
gal = [IMG[k] for k in ("salle", "plat", "grill", "salade", "salle2", "assiette", "viande", "marche")]
gl = "".join(f'<div class="rv" style="--im:url({U(i, 1000)});--d:{(n % 3) * 0.1}s"></div>' for n, i in enumerate(gal))
pages["galerie.html"] = page("galerie.html", "Galerie", hero("salle2", "GALERIE", "La salle, les plats, les gestes", small_hero=True) + f"""
<section><div class="wrap"><div class="rv"><h2>En images</h2><p class="lead">Touchez une photo pour l'agrandir.</p></div><div class="gal">{gl}</div></div></section>""", "galerie.html", "Galerie photo du restaurant Maison Aubépine (démonstration).")

# ---- Histoire
pages["histoire.html"] = page("histoire.html", "Notre histoire", hero("marche", "NOTRE HISTOIRE", "Des producteurs, un feu, une salle", small_hero=True) + f"""
<section><div class="wrap split"><div class="rv"><h2>Ouvert pour cuisiner autrement</h2><p class="lead">Maison Aubépine est née d'une idée simple : cuisiner ce qui pousse près de chez nous, au bon moment, sans en faire des tonnes. Une salle de trente couverts, un four à bois, une carte qui tient sur une page.</p></div><div class="ph rv" style="--im:url({U(IMG['grill'],1100)});--d:.15s"></div></div></section>
<section class="dark"><div class="wrap"><div class="rv"><h2>Ceux qui font la maison</h2></div><div class="team">
<div class="rv"><b>Marc</b><span style="color:#d9cdb6">Chef et fondateur</span></div><div class="rv" style="--d:.12s"><b>Léa</b><span style="color:#d9cdb6">Cheffe de salle et sommelière</span></div><div class="rv" style="--d:.24s"><b>Hugo</b><span style="color:#d9cdb6">Second de cuisine, feu de bois</span></div></div></div></section>
<section><div class="wrap tc"><div class="rv"><h2>Venez nous rencontrer</h2><a class="cta btn" href="reserver.html" style="display:inline-block">Réserver une table</a></div></div></section>""", "histoire.html", "L'histoire du restaurant Maison Aubépine (démonstration).")

# ---- Réserver
pages["reserver.html"] = page("reserver.html", "Réserver", hero("salle", "RÉSERVATION", "Réserver une table", "Choisissez le jour, l'heure et le nombre de personnes.", small_hero=True) + """
<section style="background:var(--sand)"><div class="wrap tc"><div class="rv"><h2>Votre table en quelques secondes</h2><p class="lead">Confirmation immédiate. Pour plus de 8 personnes ou une privatisation, écrivez-nous depuis la page contact.</p></div>
<form class="book rv" id="f" novalidate><label for="d">Date</label><input type="date" id="d"><label for="n">Nombre de personnes</label><select id="n"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7</option><option>8</option></select>
<label>Heure</label><div class="slots" id="sl"></div><label for="nm">Nom</label><input id="nm" placeholder="Votre nom" autocomplete="name"><label for="tl">Téléphone</label><input id="tl" type="tel" placeholder="Pour vous joindre si besoin" autocomplete="tel">
<div class="err" id="er"></div><button class="go b1 btn" type="submit">Réserver ma table</button><div class="ok" id="ok"></div></form></div></section>""", "reserver.html", "Réserver une table au restaurant Maison Aubépine (démonstration).")

# ---- Contact
pages["contact.html"] = page("contact.html", "Contact", hero("salle2", "CONTACT", "Une question ? Écrivez-nous", small_hero=True) + """
<section><div class="wrap"><div class="info"><div class="rv"><b>Adresse</b><p>12 rue des Halles<br>Adresse fictive de démonstration</p></div><div class="rv" style="--d:.12s"><b>Téléphone</b><p>01 23 45 67 89<br>Numéro fictif de démonstration</p></div><div class="rv" style="--d:.24s"><b>Horaires</b><p>Mardi au samedi<br>12h – 14h et 19h – 22h<br>Fermé dimanche et lundi</p></div></div>
<div class="plan rv">Plan d'accès et itinéraire en un geste<br>(carte intégrée sur votre vrai site)</div></div></section>
<section style="background:var(--sand)"><div class="wrap tc"><div class="rv"><h2>Nous écrire</h2><p class="lead">Groupes, privatisation, allergies, questions : nous répondons sous 24 h.</p></div>
<form class="cform rv" id="cf" novalidate><label for="cn">Nom</label><input id="cn" autocomplete="name"><label for="ce">E-mail</label><input id="ce" type="email" autocomplete="email"><label for="cm">Message</label><textarea id="cm"></textarea>
<div class="err" id="er2"></div><button class="go b1 btn" type="submit">Envoyer le message</button><div class="ok" id="ok2"></div></form></div></section>""", "contact.html", "Contacter le restaurant Maison Aubépine (démonstration).")

# ---- Mentions
pages["mentions.html"] = page("mentions.html", "Mentions légales", hero("salle", "MENTIONS LÉGALES", "Mentions légales", small_hero=True) + """
<section><div class="wrap"><div class="rv"><h2>Site de démonstration</h2><p class="lead">Ce site est une démonstration réalisée par VITRIA PRO. Maison Aubépine est un restaurant fictif : les noms, adresses, numéros, plats, prix et photographies sont fictifs ou illustratifs. Sur votre site, cette page contient vos informations légales réelles (raison sociale, adresse, contact, hébergeur, données personnelles).</p></div></div></section>""", "", "Mentions légales (démonstration).")

os.makedirs(OUT, exist_ok=True)
for fn, html in pages.items():
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
print(len(pages), "pages", sum(len(h) for h in pages.values()) // 1024, "Ko")
