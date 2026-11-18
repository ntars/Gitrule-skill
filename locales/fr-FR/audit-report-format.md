# Format de rapport d'audit

> Problème que ce fichier résout : définir l'unique format de livraison du rapport d'audit, les exigences relatives aux champs et les exemples de saisie, afin que le rapport puisse être exécuté directement par un autre agent.

Le rapport est le seul livrable de la phase d'audit. Chaque problème doit être accompagné à la fois d'une preuve, d'un responsable et d'une action ; aucune conclusion non exécutable ne doit figurer dans le rapport.

## 1. Ossature du rapport

````markdown
# Rapport d'audit de push · {{仓库名}}

Conclusion : {{结论}}
Mode : {{模式}}
Dépôt : {{仓库名}} · {{可见性}} · {{许可证}} · Branche par défaut {{默认分支}}

## I. État des portes
| Porte | État | Points en suspens |
| --- | --- | --- |
| A Sécurité | {{门禁状态}} | {{未决项}} |
| B Qualité | {{门禁状态}} | {{未决项}} |
| C Page d'accueil | {{门禁状态}} | {{未决项}} |

## II. Liste des problèmes
| Niveau | Dimension | Problème | Preuve (chemin:ligne / sortie de commande) | Agent responsable | Action |
| --- | --- | --- | --- | --- | --- |
| {{等级}} | {{维度}} | {{问题}} | {{证据}} | {{责任agent}} | {{动作}} |

## III. État de la matrice documentaire
| Fichier | État | Éléments manquants / à modifier |
| --- | --- | --- |
| {{文件路径}} | {{状态}} | {{待改项}} |

## IV. Liste d'exécution du push
- [ ] {{推送规则}}

## V. Justification du passage
{{放行说明}}
````

## 2. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Nom du dépôt | Oui | Texte | Identique caractère par caractère au nom du dépôt GitHub | `markdown-lint-cli` |
| Conclusion | Oui | Énumération | Uniquement `ALLOW PUSH` ou `BLOCK PUSH` ; les P0 non résolus imposent la seconde valeur | `BLOCK PUSH` |
| Mode | Oui | Énumération | Un dépôt privé de scripts temporaires peut indiquer « audit dégradé », les autres « audit complet » | `audit complet` |
| Visibilité | Oui | Énumération | `private` / `public` ; la licence doit être revérifiée avant toute publication | `private` |
| Licence | Oui | Identifiant SPDX | Sans licence, écrire `NONE`, la conclusion devant alors être `BLOCK PUSH` | `MIT` |
| Branche par défaut | Oui | Texte | Indiquer le nom réel de la branche, ne pas écrire `main` par supposition | `main` |
| État des portes | Oui | Énumération ×3 | Une ligne par A/B/C ; un `SKIP` doit être justifié dans les « points en suspens » | `FAIL` |
| Points en suspens | Obligatoire sous condition | Texte | Obligatoire lorsque l'état est `FAIL` ou `SKIP`, énumérer les motifs de blocage ou d'omission | `D1 : .env détecté` |
| Niveau | Oui | Énumération | `P0` bloque / `P1` à corriger avant le push ou à enregistrer / `P2` recommandation | `P0` |
| Dimension | Oui | `D1`–`D14` | Numérotation voir la [matrice des dimensions de revue](./review-dimension-matrix.md) | `D1` |
| Problème | Oui | Texte | Un énoncé factuel d'une phrase, sans supposition ni formulation émotionnelle | `.env présent à la racine du dépôt` |
| Preuve | Oui | Chemin:ligne ou sortie de commande | Doit être vérifiable ; si la preuve est impossible, écrire `SKIP + motif` | `.env:3` |
| Agent responsable | Oui | Nom d'agent | Indiquer le rôle exécutant précis, ne pas écrire « personnes concernées » | `security-auditor` |
| Action | Oui | Texte | Opération directement exécutable, incluant le fichier cible | `supprimer .env, renouveler la clé et nettoyer l'historique` |
| Chemin de fichier | Oui | Texte | Énumérer point par point selon la liste de la [matrice documentaire](./document-matrix.md) | `SECURITY.md` |
| État de la matrice documentaire | Oui | Tableau ligne par ligne | Indiquer pour chaque fichier : présent, manquant ou à modifier | `SECURITY.md manquant` |
| Liste d'exécution du push | Oui | Liste à cases à cocher | Dérouler règle par règle selon la [spécification de push et de publication](./push-and-release-specification.md) | `- [ ] confirmer que .gitignore est effectif` |
| Justification du passage | Oui | Texte | En cas de blocage, indiquer le motif et les conditions de levée ; en cas de passage, indiquer les règles absolues satisfaites | `revérification possible après résolution des P0` |

## 3. Consignes de saisie

