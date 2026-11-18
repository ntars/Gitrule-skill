# Rapport d'étude sur les gabarits de README

> Problème que ce fichier résout : consigner la méthode d'étude, la taille de l'échantillon et les constats quantifiés ayant servi à établir le gabarit standard de README, fournir une base de données au [Gabarit standard de README](./readme-standard-template.md) et aux différentes spécifications thématiques, et expliciter les limites et la portée de la méthode.

## 1. Objectifs et méthode de l'étude

### 1.1 Objectifs

Étudier les projets open source de premier plan les plus étoilés, dégager les régularités de structure, d'organisation des sections, de présentation visuelle et d'usage des badges de leurs README et documents associés, afin de constituer une spécification générale et un gabarit réutilisables.

### 1.2 Sources de données

- Métadonnées des dépôts : API GitHub GraphQL Search, tri par star décroissante, filtre `is:public archived:false fork:false`.
- Texte des README : API GitHub REST Contents (`readme` endpoint), récupéré en base64 ou en raw puis analysé.
- Paramètres des badges : documentation officielle Shields.io (pages Static Badge et Logos) et description du format badge-maker.
- Pratiques de la communauté chinoise : documentation projet, messages de commit et chapitres de promotion de phodal/github (*Guide de découverte de GitHub*, 11 362 étoiles), pour compléter les principes de rédaction et l'expérience opérationnelle que les statistiques automatisées ne couvrent pas.

### 1.3 Méthode de collecte

1. **Métadonnées** : une requête de l'API GitHub Search renvoie au maximum 1 000 résultats. Pour élargir l'échantillon, un découpage par tranches de star a été appliqué — localisation par dichotomie du seuil de star correspondant à chaque millier de rangs, puis descente progressive sur 11 lots cumulés, pour finalement obtenir les métadonnées de 10 995 dépôts de premier plan.
2. **Échantillonnage des README** : au sein des 1 000 premiers dépôts, échantillonnage stratifié par langage principal, couvrant Python, TypeScript, JavaScript, Rust, Go, C++ et d'autres langages majeurs ; 120 dépôts échantillonnés, dont tous les README ont été récupérés avec succès.
3. **Base statistique** : les taux d'apparition des sections et les taux d'utilisation des éléments sont calculés par dépôt ; les styles de badges et les paramètres de logo sont comptés selon le nombre d'occurrences dans les URL.

### 1.4 Limites de la méthode (à expliciter)

- L'API GitHub Search impose une limite de 1 000 résultats par requête ; ce rapport étend l'échelle par cumul de lots, mais les frontières des lots sont affectées par les ex æquo sur le nombre d'étoiles : l'échantillon est un ensemble approximatif de tête, non un classement strictement continu.
- La taille de l'échantillon de README est de 120 ; les conclusions reflètent des tendances et des traits communs, sans prétendre à une distribution statistiquement significative de l'ensemble des projets de premier plan.
- L'identification des sections repose sur la correspondance de mots-clés dans les titres, ce qui introduit un biais statistique dû aux variations de formulation.
- Les statistiques des paramètres de badges portent sur les paramètres explicitement présents dans l'URL ; les paramètres par défaut des badges dynamiques ne sont pas comptés.

## 2. Répartition des dépôts de premier plan (métadonnées)

### 2.1 Taille de l'échantillon

- Une requête unique permet d'obtenir de façon stable les 1 000 premiers dépôts, dans une plage de star d'environ 563 574 à 30 857.
- Après cumul de 11 lots, l'échelle atteint 10 995 dépôts de premier plan, avec une borne inférieure de star de 5 452.

### 2.2 Répartition par langage (sur les 1 000 premiers)

| Langage | Nombre | Part |
| --- | --- | --- |
| Python | 223 | 22,3 % |
| TypeScript | 178 | 17,8 % |
| JavaScript | 112 | 11,2 % |
| Rust | 80 | 8,0 % |
| Sans langage principal | 74 | 7,4 % |
| Go | 68 | 6,8 % |
| C++ | 55 | 5,5 % |
| Java | 27 | 2,7 % |

