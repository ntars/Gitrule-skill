# Processus d'exécution

> Problème que ce fichier résout : définir la séquence complète des phases, du lancement à la livraison, les conditions d'entrée et les livrables de chaque phase, ainsi que la règle de questionnement bloquant en cas d'information insuffisante.

## 1. Processus de push sous pilotage (Phase 0–6)

### Phase 0 · Lancement (Project Init)

Livrable : 3 candidats de nom de projet + justification du choix + conclusion de la recherche d'homonymes + tableau des métadonnées du dépôt (description / topics / branche par défaut / visibilité / license). Les règles de nommage figurent dans la [spécification de nommage des projets](./project-naming-specification.md).

### Phase 1 · Inventaire (Inventory)

Analyser le dépôt et produire un inventaire structuré :
- pile technique, fichier d'entrée, gestionnaire de paquets, lockfile
- documentation existante, documentation manquante
- les 10 fichiers les plus volumineux du dépôt
- CI / gabarits / règles de protection existants
- état git actuel : fichiers non suivis, modifications non commitées, commits suspects dans l'historique

### Phase 2 · Audit parallèle (Audit)

Répartir les dimensions entre les sous-agents pour une exécution parallèle selon la [matrice des dimensions d'audit](./review-dimension-matrix.md) ; le mode de répartition est décrit dans le [contrat de répartition des sous-agents](./sub-agent-dispatch-contract.md). Chaque sous-agent ne renvoie qu'une conclusion structurée, pas de long texte discursif.

### Phase 3 · Correction (Fix)

Lister les tâches à traiter dans l'ordre P0 → P1 → P2, en indiquant l'agent responsable et l'action prévue. Le passage à la Phase 5 est interdit tant que les P0 ne sont pas à zéro.

### Phase 4 · Génération documentaire (Docs)

Répartir fichier par fichier entre les agents documentaires selon la [matrice documentaire](./document-matrix.md). **Écrire un seul fichier à la fois, le valider, puis passer au suivant.**

### Phase 5 · Push (Push)

Exécuter conformément à la [spécification de push et de publication](./push-and-release-specification.md), en affichant le résultat ligne par ligne.

### Phase 6 · Après le push (Post-Push)

Créer le tag, rédiger les Release Notes, vérifier la disponibilité des badges et des liens, confirmer que la CI est verte, confirmer l'exactitude des informations de la zone About.

## 2. Processus de génération documentaire (phases 0–5)

Progresser dans l'ordre des phases ; il est interdit de passer à la phase suivante tant que la précédente n'est pas achevée.

| Phase | Nom | Condition d'entrée | Livrable |
| --- | --- | --- | --- |
| 0 | Vérification des informations | Réception de cette spécification et des éléments du projet | Liste des informations confirmées, liste des informations manquantes |
| 1 | Questionnement bloquant | Champs obligatoires manquants (voir la [collecte d'informations et gabarits](./information-collection-and-templates.md)) | Liste de questions structurée, regroupée par champ |
| 2 | Validation de la structure | Champs obligatoires complets | Sommaire des sections du README et plan des points clés de chaque section, soumis à validation de l'utilisateur |
| 3 | Génération documentaire | L'utilisateur valide la structure ou indique explicitement qu'aucune validation n'est nécessaire | Ensemble des livrables |
| 4 | Porte qualité | Génération documentaire terminée | Résultat d'évaluation point par point de la [porte qualité](./quality-gate.md) |
| 5 | Livraison | Toutes les portes franchies ou éléments non franchis déjà marqués | Sortie dans l'ordre du [format de rapport d'audit](./audit-report-format.md), avec les instructions de push en annexe |

## 3. Règles de questionnement de la phase 1

1. Poser les questions regroupées par champ, sans dépasser 15 éléments par tour.
2. Chaque question doit préciser son objectif et les sections concernées, afin de permettre à l'utilisateur d'évaluer la priorité.
3. Lorsque l'utilisateur indique explicitement qu'un élément ne peut pas être fourni, marquer «【À confirmer : nom du champ】» à l'emplacement correspondant du document et en faire la synthèse en fin de document.
4. Lorsque l'utilisateur répond « selon ton jugement », une valeur suggérée peut être proposée, mais elle doit être marquée «【Valeur suggérée, en attente de confirmation de l'utilisateur】».

## Fichiers associés

- Rôles et responsabilités : voir les [rôles et responsabilités](./roles-and-responsibilities.md)
- Champs obligatoires et marquage des manques : voir la [collecte d'informations et gabarits](./information-collection-and-templates.md)
- Évaluation des portes : voir la [porte qualité](./quality-gate.md)
