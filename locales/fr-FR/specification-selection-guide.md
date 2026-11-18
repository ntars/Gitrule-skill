# Guide de sélection des spécifications

> Problème que ce fichier résout : fournir les critères d'adaptation des spécifications selon le type de projet, la taille de l'équipe et la phase de publication, en proposant une combinaison minimale viable et une combinaison de conformité complète, afin que le « prélèvement à la demande » repose sur des critères de décision explicites et non sur un jugement personnel.

L'objet de l'adaptation ici est l'ensemble du corpus de spécifications ; les différences de type au niveau des sections du README sont traitées dans le [guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md), et la correspondance complète des phases dans la [table de correspondance du cycle de vie](./lifecycle-mapping-table.md).

## 1. Principes de sélection

1. **Les contraintes impératives ne sont pas adaptables** : les [règles absolues](./hard-rules.md) et les [pratiques interdites](./prohibited-practices.md) s'appliquent intégralement à tout projet et à toute phase.
2. **La porte de phase détermine le plancher** : avant d'entrer dans une phase, la porte de sortie indiquée pour cette phase dans la [table de correspondance du cycle de vie](./lifecycle-mapping-table.md) doit être franchie, et les spécifications centrales correspondantes ne peuvent être omises.
3. **Les différences de type n'affectent que la profondeur** : le type de projet détermine quelles spécifications sont renforcées et quels détails peuvent être simplifiés, mais ne constitue jamais une raison de contourner une porte qualité.
4. **Le déclassement doit être déclaré explicitement** : un dépôt de scripts temporaires privé peut n'exécuter que les portes P0, mais il doit signaler le « mode déclassé » dans les livrables et énumérer les éléments non exécutés.

## 2. Dimensions d'adaptation

| Dimension | Valeurs | Impact principal |
| --- | --- | --- |
| Type de projet | bibliothèque / SDK, application, outil en ligne de commande, framework, collection de ressources | Détermine les spécifications à renforcer et les détails simplifiables |
| Taille de l'équipe | individuel, petite équipe, organisation | Détermine la nécessité des spécifications de gouvernance et de collaboration |
| Phase de publication | validation de prototype, première publication publique, maintenance stable | Détermine le moment d'introduction des spécifications de conformité et d'exploitation |

Lorsque les trois dimensions se superposent, appliquer l'ordre de priorité « contraintes impératives → porte de phase → phase de publication → type de projet → taille de l'équipe » ; l'adaptation d'une dimension de priorité inférieure ne doit pas affaiblir les exigences d'une dimension de priorité supérieure.

## 3. Adaptation selon le type de projet

