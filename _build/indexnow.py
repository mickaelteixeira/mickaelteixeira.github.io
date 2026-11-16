"""Signale aux moteurs compatibles IndexNow (Bing, Yandex, Seznam, Naver) les pages modifiées.

Usage : python3 _build/indexnow.py                    les pages modifiées par le dernier commit
        python3 _build/indexnow.py --depuis <commit>  les pages modifiées depuis ce commit
        python3 _build/indexnow.py --tout             toutes les pages du sitemap
"""
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
HOTE = 'mickaelteixeira.github.io'
SITE = f'https://{HOTE}'
cle = next(p.stem for p in RACINE.glob('*.txt') if re.fullmatch(r'[0-9a-f]{32}', p.stem))
plan = re.findall(r'<loc>([^<]+)</loc>', (RACINE / 'sitemap.xml').read_text())


def modifiees():
    depuis = sys.argv[sys.argv.index('--depuis') + 1] if '--depuis' in sys.argv else 'HEAD^'
    sortie = subprocess.run(['git', 'diff', '--name-only', depuis, 'HEAD'], cwd=RACINE, capture_output=True, text=True)
    if sortie.returncode:
        return plan
    urls = set()
    for fichier in sortie.stdout.split():
        if fichier.endswith('index.html'):
            urls.add(f'{SITE}/{fichier[:-len("index.html")]}')
    return [u for u in plan if u in urls]


urls = plan if '--tout' in sys.argv else modifiees()
if not urls:
    print('Aucune page modifiée à signaler.')
    sys.exit(0)
en_ligne = urllib.request.urlopen(f'{SITE}/{cle}.txt', timeout=30).read().decode().strip()
if en_ligne != cle:
    sys.exit('La clé IndexNow en ligne ne correspond pas : rien n’est envoyé.')
corps = json.dumps({'host': HOTE, 'key': cle, 'keyLocation': f'{SITE}/{cle}.txt', 'urlList': urls}).encode()
requete = urllib.request.Request('https://api.indexnow.org/indexnow', data=corps,
                                 headers={'Content-Type': 'application/json; charset=utf-8'})
with urllib.request.urlopen(requete, timeout=30) as reponse:
    print(f'IndexNow : {len(urls)} page(s) signalée(s), réponse {reponse.status}')
for u in urls:
    print(' -', u)
