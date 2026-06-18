# Film Recipes · Fuji

Webapp mobile-first (compatible desktop) reprenant **1058 recettes de simulation de film Fujifilm**
issues du Google Sheet source, transformées en **presets applicables + curseurs classiques** d'app photo.

## Fonctionnalités
- **Moteur de rendu pixel** (`renderRecipe`, traitement canvas pixel par pixel) qui réinterprète
  chaque recette : **balance des blancs réelle** (Kelvin + presets Shade/Fluorescent/Underwater… +
  shift Rouge/Bleu), **matrice colorimétrique propre à chaque simulation** (split-tone ambre/teal de
  Classic Negative, cyans éteints de Classic Chrome, matte cinématographique d'Eterna, N&B filtré
  d'Acros…), courbes hautes/basses lumières, Color Chrome, grain et vignettage. Le **même moteur**
  alimente les cartes, l'aperçu éditeur et l'export → cohérence totale.
- **Galerie de presets** : les 1058 recettes, chaque carte applique le rendu de la recette sur
  **une même image générique** (`generic.jpg`, libre de droit) → vue d'ensemble comparable d'un
  coup d'œil. Filtres : Couleur / N&B, simulation de base, favoris.
- **Éditeur** : aperçu live (image générique ou **votre propre photo**) recalculé en temps réel, et
  des **curseurs réglables** : Hautes lumières, Ombres, Couleur, Netteté, Clarté, Réduction du bruit,
  WB Rouge/Bleu, + segments Plage dynamique, Grain, Color Chrome Effect / Blue.
- **Export** : une fois votre photo ajoutée (« Ma photo »), un bouton **Exporter** (à côté de
  « Réinitialiser ») cuit le rendu courant dans l'image et la télécharge avec un **nom de fichier
  unique** (`fuji_<recette>_<base>_<horodatage>-<id>.jpg`).
- **Simulation de base** sélectionnable (Provia, Astia, Velvia, Classic Chrome/Negative, Eterna,
  Acros…), chacune avec son grading colorimétrique propre.
- **Favoris** (stockés localement), bouton **« Créer la vôtre »** pour partir d'une base vierge,
  lien vers la **source d'origine** de chaque recette.

> L'aperçu est une **approximation** du rendu (filtres CSS) pour donner le « feel » de la recette.
> Les valeurs exactes restent celles à reporter dans le boîtier Fuji — visibles dans
> « Recette d'origine ».

## Fichiers
- `index.html` — l'app complète (HTML + CSS + JS, sans dépendances).
- `recipes.json` — les 1058 recettes structurées (généré depuis le Google Sheet).
- `generic.jpg` — image générique libre de droit utilisée pour les aperçus des cartes.

## Lancer en local
Servir le dossier en HTTP (le `fetch` de `recipes.json` ne marche pas en `file://`) :
```bash
cd fuji-recipes
python3 -m http.server 8765
# puis ouvrir http://localhost:8765/
```

## Déployer
N'importe quel hébergement statique (Vercel, Netlify, GitHub Pages…). Déposer le dossier tel quel.

## Mettre à jour les données
Réexporter le Google Sheet en CSV puis relancer le parseur (`parse.py`, voir historique) pour
régénérer `recipes.json`.
