# Spécification de réponse aux incidents

> Problème que ce fichier résout : définir le gabarit de rapport d'incident, la consignation de la chronologie, les gabarits de communication et les champs de rétrospective, afin de garantir la maîtrise des incidents, la synchronisation de l'information et la capitalisation de l'expérience.

## 1. Dispositions de la spécification

1. Niveaux d'incident : P0 fonctionnalité centrale indisponible ou données corrompues ; P1 fonctionnalité gravement dégradée affectant la majorité des utilisateurs ; P2 problème localisé, impact limité.
2. Processus de réponse : détection → qualification → arrêt de l'hémorragie → localisation → correction → annonce ; l'arrêt de l'hémorragie prime sur la localisation.
3. Chaque incident P0/P1 doit faire l'objet d'une rétrospective consignant la chronologie, la cause racine, l'impact, le traitement et les actions d'amélioration.
4. Les actions d'amélioration doivent être intégrées au suivi de la [spécification de feuille de route](./roadmap-specification.md) jusqu'à leur clôture.
5. La rétrospective se concentre sur l'amélioration du système et ne recherche pas la responsabilité individuelle.
6. Fuite de clé : renouveler immédiatement → nettoyer l'historique → annoncer ; un commit de suppression seul est interdit (voir la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)).
7. Fichier volumineux poussé par erreur : migrer vers LFS ou réécrire l'historique (voir la [spécification de push et de publication](./push-and-release-specification.md)).

## 2. Gabarit de rapport d'incident

```markdown
# Rapport d'incident : {{INC-YYYYMMDD-NN}}

- Niveau d'incident : {{P0 / P1 / P2}}
- Heure de détection : {{YYYY-MM-DD HH:MM}}
- Heure de rétablissement : {{YYYY-MM-DD HH:MM}}
- Durée : {{N 分钟}}
- Responsable de la coordination : {{姓名}}
- État actuel : {{处理中 / 已恢复 / 已复盘}}

## Portée de l'impact
| Dimension | Description |
| --- | --- |
| Fonctionnalités affectées | {{具体功能}} |
| Part d'utilisateurs affectés | {{估算值与依据}} |
| Impact sur les données | {{无 / 描述}} |
| Impact métier | {{可量化的损失或阻塞}} |

## Chronologie
| Heure | Événement | Source | Opérateur |
| --- | --- | --- | --- |
| {{HH:MM}} | Déclenchement de l'alerte | {{监控面板}} | {{姓名}} |
| {{HH:MM}} | Qualification en P1 | {{判断依据}} | {{姓名}} |
| {{HH:MM}} | Exécution de la restauration | {{命令 / 平台}} | {{姓名}} |
| {{HH:MM}} | Rétablissement du service | {{验证方式}} | {{姓名}} |

## Cause racine
- Cause directe : {{触发故障的具体事件}}
- Cause fondamentale : {{为何未被预防或及时检测}}
- Facteurs d'amplification : {{扩大影响的因素}}

## Traitement et vérification
1. {{止血措施}}
2. {{修复措施}}
3. {{验证方式与结果}}

## Actions d'amélioration
| N° | Action | Responsable | Échéance | Mode de vérification | État |
| --- | --- | --- | --- | --- | --- |
| {{A-NN}} | {{具体动作}} | {{姓名}} | {{YYYY-MM-DD}} | {{可判定阈值}} | {{待开始}} |
```

## 3. Gabarits de communication

```markdown
## Avis d'incident (initial)

- Heure : {{YYYY-MM-DD HH:MM}}
- Niveau : {{P0 / P1 / P2}}
- Symptômes : {{用户可感知的现象，不写内部细节}}
- Impact : {{受影响范围}}
- Mesures en cours : {{正在做什么}}
- Prochaine mise à jour : {{HH:MM}}

## Avis d'incident (rétablissement)

- Heure de rétablissement : {{HH:MM}}
- Confirmation du rétablissement : {{验证方式与结果}}
- Impact résiduel : {{无 / 描述}}
- Suite : {{复盘安排}}
```

## 4. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Numéro d'incident | Oui | `INC-YYYYMMDD-NN` | Numéro du jour, continu et sans réutilisation | `INC-20261118-01` |
| Niveau d'incident | Oui | Énumération | P0 / P1 / P2 | `P1` |
| Durée | Oui | Durée | Nombre de minutes entre la détection et le rétablissement | `42 minutes` |
| Responsable de la coordination | Oui | Texte | Unique, chargé des décisions et de la synchronisation | `Li Si` |
| Part d'utilisateurs affectés | Oui | Texte | La base de l'estimation est obligatoire | `environ 8 %, d'après le comptage des journaux d'erreurs` |
| Chronologie | Oui | Tableau | Chaque entrée comporte l'heure et la source | voir le gabarit |
| Cause fondamentale | Oui | Texte | Distinguer la cause directe et la cause fondamentale | `absence d'exercice de restauration` |
| Action d'amélioration.Mode de vérification | Oui | Texte | Jugeable, avec seuil | `restauration en moins de 5 minutes lors du prochain exercice` |
| Prochaine mise à jour | Oui | Horodatage | Obligatoire pendant le traitement, « mise à jour à tout moment » est interdit | `18:30` |

