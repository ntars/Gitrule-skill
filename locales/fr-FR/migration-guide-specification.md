# Spécification du guide de migration

> Problème que ce fichier résout : définir la structure, les éléments de contenu et le moment de publication du guide de migration en cas de changement incompatible, afin que les utilisateurs puissent passer progressivement de l'ancienne version à la nouvelle en suivant des étapes.

## 1. Conditions de déclenchement

Un guide de migration doit être fourni dans l'un des cas suivants :

1. Le message de commit contient `BREAKING CHANGE:` ou `feat!:` / `fix!:` (voir la [spécification des messages de commit](./commit-message-specification.md)).
2. Le nom d'une clé de configuration, sa valeur par défaut ou sa priorité change.
3. La signature d'une API, la structure de retour ou les codes d'erreur changent.
4. La version minimale d'exécution est relevée, ou une plateforme n'est plus prise en charge.
5. La structure des répertoires ou le nommage des fichiers change, affectant les chemins de référence des utilisateurs.

## 2. Emplacement et nommage des fichiers

1. Les indications de migration de faible ampleur sont intégrées à l'entrée de la version correspondante dans `CHANGELOG.md`.
2. En cas de changement important impliquant plusieurs étapes, créer un fichier distinct dans le répertoire `docs/migration/`, nommé par version, par exemple `docs/migration/v2.md`.
3. Le parcours de migration complet entre versions majeures est indexé dans `docs/migration/README.md`.
4. Le README ne contient que l'annonce de migration et le lien, sans détailler les étapes (voir la [matrice documentaire](./document-matrix.md)).

## 3. Structure du document

Le guide de migration doit être organisé dans l'ordre suivant :

1. **Titre et versions** : indiquer la version source et la version cible, par exemple « Migration de v1.x vers v2.0 ».
2. **Vue d'ensemble des impacts** : énumérer les catégories de changements et leur périmètre d'impact, en précisant quels utilisateurs doivent migrer.
3. **Prérequis** : préparatifs à effectuer avant la migration, tels que la sauvegarde et la mise à niveau de la version de l'environnement.
4. **Liste des changements** : énumérer un à un les changements incompatibles, chacun comprenant « ancien comportement », « nouveau comportement » et « motif du changement ».
5. **Étapes de migration** : énumérer de manière numérotée les opérations exécutables, en fournissant les commandes ou des exemples de code.
6. **Méthode de vérification** : comment confirmer la réussite après la migration, en fournissant la commande de contrôle ou la sortie attendue.
7. **Méthode de restauration** : comment revenir à l'ancienne version en cas d'échec de la migration.
8. **Questions fréquentes** : énumérer les questions récurrentes et leurs réponses.
9. **Obtenir de l'aide** : renvoyer vers les issues, le forum de discussion ou le site de documentation.

### 3.1 Gabarit vierge copiable

Le gabarit suivant correspond point par point aux neuf éléments de structure de la section 3 ; il suffit de le copier et de remplacer les espaces réservés pour l'utiliser :

````markdown
# Migration de {{源版本}} vers {{目标版本}}

> Ce guide décrit l'ensemble des opérations nécessaires pour passer de {{源版本}} à {{目标版本}} ; il s'adresse à {{适用使用者范围}}.

## 1. Vue d'ensemble des impacts

| Catégorie de changement | Contenu précis | Périmètre d'impact | Migration obligatoire |
| --- | --- | --- | --- |
| {{变更类别}} | {{变更内容}} | {{受影响的使用者场景}} | {{是否必须迁移}} |

## 2. Prérequis

- {{前置准备}}
- {{检查项与确认命令}}

## 3. Liste des changements

### {{变更项名称}}

- Ancien comportement : {{旧版本行为}}
- Nouveau comportement : {{新版本行为}}
- Motif du changement : {{变更原因}}

Avant la migration :

```{{代码语言}}
{{旧配置或旧代码}}
```

Après la migration :

```{{代码语言}}
{{新配置或新代码}}
```

## 4. Étapes de migration

1. {{迁移步骤}}
2. {{迁移步骤}}
3. {{人工处理步骤}}

## 5. Méthode de vérification

```bash
{{可独立运行的检查命令}}
```

Sortie attendue : {{预期结果}}

## 6. Méthode de restauration

1. {{恢复旧版本的操作}}
2. {{恢复旧配置的操作}}

## 7. Questions fréquentes

### {{问题}}

Réponse : {{解答}}

## 8. Obtenir de l'aide

- Remontée de problèmes : {{issue 地址}}
- Forum de discussion : {{讨论区地址}}
- Documentation associée : {{文档链接}}
````

Correspondance des espaces réservés :

