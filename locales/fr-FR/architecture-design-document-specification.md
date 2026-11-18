# Spécification du document de conception d'architecture

> Problème que ce fichier résout : définir les gabarits, champs et modes de rédaction du document d'architecture et des décisions d'architecture (ADR), exposer les frontières du système, les responsabilités des modules, les attributs de qualité et les arbitrages clés, et garantir la traçabilité des décisions.

## 1. Dispositions de la spécification

1. Le document d'architecture (`docs/architecture.md`) ne décrit que la structure et les frontières, sans exemples d'utilisation ; la frontière des responsabilités est définie dans la [matrice documentaire](./document-matrix.md).
2. Chaque décision technique majeure doit disposer d'une ADR correspondante ; une décision sans ADR est considérée comme non consignée.
3. Les numéros d'ADR sont continus et définitivement figés ; une fois adoptée, une ADR ne réécrit jamais l'historique, et un changement d'état est consigné par une nouvelle ADR portant la mention « remplacée ».
4. La description de l'architecture doit rester cohérente avec l'implémentation du code ; en cas d'incohérence entre le code et la documentation, le code fait foi et la documentation est corrigée immédiatement.
5. Chaque décision d'architecture doit pouvoir être rattachée à une ou plusieurs exigences ; la relation de traçabilité est décrite dans la [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md).
6. Les attributs de qualité doivent fournir des objectifs mesurables et vérifiables ; il est interdit d'écrire seulement « hautes performances » ou « haute disponibilité ».

## 2. Gabarit du document d'architecture

```markdown
# Conception d'architecture : {{项目名称}}

Version du document : {{v1.0}} ｜ Version de code correspondante : {{tag}} ｜ Date de dernière vérification : {{YYYY-MM-DD}}

## Contexte système
- Responsabilité du système : {{一句话说明系统边界内的责任}}
- Acteurs externes : {{用户、上游系统、下游系统}}
- Entrées et sorties : {{进入系统的请求与系统产出的结果}}
- Hors frontières : {{明确不由本系统承担的职责}}

## Découpage des modules
| Module | Responsabilité unique | Interface externe | Modules dépendants | Non responsable de |
| --- | --- | --- | --- | --- |
| {{模块名}} | {{仅一件事}} | {{接口名}} | {{模块名}} | {{明确排除}} |

## Flux de données clés
1. {{触发点}} → {{模块 A}} : {{传递的数据}}
2. {{模块 A}} → {{模块 B}} : {{转换与传递}}
3. {{模块 B}} → {{结果}} : {{最终产出}}

## Choix technologiques
| Domaine | Choix | Alternatives | Fondement de la décision | ADR |
| --- | --- | --- | --- | --- |
| {{语言 / 框架 / 存储}} | {{采用项}} | {{未采用项}} | {{取舍理由}} | {{ADR-000N}} |

## Attributs de qualité
| Attribut | Valeur cible | Mode de vérification | ADR associée |
| --- | --- | --- | --- |
| Performance | {{P95 延迟 < X ms}} | {{压测方式}} | {{ADR-000N}} |
| Disponibilité | {{月度可用性 ≥ X%}} | {{监控统计}} | {{ADR-000N}} |
| Sécurité | {{敏感数据零明文落盘}} | {{审计方式}} | {{ADR-000N}} |
| Extensibilité | {{横向扩容至 N 节点无需改代码}} | {{扩容演练}} | {{ADR-000N}} |

## Contraintes et arbitrages
- Contraintes techniques : {{语言版本、平台、兼容性}}
- Solutions abandonnées et raisons : {{方案 A：原因}}
- Dette technique connue : {{债务项与偿还条件}}
```

## 3. Gabarit d'ADR

```markdown
# ADR-{{四位序号}} : {{决策标题}}

- État : {{提议 / 已采纳 / 已废弃 / 被 ADR-000N 替代}}
- Date : {{YYYY-MM-DD}}
- Décideur : {{姓名}}
- Exigences associées : {{REQ-001 / …}}

## Contexte
{{面临的客观问题与约束，须可验证，不写主观偏好}}

## Décision
{{采用的方案，一句话陈述，须明确到可执行的程度}}

## Solutions alternatives
| Solution | Avantages | Inconvénients | Raison de la non-adoption |
| --- | --- | --- | --- |
| {{方案 A}} | | | |
| {{方案 B（采用）}} | | | — |

## Conséquences
- Positives : {{获得的能力}}
- Négatives : {{引入的成本或限制}}
- Tâches de suivi : {{需要跟进的事项}}

## Fichiers associés
- {{架构文档中受影响的章节}}
- {{替代或被引用的 ADR}}
```

## 4. Définition des champs

### 4.1 Champs du document d'architecture

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Version de code correspondante | Oui | tag | Conforme au tag de la [spécification de gestion des versions](./version-management-specification.md) | `v1.2.0` |
| Date de dernière vérification | Oui | Date | À mettre à jour après chaque modification de code | `2026-11-18` |
| Responsabilité unique du module | Oui | Texte | Un module ne décrit qu'une seule chose | `Analyser et valider les règles Markdown` |
| Non responsable de | Oui | Texte | Frontière explicite pour éviter la dérive des responsabilités | `non responsable de la réécriture du texte` |
| Choix technologiques.Fondement de la décision | Oui | Texte | Doit citer un numéro d'ADR | `voir ADR-0002` |
| Attributs de qualité.Valeur cible | Oui | Mesure | Avec unité et seuil, vérifiable | `P95 < 150 ms` |
| Dette technique connue | Non | Liste | Préciser la condition de déclenchement du remboursement | `remplacement de l'analyseur prévu en v2` |

