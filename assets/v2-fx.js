// v2-fx-classic.js (global, généré) — utilitaires de motion pour le portfolio V2 (ease mécanique, reveals, wipes, curseur)
const EASE = 'cubic-bezier(0.7,0,0.3,1)';
const GLYPHS = '▓▒░#%&@$01';

function initCursor() {
  if (window.matchMedia && window.matchMedia('(pointer: coarse)').matches) return;
  if (document.getElementById('mt-cursor')) return;
  const c = document.createElement('div');
  c.id = 'mt-cursor';
  c.style.cssText = 'position:fixed;top:0;left:0;width:14px;height:14px;border:1px solid #fff;z-index:9999;pointer-events:none;mix-blend-mode:difference;transform:translate(-100px,-100px);transition:width .14s ' + EASE + ',height .14s ' + EASE;
  const dot = document.createElement('div');
  dot.style.cssText = 'position:absolute;top:50%;left:50%;width:2px;height:2px;background:#fff;transform:translate(-50%,-50%)';
  c.appendChild(dot);
  document.body.appendChild(c);
  let tx = -100, ty = -100, x = -100, y = -100, w = 14;
  document.addEventListener('mousemove', (e) => { tx = e.clientX; ty = e.clientY; });
  document.addEventListener('mouseover', (e) => {
    const hot = e.target.closest && e.target.closest('a,button,input,textarea,[data-hot]');
    w = hot ? 34 : 14;
    c.style.width = w + 'px'; c.style.height = w + 'px';
  });
  (function loop() {
    x += (tx - x) * 0.22; y += (ty - y) * 0.22;
    c.style.transform = 'translate(' + (x - w / 2) + 'px,' + (y - w / 2) + 'px)';
    requestAnimationFrame(loop);
  })();
}

function scramble(el, duration = 700) {
  const orig = el.dataset.scrambleText || (el.dataset.scrambleText = el.textContent);
  const start = performance.now();
  (function tick(now) {
    const p = Math.min((now - start) / duration, 1);
    const settled = Math.floor(orig.length * p);
    let out = orig.slice(0, settled);
    for (let i = settled; i < orig.length; i++) out += orig[i] === ' ' ? ' ' : GLYPHS[(Math.random() * GLYPHS.length) | 0];
    el.textContent = out;
    if (p < 1) requestAnimationFrame(tick);
  })(performance.now());
}

function initReveals() {
  const t0 = performance.now();
  const EASE_T = ' cubic-bezier(0.7,0,0.3,1) ';
  const inView = (el, pad) => {
    const r = el.getBoundingClientRect();
    return r.top < window.innerHeight - (pad === undefined ? 40 : pad) && r.bottom > 0 && (r.width > 0 || r.height > 0);
  };
  const check = () => {
    document.querySelectorAll('[data-anim]').forEach((el) => {
      if (el.__mtDone) return;
      if (!el.__mtInit) {
        el.__mtInit = true;
        if (inView(el) && performance.now() - t0 > 1500) { el.__mtDone = true; return; }
        el.style.opacity = '0'; el.style.transform = 'translateY(18px)';
        if (!inView(el)) return;
      }
      if (inView(el)) {
        el.__mtDone = true;
        const d = (Number(el.dataset.anim) || 0) * 90;
        el.style.transition = 'opacity .5s' + EASE_T + d + 'ms, transform .5s' + EASE_T + d + 'ms';
        requestAnimationFrame(() => { el.style.opacity = '1'; el.style.transform = 'translateY(0)'; });
      }
    });
    document.querySelectorAll('[data-clip]').forEach((el) => {
      if (el.__mtDone) return;
      if (!el.__mtInit) {
        el.__mtInit = true;
        if (inView(el, 20) && performance.now() - t0 > 1500) { el.__mtDone = true; return; }
        el.style.clipPath = 'inset(0 0 100% 0)';
        if (!inView(el, 20)) return;
      }
      if (inView(el, 20)) {
        el.__mtDone = true;
        el.style.transition = 'clip-path .6s steps(8,end)';
        requestAnimationFrame(() => { el.style.clipPath = 'inset(0 0 0% 0)'; });
      }
    });
    document.querySelectorAll('[data-scramble]').forEach((el) => {
      if (el.__mtDone) return;
      if (inView(el, 10)) { el.__mtDone = true; scramble(el); }
    });
  };
  window.addEventListener('scroll', check, { passive: true });
  window.addEventListener('resize', check);
  setInterval(check, 400);
  check();
}

function revealHero(baseDelay = 0) {
  document.querySelectorAll('[data-line]').forEach((el, i) => {
    const idx = el.dataset.lineIndex !== undefined ? Number(el.dataset.lineIndex) : i;
    el.style.transform = 'translateY(115%)';
    el.style.transition = 'transform .7s ' + EASE + ' ' + (baseDelay + idx * 100) + 'ms';
    requestAnimationFrame(() => requestAnimationFrame(() => { el.style.transform = 'translateY(0)'; }));
  });
  document.querySelectorAll('[data-fade]').forEach((el, i) => {
    el.style.opacity = '0'; el.style.transform = 'translateY(14px)';
    const d = baseDelay + 350 + i * 90;
    el.style.transition = 'opacity .5s ' + EASE + ' ' + d + 'ms, transform .5s ' + EASE + ' ' + d + 'ms';
    requestAnimationFrame(() => requestAnimationFrame(() => { el.style.opacity = '1'; el.style.transform = 'translateY(0)'; }));
  });
}

