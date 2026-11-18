# Lancement de projet et spécification des exigences

> Problème que ce fichier résout : définir les gabarits et champs de l'énoncé d'objectif, de la collecte des exigences et de la délimitation du périmètre en phase de lancement, afin de garantir que le projet dispose dès le départ d'une base claire, vérifiable et traçable.

## 1. Dispositions de la spécification

1. Le document de lancement doit répondre à six questions : ce qu'est le projet, pourquoi le faire, jusqu'où aller, à qui il n'est pas destiné, qui l'utilise, quelles sont les contraintes.
2. Les exigences doivent distinguer trois niveaux : « doit / devrait / peut » ; les conventions de rédaction figurent dans la [spécification de rédaction générale](./general-writing-specification.md).
3. Chaque exigence doit être vérifiable : fournir des conditions d'acceptation sous la forme Given/When/Then, ou un seuil mesurable pouvant être évalué.
4. Chaque exigence doit disposer d'un numéro stable et d'une source ; les entrées d'exigence sans numéro sont interdites.
5. En cas d'information insuffisante, marquer « 【À confirmer : nom du champ】 » ; il est interdit de combler par supposition, les règles figurent dans [Collecte d'informations et gabarits](./information-collection-and-templates.md).
6. Le périmètre doit indiquer simultanément les éléments inclus et les éléments exclus ; des non-objectifs vides signifient un périmètre non délimité.
7. Toute modification du périmètre doit consigner la raison, l'impact et le décideur, et être inscrite dans le registre des modifications de la [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md).

## 2. Gabarit du document de lancement

```markdown
# Dossier de lancement de projet : {{项目名称}}

Version du document : {{v0.1}} ｜ État : {{草稿 / 评审中 / 已批准}} ｜ Décideur : {{姓名}} ｜ Date : {{YYYY-MM-DD}}

## Positionnement en une phrase
Fournir {{目标用户}} à {{核心能力}}, afin de résoudre {{当前痛点}}.
(≤ 60 caractères ; les qualificatifs auto-élogieux du type « puissant », « élégant » ou « leader » sont interdits)

## Contexte et motivation
- Situation actuelle : {{当前如何运作}}
- Insuffisances des solutions existantes : {{具体缺陷 1}} ; {{具体缺陷 2}}
- Fenêtre d'opportunité : {{时机、技术或市场变化}}
- Fondement du lancement : {{工单号 / 访谈记录 / 数据指标，须可溯源}}

## Objectifs et non-objectifs
| Type | Élément | Résultat vérifiable |
| --- | --- | --- |
| Objectif G1 | {{要达成的结果}} | {{可量化指标 + 阈值}} |
| Objectif G2 | {{要达成的结果}} | {{可量化指标 + 阈值}} |
| Non-objectif N1 | {{明确不做的事}} | {{判定边界，说明为何排除}} |

## Critères de réussite
| Indicateur | Référence | Valeur cible | Mode de vérification | Moment de vérification |
| --- | --- | --- | --- | --- |
| {{指标名}} | {{当前值}} | {{目标值}} | {{如何测量}} | {{何时测量}} |

## Utilisateurs cibles
| Rôle utilisateur | Scénario typique | Besoin principal | Solution de substitution actuelle |
| --- | --- | --- | --- |
| {{角色}} | {{何时何地}} | {{要完成的任务}} | {{现用方案}} |

## Contraintes
- Technique : {{语言、平台、兼容性等限制}}
- Temporelle : {{截止日期或窗口}}
- Ressources : {{人力、预算、基础设施}}
- Conformité : {{许可证、隐私、行业规范}}

## Périmètre
- Inclus : {{本期交付项}}
- Exclus : {{本期明确不交付项}}
- À confirmer : {{【待确认：字段名】}}

## Registre des décisions
| Date | Décision | Décideur | Fondement |
| --- | --- | --- | --- |
```

## 3. Gabarit d'entrée d'exigence

