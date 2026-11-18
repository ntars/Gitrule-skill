# Spécification de revue de code

> Problème que ce fichier résout : définir le gabarit de description de la demande de fusion, le gabarit d'avis de revue, le registre de revue, les champs et le processus, afin de garantir la qualité de la fusion et le partage des connaissances.

## 1. Dispositions de la spécification

1. L'auteur doit indiquer dans la description de la PR l'objectif du changement, la portée d'impact et les résultats d'auto-test ; le gabarit figure dans la [spécification du flux de travail Git et des branches](./git-workflow-and-branching-specification.md).
2. Le relecteur doit formuler des avis concrets et exécutables, en distinguant « modification obligatoire » et « suggestion ».
3. Avant la fusion, au moins 1 relecteur doit avoir approuvé et la CI doit être entièrement verte (correspond à la règle absolue H9) ; l'auto-approbation de sa propre PR par l'auteur est interdite.
4. En cas de divergence sur un avis de revue, l'arbitrage est porté au mainteneur (voir la [spécification du code de conduite](./code-of-conduct-specification.md)).
5. Après la fusion, la branche source est supprimée afin de maintenir une liste de branches propre.

## 2. Liste de contrôle de revue

Le relecteur doit confirmer chaque point :

| # | Dimension | Point de contrôle | Décision |
| --- | --- | --- | --- |
| 1 | Exactitude | Logique correcte, cas limites et exceptions traités | Conforme / à modifier |
| 2 | Tests | Le changement dispose de tests correspondants, les tests passent | Conforme / à modifier |
| 3 | Style | Conforme à la [spécification de style de code](./code-style-specification.md) | Conforme / à modifier |
| 4 | Sécurité | Aucune information sensible, aucun risque d'injection, contrôle des permissions correct | Conforme / à modifier |
| 5 | Documentation | Toute modification d'interface ou de comportement est répercutée dans la documentation | Conforme / à modifier |
| 6 | Périmètre | Le changement reste ciblé, sans modification sans rapport | Conforme / à modifier |
| 7 | Message de commit | Conforme à la [spécification des messages de commit](./commit-message-specification.md) | Conforme / à modifier |
| 8 | Traçabilité | La matrice de traçabilité des exigences est à jour | Conforme / à modifier |

## 3. Gabarit d'avis de revue

```markdown
### Avis {{序号}} : {{一句话标题}}

- Niveau : {{必须修改 / 建议 / 提问}}
- Emplacement : {{文件路径:行号}}
- Problème : {{描述可观察的问题，不评价人}}
- Fondement : {{规范条款 / 需求编号 / 风险说明}}
- Suggestion : {{具体的修改方式或替代方案}}

Exemple :
### Avis 1 : Branche d'exception non couverte
- Niveau : modification obligatoire
- Emplacement : `src/rules/spacing.ts:42`
- Problème : une exception est levée lorsque l'entrée contient du Markdown incomplet, sans retourner le résultat de déclenchement de la règle.
- Fondement : REQ-001, condition d'acceptation n° 2 (chemin limite).
- Suggestion : intercepter ici l'exception d'analyse et retourner un déclenchement « échec d'analyse », puis ajouter un cas limite.
```

## 4. Gabarit de registre de revue

```markdown
## Registre de revue : {{PR 编号}}

Relecteur : {{姓名}} ｜ Date de revue : {{YYYY-MM-DD}} ｜ Tour : {{第 N 轮}}

| Numéro d'avis | Niveau | Conclusion de traitement | Responsable du traitement | Mode de vérification |
| --- | --- | --- | --- | --- |
| 1 | Modification obligatoire | Modifié | Auteur | Voir commit abc1234 |
| 2 | Suggestion | Non retenu | Auteur | Raison : {{说明}} |

Conclusion : {{批准 / 需修改后再审 / 拒绝}}
- Conditions d'approbation : tous les points « modification obligatoire » sont traités, CI entièrement verte.
- Points en suspens : {{无 / 列出}}
```

