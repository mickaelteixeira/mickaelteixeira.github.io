"""Génère le site statique dans la racine du dépôt.

Usage : python3 _build/build.py
Sources : _build/contenu (fragments HTML des pages), _build/donnees (articles, captures).
"""
import html
import json
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CONTENU = RACINE / '_build' / 'contenu'
DONNEES = RACINE / '_build' / 'donnees'
SITE = 'https://mickaelteixeira.github.io'
NOM = 'Mickaël Teixeira'
MISE_A_JOUR = '2026-11-15'
VERIFICATION_GOOGLE = 'wsdzIL0Lmsbtvz1F2wSa2pzjxPZG2HtzG2G24YiEvAY'
LINKEDIN = 'https://www.linkedin.com/in/dev-php-bordeaux/'
PROFILS = [LINKEDIN, 'https://www.malt.fr/profile/mickaelteixeira', 'https://github.com/mickaelteixeira']

MONO = "font-family: 'JetBrains Mono', monospace"
TIGHT = "font-family: 'Inter Tight', Inter, sans-serif; font-weight: 300"
WRAP = 'max-width: 1312px; margin: 0 auto; padding-inline: clamp(20px, 4.5cqw, 64px); box-sizing: border-box'
LIEN = 'color: #2f4bff; text-underline-offset: 3px'

MISSIONS = [
    {'slug': 'maxicoffee', 'nom': 'MaxiCoffee', 'annees': '2025 – 2026', 'role': 'Middle office · freelance',
     'titre': 'Middle office MaxiCoffee : Laravel et Salesforce',
     'description': 'Mission freelance chez MaxiCoffee (2025-2026) : un middle office en architecture hexagonale, synchronisé avec Salesforce, pour la facturation et la logistique.',
     'client': 'https://www.maxicoffee.com/'},
    {'slug': 'commande', 'nom': 'Commande.com', 'annees': '2025', 'role': 'Refonte Sylius · freelance, avec Dn’D',
     'titre': 'Refonte Sylius headless de Commande.com',
     'description': 'Mission freelance avec l’agence Dn’D (2025) : la refonte de Commande.com sur Sylius en headless, API Platform, flux ERP et transporteurs, tests automatisés.',
     'client': 'https://commande.com/'},
    {'slug': 'heyteam', 'nom': 'HeyTeam', 'annees': '2025', 'role': 'Lead developer',
     'titre': 'HeyTeam : lead developer Laravel',
     'description': 'Lead developer chez HeyTeam en 2025 : une plateforme B2B d’onboarding reliée aux SIRH des clients, en architecture modulaire Laravel.',
     'client': 'https://www.heyteam.com/'},
    {'slug': 'upd', 'nom': 'Ultra Premium Direct', 'annees': '2022 – 2024', 'role': 'Migration Sylius · backend',
     'titre': 'Migration Sylius d’Ultra Premium Direct',
     'description': 'Développeur backend chez Ultra Premium Direct de 2022 à 2024 : la migration vers Sylius d’un e-commerce de petfood à fort trafic, en Symfony.',
     'client': 'https://www.ultrapremiumdirect.com/'},
    {'slug': 'onepoint', 'nom': 'onepoint', 'annees': '2013 – 2022', 'role': 'Six missions en conseil · full-stack',
     'titre': 'onepoint : huit ans de conseil en développement',
     'description': 'Développeur full-stack chez onepoint de 2013 à 2022 : six missions pour Enedis, Gaz de Bordeaux, PSA, Bureau Veritas Pro et SMIP, de Zend à Angular.',
     'client': 'https://www.groupeonepoint.com/'},
    {'slug': 'timeone', 'nom': 'TimeOne', 'annees': '2012 – 2013', 'role': 'Outils d’affiliation · PHP',
     'titre': 'TimeOne : outils d’affiliation en PHP',
     'description': 'Développeur PHP chez TimeOne de 2012 à 2013 : des outils pour un réseau d’affiliation, une application mobile et la pratique de Scrum au quotidien.',
     'client': 'https://www.timeonegroup.com/'},
    {'slug': 'webstrategies', 'nom': 'Web Stratégies', 'annees': '2009 – 2011', 'role': 'Sites et e-commerce · alternance',
     'titre': 'Web Stratégies : alternance de développeur PHP',
     'description': 'Alternance de développeur PHP chez Web Stratégies, agence web de Bordeaux, de 2009 à 2011 : des sites, de la maquette au paiement Magento.',
     'client': 'https://www.webstrategies.fr/'},
    {'slug': 'illicotravel', 'nom': 'illicotravel', 'annees': '2009', 'role': 'Comparateur de voyages · stage',
     'titre': 'illicotravel : flux partenaires en PHP',
     'description': 'Stage de développeur PHP chez illicotravel en 2009 : intégrer les flux XML de nouveaux partenaires au moteur d’un comparateur de voyages.',
     'client': None},
]

articles = sorted(json.loads((DONNEES / 'articles.json').read_text()), key=lambda a: a['date'], reverse=True)
captures = json.loads((DONNEES / 'captures.json').read_text())
pages_sitemap = []


def e(texte):
    return html.escape(texte or '', quote=True)


def url(chemin):
    return SITE + chemin


def ecrire(chemin, contenu):
    cible = RACINE / chemin.lstrip('/')
    if chemin.endswith('/'):
        cible = cible / 'index.html'
    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(contenu)


def fragment(nom):
    return (CONTENU / nom).read_text()