| Type de projet | À renforcer | Simplifiable | Livrables obligatoires |
| --- | --- | --- | --- |
| Bibliothèque / SDK | [spécification de conception d'API](./api-design-specification.md), [spécification de documentation d'API](./api-documentation-specification.md), [spécification de gestion des versions](./version-management-specification.md), [spécification du journal des modifications](./changelog-specification.md) | Déploiement et restauration, observabilité (uniquement lors de la distribution d'artefacts), spécifications visuelles de type captures d'écran | README, documentation d'API, LICENSE, CHANGELOG |
| Application | [spécification de mise en page visuelle du README](./readme-visual-layout-specification.md), [spécification d'accessibilité](./accessibility-specification.md), [spécification de déploiement et de restauration](./deployment-and-rollback-specification.md), [spécification d'observabilité](./observability-specification.md), [spécification de dépannage](./troubleshooting-specification.md) | Documentation d'API, conception de base de données (en cas d'usage d'un service hébergé) | README, captures d'écran, instructions de déploiement, SECURITY |
| Outil en ligne de commande | [spécification de message de commit](./commit-message-specification.md), [guide de rédaction des fonctionnalités et arbitrages d'ingénierie](./features-and-engineering-tradeoffs-guide.md), [guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md), [spécification d'accessibilité](./accessibility-specification.md) (sortie terminal) | Conception de base de données, déploiement et restauration (en cas de distribution principalement par paquet) | README, exemples d'utilisation, animation de démonstration, LICENSE |
| Framework | [matrice documentaire](./document-matrix.md), [spécification de documentation d'API](./api-documentation-specification.md), [spécification de guide de contribution](./contribution-guide-specification.md), [spécification de code de conduite](./code-of-conduct-specification.md), [spécification d'observabilité](./observability-specification.md) | Conception de base de données (sans stockage intégré) | README, point d'entrée documentaire, guide de contribution, code de conduite |
| Collection de ressources | [matrice documentaire](./document-matrix.md), [gabarit de guide de contribution](./contribution-guide-template.md), [spécification multilingue](./multilingual-specification.md), [spécification de rédaction générale](./general-writing-specification.md) | Tests, déploiement, API, base de données, observabilité | README, répertoire classé, guide de contribution, LICENSE |

Les projets de type collection de ressources ne contiennent généralement pas de code exécutable ; la [spécification de tests](./testing-specification.md) et la [spécification de workflow CI](./ci-workflow-specification.md) peuvent être marquées comme non applicables ; toutefois la [spécification de rédaction générale](./general-writing-specification.md) et la [spécification d'accessibilité](./accessibility-specification.md) restent obligatoires, afin de garantir l'utilisabilité du texte des liens et de la structure des listes.

## 4. Adaptation selon la taille de l'équipe

| Taille de l'équipe | Spécifications à ajouter | Spécifications omissibles |
| --- | --- | --- |
| Individuel | [règles absolues](./hard-rules.md), [spécification de nommage des projets](./project-naming-specification.md), [gabarit standard de README](./readme-standard-template.md), [spécification de LICENSE](./license-specification.md) | Code de conduite, propriété du code, rétrospective d'itération, indicateurs de mesure de la qualité (peuvent être complétés avant la première publication publique) |
| Petite équipe | En plus du niveau individuel : [spécification de propriété du code](./code-ownership-specification.md), [spécification de guide de contribution](./contribution-guide-specification.md), [spécification de workflow CI](./ci-workflow-specification.md), [porte qualité](./quality-gate.md) | Réponse aux incidents, observabilité (peuvent être complétées après la mise en service) |
| Organisation | Application intégrale ; il faut en outre mettre en œuvre la [spécification de NOTICE](./notice-specification.md), le [gabarit SECURITY](./security-template.md), la [clause de non-responsabilité](./disclaimer.md), la [spécification de réponse aux incidents](./incident-response-specification.md), la [spécification des indicateurs de mesure de la qualité](./quality-metrics-specification.md), la [spécification de matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md) | Aucune |

Lorsque la taille de l'équipe augmente, les spécifications de gouvernance doivent être complétées avant que le dépôt ne devienne visible à l'extérieur, et non ajoutées après la première publication.

## 5. Adaptation selon la phase de publication

| Phase de publication | À introduire | Reportable | Exigence de déclaration |
| --- | --- | --- | --- |
| Validation de prototype | [règles absolues](./hard-rules.md), [spécification de nommage des projets](./project-naming-specification.md), [gabarit standard de README](./readme-standard-template.md), [spécification de rédaction générale](./general-writing-specification.md) | Porte qualité, observabilité, réponse aux incidents, documents juridiques | Doit signaler le « mode déclassé » et énumérer les éléments reportés |
| Première publication publique | En plus du prototype : [porte qualité](./quality-gate.md), [spécification de conformité open source](./open-source-compliance-specification.md), [spécification de LICENSE](./license-specification.md), [gabarit de clause de non-responsabilité](./disclaimer-template.md), [gabarit de guide de contribution](./contribution-guide-template.md), [gabarit de code de conduite](./code-of-conduct-template.md), [gabarit SECURITY](./security-template.md), [spécification des badges](./badge-specification.md) | Guide de migration, rétrospective d'itération (peuvent être complétés après la première itération de version) | Les éléments de porte P0 ne peuvent être omis |
| Maintenance stable | En plus de la première publication : [spécification du journal des modifications](./changelog-specification.md), [spécification de gestion des versions](./version-management-specification.md), [spécification de guide de migration](./migration-guide-specification.md), [spécification d'observabilité](./observability-specification.md), [spécification de réponse aux incidents](./incident-response-specification.md), [spécification de dépannage](./troubleshooting-specification.md), [spécification de rétrospective d'itération](./iteration-retrospective-specification.md), [spécification de matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md) | Aucune | Tout changement cassant doit disposer d'un chemin de migration et être annoncé |

## 6. Combinaisons

### 6.1 Combinaison minimale viable

Destinée à un prototype individuel ou à un dépôt de validation privé, soit 10 documents :

| Usage | Spécifications |
| --- | --- |
| Contraintes | [règles absolues](./hard-rules.md), [pratiques interdites](./prohibited-practices.md) |
| Lancement | [spécification de lancement de projet et d'exigences](./project-initiation-and-requirements-specification.md), [spécification de nommage des projets](./project-naming-specification.md) |
| Page d'accueil | [gabarit standard de README](./readme-standard-template.md), [spécification de rédaction générale](./general-writing-specification.md) |
| Ingénierie | [spécification de style de code](./code-style-specification.md), [spécification de message de commit](./commit-message-specification.md), [spécification de tests](./testing-specification.md) |
| Publication | [spécification de push et de publication](./push-and-release-specification.md), [spécification de LICENSE](./license-specification.md) |

L'usage de cette combinaison impose de déclarer le mode déclassé dans les livrables et de compléter la combinaison intégrale de la section 6.3 avant la première publication publique.

### 6.2 Combinaison standard de publication publique

Sur la base de la combinaison minimale viable, compléter les éléments de base en matière de qualité, de conformité, de gouvernance et d'exploitation : ajouter la [porte qualité](./quality-gate.md), la [spécification des sections de README](./readme-sections-specification.md), la [spécification de mise en page visuelle du README](./readme-visual-layout-specification.md), la [spécification des badges](./badge-specification.md), la [matrice documentaire](./document-matrix.md), la [spécification de conformité open source](./open-source-compliance-specification.md), le [gabarit de clause de non-responsabilité](./disclaimer-template.md), le [gabarit SECURITY](./security-template.md), le [gabarit de guide de contribution](./contribution-guide-template.md), le [gabarit de code de conduite](./code-of-conduct-template.md), la [spécification du journal des modifications](./changelog-specification.md), la [spécification de gestion des versions](./version-management-specification.md), la [spécification d'accessibilité](./accessibility-specification.md), la [spécification de workflow CI](./ci-workflow-specification.md), la [spécification des gabarits d'Issue et de PR](./issue-and-pr-template-specification.md), la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md).

Cette combinaison satisfait toutes les conditions de passage des portes A, B et C d'un dépôt public ; elle constitue le point de départ recommandé pour la plupart des projets.

### 6.3 Combinaison de conformité complète

Elle s'applique à l'ensemble des spécifications et est destinée aux projets d'envergure organisationnelle, aux projets distribués dans un cadre réglementé, ou aux projets nécessitant une intégration programmatique expert / Skill / MCP / ligne de commande. Le nombre de documents fait foi selon l'[index en chinois simplifié](./README.md) ; lors de l'activation, vérifier item par item les portes de phase de la [table de correspondance du cycle de vie](./lifecycle-mapping-table.md).

## 7. Traitement des conflits

1. En cas de conflit au sein d'une même dimension, les exigences de la phase de publication la plus avancée prévalent ; les simplifications de la phase de prototype ne doivent pas se prolonger jusqu'à la phase publique.
2. En cas de conflit entre dimensions différentes, appliquer l'ordre de priorité de la section 2 ; les contraintes impératives et les portes de phase ne peuvent être supplantées par aucune dimension.
3. Si un projet présente effectivement un cas particulier nécessitant de s'écarter du présent guide, il doit consigner dans les livrables les spécifications écartées, la justification et les mesures compensatoires, et soumettre le tout à revue.
4. Le mode déclassé ne doit pas être utilisé pour un dépôt public, ni servir de base pour contourner les portes de licence ou de sécurité.

## Fichiers associés

- La correspondance complète entre phases et spécifications figure dans la [table de correspondance du cycle de vie](./lifecycle-mapping-table.md)
- L'adaptation des sections du README selon le type figure dans le [guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md)
- Les contraintes non adaptables figurent dans les [règles absolues](./hard-rules.md) et les [pratiques interdites](./prohibited-practices.md)
- Les conditions de passage des portes figurent dans la [porte qualité](./quality-gate.md)
