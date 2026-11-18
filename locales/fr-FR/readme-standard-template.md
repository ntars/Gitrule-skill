# Gabarit standard de README

> Problème que ce fichier résout : fournir un gabarit de README universel, directement copiable et utilisable par simple remplacement des espaces réservés, couvrant la présentation d'accueil sur l'ensemble du cycle de vie du projet, accompagné d'un tableau de correspondance des espaces réservés, de la description des sections facultatives et d'une liste d'auto-vérification avant livraison, afin que tout développeur puisse l'adapter rapidement à son propre projet.

## 1. Mode d'emploi

1. Copiez l'intégralité de la section 3 « Corps du gabarit » et créez un fichier `README.md` à la racine du projet.
2. Remplacez un à un les `{{...}}` selon le tableau de correspondance des espaces réservés de la section 4 ; supprimez les éléments non utilisés en même temps que la ligne ou la section entière concernée.
3. Chaque sous-section de la section 3 correspond aux 20 chapitres de la [Spécification des sections de README](./readme-sections-specification.md), ordonnés selon le cycle de vie de l'intérieur vers l'extérieur ; la suppression d'un chapitre impose de supprimer également le lien correspondant dans la navigation de premier écran.
4. Unifiez le style, la couleur et le nombre de badges conformément à la [Spécification des badges](./badge-specification.md) ; vérifiez le placement des captures d'écran, des tableaux et des blocs de code conformément à la [Spécification de mise en page visuelle du README](./readme-visual-layout-specification.md).
5. Retenez ou supprimez les sections selon le type de projet conformément au [Guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md).
6. Avant de livrer, exécutez la liste d'auto-vérification de la section 6 et confirmez l'absence de tout espace réservé résiduel.

## 2. Principes de personnalisation

- **Éléments obligatoires** : nom du projet, description du dépôt, positionnement en une phrase, installation, démarrage rapide, licence.
- **Ordre fixe** : l'ordre des sections est identique à celui de la [Spécification des sections de README](./readme-sections-specification.md) ; les versions française et chinoise se correspondent chapitre par chapitre.
- **Preuve prioritaire** : les caractéristiques clés, les performances et les arbitrages d'ingénierie doivent fournir des preuves vérifiables ; les éloges qualitatifs sont interdits.
- **Divulgation transparente** : les cas non applicables, les limites, les problèmes connus et les fonctionnalités non implémentées doivent être explicitement listés, sans dissimulation.
- **Absence d'engagement** : la feuille de route est marquée « non contraignante » et n'indique aucune date de livraison précise.
- **Authenticité** : toutes les commandes, exemples, liens et badges doivent être réellement utilisables ; les coordonnées et les canaux de signalement doivent être réellement joignables.

## 3. Corps du gabarit

Cette section est organisée selon le cycle de vie du projet, « de l'intérieur vers l'extérieur », en 20 sections correspondant une à une aux 20 chapitres de la [Spécification des sections de README](./readme-sections-specification.md). Le texte à l'intérieur de chaque bloc de code constitue le corps copiable.

La correspondance entre les sections et les phases du cycle de vie est la suivante, pour faciliter la localisation :

| Phase du cycle de vie | Sous-sections correspondantes | Point de présentation |
| --- | --- | --- |
| Lancement du projet | 3.1–3.2 | Positionnement, contexte, cas d'usage et limites |
| Analyse des exigences | 3.2–3.3 | Périmètre fonctionnel, cas d'usage, cas non applicables |
| Conception de l'architecture | 3.5–3.6, 3.11 | Arbitrages d'ingénierie, pile technique, arborescence |
| Développement | 3.3–3.4, 3.9–3.10 | Fonctionnalités, caractéristiques, configuration, API |
| Vérification par les tests | 3.8, 3.12 | Exemple de démarrage rapide, preuves de performance |
| Déploiement en production | 3.7, 3.14 | Installation et déploiement, matrice de compatibilité |
| Exploitation et supervision | 3.13, 3.15 | Sécurité et confidentialité, problèmes connus et limites |
| Maintenance itérative | 3.15–3.17 | Fonctionnalités non implémentées, journal des modifications, feuille de route |

