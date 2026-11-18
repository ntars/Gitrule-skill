# Spécification des workflows Git et des branches

> Problème que ce fichier résout : définir le modèle de branches, les règles de nommage, le gabarit de description des demandes de fusion et la stratégie de fusion, afin de garantir la stabilité de la ligne principale, la fluidité de la collaboration et la traçabilité des changements.

## 1. Dispositions de la spécification

1. La branche par défaut (`main` ou `master`) doit être protégée ; le push direct y est interdit (règle absolue H7).
2. Toute modification passe par une branche personnelle puis une demande de fusion vers la ligne principale.
3. Les branches longue durée et les branches courte durée doivent être clairement distinguées, afin d'éviter qu'une branche ne reste durablement non fusionnée.
4. Le `git push --force` sur une branche publique est interdit ; pour réécrire une branche personnelle, utilisez `--force-with-lease` (règle absolue H8).
5. Le rebase ou l'amend sur une branche publique déjà poussée est interdit ; avant fusion, l'intégration continue et la revue de code doivent être franchies.

## 2. Modèle de branches

| Type de branche | Cycle de vie | Créée depuis | Fusionnée vers | Format de nommage | Exemple |
| --- | --- | --- | --- | --- | --- |
| Branche par défaut | Longue durée | — | — | `main` | `main` |
| Branche de fonctionnalité | Courte durée, ≤ 2 semaines | `main` | `main` | `feat/<description courte>` | `feat/user-login` |
| Branche de correction | Courte durée, ≤ 1 semaine | `main` | `main` | `fix/<description courte>` | `fix/token-expiry` |
| Branche de documentation | Courte durée | `main` | `main` | `docs/<description courte>` | `docs/api-guide` |
| Branche de version | Durée moyenne | `main` | `main` + tag | `release/<version>` | `release/1.2.0` |
| Correction d'urgence | Courte durée, ≤ 24 heures | tag de version | `main` + tag | `hotfix/<description courte>` | `hotfix/payment-error` |

Règle de nommage : kebab-case en minuscules, la description courte doit exprimer l'intention ; les noms `test`, `temp`, `wip`, `my-xxx` sont interdits ; en cas de rattachement à une exigence, ajoutez le numéro d'exigence, par exemple `feat/spacing-rule-req001`.

## 3. Gabarit de description des demandes de fusion

```markdown
## Objectif du changement
{{一句话说明为什么需要此变更，关联需求编号}}

## Contenu du changement
- {{具体改动 1}}
- {{具体改动 2}}

## Périmètre d'impact
- Modules concernés : {{模块名}}
- Rupture de compatibilité : {{是 / 否；是则给出迁移说明}}
- Configuration ou migration de données concernées : {{是 / 否；是则说明}}

## Méthode de vérification
- Commande d'auto-test : {{命令}}
- Tests ajoutés ou modifiés : {{TC 编号}}
- Adresse d'exécution de l'intégration continue : {{URL}}

## Rattachements
- Exigence : {{REQ-NNN}}
- Matrice de traçabilité : {{已更新 / 待更新}}
- Documentation : {{docs/api.md#章节 / 无}}
- Issue : {{#编号 / 无}}

## Auto-vérification
- [ ] Le message de commit respecte la spécification
- [ ] Aucune information sensible n'est incluse
- [ ] La matrice de traçabilité des exigences a été mise à jour
- [ ] Les changements incompatibles ont été consignés dans le journal des modifications
```

## 4. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Description courte de la branche | Oui | kebab-case | Exprime l'intention de façon autonome, les termes sans information sont interdits | `spacing-rule` |
| Exigence rattachée | Oui | `REQ-NNN` | Conforme au numéro de lancement | `REQ-001` |
| Objectif du changement | Oui | Texte | Explicite le « pourquoi », et non le « quoi » | `Corrige les faux positifs sur la ponctuation chinoise` |
| Périmètre d'impact | Oui | Texte | Doit préciser s'il y a rupture de compatibilité | `Non` |
| Commande d'auto-test | Oui | Commande | Copiable et exécutable | `npm test -- -t spacing` |
| Numéro de test | Oui | `TC-NNN` | Conforme au numéro de la spécification des tests | `TC-001` |
| Adresse de l'intégration continue | Oui | URL | Permet au relecteur de vérifier | `https://github.com/.../runs/123` |
| Liste d'auto-vérification | Oui | Cases à cocher | Cocher point par point, ne jamais tout cocher d'un coup | — |

