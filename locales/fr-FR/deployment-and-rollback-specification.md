# Spécification de déploiement et de restauration

> Problème que ce fichier résout : définir les gabarits, les champs et les critères d'exécution de la liste de déploiement, du bon de changement et du plan de restauration, afin de garantir une mise en ligne maîtrisée, un état consultable et un rétablissement rapide en cas d'incident.

## 1. Dispositions normatives

1. Avant le déploiement, la CI, la revue de code et la porte qualité doivent être franchies (voir la [porte qualité](./quality-gate.md)).
2. Le déploiement s'appuie sur une version publiée et déjà taguée, sans utiliser de commit non marqué (voir la [spécification de gestion des versions](./version-management-specification.md)).
3. La configuration d'environnement est séparée du code ; les configurations sensibles sont injectées via la gestion de configuration et ne sont pas versionnées (voir la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)).
4. Les changements de structure de base de données s'exécutent via des scripts de migration et doivent être rétrocompatibles (voir la [spécification de conception de base de données](./database-design-specification.md)).
5. Chaque déploiement doit enregistrer le numéro de version, l'heure, l'opérateur et le contenu du changement ; un déploiement sans enregistrement est considéré comme non conforme.
6. Chaque version doit disposer d'un plan de restauration préparé à l'avance ; sans plan de restauration, la mise en ligne est interdite.
7. Après le déploiement, un contrôle de santé et une vérification de fumée doivent être exécutés ; la publication ne se termine qu'une fois les deux réussis.

## 2. Gabarit de liste de déploiement

```markdown
# Liste de déploiement : {{项目名称}} {{版本号}}

Version : {{vX.Y.Z}} ｜ tag : {{vX.Y.Z}} ｜ Environnement cible : {{预发布 / 生产}} ｜ Horaire prévu : {{YYYY-MM-DD HH:MM}}

## Contrôles préalables
- [ ] CI entièrement verte, adresse d'exécution du workflow : {{URL}}
- [ ] Revue de code validée, approbateur : {{姓名}}
- [ ] Portes qualité A/B/C toutes PASS
- [ ] Journal des modifications et Release Notes prêts
- [ ] Plan de restauration revu, voir la fin de cette section
- [ ] Script de migration de base de données revu et rétrocompatible
- [ ] Liste des changements de configuration confirmée (éléments injectés non versionnés)

## Contenu du changement
| Élément de changement | Type | Périmètre d'impact | Exigence rattachée | Mode de vérification |
| --- | --- | --- | --- | --- |
| {{功能 / 配置 / 数据迁移}} | {{新增 / 修改 / 移除}} | {{受影响模块}} | {{REQ-NNN}} | {{如何确认}} |

## Étapes d'exécution
1. {{步骤，含具体命令或平台操作}}
2. {{灰度比例与观察时长}}
3. {{全量放量条件}}

## Contrôle de santé et vérification de fumée
| Élément de contrôle | Condition de verdict | Mode d'exécution | Résultat |
| --- | --- | --- | --- |
| Service actif | {{HTTP 200}} | {{命令}} | {{通过 / 未通过}} |
| Chemin critique | {{主流程完成}} | {{命令}} | {{通过 / 未通过}} |
| Taux d'erreur | {{< X%}} | {{监控面板}} | {{通过 / 未通过}} |

## Enregistrement du déploiement
| Élément | Valeur |
| --- | --- |
| Heure réelle de déploiement | {{YYYY-MM-DD HH:MM}} |
| Opérateur | {{姓名}} |
| Approbateur | {{姓名}} |
| Numéro de version réel | {{vX.Y.Z}} |
| Résultat | {{成功 / 回滚 / 中止}} |

## Plan de restauration
- Version cible de restauration : {{vX.Y.Z}}
- Condition de déclenchement : {{错误率 > X% 持续 N 分钟 / 冒烟失败 / 数据异常}}
- Décideur : {{姓名}}
- Étapes de restauration : {{具体命令或操作}}
- Compatibilité des données : {{是否需要数据回滚；如果需要，说明方式}}
```

## 3. Gabarit d'enregistrement de déploiement

```markdown
## {{YYYY-MM-DD}} {{vX.Y.Z}} → {{环境}}

- Numéro de version : {{vX.Y.Z}}
- tag : {{vX.Y.Z}}
- Heure : {{HH:MM}}
- Opérateur / approbateur : {{姓名 / 姓名}}
- Résumé du changement : {{一句话}}
- Contrôle de santé : {{通过 / 未通过}}
- Résultat : {{成功 / 回滚}}
- Publication associée : {{Release Notes URL}}
- Remarque : {{异常与处理记录；无则写「无」}}
```