PERSONNE = {
    '@type': 'Person', '@id': SITE + '/#mickael-teixeira', 'name': NOM, 'givenName': 'Mickaël', 'familyName': 'Teixeira',
    'jobTitle': 'Développeur Symfony et Sylius freelance', 'url': SITE + '/',
    'image': url('/assets/img/mickael-teixeira-developpeur-symfony-bordeaux.webp'),
    'description': 'Développeur PHP depuis 2009, freelance à Bordeaux depuis 2025 : Symfony, Sylius, API Platform et Laravel. Fondateur de Yedra, le CRM des écoles.',
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Bordeaux', 'addressRegion': 'Nouvelle-Aquitaine', 'addressCountry': 'FR'},
    'alumniOf': {'@type': 'EducationalOrganization', 'name': 'ETNA', 'url': 'https://etna.io/'},
    'knowsAbout': ['PHP', 'Symfony', 'Sylius', 'API Platform', 'Laravel', 'E-commerce', 'Architecture hexagonale',
                   'Domain-Driven Design', 'Angular', 'Elasticsearch', 'RabbitMQ', 'Docker', 'GitLab CI', 'Tests automatisés'],
    'knowsLanguage': ['fr', 'en'],
    'sameAs': PROFILS,
}
ACTIVITE = {
    '@type': 'ProfessionalService', '@id': SITE + '/#activite', 'name': 'Mickaël Teixeira, développeur Symfony et Sylius freelance',
    'url': SITE + '/', 'image': url('/assets/img/partage/accueil.jpg'), 'founder': {'@id': PERSONNE['@id']},
    'description': 'Développement freelance Symfony, Sylius et API Platform : migrations e-commerce vers Sylius, middle offices, API, flux ERP, CRM et transporteurs.',
    'address': {'@type': 'PostalAddress', 'streetAddress': '269 chemin des Bouvreuils', 'postalCode': '33290',
                'addressLocality': 'Le Pian-Médoc', 'addressRegion': 'Nouvelle-Aquitaine', 'addressCountry': 'FR'},
    'areaServed': [{'@type': 'City', 'name': 'Bordeaux'}, {'@type': 'City', 'name': 'Paris'}, {'@type': 'City', 'name': 'Lyon'},
                   {'@type': 'City', 'name': 'Lille'}, {'@type': 'City', 'name': 'Nantes'}, {'@type': 'Country', 'name': 'France'}],
    'serviceType': ['Développement Symfony', 'Développement Sylius', 'Migration e-commerce vers Sylius', 'API Platform',
                    'Middle office', 'Architecture logicielle'],
    'vatID': 'FR88831303185', 'taxID': '831 303 185', 'sameAs': PROFILS,
}
SITE_WEB = {'@type': 'WebSite', '@id': SITE + '/#site', 'url': SITE + '/', 'name': NOM, 'inLanguage': 'fr-FR',
            'publisher': {'@id': PERSONNE['@id']}}


def fil(*etapes):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': nom, 'item': url(chemin)} for i, (nom, chemin) in enumerate(etapes)]}


def graphe(*noeuds):
    return {'@context': 'https://schema.org', '@graph': [n for n in noeuds if n]}


def jetons(st):
    sur_accent = 'background: #2f4bff' in st and 'color: #ffffff' in st
    st = st.replace('background: #8fa2ff; color: #171717', '§lavande§')
    st = st.replace('background: #ffffff', 'background: var(--fond)').replace('background: #f5f5f5', 'background: var(--fond-2)')
    st = st.replace('background: #171717', 'background: var(--panneau)')
    st = re.sub(r'(border(?:-top|-bottom|-left|-right)?: \d+px solid )#(?:e5e5e5|ebebeb)', r'\1var(--trait)', st)
    st = re.sub(r'(border(?:-top|-bottom|-left|-right)?: \d+px solid )#b3b3b3', r'\1var(--trait-fort)', st)
    st = re.sub(r'(border(?:-top|-bottom|-left|-right)?: \d+px solid )#171717', r'\1var(--encre)', st)
    st = re.sub(r'(?<![-\w])color: #171717', 'color: var(--encre)', st)
    st = re.sub(r'(?<![-\w])color: #3d3d3d', 'color: var(--texte)', st)
    st = re.sub(r'(?<![-\w])color: #5c5c5c', 'color: var(--second)', st)
    st = st.replace('#2f4bff', 'var(--accent)')
    if sur_accent:
        st = st.replace('color: #ffffff', 'color: var(--sur-accent)')
    return st.replace('§lavande§', 'background: #8fa2ff; color: #171717')


def themer(texte):
    morceaux = re.split(r'(<!--fixe-->.*?<!--/fixe-->)', texte, flags=re.S)
    return ''.join(m.replace('<!--fixe-->', '').replace('<!--/fixe-->', '') if m.startswith('<!--fixe-->')
                   else re.sub(r'style="([^"]*)"', lambda s: f'style="{jetons(s.group(1))}"', m) for m in morceaux)


def couvertures(texte, tailles):
    return re.sub(r'<img src="/assets/img/missions/([a-z]+)-couverture\.webp"',
                  lambda m: (f'<img src="/assets/img/missions/{m.group(1)}-couverture.webp" '
                             f'srcset="/assets/img/missions/{m.group(1)}-couverture-800.webp 800w, /assets/img/missions/{m.group(1)}-couverture.webp 1600w" '
                             f'sizes="{tailles}"'), texte)


