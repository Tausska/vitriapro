
(function(){
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var hd=$('.hd');var b=$('.bg');if(b)b.onclick=function(){hd.classList.toggle('op')};
/* triage */
var T={
fuite:{t:'Fuga de agua',do:'Primero, cierre la llave de paso (bajo el fregadero o cerca del medidor). Seque y no toque los enchufes eléctricos mojados.',p:'desde 89 €',e:'En el lugar en 45 min durante el día'},
bouchon:{t:'Cañería obstruida',do:'Evite el destapacañerías químico: daña los tubos y complica el trabajo. No vierta nada, llámenos.',p:'desde 79 €',e:'En el lugar en 1 h durante el día'},
chaudeau:{t:'Sin agua caliente',do:'Verifique que el interruptor del calentador no haya saltado. Si vuelve a saltar, no lo rearme y llámenos.',p:'49 € el diagnóstico',e:'Se descuenta si encarga la obra'},
autre:{t:'Otra necesidad',do:'Baño, grifería, instalación: cuéntenos su proyecto, recibe un presupuesto antes de cualquier intervención.',p:'Presupuesto gratis',e:'Respuesta en 24 h'}};
var pan=$('#pan'),dg=$('#dg');
$$('.tri button').forEach(function(bt){bt.onclick=function(){
 var k=bt.dataset.k,d=T[k];$$('.tri button').forEach(function(x){x.setAttribute('aria-pressed',x===bt)});
 if(dg)dg.setAttribute('data-t',k);
 pan.innerHTML='<h3>'+d.t+'</h3><p class="do">'+d.do+'</p><div class="meta"><span><b>'+d.p+'</b>Precio anunciado</span><span><b>'+d.e.split(' ')[0]+(d.e.indexOf('Sur place')==0?'':'')+'</b></span></div><div class="acts"><a class="btn b-h" href="tel:+33199001234">Llamar al 01 99 00 12 34</a><a class="btn b-o" href="devis.html?type='+k+'">Programar un horario</a></div>';
 pan.querySelector('.meta').innerHTML='<span><b>'+d.p+'</b>Precio anunciado</span><span><b style="font-size:20px;line-height:1.1">'+d.e+'</b></span>';
 pan.classList.add('show');pan.style.animation='none';void pan.offsetWidth;pan.style.animation='';
}});
/* estimation */
var E={fuite:89,bouchon:79,robinet:69,chauffeeau:290,chaudiere:95,sdb:0};
var es=$('#es');
if(es){var sv=es.querySelector('select'),mode='day',out=$('#res');
 function calc(){var base=E[sv.value];var r;
  if(sv.value==='sdb'){r='<b>A presupuesto</b><span>Visita gratis, precio firme antes de la obra.</span>';}
  else{var v=Math.round(base*(mode==='night'?1.3:1));var lab=sv.value==='chauffeeau'?'Solo instalación, sin incluir el tanque.':'Mano de obra y desplazamiento incluidos, repuestos aparte.';
   r='<b>desde '+v+' €</b><span>'+lab+(mode==='night'?' Recargo del 30 % de noche y fin de semana.':'')+' Estimación indicativa.</span>';}
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
 $('#n1').onclick=function(){if(!data.type){bad('Elija el tipo de intervención.');return}show(2)};
 $('#n2').onclick=function(){if(!data.slot){bad('Elija un horario.');return}show(3)};
 $('#p2').onclick=function(){show(1)};$('#p3').onclick=function(){show(2)};
 $('#send').onclick=function(){var nm=$('#nm').value.trim(),tl=$('#tl').value.trim(),vl=$('#vl').value.trim();
  if(!nm){bad('Indique su nombre.');return}if(tl.replace(/\D/g,'').length<9){bad('Indique un número de teléfono válido.');return}if(!vl){bad('Indique su localidad.');return}
  var dt=new Date(d.value+'T12:00:00').toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long'});
  var ok=$('#ok');ok.textContent='Gracias '+nm+'. Solicitud registrada: '+data.label.toLowerCase()+' en '+vl+', el '+dt+', horario '+data.slot+'. Lo llamamos al '+tl+' para confirmar. (Demostración: ninguna solicitud real.)';
  ok.className='ok show';$('#er').className='er';$$('.stepbox',fq).forEach(function(s){s.style.display='none'});ok.scrollIntoView({behavior:'smooth',block:'center'})};
 show(1)}
/* contact */
var cf=$('#cf');
if(cf){cf.addEventListener('submit',function(e){e.preventDefault();var er=$('#er2'),ok=$('#ok2'),nm=$('#cn').value.trim(),em=$('#ce').value.trim(),ms=$('#cm').value.trim();er.className='er';ok.className='ok';
 function bad(m){er.textContent=m;er.className='er show'}
 if(!nm)return bad('Indique su nombre.');if(!/^\S+@\S+\.\S+$/.test(em))return bad('Indique un correo electrónico válido.');if(!ms)return bad('Escriba su mensaje.');
 ok.textContent='Gracias '+nm+', su mensaje fue enviado. Le respondemos en 24 h. (Demostración: ningún mensaje real.)';ok.className='ok show'})}
})();