Les projets de tête sont dominés par Python, TypeScript et JavaScript, qui totalisent ensemble plus de 50 % ; les langages système comme Rust et Go occupent une part notable. Cela impose au gabarit de couvrir les commandes d'installation de gestionnaires de paquets de plusieurs langages et les badges multi-environnements d'exécution.

### 2.3 Répartition par licence (sur les 1 000 premiers)

| Licence | Nombre | Part |
| --- | --- | --- |
| MIT | 399 | 39,9 % |
| Apache-2.0 | 197 | 19,7 % |
| Non identifiée (NOASSERTION) | 148 | 14,8 % |
| Aucune licence (NONE) | 65 | 6,5 % |
| GPL-3.0 | 51 | 5,1 % |
| AGPL-3.0 | 50 | 5,0 % |
| BSD-3-Clause | 17 | 1,7 % |

MIT domine et constitue la recommandation par défaut du gabarit universel ; il convient toutefois de conserver des espaces réservés pour les identifiants SPDX d'options telles que Apache-2.0 et GPL.

## 3. Constats sur la structure des README (N=120)

### 3.1 Taux d'apparition des sections

| Mot-clé de section | Dépôts concernés | Taux d'apparition |
| --- | --- | --- |
| Contribution / Contributing | 66 | 55,0 % |
| Licence / License | 52 | 43,3 % |
| Installation / Install | 49 | 40,8 % |
| Démarrage rapide / Quick Start | 28 | 23,3 % |
| Documentation / Documentation | 25 | 20,8 % |
| Développement / Development | 22 | 18,3 % |
| Configuration / Configuration | 19 | 15,8 % |
| Fonctionnalités / Features | 19 | 15,8 % |
| Sécurité / Security | 15 | 12,5 % |
| Usage / Usage | 12 | 10,0 % |
| Prérequis / Requirements | 11 | 9,2 % |
| API | 10 | 8,3 % |
| Exemples / Examples | 10 | 8,3 % |

Constat : le guide de contribution et la licence sont des éléments standards des projets de premier plan, ce qui reflète la priorité accordée à la gouvernance communautaire et à la conformité ; l'installation et le démarrage rapide suivent immédiatement. Le gabarit les classe donc comme obligatoires.

### 3.2 Taux d'utilisation des éléments visuels

| Élément | Dépôts concernés | Taux d'apparition | Médiane (par dépôt) |
| --- | --- | --- | --- |
| Blocs de code | 80 | 66,7 % | 2 |
| Images | 76 | 63,3 % | 2 |
| Badges (Shields.io) | 61 | 50,8 % | 1 |
| Tableaux | 44 | 36,7 % | 0 |

Médiane de la hiérarchie des titres : 7 titres de niveau 2 ; médiane de la longueur des fichiers : 171 lignes. Cela montre que les README de premier plan restent généralement d'une longueur modérée et s'organisent autour de 6 à 12 titres de niveau 2.

### 3.3 Adaptation aux thèmes (40 premiers échantillons)

| Caractéristique | Dépôts concernés |
| --- | --- |
| Conteneur centré (`align="center"`) | 27 |
| Élément `<picture>` | 12 |
| Bascule thème clair/sombre (`prefers-color-scheme`) | 12 |
| `for-the-badge` avec `labelColor` | 2 |

Le conteneur centré est la technique dominante pour la page d'accueil ; environ un tiers des projets fournissent des images en deux versions, claire et sombre.

## 4. Constats sur les badges

### 4.1 Paramètres de style (par nombre d'occurrences dans les URL, N=120)

| style | Occurrences |
| --- | --- |
| `for-the-badge` | 65 |
| `flat-square` | 60 |
| `flat` | 32 |
| `social` | 12 |
| `plastic` | 1 |

`for-the-badge` et `flat-square` sont les plus répandus ; `plastic` est désormais pratiquement abandonné. Voir la [Spécification des badges](./badge-specification.md).

