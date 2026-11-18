# Collecte d'informations et gabarits

> Problème que ce fichier résout : définir les champs d'information du projet à collecter avant la rédaction de la documentation, les règles de marquage des informations non confirmées, et fournir un index des espaces réservés, un gabarit de correspondance terminologique, un gabarit de liste des dépendances ainsi qu'un corps de collecte d'informations du projet directement copiable.

## 1. Champs obligatoires (blocage en cas d'absence)

| Champ | Description | Sections concernées |
| --- | --- | --- |
| Nom du projet | Nom du dépôt et nom d'affichage ; en cas de divergence, la justifier | Document entier |
| Positionnement en une phrase | 60 caractères au maximum, indiquant ce qu'est le projet et quel problème il résout pour qui | Chapitre 1 |
| Description du dépôt (langue nationale et anglais) | 120 caractères au maximum par langue, précisant respectivement le type de projet et l'usage principal | Chapitre 1 |
| Étiquettes de sujets | 20 mots anglais en minuscules, reliés par `-` ; un usage mixte de casse ou un terme non anglais est considéré comme manquant | Chapitre 1 |
| Contexte du projet | Raison du lancement, insuffisances des solutions existantes | Chapitre 2 |
| Liste des fonctionnalités clés | Regroupées par module, incluant les comportements perceptibles par l'utilisateur | Chapitre 3 |
| Pile technologique | Langage, framework, contraintes de version d'exécution | Chapitre 6 |
| Liste des dépendances | Nom, version, licence, titulaire des droits, adresse de la source | Chapitre 6, NOTICE |
| Type de licence | Licence du projet lui-même, obligatoirement un identifiant SPDX | Chapitre 19 |
| Titulaire des droits d'auteur | Nom de la personne ou raison sociale complète, avec l'année | Chapitre 19, NOTICE |
| Installation et exécution | Exigences d'environnement, commandes, résultats attendus | Chapitres 7 et 8 |

## 2. Champs facultatifs

Liste des options de configuration, définition d'API, arborescence des répertoires, données de tests de performance, matrice de compatibilité, problèmes connus, journal des modifications, feuille de route, processus de contribution, politique de sécurité, captures d'écran et adresses de démonstration, sources des ressources externes.

## 3. Instructions de remplissage et exemples

| Champ | Instructions de remplissage | Exemple |
| --- | --- | --- |
| Nom du projet | Le nom du dépôt utilise des lettres minuscules, des chiffres et `-` ; le nom d'affichage peut employer une graphie de marque ; en cas de divergence, en préciser la raison | Nom du dépôt `markdown-lint-cli`, nom d'affichage `Markdown Lint CLI` |
| Positionnement en une phrase | Contient un terme de catégorie et un qualificatif, sans accumulation d'adjectifs, 60 caractères au maximum | `Outil en ligne de commande de vérification des normes Markdown pour les équipes de documentation technique` |
| Description du dépôt (langue nationale et anglais) | La langue nationale et l'anglais forment chacun une phrase autonome, 120 caractères au maximum chacun ; un slogan ne remplace pas la description | `Français : outil en ligne de commande de vérification de la structure des documents Markdown` / `English: A CLI tool for checking Markdown document structure` |
| Étiquettes de sujets | Entièrement en anglais minuscules, mots reliés par `-`, 20 au total, couvrant intégralement le langage, la forme, l'usage, l'écosystème et les scénarios | `go cli markdown linter developer-tools` |
| Pile technologique | Indiquer le langage principal, le framework et les contraintes de version d'exécution ; ne pas écrire « dernière version » | `Go >= 1.22 ; Cobra v1.8.x` |
| Liste des dépendances | Chaque entrée contient la version, la licence, le titulaire des droits et l'adresse officielle ; en cas de source inconnue, marquer comme non confirmé | Voir le gabarit de tableau des dépendances de l'annexe C |
| Type de licence | Utiliser un identifiant SPDX, sans formulation vague du type « open source » ou « librement utilisable » | `MIT` |
| Installation et exécution | Fournir le répertoire de travail courant, la commande complète et la sortie attendue vérifiable | Exécuter `go install ./cmd/mdlint` à la racine du dépôt, la sortie affiche le numéro de version |
| Éléments non confirmés | Utiliser un marqueur fixe, préciser le contenu manquant et le responsable du complément ; ne pas remplacer par « provisoire » | `【À confirmer : type de licence de la dépendance foo, responsable : Zhang San】` |

## 4. Règles de marquage des informations non confirmées

