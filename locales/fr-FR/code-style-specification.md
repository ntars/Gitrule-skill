# Spécification de style de code

> Problème que ce fichier résout : définir le gabarit de configuration du style de code, le tableau des conventions de nommage, les règles de commentaires et les instructions de remplissage, afin de réduire les divergences de style et d'améliorer la lisibilité et l'efficacité de la revue.

## 1. Dispositions de la spécification

1. Les règles de style s'appuient sur des outils automatisés ; le traitement manuel ne concerne que les parties non couvertes par les outils.
2. La configuration de formatage doit être versionnée avec le dépôt (par exemple le fichier de configuration du formateur), afin de garantir l'homogénéité entre environnements.
3. La CI doit intégrer la vérification du formatage ; en cas d'échec, la fusion est interdite (voir la [spécification des tests](./testing-specification.md)).
4. L'usage de nombres magiques et de constantes codées en dur est interdit ; ils doivent être extraits en constantes nommées.
5. Les fins de ligne sont uniformément en LF et le fichier se termine par un saut de ligne (correspond à la dimension D3, hygiène du dépôt).

## 2. Gabarit de configuration de style

```markdown
# Conventions de style de code : {{项目名称}}

Version de la configuration : {{v1.0}} ｜ Langage et version applicables : {{如 TypeScript 5.x}} ｜ Outil de formatage : {{如 Prettier 3.x}}

## Règles de formatage (imposées par l'outil)
| Règle | Valeur | Option de configuration de l'outil | Négociable |
| --- | --- | --- | --- |
| Indentation | {{2 空格 / 4 空格 / Tab}} | {{配置项名}} | Non |
| Largeur de ligne | {{100 字符}} | {{配置项名}} | Non |
| Guillemets | {{单引号 / 双引号}} | {{配置项名}} | Non |
| Fin de ligne | LF | `endOfLine: lf` | Non |
| Saut de ligne en fin de fichier | Obligatoire | Valeur par défaut de l'outil | Non |
| Point-virgule | {{有 / 无}} | {{配置项名}} | Non |

## Conventions de nommage (non imposables par l'outil, revue manuelle)
| Objet | Règle | Bon exemple | Contre-exemple |
| --- | --- | --- | --- |
| Variable | {{camelCase}} | `userName` | `UserName` |
| Constante | {{UPPER_SNAKE_CASE}} | `MAX_RETRY` | `maxRetry` |
| Fonction | {{动词开头 camelCase}} | `parseConfig` | `configParse` |
| Classe / type | {{PascalCase}} | `ConfigLoader` | `config_loader` |
| Nom de fichier | {{kebab-case}} | `config-loader.ts` | `ConfigLoader.ts` |
| Valeur booléenne | {{is/has/can 前缀}} | `isValid` | `valid` |
| Collection | {{复数名词}} | `items` | `itemList` |

## Règles de commentaires
- Cas où un commentaire est obligatoire : {{公开 API 的契约、非直观算法、绕开限制的临时方案}}
- Commentaires interdits : {{复述代码、无信息量、失效的旧注释、情绪化表述}}
- Langue des commentaires : {{与项目主语言一致}}
- Format des TODO : `// TODO({{负责人}}): {{事项}} — {{计划版本}}`

## Organisation des fichiers
1. Ordre des imports : {{标准库 → 第三方 → 本地模块，组内字典序}}
2. Ordre des déclarations : {{常量 → 类型 → 函数 → 导出}}
3. Nombre maximal de lignes par fichier : {{300 行，超出须拆分}}

## Liste des exceptions
| Cas | Règle d'exception | Approbateur | Validité |
| --- | --- | --- | --- |
| {{如生成代码}} | {{不参与格式化}} | {{姓名}} | {{至 v2.0}} |
```

## 3. Définition des champs de configuration

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Version de la configuration | Oui | Texte | Incrémentée à chaque modification des règles de style | `v1.0` |
| Langage et version applicables | Oui | Texte | Préciser la version majeure pour éviter la dérive des règles | `TypeScript 5.x` |
| Outil de formatage | Oui | Texte | Conforme à la version du lockfile | `Prettier 3.2` |
| Règle.Valeur | Oui | Énumération / valeur numérique | Doit être unique ; « cela dépend » est interdit | `2 espaces` |
| Négociable | Oui | Énumération | Non / oui ; en cas de « oui », préciser les conditions de négociation | `Non` |
| Bon exemple de nommage | Oui | Code | Choisi dans le code existant du projet | `parseConfig` |
| Contre-exemple de nommage | Oui | Code | Doit être une écriture réellement fréquente | `configParse` |
| Responsable du TODO | Oui | Texte | Écrire « équipe » est interdit | `Zhang San` |
| Validité de l'exception | Oui | Version / date | Réexamen obligatoire à l'échéance | `jusqu'à v2.0` |

