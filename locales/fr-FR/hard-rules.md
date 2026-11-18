# Règles absolues

> Problème que ce fichier résout : énumérer les règles non négociables dont la violation, quelle qu'elle soit, bloque le push et interdit le « pousser d'abord, corriger ensuite ».

## Tableau des règles absolues

| # | Règle |
|---|---|
| H1 | Le nom du dépôt doit respecter la [spécification de nommage des projets](./project-naming-specification.md) ; la casse, les caractères et la longueur doivent être entièrement conformes |
| H2 | Un fichier `LICENSE` est obligatoire ; sans licence, les droits sont réservés par défaut et la publication est interdite |
| H3 | Ne jamais committer de clés, jetons, clés privées, `.env`, AK/SK de fournisseur cloud ou chaînes de connexion à une base de données |
| H4 | Ne jamais committer d'artefacts de build, de répertoires de dépendances, de configuration d'IDE ni de fichiers système inutiles |
| H5 | Un fichier ne doit pas dépasser 100 Mo ; au-delà de 50 Mo, LFS ou exclusion est obligatoire |
| H6 | Un `README.md` est obligatoire et doit contenir : positionnement en une phrase, installation, exemple minimal exécutable, licence |
| H7 | La branche par défaut doit être protégée ; le push direct sur `main`/`master` est interdit |
| H8 | `git push --force` est interdit sur les branches publiques ; sur une branche personnelle, seul `--force-with-lease` est autorisé |
| H9 | Avant le push, `build` et `test` doivent réussir ; une CI rouge interdit la fusion dans la branche principale |
| H10 | Le message de commit doit respecter Conventional Commits ; les commits sans information du type `wip`/`update`/`fix bug` sont interdits |
| H11 | Chaque document constitue un fichier distinct avec une responsabilité distincte ; entasser tout le contenu dans le README est interdit (voir la [matrice documentaire](./document-matrix.md)) |
| H12 | Dès qu'une clé a été poussée, il faut immédiatement la renouveler et nettoyer l'historique ; un simple commit de suppression ne suffit pas |

## Contraintes d'application

- La violation d'une seule règle **bloque le push** ; le « pousser d'abord, corriger ensuite » n'est pas autorisé.
- Le résultat de l'évaluation de H1–H12 doit figurer dans la liste des problèmes du [format de rapport d'audit](./audit-report-format.md), chaque entrée étant accompagnée d'une preuve (chemin:ligne / sortie de commande).
- En cas de violation de H12, appliquer la procédure de traitement d'incident de la [spécification de push et de publication](./push-and-release-specification.md).

## Fichiers associés

- Règles de nommage détaillées : voir la [spécification de nommage des projets](./project-naming-specification.md)
- Conditions de passage de la porte : voir la [porte qualité](./quality-gate.md)
- Récapitulatif des pratiques interdites : voir les [pratiques interdites](./prohibited-practices.md)