1. Format unifié : `【À confirmer : ce qui manque précisément】` ; les formulations vagues du type « provisoire », « environ » ou « peut-être » ne doivent pas être utilisées comme substitut.
2. Emplacement du marquage : une occurrence à l'endroit correspondant du corps du texte, puis une seconde mention dans le « Récapitulatif des points à confirmer » en fin de document.
3. Les éléments non confirmés concernant la licence, le droit d'auteur ou la source des dépendances doivent être explicitement signalés dans le NOTICE ; l'omission de l'entrée entière est interdite.
4. Le récapitulatif des points à confirmer doit inclure le numéro, le champ, le contenu manquant, le responsable du complément et la date de complétion prévue ; une entrée sans responsable ou sans date ne peut pas entrer en phase 0 (voir le [processus d'exécution](./execution-process.md)).

## 5. Annexe A · Index des espaces réservés

`{{项目名称}}`、`{{一句话定位}}`、`{{当前版本}}`、`{{维护状态}}`、`{{许可证 SPDX}}`、`{{著作权人}}`、`{{年份}}`、`{{分支名}}`、`{{仓库地址}}`、`{{最低运行时版本}}`

Règles d'utilisation :

1. Cet index ne recense que les champs de base de la phase de collecte ; pour l'ensemble des espaces réservés du README et leurs descriptions, se référer au tableau de correspondance des espaces réservés du [gabarit standard de README](./readme-standard-template.md).
2. Les espaces réservés officiels s'écrivent uniformément sous la forme `{{纯名}}` ; il est interdit d'imbriquer du texte explicatif, des accents graves ou un second espace réservé entre les accolades ; le contenu en langage naturel entre accolades dans les exemples de la spécification n'est pas considéré comme un espace réservé officiel.
3. Les champs en langage naturel du tableau de collecte n'utilisent pas directement d'espaces réservés ; lors de la génération du README, ils sont mis en correspondance avec les espaces réservés adéquats selon le tableau de correspondance, et le document final ne doit conserver aucun contenu explicatif entre accolades.

## 6. Annexe B · Gabarit de table de correspondance terminologique chinois-anglais

| Chinois | English | Abréviation | Description |
| --- | --- | --- | --- |
| À compléter | TBD | — | — |

## 7. Annexe C · Gabarit de tableau de la liste des dépendances

| N° | Nom du composant | Version | Mode de référence | Titulaire des droits | Licence | Adresse officielle | Usage dans ce projet | Modifié | Description des modifications | Emplacement d'origine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | À compléter | À compléter | Direct | À compléter | À compléter | À compléter | À compléter | Non | Aucune | À compléter |

Les exigences de champs sont détaillées dans la [spécification de conformité open source](./open-source-compliance-specification.md).

## 8. Zone de saisie des informations du projet

Complétez les informations du projet ci-dessous avant de lancer la phase 0 (voir le [processus d'exécution](./execution-process.md)).

- Nom du projet :
- Positionnement en une phrase :
- Description du dépôt (langue nationale et anglais) :
- Étiquettes de sujets :
- Contexte du projet :
- Fonctionnalités clés :
- Pile technologique et versions :
- Liste des dépendances (ou chemin du fichier de liste des dépendances) :
- Type de licence :
- Titulaire des droits et année :
- Installation et exécution :
- Adresse du dépôt et branche cible :
- Autres éléments complémentaires :

## 9. Annexe D · Corps copiable de la collecte d'informations du projet

Copiez le contenu suivant dans le fichier `项目信息采集表.md` du projet cible et remplacez item par item le contenu après « Saisie : ». Les champs non confirmables sont marqués selon les règles de la section 4 et récapitulés à la section 8.

````markdown
# Fiche de collecte des informations du projet

> Ce fichier sert à collecter en une seule fois les informations nécessaires à la génération de la documentation. Une fois rempli, il permet de générer le README, le NOTICE et les autres documents livrables à partir des résultats de la collecte.

## 1. Informations de base

| Champ | Contenu saisi |
| --- | --- |
| Nom du dépôt | Saisie : nom du dépôt composé de lettres minuscules, de chiffres et de traits d'union |
| Nom d'affichage | Saisie : nom du projet affiché à l'extérieur ; s'il est identique au nom du dépôt, écrire « identique au nom du dépôt » |
| Adresse du dépôt | Saisie : adresse HTTPS complète |
| Branche cible | Saisie : nom de la branche par défaut |
| Code de langue | Saisie : code de langue prioritaire, par exemple fr-FR |
| Version actuelle | Saisie : numéro de version sémantique ou « non publié » |
| État de maintenance | Saisie : maintenance active / maintenance à basse fréquence / archivé |

## 2. Positionnement et périmètre d'application

| Champ | Contenu saisi |
| --- | --- |
| Positionnement en une phrase | Saisie : 60 caractères au maximum, avec terme de catégorie et qualificatif |
| Description du dépôt (langue nationale) | Saisie : 120 caractères au maximum |
| Description du dépôt (English) | Saisie : 120 caractères au maximum |
| Étiquettes de sujets | Saisie : 20 mots anglais en minuscules, reliés par des traits d'union |
| Contexte du projet | Saisie : raison du lancement et insuffisances des solutions existantes |
| Scénarios applicables | Saisie : énumération item par item, chacun avec sa condition de déclenchement |
| Scénarios non applicables | Saisie : énumération item par item, chacun avec sa raison |
| Atouts | Saisie : chaque élément accompagné d'un fondement vérifiable |
| Limites | Saisie : chaque élément avec sa portée d'impact et son mode de contournement |

## 3. Fonctions et caractéristiques

| Module | Comportement perceptible par l'utilisateur | Condition de déclenchement | Résultat | Preuve ou lien |
| --- | --- | --- | --- | --- |
| Saisie : nom du module | Saisie : description du comportement | Saisie : mode de déclenchement | Saisie : sortie ou changement d'état | Saisie : lien vers test, capture d'écran ou documentation |

## 4. Technique et dépendances

| Champ | Contenu saisi |
| --- | --- |
| Langage principal et contraintes de version | Saisie : par exemple `Go >= 1.22` |
| Framework et outils de build | Saisie : nom et contraintes de version |
| Environnement d'exécution et exigences système | Saisie : versions du système d'exploitation, du runtime, du navigateur ou de la base de données |
| Liste des dépendances | Saisie : chemin du fichier de liste des dépendances, ou insérer le tableau de l'annexe C dans cette section |
| Ressources externes | Saisie : source et licence des polices, images, icônes et jeux de données |

## 5. Livraison et utilisation

| Champ | Contenu saisi |
| --- | --- |
| Exigences d'environnement | Saisie : conditions indispensables avant l'installation |
| Commande d'installation | Saisie : commande complète incluant la précision du répertoire de travail courant |
| Commande de vérification et sortie attendue | Saisie : commande directement exécutable et résultat vérifiable |
| Mise à niveau et désinstallation | Saisie : commandes ou étapes d'opération |
| Liste des options de configuration | Saisie : nom de clé, type, valeur par défaut, obligatoire, plage de valeurs, rôle |
| Description de l'API ou des modules | Saisie : signature d'interface, paramètres, valeur de retour, codes d'erreur, exemple d'appel |
| Matrice de compatibilité | Saisie : combinaisons de versions explicitement prises en charge et non prises en charge |
| Données de performance | Saisie : environnement de test, méthode, indicateurs et goulots d'étranglement ; en l'absence de données, écrire « non fourni, ne pas en déduire » |

## 6. Risques et limites

| Champ | Contenu saisi |
| --- | --- |
| Problèmes connus | Saisie : description, portée d'impact, solution de contournement temporaire, lien de suivi |
| Limitations actuelles | Saisie : ce que la version actuelle ne permet pas de faire |
| Fonctionnalités non implémentées | Saisie : fonctionnalité, raison de la non-implémentation, état prévu |
| Sécurité et protection des données | Saisie : collecte, stockage, transmission des données, modèle de permissions, risques connus |
| Canal de signalement des vulnérabilités | Saisie : adresse électronique, gabarit d'Issue ou adresse dédiée |

## 7. Conformité et responsabilité

| Champ | Contenu saisi |
| --- | --- |
| Type de licence | Saisie : identifiant SPDX, par exemple `MIT` |
| Titulaire des droits d'auteur | Saisie : nom de la personne ou raison sociale complète |
| Année du droit d'auteur | Saisie : année ou intervalle d'années |
| Emplacement du texte intégral de la licence | Saisie : chemin du fichier LICENSE |
| Chemin du fichier NOTICE | Saisie : chemin du fichier NOTICE ; en l'absence de dépendances tierces, écrire « non applicable, raison : …… » |
| Clause de non-responsabilité | Saisie : adoption des limites de responsabilité ou des clauses d'absence de garantie |

## 8. Récapitulatif des points à confirmer

| Numéro | Champ | Contenu manquant | Responsable du complément | Date de complétion prévue | Portée d'impact |
| --- | --- | --- | --- | --- | --- |
| T-001 | Saisie : nom du champ | Saisie : ce qui manque précisément | Saisie : nom ou rôle | Saisie : AAAA-MM-JJ | Saisie : sections ou portes concernées |

## 9. Spécifications associées

- Structure des sections : [spécification des sections de README](./readme-sections-specification.md)
- Gabarit copiable : [gabarit standard de README](./readme-standard-template.md)
- Règles détaillées des champs de dépendances : [spécification de conformité open source](./open-source-compliance-specification.md)
- Évaluation des portes : [porte qualité](./quality-gate.md)
````

## Fichiers associés

- Règles de questionnement et conditions d'entrée en phase 0 : voir le [processus d'exécution](./execution-process.md)
- Correspondance des sections concernées : voir la [spécification des sections de README](./readme-sections-specification.md)
- Correspondance complète des espaces réservés du README : voir le [gabarit standard de README](./readme-standard-template.md)
- Règles détaillées des champs de dépendances : voir la [spécification de conformité open source](./open-source-compliance-specification.md)
- Le récapitulatif des points à confirmer relève de la porte G12, voir la [porte qualité](./quality-gate.md)