| Espace réservé | Obligatoire | Points de saisie |
| --- | --- | --- |
| `{{源版本}}` / `{{目标版本}}` | Oui | Identiques au tag cible, format `vX.Y.Z` |
| `{{适用使用者范围}}` | Oui | Préciser quels utilisateurs doivent migrer, éviter les formulations vagues |
| `{{变更类别}}` | Oui | Au moins une des quatre catégories : configuration, API, exécution, répertoires |
| `{{是否必须迁移}}` | Oui | Préciser si ce changement impose à l'utilisateur d'effectuer la migration |
| `{{旧行为}}` / `{{新行为}}` | Oui | Mise en regard point par point, sans n'écrire qu'un seul côté |
| `{{代码语言}}` | Oui | Identifiant de langage du bloc de code, par exemple `yaml`, `json`, `js` |
| `{{前置准备}}` | Oui | Sauvegarde et vérifications d'environnement à effectuer avant la migration |
| `{{迁移步骤}}` | Oui | Chaque étape directement exécutable, avec commande ou code |
| `{{人工处理步骤}}` | Oui | Les étapes non automatisables doivent être explicitement signalées ici |
| `{{检查命令}}` / `{{预期结果}}` | Oui | Commande exécutable de manière autonome, résultat déterminable |
| `{{回滚方式}}` | Oui | Ne doit pas être omis, voir les pratiques interdites de la section 7 |

## 4. Exigences de contenu

### 4.1 Exemple de mise en regard des changements

```markdown
### La clé de configuration `timeout` devient `timeoutMs`

- Ancien comportement : utiliser `timeout: 5000` dans le fichier de configuration, l'unité étant la seconde.
- Nouveau comportement : utiliser désormais `timeoutMs: 5000`, l'unité étant la milliseconde.
- Motif du changement : unifier l'unité de temps afin d'éviter une incohérence avec les paramètres de l'API.

Avant la migration :

```yaml
timeout: 5
```

Après la migration :

```yaml
timeoutMs: 5000
```

### 4.2 Exigences de rédaction

1. Chaque étape fournit une commande ou du code directement exécutable ; il est interdit de se limiter à « modifier la configuration ».
2. Fournir une mise en regard avant et après la migration, afin de faciliter la vérification point par point.
3. Signaler explicitement les étapes non automatisables nécessitant une intervention manuelle.
4. Le périmètre d'impact doit être précis ; éviter les formulations vagues du type « peut affecter certains utilisateurs ».
5. La commande de vérification doit pouvoir être exécutée de manière autonome et comporter la sortie attendue.

## 5. Moment de publication et liens

1. Le guide de migration doit être publié en même temps que la version contenant le changement incompatible, sans retard.
2. L'entrée correspondante de `CHANGELOG.md` doit renvoyer au guide de migration (voir la [spécification du journal des modifications](./changelog-specification.md)).
3. Le bloc réservé aux changements incompatibles du gabarit de PR doit inviter à renseigner la méthode de migration (voir la [spécification des gabarits Issue et PR](./issue-and-pr-template-specification.md)).
4. Le numéro de version suit le versionnage sémantique ; un changement incompatible doit incrémenter la version majeure (voir la [spécification de gestion des versions](./version-management-specification.md)).
5. Le README signale à un emplacement bien visible aux utilisateurs d'anciennes versions de lire le guide de migration.

## 6. Politique de dépréciation et de conservation

1. Le guide de migration doit être conservé à long terme et ne doit pas être supprimé après la publication d'une nouvelle version.
2. La documentation des anciennes versions peut être marquée « plus maintenue », mais son point d'entrée doit être conservé.
3. Une mise à niveau franchissant plusieurs versions majeures doit fournir un parcours progressif et ne doit pas exiger de franchir tous les changements en une seule fois.

## 7. Pratiques interdites

1. Il est interdit de se limiter à « il y a des changements incompatibles, veuillez ajuster vous-même ».
2. Il est interdit d'omettre la méthode de restauration.
3. Il est interdit d'utiliser dans les étapes de migration du pseudo-code non exécutable.
4. Il est interdit de supprimer les guides de migration des versions historiques.

## Fichiers associés

- Structure du journal des modifications : voir la [spécification du journal des modifications](./changelog-specification.md)
- Règles d'incrémentation des versions : voir la [spécification de gestion des versions](./version-management-specification.md)
- Déclaration de changement incompatible dans le message de commit : voir la [spécification des messages de commit](./commit-message-specification.md)
- Limites de responsabilité documentaire : voir la [matrice documentaire](./document-matrix.md)
- Processus de publication : voir la [spécification de push et de publication](./push-and-release-specification.md)
