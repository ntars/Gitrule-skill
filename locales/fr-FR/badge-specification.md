# Spécification des badges

> Problème que ce fichier résout : définir la syntaxe d'URL, les paramètres de style, les codages de couleur, la sélection des informations, l'ordre d'affichage et la maîtrise du nombre des badges du README, avec Shields.io comme implémentation principale, et fournir des exemples de format directement copiables ainsi que des configurations de paramètres recommandées.

Les paramètres décrits dans le présent document sont tous vérifiés au regard de la documentation officielle Shields.io (pages Static Badge et Logos, description du format badge-maker) ; les taux d'apparition proviennent de l'étude par échantillonnage des README de projets open source de premier plan menée par ce projet et sont signalés comme « mesurés ».

## 1. Syntaxe de base

### 1.1 Structure d'URL d'un badge statique

Un badge statique transmet ses paramètres par le chemin de l'URL, selon la structure standard suivante :

```text
https://img.shields.io/badge/<étiquette>-<message>-<couleur>?style=<style>&<autres paramètres de requête>
```

Les trois segments du chemin sont séparés par le trait d'union `-` :

| Segment | Nom | Obligatoire | Description |
| --- | --- | --- | --- |
| Segment 1 | Étiquette (label) | Non | Texte de gauche, indiquant le nom de l'indicateur |
| Segment 2 | Message (message) | Oui | Texte de droite, affichant la valeur de l'indicateur |
| Segment 3 | Couleur (color) | Oui | Couleur de fond de droite |

La forme à deux segments (étiquette omise, message et couleur seuls) est également valide :

```text
https://img.shields.io/badge/<message>-<couleur>
```

### 1.2 Règles d'échappement des caractères

Dans le chemin de l'URL, les espaces et les caractères spéciaux doivent être échappés, selon les règles suivantes :

| Caractère saisi | Écriture URL | Exemple |
| --- | --- | --- |
| Espace | `_` ou `%20` | `v0.1 prototype` → `v0.1%20prototype` |
| Souligné `_` | `__` (double souligné) | `my_label` → `my__label` |
| Trait d'union `-` | `--` (double trait d'union) | `dev-build` → `dev--build` |

L'exemple de prototype fourni par l'utilisateur est conforme à cette syntaxe et peut être utilisé directement :

```markdown
![Status](https://img.shields.io/badge/status-v0.1%20prototype-8957e5?style=flat-square)
```

Sa signification : étiquette `status`, message `v0.1 prototype` (espace remplacé par `%20`), couleur `8957e5` (violet hexadécimal), style `flat-square`.

### 1.3 Format d'intégration Markdown

```markdown
![Version](https://img.shields.io/badge/version-1.2.0-blue?style=flat-square)
```

Lorsqu'un clic doit mener à une page, entourer l'image d'un lien :

```markdown
[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
```

## 2. Paramètre de style (style)

`style` détermine la conception visuelle globale du badge, avec cinq valeurs possibles ; la valeur par défaut est `flat`.

| Valeur | Caractéristiques visuelles | Cas d'usage | Occurrences mesurées (N=120) |
| --- | --- | --- | --- |
| `flat` | Angles droits, plat, style par défaut de Shields.io | Premier choix générique, compatible avec la plupart des thèmes | 32 |
| `flat-square` | Angles droits, sans arrondi, légèrement plus compact | Page d'accueil recherchant l'ordre et la rigueur | 60 |
| `for-the-badge` | Grand, gras, fort contraste | Visuel principal en haut de page, badges d'accentuation | 65 |
| `social` | Arrondi, bicolore gauche-droite, plat | Page d'accueil de style réseaux sociaux | 12 |
| `plastic` | Dégradé brillant, effet skeuomorphique | Style rétro, désormais peu utilisé | 1 |

**Configuration recommandée** :

- Tous les badges d'un même README doivent utiliser un `style` unifié ; le mélange est interdit. C'est la première exigence de cohérence visuelle.
- Les projets génériques privilégient `flat` ou `flat-square` ; lorsqu'une page d'accueil de marque doit être renforcée, utiliser uniformément `for-the-badge`.
- Dans les mesures, `for-the-badge` (65 occurrences) et `flat-square` (60 occurrences) sont les plus répandus ; l'un comme l'autre peut servir de choix par défaut.

Exemple de format :

```markdown
![build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
![build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
```

## 3. Paramètres de couleur (color / labelColor)

### 3.1 Trois notations de couleur

Selon la description de badge-maker, `color` (à droite) et `labelColor` (fond de gauche) prennent tous deux en charge les trois notations suivantes :

**Méthode 1 : couleurs nommées Shields.io**

| Sémantique | Couleurs nommées |
| --- | --- |
| Succès | `brightgreen`, `green`, `success` |
| Avertissement | `yellow`, `yellowgreen`, `orange`, `important` |
| Alerte | `red`, `critical` |
| Information | `blue`, `informational` |
| Neutre | `grey` / `gray`, `lightgrey` / `lightgray`, `inactive` |

