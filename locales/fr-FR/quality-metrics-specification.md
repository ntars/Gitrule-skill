# Spécification des indicateurs de mesure de la qualité

> Problème que ce fichier résout : définir des indicateurs de qualité traçables ainsi que leurs modalités de mesure, afin d'éviter d'évaluer la qualité d'un projet à l'aide de chiffres sans fondement.

## 1. Principes des indicateurs

1. Un indicateur doit être mesurable et reproductible ; le mode de collecte et la modalité statistique doivent être précisés.
2. Un indicateur sert à l'amélioration ; il ne sert pas à établir un classement sommaire ni à créer une pression.
3. Chaque indicateur doit être assorti d'une valeur cible et d'une valeur actuelle, et faire l'objet d'une revue périodique.

## 2. Indicateurs recommandés

| Catégorie | Indicateur | Modalité de mesure |
| --- | --- | --- |
| Tests | Couverture des tests | Part des lignes de code couvertes, avec mention de l'outil de mesure |
| Tests | Taux de réussite des tests | Nombre de cas réussis / nombre total de cas |
| Build | Taux de réussite du build | Nombre de builds réussis / nombre total de builds |
| Défauts | Densité de défauts | Nombre de défauts détectés par unité de volume de code |
| Défauts | Durée moyenne de correction | Durée moyenne entre la détection et la fin de la correction |
| Performance | Temps de réponse | Scénario et centile précisés (par exemple P95) |
| Dépendances | Nombre de vulnérabilités critiques | Nombre de vulnérabilités critiques de dépendances non corrigées |

## 3. Règles obligatoires

1. Un indicateur de performance doit préciser l'environnement et la méthode de test ; les chiffres sans condition sont interdits (voir la [spécification générale de rédaction](./general-writing-specification.md)).
2. La collecte des données d'indicateurs doit être automatisée afin de réduire les biais des statistiques manuelles.
3. Toute anomalie d'indicateur doit faire l'objet d'un suivi documenté, intégré à la [spécification de feuille de route](./roadmap-specification.md) ou au suivi des problèmes.

## Fichiers associés

- Porte qualité : voir la [porte qualité](./quality-gate.md)
- Exigences de test : voir la [spécification de tests](./testing-specification.md)
- Rédaction des sections de performance : voir la [spécification des sections de README](./readme-sections-specification.md)
