# Spécification des messages de commit

> Problème que ce fichier résout : définir les champs, le format, les instructions de rédaction et les exemples de Conventional Commits, afin de garantir un historique lisible et la génération automatique du journal des modifications et des numéros de version.

## 1. Format

```text
<类型>[可选作用域][可选 !]: <描述>

[可选正文]

[可选脚注]
```

## 2. Types

Les dix types complets ci-dessous couvrent les cas de commit des projets open source courants :

| Type | Signification |
| --- | --- |
| `feat` | Ajout de fonctionnalité |
| `fix` | Correction de défaut |
| `docs` | Modification de la documentation |
| `style` | Ajustement de forme sans changement de logique (espaces, formatage, point-virgule manquant, etc.) |
| `refactor` | Refactorisation, sans ajout de fonctionnalité ni correction de défaut |
| `perf` | Modification du code améliorant les performances |
| `test` | Ajout de tests manquants ou correction de tests existants |
| `build` | Modification affectant le système de build ou les dépendances externes (par exemple npm, gulp) |
| `ci` | Modification de la configuration et des scripts d'intégration continue (par exemple GitHub Actions, CircleCI) |
| `chore` | Tâches diverses : build, dépendances, chaîne d'outils, etc. |

### 2.1 Comparaison et arbitrage des conventions d'équipe

Selon le mode de collaboration, trois conventions courantes existent ; le projet doit en choisir une au lancement et l'unifier pour toute l'équipe :

| Convention | Format | Adaptée à | Limites |
| --- | --- | --- | --- |
| Convention de travail | `[numéro de carte] auteur : contenu de la modification` | Équipes utilisant un tableau kanban et la programmation en binôme | Dépend du système de numéros de cartes, inapplicable sans numéro |
| Convention classique | `[catégorie] composant (facultatif) : contenu de la modification` | Équipes devant filtrer l'historique par module métier | Nécessite une table de catégories convenue, coût supplémentaire |
| Convention open source | `<type>(<scope>): <subject>` | Bibliothèques et applications open source nécessitant une génération automatique du CHANGELOG | Nombreux types et portées, coût d'apprentissage plus élevé |

Ce projet adopte uniformément la convention open source (c'est-à-dire Conventional Commits), pour la raison suivante : lisibilité par machine, génération automatique du journal des modifications et des numéros de version. Les conventions de travail et classique ne s'utilisent que par accord dans les équipes à code fermé et ne doivent pas être introduites dans les dépôts publics.

## 3. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Type | Oui | Énumération | L'un des dix types, aucune création libre | `feat` |
| Portée | Non | Texte | Nom de module, mot court en minuscules, sans espace | `parser` |
| Marqueur de rupture | Non | `!` | Placé après le type ou la portée, avant les deux-points | `feat!:` |
| Description | Oui | Texte | Mode impératif, minuscule initiale, ≤ 72 caractères, sans point final | `add TOML config support` |
| Corps | Non | Texte | Explique la motivation et la mise en œuvre, séparé de la description par une ligne vide | `Allow the parser to read TOML...` |
| Pied de page | Non | Texte | `BREAKING CHANGE:` ou `Refs: #N` | `BREAKING CHANGE: ...` |
| Exigence rattachée | Non | `REQ-NNN` | Inscrite dans le corps ou le pied de page, pour faciliter la traçabilité | `Refs: REQ-001` |

## 4. Instructions de rédaction

1. **Description** : utilisez le mode impératif (add, fix, remove) et décrivez « ce qui a été fait » plutôt que « une modification a été faite » ; pour un projet en chinois, une description en chinois est possible, mais elle doit être unifiée sur tout le dépôt.
2. **Portée** : prendre le nom du module et non le nom de fichier ; pour un changement inter-modules, omettre la portée, sans écrire `all` ou `global`.
3. **Corps** : ne l'écrire que si la description ne suffit pas à expliquer la motivation ; ne pas répéter la description, ne pas tenir un journal d'étapes.
4. **Changement incompatible** : `feat!:` / `fix!:` et le pied de page `BREAKING CHANGE:` s'emploient au choix ou conjointement ; lorsque l'un des deux apparaît, il faut l'inscrire simultanément dans la [spécification du journal des modifications](./changelog-specification.md) et la [spécification du guide de migration](./migration-guide-specification.md).
5. **Atomicité** : un commit ne fait qu'une seule chose ; le formatage et le changement de logique font l'objet de deux commits distincts.
6. **Sécurité** : ne doivent figurer ni clés, ni jetons, ni données personnelles, ni adresses internes ; vérifiez par un scan de clés avant de committer (voir la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)).
7. **Lien avec les versions** : `feat` déclenche l'incrément de version mineure, `fix` celui de version corrective, `BREAKING CHANGE` celui de version majeure ; voir la [spécification de gestion des versions](./version-management-specification.md).

Erreurs fréquentes :

| Formulation erronée | Problème | Correction |
| --- | --- | --- |
| `wip`, `update`, `fix bug` | Aucune information utile, violation de H10 | Préciser l'objet et l'action |
| `feat: Added new feature.` | Non impératif, majuscule initiale, point final | `feat: add config loader` |
| `feat(tous): optimisation` | Portée invalide, description vague | Utiliser un nom de module précis et décrire la modification |
| Un même commit contient formatage et changement fonctionnel | Rupture de l'atomicité | Scinder en deux commits `style:` et `feat:` |
| Le message de commit contient une adresse intranet | Fuite d'information | La retirer et passer par le scan de clés |

## 5. Exemple complet

```text
feat(parser): add support for TOML config

Allow the parser to read TOML configuration files in addition to YAML.
Refs: REQ-001

BREAKING CHANGE: the `config` option now accepts a file path instead of an object.
```

Signification des champs : `feat` est le type, `parser` la portée, le texte après les deux-points la description courte ; le corps expose la motivation et la mise en œuvre, le pied de page rattache l'exigence ; le pied de page final déclare le changement incompatible et indique la direction de migration.

Exemple de correction :

```text
fix(spacing): avoid false positives before Chinese punctuation

The spacing rule previously flagged strings such as 「使用Node.js，」 because
the punctuation check ran after whitespace normalization.

Refs: REQ-004, #142
```

## Fichiers associés

- La revue de l'historique des commits relève de la dimension D7 : [matrice des dimensions de revue](./review-dimension-matrix.md)
- Génération du journal des modifications : [spécification du journal des modifications](./changelog-specification.md)
- Base de l'incrément de version : [spécification de gestion des versions](./version-management-specification.md)
- Points de contrôle de la revue de code : [spécification de la revue de code](./code-review-specification.md)
- Traçabilité des exigences : [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md)
