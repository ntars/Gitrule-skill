# Spécification des gabarits de manuel de développement

> Problème que ce fichier résout : définir le squelette du manuel de développement en deux phases « rédaction dans le cloud, exécution en local », le format des cartes de tâches, le protocole de transfert et les portes de vérification, afin qu'une même idée puisse être transcrite par le modèle cloud en cartes de tâches sans ambiguïté, puis exécutée par relais successifs par le modèle de codage local.

## 1. Positionnement et flux d'utilisation

1. La présente spécification vise le scénario de division du travail « un modèle de raisonnement cloud + un modèle de codage local » : le cloud transcrit les idées floues en plans explicites, le local exécute le plan de manière déterministe.
2. Le flux d'utilisation comporte fixement quatre étapes, dont l'ordre ne doit pas être contourné :
   - Vérification préalable : contrôler si l'idée comporte des prémisses erronées, des sauts de logique ou des informations manquantes ; si les informations sont insuffisantes, interroger d'abord l'utilisateur, la supposition est interdite.
   - Rédaction dans le cloud : balayer les solutions open source selon la section 9 et remplir le manuel.
   - Revue par l'utilisateur : porter la revue en priorité sur les commandes d'acceptation, le registre d'adoption et les zones interdites.
   - Exécution en local : injecter les chapitres correspondants et les enregistrements de transfert selon l'index lisible par machine, et exécuter partie par partie.
3. Le corps du manuel ne doit contenir aucun mot vague tel que « etc. », « lié », « approprié », « autant que possible », « si nécessaire » ; chaque occurrence doit fournir soit une valeur exacte, soit une règle de décision.

## 2. Squelette du manuel

Chaque manuel de développement comporte fixement les parties suivantes, dans un ordre inchangé :

| Partie | Responsabilité |
| --- | --- |
| Index lisible par machine | Table de navigation des chemins de chapitres, des répertoires de code correspondants, des commandes d'acceptation et des marqueurs de phase |
| Registre d'adoption | Table d'enregistrement de la chaîne d'approvisionnement open source, unique source de vérité du projet entier (voir la section 11) |
| Constitution du projet | Invariants du projet entier, injectée dans chaque partie |
| Glossaire | Correspondance entre les termes, leurs explications en langage courant et le code concerné |
| Chapitres de module | Un chapitre par module, rédigé selon la structure de la section 4 |
| Chapitre de distribution | Règles de construction et de distribution ; les actions de publication requièrent la confirmation de l'utilisateur |
| Chapitre de textes du site web | Règles des textes destinés aux utilisateurs ordinaires ; non injecté dans le modèle local |
| Journal des changements | Date, chapitre, changement et décideur |

## 3. Constitution du projet

La constitution du projet est l'ensemble des invariants injectés dans chaque partie d'exécution locale ; elle comporte fixement cinq éléments :

1. Pile technologique et versions : précises jusqu'au numéro de version.
2. Convention d'arborescence des répertoires : arborescence accompagnée d'une phrase de responsabilité pour chaque répertoire.
3. Règles de codage : déclinées selon le type de projet, avec pour socle le chargement modulaire à la demande, le code minimal et le plus direct, l'absence de fonctionnalités non demandées, des commentaires complets et l'explication des concepts professionnels en langage courant ; les projets d'interface suivent les Apple HIG, l'unité de police est exclusivement px ou rem, rpx est interdit.
4. Zones interdites globales : ce qui ne doit jamais être fait, par exemple introduire une dépendance absente du registre d'adoption, modifier un fichier de contrat.
5. Règles de langue de sortie : les explications, journaux, progrès et messages d'erreur sont en chinois simplifié ; le code, les commandes, les chemins de fichiers et les noms propres peuvent rester dans leur langue d'origine.

## 4. Structure des chapitres de module

Chaque chapitre de module comporte fixement neuf sections, dans un ordre inchangé :

| Section | Responsabilité |
| --- | --- |
| Responsabilité du module | 1 à 3 phrases indiquant clairement ce qui est fait et ce qui n'est pas fait |
| Solutions open source dont dépend le module | Nom, usage, numéro d'entrée du registre d'adoption |
| Liste des fichiers | Chemins, actions (création / modification / lecture seule), responsabilités ; au plus 10 fichiers au total, au-delà le chapitre est scindé |
| Contrat d'interface | Signatures, routes et champs de protocole précis jusqu'au type, avec des échantillons complets d'entrée et de sortie |
| Données et états | Ce qui est stocké, où, sous quel format ; les concepts professionnels sont expliqués en langage courant |
| Relations de dépendance | Trois groupes de fichiers : à lire d'abord, qui seront appelés, jamais modifiés |
| Cartes de tâches | Les parties en lesquelles le module est décomposé, chaque carte exécutée de façon indépendante |
| Zone interdite du chapitre | Ce que le présent module n'a spécialement pas le droit de faire |
| Notes de conception | Raisons du choix, solutions écartées, distinction entre faits et conjectures ; non injecté dans le modèle local |

