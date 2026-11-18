# Guide d'adaptation du README par catégorie

> Problème que ce fichier résout : fournir, pour les différents types de projets (bibliothèques, applications, outils en ligne de commande, frameworks, collections de ressources), des recommandations différenciées sur le choix des sections du README, les priorités visuelles et la configuration des badges, et expliquer comment chaque type d'élément améliore l'esthétique et l'attrait.

Le gabarit universel s'applique à tous les projets, mais les lecteurs de types de projets différents ne portent pas le même intérêt. Le présent document fournit, au-delà de la spécification générale, des recommandations d'ajustement selon le type. Le lecteur doit partir du [Gabarit standard de README](./readme-standard-template.md) et l'adapter au type correspondant selon le présent document.

## 1. Vue d'ensemble des types

| Type | Question prioritaire du lecteur | Centre de gravité de la page d'accueil | Sections indispensables | Sections pouvant être omises |
| --- | --- | --- | --- | --- |
| Bibliothèque / SDK | Mode d'installation et usage de l'API | Version et licence | Installation, démarrage rapide, API, compatibilité | Déploiement, captures d'écran |
| Application | Apparence de l'application et fonctions clés | Captures d'écran et fonctionnalités | Fonctionnalités, captures d'écran, installation, démarrage rapide | Référence de l'API |
| Outil en ligne de commande | Usage des commandes et performances | Exemples de commandes et démonstration | Installation, usage, correspondance des commandes, démonstration | Architecture, configuration (si réduite) |
| Framework | Écosystème et coût d'apprentissage | Point d'entrée de la documentation et exemples | Positionnement, démarrage rapide, documentation, communauté | Détails de performance (lien externe possible) |
| Collection de ressources | Ce qui est recensé, comment rechercher | Classement du catalogue et navigation | Catalogue, catégories, guide de contribution | Installation, API |

## 2. Bibliothèque / SDK

Représentants typiques : clients HTTP tels que axios, bibliothèques de fonctions utilitaires, SDK clients.

### 2.1 Choix des sections

- Placer en tête « positionnement en une phrase + version + licence » pour que le lecteur puisse juger la compatibilité.
- Placer « Installation » en premier, avec la commande du gestionnaire de paquets (npm, pip, cargo, etc.).
- « Démarrage rapide » doit être un exemple complet et autonome.
- « Référence de l'API » est détaillée dans le README principal ou renvoie vers `docs/api.md` ; si les entrées d'API sont trop nombreuses, le README ne contient qu'un résumé et un lien.
- « Compatibilité » précise les versions de langage, les environnements d'exécution et les plateformes pris en charge.

### 2.2 Priorités visuelles

- Badges prioritaires : version, état de compilation, licence, nombre de téléchargements, taille du paquet.
- Usage sobre des images, généralement sans capture d'écran ; un petit logo peut suffire à établir l'identification.
- Présenter les paramètres de l'API sous forme de tableau pour améliorer la lisibilité.

### 2.3 Points d'amélioration de l'esthétique

1. Placer les badges de version et de licence en haut pour établir immédiatement la crédibilité.
2. Placer le bloc de code de démarrage rapide à proximité du premier écran pour abaisser le seuil d'essai.
3. Unifier la largeur des colonnes et la colonne des valeurs par défaut dans les tableaux d'API pour réduire la charge cognitive.

## 3. Application

Représentants typiques : éditeurs, outils de bureau, produits destinés à l'utilisateur final.

### 3.1 Choix des sections

- Le premier écran doit contenir une capture d'écran ou une image d'exécution du produit : montrer la valeur avant de parler de mise en œuvre.
- Organiser les « Fonctionnalités clés » selon les scénarios utilisateur, et non selon les modules techniques.
- « Installation » couvre les paquets d'installation ou les points de téléchargement de chaque plateforme.
- « Démarrage rapide » donne le parcours d'initiation le plus court.
- Les explications de compilation depuis les sources peuvent renvoyer à `CONTRIBUTING.md`.

### 3.2 Priorités visuelles

- Badges prioritaires : version, état de compilation, licence, nombre de téléchargements.
- La capture d'écran placée après le positionnement est l'élément central de la page d'accueil.
- Associer la liste des fonctionnalités à des icônes ou à de courtes captures pour améliorer l'efficacité du balayage visuel.

### 3.3 Points d'amélioration de l'esthétique

1. Présenter au centre des captures d'écran de haute qualité, adaptatives aux thèmes clair et sombre.
2. Formuler les points fonctionnels en phrases courtes avec icônes, en évitant les longues descriptions.
3. Rendre les points de téléchargement bien visibles, sous forme de liens-boutons.

## 4. Outil en ligne de commande

Représentants typiques : outils de terminal tels que fd et ripgrep.

### 4.1 Choix des sections

