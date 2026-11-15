(() => {
  const theme = document.querySelector('.theme');
  if (theme) {
    const libelles = { auto: 'Thème : automatique', clair: 'Thème : clair', sombre: 'Thème : sombre' };
    const suivant = { auto: 'clair', clair: 'sombre', sombre: 'auto' };
    const appliquer = choix => {
      if (choix === 'auto') document.documentElement.removeAttribute('data-theme');
      else document.documentElement.setAttribute('data-theme', choix);
      theme.setAttribute('aria-label', libelles[choix] + '. Changer de thème');
      theme.title = libelles[choix];
    };
    let courant = document.documentElement.getAttribute('data-theme') || 'auto';
    appliquer(courant);
    theme.addEventListener('click', () => {
      courant = suivant[courant];
      appliquer(courant);
      try { courant === 'auto' ? localStorage.removeItem('theme') : localStorage.setItem('theme', courant); } catch (e) {}
    });
  }

  const bouton = document.querySelector('.entete__menu');
  const menu = document.getElementById('menu-mobile');
  if (bouton && menu) {
    const basculer = ouvrir => {
      menu.hidden = !ouvrir;
      bouton.setAttribute('aria-expanded', String(ouvrir));
      bouton.setAttribute('aria-label', ouvrir ? 'Fermer le menu' : 'Ouvrir le menu');
      bouton.querySelector('path').setAttribute('d', ouvrir ? 'M6 6l12 12M18 6L6 18' : 'M4 7h16M4 12h16M4 17h16');
      document.body.classList.toggle('menu-ouvert', ouvrir);
    };
    bouton.addEventListener('click', () => basculer(menu.hidden));
    menu.addEventListener('click', e => { if (e.target.closest('a')) basculer(false); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !menu.hidden) { basculer(false); bouton.focus(); } });
  }

  const facade = document.querySelector('.facade');
  if (!facade) return;
  const canvas = facade.querySelector('canvas');
  const L = 720, H = 900, PAS = 5, CELL = 2, COLS = 360, RANGS = 180;
  const PLANCHER = 0.1, GAMMA = 1.15, EMIN = 0.6, EMAX = 2.2;
  const reduit = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduit) return;
  const dpr = Math.min(2, window.devicePixelRatio || 1);
  canvas.width = L * dpr;
  canvas.height = H * dpr;
  const ctx = canvas.getContext('2d');
  ctx.scale(dpr, dpr);
  const image = new Image();
  image.onload = () => {
    const tampon = document.createElement('canvas');
    tampon.width = COLS;
    tampon.height = RANGS;
    const tctx = tampon.getContext('2d');
    tctx.drawImage(image, 0, 0, COLS, RANGS);
    const pixels = tctx.getImageData(0, 0, COLS, RANGS).data;
    const sombre = new Float32Array(COLS * RANGS);
    for (let i = 0; i < COLS * RANGS; i++) {
      const v = 1 - pixels[i * 4] / 255;
      sombre[i] = Math.pow(Math.max(0, (v - PLANCHER) / (1 - PLANCHER)), GAMMA);
    }
    const lireCouleur = () => getComputedStyle(facade).getPropertyValue('--accent').trim() || '#2f4bff';
    let couleur = lireCouleur();
    new MutationObserver(() => { couleur = lireCouleur(); }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { couleur = lireCouleur(); });
    const dessiner = (lumiere, rangsVisibles) => {
      ctx.clearRect(0, 0, L, H);
      ctx.fillStyle = couleur;
      for (let r = 0; r < rangsVisibles; r++) {
        let erreur = 0, debut = -1, somme = 0, n = 0;
        for (let c = 0; c <= COLS; c++) {
          let allume = false, v = 0;
          if (c < COLS) {
            v = sombre[r * COLS + c];
            if (lumiere) v = Math.max(0, v - lumiere(c * CELL, r * PAS));
            const cible = v + erreur;
            allume = cible >= 0.5;
            erreur = cible - (allume ? 1 : 0);
          }
          if (allume) {
            if (debut < 0) { debut = c; somme = 0; n = 0; }
            somme += v; n++;
          } else if (debut >= 0) {
            const h = EMIN + (EMAX - EMIN) * (somme / n);
            ctx.fillRect(debut * CELL, r * PAS + (PAS - h) / 2, Math.max(1, n * CELL - 0.6), h);
            debut = -1;
          }
        }
      }
    };
    const DIAG = L * 0.8 + H * 0.6, LARGEUR = 150, PERIODE = 10000, BALAYAGE = 7000, REVELE = 1600;
    const adoucir = x => x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
    let visible = true;
    new IntersectionObserver(entrees => { visible = entrees[0].isIntersecting; }).observe(facade);
    const depart = performance.now();
    let derniere = 0;
    const boucle = maintenant => {
      requestAnimationFrame(boucle);
      if (!visible || document.hidden || maintenant - derniere < 33) return;
      derniere = maintenant;
      const t = maintenant - depart;
      const rangs = t < REVELE ? Math.ceil(RANGS * adoucir(t / REVELE)) : RANGS;
      const phase = t % PERIODE;
      let lumiere = null;
      if (t > REVELE && phase < BALAYAGE) {
        const pos = -LARGEUR * 2 + (DIAG + LARGEUR * 4) * adoucir(phase / BALAYAGE);
        lumiere = (x, y) => {
          const d = (x * 0.8 + y * 0.6 - pos) / LARGEUR;
          return 0.6 * Math.exp(-d * d);
        };
      }
      dessiner(lumiere, rangs);
      facade.classList.add('est-animee');
    };
    requestAnimationFrame(boucle);
  };
  image.src = facade.dataset.grille;
})();
