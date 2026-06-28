# fotn

**fotn** — webapp photo mobile-first (compatible desktop) : on prend une photo avec la **caméra
native du système** (ou on importe), puis on choisit un **look** inspiré des pellicules argentiques,
on l'affine et on exporte. Interface monochrome (noir/blanc/gris), typographie Geist. App
mono-fichier (`index.html`, sans dépendance, sans build).

## Logique
- **Caméra native** : le bouton appareil photo ouvre la caméra **du système** (`<input capture>`) —
  qualité maximale, format natif, orientation correcte, aucun viseur custom. La photo revient dans
  l'app et s'ouvre dans l'éditeur. Import depuis la galerie via le bouton image.
- **Bibliothèque de presets** (~22) inspirés de pellicules réelles : négatifs (Portra, Gold, Superia),
  diapos (Velvia, Provia, Kodachrome), ciné (CineStill 800T, Vision3), lomo/cross-process, vintage,
  N&B (Tri-X, HP5, Acros, Delta, Sépia, Sélénium). Chaque preset est un **look paramétrique** calibré.
- **Moteur de rendu pixel** (`renderRecipe` / `buildOps`) : balance des blancs, matrice
  colorimétrique, split-tone, contraste, courbes hautes/basses lumières, grain, vignettage. Le même
  moteur alimente les cartes de la galerie, les vignettes du bandeau, l'aperçu éditeur et l'export.
- **Galerie** : chaque carte applique le preset sur une même image de référence (`generic.jpg`).
  Filtres Favoris / Couleur / Noir & blanc ; affichage compact / grand / liste + « Charger plus ».
- **Éditeur (façon VSCO)** : aperçu plein cadre de votre photo, **bandeau de presets** dont chaque
  vignette montre le look appliqué à *votre* photo (tap pour changer de look, les réglages sont
  conservés), **recadrage** (bouton « Recadrer » → boîte ajustable + chips de ratio : Libre, Original,
  1:1, 4:5, 5:4, 3:2, 2:3, 16:9, 9:16, grille des tiers), **curseur d'intensité** du look, et
  **réglages universels** en onglets (Lumière :
  exposition, contraste, hautes lumières, ombres ; Couleur : saturation, température, teinte ;
  Rendu : intensité, grain, vignettage, estompé). Export → `fotn_<preset>_<horodatage>-<id>.jpg`.

## Fichiers
- `index.html` — toute l'app (presets embarqués). `generic.jpg` — image de référence des cartes.
- `icon.svg` + PNG, `manifest.webmanifest` — branding / PWA.

## Lancer en local
```bash
cd fuji-recipes && python3 -m http.server 8765   # puis http://localhost:8765/
```
La caméra exige un contexte sécurisé (**HTTPS** ou `localhost`).

## Déployer
Hébergement statique. Déployé sur GitHub Pages : https://gevaux-tristan.github.io/fotn/