def entete(courant):
    liens = [('Missions', '/#missions'), ('Expertises', '/#expertises'), ('Yedra', '/#yedra'), ('Parcours', '/#parcours'),
             ('Actualités', '/actualites/')]
    nav = '\n'.join(f'<a href="{h}"{" aria-current=\"page\"" if n == courant else ""}>{n}</a>' for n, h in liens)
    mobile = '\n'.join(f'<a class="menu-mobile__lien" href="{h}">{n}</a>' for n, h in liens)
    return f'''<a class="evitement" href="#contenu">Aller au contenu</a>
<header class="entete">
<div class="entete__barre">
<a class="entete__nom" href="/">{NOM}</a>
<nav class="entete__nav" aria-label="Navigation principale">
{nav}
</nav>
<div class="entete__actions">
<button class="theme" type="button" aria-label="Thème : automatique. Changer de thème" title="Thème : automatique"><svg data-icone="auto" aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><circle cx="12" cy="12" r="8"></circle><path d="M12 4a8 8 0 0 0 0 16z" fill="currentColor"></path></svg><svg data-icone="clair" aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"></path></svg><svg data-icone="sombre" aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linejoin="round"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"></path></svg></button>
<a class="entete__contact" href="/#contact">Me contacter</a>
<button class="entete__menu" type="button" aria-expanded="false" aria-controls="menu-mobile" aria-label="Ouvrir le menu"><svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"></path></svg></button>
</div>
</div>
</header>
<nav id="menu-mobile" class="menu-mobile" aria-label="Menu" hidden>
{mobile}
<div class="menu-mobile__pied">
<p>Toujours ouvert à une mission</p>
<a href="/#contact">Me contacter</a>
</div>
</nav>'''


def page(chemin, titre, description, corps, *, courant=None, image='/assets/img/partage/accueil.jpg',
         image_alt='Mickaël Teixeira, développeur Symfony et Sylius à Bordeaux', type_og='website', donnees=None,
         indexable=True, tete='', date_modif=MISE_A_JOUR, priorite='0.6'):
    titre_complet = titre if NOM in titre or len(titre) > 43 else f'{titre} · {NOM}'
    canonique = url(chemin)
    robots = 'index, follow, max-image-preview:large, max-snippet:-1' if indexable else 'noindex, follow'
    jsonld = f'<script type="application/ld+json">{json.dumps(donnees, ensure_ascii=False, separators=(",", ":"))}</script>' if donnees else ''
    if indexable:
        pages_sitemap.append((canonique, date_modif, priorite))
    contenu = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titre_complet)}</title>
