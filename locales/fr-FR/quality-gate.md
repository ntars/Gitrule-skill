# Porte qualité

> Problème que ce fichier résout : définir les conditions de passage des trois niveaux de porte, le gabarit de liste d'évaluation et ses champs, afin de garantir une décision de passage au push uniforme, exécutable et vérifiable.

## 1. Les trois niveaux de porte

| Niveau | Signification | Condition de passage |
| --- | --- | --- |
| Gate A · Porte de sécurité | Clés, vie privée, licences, fichiers volumineux | Zéro P0 |
| Gate B · Porte de qualité | Build, tests, lint, convention de commit, protection de branche | Zéro P0, P1 enregistrés en tâches à faire |
| Gate C · Porte de page d'accueil | README, métadonnées, matrice documentaire, badges, liens | Zéro P0, P1 ≤ 3 et planifiés |

Ce n'est que si A, B et C sont tous au vert que l'on émet `✅ ALLOW PUSH`. Les éléments non conformes doivent être corrigés ou accompagnés d'une justification ; le résultat est consigné dans le [format de rapport d'audit](./audit-report-format.md).

## 2. Les 14 contrôles avant livraison

Chaque point est évalué avant la livraison du document ; tout élément non conforme doit être corrigé ou accompagné d'une justification.

| N° | Point de contrôle | Critère d'évaluation |
| --- | --- | --- |
| G1 | Tournures orales et ambiguïtés | Recherche textuelle des tournures orales et des références vagues dans l'ensemble du document, zéro occurrence |
| G2 | Complétude des sections | Les versions chinoise et anglaise comptent toutes deux 20 chapitres, dans le même ordre |
| G3 | Cohérence entre fonctionnalités et arborescence | Chaque fonctionnalité décrite dans le README trouve un module correspondant dans l'arborescence |
| G4 | Preuve des caractéristiques | Chaque caractéristique dispose d'une preuve ou est marquée « à compléter » |
| G5 | Couverture des détails de conception | Les 10 catégories de la section 8 disposent chacune d'une entrée ou sont marquées « non applicable » |
| G6 | Complétude des dépendances | Le nombre de dépendances directes et indirectes correspond à l'arbre de dépendances |
| G7 | Exactitude des licences | L'identifiant SPDX de chaque dépendance correspond à la déclaration officielle |
| G8 | Texte intégral des licences | Toutes les licences exigeant le texte intégral sont accompagnées de leur version originale en anglais |
| G9 | Mentions de copyright | Les mentions de copyright du projet et celles des tiers sont complètes |
| G10 | Synchronisation bilingue | Sections, tableaux, terminologie et blocs de code sont identiques des deux côtés |
| G11 | Exécutabilité des commandes | Les commandes d'installation, de démarrage rapide et de push sont directement exécutables |
| G12 | Récapitulatif des points à confirmer | Tous les points à confirmer sont récapitulés et localisables |
| G13 | Provenance des ressources | Toutes les ressources disposent d'une source et d'une licence documentées |
| G14 | Informations sensibles | Absence de clés, jetons, adresses de réseau interne et données personnelles |

## 3. Gabarit de liste d'évaluation de la porte