```markdown
### REQ-{{三位序号}} : {{需求标题}}

- Source : {{工单号 / 访谈 / 竞品 / 推测}}
- Priorité : {{必须 / 应当 / 可以}}
- Objectif associé : {{G1 / G2 / …}}
- Récit utilisateur : en tant que {{角色}}, je souhaite {{行为}}, afin de {{价值}}
- Conditions d'acceptation :
  1. Given {{前置条件}}
     When {{操作}}
     Then {{预期结果}}
  2. Given {{边界或异常前置条件}}
     When {{操作}}
     Then {{预期结果}}
- État : {{待确认 / 已确认 / 已实现 / 已验证 / 已废弃}}
- Traçabilité associée : {{见需求追踪矩阵中的需求 ID}}
```

## 4. Définition des champs

### 4.1 Champs du dossier de lancement

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Version du document | Oui | Texte | Version sémantique ou version datée | `v0.1` |
| État | Oui | Énumération | Brouillon / en revue / approuvé | `en revue` |
| Décideur | Oui | Texte | Personne disposant du pouvoir de décision final sur le périmètre et les priorités | `Zhang San` |
| Positionnement en une phrase | Oui | Texte | Utilisateurs cibles + capacité clé + difficulté, ≤ 60 caractères | Fournir aux développeurs front-end de… |
| Fondement du lancement | Oui | Texte | Au moins un enregistrement traçable ; « décision de l'équipe » est interdit | `ISSUE-142` |
| Objectifs / non-objectifs | Oui | Tableau | Chaque objectif est associé à un résultat vérifiable ; au moins un non-objectif | `G1 : démarrage à froid < 2 s` |
| Critères de réussite | Oui | Tableau | L'indicateur doit avoir une référence, un seuil, une méthode de mesure et un moment | `taux d'erreur < 0,1 %` |
| Contraintes | Oui | Liste | Les quatre catégories doivent être renseignées ; en l'absence, écrire « aucune » | `doit être compatible avec Node 18+` |
| À confirmer | Non | Liste | Utiliser uniquement le format 【À confirmer : nom du champ】 | `【À confirmer : plafond budgétaire】` |

### 4.2 Champs de l'entrée d'exigence

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Numéro | Oui | `REQ-NNN` | Numéro à trois chiffres, continu, non réutilisé, non réordonné | `REQ-007` |
| Source | Oui | Texte | Traçable jusqu'à un enregistrement précis | `entretien utilisateur n° 3` |
| Priorité | Oui | Énumération | Doit / devrait / peut | `doit` |
| Objectif associé | Oui | Liste | Numéro G correspondant du dossier de lancement | `G1` |
| Récit utilisateur | Oui | Texte | Les trois éléments rôle + comportement + valeur doivent être présents | En tant que… je souhaite… afin de… |
| Conditions d'acceptation | Oui | Liste | Au moins 1 jeu Given/When/Then, incluant un cas limite ou exceptionnel | Voir le gabarit |
| État | Oui | Énumération | L'un des cinq états, progression uniquement sans retour arrière | `confirmé` |

## 5. Instructions de remplissage

1. **Positionnement en une phrase** : rédiger selon la structure en trois segments « pour qui + fournit quoi + résout quoi » ; si la phrase ne tient plus après suppression des qualificatifs, c'est que l'information substantielle manque.
2. **Critères de réussite** : chaque entrée doit présenter à la fois une référence et un seuil. « Améliorer les performances » ou « meilleure expérience » sont jugés non conformes et doivent être reformulés en « temps de démarrage P95 ramené de 3 s à < 1,5 s ».
3. **Non-objectifs** : indiquer le périmètre explicitement exclu et la frontière de décision, et non « à voir plus tard » ; en l'absence de non-objectifs non vides, le périmètre est considéré comme non délimité.
4. **Numéro d'exigence** : une fois attribué, il est définitivement figé ; lorsqu'une exigence est abandonnée, son état passe à « abandonné » et le numéro ne doit être ni recyclé ni réutilisé.
5. **Conditions d'acceptation** : elles doivent couvrir le chemin nominal et au moins un chemin limite ou exceptionnel ; les conditions non objectivement évaluables (comme « interface esthétique ») doivent être converties en mesures ou points de contrôle vérifiables.
6. **Points à confirmer** : le lancement autorise la présence de points à confirmer, mais ils doivent être listés intégralement avec un responsable de confirmation désigné ; ils doivent être soldés avant le passage au développement.

Erreurs fréquentes :

| Formulation erronée | Problème | Mode de correction |
| --- | --- | --- |
| « Faire un outil facile à utiliser » | Aucun utilisateur cible, aucun résultat vérifiable | Ajouter le rôle utilisateur et les indicateurs avec seuil |
| Écrire « aucun » comme non-objectif | Périmètre non délimité, risque de dérive | Lister les éléments explicitement exclus de cette phase |
| Exigence sans numéro, décrite directement dans le corps du texte | Impossibilité de tracer et de référencer | Attribuer `REQ-NNN` et le référencer partout |
| Écrire « fonctionne normalement » comme condition d'acceptation | Non évaluable | Décomposer en Given/When/Then |
| Traiter une supposition comme une exigence établie | Source non traçable | Marquer la source comme « supposition » et la basculer en à confirmer |

## 6. Exemple complet

```markdown
# Dossier de lancement de projet : markdown-lint-cli

