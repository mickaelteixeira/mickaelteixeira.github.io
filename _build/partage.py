"""Génère les images de partage (Open Graph, 1200 × 630) avec Chrome sans interface.

Usage : python3 _build/partage.py
"""
import html
import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from logo import signe  # noqa: E402
RACINE = Path(__file__).resolve().parent.parent
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SORTIE = RACINE / 'assets' / 'img' / 'partage'
articles = json.loads((RACINE / '_build' / 'donnees' / 'articles.json').read_text())


def gabarit(surtitre, titre, suite, visuel, ajustement='contain', fond_visuel='#ffffff'):
    a = RACINE.as_uri()
    return f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face{{font-family:'Inter';font-weight:400 800;src:url({a}/assets/fonts/inter-400-800.woff2)}}
@font-face{{font-family:'Inter Tight';font-weight:300 400;src:url({a}/assets/fonts/inter-tight-300-400.woff2)}}
@font-face{{font-family:'JetBrains Mono';font-weight:400 500;src:url({a}/assets/fonts/jetbrains-mono-400-500.woff2)}}
body{{margin:0;width:1200px;height:630px;overflow:hidden;background:#ffffff;font-family:Inter,sans-serif;color:#171717;-webkit-font-smoothing:antialiased}}
.cadre{{display:grid;grid-template-columns:600px 600px;height:630px}}
.texte{{padding:56px 48px 52px 64px;display:flex;flex-direction:column;justify-content:space-between;border-right:1px solid #e5e5e5}}
.sur{{font-family:'JetBrains Mono',monospace;font-size:20px;color:#5c5c5c}}
h1{{margin:0;font-family:'Inter Tight',Inter,sans-serif;font-weight:300;font-size:50px;line-height:1.06;letter-spacing:-.03em}}
h1 span{{color:#9a9a9a}}
.pied{{display:flex;justify-content:space-between;align-items:center;font-size:20px;font-weight:600}}
.pied i{{font-style:normal;font-family:'JetBrains Mono',monospace;font-weight:400;font-size:18px;color:#2f4bff}}
.marque{{display:inline-flex;align-items:center;gap:12px}}
.marque svg{{fill:#2f4bff}}
.visuel{{background:{fond_visuel};display:flex;align-items:center;justify-content:center;overflow:hidden}}
.visuel img{{width:100%;height:100%;object-fit:{ajustement}}}
</style></head><body><div class="cadre"><div class="texte"><div class="sur">{html.escape(surtitre)}</div>
<h1>{html.escape(titre)} <span>{html.escape(suite)}</span></h1>
<div class="pied"><span class="marque">{signe(30)}Mickaël Teixeira</span><i>mickaelteixeira.github.io</i></div></div>
<div class="visuel"><img src="{a}{visuel}"></div></div></body></html>'''


def rendre(nom, contenu):
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as f:
        f.write(contenu)
    sortie = SORTIE / f'{nom}.png'
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--allow-file-access-from-files', '--virtual-time-budget=3000', '--window-size=1200,630',
                    f'--screenshot={sortie}', f.name], check=True, capture_output=True)
    Path(f.name).unlink()
    from PIL import Image
    Image.open(sortie).convert('RGB').save(sortie.with_suffix('.jpg'), 'JPEG', quality=86, optimize=True, progressive=True)
    sortie.unlink()
    print(sortie.with_suffix('.jpg').name)


SORTIE.mkdir(parents=True, exist_ok=True)
from build import MISSIONS  # noqa: E402

pages = json.loads((RACINE / '_build' / 'donnees' / 'pages.json').read_text())
FACADE = '/assets/img/facade-trame.svg'
VISUELS = {'symfony': '/assets/img/actualites/php-generiques-typephp.svg', 'sylius': '/assets/img/actualites/sylius-prestashop-rapprochement.svg',
           'architecture-hexagonale-ddd': '/assets/img/actualites/claw-code-reecriture-agents.svg'}

rendre('accueil', gabarit('Développeur freelance · Bordeaux', 'Développeur Symfony et Sylius,', 'freelance à Bordeaux.', FACADE))
rendre('expertises', gabarit('Expertises', pages['expertises_hub']['h1'], '', FACADE))
rendre('missions', gabarit('Missions', pages['missions_hub']['h1'], 'Références Symfony et Sylius.', FACADE))
rendre('parcours', gabarit('Parcours', 'Mickaël Teixeira,', 'développeur PHP à Bordeaux, depuis 2009.',
                           '/assets/img/mickael-teixeira-developpeur-symfony-bordeaux.webp', 'cover', '#e9e9e9'))
rendre('actualites', gabarit('Actualités', 'Ce que je lis, ce que je teste,', 'ce que je construis.',
                             f'/assets/img/actualites/{articles[0]["slug"]}.svg', 'cover'))
for x in pages['expertises']:
    visuel = VISUELS.get(x['slug'], FACADE)
    rendre(f'expertise-{x["slug"]}', gabarit('Expertise', x['h1'], '', visuel, 'cover' if visuel != FACADE else 'contain'))
for m in MISSIONS:
    rendre(f'mission-{m["slug"]}', gabarit(f'Mission · {m["annees"]}', f'{m["nom"]}.', m['role'].replace(' · ', ', ') + '.',
                                           f'/assets/img/missions/{m["slug"]}-couverture.webp', 'cover'))
for a in articles:
    rendre(f'article-{a["slug"]}', gabarit(f'{a["date_affichee"]} · {a["rubrique"]}', a['titre'], '',
                                           f'/assets/img/actualites/{a["slug"]}.svg', 'cover'))
