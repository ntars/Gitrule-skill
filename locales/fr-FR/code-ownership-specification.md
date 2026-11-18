# Spécification de la propriété du code

> Problème que ce fichier résout : définir la syntaxe du fichier `.github/CODEOWNERS`, l'attribution de la propriété et les règles d'acheminement des revues, afin que chaque changement soit automatiquement assigné à des relecteurs responsables.

## 1. Principes de conception

1. **Correspondance explicite entre chemin et personne** : chaque règle indique qui est responsable d'un chemin, afin d'éviter l'absence de revue ou les revues redondantes.
2. **Owners minimaux nécessaires** : limiter les propriétaires d'un même chemin à 1–3 personnes ; un nombre excessif dilue la responsabilité.
3. **Prise en charge par défaut** : définir un propriétaire global par défaut, couvrant les chemins non appariés par une règle explicite.
4. **Synchronisation avec la structure d'équipe** : mettre à jour dès qu'un membre change, afin qu'un compte invalide ne bloque pas la revue.

## 2. Emplacement du fichier et syntaxe

### 2.1 Chemin

Le fichier `CODEOWNERS` peut être placé à l'un des emplacements suivants, le premier trouvé l'emportant selon la priorité :

1. `CODEOWNERS` à la racine du dépôt ;
2. `docs/CODEOWNERS` ;
3. `.github/CODEOWNERS` (recommandé).

### 2.2 Règles de syntaxe

```text
# 注释以 # 开头
<路径模式>  <所有者>  [<所有者>...]
```

- Une règle par ligne, le motif de chemin est suivi d'un ou plusieurs propriétaires.
- Le format du propriétaire est `@nom-utilisateur` ou `@organisation/équipe`.
- L'usage d'une adresse électronique comme propriétaire doit être associé à un compte GitHub.
- Les chemins sont sensibles à la casse et prennent en charge les jokers `*` et `**`.

### 2.3 Exemple

```text
# 默认所有者
*                       @org/maintainers

# 按目录分配
/src/core/              @org/core-team
/src/api/               @org/api-team @alice
/docs/                  @org/docs-team

# 按文件类型分配
*.md                    @org/docs-team
/.github/workflows/      @org/devops-team
```

## 3. Règles d'appariement

1. Seule la dernière règle correspondante s'applique, sans cumul ; les règles génériques doivent donc figurer en premier et les règles spécifiques ensuite.
2. Une règle de répertoire couvre ce répertoire et ses sous-répertoires, sauf si elle commence par `/` pour restreindre au chemin racine.
3. L'ordre des règles détermine la priorité ; il doit aller du plus large au plus étroit.
4. Les chemins non appariés relèvent de la responsabilité de revue du propriétaire par défaut.

## 4. Stratégie d'attribution de la propriété

| Dimension | Base d'attribution |
| --- | --- |
| Répertoire | Attribution selon les frontières des modules ou sous-systèmes |
| Type de fichier | Documentation, configuration et tests peuvent être attribués uniformément par type |
| Chemins critiques | Sécurité, publication et configuration d'intégration continue réservés aux mainteneurs principaux |
| Nouveaux membres | Participation d'abord comme relecteur non obligatoire, puis passage au statut de propriétaire officiel après familiarisation |

## 5. Lien avec le processus de revue

1. À la création d'une demande de fusion, GitHub demande automatiquement la revue des propriétaires des chemins correspondants.
2. L'exigence de revue obligatoire se configure via les règles de protection de branche, voir la [spécification des workflows Git et des branches](./git-workflow-and-branching-specification.md).
3. Les propriétaires doivent répondre dans le délai convenu ; en cas de dépassement, la prise en charge revient au propriétaire par défaut.
4. Tout changement de propriétaire doit être répercuté dans le fichier, afin qu'un compte invalide ne bloque pas le processus (voir la [spécification de la revue de code](./code-review-specification.md)).

## 6. Exigences de maintenance

1. Réexaminer le fichier après chaque changement d'organisation ou de responsabilités d'équipe.
2. Lors d'un transfert de dépôt ou du départ d'un membre, retirer immédiatement le propriétaire correspondant.
3. Toute modification du fichier doit être relue par au moins un propriétaire existant, afin d'empêcher une diffusion spontanée des droits.
4. Les propriétaires ne doivent pas pointer vers des comptes inactifs ou des comptes de robots (sauf dédiés à l'automatisation).

## 7. Pratiques interdites

1. L'usage de règles génériques trop larges faisant de tout le monde un propriétaire est interdit.
2. L'attribution de chemins sensibles (publication, configuration de secrets) à des membres incapables d'en assurer la revue est interdite.
3. L'écriture de coordonnées personnelles dans le fichier est interdite.
4. Le maintien à long terme du statut de propriétaire de membres partis est interdit.

## Fichiers associés

- Périmètre de responsabilité des fichiers : [matrice documentaire](./document-matrix.md)
- Critères et responsabilités de revue : [spécification de la revue de code](./code-review-specification.md)
- Protection des branches : [spécification des workflows Git et des branches](./git-workflow-and-branching-specification.md)
- Les vérifications automatisées relèvent de la dimension D9 : [matrice des dimensions de revue](./review-dimension-matrix.md)