## 4. Instructions de remplissage

1. **Priorité à l'outil** : toute règle imposable par un outil est inscrite dans la configuration de formatage et ne repose pas sur la mémoire humaine ; le manuel ne traite que le nommage, les commentaires et l'organisation des fichiers.
2. **Valeur de largeur de ligne** : elle doit être définie en fonction de la largeur de l'interface de revue, généralement 100 ou 120 ; une fois fixée, elle ne doit pas être contournée dans des fichiers isolés.
3. **Bon exemple de nommage** : choisir un nom réellement présent dans le code existant du projet ; l'usage d'espaces réservés de manuel est interdit.
4. **Nommage booléen** : les préfixes `is`/`has`/`can` doivent être cohérents avec la sémantique ; `isReady` ne doit pas désigner une action.
5. **TODO** : doit contenir le responsable, l'élément et la version prévue ; un TODO sans plan ne doit pas entrer dans la branche principale.
6. **Liste des exceptions** : chaque exception doit avoir un approbateur et une durée de validité ; sans réexamen à l'échéance, elle devient automatiquement caduque.

Erreurs fréquentes :

| Formulation erronée | Problème | Mode de correction |
| --- | --- | --- |
| « Garder le code aussi concis que possible » | Non évaluable | Remplacer par une règle vérifiable, par exemple une limite de longueur de fonction |
| Tableau de nommage sans contre-exemple | Impossible de comparer lors de la revue | Ajouter des contre-exemples réellement fréquents |
| Commentaire « il y avait un bug ici avant » | Sans information et vite obsolète | Décrire le comportement actuel et sa raison |
| TODO sans responsable | Aucun suivi | Ajouter le responsable et la version prévue |
| Exception sans durée de validité | Exemption permanente | Ajouter la durée de validité et le responsable du réexamen |

## 5. Exemple complet

```markdown
# Conventions de style de code : markdown-lint-cli

Version de la configuration : v1.0 ｜ Langage et version applicables : TypeScript 5.x ｜ Outil de formatage : Prettier 3.2

## Règles de formatage (imposées par l'outil)
| Règle | Valeur | Option de configuration de l'outil | Négociable |
| --- | --- | --- | --- |
| Indentation | 2 espaces | `tabWidth: 2` | Non |
| Largeur de ligne | 100 caractères | `printWidth: 100` | Non |
| Guillemets | Guillemets simples | `singleQuote: true` | Non |
| Fin de ligne | LF | `endOfLine: lf` | Non |
| Point-virgule | Avec | `semi: true` | Non |

## Conventions de nommage (revue manuelle)
| Objet | Règle | Bon exemple | Contre-exemple |
| --- | --- | --- | --- |
| Fonction | camelCase commençant par un verbe | `parseRules` | `rulesParser` |
| Constante | UPPER_SNAKE_CASE | `DEFAULT_RULES` | `defaultRules` |
| Nom de fichier | kebab-case | `rule-loader.ts` | `RuleLoader.ts` |

## Règles de commentaires
- Cas où un commentaire est obligatoire : la sémantique de correspondance des règles, le contournement du comportement d'une API amont.
- Commentaires interdits : reformulation du code, « correction d'un bug », TODO sans responsable.
- Format des TODO : `// TODO(Wang Wu): remplacer l'analyseur temporaire — v2.0`

## Liste des exceptions
| Cas | Règle d'exception | Approbateur | Validité |
| --- | --- | --- | --- |
| Répertoire fixtures | Exclu du formatage | Li Si | Jusqu'à v2.0 |
```

## Fichiers associés

- Base des contrôles de revue de code : [spécification de revue de code](./code-review-specification.md)
- La vérification du formatage s'exécute dans la CI : [spécification des tests](./testing-specification.md), [spécification du flux de travail CI](./ci-workflow-specification.md)
- L'hygiène du dépôt relève de la dimension D3 : [matrice des dimensions d'audit](./review-dimension-matrix.md)
- Contrôles avant commit : [spécification de push et de publication](./push-and-release-specification.md)
- Traçabilité des exigences vers l'implémentation : [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md)