## 5. Format de la carte de tâches

Une carte de tâches égale une session locale égale une commande d'acceptation ; les champs sont fixés comme suit :

| Champ | Exigence |
| --- | --- |
| Objectif | Une phrase, vérifiable par la machine |
| Préconditions | La partie précédente dont dépend la carte et les fichiers correspondants existent tous |
| Étapes | Numérotées, chaque étape constitue une action déterministe menée d'un trait, sans interruption ni question supplémentaire |
| Commande d'acceptation | Directement copiable et exécutable ; tant qu'un dispositif d'acceptation n'existe pas, la première carte doit d'abord le mettre en place |
| Résultat attendu | Sortie exacte, code de sortie ou nombre d'assertions |
| Traitement des échecs | Disposition donnée erreur type par erreur type ; après 3 échecs consécutifs, s'arrêter impérativement et l'écrire dans l'enregistrement de transfert |
| Exigences de transfert | Déclarer les champs qui doivent être écrits dans l'enregistrement de transfert |

Contraintes impératives :

1. Si une carte touche plus de 10 fichiers, elle est scindée ; si un chapitre dépasse 6 cartes, il est scindé.
2. Toute carte comportant une livraison avec autocontrôle doit lister explicitement le nettoyage du code redondant et les points de synchronisation de README, NOTICE et LICENSE.
3. Toute action de suppression ou d'écrasement de fichier s'arrête impérativement, est écrite dans le champ `block` de l'enregistrement de transfert et attend la confirmation de l'utilisateur.
4. Une tâche trop vague pour qu'on puisse y écrire une commande d'acceptation ne doit pas remplir une carte ; elle est marquée séparément « décision de l'utilisateur requise ».

## 6. Protocole de transfert PROGRESS

Le fichier d'enregistrement de transfert `PROGRESS.md` est l'unique source de vérité entre les parties, au format fixe :

| Champ | Exigence |
| --- | --- |
| done | L'objectif de la carte est-il atteint |
| files | Liste réelle des fichiers modifiés |
| decisions | Décisions prises en cours, au format « A a été choisi, parce que B » |
| next | Numéro de la carte suivante et point d'entrée, à écrire jusqu'au chemin de fichier et à la fonction d'entrée ; « continuer à améliorer » est interdit |
| block | Problèmes non résolus, laissé vide s'il n'y en a pas |

1. À la clôture de chaque carte, une entrée doit être ajoutée, sans modification du format.
2. Lors de l'exécution locale, seule la dernière entrée est injectée ; les entrées historiques ne sont pas injectées.
3. Reprise après interruption : à réception de l'instruction « continuer », lire d'abord la dernière entrée pour confirmer le point d'interruption, puis reprendre depuis le point d'entrée désigné par `next` ; refaire les étapes déjà accomplies de mémoire ou par conjecture est interdit.

## 7. Budget d'injection en local

Le harness assemble le contexte de chaque partie selon la table suivante, pour un budget total n'excédant pas 24K (75 % de la fenêtre de travail de 32K) :

| Élément injecté | Budget |
| --- | --- |
| Constitution du projet | 2-3K |
| Chapitre auquel appartient la carte de tâches courante | 2-5K |
| Dernière entrée de l'enregistrement de transfert | environ 0,5K |
| Squelette du prompt de transfert | environ 0,3K |
| Code et sorties d'outils | quota restant |

Ne sont pas injectés : la table complète du registre d'adoption (seules les entrées concernées par la carte courante sont injectées), les notes de conception, le chapitre de textes du site web.

## 8. Règles impératives du prompt de transfert

Au démarrage de chaque partie, un préambule fixe est injecté ; les règles impératives sont fixées à six :

1. Sortir exclusivement en chinois simplifié ; le code, les commandes, les chemins et les noms propres peuvent rester dans leur langue d'origine.
2. Ne faire que ce qui figure dans la carte de tâches, sans ajouter de fonctionnalités, configurations ou capacités d'extension non demandées.
3. Ne rien inventer ni fabriquer ; en cas d'incertitude sur une signature d'API, l'indiquer directement comme incertaine ; faits et conjectures sont explicitement distingués.
4. En cas d'échec de la commande d'acceptation, appliquer le traitement des échecs de la carte de tâches ; modifier soi-même les critères d'acceptation est interdit.
5. Toute action de suppression ou d'écrasement de fichier s'arrête impérativement et attend la confirmation de l'utilisateur.
6. Une fois terminé, écrire l'enregistrement de transfert strictement selon les exigences de transfert, puis conclure.

## 9. Règles de remplissage côté cloud

Avant de remplir le manuel, le modèle cloud accomplit deux préalables, puis remplit chapitre par chapitre :

