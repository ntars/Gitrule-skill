# Spécification du journal des modifications

> Problème que ce fichier résout : définir le gabarit, les champs et les règles de rédaction du journal des modifications destiné aux utilisateurs, afin de garantir que chaque changement est traçable, que chaque version peut être associée et que le chemin de mise à niveau peut être déterminé.

## 1. Dispositions normatives

1. Le journal des modifications suit la structure Keep a Changelog, et les numéros de version suivent le versionnage sémantique de la [spécification de gestion des versions](./version-management-specification.md).
2. Chaque version doit comporter une date de publication, au format `YYYY-MM-DD` ; les contenus non publiés sont placés dans la section `Unreleased`.
3. Les entrées sont regroupées en six catégories : `Added` ajout / `Changed` modification / `Deprecated` dépréciation / `Removed` suppression / `Fixed` correction / `Security` sécurité.
4. Chaque changement est destiné à l'utilisateur, doit préciser l'impact et le mode de migration, et ne doit pas décrire de détails de refactorisation interne.
5. Un changement cassant doit être marqué `BREAKING CHANGE:` et accompagné des étapes de migration (voir la [spécification de guide de migration](./migration-guide-specification.md)).
6. Le numéro de version doit être cohérent avec le tag et les Release Notes ; un changement cassant doit correspondre à `feat!:` ou `BREAKING CHANGE:` dans le message de commit.

## 2. Gabarit du journal des modifications

```markdown
# Journal des modifications

Ce fichier enregistre tous les changements destinés aux utilisateurs. Le format suit Keep a Changelog, les versions respectent le versionnage sémantique.

## [Unreleased]

### Added
- {{新增能力，说明对使用者的价值}}

### Changed
- {{行为变更，说明影响范围}}

### Deprecated
- {{即将移除的能力，说明替代方案与移除版本}}

### Removed
- {{已移除的能力，说明迁移路径}}

### Fixed
- {{缺陷修复，说明触发条件}}

### Security
- {{安全修复，说明影响与升级建议}}

## [{{X.Y.Z}}] - {{YYYY-MM-DD}}

### {{类型}}
- {{变更条目}}
- {{BREAKING CHANGE: 原行为 → 新行为；迁移步骤见链接}}

[Unreleased]: https://github.com/{{owner}}/{{repo}}/compare/v{{X.Y.Z}}...HEAD
[{{X.Y.Z}}]: https://github.com/{{owner}}/{{repo}}/compare/v{{prev}}...v{{X.Y.Z}}
```

## 3. Gabarit d'entrée

```markdown
- {{动词开头的一句话变更描述}}（{{关联 REQ 编号}}）
  - 影响：{{哪些使用者或场景受影响}}
  - 迁移：{{需要执行的动作；无则省略此行}}
  - 参考：{{Issue / PR 链接}}
```

## 4. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Numéro de version | Oui | `X.Y.Z` | Strictement identique au tag, le préfixe `v` est toléré mais l'usage doit être unifié dans tout le document | `1.2.0` |
| Date de publication | Oui | `YYYY-MM-DD` | Correspond à la date de pose du tag | `2026-11-18` |
| Type de regroupement | Oui | Énumération | L'une des six catégories ; si aucune entrée de ce type n'existe, la section entière est omise | `Fixed` |
| Description du changement | Oui | Texte | Commence par un verbe, orientée utilisateur, précise la valeur apportée | `Ajout de la vérification des tableaux GFM` |
| Impact | Obligatoire sous condition | Texte | Obligatoire en cas de changement de comportement, de dépréciation, de suppression ou de changement cassant | `L'ancien fichier de configuration doit être renommé` |
| Migration | Obligatoire sous condition | Texte | Obligatoire en cas de changement cassant, pointe vers le guide de migration | `Voir le guide de migration v1.0` |
| BREAKING CHANGE | Obligatoire sous condition | Marqueur | Obligatoire en cas de changement cassant, placé en tête de l'entrée | `BREAKING CHANGE:` |
| Lien de comparaison | Oui | URL | Chaque section de version doit fournir un lien compare | `compare/v1.1.0...v1.2.0` |
| REQ rattachée | Non | Liste | Facilite le rapprochement avec la matrice de traçabilité des exigences | `REQ-007` |

