# Matrice des dimensions de revue

> Problème que ce fichier résout : définir les 14 dimensions de la revue parallèle de la Phase 2, leurs points de contrôle respectifs, l'agent recommandé et le niveau d'échec, afin de servir de base à la répartition et à l'évaluation.

## Matrice des dimensions de revue

| # | Dimension | Points de contrôle (mots-clés, le détail est développé par le sous-agent) | Agent recommandé | Niveau d'échec |
|---|---|---|---|---|
| D1 | Sécurité et confidentialité | Analyse des clés, `.env`, clés privées, noms de domaine/IP internes, données personnelles, résidus dans les journaux | security-auditor | P0 |
| D2 | Licence et aspects juridiques | Présence et type de LICENSE, compatibilité des licences des dépendances, NOTICE, déclarations relatives aux tiers | license-checker | P0 |
| D3 | Hygiène du dépôt | Couverture du .gitignore, artefacts et répertoires de dépendances, .gitattributes, fins de ligne LF, bits exécutables, conflits de casse de noms de fichiers | repo-hygienist | P0/P1 |
| D4 | Volume et binaires | Fichiers >50 Mo, compression des images, configuration LFS, gonflement de l'historique | repo-hygienist | P1 |
| D5 | Build reproductible | Commit du lockfile, déclaration de la version du moteur, scripts de build, build réussi en environnement propre | build-verifier | P0 |
| D6 | Tests et analyse statique | Tests unitaires réussis, couverture, lint, format, vérification des types | ci-runner | P0/P1 |
| D7 | Historique des commits | Conventional Commits, atomicité, absence de WIP, informations sur l'auteur, absence de message de commit sensible | commit-reviewer | P1 |
| D8 | Branches et publication | Protection de main, nommage des branches, tag SemVer, tag annoté, Release Notes | release-manager | P1 |
| D9 | Automatisation | Flux de travail CI exécutable, badges d'état, dependabot, CODEOWNERS, gabarits d'issue/PR | ci-runner | P1 |
| D10 | Métadonnées du dépôt | description (format bilingue fusionné `langue nationale \| anglais`, chaque langue ≤120 caractères), topics (20 au maximum, en anglais uniquement, tout en minuscules), branche par défaut, lien About, social preview | metadata-agent | P1 |
| D11 | Complétude de la documentation | Vérification de l'existence de chaque élément de la matrice documentaire | docs-orchestrator | P0/P1 |
| D12 | Qualité de la documentation | Hiérarchie des titres, indication de langage des blocs de code, validité des liens, alt des images, espaces entre chinois et anglais, absence d'espaces réservés | docs-orchestrator | P1/P2 |
| D13 | Page d'accueil README | Positionnement en une phrase, installation, démarrage rapide, badges ≤4, captures d'écran, absence de chemin absolu local | readme-writer | P1 |
| D14 | Gouvernance communautaire | CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, gabarits d'issue, canaux de support | docs-orchestrator | P2 |

## Signification des niveaux

- **P0** : bloque le push.
- **P1** : doit être corrigé avant le push ou impérativement enregistré en tâche à faire.
- **P2** : optimisation recommandée.

## Répartition et consolidation

- Le mode de répartition de chaque dimension est décrit dans le [contrat de répartition des sous-agents](./sub-agent-dispatch-contract.md).
- Les résultats d'évaluation sont consolidés dans la liste des problèmes du [format de rapport d'audit](./audit-report-format.md), chaque entrée devant être accompagnée d'une preuve.
- La base de vérification de D11/D12 figure dans la [matrice documentaire](./document-matrix.md) et dans la [porte qualité](./quality-gate.md).

## Fichiers associés

- Moment d'exécution : Phase 2 du [processus d'exécution](./execution-process.md)
- Conditions de passage de la porte : voir la [porte qualité](./quality-gate.md)
