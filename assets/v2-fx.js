// v2-fx.js — utilitaires de motion pour le portfolio V2 (ease mécanique, reveals, wipes, curseur)
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

function scramble(el, duration = 900) {
  const orig = el.dataset.scrambleText || (el.dataset.scrambleText = el.textContent);
  if (reducedMotion()) { el.textContent = orig; return; }
  const start = Date.now();
  if (el.__mtScr) clearInterval(el.__mtScr);
  el.__mtScr = setInterval(() => {
    const p = Math.min((Date.now() - start) / duration, 1);
    const settled = Math.floor(orig.length * (p * p));
    let out = orig.slice(0, settled);
    for (let i = settled; i < orig.length; i++) out += orig[i] === ' ' ? ' ' : GLYPHS[(Math.random() * GLYPHS.length) | 0];
    el.textContent = out;
    if (p >= 1) { clearInterval(el.__mtScr); el.__mtScr = null; el.textContent = orig; }
  }, 45);
}

function reducedMotion() {
  return !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
}

function initReveals() {
  const t0 = performance.now();
  const EASE_T = ' cubic-bezier(0.16,1,0.3,1) ';
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
        el.style.opacity = '0'; el.style.transform = 'translateY(30px)';
        if (!inView(el)) return;
      }
      if (inView(el)) {
        el.__mtDone = true;
        const d = (Number(el.dataset.anim) || 0) * 90;
        el.style.transition = 'opacity .85s' + EASE_T + d + 'ms, transform .95s' + EASE_T + d + 'ms';
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
        el.style.transition = 'clip-path 1.1s cubic-bezier(0.16,1,0.3,1)';
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
  const t0 = Date.now(), DUR = 1100;
  let finished = false;
  const finish = () => {
    if (finished) return; finished = true;
    ov.style.transform = 'translateY(-100%)';
    setTimeout(() => { ov.remove(); done && done(); }, 560);
  };
  const tick = setInterval(() => {
    const p = Math.min((Date.now() - t0) / DUR, 1);
    bar.style.width = (p * 100) + '%';
    count.textContent = String(Math.floor(p * 100)).padStart(3, '0') + '%';
    if (p >= 1) { clearInterval(tick); finish(); }
  }, 40);
  setTimeout(() => { clearInterval(tick); finish(); }, DUR + 900);
}

function playWipeIn(done) {
  const ov = document.createElement('div');
  ov.style.cssText = 'position:fixed;inset:0;background:#000;z-index:10000;border-bottom:1px solid #fff;transition:transform .7s cubic-bezier(0.16,1,0.3,1)';
  document.body.appendChild(ov);
  setTimeout(() => { ov.style.transform = 'translateY(-100%)'; }, 24);
  setTimeout(() => { ov.remove(); done && done(); }, 760);
}

function wipeTo(href) {
  const ov = document.createElement('div');
  ov.style.cssText = 'position:fixed;inset:0;background:#000;z-index:10000;transform:translateY(100%);border-top:1px solid #fff;display:flex;align-items:center;justify-content:center;transition:transform .55s cubic-bezier(0.16,1,0.3,1)';
  ov.innerHTML = '<span style="font:500 10px var(--font-mono,monospace);letter-spacing:.25em;color:#6b6b6b;text-transform:uppercase">Chargement —</span>';
  document.body.appendChild(ov);
  setTimeout(() => { ov.style.transform = 'translateY(0)'; }, 24);
  setTimeout(() => { window.location.href = href; }, 580);
}

