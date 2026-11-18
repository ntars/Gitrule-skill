# Spécification de la matrice de traçabilité des exigences

> Problème que ce fichier résout : définir le gabarit et les champs de la matrice de traçabilité bidirectionnelle entre exigences, conception, implémentation, tests et publication, afin de garantir la cohérence des références croisées entre les livrables de chaque phase du cycle de vie, l'évaluation de l'impact des changements et la détection des lacunes de couverture.

## 1. Dispositions de la spécification

1. Chaque exigence de niveau « doit » doit occuper une ligne dans la matrice de traçabilité et enregistrer les livrables de toute la chaîne, du lancement à la publication.
2. La relation de traçabilité doit être consultable dans les deux sens : en sens direct, de l'exigence vers les livrables en aval ; en sens inverse, du livrable vers l'exigence en amont.
3. Lorsqu'une exigence correspond à plusieurs livrables, utiliser une liste de numéros séparés par des virgules ; les numéros doivent être strictement identiques aux définitions des documents correspondants.
4. Toute modification d'exigence doit être consignée dans la matrice, avec la raison du changement, la portée d'impact et le décideur ; les valeurs d'origine ne doivent pas être écrasées directement.
5. La matrice doit être vérifiée avant chaque publication de version ; une exigence de niveau « doit » non close ne doit pas être publiée.
6. Base de calcul de la couverture : couverture des exigences = nombre d'exigences de niveau « doit » publiées / nombre total d'exigences de niveau « doit ».

## 2. Gabarit de matrice de traçabilité

```markdown
# Matrice de traçabilité des exigences : {{项目名称}}

Version : {{vX.Y.Z}} ｜ Auteur de la mise à jour : {{姓名}} ｜ Dernière vérification : {{YYYY-MM-DD}}

| ID d'exigence | Titre de l'exigence | Priorité | Objectif de lancement | Décision d'architecture | Document de conception | PR d'implémentation | Cas de test | Version publiée | État |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | {{标题}} | doit | G1 | ADR-0002 | docs/api.md#check | #12 | TC-001, TC-002 | v1.0.0 | vérifié |
| REQ-002 | {{标题}} | devrait | G2 | — | — | #15 | TC-005 | — | implémenté |
| REQ-003 | {{标题}} | doit | G1 | ADR-0003 | docs/architecture.md#flow | — | — | — | à implémenter |

États : à confirmer / confirmé / à implémenter / implémenté / vérifié / publié / abandonné
```

## 3. Gabarit d'index inverse

```markdown
## Recherche inverse par livrable

| Type de livrable | Numéro du livrable | ID d'exigence couverts |
| --- | --- | --- |
| Décision d'architecture | ADR-0002 | REQ-001, REQ-004 |
| Cas de test | TC-001 | REQ-001 |
| PR d'implémentation | #12 | REQ-001, REQ-007 |
| Version publiée | v1.0.0 | REQ-001, REQ-002 |
```

## 4. Gabarit de registre des modifications

```markdown
## Registre des modifications

| Date | ID d'exigence | Contenu de la modification | Raison | Portée d'impact | Décideur |
| --- | --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{REQ-NNN}} | {{字段：原值 → 新值}} | {{依据}} | {{受影响的下游产物}} | {{姓名}} |
```

## 5. Définition des champs

| Champ | Obligatoire | Type | Points de saisie | Exemple |
| --- | --- | --- | --- | --- |
| ID d'exigence | Oui | `REQ-NNN` | Conforme au numéro de la [spécification de lancement de projet et des exigences](./project-initiation-and-requirements-specification.md) | `REQ-001` |
| Priorité | Oui | Énumération | Doit / devrait / peut | `doit` |
| Objectif de lancement | Oui | `G-N` | Numéro d'objectif correspondant du dossier de lancement | `G1` |
| Décision d'architecture | Non | `ADR-NNNN` | Écrire « — » en l'absence de décision d'architecture ; ne pas laisser vide | `ADR-0002` |
| Document de conception | Non | `chemin#ancre` | Précis jusqu'à l'ancre de section | `docs/api.md#check` |
| PR d'implémentation | Non | `#nombre` | Numéro de PR, et non hachage de commit | `#12` |
| Cas de test | Oui | Liste `TC-NNN` | Au moins un ; en l'absence de cas, en expliquer la raison | `TC-001` |
| Version publiée | Non | `vX.Y.Z` | Conforme au tag | `v1.0.0` |
| État | Oui | Énumération | L'un des sept états, progression uniquement, sauf abandon | `vérifié` |
| Registre des modifications.Portée d'impact | Oui | Texte | Lister les ADR, PR et TC concernés | `ADR-0002, TC-001` |

