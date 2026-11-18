# Liste de contrôle d'alignement des projets existants

> Problème que ce fichier résout : lors de l'application de ce corpus de spécifications à un projet existant, fournir une liste de contrôle vérifiable point par point, avec la méthode d'appréciation et le critère de réussite, couvrant les six maillons que sont les métadonnées, le nommage des fichiers, la structure des sections, la synchronisation bilingue, les liens et le push.

## 1. Champ d'application

La présente liste s'applique à deux scénarios :

1. l'intégration pour la première fois d'un dépôt existant dans la gestion par ce corpus de spécifications ;
2. après une mise à jour du corpus, la vérification de régression d'un dépôt déjà aligné.

La liste s'exécute dans l'ordre « d'abord les métadonnées, ensuite la structure, enfin le push ». Tant qu'un groupe n'est pas validé, le groupe suivant n'est pas abordé, afin d'éviter des réécritures massives sur une base erronée.

## 2. Points de contrôle

### 2.1 Métadonnées (correspond à la section 5 de la [spécification de nommage des projets](./project-naming-specification.md))

| Numéro | Point de contrôle | Méthode d'appréciation | Critère de réussite |
| --- | --- | --- | --- |
| A1 | Conformité du nom du dépôt | Comparer à la formule de nommage et aux règles de jeu de caractères | Entièrement en minuscules, kebab-case, 2 à 25 caractères, sans numéro de version ni mot informationnel |
| A2 | Description au format bilingue combiné | Lire la zone About du dépôt ou exécuter `gh repo view --json description` | `langue nationale \| anglais`, une espace de chaque côté de la barre verticale |
| A3 | Longueur de la description | Compter les caractères, séparément pour le chinois et l'anglais | 120 caractères au plus chacun, 350 caractères au plus au total |
| A4 | Nombre et langue des sujets | `gh repo view --json repositoryTopics` | Exactement 20, entièrement en anglais, en minuscules, mots séparés par des traits d'union |
| A5 | Couverture des sujets | Vérifier selon les cinq catégories : langue, domaine, forme, écosystème, scénario | Les cinq catégories sont couvertes, aucun sujet incompatible avec la pile technique |

Ordre de traitement en cas de dépassement : comprimer d'abord la version anglaise, puis la version chinoise ; lors de la compression, supprimer d'abord les qualificatifs et les déterminants redondants, puis fusionner les formulations synonymes.

### 2.2 Nommage des fichiers (correspond à la [spécification multilingue](./multilingual-specification.md))

| Numéro | Point de contrôle | Méthode d'appréciation | Critère de réussite |
| --- | --- | --- | --- |
| B1 | Nommage du README principal | Lister le répertoire | `README.md` pour le chinois, `README_EN.md` pour l'anglais |
| B2 | Nommage des autres langues | Lister le répertoire | `README_<code de langue en majuscules>.md`, par exemple `README_JA.md` |
| B3 | Cohérence du nommage | Rechercher les anciens noms dans tout le dépôt | Aucun reliquat d'ancien nommage du type `README.en.md`, `README.ja.md` |
| B4 | Synchronisation des références | Rechercher l'ancien nom de fichier | Les liens de navigation, les exemples d'arborescence et les listes blanches des scripts sont mis à jour |
| B5 | Liens de bascule | Ouvrir la première ligne de chaque version linguistique | Chaque version linguistique permet, depuis la première ligne, de basculer vers toutes les autres langues |

Le renommage de fichiers doit utiliser `git mv`, afin de conserver l'historique du fichier. Les scripts du dépôt (pré-vérification, empaquetage, validation documentaire) utilisent souvent des chaînes de noms de fichiers comme liste blanche ; ils doivent être modifiés en même temps, sinon la validation échoue après le push.

### 2.3 Structure des sections (correspond à la [spécification des sections du README](./readme-sections-specification.md))

