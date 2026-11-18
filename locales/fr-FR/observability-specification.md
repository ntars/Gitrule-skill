# Spécification d'observabilité

> Problème que ce fichier résout : définir les champs de journalisation, les objectifs SLI/SLO, les règles d'alerte et le gabarit de fiche de réponse aux alertes, afin de garantir un état du système visible, des incidents localisables et des alertes exécutables.

## 1. Dispositions normatives

1. L'observabilité repose sur trois piliers : journaux, indicateurs et traçage distribué ; les trois doivent être corrélés par un identifiant de requête unifié.
2. Les journaux doivent être structurés et comporter un horodatage, un niveau et un identifiant de requête ; l'enregistrement d'informations sensibles est interdit, les règles de masquage figurent dans la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md).
3. Chaque service critique doit définir des SLI et des SLO, avec le mode de calcul et la fenêtre statistique.
4. Les règles d'alerte doivent comporter un seuil explicite, une durée et un responsable ; une alerte sans consigne de traitement ne doit pas être mise en service.
5. Une alerte déclenchée doit pouvoir être rattachée à la classification et au processus de traitement de la [spécification de réponse aux incidents](./incident-response-specification.md).
6. Le mode de calcul des indicateurs doit être unifié avec la [spécification des indicateurs de mesure de la qualité](./quality-metrics-specification.md) ; les homonymes de sens différents sont interdits.

## 2. Les trois piliers et leurs champs

| Pilier | Champs obligatoires | Exigence | Clé de corrélation |
| --- | --- | --- | --- |
| Journaux | horodatage, niveau, identifiant de requête, message, contexte | Sortie structurée, niveaux limités à DEBUG/INFO/WARN/ERROR | `trace_id` |
| Indicateurs | nom d'indicateur, étiquettes, valeur, heure de collecte | Mode de calcul et valeur cible explicites | `service` |
| Traçage distribué | identifiant de trace, identifiant de span, span parent, durée, statut | Appels interservices chaînables | `trace_id` |

## 3. Gabarit des champs de journalisation

```markdown
| Champ | Type | Obligatoire | Description | Exemple |
| --- | --- | --- | --- | --- |
| timestamp | ISO 8601 | oui | Heure UTC, fuseau horaire inclus | 2026-11-18T10:00:00Z |
| level | énumération | oui | DEBUG / INFO / WARN / ERROR | ERROR |
| trace_id | chaîne | oui | Identifiant unique de bout en bout | 4bf92f3577b34da6 |
| service | chaîne | oui | Nom du service | lint-api |
| message | chaîne | oui | Description brève sans information sensible | rule load failed |
| context | objet | non | Champs de contexte permettant la localisation | {"rule":"spacing"} |
```

## 4. Gabarit de définition SLI/SLO

```markdown
# Définition SLO : {{服务名}}

Version : {{v1.0}} ｜ Responsable : {{姓名}} ｜ Période de réexamen : {{每季度}}

## Périmètre du service
- Responsabilité du service : {{一句话}}
- Services dépendants : {{上游 / 下游}}
- Opérations critiques pour l'utilisateur : {{列出 2–5 项}}

## Définition des SLI
| SLI | Définition | Mode de calcul | Source de données |
| --- | --- | --- | --- |
| Disponibilité | requêtes réussies / requêtes totales | code HTTP < 500 considéré comme succès | {{监控面板}} |
| Latence | distribution des durées de requête | valeur du quantile P95 | {{监控面板}} |
| Taux d'erreur | requêtes en échec / requêtes totales | comptage des 5xx | {{监控面板}} |

## Objectifs SLO
| SLI | Valeur cible | Fenêtre statistique | Valeur actuelle | État d'atteinte |
| --- | --- | --- | --- | --- |
| Disponibilité | ≥ 99,9 % | 30 jours glissants | {{值}} | {{达标 / 未达标}} |
| Latence P95 | < 300 ms | 7 jours glissants | {{值}} | {{达标 / 未达标}} |
| Taux d'erreur | < 0,1 % | 24 heures glissantes | {{值}} | {{达标 / 未达标}} |

## Budget d'erreur
- Mode de calcul : {{1 - SLO 目标值，按统计窗口换算}}
- Alertes de consommation : {{消耗达 50% / 75% / 90% 时分别通知}}
- Politique d'épuisement : {{冻结非关键发布，优先修复稳定性}}
```

## 5. Gabarit de règle d'alerte

```markdown
### ALERT-{{三位序号}} : {{告警名称}}

- SLI associé : {{可用性 / 延迟 / 错误率}}
- Expression : {{可执行的查询表达式}}
- Seuil : {{数值 + 单位}}
- Durée : {{N 分钟}}
- Niveau de gravité : {{P0 / P1 / P2}}
- Responsable : {{姓名 / 值班组}}
- Exemple de déclenchement : {{给出一个会触发的样例数据}}
- Condition de silence : {{何时允许静默，须有到期时间}}

Consignes de traitement :
1. {{第一步：确认现象的数据源与命令}}
2. {{第二步：常见原因与对应处理}}
3. {{第三步：升级条件与升级对象}}
- Niveau d'incident associé : {{见事故响应规范的分级表}}
```

