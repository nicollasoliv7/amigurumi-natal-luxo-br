(function(){
  /* ===================== CONFIGURAÇÕES ===================== */
  var VSL_URL = '';            // VSL: cole aqui a URL de incorporação (ex.: https://player.vimeo.com/video/SEU_ID). Vazio = só a imagem.
  var MUSICA_URL = '';         // Opcional: URL de um .mp3 de música de fundo. Vazio = botão escondido.
  var HORAS_OFERTA = 5;        // Duração do contador dos bônus (horas), igual ao original.
  var CHAVE_RELOGIO = 'amigurumis_timer_end';
  /* ======================================================== */

  var lp = document.querySelector('.am-lp');
  var reduz = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  lp.setAttribute('data-vivo', '');

  /* Aparecer ao rolar */
  var aparecem = document.querySelectorAll('.am-aparece');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('am-visto'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    aparecem.forEach(function(el){ io.observe(el); });
  } else { aparecem.forEach(function(el){ el.classList.add('am-visto'); }); }

  /* Faixas de modelos (marquee infinito) */
  document.querySelectorAll('.am-pista').forEach(function(p){
    Array.prototype.slice.call(p.children).forEach(function(li){
      var c = li.cloneNode(true); c.setAttribute('data-copia',''); c.setAttribute('aria-hidden','true'); p.appendChild(c);
    });
  });
  document.querySelectorAll('.am-fila').forEach(function(f){
    f.addEventListener('touchstart', function(){ f.classList.add('am-tocada'); }, { passive: true });
    f.addEventListener('touchend', function(){ setTimeout(function(){ f.classList.remove('am-tocada'); }, 1200); });
  });

  /* Abas */
  var abas = Array.prototype.slice.call(document.querySelectorAll('.am-pestana'));
  function ativar(aba){
    abas.forEach(function(a){
      var sel = a === aba;
      a.setAttribute('aria-selected', sel ? 'true' : 'false'); a.tabIndex = sel ? 0 : -1;
      var p = document.getElementById(a.getAttribute('aria-controls'));
      if (sel) { p.hidden = false; p.classList.remove('am-entra'); void p.offsetWidth; p.classList.add('am-entra'); } else { p.hidden = true; }
    });
  }
  abas.forEach(function(a, i){
    a.addEventListener('click', function(){ ativar(a); });
    a.addEventListener('keydown', function(e){
      var n = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (n) { e.preventDefault(); var t = abas[(i + n + abas.length) % abas.length]; ativar(t); t.focus(); }
    });
  });

  /* FAQ */
  document.querySelectorAll('.am-faq-q').forEach(function(q){
    var a = document.getElementById(q.getAttribute('aria-controls'));
    a.style.maxHeight = '0px';
    q.addEventListener('click', function(){
      var abrir = q.getAttribute('aria-expanded') !== 'true';
      q.setAttribute('aria-expanded', abrir ? 'true' : 'false');
      a.classList.toggle('am-abierta', abrir);
      a.style.maxHeight = abrir ? a.scrollHeight + 'px' : '0px';
    });
  });

  /* Carrosséis (girando sozinhos, com setas e arrastar) */
  document.querySelectorAll('.am-riel').forEach(function(riel){
    var ul = riel.querySelector('ul');
    var orig = Array.prototype.slice.call(ul.children);
    if (!orig.length) return;
    if (reduz) {
      wireSetas(riel, function(d){ riel.scrollBy({ left: d * passo(), behavior: 'smooth' }); });
      return;
    }
    orig.forEach(function(li){ var c = li.cloneNode(true); c.setAttribute('data-copia',''); c.setAttribute('aria-hidden','true'); c.setAttribute('inert',''); ul.appendChild(c); });
    orig.forEach(function(li){ var c = li.cloneNode(true); c.setAttribute('data-copia',''); c.setAttribute('aria-hidden','true'); c.setAttribute('inert',''); ul.appendChild(c); });
    riel.setAttribute('data-girando','');
    riel.style.scrollBehavior = 'auto';
    var pos = 0, vel = 0.35, pausado = false, arrastando = false, x0 = 0, p0 = 0, alvo = null, retomar;
    function largura(){ return orig.length ? (ul.children[orig.length].offsetLeft - ul.children[0].offsetLeft) : 0; }
    function passo(){ var li = ul.children[0]; return li.getBoundingClientRect().width + 18; }
    function norm(){ var w = largura(); if (w > 0) { while (pos >= w) pos -= w; while (pos < 0) pos += w; } }
    function pausa(ms){ pausado = true; clearTimeout(retomar); retomar = setTimeout(function(){ pausado = false; }, ms || 3500); }
    function tick(){
      if (alvo !== null) { var d = alvo - pos; if (Math.abs(d) < 0.6) { pos = alvo; alvo = null; } else pos += d * 0.14; }
      else if (!pausado && !arrastando) pos += vel;
      norm(); riel.scrollLeft = pos; requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
    riel.addEventListener('mouseenter', function(){ pausado = true; clearTimeout(retomar); });
    riel.addEventListener('mouseleave', function(){ pausa(600); });
    riel.addEventListener('pointerdown', function(e){ arrastando = true; alvo = null; x0 = e.clientX; p0 = pos; riel.setAttribute('data-arrastrando',''); try { riel.setPointerCapture(e.pointerId); } catch(_){} });
    riel.addEventListener('pointermove', function(e){ if (arrastando) { pos = p0 - (e.clientX - x0); } });
    function solta(){ if (!arrastando) return; arrastando = false; riel.removeAttribute('data-arrastrando'); pausa(3000); }
    riel.addEventListener('pointerup', solta); riel.addEventListener('pointercancel', solta);
    riel.addEventListener('keydown', function(e){ if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); ir(e.key === 'ArrowRight' ? 1 : -1); } });
    function ir(d){ pausa(4000); var s = passo(); alvo = (alvo !== null ? alvo : pos) + d * s; }
    wireSetas(riel, ir);
  });
  function wireSetas(riel, fn){
    document.querySelectorAll('.am-flechita[aria-controls="' + riel.id + '"]').forEach(function(b){
      b.addEventListener('click', function(){ fn(parseInt(b.getAttribute('data-dir'), 10)); });
    });
  }

  /* Contador de 5 horas (persistente) */
  var fim = parseInt(localStorage.getItem(CHAVE_RELOGIO) || '0', 10);
  if (!fim) { fim = Date.now() + HORAS_OFERTA * 3600 * 1000; try { localStorage.setItem(CHAVE_RELOGIO, String(fim)); } catch(_){} }
  var eh = document.querySelector('[data-h]'), em = document.querySelector('[data-m]'), es = document.querySelector('[data-s]'), ef = document.querySelector('[data-fija-reloj]');
  function dois(n){ return (n < 10 ? '0' : '') + n; }
  function relogio(){
    var r = Math.max(0, fim - Date.now());
    var h = Math.floor(r / 3600000), m = Math.floor(r % 3600000 / 60000), s = Math.floor(r % 60000 / 1000);
    eh.textContent = dois(h); em.textContent = dois(m); es.textContent = dois(s);
    if (ef) ef.textContent = dois(h) + ':' + dois(m) + ':' + dois(s);
    if (r <= 0) { lp.setAttribute('data-estado','vencido'); return; }
    setTimeout(relogio, 1000 - (Date.now() % 1000));
  }
  relogio();

  /* Barra fixa no celular */
  var fija = document.getElementById('am-fija'), heroe = document.getElementById('am-heroe'), oferta = document.getElementById('oferta'), fin = document.getElementById('am-fin');
  var vis = { heroe: true, oferta: false, fin: false };
  function barra(){
    var on = !vis.heroe && !vis.oferta && !vis.fin;
    fija.setAttribute('data-visible', on ? '1' : '0');
    if (on) { fija.removeAttribute('inert'); fija.removeAttribute('aria-hidden'); } else { fija.setAttribute('inert',''); fija.setAttribute('aria-hidden','true'); }
    document.documentElement.classList.toggle('am-con-barra', on);
  }
  if ('IntersectionObserver' in window) {
    var io2 = new IntersectionObserver(function(es){
      es.forEach(function(e){ vis[e.target === heroe ? 'heroe' : e.target === oferta ? 'oferta' : 'fin'] = e.isIntersecting; });
      barra();
    });
    [heroe, oferta, fin].forEach(function(el){ io2.observe(el); });
  }

  /* Neve */
  function neve(cv){
    if (reduz) return;
    var ctx = cv.getContext('2d'), flocos = [], W = 0, H = 0, dpr = Math.min(window.devicePixelRatio || 1, 2), ativo = true;
    function tam(){ var r = cv.getBoundingClientRect(); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr,0,0,dpr,0,0); }
    tam(); window.addEventListener('resize', tam);
    var n = Math.round(Math.min(90, W / 14));
    for (var i = 0; i < n; i++) flocos.push({ x: Math.random() * W, y: Math.random() * H, r: Math.random() * 2.2 + 0.6, v: Math.random() * 0.5 + 0.25, d: Math.random() * Math.PI * 2, o: Math.random() * 0.5 + 0.35 });
    new IntersectionObserver(function(es){ ativo = es[0].isIntersecting; }).observe(cv);
    (function loop(){
      if (ativo) {
        ctx.clearRect(0, 0, W, H);
        flocos.forEach(function(f){
          f.y += f.v; f.d += 0.01; f.x += Math.sin(f.d) * 0.35;
          if (f.y > H + 4) { f.y = -4; f.x = Math.random() * W; }
          ctx.beginPath(); ctx.arc(f.x, f.y, f.r, 0, Math.PI * 2); ctx.fillStyle = 'rgba(255,255,255,' + f.o + ')'; ctx.fill();
        });
      }
      requestAnimationFrame(loop);
    })();
  }
  document.querySelectorAll('.am-nieve').forEach(neve);

  /* VSL (vazia por enquanto) */
  var marco = document.querySelector('.am-medio-marco'), toque = document.querySelector('.am-video-toque'), aviso = document.querySelector('.am-video-sonido');
  if (!VSL_URL) {
    /* sem VSL: o quadro fica só com a imagem até você colar a URL acima */
  } else {
    toque.addEventListener('click', function(){
      var f = document.createElement('iframe');
      f.className = 'am-medio-video'; f.title = 'Vídeo: veja a coleção por dentro';
      f.allow = 'autoplay; fullscreen; picture-in-picture; encrypted-media'; f.setAttribute('allowfullscreen','');
      f.src = VSL_URL + (VSL_URL.indexOf('?') < 0 ? '?' : '&') + 'autoplay=1';
      marco.appendChild(f);
      setTimeout(function(){ f.setAttribute('data-listo',''); }, 300);
      toque.remove(); aviso.remove();
    });
  }

  /* Música de fundo (opcional) */
  var bs = document.querySelector('.am-pie-sonido');
  if (MUSICA_URL && bs) {
    var au = new Audio(MUSICA_URL); au.loop = true; au.volume = 0.35;
    bs.hidden = false;
    bs.addEventListener('click', function(){
      if (au.paused) { au.play(); bs.setAttribute('data-estado','tocando'); bs.setAttribute('aria-pressed','true'); }
      else { au.pause(); bs.setAttribute('data-estado','mudo'); bs.setAttribute('aria-pressed','false'); }
    });
  }
})();