<meta name="description" content="{e(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonique}">
<meta name="author" content="{NOM}">
<meta name="google-site-verification" content="{VERIFICATION_GOOGLE}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#171717" media="(prefers-color-scheme: dark)">
<script>try{{var t=localStorage.getItem('theme');if(t==='clair'||t==='sombre')document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">
<link rel="alternate" type="application/atom+xml" title="Actualités de {NOM}" href="/actualites/flux.xml">
<meta property="og:type" content="{type_og}">
<meta property="og:site_name" content="{NOM}">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{e(titre)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{canonique}">
<meta property="og:image" content="{url(image)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(image_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(titre)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{url(image)}">
<link rel="preload" href="/assets/fonts/inter-400-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-tight-300-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
{tete}{jsonld}
</head>
<body>
{entete(courant)}
{themer(corps)}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
'''
    ecrire(chemin, contenu)


def bande_missions(actuelle):
    lignes = []
    for m in MISSIONS:
        courant = m['slug'] == actuelle
        lignes.append(
            f'<li style="border-top: 1px solid #303030"><a href="/missions/{m["slug"]}/"{" aria-current=\"page\"" if courant else ""} '
            f'style="display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 2px 16px; padding-block: 14px; color: {"#8fa2ff" if courant else "#ebebeb"}; text-decoration: none">'
            f'<span style="font-weight: 500">{e(m["nom"])}</span><span style="{MONO}; font-size: 12px; color: #a3a3a3">{m["annees"]}</span>'
            f'<span style="grid-column: 1 / -1; font-size: 14px; color: #a3a3a3">{e(m["role"])}</span></a></li>')
    return f'''<section aria-labelledby="titre-prochain" style="container-type: inline-size; background: #171717; color: #ebebeb; font-size: 16px; line-height: 1.55">
<div style="{WRAP}; padding-block: clamp(64px, 7cqw, 112px) 40px; display: flex; flex-direction: column; gap: clamp(56px, 6cqw, 88px)">
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: end; gap: 32px 64px">
<h2 id="titre-prochain" style="margin: 0; flex: 1 1 520px; {TIGHT}; font-size: clamp(36px, 4.2cqw, 64px); line-height: 1.04; letter-spacing: -0.03em; color: #ffffff">La prochaine mission, <span style="color: #8a8a8a">c’est peut-être la vôtre.</span></h2>
<a href="/#contact" style="display: inline-flex; align-items: center; height: 48px; padding: 0 22px; background: #8fa2ff; color: #171717; border-radius: 8px; text-decoration: none; font-weight: 500">Proposer une mission</a>
</div>
<nav aria-label="Toutes les missions" style="display: flex; flex-direction: column; gap: 16px">
<p style="margin: 0; {MONO}; font-size: 13px; color: #a3a3a3">Toutes les missions, depuis 2009</p>
<ol style="margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0 32px">
{chr(10).join(lignes)}
</ol>
</nav>
{pied_sombre()}
</div>
</section>'''


def pied_sombre():
    return f'''<footer style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 16px; padding-top: 24px; border-top: 1px solid #303030; font-size: 14px; color: #a3a3a3">
<span>© 2026 {NOM} · entrepreneur individuel · Bordeaux</span>
<nav aria-label="Pied de page" style="display: flex; flex-wrap: wrap; gap: 24px"><a href="/" style="color: #a3a3a3">Accueil</a><a href="/actualites/" style="color: #a3a3a3">Actualités</a><a href="/mentions-legales/" style="color: #a3a3a3">Mentions légales</a><a href="{LINKEDIN}" style="color: #a3a3a3">LinkedIn</a></nav>
</footer>'''


def pied_actualites():
    return f'''<section aria-labelledby="titre-suite" style="container-type: inline-size; background: #171717; color: #ebebeb">
<div style="{WRAP}; padding-block: clamp(64px, 7cqw, 112px) 40px; display: flex; flex-direction: column; gap: clamp(48px, 5cqw, 72px)">
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: end; gap: 32px 64px">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
<p style="margin: 0; {MONO}; font-size: 13px; color: #a3a3a3">Développeur Symfony et Sylius · Bordeaux</p>
<h2 id="titre-suite" style="margin: 0; {TIGHT}; font-size: clamp(36px, 4.2cqw, 64px); line-height: 1.04; letter-spacing: -0.03em; color: #ffffff">Une plateforme à faire évoluer ? <span style="color: #8a8a8a">Parlons-en.</span></h2>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 12px">
<a href="/#contact" style="display: inline-flex; align-items: center; height: 48px; padding: 0 22px; background: #8fa2ff; color: #171717; border-radius: 8px; text-decoration: none; font-weight: 500">Proposer une mission</a>
<a href="{LINKEDIN}" style="display: inline-flex; align-items: center; height: 48px; padding: 0 22px; border: 1px solid #5c5c5c; color: #ffffff; border-radius: 8px; text-decoration: none; font-weight: 500">Suivre sur LinkedIn</a>
</div>
</div>
{pied_sombre()}
</div>
</section>'''


def carte(a, grand=False, theme_accueil=False):
    encre, second, trait = ('var(--encre)', 'var(--second)', 'var(--trait)') if theme_accueil else ('#171717', '#5c5c5c', '#ebebeb')
    chapo = '' if theme_accueil else f'<span style="font-size: 15px; line-height: 1.6; color: #3d3d3d">{e(a["chapo"])}</span>'
    return f'''<a href="/actualites/{a["slug"]}/" style="display: flex; flex-direction: column; gap: 14px; color: {encre}; text-decoration: none">
<span style="display: block; overflow: hidden; border-radius: 12px; border: 1px solid {trait}; background: #ffffff"><img src="/assets/img/actualites/{a["slug"]}-carte.webp" data-theme-img="clair" alt="{e(a["visuel_alt"])}" width="800" height="450" loading="lazy" decoding="async" style="display: block; width: 100%; height: auto"><img src="/assets/img/actualites/{a["slug"]}-nuit-carte.webp" data-theme-img="sombre" alt="{e(a["visuel_alt"])}" width="800" height="450" loading="lazy" decoding="async" style="display: block; width: 100%; height: auto"></span>
<span style="{MONO}; font-size: 12px; color: {second}"><time datetime="{a["date"]}">{a["date_affichee"]}</time> · {e(a["rubrique"])}</span>
<span style="{TIGHT}; font-size: 24px; line-height: 1.14; letter-spacing: -0.02em">{e(a["titre"])}</span>
{chapo}
<span style="{MONO}; font-size: 12px; color: {second}">{a["temps_lecture"]} min de lecture</span>
</a>'''


def bloc(b):
    t = b['type']
    if t == 'p':
        return f'<p style="margin: 0">{e(b["texte"])}</p>'
    if t == 'h2':
        return f'<h2 style="margin: 24px 0 0; {TIGHT}; font-size: 32px; line-height: 1.15; letter-spacing: -0.02em; color: #171717">{e(b["texte"])}</h2>'
    if t == 'liste':
        items = ''.join(f'<li>{e(i)}</li>' for i in b['items'])
        return f'<ul style="margin: 0; padding-left: 22px; display: flex; flex-direction: column; gap: 8px">{items}</ul>'
    if t == 'citation':
        auteur = e(b.get('auteur')) + (' · traduit de l’anglais' if b.get('traduction') else '')
        source = f'<a href="{e(b["source_url"])}" style="{LIEN}; color: #5c5c5c">{e(b.get("source_libelle") or "Source")}</a>' if b.get('source_url') else ''
        return (f'<figure style="margin: 16px 0; padding: 8px 0 8px 24px; border-left: 2px solid #2f4bff; display: flex; flex-direction: column; gap: 12px">'
                f'<blockquote style="margin: 0; {TIGHT}; font-size: clamp(24px, 2.4cqw, 30px); line-height: 1.28; letter-spacing: -0.02em; color: #171717"><p style="margin: 0">« {e(b["texte"])} »</p></blockquote>'
                f'<figcaption style="display: flex; flex-wrap: wrap; gap: 4px 10px; font-size: 14px; line-height: 1.5"><span style="color: #171717; font-weight: 500">{auteur}</span>{source}</figcaption></figure>')
    if t == 'code':
        source = f'<a href="{e(b["source_url"])}" style="{LIEN}">Source</a>' if b.get('source_url') else ''
        return (f'<figure style="margin: 8px 0; display: flex; flex-direction: column; gap: 10px"><div style="border-radius: 12px; background: #171717; overflow: hidden">'
                f'<div style="padding: 10px 16px; border-bottom: 1px solid #2a2a2a; {MONO}; font-size: 12px; color: #a3a3a3">{e(b.get("langage"))}</div>'
                f'<pre style="margin: 0; padding: 18px 16px; overflow-x: auto; {MONO}; font-size: 14px; line-height: 1.65; color: #ebebeb"><code>{e(b["code"])}</code></pre></div>'
                f'<figcaption style="display: flex; flex-wrap: wrap; gap: 4px 10px; font-size: 14px; line-height: 1.5; color: #5c5c5c"><span>{e(b.get("legende"))}</span>{source}</figcaption></figure>')
    if t == 'chiffre':
        source = f'<a href="{e(b["source_url"])}" style="{LIEN}; font-size: 14px">Source</a>' if b.get('source_url') else ''
        return (f'<figure style="margin: 16px 0; padding-top: 20px; border-top: 1px solid #171717; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 8px 32px; align-items: end">'
                f'<span style="{TIGHT}; font-size: clamp(56px, 6cqw, 88px); line-height: .95; letter-spacing: -0.04em; color: #2f4bff">{e(b["valeur"])}</span>'
                f'<figcaption style="display: flex; flex-direction: column; gap: 6px; font-size: 16px; line-height: 1.5; color: #171717"><span>{e(b["libelle"])}</span>{source}</figcaption></figure>')
    if t == 'encart':
        return (f'<aside style="margin: 8px 0; padding: 24px; background: #f5f5f5; border-radius: 12px; display: flex; flex-direction: column; gap: 8px">'
                f'<p style="margin: 0; font-weight: 600; font-size: 17px; color: #171717">{e(b.get("titre"))}</p><p style="margin: 0; font-size: 17px; line-height: 1.65; color: #3d3d3d">{e(b["texte"])}</p></aside>')
    if t == 'capture':
        c = captures.get(b['cle'])
        if not c:
            return ''
        return (f'<figure style="margin: 16px 0; display: flex; flex-direction: column; gap: 10px"><div style="padding: 10px; background: #f5f5f5; border-radius: 14px">'
                f'<div style="overflow: hidden; border-radius: 8px; border: 1px solid #e5e5e5; background: #ffffff"><img src="{c["image"]}" alt="{e(c["alt"])}" width="{c["l"]}" height="{c["h"]}" loading="lazy" decoding="async" style="display: block; width: 100%; height: auto"></div></div>'
                f'<figcaption style="display: flex; flex-wrap: wrap; gap: 4px 10px; font-size: 14px; line-height: 1.5; color: #5c5c5c"><span>{e(c["legende"])}</span><a href="{e(c["url"])}" style="{LIEN}">Voir la page</a></figcaption></figure>')
    raise ValueError(t)


def nettoyer_depuis(t):
    t = re.sub(r'^Et depuis\s*:\s*', '', (t or '').strip())
    t = re.sub(r'\s*Sources?\s*:\s*\S+\s*$', '', t)
    return t[:1].upper() + t[1:] if t else ''


def page_article(a):
    chemin = f'/actualites/{a["slug"]}/'
    voisins = [x for x in articles if x['id'] != a['id']]
    aussi = ([x for x in voisins if x['rubrique'] == a['rubrique']] + [x for x in voisins if x['rubrique'] != a['rubrique']])[:3]
    depuis = nettoyer_depuis(a.get('et_depuis'))
    bloc_depuis = (f'<section aria-label="Et depuis" style="margin-top: 24px; padding: 24px; background: #f5f5f5; border-radius: 12px; display: flex; flex-direction: column; gap: 8px">'
                   f'<p style="margin: 0; {MONO}; font-size: 12px; color: #2f4bff">Et depuis</p><p style="margin: 0; font-size: 17px; line-height: 1.65; color: #171717">{e(depuis)}</p></section>') if depuis else ''
    sources = ''.join(f'<li style="padding-block: 10px; border-top: 1px solid #e5e5e5"><a href="{e(s["url"])}" style="{LIEN}; overflow-wrap: anywhere">{e(s["libelle"])}</a></li>' for s in a.get('sources', []))
    bloc_sources = f'<div style="display: flex; flex-direction: column; gap: 10px"><h2 style="margin: 0; {MONO}; font-size: 12px; font-weight: 400; color: #5c5c5c">Sources</h2><ol style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column">{sources}</ol></div>' if sources else ''
    mots = ''.join(f'<li style="{MONO}; font-size: 12px; padding: 4px 10px; border-radius: 999px; background: #f5f5f5; color: #3d3d3d">{e(m)}</li>' for m in a.get('mots_cles', []))
    extrait = (f'<figure style="margin: 0; padding: 24px; border: 1px solid #e5e5e5; border-radius: 12px; display: flex; flex-direction: column; gap: 14px">'
               f'<figcaption style="{MONO}; font-size: 12px; color: #5c5c5c">En discussion sur LinkedIn</figcaption>'
               f'<blockquote style="margin: 0; color: #171717; font-size: 16px; line-height: 1.6"><p style="margin: 0">« {e(a["extrait_post"])} »</p></blockquote>'
               f'<a href="{e(a["linkedin_url"])}" style="align-self: start; display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border: 1px solid #b3b3b3; border-radius: 8px; color: #171717; text-decoration: none; font-weight: 500">Rejoindre la discussion</a></figure>') if a.get('extrait_post') else ''
    cartes_aussi = ''.join(f'<li>{carte(x)}</li>' for x in aussi)
    corps = f'''<div style="container-type: inline-size; background: #ffffff; color: #171717">
<main id="contenu">
<article aria-labelledby="titre-article">
<header style="padding-block: clamp(48px, 6cqw, 96px) clamp(32px, 4cqw, 56px)">
<div style="{WRAP}; display: flex; flex-direction: column; gap: 24px">
<nav aria-label="Fil d’Ariane" style="{MONO}; font-size: 13px; color: #5c5c5c"><a href="/" style="color: #5c5c5c">Accueil</a> / <a href="/actualites/" style="color: #5c5c5c">Actualités</a> / <span aria-current="page">{e(a["rubrique"])}</span></nav>
<p style="margin: 0; {MONO}; font-size: 13px; color: #5c5c5c"><time datetime="{a["date"]}">{a["date_affichee"]}</time> · {a["temps_lecture"]} min de lecture · par <a href="/" rel="author" style="color: #5c5c5c">{NOM}</a></p>
<h1 id="titre-article" style="margin: 0; max-width: 1080px; {TIGHT}; font-size: clamp(40px, 5cqw, 76px); line-height: 1.03; letter-spacing: -0.03em">{e(a["titre"])} <span style="color: #9a9a9a">{e(a["suite"])}</span></h1>
<p style="margin: 0; max-width: 760px; font-size: 22px; line-height: 1.55; color: #3d3d3d">{e(a["chapo"])}</p>
</div>
</header>
<figure style="{WRAP}; margin: 0 auto">
<div style="overflow: hidden; border-radius: 16px; border: 1px solid #ebebeb; background: #ffffff"><img src="/assets/img/actualites/{a["slug"]}.svg" data-theme-img="clair" alt="{e(a["visuel_alt"])}" width="1200" height="675" fetchpriority="high" style="display: block; width: 100%; height: auto"><img src="/assets/img/actualites/{a["slug"]}-nuit.svg" data-theme-img="sombre" alt="{e(a["visuel_alt"])}" width="1200" height="675" loading="lazy" style="display: block; width: 100%; height: auto"></div>
</figure>
<div style="{WRAP}; padding-block: clamp(48px, 5cqw, 80px) clamp(72px, 8cqw, 128px); display: flex; flex-wrap: wrap; gap: 48px clamp(48px, 7cqw, 112px); align-items: flex-start">
<div style="flex: 999 1 560px; min-width: 0; max-width: 700px; display: flex; flex-direction: column; gap: 24px; font-size: 18px; line-height: 1.75; color: #3d3d3d">
{chr(10).join(bloc(b) for b in a["corps"])}
{bloc_depuis}
</div>
<aside aria-label="À propos de cet article" style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 28px; font-size: 15px">
{extrait}
{bloc_sources}
<ul aria-label="Mots-clés" style="margin: 0; padding: 0; list-style: none; display: flex; flex-wrap: wrap; gap: 8px">{mots}</ul>
<div style="padding-top: 20px; border-top: 1px solid #171717; display: flex; flex-direction: column; gap: 6px">
<b style="font-weight: 600; color: #171717">{NOM}</b>
<span style="color: #5c5c5c">Développeur Symfony et Sylius, freelance à Bordeaux. Fondateur de Yedra.</span>
<a href="/#missions" style="color: #2f4bff; font-weight: 500; text-underline-offset: 4px">Voir les missions</a>
</div>
</aside>
</div>
</article>
<section aria-labelledby="titre-aussi" style="padding-bottom: clamp(72px, 8cqw, 128px)">
<div style="{WRAP}; display: flex; flex-direction: column; gap: 32px">
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: 12px; padding-top: 24px; border-top: 1px solid #171717">
<h2 id="titre-aussi" style="margin: 0; {TIGHT}; font-size: 34px; letter-spacing: -0.02em">À lire aussi.</h2>
<a href="/actualites/" style="color: #2f4bff; font-weight: 500; text-underline-offset: 4px">Toutes les actualités</a>
</div>
<ul style="margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr)); gap: 48px 32px">{cartes_aussi}</ul>
</div>
</section>
</main>
{pied_actualites()}
</div>'''
    image = f'/assets/img/partage/article-{a["slug"]}.jpg'
    donnees = graphe(
        {'@type': 'BlogPosting', '@id': url(chemin) + '#article', 'headline': a['titre'].rstrip('.'), 'alternativeHeadline': a['suite'],
         'description': a['meta_description'], 'datePublished': a['date'], 'dateModified': MISE_A_JOUR, 'inLanguage': 'fr-FR',
         'author': {'@id': PERSONNE['@id']}, 'publisher': {'@id': PERSONNE['@id']}, 'mainEntityOfPage': url(chemin),
         'image': [url(image), url(f'/assets/img/actualites/{a["slug"]}-carte.webp')], 'articleSection': a['rubrique'],
         'keywords': a.get('mots_cles', []), 'wordCount': sum(len((b.get('texte') or ' '.join(b.get('items', []))).split()) for b in a['corps']),
         'citation': [s['url'] for s in a.get('sources', [])], 'isPartOf': {'@id': url('/actualites/') + '#blog'},
         'discussionUrl': a['linkedin_url']},
        PERSONNE, SITE_WEB, fil(('Accueil', '/'), ('Actualités', '/actualites/'), (a['titre'].rstrip('.'), chemin)))
    tete = f'<meta property="article:published_time" content="{a["date"]}">\n<meta property="article:modified_time" content="{MISE_A_JOUR}">\n<meta property="article:author" content="{SITE}/">\n<meta property="article:section" content="{e(a["rubrique"])}">\n'
    page(chemin, a['titre'].rstrip('.'), a['meta_description'], corps, courant='Actualités', image=image, image_alt=a['visuel_alt'],
         type_og='article', donnees=donnees, tete=tete, date_modif=MISE_A_JOUR, priorite='0.7')


def page_actualites():
    une, reste = articles[0], articles[1:]
    cartes = ''.join(f'<li style="padding-top: 24px; border-top: 1px solid #e5e5e5">{carte(a)}</li>' for a in reste)
    corps = f'''<div style="container-type: inline-size; background: #ffffff; color: #171717">
<main id="contenu">
<section aria-labelledby="titre-actualites" style="padding-block: clamp(48px, 6cqw, 96px) clamp(40px, 4cqw, 64px)">
<div style="{WRAP}; display: flex; flex-direction: column; gap: 24px">
<nav aria-label="Fil d’Ariane" style="{MONO}; font-size: 13px; color: #5c5c5c"><a href="/" style="color: #5c5c5c">Accueil</a> / <span aria-current="page">Actualités</span></nav>
<h1 id="titre-actualites" style="margin: 0; max-width: 1080px; {TIGHT}; font-size: clamp(42px, 5.4cqw, 80px); line-height: 1.02; letter-spacing: -0.03em">Actualités. <span style="color: #9a9a9a">Ce que je lis, ce que je teste, ce que je construis.</span></h1>
<p style="margin: 0; max-width: 680px; font-size: 19px; color: #3d3d3d">L’écosystème PHP, l’IA dans le métier de développeur, les outils de mon quotidien, et Yedra.</p>
</div>
</section>
<section aria-label="À la une" style="padding-bottom: clamp(56px, 6cqw, 96px)">
<div style="{WRAP}">
<a href="/actualites/{une["slug"]}/" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)); gap: 32px clamp(32px, 4cqw, 64px); align-items: center; color: #171717; text-decoration: none; padding-top: 32px; border-top: 1px solid #171717">
<span style="display: block; overflow: hidden; border-radius: 16px; background: #171717"><img src="/assets/img/actualites/{une["slug"]}-yedra-carte.webp" alt="{e(une["visuel_alt"])}" width="800" height="450" fetchpriority="high" style="display: block; width: 100%; height: auto"></span>
<span style="display: flex; flex-direction: column; gap: 20px">
<span style="{MONO}; font-size: 12px; color: #5c5c5c"><time datetime="{une["date"]}">{une["date_affichee"]}</time> · {e(une["rubrique"])}</span>
<span style="{TIGHT}; font-size: clamp(28px, 3cqw, 40px); line-height: 1.1; letter-spacing: -0.025em">{e(une["titre"])} <span style="color: #8a8a8a">{e(une["suite"])}</span></span>
<span style="font-size: 17px; color: #3d3d3d">{e(une["chapo"])}</span>
<span style="color: #2f4bff; font-weight: 500">Lire l’article · {une["temps_lecture"]} min</span>
</span>
</a>
</div>
</section>
<section aria-labelledby="titre-tous" style="padding-bottom: clamp(72px, 8cqw, 128px)">
<div style="{WRAP}; display: flex; flex-direction: column; gap: 24px">
<h2 id="titre-tous" style="margin: 0; {MONO}; font-size: 13px; font-weight: 400; color: #5c5c5c">Tous les articles</h2>
<ol style="margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 340px), 1fr)); gap: 56px 32px">{cartes}</ol>
</div>
</section>
</main>
{pied_actualites()}
</div>'''
    donnees = graphe(
        {'@type': 'Blog', '@id': url('/actualites/') + '#blog', 'name': f'Actualités de {NOM}', 'url': url('/actualites/'), 'inLanguage': 'fr-FR',
         'author': {'@id': PERSONNE['@id']}, 'publisher': {'@id': PERSONNE['@id']},
         'blogPost': [{'@type': 'BlogPosting', '@id': url(f'/actualites/{a["slug"]}/') + '#article', 'headline': a['titre'].rstrip('.'),
                       'datePublished': a['date'], 'url': url(f'/actualites/{a["slug"]}/')} for a in articles]},
        PERSONNE, SITE_WEB, fil(('Accueil', '/'), ('Actualités', '/actualites/')))
    page('/actualites/', 'Actualités : PHP, Sylius, IA et outils de développeur',
         'Les notes de Mickaël Teixeira, développeur Symfony et Sylius à Bordeaux : l’écosystème PHP, l’IA dans le métier de développeur, les outils et Yedra.',
         corps, courant='Actualités', image='/assets/img/partage/actualites.jpg', image_alt='Actualités de Mickaël Teixeira',
         donnees=donnees, date_modif=articles[0]['date'], priorite='0.8')


def flux():
    entrees = ''.join(f'''<entry>
<title>{e(a["titre"].rstrip("."))}</title>
<link href="{url(f"/actualites/{a['slug']}/")}"/>
<id>{url(f"/actualites/{a['slug']}/")}</id>
<published>{a["date"]}T09:00:00+01:00</published>
<updated>{a["date"]}T09:00:00+01:00</updated>
<category term="{e(a["rubrique"])}"/>
<summary>{e(a["chapo"])}</summary>
</entry>
''' for a in articles)
    ecrire('/actualites/flux.xml', f'''<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="fr">
<title>Actualités de {NOM}</title>
<subtitle>L’écosystème PHP, l’IA dans le métier de développeur, les outils et Yedra.</subtitle>
<link href="{url("/actualites/flux.xml")}" rel="self"/>
<link href="{url("/actualites/")}"/>
<id>{url("/actualites/")}</id>
<updated>{articles[0]["date"]}T09:00:00+01:00</updated>
<author><name>{NOM}</name><uri>{SITE}/</uri></author>
{entrees}</feed>
''')


def page_accueil():
    t = fragment('accueil.html')
    facade = ('<div class="facade" data-grille="/assets/img/facade-grille.png">'
              '<img src="/assets/img/facade-trame.svg" data-theme-img="clair" alt="Façade d’immeuble brutaliste dessinée en trame de lignes bleues" width="720" height="900" fetchpriority="high">'
              '<img src="/assets/img/facade-trame-nuit.svg" data-theme-img="sombre" alt="Façade d’immeuble brutaliste dessinée en trame de lignes bleues" width="720" height="900" loading="lazy">'
              '<canvas aria-hidden="true"></canvas></div>')
    t = t.replace('<!--facade-->', facade)
    cartes = '\n'.join(f'<li style="padding-top: 24px; border-top: 1px solid var(--trait)">{carte(a, theme_accueil=True)}</li>' for a in articles[:3])
    t = t.replace('<!--actualites-accueil-->', cartes)
    t = couvertures(t, '(min-width: 900px) 50vw, 100vw')
    assert '<!--' not in t
    donnees = graphe(
        {'@type': 'ProfilePage', '@id': SITE + '/#page', 'url': SITE + '/', 'name': 'Développeur Symfony et Sylius freelance à Bordeaux',
         'inLanguage': 'fr-FR', 'isPartOf': {'@id': SITE_WEB['@id']}, 'mainEntity': {'@id': PERSONNE['@id']},
         'about': {'@id': ACTIVITE['@id']}, 'dateModified': MISE_A_JOUR},
        PERSONNE, ACTIVITE, SITE_WEB,
        {'@type': 'Organization', '@id': 'https://yedra.app/#organisation', 'name': 'Yedra', 'url': 'https://yedra.app/',
         'description': 'Le CRM des écoles.', 'founder': {'@id': PERSONNE['@id']}})
    page('/', 'Mickaël Teixeira, développeur Symfony et Sylius à Bordeaux',
         'Développeur Symfony, Sylius et API Platform freelance à Bordeaux : migrations e-commerce, middle offices, API et flux ERP. Fondateur de Yedra.',
         t, donnees=donnees, image_alt='Mickaël Teixeira, développeur Symfony et Sylius freelance à Bordeaux', priorite='1.0')


def pages_missions():
    for m in MISSIONS:
        chemin = f'/missions/{m["slug"]}/'
        t = fragment(f'missions/{m["slug"]}.html').replace(f'<!--missions:{m["slug"]}-->', bande_missions(m['slug']))
        t = couvertures(t, '(min-width: 1312px) 1312px, 100vw')
        assert '<!--missions' not in t, m['slug']
        a_propos = {'@type': 'Organization', 'name': m['nom']}
        if m['client']:
            a_propos['url'] = m['client']
        donnees = graphe(
            {'@type': 'WebPage', '@id': url(chemin) + '#page', 'url': url(chemin), 'name': m['titre'], 'description': m['description'],
             'inLanguage': 'fr-FR', 'isPartOf': {'@id': SITE_WEB['@id']}, 'author': {'@id': PERSONNE['@id']}, 'about': a_propos,
             'primaryImageOfPage': url(f'/assets/img/missions/{m["slug"]}-couverture.webp'), 'dateModified': MISE_A_JOUR},
            PERSONNE, SITE_WEB, fil(('Accueil', '/'), ('Missions', '/#missions'), (m['nom'], chemin)))
        page(chemin, m['titre'], m['description'], t, courant='Missions', image=f'/assets/img/partage/mission-{m["slug"]}.jpg',
             image_alt=f'{m["nom"]} × {NOM}', donnees=donnees, priorite='0.8')


def pages_simples():
    page('/mentions-legales/', 'Mentions légales', 'Mentions légales du site de Mickaël Teixeira, entrepreneur individuel : éditeur, hébergement, données personnelles et crédits.',
         fragment('mentions-legales.html'), donnees=graphe(
             {'@type': 'WebPage', '@id': url('/mentions-legales/') + '#page', 'url': url('/mentions-legales/'), 'name': 'Mentions légales',
              'isPartOf': {'@id': SITE_WEB['@id']}}, SITE_WEB, fil(('Accueil', '/'), ('Mentions légales', '/mentions-legales/'))),
         priorite='0.2')
    page('/merci/', 'Message envoyé', 'Votre message est bien parti.', fragment('merci.html'), indexable=False)
    contenu = fragment('404.html')
    page('/404.html', 'Page introuvable', 'Cette page n’existe pas, ou plus.', contenu, indexable=False)


def redirections():
    anciennes = {'project-maxicoffee.html': 'maxicoffee', 'project-commande.html': 'commande', 'project-heyteam.html': 'heyteam', 'project-upd.html': 'upd'}
    for fichier, slug in anciennes.items():
        cible = url(f'/missions/{slug}/')
        ecrire('/' + fichier, f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Page déplacée</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="{cible}">
<meta http-equiv="refresh" content="0; url={cible}">
<script>location.replace({json.dumps(cible)})</script>
</head>
<body><p>Cette page a déménagé : <a href="{cible}">{cible}</a>.</p></body>
</html>
''')


def plan_du_site():
    lignes = ''.join(f'<url><loc>{loc}</loc><lastmod>{date}</lastmod><priority>{prio}</priority></url>\n' for loc, date, prio in pages_sitemap)
    ecrire('/sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{lignes}</urlset>\n')
    ecrire('/robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')


if __name__ == '__main__':
    page_accueil()
    pages_missions()
    for article in articles:
        page_article(article)
    page_actualites()
    flux()
    pages_simples()
    redirections()
    plan_du_site()
    print(f'{len(pages_sitemap)} pages indexables, {len(articles)} articles')