## 5. Instructions de saisie

1. **Cycle de vie des branches** : une branche de fonctionnalité non fusionnée au-delà de 2 semaines doit voir sa raison exposée en rétrospective d'itération, puis être découpée ou fermée.
2. **Nommage de la description courte** : reprendre le nom noyau de l'objectif du changement et l'action ; les noms vagues comme `fix2` ou `new-feature` sont interdits.
3. **Objectif du changement** : décrire le problème et la valeur apportée ; « mise à jour du code » ou « optimisation de la logique » ne sont pas acceptables.
4. **Périmètre d'impact** : en cas de rupture de compatibilité cochée, il faut également marquer `BREAKING CHANGE:` dans le journal des modifications.
5. **Commande d'auto-test** : le relecteur doit pouvoir la copier et l'exécuter directement pour obtenir la même conclusion ; pour les étapes complexes, indiquer le chemin du script.
6. **Matrice de traçabilité** : avant la fusion de la demande de fusion, il faut mettre à jour les champs de demande de fusion d'implémentation et d'état dans la [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md).
7. **Force push** : n'utilisez `--force-with-lease` que sur votre propre branche non relue par d'autres, et précisez la raison dans la demande de fusion.

Erreurs fréquentes :

| Formulation erronée | Problème | Correction |
| --- | --- | --- |
| Nom de branche `test`, `temp` | Aucune information sur l'intention | Remplacer par `feat/<capacité précise>` |
| Description de demande de fusion réduite à « correction de bug » | Impossible d'évaluer l'impact | Ajouter l'objectif, l'impact et la méthode de vérification |
| Push direct vers `main` | Violation de H7 | Passer par une fusion de demande de fusion |
| Force push après réécriture d'une branche déjà relue | La conclusion de la revue devient caduque | Ajouter un commit répondant aux remarques |
| Ne pas supprimer la branche source après fusion | La liste des branches se gonfle | Supprimer immédiatement après fusion |

## 6. Exemple complet

```markdown
## Objectif du changement
Corriger le faux positif de la règle d'espacement lorsqu'une ponctuation chinoise est adjacente à un mot anglais (REQ-004).

## Contenu du changement
- Ajout d'une détection de frontière de ponctuation dans le moteur de règles
- Ajout du cas de régression correspondant

## Périmètre d'impact
- Modules concernés : règle spacing
- Rupture de compatibilité : non
- Configuration ou migration de données concernées : non

## Méthode de vérification
- Commande d'auto-test : `npm test -- -t "中文标点"`
- Tests ajoutés ou modifiés : TC-007-regression-142
- Adresse d'exécution de l'intégration continue : https://github.com/example/markdown-lint-cli/actions/runs/128

## Rattachements
- Exigence : REQ-004
- Matrice de traçabilité : mise à jour
- Documentation : aucune
- Issue : #142

## Auto-vérification
- [x] Le message de commit respecte la spécification
- [x] Aucune information sensible n'est incluse
- [x] La matrice de traçabilité des exigences a été mise à jour
- [x] Les changements incompatibles ont été consignés dans le journal des modifications (aucun changement incompatible ici)
```

## Fichiers associés

- Critères de revue et niveaux de remarques : [spécification de la revue de code](./code-review-specification.md)
- Format des commits : [spécification des messages de commit](./commit-message-specification.md)
- Mise à jour de l'état de traçabilité : [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md)
- Branches et publication relèvent de la dimension D8 : [matrice des dimensions de revue](./review-dimension-matrix.md)
- Règles impératives H7/H8 : [règles absolues](./hard-rules.md)
- Opérations de push : [spécification de push et de publication](./push-and-release-specification.md)