### 4.2 Paramètres de logo (par nombre d'occurrences, N=120)

| logo slug | Occurrences |
| --- | --- |
| `github` | 35 |
| `discord` | 20 |
| `npm` | 4 |
| `apple` / `docker` / `linkedin` / `x` | 2–3 chacun |

GitHub et Discord sont les icônes les plus fréquentes, correspondant aux deux catégories d'information « dépôt du code source » et « canaux communautaires ».

## 5. Constat sur le premier écran de projets de référence

| Projet | Type | Caractéristiques de la page d'accueil |
| --- | --- | --- |
| `sindresorhus/awesome` | Collection de ressources | Logo centré, zone de parrainage, catalogue classé par thème |
| `axios/axios` | Bibliothèque | Avertissement important, tableau de parrainage, multilingue |
| `sharkdp/fd` | CLI | Badges + liens multilingues, navigation entre sections, image animée de démonstration |
| `BurntSushi/ripgrep` | CLI | Badges, liens rapides, capture des résultats de recherche, comparaison de performance |
| `vercel/next.js` | Framework | Logo centré, badges `for-the-badge`, points d'entrée documentation et communauté |
| `microsoft/vscode` | Application | Badges, explication du dépôt, capture d'écran du produit, points d'entrée contribution et retours |
| `rust-lang/rust` | Langage | Bannière centrée, ligne de navigation, points de valeur Why Rust |
| `phodal/github` | Livre électronique chinois | Les quatre questions de la page d'accueil, exemples de textes en une phrase, principe de simplification de l'installation, liste des canaux de promotion |

Traits communs : le premier écran répond à « ce que c'est, comment l'utiliser, où trouver les détails » ; les badges sont accolés au titre ; la capture d'écran ou la démonstration suit immédiatement le positionnement ; les points d'entrée contribution et communauté sont placés plus bas mais restent indispensables.

## 6. Conclusions

1. Le gabarit universel doit avoir pour colonne vertébrale « positionnement → installation → démarrage rapide → documentation → contribution → licence ».
2. Par défaut, les badges utilisent `flat-square` ou `for-the-badge`, de façon unifiée dans tout le document, au nombre de 4 à 6.
3. Les images et les blocs de code sont au cœur d'une page d'accueil attractive ; ils doivent être accompagnés d'un texte `alt` et d'une indication de langage.
4. Le type de projet détermine le choix des sections, voir le [Guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md).
5. La conformité et la gouvernance communautaire (licence, guide de contribution) sont un consensus des projets de premier plan et sont classées comme obligatoires.

## 7. Précisions sur l'échelle des données

Résultat cumulé du découpage des métadonnées des dépôts de premier plan : 10 995 dépôts, plage de star de 563 575 à 5 452. La répartition des licences et des langages de cet échantillon de l'ordre de dix mille est la suivante, en cohérence avec les conclusions de l'échantillon des 1 000 premiers :

| Dimension | Répartition |
| --- | --- |
| Langage | Python 1 995, TypeScript 1 529, JavaScript 1 279, sans langage principal 888, Go 847, C++ 531, Java 528, Rust 507 |
| Licence | MIT 4 160 (37,8 %), Apache-2.0 2 073 (18,9 %), non identifiée 1 463, aucune licence 1 106, GPL-3.0 747 |

L'échantillon de statistique approfondie des README compte 120 dépôts, tous récupérés avec succès. Le découpage utilise des seuils de star approximatifs ; l'échelle est un ensemble approximatif de tête, non un classement strictement continu.

## Fichiers associés

- Gabarit directement applicable : voir le [Gabarit standard de README](./readme-standard-template.md)
- Spécification des badges : voir la [Spécification des badges](./badge-specification.md)
- Règles visuelles : voir la [Spécification de mise en page visuelle du README](./readme-visual-layout-specification.md)
- Adaptation par catégorie : voir le [Guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md)
- Définition des sections : voir la [Spécification des sections de README](./readme-sections-specification.md)