Version du document : v0.1 ｜ État : en revue ｜ Décideur : Li Si ｜ Date : 2026-11-18

## Positionnement en une phrase
Fournir aux rédacteurs techniques chinois un outil en ligne de commande de vérification des normes Markdown, afin de résoudre l'incohérence de style documentaire entre plusieurs dépôts et l'absence de validation automatique.

## Contexte et motivation
- Situation actuelle : les README de 12 dépôts sont rédigés à la main par leurs mainteneurs respectifs, avec des styles hétérogènes.
- Insuffisances des solutions existantes : les outils de lint anglais génériques ne prennent pas en charge les règles d'espacement entre chinois et anglais ; la revue manuelle coûte en moyenne 25 minutes par document.
- Fenêtre d'opportunité : l'équipe unifie actuellement sa page d'accueil open source et doit appliquer les normes en une seule fois.
- Fondement du lancement : ISSUE-142, compte rendu de revue documentaire du 2026-11-10.

## Objectifs et non-objectifs
| Type | Élément | Résultat vérifiable |
| --- | --- | --- |
| Objectif G1 | Vérifier automatiquement 8 catégories de problèmes de format | Taux de détection ≥ 95 % sur 50 documents échantillons |
| Objectif G2 | Maîtriser la durée d'une vérification | Vérification d'un document de 1000 lignes < 2 s |
| Non-objectif N1 | Ne pas fournir de polissage du contenu documentaire | Afficher uniquement l'emplacement des règles déclenchées, sans réécrire le texte |

## Critères de réussite
| Indicateur | Référence | Valeur cible | Mode de vérification | Moment de vérification |
| --- | --- | --- | --- | --- |
| Durée de revue manuelle | 25 minutes par document | < 5 minutes par document | Expérience comparative auprès de 5 mainteneurs | Avant la publication v1.0 |

### REQ-001 : Vérifier les espaces dans le texte mixte chinois-anglais
- Source : ISSUE-142
- Priorité : doit
- Objectif associé : G1
- Récit utilisateur : en tant que mainteneur de documentation, je souhaite que les espaces manquants entre chinois et anglais soient signalés automatiquement, afin d'uniformiser la mise en page.
- Conditions d'acceptation :
  1. Given le document contient « 使用Node.js开发 »
     When lancer la vérification
     Then afficher le numéro de ligne et le message « espace manquant entre chinois et anglais »
  2. Given le document comporte déjà un espace à cet endroit
     When lancer la vérification
     Then ne pas signaler de déclenchement de cette règle
- État : confirmé
```

## Fichiers associés

- Traçabilité des exigences vers la conception, les tests et la publication : [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md)
- Champs d'information et marquage des manques : [Collecte d'informations et gabarits](./information-collection-and-templates.md)
- Découpage des phases et conditions d'entrée : [processus d'exécution](./execution-process.md)
- Le nommage intervient après la conclusion du lancement : [spécification de nommage des projets](./project-naming-specification.md)
- Communication externe des modifications de périmètre : [spécification du journal des modifications](./changelog-specification.md)
