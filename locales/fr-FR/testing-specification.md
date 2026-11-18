# Spécification des tests

> Problème que ce fichier résout : définir les niveaux de test, les gabarits du plan de test et des cas de test, leurs champs, la base de calcul de la couverture et les critères d'exécution, afin de garantir que chaque exigence est vérifiable et que chaque modification peut être soumise à régression.

## 1. Dispositions de la spécification

1. Les tests se répartissent en trois niveaux : unitaire, intégration et bout en bout ; chaque niveau doit préciser l'objet testé et le périmètre non testé, afin d'éviter les couvertures redondantes.
2. Chaque exigence de niveau « doit » doit correspondre à au moins un cas de test ; la relation de traçabilité est décrite dans la [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md).
3. La correction d'un défaut doit d'abord ajouter un cas de régression, puis modifier le code ; le cas de régression doit pouvoir reproduire le défaut d'origine.
4. Le seuil de couverture est fixé par le projet et inscrit dans la CI ; il ne doit pas être inférieur au seuil établi (correspond à la règle absolue H9).
5. Les tests doivent être reproductibles et ne dépendre d'aucun état externe ; ceux qui dépendent de services externes doivent être isolés ou simulés par mock.
6. Le nommage des tests doit exprimer le comportement testé et le résultat attendu ; les tests, le lint, le format et la vérification de types doivent s'exécuter automatiquement dans la CI, et la fusion n'est autorisée qu'en cas de succès complet (voir la [spécification de revue de code](./code-review-specification.md)).

## 2. Niveaux de test

| Niveau | Objet testé | Doit couvrir | Ne couvre pas | Outils typiques |
| --- | --- | --- | --- | --- |
| Tests unitaires | Fonctions, modules de logique pure | Logique centrale, conditions limites, branches d'exception | Coopération entre modules, E/S externes | Runner natif du langage |
| Tests d'intégration | Coopération entre modules | Chaînes d'appel clés, adaptateurs, interactions de persistance | Parcours utilisateur complet | Conteneur de test / serveur mock |
| Tests de bout en bout | Scénarios utilisateur complets | Principaux chemins d'usage, boucle métier clé | Énumération exhaustive des branches, tests de charge | Pilote de navigateur / CLI |

## 3. Gabarit de plan de test

```markdown
# Plan de test : {{项目名称}} {{版本号}}

Version : {{v1.0}} ｜ Périmètre d'exigences correspondant : {{REQ-001 ~ REQ-020}} ｜ Responsable : {{姓名}}

## Périmètre des tests
- Inclus : {{模块 / 需求编号列表}}
- Exclus : {{不在本期验证的范围及原因}}
- Critères de réussite du lancement associés : {{G1 / G2}}

## Stratégie par niveau
| Niveau | Objet testé | Objectif de couverture | Outils | Moment d'exécution |
| --- | --- | --- | --- | --- |
| Unitaire | {{对象}} | {{覆盖率阈值}} | {{工具}} | À chaque commit |
| Intégration | {{对象}} | {{关键链路清单}} | {{工具}} | À chaque fusion |
| Bout en bout | {{场景}} | {{主要路径清单}} | {{工具}} | À chaque publication |

## Environnement et données
- Environnement : {{操作系统 / 运行时版本 / 依赖服务版本}}
- Données de test : {{构造方式；禁止使用生产敏感数据}}
- Dépendances externes : {{需 mock 的服务及隔离方式}}

## Conditions d'entrée et de sortie
- Entrée : {{进入测试的前置条件，如开发自测通过}}
- Sortie : {{通过率 100%、无 P0/P1 缺陷、覆盖率达标}}
- Conditions de suspension : {{阻塞性问题清单}}

## Risques et arbitrages
- Périmètre non testé et raisons : {{例如第三方付费接口以 mock 替代}}
- Risques connus : {{例如并发场景仅做 10 路验证}}
```

## 4. Gabarit de cas de test

```markdown
### TC-{{三位序号}} : {{用例标题}}

- Exigence associée : {{REQ-001}}
- Niveau : {{单元 / 集成 / 端到端}}
- Priorité : {{P0 / P1 / P2}}
- Type : {{正常 / 边界 / 异常}}
- Conditions préalables : {{环境与数据准备}}
- Étapes et résultats attendus :
  | Étape | Action | Résultat attendu |
  | --- | --- | --- |
  | 1 | {{操作}} | {{可判定的结果}} |
  | 2 | {{操作}} | {{可判定的结果}} |
- Nettoyage : {{恢复环境的操作；无则写「无」}}
```

## 5. Définition des champs

### 5.1 Champs du plan de test

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Périmètre d'exigences correspondant | Oui | Liste | Utiliser un intervalle de numéros REQ | `REQ-001 ~ REQ-020` |
| Périmètre exclu | Oui | Texte | Préciser la raison de la non-réalisation | `interface payante non testée : aucun compte de test` |
| Objectif de couverture | Oui | Seuil | La couverture doit être un pourcentage numérique | `couverture de lignes ≥ 80 %` |
| Moment d'exécution | Oui | Énumération | Commit / fusion / publication | `à chaque fusion` |
| Données de test | Oui | Texte | Déclarer le mode de construction ; données sensibles réelles interdites | `générées via fixture` |
| Conditions de sortie | Oui | Texte | Évaluables, avec seuil de niveau de défaut | `aucun défaut P0/P1 non clos` |

