# Gabarit de guide de contribution

> Problème que ce fichier résout : fournir un gabarit de guide de contribution directement copiable, permettant à un projet de générer le fichier CONTRIBUTING.md en couvrant les modes de participation, la mise en place de l'environnement, le modèle de branches, la convention de commit, les exigences relatives aux PR, les exigences de tests, le code de conduite et la déclaration de licence ; les consignes de remplissage associées couvrent les modalités d'adaptation selon le type de projet.

## 1. Mode d'emploi

1. Copier l'intégralité du contenu de la section 3 « Corps du gabarit » et créer le fichier `CONTRIBUTING.md` à la racine du projet.
2. Remplacer les espaces réservés conformément à la section 4 ; toutes les commandes doivent être des commandes réelles directement exécutables.
3. Adapter selon les variantes de scénario de la section 5 : pour un projet documentaire, supprimer le paragraphe des commandes de test et conserver les processus Issue et PR.
4. La base des règles figure dans la [spécification du guide de contribution](./contribution-guide-specification.md) ; les détails relatifs aux branches et aux commits figurent respectivement dans la [spécification du workflow Git et de la gestion des branches](./git-workflow-and-branching-specification.md) et la [spécification des messages de commit](./commit-message-specification.md).

## 2. Principes de personnalisation

- **Exécutable** : les commandes précisent le répertoire de travail complet et les prérequis de dépendances ; il est interdit de se limiter à « installer les dépendances » sans commande concrète.
- **Avec condition de déclenchement** : chaque étape précise quand l'exécuter et le résultat attendu.
- **Non générique** : il est interdit de se limiter à « les PR sont bienvenues » sans processus concret, conformément au contrôle de gouvernance communautaire de la [porte qualité](./quality-gate.md).
- **Référencer plutôt que recopier** : les règles de commit et de test renvoient aux spécifications correspondantes, sans en répéter le texte intégral dans ce fichier.

## 3. Corps du gabarit

````markdown
# Guide de contribution

> Ce fichier explique comment participer à la contribution de {{项目名称}} ; il s'adresse aux contributeurs externes et aux participants de première fois.

## Modes de participation

| Mode | Scénario applicable | Point d'entrée |
| --- | --- | --- |
| Discussion des tickets | Suggestions de fonctionnalités, remontée de problèmes | {{议题入口}} |
| Amélioration de la documentation | Fautes de frappe, ajout d'exemples, optimisation de la structure | Soumission directe d'une PR |
| Contribution au code | Correction de défauts, implémentation de fonctionnalités | Voir le processus ci-dessous |
| Remontée de problèmes | Blocage d'utilisation, reproduction d'anomalies | {{问题反馈入口}} |

## Mise en place de l'environnement de développement

Prérequis : {{环境前提}}

```bash
# Cloner le dépôt
git clone {{仓库地址}}
cd {{项目目录名}}

# Installer les dépendances
{{依赖安装命令}}

# Exécution locale
{{本地运行命令}}
```

Résultat attendu : {{验证本地环境可用的方式}}

## Modèle de branches

- Créer une branche personnelle à partir de {{基准分支}}, au format de nommage `{{分支命名格式}}` (par exemple `feat/description-courte`).
- Chaque PR ne traite qu'un seul sujet ; en cas de périmètre de modification trop large, veuillez scinder.
- Il est interdit de committer directement sur {{受保护分支}} ; la fusion doit passer par une PR.

## Convention de commit

