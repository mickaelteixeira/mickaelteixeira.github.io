# mickaelteixeira.github.io

Le site de Mickaël Teixeira, développeur Symfony et Sylius freelance à Bordeaux : https://mickaelteixeira.github.io

Le site est statique et servi par GitHub Pages. Les pages HTML de la racine sont générées : on ne les modifie pas à la main.

## Générer le site

```sh
python3 _build/build.py      # pages, sitemap.xml, robots.txt, flux Atom, redirections
python3 _build/partage.py    # images de partage 1200 × 630 (Chrome requis)
```

Python 3 suffit pour `build.py` ; `partage.py` a besoin de Pillow et de Google Chrome.

## Où modifier quoi

| Contenu | Fichier |
| --- | --- |
| Accueil | `_build/contenu/accueil.html` |
| Une mission | `_build/contenu/missions/<mission>.html`, et ses titre et description dans `MISSIONS` de `_build/build.py` |
| Un article | `_build/donnees/articles.json` (blocs `p`, `h2`, `liste`, `citation`, `code`, `chiffre`, `encart`, `capture`) |
| Une capture d’article | `_build/donnees/captures.json` et `assets/img/actualites/captures/` |
| Mentions légales, 404, merci | `_build/contenu/*.html` |
| Styles et script communs | `assets/css/site.css`, `assets/js/site.js` |

Le dossier `_build` n’est pas publié : GitHub Pages ignore les dossiers qui commencent par un tiret bas.

## Référencement

Chaque page a son titre, sa description, son URL canonique, ses balises Open Graph et ses données structurées
(Person, ProfessionalService, ProfilePage, Blog, BlogPosting, BreadcrumbList). `sitemap.xml`, `robots.txt` et le flux
`actualites/flux.xml` sont régénérés à chaque build. Les anciennes adresses `project-*.html` redirigent vers les missions.