function playIntro(done) {
  const ov = document.createElement('div');
  ov.style.cssText = 'position:fixed;inset:0;background:#000;color:#fff;z-index:10000;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;transition:transform .5s ' + EASE;
  ov.innerHTML = '<div style="font:700 12px var(--font-mono,monospace);letter-spacing:.2em;text-transform:uppercase">Mickaël Teixeira<sup>®</sup></div>'
    + '<div style="width:220px;height:1px;background:#1f1f1f;position:relative"><div id="mt-bar" style="position:absolute;left:0;top:-1px;height:3px;background:#fff;width:0%"></div></div>'
    + '<div id="mt-count" style="font:400 10px var(--font-mono,monospace);letter-spacing:.2em;color:#6b6b6b">000%</div>'
    + '<div style="position:absolute;bottom:24px;left:24px;font:400 9px var(--font-mono,monospace);letter-spacing:.2em;color:#454545;text-transform:uppercase">Portfolio — Vol.02</div>'
    + '<div style="position:absolute;bottom:24px;right:24px;font:400 9px var(--font-mono,monospace);letter-spacing:.2em;color:#454545">44°50\'16"N 0°34\'46"W</div>';
  document.body.appendChild(ov);
  const bar = ov.querySelector('#mt-bar'), count = ov.querySelector('#mt-count');
  const t0 = performance.now(), DUR = 1000;
  (function tick(now) {
    const p = Math.min((now - t0) / DUR, 1);
    const stepped = Math.floor(p * 10) / 10;
    bar.style.width = (stepped * 100) + '%';
    count.textContent = String(Math.floor(stepped * 100)).padStart(3, '0') + '%';
    if (p < 1) requestAnimationFrame(tick);
    else { ov.style.transform = 'translateY(-100%)'; setTimeout(() => { ov.remove(); done && done(); }, 500); }
  })(performance.now());
}

function playWipeIn(done) {
  const ov = document.createElement('div');
  ov.style.cssText = 'position:fixed;inset:0;background:#000;z-index:10000;border-bottom:1px solid #fff;transition:transform .45s ' + EASE;
  document.body.appendChild(ov);
  requestAnimationFrame(() => requestAnimationFrame(() => { ov.style.transform = 'translateY(-100%)'; }));
  setTimeout(() => { ov.remove(); done && done(); }, 480);
}

function wipeTo(href) {
  const ov = document.createElement('div');
  ov.style.cssText = 'position:fixed;inset:0;background:#000;z-index:10000;transform:translateY(100%);border-top:1px solid #fff;display:flex;align-items:center;justify-content:center;transition:transform .38s ' + EASE;
  ov.innerHTML = '<span style="font:500 10px var(--font-mono,monospace);letter-spacing:.25em;color:#6b6b6b;text-transform:uppercase">Chargement —</span>';
  document.body.appendChild(ov);
  requestAnimationFrame(() => requestAnimationFrame(() => { ov.style.transform = 'translateY(0)'; }));
  setTimeout(() => { window.location.href = href; }, 420);
}

function initHoverPreview() {
  const rows = Array.from(document.querySelectorAll('[data-preview]'));
  if (!rows.length) return;
  let box = document.getElementById('mt-preview');
  if (!box) {
    box = document.createElement('div');
    box.id = 'mt-preview';
    box.style.cssText = 'position:fixed;top:0;left:0;width:280px;height:190px;border:1px solid var(--border-strong,#454545);background:#000;z-index:800;pointer-events:none;overflow:hidden;display:none';
    box.innerHTML = '<img style="width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.15)" alt=""><div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.45) 0 1px,transparent 1px 3px)"></div><span style="position:absolute;bottom:6px;right:8px;font:400 9px var(--font-mono,monospace);letter-spacing:.15em;color:#fff;mix-blend-mode:difference;text-transform:uppercase"></span>';
    document.body.appendChild(box);
  }
  const img = box.querySelector('img'); const cap = box.querySelector('span');
  let tx = 0, ty = 0, x = 0, y = 0, on = false;
  document.addEventListener('mousemove', (e) => { tx = e.clientX + 26; ty = e.clientY + 22; });
  (function loop() {
    x += (tx - x) * 0.18; y += (ty - y) * 0.18;
    if (on) box.style.transform = 'translate(' + Math.min(x, window.innerWidth - 300) + 'px,' + Math.min(y, window.innerHeight - 210) + 'px)';
    requestAnimationFrame(loop);
  })();
  rows.forEach((r) => {
    r.addEventListener('mouseenter', () => { img.src = r.dataset.preview; cap.textContent = r.dataset.previewLabel || ''; box.style.display = 'block'; on = true; });
    r.addEventListener('mouseleave', () => { box.style.display = 'none'; on = false; });
  });
}

function initScrollMeter() {
  const span = document.getElementById('mt-scroll');
  if (!span) return;
  const upd = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const p = max > 0 ? Math.round(window.scrollY / max * 100) : 0;
    span.textContent = String(p).padStart(3, '0');
  };
  window.addEventListener('scroll', upd, { passive: true });
  upd();
}

window.MTFX = { initCursor, scramble, initReveals, revealHero, playIntro, playWipeIn, wipeTo, initScrollMeter, initHoverPreview };