| Numéro | Point de contrôle | Méthode d'appréciation | Critère de réussite |
| --- | --- | --- | --- |
| C1 | Exhaustivité des sections | Extraire les titres de niveau 2 et les comparer à la liste des 20 chapitres | Les 20 chapitres sont tous présents, aucun ne manque |
| C2 | Nommage des sections | Comparer un à un le texte des titres | Conforme aux termes de la spécification, sans variantes du type « points forts essentiels » ou « détails de conception et petites astuces » |
| C3 | Ordre des sections | Comparer selon l'ordre d'apparition | Conforme à l'ordre de la spécification |
| C4 | Sections supplémentaires | Vérifier la présence de sections additionnelles | Le contenu supplémentaire est placé sous forme d'« annexe » après les 20 chapitres, sans insertion dans l'ordre du corps du texte |
| C5 | Correspondance des versions linguistiques | Comparer le nombre et l'ordre des titres de niveau 2 en chinois et en anglais | Correspondance une à une entre les deux langues |

Lorsque le corps du texte comporte des noms de sections non conformes à la spécification, les unifier selon les termes de la spécification ; lorsque la section contient un volume important de contenu existant, privilégier le renommage plutôt que la réécriture du corps du texte.

### 2.4 Synchronisation bilingue (correspond à la [spécification multilingue](./multilingual-specification.md))

| Numéro | Point de contrôle | Méthode d'appréciation | Critère de réussite |
| --- | --- | --- | --- |
| D1 | Cohérence du numéro de version | Rechercher la chaîne de version | Les deux langues indiquent le même numéro de version et le même état |
| D2 | Cohérence des chiffres | Comparer le nombre de fonctionnalités, de tests, de plateformes | Un même indicateur a la même valeur dans les deux versions |
| D3 | Cohérence des liens | Comparer l'ensemble des liens relatifs | Les deux versions pointent vers le même lot de fichiers |
| D4 | Cohérence terminologique | Contrôler par échantillonnage les termes techniques | Un même concept utilise la même traduction dans les deux versions |
| D5 | Cohérence de structure | Comparer le nombre de tableaux et de listes | Le nombre de tableaux et de listes dans une section est identique |

Après modification d'un contenu factuel dans une version, l'autre version doit être mise à jour dans le même commit ; aucune traduction complémentaire différée sur un autre commit n'est admise.

### 2.5 Liens et contenu (correspond à la [spécification rédactionnelle générale](./general-writing-specification.md))

| Numéro | Point de contrôle | Méthode d'appréciation | Critère de réussite |
| --- | --- | --- | --- |
| E1 | Accessibilité des liens relatifs | Résoudre un à un et vérifier l'existence des fichiers | Nombre de liens rompus égal à 0 |
| E2 | Identifiant de langage des blocs de code | Rechercher les délimiteurs | Tous comportent un identifiant de langage, aucun délimiteur nu |
| E3 | Nombre de colonnes des tableaux | Vérifier tableau par tableau la ligne de séparation et les lignes de données | Nombre de colonnes identique |
| E4 | Expressions proscrites | Rechercher les tournures orales, points d'exclamation, points de suspension, émojis | Aucune occurrence ; en cas de citation de l'original, la placer entre guillemets avec mention de la source |
| E5 | Données non vérifiées | Rechercher les chiffres de performance | Chaque chiffre dispose d'un environnement et d'une méthode de test |
| E6 | Formulations d'engagement | Rechercher les termes du type « garantir », « permanent », « totalement » | Les qualificatifs techniques peuvent être conservés ; les engagements vis-à-vis de l'extérieur doivent être supprimés |

### 2.6 Fichiers communautaires et push (correspond à la [matrice documentaire](./document-matrix.md) et à la [spécification de push et de publication](./push-and-release-specification.md))

| Numéro | Point de contrôle | Méthode d'appréciation | Critère de réussite |
| --- | --- | --- | --- |
| F1 | Présence des fichiers obligatoires | Lister le répertoire | `LICENSE`, `NOTICE`, `CONTRIBUTING.md`, `SECURITY.md` présents |
| F2 | Cohérence entre licence et NOTICE | Comparer la table de routage par niveaux | La licence au niveau du répertoire est cohérente avec la déclaration du NOTICE |
| F3 | Règles d'exclusion | Rechercher dans `.gitignore` | Les artefacts de build, les répertoires de dépendances, `.DS_Store` et `.workbuddy/` sont tous exclus |
| F4 | Messages de commit | Consulter `git log` | Conformes à `<type>(<scope>): <subject>` |
| F5 | Cohérence avec le distant | Comparer le `HEAD` local et `origin/main` | Identiques, espace de travail propre |

## 3. Vérifications complémentaires pour un dépôt multilingue