- Faire suivre le « positionnement en une phrase » d'une navigation entre sections pour faciliter le saut.
- « Installation » liste les principaux gestionnaires de paquets et les binaires par plateforme.
- « Usage » est orienté vers les tâches, avec des exemples de commandes courantes.
- La « correspondance des commandes » ou la « comparaison avec des outils similaires » répond à un besoin fréquent.
- « Demo » montre le résultat réel au moyen d'un GIF ou d'un enregistrement de terminal.
- Les données de performance doivent préciser l'environnement et la méthode de test.

### 4.2 Priorités visuelles

- Badges prioritaires : version, état de compilation, plateformes prises en charge, licence.
- L'image animée de démonstration est l'atout visuel central : elle montre la vitesse et l'expérience d'utilisation.
- Les commandes utilisent des blocs de code annotés de leur langage, les sorties des blocs `text`.

### 4.3 Points d'amélioration de l'esthétique

1. Placer les exemples de commandes en haut pour que le lecteur puisse les copier sans défiler.
2. L'image animée de démonstration montre le rendu réel du terminal et renforce l'impression de « rapidité ».
3. Placer les liens multilingues (par exemple versions chinoise et coréenne) à proximité de la ligne de badges.

## 5. Framework

Représentants typiques : frameworks full-stack tels que next.js.

### 5.1 Choix des sections

- Le premier écran met en avant le positionnement, la taille de l'écosystème et le point d'entrée d'apprentissage.
- Le point d'entrée « Documentation » doit être bien visible et pointer généralement vers un site de documentation dédié.
- « Communauté » précise les espaces de discussion, les canaux de messagerie instantanée et le code de conduite.
- « Démarrage rapide » donne la commande minimale de création de projet.
- Les contenus approfondis (architecture, API) renvoient vers des liens externes et ne sont pas développés dans le README.

### 5.2 Priorités visuelles

- Badges prioritaires : version, état de compilation, licence, canaux communautaires.
- Combiner le logo de marque avec des badges de style `for-the-badge` pour renforcer la page d'accueil.
- Des captures de type Showcase peuvent illustrer les cas d'usage de l'écosystème.

### 5.3 Points d'amélioration de l'esthétique

1. Logo centré et grands badges de style unifié forment un premier écran identitaire.
2. Présenter les points d'entrée de la documentation et de la communauté sous forme de blocs de navigation bien visibles.
3. Des points d'entrée pour débutants tels que Good First Issues abaissent le seuil de contribution.

## 6. Collection de ressources

Représentants typiques : listes de la série awesome.

### 6.1 Choix des sections

- Il est courant d'ouvrir le premier écran sur le logo et les informations de parrainage.
- Le corps du document organise le catalogue par thème et fournit une navigation claire.
- Le « Guide de contribution » précise les critères d'inclusion et le format de soumission.
- Les sections installation, API et déploiement sont inutiles.

### 6.2 Priorités visuelles

- Le nombre de badges peut être plus élevé, mais le style doit rester unifié.
- Le catalogue utilise des titres de niveau 2 et des listes, chaque entrée étant accompagnée d'une brève description.
- Les logos des sponsors sont disposés en tableau ou en grille, en conservant l'alignement.

### 6.3 Points d'amélioration de l'esthétique

1. Une structure de catalogue claire, avec des titres de catégories de niveau cohérent.
2. Chaque entrée est accompagnée d'une phrase de description, sans se limiter à un lien.
3. Les zones de parrainage et de remerciements sont alignées et ordonnées, sans gêner la lecture du corps du document.

## 7. Principes généraux inter-types

1. **Le lecteur d'abord** : le premier écran répond aux questions les plus importantes du lecteur ; les différences de type n'affectent que l'ordre, pas l'intégralité de l'information.
2. **Style unifié** : les badges, les titres et le style des blocs de code d'un même projet doivent être cohérents.
3. **Exemple copiable** : tout type de projet fournit au moins un exemple directement exécutable.
4. **Renvoi par lien** : les contenus approfondis dépassant le rôle de la page d'accueil renvoient vers une documentation dédiée.
5. **Synchronisation continue** : les captures d'écran, les badges de version et les listes de fonctionnalités doivent être mis à jour avec les versions, afin d'éviter que des informations obsolètes nuisent à la crédibilité.

## Fichiers associés

- Liste générale des sections : voir la [Spécification des sections de README](./readme-sections-specification.md)
- Spécification des éléments visuels : voir la [Spécification de mise en page visuelle du README](./readme-visual-layout-specification.md)
- Configuration des badges : voir la [Spécification des badges](./badge-specification.md)
- Gabarit universel : voir le [Gabarit standard de README](./readme-standard-template.md)
- Constat sur la répartition des types : voir le [Rapport d'étude sur les gabarits de README](./readme-template-research-report.md)
