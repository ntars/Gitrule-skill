# Index général des spécifications en français

[简体中文](../zh-CN/README.md) | [English](../en-US/README.md) | [繁體中文](../zh-TW/README.md) | [日本語](../ja-JP/README.md) | [한국어](../ko-KR/README.md) | [Français](./README.md)

> Problème que ce fichier résout : servir de navigation pour l'ensemble des spécifications en français, en listant la responsabilité, le domaine et le parcours de lecture des 67 documents, afin de les consulter à la demande.

> Ce dépôt constitue le premier cas de mise en œuvre de son propre référentiel : ce document et tous les fichiers de ce répertoire sont rédigés selon le référentiel et passent ses contrôles structurels.


## 1. Principes généraux et gouvernance (10 documents)

| Fichier | Responsabilité unique |
| --- | --- |
| [Table de correspondance du cycle de vie](./lifecycle-mapping-table.md) | Associe chaque spécification aux huit phases du cycle de vie d'un projet, en précisant les conditions d'entrée, les livrables et les portes de sortie |
| [Guide de sélection des spécifications](./specification-selection-guide.md) | Fournit les critères de sélection et de combinaison selon le type de projet, la taille de l'équipe et l'étape de publication |
| [Rôles et responsabilités](./roles-and-responsibilities.md) | Définit l'identité de l'acteur, les limites de responsabilité, les conditions de déclenchement, le périmètre d'application et les contraintes absolues |
| [Processus d'exécution](./execution-process.md) | Définit les phases du lancement à la livraison, les conditions d'entrée, les livrables et les règles de questionnement |
| [Règles absolues](./hard-rules.md) | Définit 12 règles non négociables dont la violation bloque le push |
| [Pratiques interdites](./prohibited-practices.md) | Regroupe tous les comportements interdits à ne jamais enfreindre |
| [Glossaire](./glossary.md) | Définit de manière centralisée les termes techniques et les correspondances chinois-anglais afin de garantir une expression cohérente |
| [Spécification du guide de contribution](./contribution-guide-specification.md) | Définit le processus et les normes de participation des contributeurs externes |
| [Spécification du code de conduite](./code-of-conduct-specification.md) | Définit la structure et le mécanisme d'application du code de conduite communautaire |
| [Clause de non-responsabilité](./disclaimer.md) | Définit la nature du contenu, les clauses d'absence de garantie, les responsabilités de l'utilisateur et les limites de responsabilité, et précise la relation avec la licence MIT |

## 2. Planification et lancement (3 documents)

| Fichier | Responsabilité unique |
| --- | --- |
| [Spécification de lancement et d'exigences](./project-initiation-and-requirements-specification.md) | Définit les éléments de lancement, la collecte des exigences et la délimitation du périmètre |
| [Spécification de la feuille de route](./roadmap-specification.md) | Définit les champs de la feuille de route, le marquage des statuts et le principe de non-engagement |
| [Collecte d'informations et gabarits](./information-collection-and-templates.md) | Définit les champs obligatoires et facultatifs, le marquage des éléments manquants et les différents gabarits |

## 3. Nommage et documentation (18 documents)

| Fichier | Responsabilité unique |
| --- | --- |
| [Spécification de nommage des projets](./project-naming-specification.md) | Définit les règles de nommage des dépôts ainsi que le format de la description et des sujets |
| [Matrice documentaire](./document-matrix.md) | Définit quels documents produire à chaque phase et où les placer |
| [Spécification des sections du README](./readme-sections-specification.md) | Définit les 20 sections obligatoires du README et ce que chacune doit ou ne doit pas contenir |
| [Spécification de rédaction générale](./general-writing-specification.md) | Définit le ton, la terminologie, les conventions de ponctuation, les règles de titres et les conventions de espaces réservés |
| [Spécification multilingue](./multilingual-specification.md) | Définit l'organisation par code de langue, le basculement de langue, la cohérence des traductions et la synchronisation des modifications unilatérales |
| [Guide de rédaction des fonctionnalités et des arbitrages techniques](./features-and-engineering-tradeoffs-guide.md) | Définit la structure de rédaction des fonctionnalités et des arbitrages techniques, avec preuves et limites |
| [Spécification du journal des modifications](./changelog-specification.md) | Définit le format du journal des modifications, la classification des changements et les règles de publication |
| [Spécification de la documentation API](./api-documentation-specification.md) | Définit la structure, les champs et les exemples de la documentation API |
| [Spécification des gabarits d'issue et de PR](./issue-and-pr-template-specification.md) | Définit les champs et la structure des gabarits d'issue et de pull request |
| [Rapport d'étude sur les gabarits de README](./readme-template-research-report.md) | Synthétise les pratiques de page d'accueil des projets open source de premier plan et en tire les conclusions de conception |
| [Gabarit standard de README](./readme-standard-template.md) | Fournit un README de 20 sections directement copiable, avec table de correspondance des espaces réservés et liste d'auto-contrôle |
| [Spécification de la mise en page visuelle du README](./readme-visual-layout-specification.md) | Définit la structure de la première écran, la largeur des images, les tableaux et les règles de mise en page |
| [Spécification des badges](./badge-specification.md) | Définit les types de badges, leur ordre, leur nombre et les règles d'affichage statique |
| [Guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md) | Donne les priorités de sections et les variantes de contenu selon la catégorie de projet |
| [Gabarit de clause de non-responsabilité](./disclaimer-template.md) | Gabarit copiable de clause de non-responsabilité, avec table de correspondance des espaces réservés |
| [Gabarit de code de conduite](./code-of-conduct-template.md) | Gabarit copiable de code de conduite communautaire |
| [Gabarit de guide de contribution](./contribution-guide-template.md) | Gabarit copiable de guide de contribution pour les contributeurs externes |
| [Gabarit SECURITY](./security-template.md) | Gabarit copiable de politique de sécurité et de signalement des vulnérabilités |

## 4. Développement et ingénierie (12 documents)

| Fichier | Responsabilité unique |
| --- | --- |
| [Spécification de style de code](./code-style-specification.md) | Définit les règles de formatage, de nommage et de commentaires du code |
| [Spécification Git et branches](./git-workflow-and-branching-specification.md) | Définit la stratégie de branches, les règles de fusion et la protection des branches |
| [Spécification des messages de commit](./commit-message-specification.md) | Définit le format, le type et la portée des messages de commit |
| [Spécification de revue de code](./code-review-specification.md) | Définit le processus de revue, les points de contrôle et les critères d'approbation |
| [Spécification des tests](./testing-specification.md) | Définit les niveaux de test, la couverture, les données de test et les critères de réussite |
| [Spécification de gestion des dépendances](./dependency-management-specification.md) | Définit les règles d'introduction, de mise à jour, de verrouillage et de suppression des dépendances |
| [Spécification du document de conception d'architecture](./architecture-design-document-specification.md) | Définit la structure du document de conception d'architecture et les décisions d'architecture consignées |
| [Spécification de conception d'API](./api-design-specification.md) | Définit les conventions de nommage, les codes de retour, la pagination et la gestion des erreurs des API |
| [Spécification de conception de base de données](./database-design-specification.md) | Définit la conception des tables, les conventions de nommage, les index et les règles de migration |
| [Spécification du flux de travail CI](./ci-workflow-specification.md) | Définit les étapes, les déclencheurs et les conditions d'échec du pipeline d'intégration continue |
| [Spécification de propriété du code](./code-ownership-specification.md) | Définit les règles de propriété du code et le mécanisme d'approbation |
| [Spécification d'accessibilité](./accessibility-specification.md) | Définit les exigences d'accessibilité, les critères de contrôle et les méthodes de vérification |

## 5. Qualité et conformité (10 documents)

| Fichier | Responsabilité unique |
| --- | --- |
| [Matrice des dimensions d'audit](./review-dimension-matrix.md) | Définit les 14 dimensions d'audit, les agents responsables et les niveaux de priorité |
| [Porte qualité](./quality-gate.md) | Définit les conditions de passage des trois niveaux de porte et le gabarit de liste d'évaluation |
| [Spécification des métriques de qualité](./quality-metrics-specification.md) | Définit les métriques de qualité, les méthodes de mesure et les seuils |
| [Spécification de conformité open source](./open-source-compliance-specification.md) | Définit les obligations de conformité, la vérification des licences et la gestion des avis |
| [Spécification NOTICE](./notice-specification.md) | Définit le contenu, le format et les règles de mise à jour du fichier NOTICE |
| [Spécification de licence](./license-specification.md) | Définit les règles de choix de licence, de dépôt du fichier et d'indication dans le README |
| [Spécification de sécurité et de confidentialité](./security-and-privacy-specification.md) | Définit la gestion des secrets, la protection des données personnelles et la divulgation des vulnérabilités |
| [Format du rapport d'audit](./audit-report-format.md) | Définit la structure du rapport d'audit, la classification des problèmes et les conclusions |
| [Spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md) | Définit la traçabilité bidirectionnelle des exigences vers la conception, l'implémentation, les tests et la publication, ainsi que les statistiques de couverture |
| [Contrat de délégation des sous-agents](./sub-agent-dispatch-contract.md) | Définit les conditions de délégation, les entrées et sorties attendues et les limites de responsabilité des sous-agents |

## 6. Publication et exploitation (10 documents)

| Fichier | Responsabilité unique |
| --- | --- |
| [Spécification de push et de publication](./push-and-release-specification.md) | Définit la liste de contrôle avant push, le processus de publication et les règles de retour arrière |
| [Spécification de gestion des versions](./version-management-specification.md) | Définit les règles de numérotation des versions, le marquage et la stratégie de maintenance |
| [Spécification de déploiement et de restauration](./deployment-and-rollback-specification.md) | Définit les étapes de déploiement, les conditions de restauration et le plan de retour arrière |
| [Spécification d'observabilité](./observability-specification.md) | Définit les journaux, les métriques, le traçage et les règles d'alerte |
| [Spécification de réponse aux incidents](./incident-response-specification.md) | Définit les niveaux d'incident, le processus de réponse et la rédaction du post-mortem |
| [Spécification de promotion open source](./open-source-promotion-specification.md) | Définit les éléments de la page d'accueil, les canaux de promotion et le rythme de publication |
| [Spécification du guide de migration](./migration-guide-specification.md) | Définit la structure du guide de migration, la description des changements cassants et les chemins de restauration |
| [Spécification de dépannage](./troubleshooting-specification.md) | Définit la structure des fiches de dépannage, la description des symptômes et les étapes de vérification |
| [Spécification de la rétrospective d'itération](./iteration-retrospective-specification.md) | Définit le format de la rétrospective, l'analyse des causes racines et le suivi des actions |
| [Liste de contrôle d'alignement d'un projet existant](./legacy-project-alignment-checklist.md) | Fournit une liste de contrôle pour aligner un projet existant sur le référentiel |

## 7. Adaptation à l'IA et aux machines (4 documents)

| Fichier | Responsabilité unique |
| --- | --- |
| [Spécification des métadonnées lisibles par machine](./machine-readable-metadata-specification.md) | Définit la structure du manifeste de métadonnées destiné à une consommation programmatique |
| [Spécification de rédaction de Skill](./skill-authoring-specification.md) | Définit la structure, le déclenchement et le chargement progressif des Skills |
| [Spécification des outils MCP](./mcp-tool-specification.md) | Définit la conception des interfaces d'outils MCP et les règles de description |
| [Spécification d'invocation d'Agent et de prompt](./agent-invocation-and-prompt-specification.md) | Définit les contrats de répartition des Agents et la rédaction des prompts |

Total des sept domaines : 67 documents.

## Parcours de lecture

- **Déterminer le périmètre retenu** : Guide de sélection des spécifications → Table de correspondance du cycle de vie → les fichiers de spécification de la phase concernée.
- **Tout au long du cycle de vie** : Table de correspondance du cycle de vie → Spécification de lancement et d'exigences → Spécification de la matrice de traçabilité des exigences → Spécification du document de conception d'architecture → Spécification des tests → Spécification de déploiement et de restauration → Spécification d'observabilité → Spécification de la rétrospective d'itération.
- **Push rapide** : Règles absolues → Porte qualité → Spécification de push et de publication → Format du rapport d'audit.
- **Générer la documentation de zéro** : Rôles et responsabilités → Processus d'exécution → Collecte d'informations et gabarits → Matrice documentaire → Spécification des sections du README → Spécification de conformité open source → Porte qualité.
- **Rédiger un README** : Rapport d'étude sur les gabarits de README → Spécification de la mise en page visuelle du README → Spécification des badges → Guide d'adaptation du README par catégorie → Gabarit standard de README.
- **Audit complet** : Matrice des dimensions d'audit → Contrat de délégation des sous-agents → Règles absolues → Porte qualité → Format du rapport d'audit.
- **Intégration programmatique** : Spécification des métadonnées lisibles par machine → Spécification de rédaction de Skill / Spécification des outils MCP / Spécification d'invocation d'Agent et de prompt.
- **Limites de risque et de responsabilité** : Clause de non-responsabilité → Gabarit de clause de non-responsabilité → Gabarit SECURITY → Spécification de sécurité et de confidentialité → Spécification de conformité open source.
- **Générer les fichiers de gouvernance communautaire** : Gabarit de guide de contribution → Gabarit de code de conduite → Gabarit SECURITY → Gabarit de clause de non-responsabilité.

## Conventions terminologiques

- **Doit / Ne doit pas** : exigence impérative.
- **Devrait / Ne devrait pas** : recommandé ou déconseillé ; tout écart doit être justifié.
- **Peut** : facultatif.
- **P0 / P1 / P2** : P0 bloque le push ; P1 doit être corrigé avant le push ou consigné comme tâche à traiter ; P2 est une optimisation suggérée.

## Fichiers associés

- Retour à l'accueil du dépôt : [../../README.md](../../README.md)
- Licence : [../../LICENSE](../../LICENSE)