Les messages de commit suivent les Conventional Commits, au format `type(scope): subject`. Types courants : `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Exemple :

```text
feat(cli): add config file support
```

Les règles complètes figurent dans la [spécification des messages de commit]({{提交规范链接}}).

## Exigences relatives aux PR

Avant de soumettre une PR, veuillez effectuer les vérifications suivantes :

- [ ] Le périmètre de modification est unique et dispose d'un ticket ou d'une explication correspondante.
- [ ] Le message de commit respecte le format ci-dessus.
- [ ] L'exécution locale de `{{测试命令}}` est entièrement réussie.
- [ ] La documentation est mise à jour en même temps que le code.
- [ ] Aucune clé, clé privée ou information sensible n'a été introduite.
- [ ] La description précise le contenu des modifications, leur motif et la méthode de vérification.

## Exigences de tests

| Élément de contrôle | Commande | Critère de réussite |
| --- | --- | --- |
| Tests unitaires | `{{单元测试命令}}` | Entièrement réussis |
| Analyse statique | `{{lint 命令}}` | Aucune erreur |
| Vérification de build | `{{构建命令}}` | Build réussi |

Seuil de couverture : {{覆盖率要求}}.

## Code de conduite

Participer à ce projet implique l'engagement de respecter le [code de conduite](./CODE_OF_CONDUCT.md).

## Convention relative aux Issue

- Rechercher les tickets existants avant de poser une question, afin d'éviter les doublons.
- Un rapport de défaut doit contenir : informations sur l'environnement, étapes de reproduction, résultat attendu, résultat réel, journaux d'erreur.
- Une suggestion de fonctionnalité doit préciser le scénario d'usage et la solution alternative en cas de non-adoption.

## Déclaration de licence

Les contributions suivent par défaut la licence de ce projet {{许可证名称及 SPDX 标识符}}, dont le texte intégral figure dans [LICENSE](./LICENSE). La soumission vaut déclaration que vous disposez du droit d'autoriser votre contribution sous cette licence.
````

## 4. Tableau de correspondance des espaces réservés et définition des champs

| Espace réservé | Obligatoire | Définition du champ | Exemple de saisie |
| --- | --- | --- | --- |
| `{{项目名称}}` | Oui | Nom public du projet | `FooBar` |
| `{{议题入口}}` | Oui | Adresse réelle et accessible des tickets | `https://github.com/owner/repo/issues` |
| `{{问题反馈入口}}` | Non | Canal dédié lorsqu'il diffère de l'entrée des tickets | `https://github.com/owner/repo/issues/new` |
| `{{环境前提}}` | Oui | Version du langage, gestionnaire de paquets et dépendances système | `Node.js 20+、pnpm 8+` |
| `{{仓库地址}}` | Oui | Adresse du dépôt permettant le clonage | `https://github.com/owner/repo.git` |
| `{{项目目录名}}` | Oui | Nom du répertoire après clonage | `repo` |
| `{{依赖安装命令}}` | Oui | Commande d'installation réelle | `pnpm install` |
| `{{本地运行命令}}` | Oui | Commande de démarrage réelle | `pnpm dev` |
| `{{验证本地环境可用的方式}}` | Oui | Signe de succès observable | `L'accès à localhost:3000 affiche la page d'accueil` |
| `{{基准分支}}` | Oui | Branche source à partir de laquelle la branche est créée | `main` |
| `{{分支命名格式}}` | Oui | Règle de nommage des branches | `feat/description-courte` |
| `{{受保护分支}}` | Oui | Branche sur laquelle tout commit direct est interdit | `main` |
| `{{提交规范链接}}` | Non | Adresse de la convention de commit interne ou externe au projet | `./docs/COMMIT_CONVENTION.md` |
| `{{测试命令}}` | Oui | Commande de test réelle | `pnpm test` |
| `{{lint 命令}}` | Oui | Commande d'analyse statique réelle | `pnpm lint` |
| `{{构建命令}}` | Oui | Commande de build réelle | `pnpm build` |
| `{{覆盖率要求}}` | Non | Seuil de couverture du nouveau code | `Nouveau code non inférieur à 80 %` |
| `{{许可证名称及 SPDX 标识符}}` | Oui | Nom complet et identifiant SPDX de la licence du projet | `Licence MIT (MIT)` |

## 5. Consignes de remplissage et variantes de scénario

| Scénario | Sections à conserver | Sections pouvant être supprimées | Points d'ajustement |
| --- | --- | --- | --- |
| Projet de code | Toutes | Aucune | Les commandes doivent être réellement exécutées et validées |
| Projet documentaire | Modes de participation, exigences relatives aux PR, code de conduite, licence | Exigences de tests, mise en place de l'environnement de développement | Supprimer le tableau des tests, conserver l'auto-vérification des PR |
| Projet personnel | Modes de participation, exigences relatives aux PR, code de conduite, licence | La mise en place de l'environnement peut être allégée | Préciser si les contributions externes sont acceptées |
| Projet d'entreprise | Toutes | Aucune | Ajouter le lien vers l'accord de licence de contributeur (CLA) et les exigences juridiques |

Tableau des erreurs fréquentes :

| Rédaction erronée | Conséquence | Rédaction correcte |
| --- | --- | --- |
| « Toute forme de contribution est bienvenue » | Aucun parcours concret, le contributeur ne sait pas par où commencer | Énumérer le tableau des modes de participation et les points d'entrée |
| « Il suffit de lancer les tests » | Ni commande ni critère de réussite connus | Préciser la commande, le critère de réussite et le seuil de couverture |
| Écrire `npm install` alors que le projet utilise pnpm | Commande non exécutable | Être cohérent avec le fichier lock réel |

## 6. Exemple complet

Voici un exemple rempli du paragraphe des commandes, fourni à titre de référence de format uniquement.

```bash
# Cloner le dépôt
git clone https://github.com/owner/repo.git
cd repo

# Installer les dépendances
pnpm install

# Exécution locale
pnpm dev
```

Résultat attendu : l'accès à localhost:3000 affiche la page d'accueil.

## Fichiers associés

- Spécification correspondante : [spécification du guide de contribution](./contribution-guide-specification.md)
- Gabarits complémentaires : [gabarit de code de conduite](./code-of-conduct-template.md), [gabarit SECURITY](./security-template.md)
- Détails des tests : [spécification des tests](./testing-specification.md)
- Dimension de gouvernance communautaire : [matrice des dimensions de revue](./review-dimension-matrix.md)
- Retour à l'index en chinois simplifié : [README](./README.md)