Attention : la valeur par défaut de `labelColor` est `grey`, celle de `color` est `lightgrey` (la documentation précise par ailleurs qu'`inactive` est aussi l'une des couleurs par défaut) ; certaines couleurs nommées diffèrent légèrement des couleurs CSS homonymes, le rendu Shields.io faisant foi.

**Méthode 2 : couleur hexadécimale**

Prend en charge trois ou six chiffres hexadécimaux, avec ou sans préfixe `#` :

```text
?color=8957e5
?color=007fff
?color=%23007fff    ← si # est conservé, l'encoder en %23
```

**Méthode 3 : valeur de couleur CSS**

Prend en charge `rgb(...)`, `rgba(...)`, `hsl(...)`, `hsla(...)` ainsi que les couleurs nommées CSS (telles que `aqua`, `fuchsia`, `lightslategray`) ; leur usage exige un encodage URL.

### 3.2 Correspondance sémantique des couleurs (configuration recommandée)

| Type d'information | Couleur recommandée | Exemple de message |
| --- | --- | --- |
| Compilation réussie, tests réussis | `brightgreen` / `success` | `passing` |
| Échec de compilation | `red` / `critical` | `failing` |
| Version stable | `blue` | `v1.2.0` |
| Pré-version, prototype | Violet personnalisé `8957e5` / `orange` | `v0.1 prototype` |
| Licence | `blue` / `green` | `MIT` |
| État de la documentation | `yellowgreen` | `docs` |
| Obsolète, maintenance arrêtée | `red` / `inactive` | `deprecated` |

**Configuration recommandée** : fixer pour chaque projet un jeu unique de couleurs de marque et de couleurs d'état, sans changement arbitraire ; la même sémantique utilise le même codage de couleur dans tout le dépôt.

Exemple de format :

```markdown
![Couverture](https://img.shields.io/badge/coverage-95%25-orange?style=flat-square)
![État](https://img.shields.io/badge/status-v0.1%20prototype-8957e5?style=flat-square)
![Licence](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
```

## 4. Paramètres d'icône (logo / logoColor / logoSize)

### 4.1 Utilisation de Simple Icons

Le paramètre `logo` prend le slug d'icône de Simple Icons, sous la forme `?logo=<slug>`. Slugs courants :

| Usage | slug | Occurrences mesurées (N=120) |
| --- | --- | --- |
| Dépôt GitHub | `github` | 35 |
| Communauté Discord | `discord` | 20 |
| Paquet npm | `npm` | 4 |
| Plateformes Apple | `apple` | 3 |
| Docker | `docker` | 3 |
| Plateforme sociale X | `x` | 3 |
| Paquet Python | `pypi` | 2 |

Le slug complet fait foi sur le site Simple Icons ou dans `slugs.md` du dépôt simple-icons.

### 4.2 Couleur et taille des icônes

- `logoColor` : définit la couleur de l'icône Simple Icons ; prend en charge l'hexadécimal, rgb, hsl et les couleurs nommées CSS ; ne s'applique qu'aux icônes Simple Icons, sans effet sur les icônes personnalisées.
- `logoSize` : réglé sur `auto`, l'icône est mise à l'échelle selon le contenu, ce qui convient aux icônes larges ; ne s'applique également qu'aux Simple Icons.

Exemple de format :

```markdown
![repo](https://img.shields.io/badge/github-repo-blue?logo=github)
![couleur du logo](https://img.shields.io/badge/logo-javascript-blue?logo=javascript&logoColor=f5f5f5)
```

Les icônes personnalisées peuvent être transmises via `logo=data:image/svg+xml;base64,...`, mais l'URL devient extrêmement longue et difficile à maintenir ; à déconseiller sauf besoin particulier.

## 5. Autres paramètres de requête

| Paramètre | Rôle | Exemple |
| --- | --- | --- |
| `label` | Remplace le texte par défaut de gauche (les espaces doivent être encodés) | `?label=healthiness` |
| `labelColor` | Couleur de fond de gauche | `?labelColor=abcdef` |
| `color` | Couleur de fond de droite | `?color=fedcba` |
| `cacheSeconds` | Durée du cache HTTP (secondes) ; une valeur inférieure à la valeur par défaut est ignorée | `?cacheSeconds=3600` |
| `link` | Définit l'adresse de clic des moitiés gauche et droite | Ne fonctionne que dans une balise `<object>`, sans effet sur une image Markdown |

## 6. Badges dynamiques

Les badges dynamiques récupèrent des données en temps réel auprès de services externes via Shields.io, sans mise à jour manuelle des valeurs. Types courants :