```markdown
# Évaluation de la porte : {{项目名称}} {{版本号}}

Date d'évaluation : {{YYYY-MM-DD}} ｜ Évaluateur : {{姓名}} ｜ Dépôt : {{owner/repo}}

## Gate A · Porte de sécurité
| N° | Point de contrôle | Conclusion | Preuve | Niveau | Traitement |
| --- | --- | --- | --- | --- | --- |
| A1 | Clés dans l'espace de travail | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |
| A2 | Clés dans l'historique | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |
| A3 | Nettoyage des informations sensibles | PASS / FAIL / SKIP | {{证据}} | {{P0}} | {{动作}} |
| A4 | Présence et type de LICENSE | PASS / FAIL / SKIP | {{路径}} | {{P0}} | {{动作}} |
| A5 | Fichiers volumineux et LFS | PASS / FAIL / SKIP | {{命令输出}} | {{P0}} | {{动作}} |

Conclusion : {{PASS / FAIL}}, points en suspens : {{列出 / 无}}

## Gate B · Porte de qualité
| N° | Point de contrôle | Conclusion | Preuve | Niveau | Traitement |
| --- | --- | --- | --- | --- | --- |
| B1 | Build réussi | PASS / FAIL / SKIP | {{CI URL}} | {{P0}} | {{动作}} |
| B2 | Tests réussis | PASS / FAIL / SKIP | {{CI URL}} | {{P0}} | {{动作}} |
| B3 | lint / format | PASS / FAIL / SKIP | {{CI URL}} | {{P1}} | {{动作}} |
| B4 | Convention de message de commit | PASS / FAIL / SKIP | {{git log}} | {{P1}} | {{动作}} |
| B5 | Protection de branche | PASS / FAIL / SKIP | {{平台设置截图说明}} | {{P0}} | {{动作}} |

Conclusion : {{PASS / FAIL}}, points en suspens : {{列出 / 无}}

## Gate C · Porte de page d'accueil
| N° | Point de contrôle | Conclusion | Preuve | Niveau | Traitement |
| --- | --- | --- | --- | --- | --- |
| C1 | Les quatre éléments du README | PASS / FAIL / SKIP | {{路径:行号}} | {{P1}} | {{动作}} |
| C2 | Matrice documentaire complète | PASS / FAIL / SKIP | {{清单}} | {{P1}} | {{动作}} |
| C3 | Métadonnées complètes | PASS / FAIL / SKIP | {{平台设置}} | {{P1}} | {{动作}} |
| C4 | Badges fonctionnels | PASS / FAIL / SKIP | {{HTTP 检查}} | {{P2}} | {{动作}} |
| C5 | Liens valides | PASS / FAIL / SKIP | {{校验输出}} | {{P1}} | {{动作}} |

Conclusion : {{PASS / FAIL}}, points en suspens : {{列出 / 无}}

## Les 14 contrôles avant livraison
| N° | Conclusion | Preuve | Traitement |
| --- | --- | --- | --- |
| G1 ~ G14 | {{PASS / FAIL / SKIP}} | {{证据}} | {{动作}} |

## Décision globale
- A : {{PASS / FAIL}} ｜ B : {{PASS / FAIL}} ｜ C : {{PASS / FAIL}}
- Conclusion de passage : {{✅ ALLOW PUSH / ⛔ BLOCK PUSH}}
- Motif de blocage : {{无 / 列出 P0}}
```

## 4. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Évaluateur | Oui | Texte | Unique, l'emploi de « équipe » est interdit | `Wang Wu` |
| Conclusion | Oui | Énumération | PASS / FAIL / SKIP | `PASS` |
| Preuve | Oui | Texte | Chemin + numéro de ligne ou sortie de commande, toute évaluation sans preuve est interdite | `gitleaks: 0 findings` |
| Niveau | Obligatoire sous condition | Énumération | Obligatoire en cas de FAIL : P0 / P1 / P2 | `P0` |
| Traitement | Obligatoire sous condition | Texte | Obligatoire en cas de FAIL : action concrète et responsable | `renouveler la clé et nettoyer l'historique` |
| Motif de SKIP | Obligatoire sous condition | Texte | Obligatoire en cas de SKIP, tout contournement sans motif est interdit | `aucun script de build` |
| Conclusion de passage | Oui | Énumération | ALLOW PUSH / BLOCK PUSH | `BLOCK PUSH` |
| Motif de blocage | Obligatoire sous condition | Texte | Obligatoire en cas de BLOCK, énumérer les P0 | `A2 : clé détectée dans l'historique` |

## 5. Consignes de saisie

