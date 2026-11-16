"""Le logo : un carré de la trame de lignes de la façade, traversé par sa diagonale de lumière.

Usage : python3 _build/logo.py   (favicon, icônes et logo carré ; Pillow requis)
build.py et partage.py importent d'ici le balisage du signe.
"""
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
COBALT = '#2f4bff'
RANGS, PAS, BARRE, LARGEUR, FENTE, DEPART = 6, 4, 2, 24, 5, 17
HAUTEUR = (RANGS - 1) * PAS + BARRE
# La lumière de la façade suit (0,8 ; 0,6) dans assets/js/site.js : trois quarts de pixel de recul par pixel descendu.
RECUL = PAS * 3 // 4
# Les barres débordent du cadre pour le couvrir encore quand la lumière le traverse (translation de 44 px dans site.css).
COURSE = 72
PETIT = [(2, 3, 8, 2), (12, 3, 2, 2), (2, 7, 5, 2), (9, 7, 5, 2), (2, 11, 2, 2), (6, 11, 8, 2)]


def tirets(echelle=1, dx=0, dy=0):
    for r in range(RANGS):
        fente = DEPART - r * RECUL
        y = dy + r * PAS * echelle
        yield dx, y, fente * echelle, BARRE * echelle
        yield dx + (fente + FENTE) * echelle, y, (LARGEUR - fente - FENTE) * echelle, BARRE * echelle


def trace(formes):
    return ''.join(f'M{x:g} {y:g}h{w:g}v{h:g}h{-w:g}z' for x, y, w, h in formes)


def signe(largeur=LARGEUR):
    return (f'<svg class="logo" viewBox="0 0 {LARGEUR} {HAUTEUR}" width="{largeur:g}" height="{largeur * HAUTEUR / LARGEUR:g}" '
            f'aria-hidden="true" focusable="false"><path d="{trace(tirets())}"/></svg>')


def signe_anime():
    def barres(decalage):
        return ''.join(f'<rect x="{DEPART - r * RECUL + decalage}" y="{r * PAS}" width="{COURSE}" height="{BARRE}"/>' for r in range(RANGS))
    return (f'<svg class="logo logo--anime" viewBox="0 0 {LARGEUR} {HAUTEUR}" width="{LARGEUR}" height="{HAUTEUR}" '
            f'aria-hidden="true" focusable="false"><g>{barres(-COURSE)}</g><g>{barres(FENTE)}</g></svg>')


def favicon_svg():
    grand = trace(tirets(1, (32 - LARGEUR) / 2, (32 - HAUTEUR) / 2))
    petit = trace((x * 2, y * 2, w * 2, h * 2) for x, y, w, h in PETIT)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><style>.p{display:none}'
            '@media (max-width:20px){.g{display:none}.p{display:inline}}</style>'
            f'<rect width="32" height="32" rx="7" fill="{COBALT}"/><path class="g" fill="#fff" d="{grand}"/>'
            f'<path class="p" fill="#fff" d="{petit}"/></svg>\n')


def icone(cote, echelle=None, rayon=0.22):
    from PIL import Image, ImageDraw
    sur = 8
    image = Image.new('RGBA', (cote * sur, cote * sur), (0, 0, 0, 0))
    dessin = ImageDraw.Draw(image)
    if rayon:
        dessin.rounded_rectangle([0, 0, cote * sur - 1, cote * sur - 1], radius=round(cote * sur * rayon), fill=COBALT)
    else:
        dessin.rectangle([0, 0, cote * sur, cote * sur], fill=COBALT)
    formes = tirets(echelle, (cote - LARGEUR * echelle) // 2, (cote - HAUTEUR * echelle) // 2) if echelle else PETIT
    for x, y, w, h in formes:
        dessin.rectangle([round(x) * sur, round(y) * sur, round(x + w) * sur - 1, round(y + h) * sur - 1], fill='#ffffff')
    image = image.reduce(sur)
    return image if rayon else image.convert('RGB')


if __name__ == '__main__':
    (RACINE / 'favicon.svg').write_text(favicon_svg())
    icone(48, 1.5).save(RACINE / 'favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)],
                        append_images=[icone(16), icone(32, 1)])
    icone(180, 5, rayon=0).save(RACINE / 'apple-touch-icon.png', optimize=True)
    icone(192, 5).save(RACINE / 'icon-192.png', optimize=True)
    icone(512, 13).save(RACINE / 'icon-512.png', optimize=True)
    icone(512, 11, rayon=0).save(RACINE / 'icon-maskable-512.png', optimize=True)
    icone(720, 18, rayon=0).save(RACINE / 'assets' / 'img' / 'logo-mickael-teixeira.png', optimize=True)
    for fichier in ('favicon.svg', 'favicon.ico', 'apple-touch-icon.png', 'icon-192.png', 'icon-512.png', 'icon-maskable-512.png',
                    'assets/img/logo-mickael-teixeira.png'):
        print(f'{fichier} : {(RACINE / fichier).stat().st_size} octets')
