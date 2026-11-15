"""Génère le site statique dans la racine du dépôt.

Usage : python3 _build/build.py
Sources : _build/contenu (fragments HTML), _build/donnees (articles, captures, pages, dates), _build/styles.
"""
import hashlib
import html
import json
import re
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

RACINE = Path(__file__).resolve().parent.parent
CONTENU = RACINE / '_build' / 'contenu'
DONNEES = RACINE / '_build' / 'donnees'
CSS = (RACINE / '_build' / 'styles' / 'site.css').read_text().strip()
SITE = 'https://mickaelteixeira.github.io'
NOM = 'Mickaël Teixeira'
AUJOURDHUI = date.today().isoformat()
VERIFICATION_GOOGLE = 'wsdzIL0Lmsbtvz1F2wSa2pzjxPZG2HtzG2G24YiEvAY'
CLE_INDEXNOW = 'cc7356b57641010ac676fad905b44676'
LINKEDIN = 'https://www.linkedin.com/in/dev-php-bordeaux/'
MALT = 'https://www.malt.fr/profile/mickaelteixeira'
GITHUB = 'https://github.com/mickaelteixeira'
PROFILS = [LINKEDIN, MALT, GITHUB]

MONO = "font-family: 'JetBrains Mono', monospace"
TIGHT = "font-family: 'Inter Tight', Inter, sans-serif; font-weight: 300"
WRAP = 'max-width: 1312px; margin: 0 auto; padding-inline: clamp(20px, 4.5cqw, 64px); box-sizing: border-box'
LIEN = 'color: #2f4bff; text-underline-offset: 3px'
H2 = f'margin: 0; {TIGHT}; font-size: 34px; line-height: 1.15; letter-spacing: -0.02em; color: #171717'
BOUTON = 'display: inline-flex; align-items: center; height: 48px; padding: 0 22px; border-radius: 8px; text-decoration: none; font-weight: 500; font-size: 16px'

MISSIONS = [
    {'slug': 'maxicoffee', 'resume': 'Un middle office pour les territoires, la facturation et la logistique, synchronisé avec Salesforce.', 'pile': 'PHP 8.3 · Laravel · API Platform · RedPanda',
     'nom': 'MaxiCoffee', 'annees': '2025 – 2026', 'role': 'Middle office · freelance',
     'titre': 'Middle office MaxiCoffee : Laravel et Salesforce',
     'description': 'Mission freelance chez MaxiCoffee (2025-2026) : un middle office Laravel en architecture hexagonale et DDD, synchronisé avec Salesforce.',
     'client': 'https://www.maxicoffee.com/'},
    {'slug': 'commande', 'resume': 'La refonte complète d’une plateforme e-commerce sur Sylius, en headless.', 'pile': 'PHP 8.2 · Symfony · Sylius · API Platform',
     'nom': 'Commande.com', 'annees': '2025', 'role': 'Refonte Sylius · freelance, avec Dn’D',
     'titre': 'Refonte Sylius headless de Commande.com',
     'description': 'Mission freelance avec l’agence Dn’D (2025) : la refonte de Commande.com sur Sylius en headless, API Platform, flux ERP et transporteurs, tests automatisés.',
     'client': 'https://commande.com/'},
    {'slug': 'heyteam', 'resume': 'Une architecture modulaire pour relier une plateforme RH aux outils SIRH.', 'pile': 'Laravel 8 · PHP 7.4 · MySQL · DDD',
     'nom': 'HeyTeam', 'annees': '2025', 'role': 'Lead developer',
     'titre': 'HeyTeam : lead developer Laravel',
     'description': 'Lead developer chez HeyTeam en 2025 : une plateforme B2B d’onboarding reliée aux SIRH des clients, en architecture modulaire Laravel.',
     'client': 'https://www.heyteam.com/'},
    {'slug': 'upd', 'resume': 'La migration vers Sylius d’un e-commerce de petfood à fort trafic.', 'pile': 'PHP 8 · Symfony 5 · Sylius 1.10 · API Platform',
     'nom': 'Ultra Premium Direct', 'annees': '2022 – 2024', 'role': 'Migration Sylius · backend',
     'titre': 'Migration Sylius d’Ultra Premium Direct',
     'description': 'Développeur backend chez Ultra Premium Direct de 2022 à 2024 : la migration vers Sylius d’un e-commerce de petfood à fort trafic, en Symfony.',
     'client': 'https://www.ultrapremiumdirect.com/'},
    {'slug': 'onepoint', 'resume': 'Six missions chez cinq clients : Enedis, Gaz de Bordeaux, PSA, Bureau Veritas Pro, SMIP.', 'pile': 'Zend Framework · Symfony · Angular · Java',
     'nom': 'onepoint', 'annees': '2013 – 2022', 'role': 'Six missions en conseil · full-stack',
     'titre': 'onepoint : huit ans de conseil en développement',
     'description': 'Développeur full-stack chez onepoint de 2013 à 2022 : six missions pour Enedis, Gaz de Bordeaux, PSA, Bureau Veritas Pro et SMIP, de Zend à Angular.',
     'client': 'https://www.groupeonepoint.com/'},
    {'slug': 'timeone', 'resume': 'Des outils pour l’affiliation, une application mobile, Scrum.', 'pile': 'PHP · MySQL · jQuery · PhoneGap',
     'nom': 'TimeOne', 'annees': '2012 – 2013', 'role': 'Outils d’affiliation · PHP',
     'titre': 'TimeOne : outils d’affiliation en PHP',
     'description': 'Développeur PHP chez TimeOne de 2012 à 2013 : des outils pour un réseau d’affiliation, une application mobile et la pratique de Scrum au quotidien.',
     'client': 'https://www.timeonegroup.com/'},
    {'slug': 'webstrategies', 'resume': 'Des sites et un premier paiement e-commerce, en agence.', 'pile': 'PHP 5 · Magento · Joomla · WordPress',
     'nom': 'Web Stratégies', 'annees': '2009 – 2011', 'role': 'Sites et e-commerce · alternance',
     'titre': 'Web Stratégies : alternance de développeur PHP',
     'description': 'Alternance de développeur PHP chez Web Stratégies, agence web de Bordeaux, de 2009 à 2011 : des sites, de la maquette au paiement Magento.',
     'client': 'https://www.webstrategies.fr/'},
    {'slug': 'illicotravel', 'resume': 'Brancher de nouveaux partenaires au moteur d’un comparateur de voyages.', 'pile': 'PHP · MySQL · XML · MooTools',
     'nom': 'illicotravel', 'annees': '2009', 'role': 'Comparateur de voyages · stage',
     'titre': 'illicotravel : flux partenaires en PHP',
     'description': 'Stage de développeur PHP chez illicotravel en 2009 : intégrer les flux XML de nouveaux partenaires au moteur d’un comparateur de voyages.',
     'client': None},
]
MISSION = {m['slug']: m for m in MISSIONS}

ETAPES = [
    ('2025 – aujourd’hui', 'Développeur freelance', [('MaxiCoffee', '/missions/maxicoffee/'), ('Commande.com, avec l’agence Dn’D', '/missions/commande/')]),
    ('2024 – aujourd’hui', 'Fondateur et éditeur', [('Yedra, le CRM des écoles', 'https://yedra.app')]),
    ('2025', 'Lead developer', [('HeyTeam', '/missions/heyteam/')]),
    ('2022 – 2024', 'Développeur backend e-commerce', [('Ultra Premium Direct', '/missions/upd/')]),
    ('2013 – 2022', 'Développeur full-stack', [('onepoint : Enedis, Gaz de Bordeaux, PSA, Bureau Veritas Pro, SMIP', '/missions/onepoint/')]),
    ('2012 – 2013', 'Développeur PHP', [('TimeOne', '/missions/timeone/')]),
    ('2009 – 2011', 'Développeur PHP en alternance', [('Agence Web Stratégies', '/missions/webstrategies/'), ('illicotravel', '/missions/illicotravel/')]),
    ('2008 – 2011', 'Master Architecte logiciel', [('ETNA, école d’alternance en informatique', None)]),
]
ARTICLES_LIES = {
    'symfony': ['php-generiques-typephp', 'sylius-prestashop-rapprochement'],
    'sylius': ['sylius-prestashop-rapprochement'],
    'laravel': ['php-generiques-typephp'],
}

