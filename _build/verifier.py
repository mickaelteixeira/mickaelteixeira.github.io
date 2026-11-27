"""Contrôle le site généré : liens internes, balises de référencement, données structurées.

Usage : python3 _build/verifier.py
"""
import html
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
pages = sorted(p for p in RACINE.rglob('*.html') if '_build' not in p.parts and '.git' not in p.parts)
ancres = {p: set(re.findall(r'\bid="([^"]+)"', p.read_text())) for p in pages}
erreurs = []
titres, descriptions = {}, {}

for p in pages:
    t = p.read_text()
    nom = str(p.relative_to(RACINE))
    cibles = re.findall(r'\b(?:src|href|data-grille)="([^"]+)"', t)
    cibles += [morceau.split()[0] for s in re.findall(r'srcset="([^"]+)"', t) for morceau in s.split(',')]
    for v in cibles:
        v = html.unescape(v.strip())
        if v.startswith(('http', 'mailto:', 'data:')):
            continue
        chemin, _, ancre = v.partition('#')
        if not chemin:
            if ancre and ancre not in ancres[p]:
                erreurs.append(f'{nom} : ancre introuvable {v}')
            continue
        cible = RACINE / chemin.lstrip('/')
        if chemin.endswith('/'):
            cible = cible / 'index.html'
        if not cible.exists():
            erreurs.append(f'{nom} : lien cassé {v}')
        elif ancre and cible.suffix == '.html' and ancre not in ancres.get(cible, set()):
            erreurs.append(f'{nom} : ancre introuvable {v}')
    if 'http-equiv="refresh"' in t:
        continue
    titre = html.unescape(re.search(r'<title>(.*?)</title>', t).group(1))
    description = html.unescape(re.search(r'name="description" content="([^"]*)"', t).group(1))
    indexable = 'content="noindex' not in t
    if indexable:
        if len(titre) > 60:
            erreurs.append(f'{nom} : titre de {len(titre)} signes')
        if not 50 <= len(description) <= 158:
            erreurs.append(f'{nom} : description de {len(description)} signes')
        if titre in titres:
            erreurs.append(f'{nom} : même titre que {titres[titre]}')
        if description in descriptions:
            erreurs.append(f'{nom} : même description que {descriptions[description]}')
        titres[titre], descriptions[description] = nom, nom
        if 'rel="canonical"' not in t:
            erreurs.append(f'{nom} : pas d’URL canonique')
    if len(re.findall(r'<h1\b', t)) != 1:
        erreurs.append(f'{nom} : {len(re.findall(r"<h1", t))} titres h1')
    niveaux = [int(n) for n in re.findall(r'<h([1-6])\b', t)]
    for avant, apres in zip(niveaux, niveaux[1:]):
        if apres > avant + 1:
            erreurs.append(f'{nom} : saut de titre h{avant} vers h{apres}')
            break
    for image in re.findall(r'<img\b[^>]*>', t):
        if ' alt=' not in image:
            erreurs.append(f'{nom} : image sans alt {image[:80]}')
        if ' width=' not in image or ' height=' not in image:
            erreurs.append(f'{nom} : image sans dimensions {image[:80]}')
    for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        try:
            json.loads(bloc)
        except ValueError as erreur:
            erreurs.append(f'{nom} : JSON-LD invalide ({erreur})')

def nodes(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from nodes(child)


# Search engines derive the site name from the home page: its entities must not compete with the WebSite node.
home = (RACINE / 'index.html').read_text()
home_nodes = [n for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', home, re.S) for n in nodes(json.loads(bloc))]
websites = [n for n in home_nodes if n.get('@type') == 'WebSite']
host = re.search(r'rel="canonical" href="https://([^/"]+)', home).group(1)
if len(websites) != 1:
    erreurs.append(f'index.html : {len(websites)} nœuds WebSite, un seul attendu')
else:
    site_name = html.unescape(re.search(r'property="og:site_name" content="([^"]*)"', home).group(1))
    if websites[0].get('name') != site_name:
        erreurs.append(f'index.html : WebSite « {websites[0].get("name")} » et og:site_name « {site_name} » diffèrent')
    if websites[0].get('alternateName', [None])[-1] != host:
        erreurs.append(f'index.html : le dernier alternateName du WebSite doit être {host}')
for n in home_nodes:
    if n.get('@type') == 'Organization':
        erreurs.append(f'index.html : nœud Organization « {n.get("name")} », qui concurrence le nom du site')

plan = (RACINE / 'sitemap.xml').read_text()
for loc in re.findall(r'<loc>([^<]+)</loc>', plan):
    chemin = loc.replace('https://mickaelteixeira.github.io', '')
    if not (RACINE / chemin.lstrip('/') / 'index.html').exists():
        erreurs.append(f'sitemap : page absente {loc}')

print(f'{len(pages)} pages contrôlées, {len(erreurs)} erreur(s)')
for erreur in erreurs:
    print(' -', erreur)
sys.exit(1 if erreurs else 0)
