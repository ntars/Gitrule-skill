# Matrice documentaire

> Problème que ce fichier résout : définir la responsabilité unique de chaque document livrable, les contenus strictement interdits et les contraintes de découpage, afin de garantir un fichier par responsabilité et d'interdire les fusions.

## 1. Fichiers et responsabilités

| Fichier | Responsabilité unique | Strictement interdit |
|---|---|---|
| `README.md` | Page d'accueil : de quoi s'agit-il, comment installer, comment exécuter, où consulter les détails | API intégrale, processus de contribution, journal des modifications |
| `LICENSE` | Texte intégral de la licence | Tout texte explicatif |
| `CHANGELOG.md` | Changements de version destinés aux utilisateurs | Détails de refactorisation interne, plan de développement |
| `CONTRIBUTING.md` | Processus et règles destinés aux contributeurs externes | Description fonctionnelle du projet |
| `CODE_OF_CONDUCT.md` | Code de conduite | Contenu technique |
| `SECURITY.md` | Canal de signalement des vulnérabilités et politique de réponse | Liste des vulnérabilités connues |
| `docs/api.md` | Référence API complète | Tutoriels |
| `docs/architecture.md` | Architecture et frontières des modules | Exemples d'utilisation |
| `docs/naming.md` | Spécification de nommage | Autres spécifications |
| `docs/release.md` | Processus de publication et stratégie de version | Enregistrement des changements |
| `.github/PULL_REQUEST_TEMPLATE.md` | Liste d'autocontrôle de la PR | Présentation du projet |
| `.github/ISSUE_TEMPLATE/*.yml` | Formulaires d'issue structurés | Texte libre |
| `.github/workflows/*.yml` | CI/CD | Documentation explicative |

> Remarque : le corps normatif de `docs/naming.md` figure dans la [spécification de nommage des projets](./project-naming-specification.md) ; le corps normatif de `docs/release.md` figure dans la [spécification de push et de publication](./push-and-release-specification.md).

## 2. Contraintes

- Un fichier dépassant 300 lignes doit être découpé vers `docs/`, le README ne conserve qu'un résumé et un lien.
- Les noms de fichiers sont fixes et en majuscules, les chemins sont fixes, aucune hiérarchie de répertoires ne doit être inventée.
- Chaque document commence par une phrase indiquant « quel problème ce fichier résout » et se termine par des liens croisés vers les fichiers associés.

## Fichiers associés

- La structure en 20 chapitres du README figure dans la [spécification des sections de README](./readme-sections-specification.md)
- La spécification autonome de NOTICE figure dans la [spécification de NOTICE](./notice-specification.md)
- La spécification autonome de LICENSE figure dans la [spécification de LICENSE](./license-specification.md)
- La complétude et la qualité de la documentation relèvent des dimensions D11 et D12, voir la [matrice des dimensions d'audit](./review-dimension-matrix.md)
