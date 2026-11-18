# Spécification des sections de README

> Problème que ce fichier résout : définir les 20 sections que le README de chaque répertoire de langue doit obligatoirement contenir, le contenu que chaque chapitre doit inclure et ne doit pas inclure, ainsi que le format standard de la ligne de copyright.

## 1. Exigences générales relatives aux sections

Les 20 chapitres suivants doivent tous être présents, dans un ordre fixe, avec une correspondance une à une entre les versions linguistiques.

| Numéro | Section | Doit contenir | Ne doit pas contenir |
| --- | --- | --- | --- |
| 1 | Nom et positionnement du projet | Nom du projet, description du dépôt (format bilingue fusionné `langue nationale \| anglais`), étiquettes de sujets (20 au total, en anglais uniquement), positionnement en une phrase, lien de bascule de langue, version actuelle, état de maintenance | Adjectifs vagues ; description du dépôt dépassant 120 caractères ; étiquettes de sujets à casse mixte ou contenant des termes non anglais |
| 2 | Présentation du projet | Contexte, problème à résoudre, approche clé, cas d'usage, cas non applicables, ainsi que les avantages et limites présentés séparément (les limites doivent inclure le périmètre d'impact et le mode de contournement) | Traitement en une phrase ; liste des seuls avantages sans les limites |
| 3 | Fonctionnalités clés | Entrées fonctionnelles regroupées par module, chacune avec sa condition de déclenchement et son résultat | Simple liste de noms de fonctionnalités |
| 4 | Caractéristiques clés | Développement selon la structure de la [Guide de rédaction des caractéristiques et arbitrages d'ingénierie](./features-and-engineering-tradeoffs-guide.md) | Éloges sans preuve |
| 5 | Détails de conception et arbitrages d'ingénierie | Développement selon la structure de la [Guide de rédaction des caractéristiques et arbitrages d'ingénierie](./features-and-engineering-tradeoffs-guide.md) | Descriptions redondantes avec les fonctionnalités |
| 6 | Pile technique et liste des dépendances | Chaîne d'outils d'exécution, de compilation et de test avec contraintes de version ; le détail des dépendances renvoie à NOTICE | Absence de numéro de version |
| 7 | Installation et déploiement | Prérequis, étapes d'installation, commande de vérification, modes de mise à niveau et de désinstallation, explication de la conteneurisation | Étapes sautées ou vérification omise |
| 8 | Démarrage rapide | Exemple minimal exécutable, avec commandes complètes et sortie attendue | Pseudo-code non exécutable |
| 9 | Description de la configuration | Tableau des éléments de configuration (clé, type, valeur par défaut, obligatoire, plage de valeurs, rôle, exemple), priorité de configuration, prise en charge du rechargement à chaud | Absence de valeur par défaut |
| 10 | Description de l'API ou des modules | Signature d'interface, paramètres, valeur de retour, codes d'erreur, exemple d'appel, limitation de débit et quotas | Absence de codes d'erreur |
| 11 | Arborescence | Structure arborescente et description de la responsabilité de chaque niveau | Énumération fichier par fichier sans explication |
| 12 | Performances | Environnement de test, méthode de test, données d'indicateurs, analyse des goulets d'étranglement, recommandations d'optimisation | Chiffres sans conditions de test |
| 13 | Sécurité et confidentialité | Collecte et stockage des données, chiffrement en transit, modèle de permissions, canal de signalement des vulnérabilités, risques connus | Promesse de sécurité absolue |
| 14 | Compatibilité | Matrice des versions de systèmes d'exploitation, environnements d'exécution, navigateurs et bases de données, éléments explicitement non pris en charge | Formulations ambiguës |
| 15 | Problèmes connus et limites | Problèmes connus (description, périmètre d'impact, contournement temporaire, lien de suivi), limites actuelles, liste des fonctionnalités non implémentées (fonctionnalité, raison de non-implémentation, état de la planification) | Dissimulation de défauts graves ; présentation d'une fonctionnalité non implémentée comme implémentée |
| 16 | Journal des modifications | Conforme à la structure Keep a Changelog, numéros de version conformes au versionnage sémantique | Entrées sans date |
| 17 | Feuille de route | Éléments planifiés, état, version cible, avec la mention « non contraignante » | Engagement de délai de livraison |
| 18 | Contribution | Mise en place de l'environnement de développement, modèle de branches, convention de commit, exigences relatives aux PR, code de conduite, gabarits d'issue | Simple mention « bienvenue aux PR » |
| 19 | Droits d'auteur et licence | Ligne de copyright, nom de la licence, identifiant SPDX, emplacement du texte intégral de la licence | Absence de titulaire des droits |
| 20 | Déclaration de conformité NOTICE | Résumé des dépendances tierces, lien relatif vers le fichier NOTICE | Substitution de NOTICE par ce chapitre |

## 1.1 Les quatre questions de la page d'accueil et le texte d'une phrase

Le premier écran du README doit répondre à quatre questions, dans un ordre fixe :

1. ce que fait le projet ;
2. quel problème le projet résout ;
3. quelles caractéristiques le projet possède ;
4. l'exemple hello world minimal.

La première question correspond au « positionnement en une phrase », qui doit satisfaire simultanément trois points : indiquer le type de projet, employer des qualificatifs précis, et pouvoir être répété directement. Les textes publics de projets matures peuvent servir de référence :

| Projet | Texte en une phrase | Analyse de la structure |
| --- | --- | --- |
| Angular | One framework. Mobile & desktop. | Catégorie + périmètre de couverture |
| React | A declarative, efficient, and flexible JavaScript library for building user interfaces. | Trois qualificatifs + catégorie + usage |
| Vue | A progressive, incrementally-adoptable JavaScript framework for building UI on the web. | Deux caractéristiques + catégorie + usage |

Contraintes de rédaction :

- Ne pas employer d'adjectifs sans information tels que « puissant », « excellent » ou « révolutionnaire » ;
- Indiquer un terme de catégorie (bibliothèque, framework, outil, application) afin que le lecteur puisse classer le projet au premier regard ;
- Limiter à trois qualificatifs de caractéristiques au maximum pour éviter l'accumulation ;
- La version chinoise doit rester sous 60 caractères, la version anglaise sous 25 mots.

La troisième question, « quelles caractéristiques », doit divulguer en même temps les cas non applicables. Exemple de rédaction efficace : préciser qu'un intergiciel de messagerie « ne prend en charge que le niveau QoS 0 et ne convient pas aux scénarios nécessitant le niveau 1 » ; une rédaction inefficace consiste à n'énumérer que les avantages. La comparaison des caractéristiques doit reposer sur des faits vérifiables et ne doit pas dénigrer des projets similaires.

L'exemple hello world de la quatrième question doit permettre l'installation et l'exécution en deux étapes ; les projets dont l'installation est fastidieuse devraient fournir une image de conteneur ou un environnement de démonstration en ligne, afin d'éviter que le lecteur abandonne après avoir lu le README.

## 2. Format standard de la ligne de copyright

```text
Copyright © {{年份}} {{著作权人}}. Licensed under {{SPDX 标识符}}.
```

## Fichiers associés

- Périmètre du contenu des sections : voir la [Matrice documentaire](./document-matrix.md)
- Règles relatives à la description du dépôt et aux étiquettes de sujets : voir la section 5 de la [Spécification de nommage des projets](./project-naming-specification.md)
- Cohérence des versions chinoise et anglaise : voir la [Spécification multilingue](./multilingual-specification.md)
- NOTICE référencé par le détail des dépendances : voir la [Spécification NOTICE](./notice-specification.md)
- Normes de rédaction : voir la [Spécification générale de rédaction](./general-writing-specification.md)