1. Vérification des prémisses : contrôler les prémisses erronées, les sauts de logique et les informations manquantes ; si c'est insuffisant, interroger d'abord l'utilisateur.
2. Balayage des solutions open source : rechercher les solutions existantes disponibles dans l'écosystème open source, balayer avant de remplir, utiliser une solution éprouvée plutôt que réinventer la roue, puis enregistrer les résultats dans le registre d'adoption.

Lors du remplissage, respecter :

1. Éliminer tout mot vague, fournir à chaque occurrence une valeur exacte ou une règle de décision.
2. Écrire les décisions de conception dans les notes de conception, avec les raisons du choix et les solutions écartées, pour revue par l'utilisateur ; non injecté dans le modèle local.
3. Rédiger les instructions destinées au modèle local comme si « son destinataire ne connaissait pas le contexte du projet » ; écrire explicitement toutes les prémisses.
4. Socle de conformité : marquer « à confirmer » toute licence inconnue ; signaler l'obligation de dérivé pour les solutions fortement copyleft ; conserver le copyright d'origine et la note de modification du code open source modifié ; chaque entrée adoptée doit être synchronisée avec README, README_EN, NOTICE et LICENSE, la synchronisation constituant une étape explicite et un contenu d'acceptation de la carte de tâches correspondante.
5. Pour les règles de format documentaire, référencer les spécifications correspondantes du présent dépôt, sans copier le corps des spécifications dans le manuel.

## 10. États de phase et fenêtre de travail

Chaque chapitre de l'index lisible par machine porte un marqueur de phase, sur la base duquel la fenêtre de travail locale est ajustée :

| Phase | Caractéristique | Fenêtre de travail |
| --- | --- | --- |
| Terrain vierge | Remplir l'implémentation selon le contrat gelé | 16-24K |
| Croissance | Fonctionnalités transversales aux modules, niveau par défaut | 32K |
| Maintenance | Refactorisation et diagnostic transversal aux modules | 48-64K, parallélisme réduit en conséquence |

Les chapitres en phase de maintenance doivent en outre comporter un guide de diagnostic à trois colonnes : symptôme, emplacement possible, commande de vérification.

## 11. Registre d'adoption, distribution et textes du site web

1. Les champs de la table du registre d'adoption sont fixés à : nom, catégorie, version, usage, licence, titulaire des droits, adresse officielle, modification ou non, note de modification, mode de déclaration, état d'adoption ; l'état d'adoption se décline en trois niveaux : « adoptable immédiatement », « à évaluer », « momentanément indisponible ».
2. Le chapitre de distribution couvre les scripts de construction, la matrice CI, les checksum, le gabarit des variables d'environnement de signature ; la commande d'acceptation de la carte de distribution est le contrôle des artefacts de construction ; les actions de publication externe n'entrent pas dans le modèle local et sont exécutées après confirmation de l'utilisateur.
3. Le chapitre de textes du site web s'adresse aux utilisateurs ordinaires : le code, la ligne de commande, les termes techniques et les mots creux sont interdits ; la structure est : positionnement du premier écran, points de douleur, points forts, confiance, téléchargement, récits d'usage, questions fréquentes ; le ton est calme et retenu.

## 12. Références entre projets et vérification

1. Lorsqu'un projet cible référence la présente spécification, il en lit l'intégralité par `gitrule spec` et copie le squelette du manuel comme squelette initial du manuel interne au projet ; la présente spécification n'est pas révisée avec le projet, et l'évolution du manuel interne se boucle dans le dépôt du projet.
2. Pour les cartes de tâches produisant de la documentation, la commande d'acceptation est complétée par `gitrule check` ; pour les projets multilingues, par `gitrule xcheck` ; après toute modification du glossaire, exécuter `gitrule termcheck`.
3. Les violations documentaires détectées par `gitrule check` relèvent de la catégorie réparable automatiquement : exécuter d'abord `gitrule optimize` puis revérifier ; si le contrôle échoue encore, l'écrire dans le champ `block` de l'enregistrement de transfert.
4. Les spécifications Gitrule ne couvrent que la documentation et les règles de dépôt ; la qualité du code relève des tests et des scripts de vérification de chaque projet, et l'un ne remplace pas l'autre.

## Fichiers associés

- [Index général des spécifications](./README.md) : point d'entrée de l'enregistrement de la présente spécification
- [Règles absolues](./hard-rules.md) : contrainte supérieure de la porte de vérification de la présente spécification
- [Matrice documentaire](./document-matrix.md) : définition unique des responsabilités des documents livrables auxquels le manuel appartient
- [Spécification générale de rédaction](./general-writing-specification.md) : norme rédactionnelle du corps du manuel
- [Spécification multilingue](./multilingual-specification.md) : règles de synchronisation multilingue de la présente spécification
- [Spécification des métadonnées lisibles par machine](./machine-readable-metadata-specification.md) : identifiant stable et correspondance des chemins de la présente spécification
- [Collecte d'informations et gabarits](./information-collection-and-templates.md) : tableau de correspondance terminologique et conventions des champs des gabarits
