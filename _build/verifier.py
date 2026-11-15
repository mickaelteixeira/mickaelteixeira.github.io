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
        if len(titre) > 70:
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

plan = (RACINE / 'sitemap.xml').read_text()
for loc in re.findall(r'<loc>([^<]+)</loc>', plan):
    chemin = loc.replace('https://mickaelteixeira.github.io', '')
    if not (RACINE / chemin.lstrip('/') / 'index.html').exists():
        erreurs.append(f'sitemap : page absente {loc}')

print(f'{len(pages)} pages contrôlées, {len(erreurs)} erreur(s)')
for erreur in erreurs:
    print(' -', erreur)
sys.exit(1 if erreurs else 0)