## 5. Consignes de saisie

1. **Qualification** : qualifier selon la portée et la gravité de l'impact ; en cas de doute, qualifier au niveau le plus élevé, puis ajuster en consignant le motif.
2. **Priorité à l'arrêt de l'hémorragie** : rétablir d'abord le service (restauration, dégradation, limitation de débit), puis localiser la cause racine ; la localisation ne doit pas retarder l'arrêt de l'hémorragie.
3. **Chronologie** : consigner dans l'ordre chronologique, avec des sources vérifiables (identifiant d'alerte, commande, extrait de journal) ; la reconstitution de mémoire après coup est interdite.
4. **Cause racine** : la cause directe est l'événement déclencheur, la cause fondamentale est un défaut systémique ; les deux doivent être renseignées.
5. **Communication** : l'avis initial doit indiquer la prochaine mise à jour ; l'avis de rétablissement doit préciser le mode de vérification et l'impact résiduel.
6. **Actions d'amélioration** : trois au maximum, suivies dans la feuille de route ; une action sans responsable ne doit pas figurer dans le rapport.
7. **Rétrospective** : se concentrer sur l'amélioration du système et des processus, sans évaluer les personnes ; la recherche de responsabilité et les formulations du type « untel a été négligent » sont proscrites.
8. **Incidents particuliers** : une fuite de clé est traitée selon H12 ; un fichier volumineux poussé par erreur est traité par migration LFS ; les deux doivent faire l'objet d'une trace distincte.

Erreurs fréquentes :

| Formulation erronée | Problème | Correction |
| --- | --- | --- |
| Localiser la cause racine avant d'arrêter l'hémorragie | Prolonge la durée de l'incident | Restaurer d'abord |
| Chronologie reconstituée après coup | Faits non fiables | Consigner en temps réel pendant le traitement |
| Cause racine écrite « untel a été négligent » | Mise en cause individuelle, sans valeur d'amélioration | Remonter au niveau du processus ou de l'outil |
| Avis indiquant « correction dès que possible » | Aucune prochaine mise à jour | Indiquer un horodatage précis |
| Action d'amélioration sans mode de vérification | Clôture non jugeable | Ajouter un seuil et un moment de contrôle |

## 6. Exemple complet

```markdown
# Rapport d'incident : INC-20261118-01

- Niveau d'incident : P1
- Heure de détection : 2026-11-18 10:12
- Heure de rétablissement : 2026-11-18 10:54
- Durée : 42 minutes
- Responsable de la coordination : Li Si
- État actuel : rétrospective effectuée

## Portée de l'impact
| Dimension | Description |
| --- | --- |
| Fonctionnalités affectées | L'API de contrôle des règles renvoie des erreurs 5xx |
| Part d'utilisateurs affectés | Environ 8 %, d'après le comptage des journaux 5xx |
| Impact sur les données | aucun |
| Impact métier | Impossible de soumettre des tâches de contrôle pendant 42 minutes |

## Cause racine
- Cause directe : le chemin de chargement du greffon de règles a été écrasé par la nouvelle configuration, provoquant l'échec du démarrage.
- Cause fondamentale : la modification de configuration n'a pas été intégrée à la validation de préproduction.

## Actions d'amélioration
| N° | Action | Responsable | Échéance | Mode de vérification | État |
| --- | --- | --- | --- | --- | --- |
| A-01 | Intégrer les modifications de configuration à la liste de contrôle de préproduction | Wang Wu | 2026-11-25 | Les 5 prochaines modifications comportent toutes une trace de contrôle | À démarrer |
```

## Fichiers associés

- Sources d'alerte et guide de traitement : [spécification d'observabilité](./observability-specification.md)
- Opérations de restauration : [spécification de déploiement et de restauration](./deployment-and-rollback-specification.md)
- Traitement des clés et des informations sensibles : [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)
- Fichiers volumineux et réécriture de l'historique : [spécification de push et de publication](./push-and-release-specification.md)
- Suivi des actions d'amélioration : [spécification de feuille de route](./roadmap-specification.md)
- Rétrospective d'amélioration des processus : [spécification de rétrospective d'itération](./iteration-retrospective-specification.md)
- Modalités de qualification des alertes : [spécification des indicateurs de mesure de la qualité](./quality-metrics-specification.md)
