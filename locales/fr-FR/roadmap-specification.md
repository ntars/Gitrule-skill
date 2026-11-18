# Spécification de la feuille de route

> Problème que ce fichier résout : définir le gabarit, les champs, le marquage des états et le principe de non-engagement de la feuille de route, afin d'éviter de présenter un plan comme un engagement et de garantir la cohérence avec le journal des modifications et la rétrospective d'itération.

## 1. Dispositions de la spécification

1. La feuille de route doit porter, à un emplacement bien visible, la mention « Cette feuille de route est un plan, non un engagement de livraison ».
2. Aucune date de livraison précise ne doit être promise ; les versions cibles sont exprimées par un intervalle de versions ou par un trimestre.
3. Toute modification d'état doit être consignée ; tout élément annulé doit être justifié.
4. Chaque élément achevé doit pointer vers l'entrée correspondante de la [spécification du journal des modifications](./changelog-specification.md), afin d'éviter une incohérence entre les deux emplacements.
5. La feuille de route porte sur les plans futurs et autorise les ajustements et les annulations ; le journal des modifications porte sur des faits publiés et ne permet pas de réécrire les entrées historiques.
6. Chaque élément planifié doit être associé à au moins une exigence ou à une action d'amélioration issue d'une rétrospective ; la relation de traçabilité est décrite dans la [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md).

## 2. Gabarit de feuille de route

```markdown
# Feuille de route : {{项目名称}}

> Cette feuille de route est un plan, non un engagement de livraison. Les versions cibles et les trimestres ne sont que des prévisions et peuvent être ajustés selon les priorités.

Version : {{v1.0}} ｜ Auteur de la mise à jour : {{姓名}} ｜ Dernière vérification : {{YYYY-MM-DD}}

## Maintenant / Ensuite / Plus tard

| Phase | Élément planifié | État | Version cible | Exigence associée | Dépendances | Critères d'acceptation | Journal des modifications |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Maintenant | {{能力描述}} | En cours | {{v1.0}} | {{REQ-001}} | {{无}} | {{可验证条件}} | — |
| Ensuite | {{能力描述}} | Planifié | {{v1.1 ~ v1.2}} | {{REQ-008}} | {{计划项 A}} | {{可验证条件}} | — |
| Plus tard | {{能力描述}} | Planifié | {{待定}} | {{REQ-015}} | {{外部依赖}} | {{可验证条件}} | — |
| Annulé | {{能力描述}} | Annulé | — | {{REQ-020}} | — | — | — |

États : planifié / en cours / achevé / annulé

## Registre des changements d'état
| Date | Élément planifié | Ancien état → nouvel état | Raison | Décideur |
| --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{计划项}} | {{规划中 → 已取消}} | {{原因}} | {{姓名}} |

## Justification des annulations
- {{计划项}} : {{取消原因，如需求变更、依赖 unavailable}}
```

## 3. Gabarit d'élément planifié

```markdown
### {{计划项名称}}

- État : {{规划中 / 进行中 / 已完成 / 已取消}}
- Version cible : {{vX.Y / 季度 / 待定}}
- Exigence associée : {{REQ-NNN}}
- Source : {{立项书 / 迭代回顾 A-NN / 用户反馈}}
- Dépendances : {{前置计划项或外部依赖；无则写「无」}}
- Critères d'acceptation : {{可验证的完成条件，须含阈值}}
- Raison de la non-réalisation : {{仅已取消项填写}}
```

## 4. Définition des champs

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Élément planifié | Oui | Groupe nominal | Décrire la capacité à livrer, non une action de tâche | `Prise en charge de la configuration TOML` |
| État | Oui | Énumération | Planifié / en cours / achevé / annulé | `en cours` |
| Version cible | Oui | Version / trimestre / à déterminer | Dates précises interdites | `v1.1 ~ v1.2` |
| Exigence associée | Oui | `REQ-NNN` | Conforme au numéro du dossier de lancement | `REQ-008` |
| Source | Oui | Texte | Lancement, rétrospective d'itération ou retour utilisateur | `rétrospective A-01` |
| Dépendances | Oui | Texte | Écrire « aucune » s'il n'y en a pas ; ne pas laisser vide | `dépend de l'élément planifié A` |
| Critères d'acceptation | Oui | Texte | Vérifiables, avec seuil | `analyse de 100 échantillons sans échec` |
| Journal des modifications | Obligatoire sous condition | Lien | Obligatoire pour les éléments achevés | `[1.0.0]` |
| Raison de l'annulation | Obligatoire sous condition | Texte | Obligatoire pour les éléments annulés | `l'API externe dont dépend l'élément a été retirée` |