Lorsque le dépôt comporte trois versions linguistiques ou plus, ajouter trois points aux vérifications ci-dessus :

1. **Vérification des titres de sections langue par langue** : les titres des 20 chapitres de chaque langue doivent être conformes au sens de la référence chinoise ou anglaise, aucune langue ne doit comporter de chapitre manquant ;
2. **Cohérence du nombre de lignes des tableaux** : les listes de projets, les tableaux d'état et les tableaux de paramètres ont le même nombre de lignes dans chaque version linguistique ;
3. **Synchronisation du glossaire** : le tableau de correspondance terminologique est placé dans un fichier autonome commun aux deux langues, chaque version linguistique y renvoyant.

## 4. Erreurs fréquentes et traitement

| Erreur | Symptôme | Traitement |
| --- | --- | --- |
| Confusion sur les chiffres chinois lors d'un changement massif de numéros de chapitre | « 十、 » identifié comme « 二十、 », le chapitre 10 se voit attribuer le titre du chapitre 20 | Passer à un remplacement explicite un à un « ancienne chaîne → nouvelle chaîne », avec assertion de correspondance avant écriture |
| Chemin de lien modifié sans le texte affiché | Le lien est cliquable, mais le corps du texte mentionne encore l'ancien nom de section | Rechercher l'ancien nom de section dans tout le texte, mettre à jour le chemin et le texte affiché simultanément |
| Fichier renommé sans mise à jour des scripts | La documentation locale est correcte, mais le script de validation échoue après le push | Rechercher toutes les chaînes de noms de fichiers du dépôt, y compris scripts, configurations et exemples documentaires |
| Une seule des deux versions bilingues modifiée | Les faits divergent entre les deux versions | Se fonder sur l'état réel du dépôt, modifier d'abord la version principale, puis l'autre version dans le même commit |
| Page d'index non synchronisée | Le nouveau fichier n'est pas dans l'index et est considéré comme orphelin | Mettre à jour immédiatement le comptage et l'entrée de l'index après l'ajout d'un fichier, et revérifier la somme des comptages par domaine |
| Description du dépôt incohérente avec le corps du texte | La zone About mentionne sept projets, le corps du texte neuf | Mettre à jour la description à partir de la liste du corps du texte et le signaler dans le message de commit |

## 5. Gabarit d'enregistrement de recette

```text
仓库：{{仓库名}}
检查日期：{{日期}}
规范版本：{{版本或提交号}}

元数据：A1 {{通过/不通过}} A2 {{通过/不通过}} A3 {{通过/不通过}} A4 {{通过/不通过}} A5 {{通过/不通过}}
文件命名：B1 {{ }} B2 {{ }} B3 {{ }} B4 {{ }} B5 {{ }}
章节结构：C1 {{ }} C2 {{ }} C3 {{ }} C4 {{ }} C5 {{ }}
双语同步：D1 {{ }} D2 {{ }} D3 {{ }} D4 {{ }} D5 {{ }}
链接与内容：E1 {{ }} E2 {{ }} E3 {{ }} E4 {{ }} E5 {{ }} E6 {{ }}
社区与推送：F1 {{ }} F2 {{ }} F3 {{ }} F4 {{ }} F5 {{ }}

未通过项与处置：{{逐条列出}}
放行结论：{{通过 / 有条件通过 / 阻断}}
```

## 6. Définition des champs

| Champ | Signification | Valeur |
| --- | --- | --- |
| Nom du dépôt | Nom complet du dépôt contrôlé | `propriétaire/dépôt` |
| Version de la spécification | État du corpus de spécifications servant de base à ce contrôle | Numéro de commit ou de version |
| Réussi | L'élément satisfait le critère de réussite | Booléen |
| Conclusion de libération | Traitement du résultat du contrôle | Réussi / Réussi sous conditions / Bloqué |

## Fichiers associés

- Nommage et métadonnées du dépôt : voir la [spécification de nommage des projets](./project-naming-specification.md)
- Liste des chapitres : voir la [spécification des sections du README](./readme-sections-specification.md)
- Règles bilingues : voir la [spécification multilingue](./multilingual-specification.md)
- Rédaction et expressions proscrites : voir la [spécification rédactionnelle générale](./general-writing-specification.md)
- Actions de push : voir la [spécification de push et de publication](./push-and-release-specification.md)
