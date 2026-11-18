# Spécification de la rétrospective d'itération

> Problème que ce fichier résout : définir le gabarit de rétrospective de fin d'itération, ses champs et le mécanisme de suivi des actions d'amélioration, afin que les problèmes se traduisent en actions concrètes et vérifiables pour le cycle suivant, en évitant la répétition des erreurs.

## 1. Dispositions normatives

1. Une rétrospective doit être menée dans les cinq jours ouvrés suivant la fin de chaque itération ; tout dépassement doit être justifié.
2. La rétrospective doit se fonder sur des données factuelles ; il est interdit de substituer une impression à une mesure ; les sources de données figurent dans la [spécification des indicateurs de mesure de la qualité](./quality-metrics-specification.md).
3. Chaque problème doit préciser sa cause racine, l'action d'amélioration, le responsable et la méthode de vérification ; aucune entrée sans responsable ni méthode de vérification ne peut figurer dans la liste d'actions.
4. Le nombre d'actions d'amélioration est limité à trois, classées par impact ; au-delà de trois, elles doivent être fusionnées ou rétrogradées en suggestions.
5. Les actions d'amélioration du cycle précédent doivent être vérifiées une à une quant à leur état lors de la rétrospective du cycle en cours ; celles non réalisées doivent être justifiées et replanifiées.
6. Le document de rétrospective ne consigne que l'amélioration du processus, et non le contenu des changements de version, lequel relève de la [spécification du journal des modifications](./changelog-specification.md).

## 2. Gabarit du document de rétrospective

```markdown
# Rétrospective d'itération : {{项目名称}} {{迭代标识}}

Période de l'itération : {{YYYY-MM-DD ~ YYYY-MM-DD}} ｜ Animateur : {{姓名}} ｜ Participants : {{姓名列表}} ｜ Date de la rétrospective : {{YYYY-MM-DD}}

## 1. Retour sur les objectifs
| Objectif de l'itération | Source | État d'atteinte | Base d'appréciation |
| --- | --- | --- | --- |
| {{目标描述}} | {{路线图 / 立项书}} | {{达成 / 未达成 / 部分达成}} | {{数据或交付物}} |

## 2. Instantané des données
| Indicateur | Valeur du cycle précédent | Valeur du cycle en cours | Variation | Cible |
| --- | --- | --- | --- | --- |
| Nombre d'exigences livrées | | | | |
| Nombre de défauts échappés | | | | |
| Durée moyenne de la CI | | | | |
| Couverture des exigences | | | | |
| Nombre d'incidents | | | | |

## 3. Liste des faits
- Ce qui a bien fonctionné : {{基于数据的事实，如「本轮 CI 全绿率 98%」}}
- Obstacles : {{基于数据的障碍，如「集成环境等待平均 4 小时」}}
- Imprévus : {{未预见的事件及其影响}}

## 4. Problèmes et causes racines
| Numéro | Problème | Preuve | Cause racine | Impact |
| --- | --- | --- | --- | --- |
| R-01 | {{问题描述}} | {{数据 / 事件}} | {{根因，非表象}} | {{造成的影响}} |

## 5. Actions d'amélioration
| Numéro | Problème associé | Action | Responsable | Échéance | Méthode de vérification | État |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | R-01 | {{具体动作}} | {{姓名}} | {{YYYY-MM-DD}} | {{如何验证生效}} | À démarrer |

## 6. Vérification des actions du cycle précédent
| Numéro | Action | État au cycle précédent | Conclusion du cycle en cours | Suite donnée |
| --- | --- | --- | --- | --- |
| A-00 | {{动作}} | En cours | {{完成 / 未完成 / 放弃}} | {{继续 / 重排 / 关闭并说明}} |

## 7. Consensus et points en suspens
- Consensus du cycle : {{需要长期遵守的约定}}
- Points en suspens : {{不在本轮处理的问题及原因}}
```

## 3. Gabarit d'entrée d'action d'amélioration

```markdown
### A-{{两位序号}}：{{动作标题}}

- Problème associé : {{R-NN}}
- Action : {{一个可执行的动作，含具体对象}}
- Responsable : {{姓名，唯一}}
- Échéance : {{YYYY-MM-DD}}
- Méthode de vérification : {{可判定的检查和阈值}}
- Effet attendu : {{用指标描述}}
- État : À démarrer / En cours / Terminé / Abandonné
```

## 4. Définition des champs

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Identifiant d'itération | Oui | Texte | Identique au numéro de phase de la [spécification de la feuille de route](./roadmap-specification.md) | `Sprint-12` |
| État d'atteinte | Oui | Enumération | Atteint / Non atteint / Partiellement atteint | `Partiellement atteint` |
| Base d'appréciation | Oui | Texte | Données ou lien vers un livrable, ne doit pas être vide | `REQ-001 publié` |
| Instantané des données | Oui | Tableau | Au moins 3 indicateurs, avec valeurs du cycle précédent et du cycle en cours | `Défauts échappés 2 → 0` |
| Cause racine | Oui | Texte | Distinguer le symptôme de la cause racine, chaîner par « parce que » de manière vérifiable | `Parce que l'environnement n'était pas intégré à la CI` |
| Action | Oui | Texte | Action unique, avec objet et comportement | `Intégrer l'environnement d'intégration à la CI` |
| Responsable | Oui | Texte | Unique, il est interdit d'écrire « l'équipe » | `王五` |
| Méthode de vérification | Oui | Texte | Déterminable, avec moment du contrôle | `Durée de la CI au prochain cycle < 10 minutes` |
| État | Oui | Enumération | L'un des quatre états | `Terminé` |

