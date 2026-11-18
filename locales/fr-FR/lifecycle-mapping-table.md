# Table de correspondance du cycle de vie

> Problème que ce fichier résout : mapper l'ensemble des spécifications sur les huit phases du cycle de vie d'un projet, en précisant pour chaque phase les conditions d'entrée, les livrables clés, les spécifications centrales et la porte de sortie, afin de servir de point d'entrée unique de navigation pour puiser les spécifications « de l'intérieur vers l'extérieur, du début à la fin ».

Ce fichier ne répond qu'à la question « quelles spécifications sont nécessaires à une phase donnée, et quand peut-on passer à la phase suivante ». Les dispositions détaillées de chaque spécification au sein d'une phase restent régies par le fichier correspondant ; le déroulé opérationnel figure dans le [processus d'exécution](./execution-process.md), et l'adaptation selon le type de projet dans le [guide de sélection des spécifications](./specification-selection-guide.md).

## 1. Vue d'ensemble des phases

| Phase | Nom | Question centrale | Livrables clés | Porte de sortie |
| --- | --- | --- | --- | --- |
| 1 | Lancement du projet | Quoi faire, quel nom, comment configurer le dépôt | Conclusion de nommage, tableau des métadonnées du dépôt, liste des informations | Nommage conforme, informations obligatoires complètes ou signalées |
| 2 | Analyse des exigences | Quelles sont les exigences, comment les accepter | Liste des exigences, critères d'acceptation, matrice de traçabilité | Chaque exigence possède un identifiant unique et un critère d'acceptation |
| 3 | Conception de l'architecture | Comment décomposer, comment convenir des interfaces et des données | Documentation d'architecture, contrat d'API, modèle de données | Traçabilité des exigences vers la conception sans omission, interfaces revues |
| 4 | Développement | Comment écrire le code et livrer les commits de manière cohérente | Code, séquence de commits, workflow CI, documentation d'API | Revue validée, CI verte, aucune vulnérabilité critique dans les dépendances |
| 5 | Vérification par les tests | La qualité requise pour publier est-elle atteinte | Suite de tests, rapport de couverture, verdict des portes | Build et tests réussis, P0 à zéro |
| 6 | Déploiement et mise en ligne | Comment publier, comment présenter la page d'accueil | tag, Release, documentation de la page d'accueil, plan de restauration | Les trois niveaux de portes sont verts, plan de restauration vérifié |
| 7 | Exploitation et supervision | Comment détecter les problèmes, comment réagir | Supervision et alertes, processus de réponse, documentation d'incidents | Indicateurs clés sous alerte, canaux de réponse disponibles |
| 8 | Maintenance itérative | Comment faire une rétrospective, comment faire évoluer | Rapport de rétrospective, mise à jour de la feuille de route, guide de migration | Actions enregistrées, changements cassants dotés d'un chemin de migration |

Les phases 1 à 5 progressent de l'intérieur vers l'extérieur ; les phases 6 à 8 passent de la livraison à l'exploitation et à l'évolution. Les phases 7 et 8 peuvent se dérouler en parallèle, mais aucune ne peut contourner la porte de la phase 5.

## 2. Phase un : lancement du projet

- **Objectif de la phase** : déterminer le positionnement du projet, un nommage conforme et les métadonnées du dépôt, et établir la base d'informations commune aux phases suivantes.
- **Conditions d'entrée** : l'idée du projet est formée, les utilisateurs cibles et les problèmes à résoudre peuvent être énoncés.
- **Spécifications centrales** : [rôles et responsabilités](./roles-and-responsibilities.md), [spécification de lancement de projet et d'exigences](./project-initiation-and-requirements-specification.md), [spécification de nommage des projets](./project-naming-specification.md), [collecte d'informations et gabarits](./information-collection-and-templates.md), [processus d'exécution](./execution-process.md).
- **Livrables clés** : trois candidats de nom et conclusion de la recherche d'homonymes ; tableau des métadonnées du dépôt (description, topics, branche par défaut, visibilité, licence) ; liste des informations obligatoires et liste des informations manquantes.
- **Porte de sortie** : le nom du dépôt respecte toutes les règles absolues de la [spécification de nommage des projets](./project-naming-specification.md) ; le type de licence est déterminé ; les champs obligatoires sont complets, les éléments manquants sont signalés conformément à la [collecte d'informations et gabarits](./information-collection-and-templates.md).

## 3. Phase deux : analyse des exigences

- **Objectif de la phase** : décomposer l'idée en éléments d'exigence acceptables et traçables, et en déduire la feuille de route.
- **Conditions d'entrée** : les conclusions de nommage et de métadonnées de la phase un sont confirmées.
- **Spécifications centrales** : [spécification de lancement de projet et d'exigences](./project-initiation-and-requirements-specification.md), [spécification de matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md), [spécification de feuille de route](./roadmap-specification.md), [collecte d'informations et gabarits](./information-collection-and-templates.md).
- **Livrables clés** : liste des exigences et identifiants uniques ; critères d'acceptation de chaque exigence ; version initiale de la matrice de traçabilité des exigences ; feuille de route ordonnée par priorité.
- **Porte de sortie** : chaque exigence dispose d'un identifiant unique et d'un critère d'acceptation évaluable ; la matrice de traçabilité comporte les champs côté exigences ; les éléments planifiés de la feuille de route sont signalés comme non engageants en termes de livraison.

## 4. Phase trois : conception de l'architecture

- **Objectif de la phase** : déterminer les frontières des modules, les contrats d'interface et le modèle de données, afin que les exigences puissent être affectées à des unités de conception concrètes.
- **Conditions d'entrée** : la liste des exigences et les critères d'acceptation sont confirmés.
- **Spécifications centrales** : [spécification de documentation d'architecture](./architecture-design-document-specification.md), [spécification de conception d'API](./api-design-specification.md), [spécification de conception de base de données](./database-design-specification.md), [matrice documentaire](./document-matrix.md), [spécification de rédaction générale](./general-writing-specification.md).
- **Livrables clés** : documentation de conception d'architecture ; contrat d'API ; modèle de données et stratégie de migration ; inventaire de la matrice documentaire.
- **Porte de sortie** : chaque exigence pointe dans la matrice de traçabilité vers au moins une unité de conception ; les interfaces et le modèle de données ont été revus ; les responsabilités de chaque fichier de la matrice documentaire ne se chevauchent pas.

## 5. Phase quatre : développement

- **Objectif de la phase** : mettre en œuvre la conception avec un style de code, un format de commit et un processus de revue cohérents, tout en gardant les dépendances et l'automatisation maîtrisées.
- **Conditions d'entrée** : l'architecture et les contrats d'interface ont passé la revue.
- **Spécifications centrales** : [spécification de style de code](./code-style-specification.md), [spécification de workflow Git et de branches](./git-workflow-and-branching-specification.md), [spécification de message de commit](./commit-message-specification.md), [spécification de revue de code](./code-review-specification.md), [spécification de gestion des dépendances](./dependency-management-specification.md), [spécification de propriété du code](./code-ownership-specification.md), [spécification de documentation d'API](./api-documentation-specification.md), [spécification de workflow CI](./ci-workflow-specification.md).
- **Livrables clés** : code conforme à la spécification de style ; séquence de commits conforme à Conventional Commits ; workflow CI ; documentation d'API synchronisée avec l'implémentation.
- **Porte de sortie** : les messages de commit et le nommage des branches sont conformes ; le code a été revu et le routage de propriété est correct ; le workflow CI passe ; les dépendances ne présentent aucune vulnérabilité critique non traitée.

## 6. Phase cinq : vérification par les tests

- **Objectif de la phase** : confirmer, par des tests reproductibles et un verdict de porte, que les livrables atteignent la base de qualité requise pour la publication.
- **Conditions d'entrée** : l'implémentation fonctionnelle est terminée, le workflow CI peut s'exécuter.
- **Spécifications centrales** : [spécification de tests](./testing-specification.md), [porte qualité](./quality-gate.md), [spécification des indicateurs de mesure de la qualité](./quality-metrics-specification.md), [spécification d'accessibilité](./accessibility-specification.md), [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md).
- **Livrables clés** : suite de tests et rapport de couverture ; verdict item par item des portes ; enregistrement des contrôles de sécurité et d'accessibilité.
- **Porte de sortie** : build, tests et analyse statique réussis ; tous les éléments P0 des portes A, B et C sont à zéro ; les éléments P1 sont enregistrés comme tâches à faire ou sont terminés.

## 7. Phase six : déploiement et mise en ligne

- **Objectif de la phase** : publier la version selon un processus maîtrisé, et finaliser la documentation de la page d'accueil ainsi que les livrables visibles par les utilisateurs.
- **Conditions d'entrée** : la porte de la phase cinq est franchie, aucun élément P0 n'est non résolu.
- **Spécifications centrales** : [spécification de push et de publication](./push-and-release-specification.md), [spécification de gestion des versions](./version-management-specification.md), [spécification du journal des modifications](./changelog-specification.md), [spécification de déploiement et de restauration](./deployment-and-rollback-specification.md), [spécification de guide de migration](./migration-guide-specification.md), [spécification de workflow CI](./ci-workflow-specification.md), [spécification des gabarits d'Issue et de PR](./issue-and-pr-template-specification.md) ; pour la documentation de la page d'accueil, voir le [gabarit standard de README](./readme-standard-template.md), la [spécification des sections de README](./readme-sections-specification.md), la [spécification de mise en page visuelle du README](./readme-visual-layout-specification.md), la [spécification des badges](./badge-specification.md) et le [guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md).
- **Livrables clés** : version sémantique et tag annoté ; Release Notes et journal des modifications ; README de la page d'accueil et gabarits communautaires ; enregistrement du déploiement et plan de restauration.
- **Porte de sortie** : les trois niveaux de portes sont verts ; le tag est de type annotated et conforme à SemVer ; le plan de restauration a été vérifié ; la documentation de la page d'accueil ne contient ni chemin absolu local ni espace réservé résiduel.

## 8. Phase sept : exploitation et supervision

- **Objectif de la phase** : établir les capacités d'observabilité et les mécanismes de réponse, afin que les problèmes en production puissent être détectés, localisés et traités.
- **Conditions d'entrée** : la version est publiée, le service ou l'artefact est disponible.
- **Spécifications centrales** : [spécification d'observabilité](./observability-specification.md), [spécification de réponse aux incidents](./incident-response-specification.md), [spécification de dépannage](./troubleshooting-specification.md), [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md), [gabarit SECURITY](./security-template.md), [clause de non-responsabilité](./disclaimer.md), [gabarit de clause de non-responsabilité](./disclaimer-template.md).
- **Livrables clés** : indicateurs clés et règles d'alerte ; classification des incidents et processus de réponse ; documentation des questions fréquentes et du dépannage ; canal de réception des vulnérabilités.
- **Porte de sortie** : tous les indicateurs clés sont dotés d'alertes ; le canal de signalement des vulnérabilités est disponible et vérifié ; le processus de réponse aux incidents a fait l'objet d'au moins un exercice ou une simulation sur table.

## 9. Phase huit : maintenance itérative

- **Objectif de la phase** : faire la rétrospective des itérations livrées, gérer le chemin d'évolution et maintenir l'alignement continu entre exigences, conception et tests.
- **Conditions d'entrée** : au moins une publication ou un cycle d'itération est achevé.
- **Spécifications centrales** : [spécification de rétrospective d'itération](./iteration-retrospective-specification.md), [spécification de feuille de route](./roadmap-specification.md), [spécification de matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md), [spécification du journal des modifications](./changelog-specification.md), [spécification de guide de migration](./migration-guide-specification.md), [spécification de gestion des versions](./version-management-specification.md), [spécification de promotion open source](./open-source-promotion-specification.md).
- **Livrables clés** : rapport de rétrospective d'itération et actions ; feuille de route et matrice de traçabilité mises à jour ; guide de migration des changements cassants ; enregistrement des changements de version.
- **Porte de sortie** : les actions du cycle précédent ont un responsable et une échéance enregistrés ; les changements cassants disposent d'un chemin de migration et d'une annonce ; la matrice de traçabilité ne présente aucun lien rompu.

## 10. Spécifications transverses

Les spécifications suivantes ne relèvent pas d'une phase unique et doivent rester en vigueur pendant toutes les phases :

| Catégorie | Spécifications | Mode d'application |
| --- | --- | --- |
| Contraintes impératives | [règles absolues](./hard-rules.md), [pratiques interdites](./prohibited-practices.md) | Toute violation à n'importe quelle phase bloque, aucune exemption n'est admise pour raison d'avancement |
| Processus et terminologie | [rôles et responsabilités](./roles-and-responsibilities.md), [processus d'exécution](./execution-process.md), [glossaire](./glossary.md) | Unifient la répartition des rôles, la terminologie des phases et l'ordre de livraison |
| Communauté et gouvernance | [spécification de guide de contribution](./contribution-guide-specification.md), [gabarit de guide de contribution](./contribution-guide-template.md), [spécification de code de conduite](./code-of-conduct-specification.md), [gabarit de code de conduite](./code-of-conduct-template.md) | À finaliser avant que le dépôt ne devienne visible, puis ajustés avec la taille de la communauté |
| Juridique et conformité | [spécification de conformité open source](./open-source-compliance-specification.md), [spécification de LICENSE](./license-specification.md), [spécification de NOTICE](./notice-specification.md), [clause de non-responsabilité](./disclaimer.md), [gabarit de clause de non-responsabilité](./disclaimer-template.md) | Licence déterminée en phase un, tous les documents juridiques finalisés avant la phase six |
| Rédaction et multilinguisme | [spécification de rédaction générale](./general-writing-specification.md), [spécification multilingue](./multilingual-specification.md), [guide de rédaction des fonctionnalités et arbitrages d'ingénierie](./features-and-engineering-tradeoffs-guide.md), [matrice documentaire](./document-matrix.md) | Applicables à toute la production documentaire, garantissent la cohérence des formulations |
| Intégration programmatique | [spécification de métadonnées lisibles par machine](./machine-readable-metadata-specification.md), [spécification de rédaction de Skill](./skill-authoring-specification.md), [spécification des outils MCP](./mcp-tool-specification.md), [spécification d'invocation d'Agent et de prompts](./agent-invocation-and-prompt-specification.md) | À superposer lorsqu'un appel expert, Skill, MCP ou en ligne de commande est nécessaire |

## 11. Déclassement et repli

1. Un dépôt de scripts temporaires privé peut être déclassé en n'exécutant que les portes P0, mais il doit déclarer le « mode déclassé » dans les livrables et préciser les éléments non exécutés.
2. Si la porte de sortie d'une phase n'est pas franchie, il est interdit de passer à la phase suivante ; les problèmes, responsabilités et actions doivent être enregistrés conformément au [format de rapport d'audit](./audit-report-format.md).
3. Si un problème P0 est découvert après la phase six, revenir à la phase cinq pour un nouveau verdict et, si nécessaire, exécuter le processus de traitement des incidents de la [spécification de push et de publication](./push-and-release-specification.md).

## Fichiers associés

- Le déroulé opérationnel au sein d'une phase figure dans le [processus d'exécution](./execution-process.md)
- L'adaptation des spécifications selon le type de projet figure dans le [guide de sélection des spécifications](./specification-selection-guide.md)
- Les critères de verdict des portes figurent dans la [porte qualité](./quality-gate.md)
- Le format d'enregistrement des problèmes d'audit figure dans le [format de rapport d'audit](./audit-report-format.md)