### 5.2 Champs du cas de test

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Numéro | Oui | `TC-NNN` | Continu, non réutilisé | `TC-007` |
| Exigence associée | Oui | Liste | Au moins un numéro REQ | `REQ-001` |
| Priorité | Oui | Énumération | P0 / P1 / P2 | `P0` |
| Type | Oui | Énumération | Nominal / limite / exceptionnel | `limite` |
| Étapes et résultats attendus | Oui | Tableau | Chaque étape doit avoir un résultat attendu évaluable | Voir le gabarit |
| Nettoyage | Oui | Texte | Écrire « aucun » en l'absence de nettoyage ; ne pas laisser vide | `aucun` |

### 5.3 Base de calcul de la couverture

| Base | Définition | Niveau applicable | Seuil recommandé |
| --- | --- | --- | --- |
| Couverture de lignes | Nombre d'instructions exécutées / nombre total d'instructions | Unitaire | ≥ 80 % |
| Couverture de branches | Nombre de branches exécutées / nombre total de branches | Unitaire | ≥ 70 % |
| Couverture des exigences | Nombre d'exigences « doit » couvertes par des cas de test / nombre total d'exigences « doit » | Tous niveaux | 100 % |
| Couverture des chemins | Nombre de chemins principaux vérifiés / nombre total de chemins principaux identifiés | Bout en bout | 100 % |

Note sur les bases de calcul : la couverture est un moyen de détecter les zones non testées, et non un objectif de qualité en soi ; une couverture élevée ne remplace pas la qualité des assertions, celles-ci devant vérifier le comportement et non seulement exécuter le code.

## 6. Instructions de remplissage

1. **Exigence associée** : renseigner un numéro REQ ; les cas non rattachables doivent être versés au registre des tests exploratoires et non intégrés au jeu de cas officiel.
2. **Résultat attendu** : il doit être évaluable. « Renvoie un résultat correct » est non conforme ; « renvoie le code de statut 200 et le champ `name` non vide » est conforme.
3. **Répartition des types** : chaque exigence de niveau « doit » doit disposer d'au moins un cas nominal et d'un cas limite ou exceptionnel.
4. **Nettoyage** : les cas touchant des fichiers, une base de données ou un état global doivent comporter des étapes de nettoyage ; l'absence de nettoyage rend le cas incomplet.
5. **Cas de régression** : la correction d'un défaut doit être nommée avec le numéro du défaut en préfixe, par exemple `TC-007-regression-142`.
6. **Isolation** : les cas ne doivent pas dépendre de l'ordre d'exécution ; ceux qui partagent un état doivent le reconstruire dans les conditions préalables.

Erreurs fréquentes :

| Formulation erronée | Problème | Mode de correction |
| --- | --- | --- |
| Résultat attendu « fonctionne normalement » | Non évaluable | Écrire une valeur de retour ou un état précis |
| Cas sans exigence associée | Chaîne de traçabilité rompue | Ajouter le numéro REQ |
| Tester uniquement le chemin nominal | Défauts limites non détectés | Ajouter des cas exceptionnels et limites |
| Cas dépendant du résultat du cas précédent | Exécution non reproductible | Reconstruire l'état dans les conditions préalables |
| Tester avec des données de production | Risque de confidentialité et de conformité | Utiliser une fixture |

## 7. Exemple complet

```markdown
# Plan de test : markdown-lint-cli v1.0

Version : v1.0 ｜ Périmètre d'exigences correspondant : REQ-001 ~ REQ-014 ｜ Responsable : Wang Wu

## Périmètre des tests
- Inclus : moteur de règles, analyse des arguments de la CLI, sortie de rapport (REQ-001 ~ REQ-014)
- Exclus : intégration au greffon d'éditeur (reportée à v1.1, aucune exigence correspondante)
- Critères de réussite du lancement associés : G1, G2

## Stratégie par niveau
| Niveau | Objet testé | Objectif de couverture | Outils | Moment d'exécution |
| --- | --- | --- | --- | --- |
| Unitaire | Fonctions de règles | Couverture de lignes ≥ 85 % | Runner natif du langage | À chaque commit |
| Intégration | CLI → moteur de règles → rapport | 3 chaînes clés | Conteneur de test | À chaque fusion |
| Bout en bout | Vérification par lots sur un dépôt réel | 2 chemins principaux | Pilote shell | À chaque publication |

### TC-001 : Détection de l'espace manquant entre chinois et anglais
- Exigence associée : REQ-001
- Niveau : unitaire
- Priorité : P0
- Type : limite
- Conditions préalables : charger la règle `spacing`
- Étapes et résultats attendus :
  | Étape | Action | Résultat attendu |
  | --- | --- | --- |
  | 1 | Saisir « 使用Node.js开发 » | Renvoie 1 déclenchement, ligne 1 |
  | 2 | Saisir « 使用 Node.js 开发 » | Renvoie 0 déclenchement |
- Nettoyage : aucun
```

## Fichiers associés

- Traçabilité bidirectionnelle des exigences vers les cas : [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md)
- Bases de calcul par niveau et définitions des indicateurs : [spécification des indicateurs de mesure de la qualité](./quality-metrics-specification.md)
- Porte d'entrée : [porte qualité](./quality-gate.md)
- Dimension d'audit D6 : [matrice des dimensions d'audit](./review-dimension-matrix.md)
- Configuration d'exécution automatique de la CI : [spécification du flux de travail CI](./ci-workflow-specification.md)
- Exécution locale avant commit : [spécification de push et de publication](./push-and-release-specification.md)