1. **La conclusion d'abord** : déterminer d'abord le nombre de P0, puis rédiger la conclusion. Tant qu'un P0 n'est pas résolu, `ALLOW PUSH` ne doit pas être émis.
2. **Preuve obligatoire** : chaque problème doit comporter un `chemin:numéro de ligne` ou une sortie de commande copiable. Une conclusion sans preuve est marquée `SKIP` avec motif explicite, `PASS` est interdit.
3. **Responsabilité par rôle** : l'agent responsable utilise le nom de rôle de la [matrice des dimensions de revue](./review-dimension-matrix.md) ; un problème correspond à un seul responsable.
4. **Action exécutable** : l'action doit désigner le fichier cible et le type d'opération ; « traitement ultérieur » ou « ajustement libre » sont considérés comme invalides.
5. **Cohérence des portes** : les trois lignes d'état A/B/C correspondent à la liste des problèmes ; si une porte est en `FAIL`, la conclusion doit être `BLOCK PUSH`.
6. **Matrice documentaire point par point** : énumérer fichier par fichier selon la liste, ne pas se contenter d'écrire « documentation globalement complète ».
7. **Déroulement de la liste** : la liste d'exécution du push doit dérouler les règles une à une, sans les remplacer par « appliquer la spécification ».

Erreurs fréquentes :

| Formulation erronée | Problème | Correction |
| --- | --- | --- |
| Colonne preuve remplie avec « problème suspecté » | Ni chemin ni sortie, non vérifiable | Ajouter `chemin de fichier:numéro de ligne` ou la sortie de commande |
| `ALLOW PUSH` alors que les P0 ne sont pas résolus | Violation des règles absolues | Remplacer par `BLOCK PUSH` et énumérer les conditions de levée |
| `PASS` sur un point non contrôlable | Résultat inventé | Écrire `SKIP` et justifier dans les points en suspens |
| Responsable indiqué comme « personnes concernées » | Aucun sujet responsable | Indiquer le nom précis de l'agent |
| Action indiquée comme « traitement ultérieur » | Non exécutable | Préciser le fichier cible et l'opération concrète |
| Branche par défaut écrite `main` sans vérification | Non conforme à la réalité | Se fonder sur la sortie de `git branch` |

## 4. Exemple complet

Voici un exemple complet de saisie pour `BLOCK PUSH` :

````markdown
# Rapport d'audit de push · markdown-lint-cli

Conclusion : BLOCK PUSH
Mode : audit complet
Dépôt : markdown-lint-cli · private · NONE · Branche par défaut main

## I. État des portes
| Porte | État | Points en suspens |
| --- | --- | --- |
| A Sécurité | FAIL | D1 a détecté .env, D2 absence de LICENSE |
| B Qualité | SKIP | Dépendances non installées dans le dépôt, build et tests impossibles à exécuter |
| C Page d'accueil | FAIL | README sans section d'installation ni exemple minimal |

## II. Liste des problèmes
| Niveau | Dimension | Problème | Preuve (chemin:ligne / sortie de commande) | Agent responsable | Action |
| --- | --- | --- | --- | --- | --- |
| P0 | D1 | Un fichier .env est présent à la racine | `.env:3` contient DATABASE_URL | security-auditor | Supprimer .env, renouveler les identifiants de base de données et nettoyer l'historique |
| P0 | D2 | Aucun fichier de licence | `ls LICENSE` renvoie `No such file or directory` | license-checker | Faire confirmer la licence par le propriétaire du dépôt puis générer LICENSE |
| P1 | D13 | README sans section d'installation | `README.md:1-28` ne contient aucun titre « installation » | readme-writer | Compléter l'installation et l'exemple minimal selon le gabarit standard de README |

## III. État de la matrice documentaire
| Fichier | État | Éléments manquants / à modifier |
| --- | --- | --- |
| README.md | À modifier | Section d'installation et exemple minimal manquants |
| LICENSE | Manquant | Type de licence à confirmer par le propriétaire |
| SECURITY.md | Manquant | Pas encore créé |

## IV. Liste d'exécution du push
- [ ] Confirmer que git status est propre
- [ ] Exécuter une analyse complète des clés (y compris les commits historiques)
- [ ] Réussir localement build, test et lint
- [ ] Matrice documentaire complète

## V. Justification du passage
Motif de blocage : 2 P0 présents (fuite d'identifiants, absence de licence) et porte qualité non évaluable faute de dépendances installées. Conditions de levée : achever le renouvellement des clés et le nettoyage de l'historique, déterminer la licence, relancer les tests dans un environnement constructible, puis revérifier après résolution des P0.
````

En cas de `ALLOW PUSH`, la section V peut indiquer : « Toutes les règles absolues sont satisfaites, les trois portes sont en PASS, le push peut être exécuté. » Les autres sections sont remplies selon la situation réelle, sans omettre les preuves ni les listes.

## 5. Ordre de livraison

1. Contenu complet de la navigation linguistique du README racine.
2. Contenu complet du README de chaque répertoire de langue achevé, avec énumération du code de langue et du chemin de fichier.
3. Contenu du fichier NOTICE.
4. Explication du choix de licence (si l'utilisateur n'a pas spécifié de licence, fournir uniquement les candidats et leurs différences, sans générer directement).
5. Récapitulatif des points à confirmer.
6. Rapport d'audit (le présent rapport).
7. Guide de push vers GitHub.

## Fichiers associés

- Détermination de l'état des portes : voir la [porte qualité](./quality-gate.md)
- Numérotation des dimensions de la liste des problèmes : voir la [matrice des dimensions de revue](./review-dimension-matrix.md)
- État de la matrice documentaire : voir la [matrice documentaire](./document-matrix.md)
- Liste d'exécution du push issue de la [spécification de push et de publication](./push-and-release-specification.md)
- Mode de répartition : voir le [contrat de répartition des sous-agents](./sub-agent-dispatch-contract.md)