## 5. Instructions de saisie

1. **Granularité des entrées** : un changement décrit un seul résultat perceptible par l'utilisateur ; plusieurs résultats sont scindés en plusieurs entrées.
2. **Commencement par un verbe** : utiliser « ajout », « prise en charge », « correction », « suppression », « dépréciation », « ajustement », et non « a mis à jour », « quelques modifications ».
3. **Contenus interdits** : entrées sans date, refactorisation interne, plan de développement, contenu de feuille de route, formulations vagues (« optimisation de l'expérience », « correction de plusieurs problèmes »).
4. **Changements cassants** : doivent réunir simultanément le marqueur `BREAKING CHANGE:`, la description de l'impact, les étapes de migration et le lien vers le guide de migration, les quatre étant indissociables.
5. **Éléments dépréciés** : doivent indiquer la solution de remplacement et le numéro de version de suppression prévue, par exemple « sera supprimé en v2.0 ».
6. **Unreleased** : enregistrer dès la fusion, sans accumuler pour compléter le jour de la publication.
7. **Cohérence** : le numéro de version et la date de publication doivent être cohérents avec le tag, les Release Notes et l'enregistrement de déploiement ; en cas d'incohérence, le tag fait foi et les trois autres sont corrigés.

Erreurs courantes :

| Rédaction erronée | Problème | Mode de correction |
| --- | --- | --- |
| « Refactorisation de la structure interne des modules » | Relève des détails internes, invisible pour l'utilisateur | Supprimer ou reformuler en effet perceptible |
| « Correction de plusieurs problèmes » | Non évaluable | Énumérer chaque correction |
| Changement cassant mentionnant seulement « il y a des changements » | Absence de chemin de migration | Ajouter l'impact, les étapes de migration et le lien vers le guide |
| Numéro de version incohérent avec le tag | Rupture de la correspondance des versions | Unifier en se référant au tag |
| Absence de lien compare | Impossible de consulter les différences | Ajouter l'URL compare GitHub |

## 6. Exemple complet

```markdown
## [1.0.0] - 2026-11-20

### Added
- Ajout de la règle de vérification des espaces entre caractères chinois et anglais (REQ-001), avec prise en charge de l'appel direct en ligne de commande.
- Ajout de la sortie de rapport JSON, facilitant l'intégration aux statistiques CI.

### Changed
- BREAKING CHANGE: le nom du fichier de configuration passe de `.mdlint.json` à `.mdlintrc.json`. L'ancien fichier n'est plus lu ; les étapes de migration figurent dans le [guide de migration](./migration-guide-specification.md).

### Deprecated
- Le paramètre `--format=table` sera supprimé en v2.0, veuillez utiliser `--reporter=table`.

### Fixed
- Correction d'un faux positif lorsque la ponctuation chinoise est adjacente à un mot anglais.

### Security
- Correction d'un problème où le chemin de chargement des plugins de règles pouvait être écrasé par une entrée externe ; il est recommandé à tous les utilisateurs de mettre à niveau vers v1.0.0.

[1.0.0]: https://github.com/example/markdown-lint-cli/compare/v0.9.3...v1.0.0
```

## Fichiers associés

- Règles d'incrémentation des versions : [spécification de gestion des versions](./version-management-specification.md)
- Documentation de migration des changements cassants : [spécification de guide de migration](./migration-guide-specification.md)
- Frontières de responsabilité documentaire : [matrice documentaire](./document-matrix.md)
- Marqueurs de rupture dans les messages de commit : [spécification de message de commit](./commit-message-specification.md)
- Section du journal des modifications dans le README : [spécification des sections de README](./readme-sections-specification.md)
- tag et Release Notes : [spécification de push et de publication](./push-and-release-specification.md)