## 6. Instructions de remplissage

1. **Cohérence des numéros** : les ID d'exigence, les numéros ADR et les numéros TC de la matrice doivent être strictement identiques, caractère par caractère, aux documents sources ; l'usage d'abréviations ou d'alias est interdit.
2. **Valeurs vides** : écrire « — » lorsque non applicable et « à compléter » lorsque non encore produit ; ces deux significations sont différentes et ne doivent pas être confondues.
3. **Index inverse** : après chaque mise à jour de la matrice directe, mettre à jour en parallèle l'index inverse ; en cas d'incohérence, la matrice directe fait foi et la correction est immédiate.
4. **Consignation des modifications** : avant de modifier un champ, ajouter d'abord une ligne dans le registre des modifications en indiquant l'ancienne et la nouvelle valeur ; il est interdit d'écraser directement.
5. **Vérification avant publication** : avant la publication, contrôler une par une que chaque exigence de niveau « doit » dispose d'un cas de test et d'une version publiée ; l'absence de l'un de ces éléments bloque la publication.
6. **Exigences abandonnées** : conserver la ligne sans la supprimer, passer l'état à « abandonné » et préciser la raison de l'abandon dans le registre des modifications.

Erreurs fréquentes :

| Formulation erronée | Problème | Mode de correction |
| --- | --- | --- |
| Champ du cas de test laissé vide | Lacune de couverture invisible | Renseigner « à compléter » et la solder avant publication |
| Renseigner un hachage de commit dans le champ PR | Impossible de localiser l'enregistrement de revue | Utiliser le numéro de PR |
| Modification directe de la valeur | Impact non traçable | Ajouter d'abord une entrée de modification |
| Retour de l'état « vérifié » à « implémenté » | Viole le principe de progression uniquement | Ouvrir un nouveau défaut et créer une ligne de traçabilité distincte |
| Incohérence entre l'index direct et l'index inverse | Références désaccordées | Aligner sur la matrice directe avant publication |

## 7. Exemple complet

```markdown
# Matrice de traçabilité des exigences : markdown-lint-cli

Version : v1.0.0 ｜ Auteur de la mise à jour : Wang Wu ｜ Dernière vérification : 2026-11-20

| ID d'exigence | Titre de l'exigence | Priorité | Objectif de lancement | Décision d'architecture | Document de conception | PR d'implémentation | Cas de test | Version publiée | État |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | Vérification des espaces chinois-anglais | doit | G1 | ADR-0002 | docs/api.md#rules-spacing | #12 | TC-001, TC-002 | v1.0.0 | publié |
| REQ-002 | Sortie de rapport JSON | devrait | G1 | — | docs/api.md#reporter | #15 | TC-011 | v1.0.0 | publié |
| REQ-003 | Intégration au greffon d'éditeur | peut | G2 | à compléter | à compléter | — | à compléter | — | à confirmer |

## Registre des modifications

| Date | ID d'exigence | Contenu de la modification | Raison | Portée d'impact | Décideur |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | REQ-003 | Priorité : devrait → peut | Délai insuffisant pour v1.0 | ADR-0005, TC-020 | Li Si |
```

## Fichiers associés

- Numéros d'exigence et conditions d'acceptation : [lancement de projet et spécification des exigences](./project-initiation-and-requirements-specification.md)
- Numéros de décision d'architecture : [spécification du document de conception d'architecture](./architecture-design-document-specification.md)
- Numéros de cas de test : [spécification des tests](./testing-specification.md)
- Versions publiées et tags : [spécification de gestion des versions](./version-management-specification.md)
- Description externe des changements de version : [spécification du journal des modifications](./changelog-specification.md)
- Rétrospective de processus en fin d'itération : [spécification de la rétrospective d'itération](./iteration-retrospective-specification.md)