articles = sorted(json.loads((DONNEES / 'articles.json').read_text()), key=lambda a: a['date'], reverse=True)
ARTICLE = {a['slug']: a for a in articles}
captures = json.loads((DONNEES / 'captures.json').read_text())
PAGES = json.loads((DONNEES / 'pages.json').read_text())
expertises = PAGES['expertises']
for m in MISSIONS:
    m['expertises'] = [x for x in expertises if any(p['slug'] == m['slug'] for p in x['preuves']['missions'])]
FICHIER_DATES = DONNEES / 'dates.json'
dates = json.loads(FICHIER_DATES.read_text()) if FICHIER_DATES.exists() else {}
pages_sitemap = []
textes_llm = []


def e(texte):
    return html.escape(texte or '', quote=True)


def url(chemin):
    return chemin if chemin.startswith('http') else SITE + chemin


def ecrire(chemin, contenu):
    cible = RACINE / chemin.lstrip('/')
    if chemin.endswith('/'):
        cible = cible / 'index.html'
    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(contenu)


def fragment(nom):
    return (CONTENU / nom).read_text()


def sans_point(texte):
    return texte.rstrip('.')


def horodatage(jour):
    return datetime.fromisoformat(jour).replace(hour=12, tzinfo=ZoneInfo('Europe/Paris')).isoformat()


def date_modif(chemin, signature):
    empreinte = hashlib.sha256(signature.encode()).hexdigest()[:16]
    connue = dates.get(chemin)
    if not connue or connue['empreinte'] != empreinte:
        dates[chemin] = {'empreinte': empreinte, 'modifie': AUJOURDHUI}
    return dates[chemin]['modifie']


def en_texte(source):
    t = re.sub(r'<section(?:(?!<section).)*?<!--fixe--><article.*?<!--/fixe-->.*?</section>', '', source, flags=re.S)
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    t = re.sub(r'<(svg|script|style|nav|form)\b.*?</\1>', ' ', t, flags=re.S)
    t = re.sub(r'</dt>\s*<dd[^>]*>', ' : ', t)
    t = re.sub(r'<(h[1-4])[^>]*>', lambda m: '\n\n' + '#' * (int(m.group(1)[1]) + 1) + ' ', t)
    t = re.sub(r'<li[^>]*>', '\n- ', t)
    t = re.sub(r'<(p|dt|dd|blockquote|figcaption|tr)[^>]*>', '\n', t)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    lignes = [' '.join(ligne.split()) for ligne in t.split('\n')]
    return '\n'.join(ligne for ligne in lignes if ligne and ligne not in ('-', 'Lire la mission →')).replace('\n##', '\n\n##')


PERSONNE = {
    '@type': 'Person', '@id': SITE + '/#mickael-teixeira', 'name': NOM, 'givenName': 'Mickaël', 'familyName': 'Teixeira',
    'jobTitle': 'Développeur Symfony et Sylius freelance', 'url': SITE + '/', 'mainEntityOfPage': SITE + '/parcours/',
    'image': url('/assets/img/mickael-teixeira-developpeur-symfony-bordeaux.webp'),
    'description': 'Développeur PHP depuis 2009, freelance à Bordeaux depuis 2025 : Symfony, Sylius, API Platform et Laravel. Fondateur de Yedra, le CRM des écoles.',
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Bordeaux', 'addressRegion': 'Nouvelle-Aquitaine', 'addressCountry': 'FR'},
    'workLocation': {'@type': 'City', 'name': 'Bordeaux'},
    'alumniOf': {'@type': 'EducationalOrganization', 'name': 'ETNA', 'url': 'https://etna.io/'},
    'hasCredential': {'@type': 'EducationalOccupationalCredential', 'name': 'Master Architecte logiciel', 'credentialCategory': 'degree',
                      'recognizedBy': {'@type': 'EducationalOrganization', 'name': 'ETNA'}},
    'hasOccupation': {'@type': 'Occupation', 'name': 'Développeur web freelance',
                      'occupationLocation': {'@type': 'City', 'name': 'Bordeaux'},
                      'skills': 'PHP, Symfony, Sylius, API Platform, Laravel, architecture hexagonale, Domain-Driven Design, intégration ERP et CRM'},
    'knowsAbout': ['PHP', 'Symfony', 'Sylius', 'API Platform', 'Laravel', 'E-commerce', 'Architecture hexagonale',
                   'Domain-Driven Design', 'Salesforce', 'Angular', 'Elasticsearch', 'RabbitMQ', 'RedPanda', 'Docker', 'GitLab CI',
                   'Tests automatisés'],
    'knowsLanguage': ['fr', 'en'],
    'worksFor': {'@id': SITE + '/#activite'},
    'sameAs': PROFILS,
}
ACTIVITE = {
    '@type': 'ProfessionalService', '@id': SITE + '/#activite', 'name': 'Mickaël Teixeira, développeur Symfony et Sylius freelance',
    'url': SITE + '/', 'image': url('/assets/img/partage/accueil.jpg'), 'founder': {'@id': PERSONNE['@id']},
    'description': 'Développement freelance Symfony, Sylius et API Platform : migrations e-commerce vers Sylius, middle offices, API, flux ERP, CRM et transporteurs.',
    'address': {'@type': 'PostalAddress', 'postalCode': '33290', 'addressLocality': 'Le Pian-Médoc',
                'addressRegion': 'Nouvelle-Aquitaine', 'addressCountry': 'FR'},
    'areaServed': [{'@type': 'City', 'name': 'Bordeaux'}, {'@type': 'City', 'name': 'Paris'}, {'@type': 'City', 'name': 'Lyon'},
                   {'@type': 'City', 'name': 'Lille'}, {'@type': 'City', 'name': 'Nantes'}, {'@type': 'Country', 'name': 'France'}],
    'availableLanguage': ['fr', 'en'],
    'contactPoint': {'@type': 'ContactPoint', 'contactType': 'Demande de mission', 'url': SITE + '/#contact', 'availableLanguage': ['fr', 'en']},
    'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Expertises', 'itemListElement': [
        {'@type': 'Offer', 'itemOffered': {'@id': f'{SITE}/expertises/{x["slug"]}/#service'}} for x in expertises]},
    'vatID': 'FR88831303185', 'taxID': '831 303 185', 'sameAs': PROFILS,
}
SITE_WEB = {'@type': 'WebSite', '@id': SITE + '/#site', 'url': SITE + '/', 'name': NOM,
            'alternateName': 'Mickaël Teixeira, développeur Symfony et Sylius freelance', 'inLanguage': 'fr-FR',
            'description': 'Le site de Mickaël Teixeira, développeur Symfony, Sylius et API Platform freelance à Bordeaux.',
            'publisher': {'@id': PERSONNE['@id']}}


def fil(*etapes):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': nom, 'item': url(chemin)} for i, (nom, chemin) in enumerate(etapes)]}


def graphe(*noeuds):
    return {'@context': 'https://schema.org', '@graph': [n for n in noeuds if n]}


def questions(faq):
    return {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q['question'], 'acceptedAnswer': {'@type': 'Answer', 'text': q['reponse']}} for q in faq]}


def service(x):
    return {'@type': 'Service', '@id': f'{SITE}/expertises/{x["slug"]}/#service', 'name': sans_point(x['h1']),
            'serviceType': x['nom'], 'description': x['meta_description'], 'url': f'{SITE}/expertises/{x["slug"]}/',
            'provider': {'@id': ACTIVITE['@id']}, 'areaServed': ACTIVITE['areaServed'], 'availableLanguage': ['fr', 'en']}


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
    st = re.sub(r'(?<![-\w])color: #9a9a9a', 'color: #8a8a8a', st)
    st = st.replace('#2f4bff', 'var(--accent)')
    if sur_accent:
        st = st.replace('color: #ffffff', 'color: var(--sur-accent)')
    return st.replace('§lavande§', 'background: #8fa2ff; color: #171717')


def themer(texte):
    morceaux = re.split(r'(<!--fixe-->.*?<!--/fixe-->)', texte, flags=re.S)
    return ''.join(m.replace('<!--fixe-->', '').replace('<!--/fixe-->', '') if m.startswith('<!--fixe-->')
                   else re.sub(r'style="([^"]*)"', lambda s: f'style="{jetons(s.group(1))}"', m) for m in morceaux)


