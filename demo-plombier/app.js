
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
 pan.innerHTML='<h3>'+d.t+'</h3><p class="do">'+d.do+'</p><div class="meta"><span><b>'+d.p+'</b>Tarif annoncé</span><span><b>'+d.e.split(' ')[0]+(d.e.indexOf('Sur place')==0?'':'')+'</b></span></div><div class="acts"><a class="btn b-h" href="tel:+33199001234">Appeler le 01 99 00 12 34</a><a class="btn b-o" href="devis.html?type='+k+'">Planifier un créneau</a></div>';
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