Remarque : le README est la page d'accueil du projet ; les documents de processus de chaque phase (traces complètes des exigences, de la conception, des tests, du déploiement et de l'exploitation) sont portés par les spécifications correspondantes, voir la [Matrice documentaire](./document-matrix.md) ; ce chapitre ne présente que les conclusions visibles par l'utilisateur.

### 3.1 Nom et positionnement du projet (chapitre 1)

````markdown
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{{LOGO_DARK_URL}}">
    <img alt="{{项目名称}} Logo" src="{{LOGO_LIGHT_URL}}" width="{{LOGO_WIDTH}}">
  </picture>

  <h1>{{项目名称}}</h1>

  [![build](https://img.shields.io/github/actions/workflow/status/{{OWNER}}/{{REPO}}/{{WORKFLOW}}?style=flat-square&logo=github)](https://github.com/{{OWNER}}/{{REPO}}/actions)
  [![version](https://img.shields.io/badge/version-{{VERSION}}-blue?style=flat-square)]({{RELEASE_URL}})
  [![license](https://img.shields.io/badge/license-{{LICENSE_SPDX}}-blue?style=flat-square)](./LICENSE)

  **Description du dépôt** : 【{{仓库描述中文}} | {{REPO_DESCRIPTION_EN}}】

  **Étiquettes de sujets** : {{TOPICS}}

  {{一句话定位}}

  {{语言切换链接}}

  [Installation](#installation) · [Démarrage rapide](#démarrage-rapide) · [Caractéristiques clés](#caractéristiques-clés) · [Problèmes connus et limites](#problèmes-connus-et-limites) · [Feuille de route](#feuille-de-route) · [Documentation](#documentation) · [Contribution](#contribution)
</div>
````

### 3.2 Présentation du projet (chapitre 2)

````markdown
## Présentation du projet

{{背景}}

{{核心思路}}

**Cas d'usage**

- {{适用场景一}}
- {{适用场景二}}

**Cas non applicables**

- {{不适用场景一}}
- {{不适用场景二}}

### Avantages et limites

**Avantages**

| Avantage | Description | Méthode de vérification |
| --- | --- | --- |
| {{优势名称}} | {{优势说明}} | {{证据}} |
| {{优势名称}} | {{优势说明}} | {{证据}} |

**Limites**

| Limite | Périmètre d'impact | Contournement temporaire |
| --- | --- | --- |
| {{局限描述}} | {{影响范围}} | {{规避方式}} |
| {{局限描述}} | {{影响范围}} | {{规避方式}} |
````

### 3.3 Fonctionnalités clés (chapitre 3)

````markdown
## Fonctionnalités clés

- {{功能一}} : {{触发条件与结果}}
- {{功能二}} : {{触发条件与结果}}
- {{功能三}} : {{触发条件与结果}}
````

### 3.4 Caractéristiques clés (chapitre 4)

Chaque caractéristique doit comporter la structure complète en cinq parties ; l'absence d'un paragraphe interdit de la lister. Voir la [Guide de rédaction des caractéristiques et arbitrages d'ingénierie](./features-and-engineering-tradeoffs-guide.md) pour les modalités de rédaction.

````markdown
## Caractéristiques clés

### {{特性名称}}

- **Valeur** : {{价值}}
- **Mode de mise en œuvre** : {{实现方式}}
- **Différenciation** : {{差异化}}
- **Preuve** : {{证据}}
````

### 3.5 Détails de conception et arbitrages d'ingénierie (chapitre 5)

Rédigez selon les trois parties « scénario → traitement → raison » ; les catégories couvertes figurent à la section 2 de la [Guide de rédaction des caractéristiques et arbitrages d'ingénierie](./features-and-engineering-tradeoffs-guide.md).

````markdown
## Détails de conception et arbitrages d'ingénierie

### {{取舍主题}}

- **Scénario** : {{场景}}
- **Traitement** : {{处理方式}}
- **Raison** : {{原因}}
````

### 3.6 Pile technique et liste des dépendances (chapitre 6)

````markdown
## Pile technique et liste des dépendances

| Catégorie | Technologie ou composant | Contrainte de version | Usage |
| --- | --- | --- | --- |
| Exécution | {{运行时与版本}} | {{运行时版本约束}} | {{运行时用途}} |
| Compilation | {{构建工具与版本}} | {{构建版本约束}} | {{构建用途}} |
| Tests | {{测试工具与版本}} | {{测试版本约束}} | {{测试用途}} |

Le détail des dépendances tierces et leurs licences figurent dans [NOTICE](./NOTICE).
````

### 3.7 Installation et déploiement (chapitre 7)

````markdown
## Installation

Prérequis : {{运行时 / 操作系统 / 版本}}

```bash
{{包管理器安装命令}}
```

Vérification de l'installation :

```bash
{{验证命令}}
```

Sortie :

```text
{{预期输出}}
```

Mise à niveau : `{{升级命令}}`. Désinstallation : `{{卸载命令}}`.

Déploiement conteneurisé : {{容器化说明}}
````

### 3.8 Démarrage rapide (chapitre 8)

````markdown
## Démarrage rapide

{{一句话说明本示例完成什么}}

```{{语言标识}}
{{最小可运行示例}}
```

Sortie attendue :

```text
{{输出}}
```
````

### 3.9 Description de la configuration (chapitre 9)

````markdown
## Description de la configuration

| Clé | Type | Valeur par défaut | Obligatoire | Plage de valeurs | Rôle | Exemple |
| --- | --- | --- | --- | --- | --- | --- |
| {{键名}} | {{类型}} | {{默认值}} | {{是否必填}} | {{取值范围}} | {{作用}} | {{示例值}} |

Priorité de configuration : {{配置优先级}}.

Rechargement à chaud : {{热更新支持说明}}
````

### 3.10 Description de l'API ou des modules (chapitre 10)

````markdown
## API

{{模块概述}}

```{{语言标识}}
{{接口签名}}
```

Paramètres :

| Paramètre | Type | Obligatoire | Description |
| --- | --- | --- | --- |
| {{参数名}} | {{参数类型}} | {{参数是否必填}} | {{参数说明}} |

Valeur de retour : {{返回值说明}}

Codes d'erreur :

| Code d'erreur | Signification | Traitement |
| --- | --- | --- |
| {{错误码}} | {{错误含义}} | {{错误处理方式}} |

Exemple d'appel :

```{{语言标识}}
{{调用示例}}
```

Limitation de débit et quotas : {{限流与配额说明}}

Voir la [Documentation de l'API]({{API_DOC_PATH}}).
````

### 3.11 Arborescence (chapitre 11)

````markdown
## Arborescence

```text
{{项目名}}/
├── {{目录条目}}   # {{职责}}
├── {{目录条目}}   # {{职责}}
└── {{目录条目}}   # {{职责}}
```
````

### 3.12 Performances (chapitre 12)

````markdown
## Performances

Environnement de test : {{测试环境}}

Méthode de test : {{测试方法}}

| Indicateur | Valeur | Référence de comparaison |
| --- | --- | --- |
| {{性能指标}} | {{指标数值}} | {{对比基线}} |

Analyse des goulets d'étranglement : {{瓶颈分析}}

Recommandations d'optimisation : {{调优建议}}
````

### 3.13 Sécurité et confidentialité (chapitre 13)

````markdown
## Sécurité et confidentialité

Collecte et stockage des données : {{数据收集与存储说明}}

Chiffrement en transit : {{传输加密说明}}

Modèle de permissions : {{权限模型说明}}

Risques connus : {{已知风险}}

Canal de signalement des vulnérabilités : {{漏洞上报渠道}}

La politique de sécurité est disponible dans [SECURITY.md](./SECURITY.md).
````

### 3.14 Compatibilité (chapitre 14)

````markdown
## Compatibilité

| Dimension | Périmètre pris en charge | État de vérification |
| --- | --- | --- |
| Système d'exploitation | {{操作系统}} | {{操作系统验证状态}} |
| Environnement d'exécution | {{运行时兼容版本}} | {{运行时验证状态}} |
| Navigateur | {{浏览器}} | {{浏览器验证状态}} |
| Base de données | {{数据库版本}} | {{数据库验证状态}} |

Explicitement non pris en charge : {{明确不支持项}}
````

### 3.15 Problèmes connus, limites et fonctionnalités non implémentées (chapitre 15)

````markdown
## Problèmes connus et limites

**Problèmes connus**

| Description du problème | Périmètre d'impact | Contournement temporaire | Lien de suivi |
| --- | --- | --- | --- |
| {{问题描述}} | {{影响范围}} | {{临时规避方案}} | {{跟踪链接}} |

**Limites actuelles**

{{当前限制说明}}

**Fonctionnalités non implémentées**

| Fonctionnalité | Raison de non-implémentation | État de la planification |
| --- | --- | --- |
| {{未实现功能}} | {{未实现原因}} | {{计划状态}} |
````

### 3.16 Journal des modifications (chapitre 16)

````markdown
## Journal des modifications

Les changements de version suivent le versionnage sémantique et la structure Keep a Changelog ; l'historique complet figure dans [CHANGELOG.md](./CHANGELOG.md).
````

### 3.17 Feuille de route (chapitre 17)

Les modalités de rédaction de l'état des éléments planifiés et de la version cible figurent dans la [Spécification de la feuille de route](./roadmap-specification.md) ; la mention « non contraignante » est obligatoire.

````markdown
## Feuille de route

> Les éléments ci-dessous sont planifiés et ne constituent aucun engagement de livraison ; le périmètre et les délais réels sont ceux consignés dans les notes de version.

| Élément planifié | État | Version cible |
| --- | --- | --- |
| {{计划项}} | {{计划状态}} | {{目标版本}} |
| {{计划项}} | {{计划状态}} | {{目标版本}} |
````

### 3.18 Contribution (chapitre 18)

````markdown
## Contribution

- Mise en place de l'environnement de développement : {{搭建步骤}}
- Modèle de branches : {{说明}}
- Convention de commit : {{Conventional Commits 等}}
- Exigences relatives aux PR : {{要求}}
- Code de conduite : voir [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- Gabarits d'issue : voir [.github/ISSUE_TEMPLATE/](./.github/ISSUE_TEMPLATE/)
````

### 3.19 Droits d'auteur et licence (chapitre 19)

````markdown
## Licence

Copyright © {{年份}} {{著作权人}}. Licensed under {{SPDX 标识符}}.

Ce projet est distribué sous licence {{许可证名称}} ; le texte intégral figure dans [LICENSE](./LICENSE).
````

### 3.20 Déclaration de conformité NOTICE (chapitre 20)

````markdown
## Déclaration de conformité NOTICE

Ce projet utilise des composants et ressources tiers ; le résumé de leurs licences et mentions de droits d'auteur figure dans [NOTICE](./NOTICE). Ce chapitre ne remplace pas le fichier NOTICE.
````

## 4. Tableau de correspondance des espaces réservés

Le tableau liste l'ensemble des espaces réservés présents dans le corps du gabarit. Ils sont classés par ordre de section ; supprimez les éléments non utilisés avec la ligne concernée.

| Espace réservé | Signification | Exemple | Obligatoire |
| --- | --- | --- | --- |
| `{{项目名称}}` | Nom d'affichage du projet | `Awesome Tool` | Oui |
| `{{LOGO_DARK_URL}}` | Adresse du logo pour thème sombre | `media/logo-dark.svg` | Non |
| `{{LOGO_LIGHT_URL}}` | Adresse du logo pour thème clair | `media/logo-light.svg` | Non |
| `{{LOGO_WIDTH}}` | Largeur d'affichage du logo (px) | `200` | Non |
| `{{OWNER}}` | Propriétaire du dépôt | `octocat` | Non |
| `{{REPO}}` | Nom du dépôt | `awesome-tool` | Non |
| `{{WORKFLOW}}` | Nom du fichier de workflow CI | `ci.yml` | Non |
| `{{VERSION}}` | Numéro de version actuel | `1.2.0` | Non |
| `{{LICENSE_SPDX}}` | Identifiant SPDX de la licence | `MIT` | Oui |
| `{{RELEASE_URL}}` | URL de la page de publication | Lien GitHub Releases | Non |
| `{{仓库描述中文}}` | Partie chinoise de la description du dépôt, ≤ 120 caractères | `Outil en ligne de commande léger pour traiter du JSON en Go` | Oui |
| `{{REPO_DESCRIPTION_EN}}` | Partie anglaise de la description du dépôt, ≤ 120 caractères | `A lightweight Go CLI for JSON processing` | Oui |
| `{{TOPICS}}` | Étiquettes de sujets, 20 mots anglais en minuscules, reliés par `-` | `go cli json command-line developer-tools` | Non |
| `{{一句话定位}}` | Phrase unique indiquant ce qu'est le projet, à qui il s'adresse et quel problème il résout | `Outil léger en ligne de commande Go pour traiter du JSON` | Oui |
| `{{语言切换链接}}` | Lien de bascule entre versions multilingues | Texte du lien `English`, chemin cible selon le répertoire de langue réel, par ex. `../en-US/README.md` | Non |
| `{{背景}}` | Raison d'être du projet et problème à résoudre | Selon le projet | Oui |
| `{{核心思路}}` | Approche clé ou arbitrage de conception retenu | Selon le projet | Oui |
| `{{适用场景一}}` / `{{适用场景二}}` | Situations adaptées à l'usage | `Traitement rapide de petits fichiers JSON` | Oui |
| `{{不适用场景一}}` / `{{不适用场景二}}` | Situations explicitement déconseillées et raisons | `Traitement en flux de fichiers de l'ordre du Go` | Oui |
| `{{优势名称}}` | Nom substantif de l'avantage | `Zéro dépendance` | Non |
| `{{优势说明}}` | Description concrète de l'avantage | `Aucune dépendance d'exécution tierce` | Non |
| `{{证据}}` | Preuve vérifiable ou étapes reproductibles de l'avantage | La sortie de `ldd` est vide | Non |
| `{{局限描述}}` | Description concrète de la limite | `Pas de prise en charge de l'écriture concurrente` | Non |
| `{{影响范围}}` | Fonctionnalité ou scénario affecté par la limite | `Écriture simultanée par plusieurs processus` | Non |
| `{{规避方式}}` | Contournement temporaire de la limite | `Verrouillage externe` | Non |
| `{{功能一}}` / `{{功能二}}` / `{{功能三}}` | Nom de la fonctionnalité | `Filtrage` | Oui |
| `{{触发条件与结果}}` | Condition de déclenchement et résultat de la fonctionnalité | `Transmission de --filter puis sortie selon la condition` | Oui |
| `{{特性名称}}` | Nom de la caractéristique, 15 caractères maximum | `Distribution en fichier unique` | Non |
| `{{价值}}` | Problème concret résolu par la caractéristique et conséquence en cas de non-résolution | Selon le projet | Non |
| `{{实现方式}}` | Technologie, mécanisme ou algorithme retenu, avec fichiers ou fonctions clés | Selon le projet | Non |
| `{{差异化}}` | Dimension de comparaison objectivement évaluable avec une solution nommée | Selon le projet | Non |
| `{{证据}}` | Test reproductible, benchmark, emplacement de code ou étapes | Selon le projet | Non |
| `{{取舍主题}}` | Thème de l'arbitrage d'ingénierie | `Écriture concurrente` | Non |
| `{{场景}}` | Situation concrète déclenchant cette conception | Selon le projet | Non |
| `{{处理方式}}` | Solution retenue | Selon le projet | Non |
| `{{原因}}` | Raison du rejet des autres solutions | Selon le projet | Non |
| `{{运行时与版本}}` / `{{构建工具与版本}}` / `{{测试工具与版本}}` | Nom et version du composant de la pile technique | `Go 1.22` | Non |
| `{{运行时版本约束}}` / `{{构建版本约束}}` / `{{测试版本约束}}` | Plage de contraintes de version | `>=1.22` | Non |
| `{{运行时用途}}` / `{{构建用途}}` / `{{测试用途}}` | Usage du composant | `Compilation et exécution` | Non |
| `{{运行时 / 操作系统 / 版本}}` | Prérequis de l'environnement d'installation | `Go 1.22+, Linux/macOS` | Oui |
| `{{包管理器安装命令}}` | Commande d'installation réelle | `go install example.com/tool@latest` | Oui |
| `{{验证命令}}` | Commande de vérification de l'installation | `tool --version` | Non |
| `{{预期输出}}` | Résultat attendu de la commande de vérification | `tool 1.2.0` | Non |
| `{{升级命令}}` / `{{卸载命令}}` | Commandes de mise à niveau et de désinstallation | `go install example.com/tool@latest` | Non |
| `{{容器化说明}}` | Explication de la conteneurisation ou adresse d'image | `docker run ...` | Non |
| `{{一句话说明本示例完成什么}}` | Objectif de l'exemple de démarrage rapide | `Filtrer le JSON par champ puis produire la sortie` | Oui |
| `{{语言标识}}` | Identifiant de langage du bloc de code | `bash` | Oui |
| `{{最小可运行示例}}` | Exemple minimal exécutable | Selon le projet | Oui |
| `{{输出}}` | Sortie attendue de l'exemple | Selon le projet | Oui |
| `{{键名}}` | Nom de la clé de configuration | `output.format` | Non |
| `{{类型}}` | Type de la valeur de configuration | `string` | Non |
| `{{默认值}}` | Valeur par défaut de la configuration | `json` | Non |
| `{{是否必填}}` | Caractère obligatoire ou non | Non | Non |
| `{{取值范围}}` | Plage de valeurs autorisées | `json / yaml` | Non |
| `{{作用}}` | Rôle de la configuration | `Définir le format de sortie` | Non |
| `{{示例值}}` | Exemple de configuration | `yaml` | Non |
| `{{配置优先级}}` | Ordre de priorité des configurations multi-sources | `Arguments de ligne de commande > variables d'environnement > fichier de configuration` | Non |
| `{{热更新支持说明}}` | Prise en charge du rechargement à chaud et modalités | `Non pris en charge ; redémarrage requis` | Non |
| `{{模块概述}}` | Aperçu de l'usage du module | Selon le projet | Non |
| `{{接口签名}}` | Signature de fonction ou d'interface | `func Filter(in io.Reader, key string) error` | Non |
| `{{参数名}}` / `{{参数类型}}` / `{{参数是否必填}}` / `{{参数说明}}` | Champs des paramètres d'interface | in / io.Reader / Oui / flux d'entrée | Non |
| `{{返回值说明}}` | Signification de la valeur de retour | Retourne `nil` en cas de succès | Non |
| `{{错误码}}` / `{{错误含义}}` / `{{错误处理方式}}` | Champs du code d'erreur | E001 / entrée vide / vérifier l'entrée | Non |
| `{{调用示例}}` | Code d'appel de l'interface | Selon le projet | Non |
| `{{限流与配额说明}}` | Règles de limitation de débit et de quotas | `Aucune limitation de débit` | Non |
| `{{API_DOC_PATH}}` | Chemin relatif de la documentation de l'API | `./docs/api.md` | Non |
| `{{项目名}}` | Nom du nœud racine de l'arborescence | `awesome-tool` | Oui |
| `{{目录条目}}` / `{{职责}}` | Entrée de l'arborescence et responsabilité | cmd/ / point d'entrée des commandes | Oui |
| `{{测试环境}}` | Matériel, système, version de l'environnement d'exécution | Intel i7 / Ubuntu 22.04 / Go 1.22 | Non |
| `{{测试方法}}` | Méthode de test de performance | `go test -bench` | Non |
| `{{性能指标}}` / `{{指标数值}}` / `{{对比基线}}` | Champs des indicateurs de performance | Débit / 120 MB/s / 80 MB/s | Non |
| `{{瓶颈分析}}` | Explication des goulets d'étranglement de performance | Selon le projet | Non |
| `{{调优建议}}` | Recommandations d'optimisation des performances | Selon le projet | Non |
| `{{数据收集与存储说明}}` | Périmètre de collecte et mode de stockage des données | `Aucune collecte de données utilisateur` | Non |
| `{{传输加密说明}}` | Mode de chiffrement en transit | `HTTPS` | Non |
| `{{权限模型说明}}` | Explication du modèle de permissions | Basé sur un jeton | Non |
| `{{已知风险}}` | Risques de sécurité connus | Selon le projet | Non |
| `{{漏洞上报渠道}}` | Canal de signalement des vulnérabilités réellement joignable | `security@example.com` | Non |
| `{{操作系统}}` / `{{操作系统验证状态}}` | Périmètre de prise en charge des systèmes d'exploitation et état de vérification | Linux, macOS / vérifié | Non |
| `{{运行时兼容版本}}` / `{{运行时验证状态}}` | Périmètre de compatibilité de l'environnement d'exécution et état de vérification | Go 1.20+ / vérifié | Non |
| `{{浏览器}}` / `{{浏览器验证状态}}` | Périmètre de prise en charge des navigateurs et état de vérification | Chrome 100+ / vérifié | Non |
| `{{数据库版本}}` / `{{数据库验证状态}}` | Version de base de données et état de vérification | PostgreSQL 14+ / vérifié | Non |
| `{{明确不支持项}}` | Environnements explicitement non pris en charge | Windows 32 bits | Non |
| `{{问题描述}}` | Description du problème connu | Consommation mémoire élevée en cas d'entrée très longue | Non |
| `{{影响范围}}` | Fonctionnalité ou scénario affecté par le problème | Lorsque l'entrée dépasse 100 Mo | Non |
| `{{临时规避方案}}` | Mode de contournement temporaire | Traitement par lots | Non |
| `{{跟踪链接}}` | Adresse de suivi du problème | Lien GitHub Issue | Non |
| `{{当前限制说明}}` | Limites fonctionnelles actuelles | Écriture concurrente non encore prise en charge | Non |
| `{{未实现功能}}` | Fonctionnalité non encore implémentée | Rechargement à chaud de la configuration | Non |
| `{{未实现原因}}` | Raison de la non-implémentation | Priorité faible | Non |
| `{{计划状态}}` | État de la planification (pour les fonctionnalités non implémentées et la feuille de route) | Planifié | Non |
| `{{计划项}}` | Élément planifié de la feuille de route | Prise en charge du rechargement à chaud du fichier de configuration | Non |
| `{{目标版本}}` | Version cible de l'élément planifié | `v1.3.0` | Non |
| `{{搭建步骤}}` | Étapes ou lien de mise en place de l'environnement de développement | Voir CONTRIBUTING.md | Non |
| `{{说明}}` | Explication du modèle de branches | Créer des branches `feat` depuis `main` | Non |
| `{{Conventional Commits 等}}` | Explication de la convention de commit | `Conventional Commits` | Non |
| `{{要求}}` | Exigences relatives aux PR | Modification à objet unique, tests réussis | Non |
| `{{年份}}` | Année du copyright | `2026` | Oui |
| `{{著作权人}}` | Titulaire des droits d'auteur | `Ntarstudio` | Oui |
| `{{SPDX 标识符}}` | Identifiant SPDX dans la ligne de copyright | `MIT` | Oui |
| `{{许可证名称}}` | Nom complet de la licence | `MIT` | Oui |

## 5. Description des sections facultatives

La section 3 fournit le corps copiable des 20 chapitres. Voici des compléments sur l'ajout et la suppression selon le type de projet ; la suppression d'une section impose de supprimer également le lien de navigation de premier écran.

| Section | Types de projets où la conserver | Condition de suppression |
| --- | --- | --- |
| Caractéristiques clés | Tous | Supprimable en l'absence de preuve vérifiable, sans substitution par une description qualitative |
| Détails de conception et arbitrages d'ingénierie | Frameworks, applications, services | Supprimable en l'absence d'arbitrage clé |
| Pile technique et liste des dépendances | Bibliothèques, frameworks | Supprimable en l'absence de dépendances externes |
| Performances | CLI, bibliothèques, services | Supprimable en l'absence de données de test ; les chiffres estimés sont interdits |
| Sécurité et confidentialité | Services, applications, projets traitant des données personnelles | Peut être allégée pour un outil purement local |
| Compatibilité | Bibliothèques, SDK, applications multiplateformes | Peut être allégée pour un environnement d'exécution unique |
| Journal des modifications | Tous | Remplacé par un résumé des changements intégré uniquement si CHANGELOG n'existe pas |
| Feuille de route | Tous | Supprimable en l'absence de plan public |
| Déclaration de conformité NOTICE | Projets avec dépendances tierces | Supprimable en l'absence de dépendances tierces |

## 6. Liste d'auto-vérification avant livraison

- [ ] Aucun espace réservé `{{...}}` résiduel.
- [ ] Le premier écran contient la description du dépôt 【chinois | anglais】 et les étiquettes de sujets, cohérentes avec les métadonnées du dépôt.
- [ ] La description du dépôt ne dépasse pas 120 caractères en chinois comme en anglais.
- [ ] Les étiquettes de sujets atteignent 20 entrées, toutes en anglais minuscule, reliées par `-`.
- [ ] Le positionnement en une phrase contient un terme de catégorie ; 60 caractères maximum en chinois, 25 mots maximum en anglais.
- [ ] Chaque caractéristique clé comporte la structure en cinq parties avec des preuves vérifiables.
- [ ] Avantages et limites sont séparés ; les limites incluent le périmètre d'impact et le mode de contournement.
- [ ] Les problèmes connus incluent un lien de suivi ; les fonctionnalités non implémentées incluent la raison et l'état de la planification.
- [ ] La feuille de route est marquée « non contraignante » et ne contient aucune date de livraison précise.
- [ ] Les cas non applicables et les éléments explicitement non pris en charge sont listés.
- [ ] Le titre de niveau 1 est unique, les titres de niveau 2 sont hiérarchisés de façon continue, l'ordre des sections est identique aux 20 chapitres de la spécification.
- [ ] Le style des badges est unifié, les liens sont valides, le texte alternatif est explicite.
- [ ] Les commandes d'installation et l'exemple de démarrage rapide ont été testés et fonctionnent.
- [ ] Tous les blocs de code indiquent leur langage, toutes les images disposent d'un texte alternatif.
- [ ] Les chemins relatifs restent utilisables après fork et hors ligne.
- [ ] Le fichier LICENSE existe et l'identifiant SPDX correspond à celui du README.
- [ ] L'ordre des sections des versions chinoise et anglaise se correspond une à une.

## Fichiers associés

- Définition complète des sections : voir la [Spécification des sections de README](./readme-sections-specification.md)
- Configuration des badges : voir la [Spécification des badges](./badge-specification.md)
- Règles visuelles : voir la [Spécification de mise en page visuelle du README](./readme-visual-layout-specification.md)
- Sélection par type : voir le [Guide d'adaptation du README par catégorie](./readme-category-adaptation-guide.md)
- Base de l'étude : voir le [Rapport d'étude sur les gabarits de README](./readme-template-research-report.md)
- Rédaction des caractéristiques et arbitrages : voir la [Guide de rédaction des caractéristiques et arbitrages d'ingénierie](./features-and-engineering-tradeoffs-guide.md)
- Règles de métadonnées : voir la [Spécification de nommage des projets](./project-naming-specification.md)
- Règles de feuille de route : voir la [Spécification de la feuille de route](./roadmap-specification.md)
