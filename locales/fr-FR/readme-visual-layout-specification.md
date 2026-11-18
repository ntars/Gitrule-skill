# Spécification de mise en page visuelle du README

> Problème que ce fichier résout : définir les niveaux de mise en page du README, l'organisation des paragraphes, les cas d'usage et l'emplacement des tableaux, des captures d'écran et des GIF, afin que la documentation atteigne un équilibre entre densité d'information et attrait visuel.

Les données « mesurées » du présent document proviennent d'une étude par échantillonnage des README de projets open source de premier plan menée par ce projet (échantillon N=120) ; les pratiques de référence sont issues de la constatation de la structure de premier écran de plusieurs projets très étoilés.

## 1. Niveaux de mise en page

### 1.1 Hiérarchie des titres

Le README doit établir une hiérarchie de titres claire, selon les contraintes suivantes :

1. Le document ne conserve qu'un seul titre de niveau 1 (`#`), à savoir le nom du projet, placé à la première ligne du fichier.
2. Les titres de niveau 2 (`##`) sont les sections principales ; leur nombre devrait se situer entre 6 et 12 ; la médiane mesurée est de 7.
3. Les titres de niveau 3 (`###`) servent aux subdivisions internes et ne sont utilisés que lorsque le contenu d'un titre de niveau 2 est long.
4. Aucun saut de niveau de titre n'est autorisé (par exemple passer de `#` directement à `###`).
5. Le libellé des titres est concis, sous forme de nom ou de groupe nominal, sans point final.

### 1.2 Ordre de la structure du premier écran

Le premier écran désigne le contenu visible sans défilement ; il est organisé dans l'ordre suivant :

1. Logo ou bannière du projet centré (facultatif) ;
2. Titre de niveau 1 (nom du projet) ;
3. Ligne de badges (voir la [Spécification des badges](./badge-specification.md)) ;
4. Positionnement en une phrase (ce qu'est le projet, à qui il s'adresse, quel problème il résout) ;
5. Ligne de liens de navigation entre sections (facultatif, pour les README longs) ;
6. Résumé des fonctionnalités ou caractéristiques clés.

Constat de référence : `fd` et `ripgrep` font suivre le positionnement d'une navigation entre sections ; `next.js` et `rust-lang/rust` ouvrent sur un logo centré et une bannière ; `vscode` insère une capture d'écran du produit immédiatement après le positionnement.

### 1.3 Paragraphes et espacement

- Limiter chaque paragraphe à 1–4 lignes pour éviter les blocs de texte dense.
- Laisser une ligne vide entre les paragraphes afin de préserver une respiration visuelle après rendu.
- Placer les conclusions clés en premier, les explications ensuite.
- Conserver une espace entre les caractères chinois et les caractères anglais ou les chiffres ; utiliser la ponctuation propre à chaque contexte linguistique.

## 2. Règles d'utilisation des tableaux

### 2.1 Cas d'usage

Les tableaux conviennent aux informations multidimensionnelles et comparables. 36,7 % des échantillons mesurés utilisent des tableaux ; c'est la forme recommandée pour la description de la configuration, la matrice de compatibilité et la correspondance des commandes. Les cas d'usage comprennent :