## 5. Instructions de remplissage

1. **Découpage des phases** : trois niveaux « Maintenant / Ensuite / Plus tard » ; « Maintenant » ne dépasse pas 3 éléments, au-delà les priorités doivent être réordonnées.
2. **Non-engagement** : il est interdit d'écrire des engagements datés du type « publication au T3 » ou « achèvement en décembre » ; exprimer les prévisions par numéro de version ou intervalle de trimestres.
3. **Critères d'acceptation** : ils doivent pouvoir être évalués objectivement ; « améliorer la facilité d'usage » est non conforme, « réduire les options de configuration de 5 à 2 » est conforme.
4. **Changements d'état** : chaque changement ajoute un enregistrement, sans écraser la valeur d'origine ; les éléments annulés conservent leur ligne et indiquent la raison.
5. **Lien avec l'achèvement** : lorsque l'état passe à « achevé », l'ancre du journal des modifications doit être renseignée en même temps ; sans entrée de journal correspondante, l'achèvement ne peut pas être marqué.
6. **Lien avec la rétrospective** : lorsqu'une action d'amélioration issue d'une rétrospective d'itération est intégrée à la feuille de route, indiquer A-NN dans « Source » et consigner en parallèle dans la [spécification de la rétrospective d'itération](./iteration-retrospective-specification.md).
7. **Résumé dans le README** : le README ne contient que le résumé des trois niveaux et un lien ; le tableau complet reste dans ce fichier, voir la [spécification des sections de README](./readme-sections-specification.md).

Erreurs fréquentes :

| Formulation erronée | Problème | Mode de correction |
| --- | --- | --- |
| « Publication en décembre 2026 » | Constitue un engagement | Remplacer par `v1.2` ou `T4` |
| Élément achevé sans lien vers le journal des modifications | Incohérence entre les deux emplacements | Ajouter l'ancre du journal |
| Suppression pure et simple de la ligne d'un élément annulé | Historique non traçable | Conserver la ligne et indiquer la raison |
| Élément planifié formulé « optimiser les performances » | Aucun critère d'acceptation | Ajouter un indicateur avec seuil |
| Feuille de route saturée de 20 éléments | Priorités indécidables | Converger vers trois niveaux, avec un nombre d'éléments limité par niveau |

## 6. Exemple complet

```markdown
# Feuille de route : markdown-lint-cli

> Cette feuille de route est un plan, non un engagement de livraison.

Version : v1.0 ｜ Auteur de la mise à jour : Li Si ｜ Dernière vérification : 2026-11-20

| Phase | Élément planifié | État | Version cible | Exigence associée | Dépendances | Critères d'acceptation | Journal des modifications |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Maintenant | Ensemble de règles de base | Achevé | v1.0.0 | REQ-001~007 | aucune | Taux de détection ≥ 95 % sur 50 échantillons | [1.0.0] |
| Ensuite | Intégration au greffon d'éditeur | Planifié | v1.1 | REQ-003 | ensemble de règles de base stabilisé | Appel possible depuis les éditeurs courants | — |
| Plus tard | DSL de règles personnalisées | Planifié | à déterminer | REQ-018 | API de greffon stabilisée | Ajout de règles par l'utilisateur sans modifier le code source | — |
| Annulé | Synchronisation des règles dans le cloud | Annulé | — | REQ-020 | — | — | — |

## Registre des changements d'état
| Date | Élément planifié | Ancien état → nouvel état | Raison | Décideur |
| --- | --- | --- | --- | --- |
| 2026-11-15 | Synchronisation des règles dans le cloud | Planifié → annulé | Aucune ressource de maintenance côté serveur | Li Si |
```

## Fichiers associés

- Nommage des versions et versions cibles : [spécification de gestion des versions](./version-management-specification.md)
- Fondement du lancement et numéros d'exigence : [lancement de projet et spécification des exigences](./project-initiation-and-requirements-specification.md)
- Enregistrement externe des éléments achevés : [spécification du journal des modifications](./changelog-specification.md)
- Source des actions d'amélioration : [spécification de la rétrospective d'itération](./iteration-retrospective-specification.md)
- Traçabilité des exigences vers le plan : [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md)
- Section feuille de route du README : [spécification des sections de README](./readme-sections-specification.md)