1. **Preuve obligatoire** : chaque évaluation doit être fondée sur une preuve ; un PASS sans preuve est réputé invalide et doit être requalifié en SKIP avec justification.
2. **Correspondance des niveaux** : un FAIL doit porter un niveau ; un P0 bloque directement le passage, un P1 doit être enregistré en tâche à faire, un P2 est consigné en recommandation.
3. **Seuil de la Gate C** : le PASS n'est possible que si P1 ≤ 3 et que les points sont planifiés ; au-delà, il faut déclasser ou bloquer.
4. **Usage du SKIP** : lorsque le contrôle est impossible, indiquer SKIP + motif, ne jamais écrire PASS ; effectuer le contrôle ultérieurement lorsque les conditions sont réunies.
5. **Cohérence** : l'évaluation de la porte doit être cohérente avec les niveaux P0/P1/P2 de la [matrice des dimensions de revue](./review-dimension-matrix.md) et avec les règles de blocage des [règles absolues](./hard-rules.md).
6. **Passage** : ce n'est que si les trois niveaux sont au vert que l'on émet `✅ ALLOW PUSH` ; tout FAIL impose `⛔ BLOCK PUSH` avec énumération des motifs de blocage.
7. **Format de livraison** : le résultat de l'évaluation est produit selon le [format de rapport d'audit](./audit-report-format.md) ; après validation, appliquer la [spécification de push et de publication](./push-and-release-specification.md).

Erreurs fréquentes :

| Formulation erronée | Problème | Correction |
| --- | --- | --- |
| Conclusion PASS mais preuve vide | Évaluation invalide | Compléter la preuve ou requalifier en SKIP |
| ALLOW PUSH alors que les P0 ne sont pas à zéro | Violation des règles absolues | Requalifier en BLOCK PUSH |
| SKIP sans motif | Soupçon d'omission de contrôle | Ajouter le motif |
| Gate C avec 5 points P1 mais PASS | Seuil dépassé | Déclasser ou bloquer |
| Résultat d'évaluation rédigé en texte sans liste | Non vérifiable | Remplir le gabarit point par point |

## 6. Exemple complet

```markdown
# Évaluation de la porte : markdown-lint-cli v1.0.0

Date d'évaluation : 2026-11-20 ｜ Évaluateur : Wang Wu ｜ Dépôt : example/markdown-lint-cli

## Gate A · Porte de sécurité
| N° | Point de contrôle | Conclusion | Preuve | Niveau | Traitement |
| --- | --- | --- | --- | --- | --- |
| A1 | Clés dans l'espace de travail | PASS | gitleaks detect: 0 findings | — | — |
| A2 | Clés dans l'historique | PASS | gitleaks --log-opts=--all: 0 findings | — | — |
| A4 | Présence et type de LICENSE | PASS | LICENSE ligne 1 : MIT | — | — |
| A5 | Fichiers volumineux et LFS | PASS | find -size +50M: aucun | — | — |

Conclusion : PASS, points en suspens : aucun

## Gate B · Porte de qualité
| N° | Point de contrôle | Conclusion | Preuve | Niveau | Traitement |
| --- | --- | --- | --- | --- | --- |
| B1 | Build réussi | PASS | run #128 | — | — |
| B2 | Tests réussis | PASS | 132/132 passed | — | — |
| B4 | Convention de message de commit | PASS | git log --oneline : tous conformes | — | — |

Conclusion : PASS, points en suspens : aucun

## Décision globale
- A : PASS ｜ B : PASS ｜ C : PASS
- Conclusion de passage : ✅ ALLOW PUSH
- Motif de blocage : aucun
```

## Fichiers associés

- Base d'évaluation et niveaux d'échec : [matrice des dimensions de revue](./review-dimension-matrix.md)
- Règles dont la violation bloque : [règles absolues](./hard-rules.md)
- Format de sortie du résultat : [format de rapport d'audit](./audit-report-format.md)
- Après validation de la porte : [spécification de push et de publication](./push-and-release-specification.md)
- Source des preuves de la porte de sécurité : [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)
- Source des preuves de la porte de qualité : [spécification de tests](./testing-specification.md), [spécification du flux de travail CI](./ci-workflow-specification.md)
- Base d'évaluation de la porte de page d'accueil : [gabarit standard de README](./readme-standard-template.md), [matrice documentaire](./document-matrix.md)