def couvertures(texte, tailles, differe=True):
    def balise(m):
        slug = m.group(1)
        base = f'/assets/img/missions/{slug}-couverture'
        return (f'<img src="{base}.webp" srcset="{base}-480.webp 480w, {base}-800.webp 800w, {base}.webp 1600w" '
                f'sizes="{tailles(slug) if callable(tailles) else tailles}"' + (' loading="lazy" decoding="async"' if differe else ' fetchpriority="high"'))
    return re.sub(r'<img src="/assets/img/missions/([a-z]+)-couverture\.webp"', balise, texte)


def entete(courant):
    liens = [('Missions', '/missions/'), ('Expertises', '/expertises/'), ('Yedra', '/#yedra'), ('Parcours', '/parcours/'),
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


def pied():
    liste = lambda liens: ''.join(f'<li><a href="{h}"{attr}>{e(n)}</a></li>' for n, h, attr in liens)
    expertises_liens = [(x['nom'], f'/expertises/{x["slug"]}/', '') for x in expertises]
    site = [('Missions', '/missions/', ''), ('Parcours', '/parcours/', ''), ('Actualités', '/actualites/', ''),
            ('Contact', '/#contact', ''), ('Mentions légales', '/mentions-legales/', '')]
    profils = [('LinkedIn', LINKEDIN, ' rel="me noopener"'), ('Malt', MALT, ' rel="me noopener"'),
               ('GitHub', GITHUB, ' rel="me noopener"'), ('Yedra', 'https://yedra.app', ' rel="noopener"')]
    return f'''<footer class="pied">
<div class="pied__cadre">
<div class="pied__grille">
<div class="pied__marque">
<a class="pied__nom" href="/">{NOM}</a>
<p>Développeur Symfony et Sylius freelance à Bordeaux. PHP depuis 2009.</p>
</div>
<nav aria-labelledby="pied-expertises"><h2 class="pied__titre" id="pied-expertises">Expertises</h2><ul>{liste(expertises_liens)}</ul></nav>
<nav aria-labelledby="pied-site"><h2 class="pied__titre" id="pied-site">Site</h2><ul>{liste(site)}</ul></nav>
<nav aria-labelledby="pied-profils"><h2 class="pied__titre" id="pied-profils">Profils</h2><ul>{liste(profils)}</ul></nav>
</div>
<div class="pied__bas">
<span>© 2026 {NOM} · entrepreneur individuel · Bordeaux</span>
<a href="/actualites/flux.xml">Flux des actualités</a>
</div>
</div>
</footer>'''


def page(chemin, titre, description, corps, *, courant=None, image='/assets/img/partage/accueil.jpg',
         image_alt='Mickaël Teixeira, développeur Symfony et Sylius à Bordeaux', type_og='website', donnees=None,
         indexable=True, tete='', modifie=None, priorite='0.6'):
    titre_complet = titre if NOM in titre or len(titre) > 43 else f'{titre} · {NOM}'
    canonique = url(chemin)
    robots = 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' if indexable else 'noindex, follow'
    jsonld = f'<script type="application/ld+json">{json.dumps(donnees, ensure_ascii=False, separators=(",", ":"))}</script>' if donnees else ''
    if indexable:
        pages_sitemap.append((canonique, modifie or date_modif(chemin, titre + description + corps), priorite))
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
<link rel="preload" href="/assets/fonts/inter-400-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-tight-300-400.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">
<link rel="alternate" type="application/atom+xml" title="Actualités de {NOM}" href="/actualites/flux.xml">
<link rel="alternate" type="text/plain" title="Résumé du site pour les modèles de langage" href="/llms.txt">
<link rel="me" href="{LINKEDIN}">
<link rel="me" href="{GITHUB}">
<meta property="og:type" content="{type_og}">
<meta property="og:site_name" content="{NOM}">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{e(titre)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{canonique}">
<meta property="og:image" content="{url(image)}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(image_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(titre)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{url(image)}">
{tete}{jsonld}
</head>
<body>
{entete(courant)}
{themer(corps)}
{pied()}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
'''
    ecrire(chemin, contenu)


def ariane(*etapes):
    morceaux = [f'<a href="{c}" style="color: #5c5c5c">{e(n)}</a>' if c else f'<span aria-current="page">{e(n)}</span>' for n, c in etapes]
    return f'<nav aria-label="Fil d’Ariane" style="{MONO}; font-size: 13px; color: #5c5c5c">{" / ".join(morceaux)}</nav>'


def ouverture(identifiant, etapes, h1, suite, chapo, boutons=''):
    return f'''<section aria-labelledby="{identifiant}" style="padding-block: clamp(48px, 6cqw, 96px) clamp(40px, 4cqw, 64px)">
<div style="{WRAP}; display: flex; flex-direction: column; gap: 24px">
{ariane(*etapes)}
<h1 id="{identifiant}" style="margin: 0; max-width: 1080px; {TIGHT}; font-size: clamp(36px, 5.4cqw, 80px); line-height: 1.02; letter-spacing: -0.03em">{e(h1)} <span style="color: #8a8a8a">{e(suite)}</span></h1>
<p style="margin: 0; max-width: 760px; font-size: 21px; line-height: 1.55; color: #3d3d3d">{e(chapo)}</p>
{boutons}
</div>
</section>'''


def bande(titre, suite, complement=''):
    return f'''<section aria-labelledby="titre-suite" style="container-type: inline-size; background: #171717; color: #ebebeb; font-size: 16px; line-height: 1.55">
<div style="{WRAP}; padding-block: clamp(64px, 7cqw, 112px); display: flex; flex-direction: column; gap: clamp(48px, 5cqw, 72px)">
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: end; gap: 32px 64px">
<h2 id="titre-suite" style="margin: 0; flex: 1 1 520px; {TIGHT}; font-size: clamp(36px, 4.2cqw, 64px); line-height: 1.04; letter-spacing: -0.03em; color: #ffffff">{e(titre)} <span style="color: #8a8a8a">{e(suite)}</span></h2>
<div style="display: flex; flex-wrap: wrap; gap: 12px">
<a href="/#contact" style="{BOUTON}; background: #8fa2ff; color: #171717">Proposer une mission</a>
<a href="{LINKEDIN}" rel="noopener" style="{BOUTON}; border: 1px solid #5c5c5c; color: #ffffff">Suivre sur LinkedIn</a>
</div>
</div>
{complement}
</div>
</section>'''


def bande_missions(actuelle):
    lignes = []
    for m in MISSIONS:
        courant = m['slug'] == actuelle
        lignes.append(
            f'<li style="border-top: 1px solid #303030"><a href="/missions/{m["slug"]}/"{" aria-current=\"page\"" if courant else ""} '
            f'style="display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 2px 16px; padding-block: 14px; color: {"#8fa2ff" if courant else "#ebebeb"}; text-decoration: none">'
            f'<span style="font-weight: 500">{e(m["nom"])}</span><span style="{MONO}; font-size: 12px; color: #a3a3a3">{m["annees"]}</span>'
            f'<span style="grid-column: 1 / -1; font-size: 14px; color: #a3a3a3">{e(m["role"])}</span></a></li>')
    liste = f'''<nav aria-label="Toutes les missions" style="display: flex; flex-direction: column; gap: 16px">
<p style="margin: 0; {MONO}; font-size: 13px; color: #a3a3a3">Toutes les missions, depuis 2009</p>
<ol style="margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0 32px">
{chr(10).join(lignes)}
</ol>
</nav>'''
    return bande('La prochaine mission,', 'c’est peut-être la vôtre.', liste)


def bande_contact():
    return bande('Une plateforme à faire évoluer ?', 'Parlons-en.')


def carte(a, theme_accueil=False):
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


def bloc_texte(b):
    t = b['type']
    if t == 'p':
        return b['texte']
    if t == 'h2':
        return f'### {b["texte"]}'
    if t == 'liste':
        return '\n'.join(f'- {i}' for i in b['items'])
    if t == 'citation':
        return f'> « {b["texte"]} » ({b.get("auteur", "")})'
    if t == 'code':
        return f'```{b.get("langage", "")}\n{b["code"]}\n```'
    if t == 'chiffre':
        return f'**{b["valeur"]}** : {b["libelle"]}'
    if t == 'encart':
        return f'**{b.get("titre", "")}** {b["texte"]}'
    return ''


def nettoyer_depuis(t):
    t = re.sub(r'^Et depuis\s*:\s*', '', (t or '').strip())
    t = re.sub(r'\s*Sources?\s*:\s*\S+\s*$', '', t)
    return t[:1].upper() + t[1:] if t else ''


def liste_faq(faq):
    lignes = ''.join(
        f'<div style="padding-block: 20px; border-top: 1px solid #e5e5e5; display: flex; flex-direction: column; gap: 8px">'
        f'<h3 style="margin: 0; font-size: 18px; line-height: 1.4; font-weight: 600; color: #171717">{e(q["question"])}</h3>'
        f'<p style="margin: 0; font-size: 17px; line-height: 1.65">{e(q["reponse"])}</p></div>' for q in faq)
    return f'<div style="display: flex; flex-direction: column; border-bottom: 1px solid #e5e5e5">{lignes}</div>'


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
               f'<a href="{e(a["linkedin_url"])}" rel="noopener" style="align-self: start; display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border: 1px solid #b3b3b3; border-radius: 8px; color: #171717; text-decoration: none; font-weight: 500">Rejoindre la discussion</a></figure>') if a.get('extrait_post') else ''
    cartes_aussi = ''.join(f'<li>{carte(x)}</li>' for x in aussi)
    corps = f'''<div style="container-type: inline-size; background: #ffffff; color: #171717">
<main id="contenu">
<article aria-labelledby="titre-article">
<header style="padding-block: clamp(48px, 6cqw, 96px) clamp(32px, 4cqw, 56px)">
<div style="{WRAP}; display: flex; flex-direction: column; gap: 24px">
{ariane(('Accueil', '/'), ('Actualités', '/actualites/'), (a['rubrique'], None))}
<p style="margin: 0; {MONO}; font-size: 13px; color: #5c5c5c"><time datetime="{a["date"]}">{a["date_affichee"]}</time> · {a["temps_lecture"]} min de lecture · par <a href="/parcours/" rel="author" style="color: #5c5c5c">{NOM}</a></p>
<h1 id="titre-article" style="margin: 0; max-width: 1080px; {TIGHT}; font-size: clamp(40px, 5cqw, 76px); line-height: 1.03; letter-spacing: -0.03em">{e(a["titre"])} <span style="color: #8a8a8a">{e(a["suite"])}</span></h1>
<p style="margin: 0; max-width: 760px; font-size: 22px; line-height: 1.55; color: #3d3d3d">{e(a["chapo"])}</p>
</div>
</header>
<figure style="{WRAP}; margin: 0 auto">
<div style="overflow: hidden; border-radius: 16px; border: 1px solid #ebebeb; background: #ffffff"><img src="/assets/img/actualites/{a["slug"]}.svg" data-theme-img="clair" alt="{e(a["visuel_alt"])}" width="1200" height="675" loading="lazy" style="display: block; width: 100%; height: auto"><img src="/assets/img/actualites/{a["slug"]}-nuit.svg" data-theme-img="sombre" alt="{e(a["visuel_alt"])}" width="1200" height="675" loading="lazy" style="display: block; width: 100%; height: auto"></div>
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
<a href="/parcours/" style="font-weight: 600; color: #171717; text-decoration: none">{NOM}</a>
<span style="color: #5c5c5c">Développeur <a href="/expertises/symfony/" style="color: #5c5c5c">Symfony</a> et <a href="/expertises/sylius/" style="color: #5c5c5c">Sylius</a>, freelance à Bordeaux. Fondateur de Yedra.</span>
<a href="/missions/" style="color: #2f4bff; font-weight: 500; text-underline-offset: 4px">Voir les missions</a>
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
{bande_contact()}
</div>'''
    image = f'/assets/img/partage/article-{a["slug"]}.jpg'
    modifie = max(a['date'], date_modif(chemin, json.dumps(a, ensure_ascii=False, sort_keys=True)))
    donnees = graphe(
        {'@type': 'BlogPosting', '@id': url(chemin) + '#article', 'headline': sans_point(a['titre']), 'alternativeHeadline': a['suite'],
         'description': a['meta_description'], 'datePublished': a['date_heure'], 'dateModified': max(a['date_heure'], horodatage(modifie)), 'inLanguage': 'fr-FR',
         'author': {'@id': PERSONNE['@id']}, 'publisher': {'@id': PERSONNE['@id']}, 'mainEntityOfPage': url(chemin),
         'image': [url(image), url(f'/assets/img/actualites/{a["slug"]}-carte.webp')], 'articleSection': a['rubrique'],
         'keywords': a.get('mots_cles', []), 'wordCount': sum(len((b.get('texte') or ' '.join(b.get('items', []))).split()) for b in a['corps']),
         'citation': [s['url'] for s in a.get('sources', [])], 'isPartOf': {'@id': url('/actualites/') + '#blog'},
         'discussionUrl': a['linkedin_url']},
        PERSONNE, SITE_WEB, fil(('Accueil', '/'), ('Actualités', '/actualites/'), (sans_point(a['titre']), chemin)))
    tete = f'<meta property="article:published_time" content="{a["date_heure"]}">\n<meta property="article:modified_time" content="{max(a["date_heure"], horodatage(modifie))}">\n<meta property="article:author" content="{SITE}/parcours/">\n<meta property="article:section" content="{e(a["rubrique"])}">\n'
    page(chemin, sans_point(a['titre']), a['meta_description'], corps, courant='Actualités', image=image, image_alt=a['visuel_alt'],
         type_og='article', donnees=donnees, tete=tete, modifie=modifie, priorite='0.7')
    sources_texte = ''.join(f'\n- {s["libelle"]} : {s["url"]}' for s in a.get('sources', []))
    textes_llm.append((chemin, f'{a["titre"]} {a["suite"]}', f'Publié le {a["date_affichee"]} · {a["rubrique"]}\n\n{a["chapo"]}\n\n'
                       + '\n\n'.join(filter(None, (bloc_texte(b) for b in a['corps'])))
                       + (f'\n\nEt depuis : {depuis}' if depuis else '') + (f'\n\nSources :{sources_texte}' if sources_texte else '')))


def page_actualites():
    une, reste = articles[0], articles[1:]
    cartes = ''.join(f'<li style="padding-top: 24px; border-top: 1px solid #e5e5e5">{carte(a)}</li>' for a in reste)
    corps = f'''<div style="container-type: inline-size; background: #ffffff; color: #171717">
<main id="contenu">
<section aria-labelledby="titre-actualites" style="padding-block: clamp(48px, 6cqw, 96px) clamp(40px, 4cqw, 64px)">
<div style="{WRAP}; display: flex; flex-direction: column; gap: 24px">
{ariane(('Accueil', '/'), ('Actualités', None))}
<h1 id="titre-actualites" style="margin: 0; max-width: 1080px; {TIGHT}; font-size: clamp(42px, 5.4cqw, 80px); line-height: 1.02; letter-spacing: -0.03em">Actualités. <span style="color: #8a8a8a">Ce que je lis, ce que je teste, ce que je construis.</span></h1>
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
{bande_contact()}
</div>'''
    donnees = graphe(
        {'@type': 'Blog', '@id': url('/actualites/') + '#blog', 'name': f'Actualités de {NOM}', 'url': url('/actualites/'), 'inLanguage': 'fr-FR',
         'author': {'@id': PERSONNE['@id']}, 'publisher': {'@id': PERSONNE['@id']},
         'blogPost': [{'@type': 'BlogPosting', '@id': url(f'/actualites/{a["slug"]}/') + '#article', 'headline': sans_point(a['titre']),
                       'datePublished': a['date_heure'], 'url': url(f'/actualites/{a["slug"]}/')} for a in articles]},
        PERSONNE, SITE_WEB, fil(('Accueil', '/'), ('Actualités', '/actualites/')))
    page('/actualites/', 'Actualités : PHP, Sylius, IA et outils de développeur',
         'Les notes de Mickaël Teixeira, développeur Symfony et Sylius à Bordeaux : l’écosystème PHP, l’IA dans le métier de développeur, les outils et Yedra.',
         corps, courant='Actualités', image='/assets/img/partage/actualites.jpg', image_alt='Actualités de Mickaël Teixeira',
         donnees=donnees, modifie=date_modif('/actualites/', ''.join(a['slug'] + a['titre'] for a in articles)), priorite='0.8')


def flux():
    entrees = ''.join(f'''<entry>
<title>{e(sans_point(a["titre"]))}</title>
<link href="{url(f"/actualites/{a['slug']}/")}"/>
<id>{url(f"/actualites/{a['slug']}/")}</id>
<published>{a["date_heure"]}</published>
<updated>{a["date_heure"]}</updated>
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
<updated>{articles[0]["date_heure"]}</updated>
<author><name>{NOM}</name><uri>{SITE}/</uri></author>
{entrees}</feed>
''')


def page_accueil():
    source = fragment('accueil.html')
    facade = ('<div class="facade" data-grille="/assets/img/facade-grille.png">'
              '<img src="/assets/img/facade-trame.svg" data-theme-img="clair" alt="Façade d’immeuble brutaliste dessinée en trame de lignes bleues" width="720" height="900" fetchpriority="high">'
              '<img src="/assets/img/facade-trame-nuit.svg" data-theme-img="sombre" alt="Façade d’immeuble brutaliste dessinée en trame de lignes bleues" width="720" height="900" loading="lazy">'
              '<canvas aria-hidden="true"></canvas></div>')
    t = source.replace('<!--facade-->', facade)
    cartes = '\n'.join(f'<li style="padding-top: 24px; border-top: 1px solid var(--trait)">{carte(a, theme_accueil=True)}</li>' for a in articles[:3])
    t = t.replace('<!--actualites-accueil-->', cartes)
    liens = ''.join(f'<a href="/expertises/{x["slug"]}/" style="color: var(--lien); font-weight: 500; text-underline-offset: 4px">{e(x["nom"])}</a>' for x in expertises)
    t = t.replace('<!--liens-expertises-->', f'<nav aria-label="Expertises en détail" style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 12px 28px; padding-top: 24px; border-top: 1px solid var(--trait)"><span style="{MONO}; font-size: 12px; color: var(--second)">En détail</span>{liens}<a href="/expertises/" style="color: var(--encre); font-weight: 500; text-underline-offset: 4px">Toutes les expertises</a></nav>')
    grandes = {'maxicoffee', 'commande', 'heyteam', 'upd'}
    t = couvertures(t, lambda slug: '(min-width: 1100px) 640px, 100vw' if slug in grandes else '(min-width: 1160px) 320px, (min-width: 620px) 50vw, 100vw')
    assert '<!--' not in t
    modifie = date_modif('/', source)
    donnees = graphe(
        {'@type': 'ProfilePage', '@id': SITE + '/#page', 'url': SITE + '/', 'name': 'Développeur Symfony et Sylius freelance à Bordeaux',
         'inLanguage': 'fr-FR', 'isPartOf': {'@id': SITE_WEB['@id']}, 'mainEntity': {'@id': PERSONNE['@id']},
         'about': {'@id': ACTIVITE['@id']}, 'dateModified': horodatage(modifie)},
        PERSONNE, ACTIVITE, SITE_WEB,
        {'@type': 'Organization', '@id': 'https://yedra.app/#organisation', 'name': 'Yedra', 'url': 'https://yedra.app/',
         'description': 'Yedra, le CRM des écoles et des établissements scolaires.', 'founder': {'@id': PERSONNE['@id']},
         'foundingDate': '2024-11'})
    page('/', 'Développeur Symfony & Sylius freelance à Bordeaux · Mickaël Teixeira',
         'Développeur Symfony, Sylius et API Platform freelance à Bordeaux, PHP depuis 2009 : migrations e-commerce, middle offices, API et flux ERP.',
         t, donnees=donnees, image_alt='Mickaël Teixeira, développeur Symfony et Sylius freelance à Bordeaux', modifie=modifie, priorite='1.0')
    textes_llm.append(('/', 'Accueil', en_texte(source)))


def pages_missions():
    for m in MISSIONS:
        chemin = f'/missions/{m["slug"]}/'
        source = fragment(f'missions/{m["slug"]}.html')
        liees = ''
        if m['expertises']:
            liens = ''.join(f'<li><a href="/expertises/{x["slug"]}/" style="{LIEN}">{e(x["nom"])}</a></li>' for x in m['expertises'])
            liees = (f'<nav aria-label="Expertises mobilisées" style="display: flex; flex-direction: column; gap: 10px; padding-top: 16px; border-top: 1px solid #e5e5e5; font-size: 15px">'
                     f'<p style="margin: 0; {MONO}; font-size: 12px; color: #5c5c5c">Expertises mobilisées</p>'
                     f'<ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-wrap: wrap; gap: 6px 18px">{liens}</ul></nav>')
        t = source.replace('<!--expertises-liees-->', liees).replace(f'<!--missions:{m["slug"]}-->', bande_missions(m['slug']))
        t = couvertures(t, '(min-width: 1312px) 1312px, 100vw', differe=False)
        assert '<!--missions' not in t and '<!--expertises' not in t, m['slug']
        modifie = date_modif(chemin, source + m['titre'] + m['description'])
        a_propos = {'@type': 'Organization', 'name': m['nom']}
        if m['client']:
            a_propos['url'] = m['client']
        donnees = graphe(
            {'@type': 'WebPage', '@id': url(chemin) + '#page', 'url': url(chemin), 'name': m['titre'], 'description': m['description'],
             'inLanguage': 'fr-FR', 'isPartOf': {'@id': SITE_WEB['@id']}, 'author': {'@id': PERSONNE['@id']}, 'about': a_propos,
             'primaryImageOfPage': url(f'/assets/img/missions/{m["slug"]}-couverture.webp'), 'dateModified': horodatage(modifie)},
            PERSONNE, SITE_WEB, fil(('Accueil', '/'), ('Missions', '/missions/'), (m['nom'], chemin)))
        page(chemin, m['titre'], m['description'], t, courant='Missions', image=f'/assets/img/partage/mission-{m["slug"]}.jpg',
             image_alt=f'{m["nom"]} × {NOM}', donnees=donnees, modifie=modifie, priorite='0.8')
        textes_llm.append((chemin, f'Mission : {m["nom"]} ({m["annees"]})', en_texte(source)))


def page_missions():
    hub = PAGES['missions_hub']
    cartes = ''.join(f'''<li><a href="/missions/{m["slug"]}/" style="display: flex; flex-direction: column; gap: 14px; color: #171717; text-decoration: none">
<span style="display: block; overflow: hidden; border-radius: 12px; aspect-ratio: 16 / 9; background: #171717"><img src="/assets/img/missions/{m["slug"]}-couverture-800.webp" srcset="/assets/img/missions/{m["slug"]}-couverture-480.webp 480w, /assets/img/missions/{m["slug"]}-couverture-800.webp 800w, /assets/img/missions/{m["slug"]}-couverture.webp 1600w" sizes="(min-width: 900px) 640px, 100vw" alt="" width="800" height="533" {'fetchpriority="high"' if i < 2 else 'loading="lazy" decoding="async"'} style="display: block; width: 100%; height: 100%; object-fit: cover"></span>
<span style="{MONO}; font-size: 12px; color: #5c5c5c">{m["annees"]} · {e(m["role"])}</span>
<h2 style="margin: 0; {TIGHT}; font-size: 30px; line-height: 1.1; letter-spacing: -0.02em">{e(m["nom"])}</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #3d3d3d">{e(m["resume"])}</p>
<span style="{MONO}; font-size: 12px; color: #5c5c5c">{e(m["pile"])}</span>
</a></li>''' for i, m in enumerate(MISSIONS))
    corps = f'''<div style="container-type: inline-size; background: #ffffff; color: #171717">
<main id="contenu">
{ouverture('titre-missions', [('Accueil', '/'), ('Missions', None)], hub['h1'], hub['h1_suite'], hub['chapo'])}
<section aria-label="Toutes les missions" style="padding-bottom: clamp(72px, 8cqw, 128px)">
<div style="{WRAP}">
<ol style="margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)); gap: 56px 32px">{cartes}</ol>
</div>
</section>
</main>
{bande_contact()}
</div>'''
    donnees = graphe(
        {'@type': 'CollectionPage', '@id': url('/missions/') + '#page', 'url': url('/missions/'), 'name': hub['titre_seo'],
         'description': hub['meta_description'], 'inLanguage': 'fr-FR', 'isPartOf': {'@id': SITE_WEB['@id']}, 'author': {'@id': PERSONNE['@id']},
         'mainEntity': {'@type': 'ItemList', 'itemListElement': [
             {'@type': 'ListItem', 'position': i + 1, 'name': m['titre'], 'url': url(f'/missions/{m["slug"]}/')} for i, m in enumerate(MISSIONS)]}},
        PERSONNE, SITE_WEB, fil(('Accueil', '/'), ('Missions', '/missions/')))
    page('/missions/', hub['titre_seo'], hub['meta_description'], corps, courant='Missions', image='/assets/img/partage/missions.jpg',
         image_alt='Les missions de Mickaël Teixeira', donnees=donnees,
         modifie=date_modif('/missions/', json.dumps(hub, ensure_ascii=False) + ''.join(m['resume'] + m['pile'] for m in MISSIONS)), priorite='0.8')


def page_expertise(x):
    chemin = f'/expertises/{x["slug"]}/'
    en_bref = ''.join(
        f'<div style="display: flex; flex-direction: column; gap: 4px; padding-top: 14px; border-top: 1px solid #171717">'
        f'<dt style="{MONO}; color: #5c5c5c; font-size: 12px">{e(b["terme"])}</dt><dd style="margin: 0">{e(b["valeur"])}</dd></div>' for b in x['en_bref'])
    cartes = ''.join(
        f'<div style="padding: 20px; background: #f5f5f5; border-radius: 12px; display: flex; flex-direction: column; gap: 6px">'
        f'<h3 style="margin: 0; font-weight: 600; color: #171717; font-size: 17px">{e(c["titre"])}</h3>'
        f'<p style="margin: 0; font-size: 16px; line-height: 1.6">{e(c["texte"])}</p></div>' for c in x['prestations']['cartes'])
    preuves = ''.join(
        f'<li style="border-top: 1px solid #e5e5e5"><a href="/missions/{p["slug"]}/" style="display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 6px 16px; padding-block: 20px; color: #171717; text-decoration: none">'
        f'<h3 style="margin: 0; font-weight: 600; font-size: 19px">{e(MISSION[p["slug"]]["nom"])}</h3><span style="{MONO}; font-size: 12px; color: #5c5c5c; padding-top: 4px">{MISSION[p["slug"]]["annees"]}</span>'
        f'<span style="grid-column: 1 / -1; font-size: 17px; line-height: 1.65; color: #3d3d3d">{e(p["accroche"])}</span>'
        f'<span style="grid-column: 1 / -1; color: #2f4bff; font-weight: 500; font-size: 15px">Lire la mission {e(MISSION[p["slug"]]["nom"])}</span></a></li>'
        for p in x['preuves']['missions'])
    approche = ''.join(f'<p style="margin: 0">{e(p)}</p>' for p in x['approche']['paragraphes'])
    autres = ''.join(f'<li><a href="/expertises/{o["slug"]}/" style="{LIEN}">{e(o["nom"])}</a></li>' for o in expertises if o['slug'] != x['slug'])
    lies = [ARTICLE[s] for s in ARTICLES_LIES.get(x['slug'], []) if s in ARTICLE]
    a_lire = (f'<nav aria-labelledby="titre-a-lire" style="display: flex; flex-direction: column; gap: 12px; padding-top: 20px; border-top: 1px solid #e5e5e5">'
              f'<h2 id="titre-a-lire" style="margin: 0; {MONO}; font-size: 12px; font-weight: 400; color: #5c5c5c">À lire</h2>'
              f'<ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px">'
              + ''.join(f'<li><a href="/actualites/{a["slug"]}/" style="{LIEN}">{e(sans_point(a["titre"]))}</a></li>' for a in lies)
              + '</ul></nav>') if lies else ''
    boutons = (f'<div style="display: flex; flex-wrap: wrap; gap: 12px; padding-top: 4px"><a href="/#contact" style="{BOUTON}; background: #2f4bff; color: #ffffff">Proposer une mission</a>'
               f'<a href="#preuves" style="{BOUTON}; border: 1px solid #b3b3b3; color: #171717">Voir les missions</a></div>')
    corps = f'''<div style="container-type: inline-size; background: #ffffff; color: #171717">
<main id="contenu">
{ouverture('titre-expertise', [('Accueil', '/'), ('Expertises', '/expertises/'), (x['nom'], None)], x['h1'], x['h1_suite'], x['chapo'], boutons)}
<section aria-label="En bref" style="padding-bottom: clamp(48px, 5cqw, 72px)">
<dl style="{WRAP}; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)); gap: 20px 32px; font-size: 16px">{en_bref}</dl>
</section>
<div style="{WRAP}; padding-bottom: clamp(72px, 8cqw, 128px); display: flex; flex-wrap: wrap; gap: 48px clamp(48px, 7cqw, 112px); align-items: flex-start">
<div style="flex: 999 1 560px; min-width: 0; max-width: 700px; display: flex; flex-direction: column; gap: 64px; font-size: 18px; line-height: 1.7; color: #3d3d3d">
<section aria-labelledby="titre-prestations" style="display: flex; flex-direction: column; gap: 20px">
<h2 id="titre-prestations" style="{H2}">{e(x["prestations"]["titre"])}</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 12px">{cartes}</div>
</section>
<section id="preuves" aria-labelledby="titre-preuves" style="display: flex; flex-direction: column; gap: 20px">
<h2 id="titre-preuves" style="{H2}">{e(x["preuves"]["titre"])}</h2>
<ol style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; border-bottom: 1px solid #e5e5e5">{preuves}</ol>
</section>
<section aria-labelledby="titre-approche" style="display: flex; flex-direction: column; gap: 16px">
<h2 id="titre-approche" style="{H2}">{e(x["approche"]["titre"])}</h2>
{approche}
</section>
<section aria-labelledby="titre-faq" style="display: flex; flex-direction: column; gap: 20px">
<h2 id="titre-faq" style="{H2}">Questions fréquentes.</h2>
{liste_faq(x["faq"])}
</section>
</div>
<aside aria-label="Pour aller plus loin" style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 28px; font-size: 15px">
<div style="padding: 24px; border: 1px solid #e5e5e5; border-radius: 12px; display: flex; flex-direction: column; gap: 14px">
<p style="margin: 0; color: #171717; font-size: 16px; line-height: 1.6">Toujours ouvert à une mission ou à un échange, à distance ou sur site.</p>
<a href="/#contact" style="align-self: start; display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border: 1px solid #b3b3b3; border-radius: 8px; color: #171717; text-decoration: none; font-weight: 500">Me contacter</a>
</div>
<nav aria-labelledby="titre-autres" style="display: flex; flex-direction: column; gap: 12px">
<h2 id="titre-autres" style="margin: 0; {MONO}; font-size: 12px; font-weight: 400; color: #5c5c5c">Autres expertises</h2>
<ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px">{autres}</ul>
</nav>
{a_lire}
</aside>
</div>
</main>
{bande_contact()}
</div>'''
    signature = json.dumps(x, ensure_ascii=False, sort_keys=True)
    modifie = date_modif(chemin, signature)
    donnees = graphe(
        {'@type': 'WebPage', '@id': url(chemin) + '#page', 'url': url(chemin), 'name': x['titre_seo'], 'description': x['meta_description'],
         'inLanguage': 'fr-FR', 'isPartOf': {'@id': SITE_WEB['@id']}, 'author': {'@id': PERSONNE['@id']},
         'mainEntity': {'@id': url(chemin) + '#service'}, 'dateModified': horodatage(modifie)},
        service(x), questions(x['faq']), ACTIVITE, PERSONNE, SITE_WEB,
        fil(('Accueil', '/'), ('Expertises', '/expertises/'), (x['nom'], chemin)))
    page(chemin, x['titre_seo'], x['meta_description'], corps, courant='Expertises', image=f'/assets/img/partage/expertise-{x["slug"]}.jpg',
         image_alt=sans_point(x['h1']), donnees=donnees, modifie=modifie, priorite='0.9')
    texte = [x['chapo'], 'En bref : ' + ' ; '.join(f'{b["terme"]} : {b["valeur"]}' for b in x['en_bref']),
             f'### {x["prestations"]["titre"]}', '\n'.join(f'- {c["titre"]} : {c["texte"]}' for c in x['prestations']['cartes']),
             f'### {x["preuves"]["titre"]}', '\n'.join(f'- {MISSION[p["slug"]]["nom"]} ({MISSION[p["slug"]]["annees"]}) : {p["accroche"]}' for p in x['preuves']['missions']),
             f'### {x["approche"]["titre"]}', '\n\n'.join(x['approche']['paragraphes']),
             '### Questions fréquentes', '\n\n'.join(f'**{q["question"]}** {q["reponse"]}' for q in x['faq'])]
    textes_llm.append((chemin, f'{x["h1"]} {x["h1_suite"]}', '\n\n'.join(texte)))


def page_expertises():
    hub = PAGES['expertises_hub']
    faq = PAGES['faq_generale']
    cartes = ''.join(f'''<li><a href="/expertises/{x["slug"]}/" style="height: 100%; display: flex; flex-direction: column; gap: 12px; padding-top: 20px; border-top: 2px solid #171717; color: #171717; text-decoration: none">
<h2 style="margin: 0; {TIGHT}; font-size: 30px; line-height: 1.1; letter-spacing: -0.02em">{e(x["nom"])}</h2>
<p style="margin: 0; font-size: 16px; line-height: 1.6; color: #3d3d3d">{e(x["resume"])}</p>
<span style="margin-top: auto; padding-top: 6px; color: #2f4bff; font-weight: 500; font-size: 15px">{e(sans_point(x["h1"]))}</span>
</a></li>''' for x in expertises)
    corps = f'''<div style="container-type: inline-size; background: #ffffff; color: #171717">
<main id="contenu">
{ouverture('titre-expertises', [('Accueil', '/'), ('Expertises', None)], hub['h1'], hub['h1_suite'], hub['chapo'])}
<section aria-label="Toutes les expertises" style="padding-bottom: clamp(72px, 8cqw, 112px)">
<div style="{WRAP}">
<ul style="margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 48px 32px">{cartes}</ul>
</div>
</section>
<section aria-labelledby="titre-faq" style="padding-bottom: clamp(72px, 8cqw, 128px)">
<div style="{WRAP}; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 400px), 1fr)); gap: 32px clamp(48px, 7cqw, 112px); align-items: start">
<h2 id="titre-faq" style="margin: 0; position: sticky; top: 96px; {TIGHT}; font-size: clamp(34px, 3.6cqw, 52px); line-height: 1.08; letter-spacing: -0.02em">Avant de m’écrire. <span style="color: #8a8a8a">Les questions qui reviennent.</span></h2>
<div style="font-size: 18px; line-height: 1.7; color: #3d3d3d">{liste_faq(faq)}</div>
</div>
</section>
</main>
{bande_contact()}
</div>'''
    donnees = graphe(
        {'@type': 'CollectionPage', '@id': url('/expertises/') + '#page', 'url': url('/expertises/'), 'name': hub['titre_seo'],
         'description': hub['meta_description'], 'inLanguage': 'fr-FR', 'isPartOf': {'@id': SITE_WEB['@id']}, 'author': {'@id': PERSONNE['@id']},
         'mainEntity': {'@type': 'ItemList', 'itemListElement': [
             {'@type': 'ListItem', 'position': i + 1, 'name': sans_point(x['h1']), 'url': url(f'/expertises/{x["slug"]}/')} for i, x in enumerate(expertises)]}},
        questions(faq), ACTIVITE, PERSONNE, SITE_WEB, fil(('Accueil', '/'), ('Expertises', '/expertises/')))
    page('/expertises/', hub['titre_seo'], hub['meta_description'], corps, courant='Expertises', image='/assets/img/partage/expertises.jpg',
         image_alt='Les expertises de Mickaël Teixeira', donnees=donnees,
         modifie=date_modif('/expertises/', json.dumps([hub, faq, [x['resume'] for x in expertises]], ensure_ascii=False)), priorite='0.9')
    textes_llm.append(('/expertises/', 'Questions fréquentes', '\n\n'.join(f'**{q["question"]}** {q["reponse"]}' for q in faq)))


def page_parcours():
    p = PAGES['parcours']
    sections = ''.join(
        f'<section style="display: flex; flex-direction: column; gap: 16px"><h2 style="{H2}">{e(s["titre"])}</h2>'
        + ''.join(f'<p style="margin: 0">{e(par)}</p>' for par in s['paragraphes']) + '</section>' for s in p['sections'])
    etapes = ''
    for i, (periode, role, lieux) in enumerate(ETAPES):
        liens = ', '.join(f'<a href="{h}" style="color: #5c5c5c">{e(n)}</a>' if h else e(n) for n, h in lieux)
        etapes += (f'<li style="display: grid; grid-template-columns: 150px minmax(0, 1fr); gap: 4px 24px; padding-block: 18px; border-top: 1px solid #e5e5e5">'
                   f'<span style="{MONO}; font-size: 13px; color: #5c5c5c; padding-top: 3px">{periode}</span>'
                   f'<span><b style="font-weight: 600; color: #171717">{e(role)}</b><br><span style="color: #5c5c5c">{liens}</span></span></li>')
    faits = [('Métier', 'Développeur Symfony, Sylius et API Platform, freelance'), ('Depuis', 'PHP depuis 2009, freelance depuis 2025'),
             ('Base', 'Bordeaux'), ('Intervention', 'À distance, ou sur site à Bordeaux, Paris, Lyon, Lille, Nantes'),
             ('Formation', 'Master Architecte logiciel, ETNA'), ('Statut', 'Entrepreneur individuel')]
    en_bref = ''.join(f'<div style="display: flex; flex-direction: column; gap: 2px; padding-block: 12px; border-top: 1px solid #e5e5e5"><dt style="{MONO}; color: #5c5c5c; font-size: 12px">{t}</dt><dd style="margin: 0; color: #171717">{e(v)}</dd></div>' for t, v in faits)
    profils = ''.join(f'<li><a href="{h}" rel="me noopener" style="{LIEN}">{n}</a></li>' for n, h in [('LinkedIn', LINKEDIN), ('Malt', MALT), ('GitHub', GITHUB)])
    corps = f'''<div style="container-type: inline-size; background: #ffffff; color: #171717">
<main id="contenu">
{ouverture('titre-parcours', [('Accueil', '/'), ('Parcours', None)], p['h1'], p['h1_suite'], p['chapo'])}
<div style="{WRAP}; padding-bottom: clamp(72px, 8cqw, 128px); display: flex; flex-wrap: wrap; gap: 48px clamp(48px, 7cqw, 112px); align-items: flex-start">
<div style="flex: 999 1 560px; min-width: 0; max-width: 700px; display: flex; flex-direction: column; gap: 64px; font-size: 18px; line-height: 1.7; color: #3d3d3d">
{sections}
<section aria-labelledby="titre-etapes" style="display: flex; flex-direction: column; gap: 20px">
<h2 id="titre-etapes" style="{H2}">Les étapes.</h2>
<ol style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; font-size: 16px; border-bottom: 1px solid #e5e5e5">{etapes}</ol>
</section>
<figure style="margin: 0; display: flex; flex-direction: column; gap: 20px">
<blockquote style="margin: 0; padding-left: 24px; border-left: 2px solid #2f4bff; {TIGHT}; font-size: clamp(24px, 2.4cqw, 30px); line-height: 1.28; letter-spacing: -0.02em; color: #171717"><p style="margin: 0">« Clairement l’une des meilleures personnes avec lesquelles j’ai travaillé. Sérieux, fiable, intelligent et humain, vous pouvez foncer les yeux fermés avec Mickaël si vous avez un projet. Vous pouvez être sûr qu’il répondra à toutes vos attentes ! »</p></blockquote>
<figcaption style="display: flex; flex-direction: column; gap: 2px; font-size: 15px"><span style="font-weight: 600; color: #171717">Mathieu Dumez</span><span style="color: #5c5c5c">Développeur web senior freelance, dans la même équipe</span><span style="{MONO}; font-size: 12px; color: #5c5c5c">Recommandation LinkedIn · 09.2026</span></figcaption>
</figure>
</div>
<aside aria-label="En bref" style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 28px; font-size: 15px">
<img src="/assets/img/mickael-teixeira-developpeur-symfony-bordeaux.webp" alt="Mickaël Teixeira, de face, en chemise grise" width="720" height="900" fetchpriority="high" style="display: block; width: 100%; max-width: 360px; height: auto; border-radius: 12px; background: #e9e9e9">
<dl style="margin: 0; display: flex; flex-direction: column; border-bottom: 1px solid #e5e5e5">{en_bref}</dl>
<nav aria-labelledby="titre-profils" style="display: flex; flex-direction: column; gap: 12px">
<h2 id="titre-profils" style="margin: 0; {MONO}; font-size: 12px; font-weight: 400; color: #5c5c5c">Profils</h2>
<ul style="margin: 0; padding: 0; list-style: none; display: flex; flex-wrap: wrap; gap: 8px 20px">{profils}</ul>
</nav>
</aside>
</div>
</main>
{bande_contact()}
</div>'''
    signature = json.dumps(p, ensure_ascii=False, sort_keys=True)
    modifie = date_modif('/parcours/', signature)
    donnees = graphe(
        {'@type': 'AboutPage', '@id': url('/parcours/') + '#page', 'url': url('/parcours/'), 'name': p['titre_seo'], 'description': p['meta_description'],
         'inLanguage': 'fr-FR', 'isPartOf': {'@id': SITE_WEB['@id']}, 'mainEntity': {'@id': PERSONNE['@id']}, 'dateModified': horodatage(modifie)},
        PERSONNE, SITE_WEB, fil(('Accueil', '/'), ('Parcours', '/parcours/')))
    page('/parcours/', p['titre_seo'], p['meta_description'], corps, courant='Parcours', image='/assets/img/partage/parcours.jpg',
         image_alt='Mickaël Teixeira, développeur Symfony et Sylius freelance à Bordeaux', type_og='profile', donnees=donnees, modifie=modifie,
         tete='<meta property="profile:first_name" content="Mickaël">\n<meta property="profile:last_name" content="Teixeira">\n', priorite='0.7')
    texte = [p['chapo']] + [f'### {s["titre"]}\n\n' + '\n\n'.join(s['paragraphes']) for s in p['sections']]
    texte.append('### Les étapes\n\n' + '\n'.join(f'- {periode} : {role}, {", ".join(n for n, _ in lieux)}' for periode, role, lieux in ETAPES))
    textes_llm.append(('/parcours/', f'{p["h1"]} {p["h1_suite"]}', '\n\n'.join(texte)))


def pages_simples():
    source = fragment('mentions-legales.html')
    page('/mentions-legales/', 'Mentions légales', 'Mentions légales du site de Mickaël Teixeira, entrepreneur individuel : éditeur, hébergement, données personnelles et crédits.',
         source, donnees=graphe(
             {'@type': 'WebPage', '@id': url('/mentions-legales/') + '#page', 'url': url('/mentions-legales/'), 'name': 'Mentions légales',
              'isPartOf': {'@id': SITE_WEB['@id']}}, SITE_WEB, fil(('Accueil', '/'), ('Mentions légales', '/mentions-legales/'))),
         modifie=date_modif('/mentions-legales/', source), priorite='0.2')
    page('/merci/', 'Message envoyé', 'Votre message est bien parti.', fragment('merci.html'), indexable=False)
    page('/404.html', 'Page introuvable', 'Cette page n’existe pas, ou plus.', fragment('404.html'), indexable=False)


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


ROBOTS_IA = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'anthropic-ai',
             'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot-Extended', 'Bingbot', 'CCBot', 'Amazonbot',
             'meta-externalagent', 'MistralAI-User', 'DuckAssistBot', 'cohere-ai', 'YouBot']


def plan_du_site():
    lignes = ''.join(f'<url><loc>{loc}</loc><lastmod>{modifie}</lastmod><priority>{prio}</priority></url>\n'
                     for loc, modifie, prio in sorted(pages_sitemap, key=lambda p: (-float(p[2]), p[0])))
    ecrire('/sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{lignes}</urlset>\n')
    agents = ''.join(f'User-agent: {r}\n' for r in ROBOTS_IA)
    ecrire('/robots.txt', f'''# {SITE}
# Tous les robots sont les bienvenus, moteurs de recherche comme assistants d'IA.
# Résumé du site pour les modèles de langage : {SITE}/llms.txt

User-agent: *
Allow: /

{agents}Allow: /

Sitemap: {SITE}/sitemap.xml
''')
    ecrire(f'/{CLE_INDEXNOW}.txt', CLE_INDEXNOW + '\n')


def fichiers_llm():
    lien = lambda titre, chemin, texte: f'- [{titre}]({url(chemin)}) : {texte}'
    references = ', '.join('onepoint (Enedis, Gaz de Bordeaux, PSA, Bureau Veritas Pro, SMIP)' if m['slug'] == 'onepoint'
                           else 'Commande.com (avec l’agence Dn’D)' if m['slug'] == 'commande' else m['nom'] for m in MISSIONS)
    entete_llm = f'''# {NOM}

> {PAGES["resume_llm_fr"]}

{PAGES["resume_llm_en"]}

## Faits essentiels

- Métier : développeur Symfony, Sylius et API Platform, freelance ; aussi Laravel, architecture hexagonale et DDD, intégration ERP, CRM et SIRH
- Base : Bordeaux (France) ; intervention à distance, ou sur site à Bordeaux, Paris, Lyon, Lille, Nantes
- Expérience : développeur PHP depuis 2009, freelance depuis 2025
- Références : {references}
- Formation : Master Architecte logiciel, ETNA
- Produit : fondateur de Yedra, le CRM des écoles (https://yedra.app), depuis novembre 2024
- Disponibilité : toujours ouvert à une mission ou à un échange
- Contact : {SITE}/#contact · {LINKEDIN} · {MALT} · {GITHUB}
'''
    index = [entete_llm, '## Expertises\n', *[lien(sans_point(x['h1']), f'/expertises/{x["slug"]}/', x['resume']) for x in expertises],
             lien('Toutes les expertises et les questions fréquentes', '/expertises/', PAGES['expertises_hub']['meta_description']),
             '\n## Missions\n', *[lien(f'{m["nom"]} ({m["annees"]})', f'/missions/{m["slug"]}/', m['description']) for m in MISSIONS],
             '\n## Parcours\n', lien('Parcours', '/parcours/', PAGES['parcours']['meta_description']),
             '\n## Actualités\n', *[lien(sans_point(a['titre']), f'/actualites/{a["slug"]}/', f'{a["date_affichee"]}. {a["chapo"]}') for a in articles],
             '\n## Optional\n', lien('Tout le contenu du site en un seul fichier texte', '/llms-full.txt', 'expertises, missions, parcours et articles.'),
             lien('Flux Atom des actualités', '/actualites/flux.xml', 'les articles, du plus récent au plus ancien.'),
             lien('Mentions légales', '/mentions-legales/', 'éditeur, hébergement, données personnelles.')]
    ecrire('/llms.txt', '\n'.join(index) + '\n')
    ordre = {'/expertises/': 1, '/parcours/': 2, '/missions/': 3, '/actualites/': 4, '/': 5}
    rang = lambda chemin: next((v for k, v in ordre.items() if chemin.startswith(k) and k != '/'), ordre['/'])
    sections = [f'## {titre}\n\nPage : {url(chemin)}\n\n{texte}' for chemin, titre, texte in sorted(textes_llm, key=lambda t: rang(t[0]))]
    ecrire('/llms-full.txt', entete_llm + '\n' + '\n\n---\n\n'.join(sections) + '\n')


if __name__ == '__main__':
    page_accueil()
    for expertise in expertises:
        page_expertise(expertise)
    page_expertises()
    pages_missions()
    page_missions()
    page_parcours()
    for article in articles:
        page_article(article)
    page_actualites()
    flux()
    pages_simples()
    redirections()
    plan_du_site()
    fichiers_llm()
    FICHIER_DATES.write_text(json.dumps(dict(sorted(dates.items())), ensure_ascii=False, indent=1) + '\n')
    print(f'{len(pages_sitemap)} pages indexables, {len(articles)} articles, {len(expertises)} expertises')