- la description des éléments de configuration (clé, type, valeur par défaut, rôle) ;
- la matrice de compatibilité des plateformes et des versions ;
- la correspondance des commandes ou des paramètres ;
- la comparaison des fonctionnalités (ce projet et d'autres solutions) ;
- la feuille de route et les états.

### 2.2 Emplacement

Le tableau suit immédiatement le titre de niveau 2 dont il dépend, précédé d'une phrase d'introduction précisant son objet ; si des exceptions existent après le tableau, les compléter dans un paragraphe distinct.

### 2.3 Exigences de rédaction

| Exigence | Description |
| --- | --- |
| Maîtrise du nombre de colonnes | 3–6 colonnes ; envisager une séparation au-delà de 6 |
| En-têtes explicites | Donner un en-tête nominal court à chaque colonne, éviter les en-têtes vides |
| Alignement cohérent | Unifier le mode d'alignement des tableaux dans tout le document |
| Contenu concis | Ne pas rédiger de longs paragraphes dans les cellules ; développer si nécessaire par une note de bas de page ou un lien |
| Aucune cellule vide | Indiquer « aucun » ou « non applicable » en l'absence de contenu |

## 3. Règles d'utilisation des blocs de code

### 3.1 Cas d'usage

Les blocs de code servent aux commandes, à la configuration, aux appels d'API et aux sorties d'exemple. 66,7 % des échantillons mesurés contiennent des blocs de code ; ils sont un élément indispensable de la section « Démarrage rapide », avec une médiane de 2.

### 3.2 Exigences de rédaction

1. Chaque bloc de code doit indiquer son langage, par exemple `bash`, `json`, `python`, `javascript`, pour faciliter la coloration syntaxique.
2. Les exemples de commandes doivent fournir la commande complète et exécutable, sans omettre les étapes préalables.
3. Lorsqu'un résultat doit être montré, créer un bloc de code distinct annoté `text` et expliquer la sortie attendue dans le texte.
4. Laisser une ligne vide avant et après chaque bloc de code.
5. Limiter le contenu d'un bloc à 20 lignes ; scinder les exemples trop longs ou les déplacer dans le répertoire `examples/` avec un lien.
6. Si le symbole d'invite `$` est utilisé pour les commandes interactives, il doit l'être de façon uniforme dans tout le document.

Exemple de format :

```bash
npm install <package-name>
```

```text
✓ Installation complete
```

## 4. Règles d'utilisation des captures d'écran et des GIF

### 4.1 Cas d'usage et arbitrages

| Élément | Cas d'usage | Points d'attention |
| --- | --- | --- |
| Capture d'écran statique | Interface applicative, résultat d'exécution, graphiques | Taux d'utilisation mesuré de 63,3 %, le plus employé |
| GIF / image animée | Démonstration en ligne de commande, parcours interactif, comparaison avant/après | Volume de fichier important, compression obligatoire, durée maîtrisée |
| Logo / bannière | Identification de marque, page d'accueil de premier écran | Fournir deux versions, claire et sombre |
| Schéma explicatif | Architecture, processus, flux de données | Doit être mis à jour en phase avec la version de la documentation |

63,3 % des échantillons mesurés contiennent des images. Constat de référence : `fd` utilise `doc/screencast.svg` comme démonstration, `ripgrep` utilise une capture des résultats de recherche, `vscode` utilise une capture de l'exécution du produit, `rust` et `next.js` utilisent une bannière de logo adaptative aux thèmes clair et sombre.

### 4.2 Emplacement

1. Logo / bannière : en tout haut du fichier, centré.
2. Capture d'écran du produit : après le positionnement en une phrase et avant le « Démarrage rapide », pour établir une perception immédiate.
3. Démonstration GIF : dans une section distincte « Demo / Démonstration », immédiatement après les « Fonctionnalités clés ».
4. Schéma d'architecture : dans la section « Architecture » ou « Conception », ou déplacé dans `docs/architecture.md` avec un lien depuis le README.

### 4.3 Exigences de rédaction

- Chaque image doit fournir un texte `alt` décrivant le contenu de l'image ; les textes dépourvus de sens tels que `image` ou `capture d'écran` sont interdits.
- Référencer les images par chemin relatif vers les ressources du dépôt, ou par URL absolue stable ; éviter les liens temporaires soumis à expiration.
- Pour les images devant s'adapter au thème, utiliser le HTML `<picture>` avec `prefers-color-scheme` pour fournir les deux versions, claire et sombre.
- Maîtriser le volume des images : privilégier le WebP ou le PNG optimisé pour les captures, convertir de préférence les GIF en vidéos courtes ou en images animées compressées.
- Adapter la largeur des images : utiliser l'attribut `width` ou un conteneur externe pour limiter la largeur et éviter de déborder la page.

## 5. Liens et navigation

### 5.1 Navigation entre sections

Lorsque le README dépasse 200 lignes, ajouter au premier écran une ligne de liens de navigation vers les sections principales :

```markdown
[Installation](#installation) · [Démarrage rapide](#démarrage-rapide) · [Documentation](#documentation) · [Contribution](#contribution)
```

### 5.2 Priorité aux liens relatifs

Les documents, images et licences internes au dépôt doivent tous utiliser des chemins relatifs, afin de rester utilisables après un fork et en lecture hors ligne. Les liens externes doivent pointer vers des sources faisant autorité (documentation officielle, page du gestionnaire de paquets, page de CI).

## 6. Liste de mise en œuvre de l'esthétique et de l'attrait

1. Le premier écran comporte un logo ou un titre explicite et transmet le positionnement du projet en 3 secondes.
2. Les badges ont un style unifié, une couleur sémantique et un nombre modéré.
3. Le titre de niveau 1 est unique, les titres de niveau 2 sont au nombre de 6 à 12, sans saut de niveau.
4. Au moins un exemple de code copiable et exécutable.
5. Au moins une capture d'écran ou une démonstration illustrant la valeur du produit.
6. Les tableaux servent aux informations comparatives, avec un nombre de colonnes maîtrisé et des en-têtes clairs.
7. Toutes les images disposent d'un texte `alt`, tous les blocs de code d'une indication de langage.
8. Les documents longs disposent d'une navigation entre sections.
9. Les images et les badges restent lisibles en thème clair comme en thème sombre.

## Fichiers associés

- Style et couleurs des badges : voir la [Spécification des badges](./badge-specification.md)
- Liste complète des sections : voir la [Spécification des sections de README](./readme-sections-specification.md)
- Priorités visuelles selon le type de projet : voir le [Guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md)
- Squelette de mise en page directement applicable : voir le [Gabarit standard de README](./readme-standard-template.md)
- Échantillons mesurés et méthode : voir le [Rapport d'étude sur les gabarits de README](./readme-template-research-report.md)