function initHoverPreview() {
  if (window.matchMedia && window.matchMedia('(pointer: coarse)').matches) return;
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

function initSectionDeck(opts) {
  const scroller = document.querySelector(opts.scroller);
  if (!scroller) return null;
  const sections = Array.from(scroller.querySelectorAll('[data-deck-section]'));
  if (!sections.length) return null;

  const SOFT = 'cubic-bezier(0.16,1,0.3,1)';
  const reduced = reducedMotion();
  const canAnim = typeof Element !== 'undefined' && !!Element.prototype.animate;

  const run = (el, from, to, dur, delay) => {
    if (el.__mtAnim) { try { el.__mtAnim.cancel(); } catch (e) {} el.__mtAnim = null; }
    el.style.transition = 'none';
    if (!canAnim) { Object.assign(el.style, to); return; }
    Object.assign(el.style, from);
    el.__mtAnim = el.animate([from, to], { duration: dur, delay: delay, easing: SOFT, fill: 'both' });
  };
  const clear = (el) => { if (el.__mtAnim) { try { el.__mtAnim.cancel(); } catch (e) {} el.__mtAnim = null; } };

  const settle = (s) => {
    s.querySelectorAll('[data-line]').forEach((el) => { clear(el); el.style.transition = 'none'; el.style.transform = 'translateY(0)'; });
    s.querySelectorAll('[data-anim],[data-fade]').forEach((el) => { clear(el); el.style.transition = 'none'; el.style.opacity = '1'; el.style.transform = 'none'; });
    s.querySelectorAll('[data-clip]').forEach((el) => { clear(el); el.style.transition = 'none'; el.style.clipPath = 'inset(0 0 0% 0)'; });
    s.querySelectorAll('[data-scramble]').forEach((el) => { if (el.dataset.scrambleText) el.textContent = el.dataset.scrambleText; });
  };
  const prep = (s) => {
    if (reduced || !canAnim) { settle(s); return; }
    s.querySelectorAll('[data-line]').forEach((el) => { clear(el); el.style.transition = 'none'; el.style.transform = 'translateY(108%)'; });
    s.querySelectorAll('[data-anim],[data-fade]').forEach((el) => { clear(el); el.style.transition = 'none'; el.style.opacity = '0'; el.style.transform = 'translateY(30px)'; });
    s.querySelectorAll('[data-clip]').forEach((el) => { clear(el); el.style.transition = 'none'; el.style.clipPath = 'inset(0 0 100% 0)'; });
  };
  const play = (s) => {
    if (reduced || !canAnim) { settle(s); return; }
    s.querySelectorAll('[data-line]').forEach((el, i) => {
      const idx = el.dataset.lineIndex !== undefined ? Number(el.dataset.lineIndex) : i;
      run(el, { transform: 'translateY(108%)' }, { transform: 'translateY(0)' }, 1050, idx * 105);
    });
    s.querySelectorAll('[data-anim],[data-fade]').forEach((el, i) => {
      const idx = el.dataset.anim !== undefined ? Number(el.dataset.anim) : i;
      run(el, { opacity: '0', transform: 'translateY(30px)' }, { opacity: '1', transform: 'translateY(0px)' }, 900, 200 + idx * 110);
    });
    s.querySelectorAll('[data-clip]').forEach((el, i) => {
      run(el, { clipPath: 'inset(0 0 100% 0)' }, { clipPath: 'inset(0 0 0% 0)' }, 1100, 120 + i * 110);
    });
    if (s.__mtSafety) clearTimeout(s.__mtSafety);
    s.__mtSafety = setTimeout(() => settle(s), 2800);
    s.querySelectorAll('[data-scramble]').forEach((el) => scramble(el));
  };
  sections.forEach(prep);
  let current = -1;
  const paintRail = (i) => {
    Array.from(document.querySelectorAll('[data-rail-item]')).forEach((r, j) => {
      const on = j === i;
      r.style.color = on ? 'var(--accent)' : 'var(--text-tertiary)';
      const bar = r.querySelector('[data-rail-bar]');
      const narrow = window.innerWidth < 720;
      if (bar) { bar.style.width = on ? (narrow ? '18px' : '30px') : (narrow ? '7px' : '12px'); bar.style.background = on ? 'var(--accent)' : 'var(--gray-700)'; }
    });
  };
  const setActive = (i) => {
    if (i !== current) {
      if (current >= 0) prep(sections[current]);
      current = i;
      play(sections[i]);
    }
    paintRail(i);
  };
  const onScroll = () => {
    const h = scroller.clientHeight;
    setActive(Math.max(0, Math.min(sections.length - 1, Math.round(scroller.scrollTop / h))));
    const meter = document.getElementById('mt-scroll');
    if (meter) {
      const max = scroller.scrollHeight - h;
      meter.textContent = String(max > 0 ? Math.round(scroller.scrollTop / max * 100) : 0).padStart(3, '0');
    }
  };
  const go = (i) => {
    const t = Math.max(0, Math.min(sections.length - 1, i));
    scroller.scrollTo({ top: t * scroller.clientHeight, behavior: 'smooth' });
  };
  scroller.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  document.addEventListener('keydown', (e) => {
    const t = e.target && e.target.tagName;
    if (t === 'INPUT' || t === 'TEXTAREA') return;
    if (e.key === 'ArrowDown' || e.key === 'PageDown' || e.key === ' ') { e.preventDefault(); go(current + 1); }
    else if (e.key === 'ArrowUp' || e.key === 'PageUp') { e.preventDefault(); go(current - 1); }
  });
  onScroll();
  [80, 300, 900].forEach((d) => setTimeout(onScroll, d));
  return { go, onScroll };
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

window.MTFX = { initCursor, scramble, reducedMotion, initReveals, revealHero, playIntro, playWipeIn, wipeTo, initScrollMeter, initHoverPreview, initSectionDeck };