## 4. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| tag | Oui | Texte | Strictement identique au tag de la [spécification de gestion des versions](./version-management-specification.md) | `v1.2.0` |
| Environnement cible | Oui | Énumération | préproduction / production, aucune configuration ne doit être mélangée | `production` |
| Élément de changement.Type | Oui | Énumération | ajout / modification / suppression | `modification` |
| Exigence rattachée | Oui | Liste | Numéro REQ, écrire « aucune » pour un changement sans exigence | `REQ-007` |
| Proportion de déploiement progressif | Non | Pourcentage | Obligatoire en cas de montée en charge progressive | `10 % → 50 % → 100 %` |
| Condition de verdict | Oui | Seuil | Observable et évaluable | `HTTP 200` |
| Numéro de version réel | Oui | Texte | Justifier l'écart avec le numéro de version planifié | `v1.2.1` |
| Condition de déclenchement de la restauration | Oui | Seuil + durée | Les formulations du type « je sens une anomalie » sont interdites | `taux d'erreur > 1 % pendant 5 minutes` |
| Compatibilité des données | Oui | Texte | Indiquer clairement si une restauration de données est nécessaire | `aucune restauration de données nécessaire` |

## 5. Instructions de saisie

1. **Contrôles préalables** : cocher item par item, le cochage global en une seule fois est interdit ; si un élément n'est pas terminé, le déploiement est interrompu.
2. **Contenu du changement** : chaque ligne doit être rattachée à un numéro REQ ; un changement purement opérationnel sans exigence associée est noté « aucune » avec justification du changement.
3. **Contrôle de santé** : la condition doit être évaluable automatiquement ; « le service semble normal » est insuffisant.
4. **Condition de déclenchement de la restauration** : le seuil et la durée doivent être fournis ensemble, afin d'éviter un déclenchement erroné sur une fluctuation instantanée.
5. **Montée en charge progressive** : après chaque palier, observer pendant la durée prescrite et consigner la conclusion d'observation avant de passer au palier suivant.
6. **Enregistrement du déploiement** : ajout chronologique, sans écrasement de l'historique ; le numéro de version doit être cohérent avec le push, le tag et les Release Notes.
7. **Exécution de la restauration** : pour la restauration de code, utiliser `git revert` afin de générer un commit inverse, sans push forcé sur un historique déjà public (voir la [spécification de push et de publication](./push-and-release-specification.md)).

Erreurs courantes :

| Rédaction erronée | Problème | Mode de correction |
| --- | --- | --- |
| Déployer un commit non tagué | Version non reproductible | Poser le tag avant de déployer |
| Plan de restauration indiquant « restaurer en cas de problème » | Absence de condition de déclenchement et d'étapes | Ajouter le seuil, le décideur et les étapes |
| Changement de base de données incompatible avec l'ancienne version | Données inutilisables après restauration | Adopter la méthode en trois temps : extension, migration, contraction |
| Enregistrement de déploiement rédigé après coup | État non fiable | Enregistrer au moment du déploiement |
| Contrôle de santé limité à la page d'accueil | Chemin critique non vérifié | Ajouter des cas de fumée sur le parcours principal |

## 6. Exemple complet

```markdown
# Liste de déploiement : markdown-lint-cli v1.0.0

Version : v1.0.0 ｜ tag : v1.0.0 ｜ Environnement cible : production ｜ Horaire prévu : 2026-11-20 10:00

## Contrôles préalables
- [x] CI entièrement verte : https://github.com/example/markdown-lint-cli/actions/runs/123
- [x] Revue de code validée, approbateur : 李四
- [x] Portes qualité A/B/C toutes PASS
- [x] Journal des modifications et Release Notes prêts
- [x] Plan de restauration revu
- [x] Aucune migration de base de données
- [x] Liste des changements de configuration confirmée : aucune

## Contenu du changement
| Élément de changement | Type | Périmètre d'impact | Exigence rattachée | Mode de vérification |
| --- | --- | --- | --- | --- |
| Règle d'espacement chinois-anglais | ajout | moteur de règles | REQ-001 | exécuter TC-001 |
| Sortie de rapport CLI | modification | module de rapport | REQ-007 | exécuter TC-012 |

## Étapes d'exécution
1. Récupérer le tag v1.0.0 et vérifier la somme de contrôle
2. Déploiement progressif à 10 %, observation pendant 10 minutes
3. Passage à 100 % une fois le taux d'erreur < 0,1 %

## Contrôle de santé et vérification de fumée
| Élément de contrôle | Condition de verdict | Mode d'exécution | Résultat |
| --- | --- | --- | --- |
| Service actif | HTTP 200 | curl /healthz | réussi |
| Chemin critique | vérification de 50 documents achevée | script shell | réussi |
| Taux d'erreur | < 0,1 % | tableau de supervision | réussi |

## Plan de restauration
- Version cible de restauration : v0.9.3
- Condition de déclenchement : taux d'erreur > 1 % pendant 5 minutes
- Décideur : 李四
- Étapes de restauration : basculer l'étiquette de déploiement vers v0.9.3 et exécuter le contrôle de compatibilité des données
- Compatibilité des données : aucun changement de base de données, aucune restauration de données nécessaire
```

## Fichiers associés

- Règles de version et de tag : [spécification de gestion des versions](./version-management-specification.md)
- Actions de push et traitement des incidents : [spécification de push et de publication](./push-and-release-specification.md)
- Classification des incidents et rétrospective : [spécification de réponse aux incidents](./incident-response-specification.md)
- Support des indicateurs et des alertes : [spécification d'observabilité](./observability-specification.md)
- Scripts de migration et compatibilité : [spécification de conception de base de données](./database-design-specification.md)
- Injection de configuration sensible : [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)
