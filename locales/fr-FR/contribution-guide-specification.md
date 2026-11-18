# Spécification du guide de contribution

> Problème que ce fichier résout : définir le processus complet et les règles de participation des contributeurs externes au projet, servant de base à la rédaction du fichier CONTRIBUTING.md.

## 1. Contenu obligatoire

Le guide de contribution doit comporter les parties suivantes :

1. **Modes de participation** : canaux de discussion des tickets, d'amélioration de la documentation, de contribution au code et de remontée de problèmes.
2. **Mise en place de l'environnement de développement** : installation des dépendances, prérequis d'environnement, commandes d'exécution locale.
3. **Modèle de branches** : règles de nommage des branches, branche de création, branche cible.
4. **Convention de commit** : format du message de commit (voir la [spécification des messages de commit](./commit-message-specification.md)).
5. **Exigences relatives aux PR** : périmètre des modifications, points d'auto-test, gabarit de description, critères de revue.
6. **Exigences de tests** : commandes de test à faire passer et seuil de couverture (voir la [spécification des tests](./testing-specification.md)).
7. **Code de conduite** : renvoi vers CODE_OF_CONDUCT.md (voir la [spécification du code de conduite](./code-of-conduct-specification.md)).
8. **Convention relative aux Issue** : exigences de rédaction des questions et des rapports de défauts.
9. **Déclaration de licence** : les contributions suivent par défaut la licence du projet (voir la [spécification LICENSE](./license-specification.md)).

## 2. Exigences de rédaction

1. Les commandes doivent être directement exécutables et inclure les indications nécessaires sur le répertoire de travail.
2. Chaque étape du processus précise sa condition de déclenchement et son résultat attendu.
3. Il est interdit de se limiter à « les PR sont bienvenues » sans processus concret (correspond au contrôle de gouvernance communautaire de la [porte qualité](./quality-gate.md)).

## Fichiers associés

- Limites de responsabilité documentaire : voir la [matrice documentaire](./document-matrix.md)
- Les gabarits de PR et d'Issue relèvent de la dimension D14, voir la [matrice des dimensions de revue](./review-dimension-matrix.md)
- Conventions de branches et de commit : voir la [spécification du workflow Git et de la gestion des branches](./git-workflow-and-branching-specification.md)