| Catégorie | Modèle d'URL | Usage |
| --- | --- | --- |
| État de compilation | `https://img.shields.io/github/actions/workflow/status/<owner>/<repo>/<workflow>` | État de la CI |
| Version | `https://img.shields.io/npm/v/<package>` | Dernière version npm |
| Licence | `https://img.shields.io/npm/l/<package>` | Licence du paquet |
| Nombre d'étoiles | `https://img.shields.io/github/stars/<owner>/<repo>` | Popularité |
| Nombre d'issues | `https://img.shields.io/github/issues/<owner>/<repo>` | Problèmes en attente |
| Nombre de téléchargements | `https://img.shields.io/npm/dt/<package>` | Téléchargements cumulés |

Les badges dynamiques acceptent l'ajout de paramètres tels que `?style=` et `?logo=`, selon les mêmes règles que les badges statiques. Les projets de référence adoptent généralement la combinaison « badges dynamiques pour les indicateurs réels + badges statiques pour les états personnalisés ».

## 7. Sélection des informations et ordre d'affichage

### 7.1 Sélection des informations

Les badges doivent transmettre des informations d'état « vérifiables et utiles au lecteur ». Il est recommandé de ne conserver que les catégories suivantes :

1. état de compilation / de test ;
2. version ou dernière publication ;
3. licence ;
4. état de la documentation ;
5. canaux communautaires (Discord, espaces de discussion) ;
6. état personnalisé du projet (prototype, en maintenance, obsolète).

Ne doivent pas figurer : des nombres de téléchargements sans source, des étiquettes marketing sans rapport avec le projet, des notes non vérifiables, des blocs de couleur purement décoratifs.

### 7.2 Ordre d'affichage

Il est recommandé d'ordonner selon « état → version → licence → plateforme/communauté → état personnalisé », l'importance décroissant de gauche à droite. Raison : l'état de compilation détermine l'adoption par le lecteur, la version détermine le jugement de compatibilité, la licence détermine la possibilité d'utilisation ; les deux dernières sont des informations préalables à la décision.

### 7.3 Maîtrise du nombre

- Projet courant : 4–6 badges.
- Collection de ressources ou projet d'écosystème : peut être étendu à 8–10 badges.
- Tous les badges sont placés après le nom du projet et le positionnement en une phrase, avant le corps du texte, sur une ligne dédiée ou dans un conteneur centré, sans dispersion dans le corps du document.

### 7.4 Badge statique d'état de livraison

L'implémentation standard du point 6 de la section 7.1, « état personnalisé du projet », est le badge statique d'état de livraison, dont la valeur est mise à jour manuellement par l'auteur du projet ; il convient à l'avancement de livraison et à l'état de maintenance dépourvus de source de données externe :

```text
![Status](https://img.shields.io/badge/status-4%20of%204%20delivered-brightgreen?style=flat-square)
```

1. La structure standard est `badge/<étiquette>-<message>-<couleur>`, le style étant uniformément `?style=flat-square` ; l'exemple signifie « les 4 livrables sont tous livrés ».
2. Dans le texte du message, l'espace s'écrit `%20`, le tiret `--`, le souligné `__` ; aucun saut de ligne ni autre caractère spécial non échappé n'est autorisé.
3. Convention sémantique des couleurs : `brightgreen` indique un achèvement, `yellow` un travail en cours, `red` un blocage, `lightgrey` un état non commencé.
4. Lorsque les valeurs changent, le badge et le corps du texte doivent être mis à jour simultanément ; le badge ne doit pas rester durablement en retard sur l'état réel ; si la synchronisation ne peut être garantie, passer à un badge dynamique.
5. Le texte `alt` doit exprimer la signification réelle, par exemple `![交付状态]` ; il peut pointer vers la liste des livrables ou la section d'index correspondante.

## 8. Accessibilité et adaptation aux thèmes

- Le texte `alt` de chaque badge doit exprimer sa signification réelle, par exemple `![构建状态]` et non `![badge]`.
- En thème sombre ou clair, il est possible de basculer la source de l'image du badge via `<picture>` ; l'usage de `for-the-badge` avec `labelColor=000` maintient un contraste stable dans les deux thèmes.
- Chaque badge doit pouvoir être cliqué vers la source de données correspondante (l'état de compilation vers la CI, la version vers la page du gestionnaire de paquets, la licence vers le fichier LICENSE).

## Fichiers associés

- Rattachement et ordre des sections : voir la [Spécification des sections de README](./readme-sections-specification.md)
- Niveaux visuels et emplacement : voir la [Spécification de mise en page visuelle du README](./readme-visual-layout-specification.md)
- Recommandations différenciées par type de projet : voir le [Guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md)
- Ligne de badges complète directement applicable : voir le [Gabarit standard de README](./readme-standard-template.md)
- Méthode d'étude et échantillons mesurés : voir le [Rapport d'étude sur les gabarits de README](./readme-template-research-report.md)