## 6. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Définition du SLI | Oui | Texte | Doit être un ratio ou un quantile calculable | requêtes réussies / requêtes totales |
| Mode de calcul | Oui | Texte | Préciser les conditions d'inclusion et d'exclusion | exclusion des requêtes de contrôle de santé |
| Valeur cible SLO | Oui | Seuil | valeur + unité + pourcentage | `≥ 99,9 %` |
| Fenêtre statistique | Oui | Durée | Fenêtre glissante, les formulations vagues en mois civil sont interdites | `30 jours glissants` |
| Budget d'erreur | Oui | Valeur | Déduit de l'objectif SLO | `43 minutes d'indisponibilité autorisées par mois` |
| Expression d'alerte | Oui | Requête | Directement copiable et exécutable | `rate(http_5xx[5m]) > 0.01` |
| Durée | Oui | Durée | Évite les fausses alertes sur fluctuation instantanée | `5 minutes` |
| Consignes de traitement | Oui | Liste | Au moins 3 étapes, avec conditions d'escalade | voir le gabarit |
| Condition de silence | Oui | Texte | Doit comporter une échéance | `pendant la fenêtre de publication, 30 minutes au maximum` |

## 7. Instructions de saisie

1. **Choix des SLI** : retenir 2 à 5 dimensions perceptibles par l'utilisateur ; les indicateurs de ressources internes tels que CPU ou mémoire ne remplacent pas les SLI utilisateur.
2. **Unification du mode de calcul** : un indicateur de même nom doit employer le même mode de calcul dans les journaux, les tableaux de supervision et les expressions d'alerte.
3. **Fixation des objectifs** : les objectifs SLO doivent se fonder sur les valeurs mesurées actuelles et la tolérance métier ; appliquer directement « quatre neuf » sans justification est interdit.
4. **Budget d'erreur** : indiquer le résultat de la conversion et les actions de consommation par palier ; lorsque le budget est épuisé, geler les publications non critiques.
5. **Alertes exécutables** : chaque alerte doit répondre aux trois questions « quoi surveiller, comment diagnostiquer, quand escalader » ; si une réponse manque, l'alerte ne doit pas être mise en service.
6. **Lutte contre la fatigue d'alerte** : une alerte n'ayant produit aucun traitement effectif pendant 30 jours consécutifs doit être abaissée de niveau ou supprimée, avec justification.
7. **Masquage** : si les champs de contexte des journaux peuvent contenir des clés, des jetons ou des données personnelles, le masquage doit être appliqué avant la sortie.

Erreurs courantes :

| Rédaction erronée | Problème | Mode de correction |
| --- | --- | --- |
| Utiliser le taux d'utilisation CPU comme SLI | Non perceptible par l'utilisateur | Utiliser la disponibilité, la latence et le taux d'erreur |
| Alerte indiquant seulement « service anormal » | Ni seuil ni consigne | Ajouter l'expression, le seuil et les étapes de traitement |
| Journalisation de l'en-tête de requête complet | Risque de fuite de données privées et de clés | Sortie en liste blanche des champs nécessaires |
| Alerte sans échéance de silence | Un silence prolongé provoque des non-détections | Fixer une durée de silence maximale |
| SLO sans fenêtre statistique | Objectif non évaluable | Ajouter la fenêtre glissante |

## 8. Exemple complet

```markdown
# Définition SLO : lint-api

Version : v1.0 ｜ Responsable : 王五 ｜ Période de réexamen : chaque trimestre

## Définition des SLI
| SLI | Définition | Mode de calcul | Source de données |
| --- | --- | --- | --- |
| Disponibilité | requêtes réussies / requêtes totales | code de statut < 500, hors contrôles de santé | Grafana lint-overview |
| Latence | durée des requêtes de vérification P95 | statistiques limitées au chemin /check | Grafana lint-overview |

## Objectifs SLO
| SLI | Valeur cible | Fenêtre statistique | Valeur actuelle | État d'atteinte |
| --- | --- | --- | --- | --- |
| Disponibilité | ≥ 99,9 % | 30 jours glissants | 99,94 % | atteint |
| Latence P95 | < 300 ms | 7 jours glissants | 268 ms | atteint |

## Budget d'erreur
- Mode de calcul : 0,1 % × 30 jours = 43 minutes/mois
- Alertes de consommation : 50 % notifier le responsable, 75 % notifier l'équipe d'astreinte, 90 % geler les publications non critiques
- Politique d'épuisement : suspendre les publications de fonctionnalités, seules les corrections de stabilité sont autorisées

### ALERT-001 : taux d'erreur 5xx au-delà du seuil
- SLI associé : disponibilité
- Expression : `rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])`
- Seuil : > 0,01
- Durée : 5 minutes
- Niveau de gravité : P1
- Responsable : 王五
- Consignes de traitement :
  1. Ouvrir Grafana lint-overview pour identifier le service d'origine de l'erreur
  2. Interroger les journaux ERROR et chaîner les appels par trace_id ; la cause courante est l'échec de chargement d'un plugin de règles
  3. Si la localisation n'aboutit pas sous 10 minutes, escalader vers 李四 et déclencher le processus d'incident P1
```

## Fichiers associés

- Mode de calcul et définition des indicateurs : [spécification des indicateurs de mesure de la qualité](./quality-metrics-specification.md)
- Processus de traitement après alerte : [spécification de réponse aux incidents](./incident-response-specification.md)
- Contrôle de santé au déploiement : [spécification de déploiement et de restauration](./deployment-and-rollback-specification.md)
- Masquage des journaux et protection de la vie privée : [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)
- Éléments de dépannage courants : [spécification de dépannage](./troubleshooting-specification.md)