## 5. Consignes de remplissage

1. **Retour sur les objectifs** : se fonder sur les objectifs d'origine du lancement ou de la feuille de route ; ne pas réécrire les objectifs pour les faire coïncider avec les résultats.
2. **Instantané des données** : utiliser le même référentiel de mesure que le cycle précédent ; en cas de changement de référentiel, signaler simultanément « référentiel modifié » et les définitions ancienne et nouvelle.
3. **Liste des faits** : ne consigner que des faits vérifiables ; les jugements subjectifs du type « communication insuffisante » doivent être convertis en événements et moments précis.
4. **Cause racine** : poursuivre le questionnement jusqu'au niveau où une action est possible ; « parce que les tests sont insuffisants » reste un symptôme, « parce que les exigences ne sont pas associées à des cas de test » est la cause racine.
5. **Nombre d'actions** : trois au maximum ; si les problèmes sont plus nombreux, les classer par impact et consigner les autres dans les « points en suspens ».
6. **Méthode de vérification** : préciser le moment du contrôle et le seuil de décision ; « observation ultérieure » n'est pas acceptable.
7. **Vérification du cycle précédent** : donner une conclusion pour chaque entrée, sans sauter un paragraphe entier ; tout abandon doit être motivé.

Erreurs fréquentes :

| Rédaction erronée | Problème | Correction |
| --- | --- | --- |
| « Il faut accorder plus d'importance à la qualité » | Aucune action, aucun responsable | Remplacer par une action et un responsable précis |
| Écrire « négligence » comme cause racine | Non vérifiable, non améliorable | Questionner jusqu'au niveau du processus ou de l'outil |
| Huit actions d'amélioration listées | Impossible à mettre en œuvre | Classer par impact et retenir les trois premières |
| Écrire « voir l'effet » comme méthode de vérification | Non déterminable | Ajouter un seuil et un moment de contrôle |
| Actions du cycle précédent non vérifiées | Rupture de la boucle d'amélioration | Renseigner une conclusion pour chaque entrée de ce cycle |

## 6. Exemple complet

```markdown
# Rétrospective d'itération : markdown-lint-cli Sprint-12

Période de l'itération : 2026-11-10 ~ 2026-11-21 ｜ Animateur : 李四 ｜ Participants : 王五、赵六 ｜ Date de la rétrospective : 2026-11-23

## 1. Retour sur les objectifs
| Objectif de l'itération | Source | État d'atteinte | Base d'appréciation |
| --- | --- | --- | --- |
| Publier les règles centrales de la v1.0.0 | Feuille de route S12 | Atteint | Tag v1.0.0 publié |
| Couverture des exigences à 100 % | Dossier de lancement G1 | Partiellement atteint | 13 exigences obligatoires sur 14 bouclées |

## 2. Instantané des données
| Indicateur | Valeur du cycle précédent | Valeur du cycle en cours | Variation | Cible |
| --- | --- | --- | --- | --- |
| Nombre d'exigences livrées | 6 | 14 | +8 | 14 |
| Nombre de défauts échappés | 2 | 1 | -1 | 0 |
| Couverture des exigences | 85 % | 92,9 % | +7,9 % | 100 % |

## 4. Problèmes et causes racines
| Numéro | Problème | Preuve | Cause racine | Impact |
| --- | --- | --- | --- | --- |
| R-01 | REQ-003 sans cas de test | Champ TC de la matrice de traçabilité à « à compléter » | Parce que l'exhaustivité de la matrice de traçabilité n'était pas contrôlée obligatoirement lors de la revue des exigences | Couverture des exigences non atteinte |

## 5. Actions d'amélioration
| Numéro | Problème associé | Action | Responsable | Échéance | Méthode de vérification | État |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | R-01 | Ajouter au formulaire de revue des exigences le point de contrôle « matrice de traçabilité renseignée » | 王五 | 2026-11-27 | Les 5 comptes rendus de revue du prochain cycle comportent tous cette case cochée | À démarrer |
```

## Fichiers associés

- Données de traçabilité des exigences jusqu'à la publication : [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md)
- Référentiel et mode de calcul des indicateurs : [spécification des indicateurs de mesure de la qualité](./quality-metrics-specification.md)
- Source des phases et des objectifs : [spécification de la feuille de route](./roadmap-specification.md)
- Contenu des changements de version : [spécification du journal des modifications](./changelog-specification.md)
- Rétrospective et amélioration après incident : [spécification de la réponse aux incidents](./incident-response-specification.md)
- Phase d'exécution du suivi : [processus d'exécution](./execution-process.md)