## 5. Définition des champs

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Niveau | Oui | Énumération | Modification obligatoire / suggestion / question | `modification obligatoire` |
| Emplacement | Oui | `chemin:numéro de ligne` | Précis jusqu'à la ligne ; écrire seulement le nom de fichier est interdit | `src/parser.ts:42` |
| Problème | Oui | Texte | Décrire le phénomène, sans juger l'auteur | `exception d'analyse non interceptée` |
| Fondement | Oui | Texte | Disposition de la spécification ou numéro REQ | `REQ-001, condition d'acceptation 2` |
| Suggestion | Oui | Texte | Exécutable ; ne pas se contenter de « merci d'optimiser » | `intercepter l'exception et retourner le déclenchement` |
| Conclusion de traitement | Oui | Énumération | Modifié / non retenu / reporté | `modifié` |
| Mode de vérification | Oui | Texte | Hachage de commit ou mode de re-vérification | `voir commit abc1234` |
| Conclusion | Oui | Énumération | Approuvée / à modifier puis re-revue / refusée | `approuvée` |

## 6. Instructions de remplissage

1. **Distinction des niveaux** : « modification obligatoire » désigne un problème bloquant la fusion (exactitude, sécurité, absence de test) ; « suggestion » n'affecte pas la fusion ; « question » exige une clarification de l'auteur sans modification imposée.
2. **Formulation des avis** : décrire un problème observable ; les formulations évaluatives du type « c'est très mal écrit ici » sont interdites.
3. **Emplacement** : préciser jusqu'au numéro de ligne ; pour un problème couvrant plusieurs fichiers, l'indiquer séparément dans chaque avis.
4. **Fondement** : rattacher à une référence dès que possible ; en l'absence de fondement normatif, décrire le risque ou l'impact ; « je pense que » est interdit.
5. **Conclusion de traitement** : « non retenu » doit être motivé ; « reporté » doit indiquer l'emplacement de suivi ultérieur.
6. **Approbation** : confirmer que tous les points « modification obligatoire » sont clos et que la CI est entièrement verte ; l'auteur ne doit pas approuver sa propre PR.
7. **Divergences** : en cas de désaccord entre relecteur et auteur, l'arbitrage revient au mainteneur et la conclusion est consignée dans le registre de revue.

Erreurs fréquentes :

| Formulation erronée | Problème | Mode de correction |
| --- | --- | --- |
| « Ça ne va pas ici » | Aucun problème, aucun fondement, aucune suggestion | Ajouter les trois éléments |
| « Merci d'optimiser un peu les performances » | Non exécutable | Fournir une méthode concrète et un indicateur de décision |
| Indiquer seulement le nom de fichier sans numéro de ligne | Localisation difficile | Préciser jusqu'à la ligne |
| Auto-approbation par l'auteur | Viole la règle | Faire relire par une autre personne |
| « Modification obligatoire » utilisé pour une préférence personnelle | Usage abusif du niveau | Rétrograder en « suggestion » |

## 7. Exemple complet

```markdown
## Registre de revue : #12

Relecteur : Li Si ｜ Date de revue : 2026-11-18 ｜ Tour : tour n° 1

| Numéro d'avis | Niveau | Conclusion de traitement | Responsable du traitement | Mode de vérification |
| --- | --- | --- | --- | --- |
| 1 | Modification obligatoire | Modifié | Wang Wu | Voir commit a1b2c3d |
| 2 | Suggestion | Non retenu | Wang Wu | Raison : le QPS actuel n'atteint pas le goulot d'étranglement, éviter la surconception |
| 3 | Question | Clarifié | Wang Wu | Explication complétée dans le corps de la PR |

Conclusion : approuvée
- Conditions d'approbation : tous les points « modification obligatoire » sont traités, CI entièrement verte (run #128).
- Points en suspens : aucun
```

## Fichiers associés

- Description de PR et modèle de branches : [spécification du flux de travail Git et des branches](./git-workflow-and-branching-specification.md)
- Base des contrôles de style : [spécification de style de code](./code-style-specification.md)
- Critères de réussite des tests : [spécification des tests](./testing-specification.md)
- Mise à jour des états de traçabilité : [spécification de la matrice de traçabilité des exigences](./requirements-traceability-matrix-specification.md)
- Porte qualité : [porte qualité](./quality-gate.md)
- Base d'arbitrage des divergences : [spécification du code de conduite](./code-of-conduct-specification.md)
- Les contrôles automatisés relèvent de la dimension D9 : [matrice des dimensions d'audit](./review-dimension-matrix.md)
