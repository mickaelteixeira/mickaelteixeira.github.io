# mickaelteixeira.github.io

Le site de Mickaël Teixeira, développeur Symfony et Sylius freelance à Bordeaux : https://mickaelteixeira.github.io

Le site est statique et servi par GitHub Pages. Les pages HTML de la racine sont générées : on ne les modifie pas à la main.

## Générer le site

```sh
python3 _build/build.py      # pages, sitemap.xml, robots.txt, llms.txt, flux Atom, redirections
python3 _build/verifier.py   # liens, balises de référencement, données structurées
python3 _build/partage.py    # images de partage 1200 × 630 (Pillow et Chrome requis)
python3 _build/logo.py       # favicon, icônes et logo carré (Pillow requis)
```

Python 3.12 ou plus récent suffit pour `build.py` et `verifier.py`.

## Où modifier quoi

| Contenu | Fichier |
| --- | --- |
| Accueil | `_build/contenu/accueil.html` |
| Une mission | `_build/contenu/missions/<mission>.html`, et son titre, sa description et son résumé dans `MISSIONS` de `_build/build.py` |
| Une expertise, la page Parcours, les questions fréquentes, le résumé pour les IA | `_build/donnees/pages.json` |
| Un article | `_build/donnees/articles.json` (blocs `p`, `h2`, `liste`, `citation`, `code`, `chiffre`, `encart`, `capture`) |
| Une capture d’article | `_build/donnees/captures.json` et `assets/img/actualites/captures/` |
| Mentions légales, 404, merci | `_build/contenu/*.html` |
| Styles | `_build/styles/site.css`, intégrée dans chaque page à la génération |
| Logo, favicon, icônes | `_build/logo.py` ; son animation est dans `_build/styles/site.css` |
| Script commun | `assets/js/site.js` |

Le dossier `_build` n’est pas publié : `_config.yml` l’exclut, et GitHub Pages ignore les dossiers qui commencent par un tiret bas.

## Logo

Le signe est un carré de la trame de lignes de la façade : six rangées de tirets, traversées par la diagonale de lumière
qui balaie la façade. Il est défini une seule fois, dans `_build/logo.py` ; `build.py` le pose dans l’en-tête et le pied de page,
`partage.py` dans les images de partage. Dans l’en-tête, il se trace de haut en bas au chargement, puis la lumière passe ;
elle repasse au survol. `python3 _build/logo.py` régénère `favicon.svg`, `favicon.ico`, les icônes du manifeste,
l’icône d’écran d’accueil et `assets/img/logo-mickael-teixeira.png`, le carré de 720 px déclaré dans les données structurées.

## Thèmes clair et sombre

Le thème suit le système du visiteur, ou son choix (bouton dans l’en-tête, mémorisé dans le navigateur).
Les couleurs sont des variables dans `_build/styles/site.css`. Les couleurs neutres écrites dans les fragments
(`#ffffff`, `#171717`, `#2f4bff`…) sont converties en variables par `build.py` ; une zone entourée de
`<!--fixe-->` et `<!--/fixe-->` garde ses couleurs, comme les pièces aux couleurs des clients. Une image
propre à un thème porte `data-theme-img="clair"` ou `data-theme-img="sombre"`.

## Référencement

- Chaque page a son titre, sa description, son URL canonique, ses balises Open Graph et ses données structurées
  (Person, ProfessionalService, Service, FAQPage, ProfilePage, AboutPage, CollectionPage, Blog, BlogPosting, BreadcrumbList).
- `sitemap.xml` porte de vraies dates de modification : `_build/donnees/dates.json` garde l’empreinte de chaque page
  et la date de son dernier changement. Ce fichier se met à jour tout seul à la génération ; il se commite avec le reste.
- `robots.txt` ouvre le site à tous les robots, moteurs de recherche et assistants d’IA compris.
- `llms.txt` résume le site pour les modèles de langage ; `llms-full.txt` en donne tout le contenu en texte.
- IndexNow : après chaque mise en ligne, l’action « Signaler les pages modifiées aux moteurs » envoie à Bing, Yandex,
  Seznam et Naver les pages changées par le dernier commit (`_build/indexnow.py`). La clé est le fichier `.txt` de 32 caractères à la racine.
- Les anciennes adresses `project-*.html` redirigent vers les missions.
- L’action « Vérifier le site généré » refuse une PR dont les pages publiées ne correspondent pas aux sources, ou dont un lien est cassé.