### 4.2 Champs d'ADR

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Numéro | Oui | `ADR-NNNN` | Numéro à quatre chiffres, continu et définitivement figé | `ADR-0002` |
| État | Oui | Énumération | Proposée / adoptée / abandonnée / remplacée | `adoptée` |
| Exigences associées | Oui | Liste | Numéros REQ correspondants du dossier de lancement | `REQ-001` |
| Contexte | Oui | Texte | Énoncer des contraintes objectives ; « je pense que » est interdit | `compatibilité avec Node 18 requise` |
| Décision | Oui | Texte | Une phrase, exécutable | `adopter remark comme analyseur` |
| Solutions alternatives | Oui | Tableau | Contenir au moins 1 solution non retenue | Voir le gabarit |
| Motifs de rejet | Oui | Texte | À fournir pour chaque solution non retenue | Voir le gabarit |
| Conséquences | Oui | Liste | Les trois éléments positif, négatif et tâches de suivi doivent être présents | Voir le gabarit |

## 5. Instructions de remplissage

1. **Découpage des modules** : si la « responsabilité unique » d'une ligne contient deux choses reliées par « et » ou « ainsi que », elle doit être scindée en deux modules.
2. **Flux de données** : numéroter dans l'ordre chronologique et indiquer le contenu des données transmises ; il est interdit de n'écrire qu'une flèche entre noms de modules.
3. **Attributs de qualité** : chaque entrée doit comporter une valeur cible, un mode de vérification et une référence d'ADR ; l'absence de l'un de ces éléments la rend incomplète.
4. **Contexte de l'ADR** : rédiger le problème et les contraintes, sans la décision elle-même ; la décision n'apparaît qu'une fois, dans la section « Décision ».
5. **Solutions alternatives** : même s'il n'existe qu'une seule solution, écrire « une implémentation maison a été envisagée puis écartée en raison d'un coût de maintenance trop élevé » ; l'absence d'alternative est considérée comme une argumentation insuffisante.
6. **Changement d'état** : ne pas modifier le corps de l'ADR d'origine, créer une nouvelle ADR et faire passer l'état de l'ancienne à « remplacée par ADR-000N ».
7. **Dette technique** : indiquer la condition de déclenchement du remboursement ; il est interdit de ne lister que le symptôme.

Erreurs fréquentes :

| Formulation erronée | Problème | Mode de correction |
| --- | --- | --- |
| Placer des exemples d'appel d'API dans le document d'architecture | Chevauchement de responsabilités avec la [spécification de documentation d'API](./api-documentation-specification.md) | Déplacer vers la documentation d'API, ne conserver que les noms d'interface dans l'architecture |
| « Le système doit être performant » | Aucun seuil, non vérifiable | Fournir un objectif de latence P95 et une méthode de test de charge |
| ADR sans alternative, seulement la décision | Non argumentée | Ajouter au moins 1 solution non retenue et sa raison |
| Modifier le corps d'une ADR déjà adoptée | Historique réécrit | Créer une nouvelle ADR en marquant la relation de remplacement |
| Décision non rattachable à une exigence | Chaîne de traçabilité rompue | Ajouter les numéros REQ associés |

## 6. Exemple complet

```markdown
# ADR-0002 : Adopter remark comme couche d'analyse Markdown

- État : adoptée
- Date : 2026-11-18
- Décideur : Li Si
- Exigences associées : REQ-001, REQ-004

## Contexte
La prise en charge de GFM et du repérage des nœuds de texte chinois est nécessaire, et les dépendances d'exécution doivent être compatibles avec Node 18 ; la limite de main-d'œuvre de l'équipe pour la maintenance de l'analyseur est de 0,5 personne-mois par trimestre.

## Décision
Adopter l'écosystème remark comme unique couche d'analyse Markdown, les règles étant implémentées sous forme de greffons.

## Solutions alternatives
| Solution | Avantages | Inconvénients | Raison de la non-adoption |
| --- | --- | --- | --- |
| Analyseur maison | Contrôle total | Maintenance à long terme des cas limites | Dépasse la limite de main-d'œuvre |
| marked | Léger | Faible capacité de repérage des nœuds chinois | Ne satisfait pas REQ-004 |

## Conséquences
- Positives : la compatibilité GFM est maintenue en amont, le repérage des nœuds satisfait les conditions d'acceptation.
- Négatives : les changements d'API des greffons nécessitent un suivi des versions amont.
- Tâches de suivi : verrouiller la version majeure de remark dans la CI et s'abonner aux notifications de publication en amont.
```

## Fichiers associés

- Frontières des responsabilités et contenus interdits : [matrice documentaire](./document-matrix.md)
- Traçabilité inverse des décisions vers les exigences : [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md)
- Rédaction externe des arbitrages d'ingénierie : [guide de rédaction des fonctionnalités et arbitrages d'ingénierie](./features-and-engineering-tradeoffs-guide.md)
- Conventions de conception d'interface : [spécification de conception d'API](./api-design-specification.md)
- Modèle de données et migration : [spécification de conception de base de données](./database-design-specification.md)
- Unification terminologique : [glossaire](./glossary.md)
