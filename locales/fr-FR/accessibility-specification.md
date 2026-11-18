# Spécification d'accessibilité

> Problème que ce fichier résout : définir les exigences d'accessibilité de la documentation du projet, du README et des interfaces utilisateur, afin que le contenu reste utilisable pour les lecteurs recourant à un lecteur d'écran, à une navigation au clavier ou confrontés à diverses conditions visuelles.

## 1. Périmètre d'application

1. Accessibilité de la documentation : README, site de documentation, exemples de code, tableaux, images.
2. Accessibilité des interfaces : interfaces utilisateur des applications et des projets Web.
3. Accessibilité de la ligne de commande : textes d'aide, messages d'erreur et formats de sortie.

## 2. Accessibilité de la documentation

### 2.1 Images et médias

1. Chaque image doit fournir un texte `alt` décrivant le contenu visuel et sa fonction ; une image purement décorative utilise un `alt` vide.
2. L'usage de textes sans information comme « image », « capture d'écran » ou « image » pour le `alt` est interdit.
3. Les animations GIF doivent voir leur contenu explicité dans un texte voisin, afin d'éviter que l'information ne repose uniquement sur l'animation.
4. Les graphiques doivent être accompagnés d'une description textuelle ou d'un tableau de données ; les séries de données ne doivent pas être distinguées par la seule couleur.

### 2.2 Titres et structure

1. La hiérarchie des titres est continue, sans saut de niveau (voir la [spécification de mise en page visuelle du README](./readme-visual-layout-specification.md)).
2. Le document ne comporte qu'un seul titre de niveau un.
3. Les listes utilisent la syntaxe Markdown normalisée, afin que le lecteur d'écran les identifie comme listes.
4. Les tableaux doivent avoir une ligne d'en-tête ; l'usage de tableaux sans en-tête pour mettre en page le document est interdit.

### 2.3 Liens et texte

1. Le texte du lien doit décrire sa cible de façon autonome ; « cliquez ici » ou « plus » sont interdits.
2. La couleur ne doit pas être le seul moyen de transmettre une information ; elle doit être accompagnée de texte ou d'icône.
3. En cas de texte mixte chinois et étranger, conserver les espaces afin de garantir une césure et une lecture correctes.
4. À la première occurrence d'un sigle, indiquer sa forme complète.

### 2.4 Code et tableaux

1. Les blocs de code indiquent leur langage, afin de faciliter leur identification par les outils d'assistance (voir la [spécification de mise en page visuelle du README](./readme-visual-layout-specification.md)).
2. Le contenu des cellules de tableau est concis ; éviter les fusions de lignes qui rendent l'analyse difficile pour les lecteurs d'écran.
3. Les commandes longues sont présentées avec des retours à la ligne, sans dépendre d'un défilement horizontal.

## 3. Accessibilité des interfaces

### 3.1 Navigation au clavier

1. Tous les éléments interactifs doivent être atteignables et utilisables au clavier.
2. L'ordre de focus est cohérent avec l'ordre visuel, et l'état de focus est clairement visible.
3. Fournir un accès rapide pour contourner le contenu répété (par exemple, aller au contenu principal).

### 3.2 Sémantique et étiquettes

1. Utiliser des balises sémantiques pour exprimer la structure et les rôles ; éviter de simuler des contrôles avec des éléments non sémantiques.
2. Les contrôles de formulaire doivent avoir une étiquette associée, et le message d'erreur doit être lié au champ correspondant.
3. Les changements d'état dynamiques sont transmis aux technologies d'assistance via des annonces d'accessibilité.

### 3.3 Conditions visuelles

1. Le contraste entre le texte et le fond doit satisfaire aux exigences de lisibilité ; le contraste du texte courant ne doit pas être inférieur à 4,5:1, celui des grands textes à 3:1.
2. Prise en charge des thèmes clair et sombre du système ; le changement de thème ne doit pas modifier la structure de l'information (voir la [spécification de mise en page visuelle du README](./readme-visual-layout-specification.md)).
3. Les animations offrent une option de réduction, afin d'éviter les contenus à clignotement rapide lancés automatiquement.
4. Lorsque le texte est agrandi à 200 %, la mise en page reste utilisable, sans troncature de contenu.

## 4. Accessibilité de la ligne de commande

1. Les messages d'erreur expliquent la cause et l'action corrective possible ; l'affichage du seul code d'erreur est interdit.
2. La sortie de `--help` est clairement catégorisée et liste les paramètres obligatoires et les valeurs par défaut.
3. Prise en charge d'une variable d'environnement désactivant la sortie en couleur, pour faciliter l'usage des lecteurs d'écran et le traitement des journaux.
4. Les invites interactives proposent des paramètres équivalents non interactifs, pour les scénarios automatisés.

## 5. Liste de vérification

- [ ] Toutes les images ont un texte `alt` porteur d'information.
- [ ] La hiérarchie des titres est continue, avec un seul titre de niveau un dans le document.
- [ ] Le texte des liens est compréhensible de façon autonome.
- [ ] Les tableaux ont un en-tête et la couleur n'est pas le seul support de l'information.
- [ ] Les blocs de code indiquent leur langage.
- [ ] Les éléments d'interface sont utilisables au clavier et le focus est visible.
- [ ] Le contraste satisfait aux exigences minimales, et les thèmes clair comme sombre sont lisibles.
- [ ] Les textes d'aide et messages d'erreur guident l'action suivante.

## 6. Pratiques interdites

1. Transmettre une information clé par une image seule sans fournir d'alternative textuelle est interdit.
2. Indiquer un état ou une erreur par la seule couleur est interdit.
3. L'usage de textes de lien dénués de sens est interdit.
4. La suppression du style d'indication de focus sans fournir d'alternative est interdite.

## Fichiers associés

- Mise en page de la documentation : [spécification de mise en page visuelle du README](./readme-visual-layout-specification.md)
- Exigences d'accessibilité des badges : [spécification des badges](./badge-specification.md)
- Normes rédactionnelles : [spécification de rédaction générale](./general-writing-specification.md)
- La qualité de la documentation relève de la dimension D12 : [matrice des dimensions de revue](./review-dimension-matrix.md)
