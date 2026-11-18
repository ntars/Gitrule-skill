# Spécification de nommage des projets

> Problème que ce fichier résout : définir les règles impératives de caractères, de casse, de découpage, de longueur et de sémantique applicables au nom de dépôt, ainsi que la formule de nommage, les suffixes conventionnels, le processus de recherche et les exigences de métadonnées associées.

## 1. Règles impératives

| Règle | Exigence | Contre-exemple |
|---|---|---|
| Jeu de caractères | Uniquement `a-z`, `0-9`, `-` | `My_Proj`、`我的项目` |
| Casse | Entièrement en minuscules | `MyProject` |
| Découpage | kebab-case, relié par `-` | `myproject`、`my_project` |
| Longueur | 2–25 caractères | nom concaténé trop long |
| Terminaison | Nom ou suffixe morphologique | terminaison par `-project`, `-test` |
| Version | Sans numéro de version, année ni date | `tool-v2`、`app2024` |
| Mots sans information | `my`/`demo`/`test`/`new`/`tmp` interdits | `my-new-demo` |
| Unicité | Une recherche sur GitHub / npm / PyPI chacun | homonyme d'une bibliothèque connue |
| Sémantique | Le nom seul permet de lire « ce qu'il fait » | `xyz`、`abc123` |

## 2. Formule de nommage (un choix parmi quatre)

```text
<技术>-<对象>          vue-virtual-table      go-ratelimit
<对象>-<形态>          note-cli   image-api   config-loader
<动词>-<对象>          parse-markdown   sync-dotfiles
<领域>-<子领域>        web-ui-kit   data-pipeline
```

## 3. Suffixes conventionnels

`-cli` ligne de commande / `-sdk` bibliothèque cliente / `-api` `-server` côté serveur / `-template` `-boilerplate` échafaudage / `-loader` `-parser` intergiciel / `-kit` ensemble de composants / `-notes` `-guide` documentation / `dotfiles` dépôt de configuration / `awesome-xxx` compilation de ressources.

## 4. Processus de nommage

1. Écrire en une phrase « à qui le projet résout quel problème ».
2. Extraire de cette phrase le nom noyau + la forme, et appliquer l'une des formules de la section 2.
3. Générer 3 candidats et effectuer pour chacun une recherche d'homonymes.
4. Choisir celui qui reste le plus compréhensible sans lire le README.
5. Le nom chinois ne figure pas dans le nom du dépôt ; il est placé après le titre de la première ligne du README.

## 5. Métadonnées associées

### 5.1 Description du dépôt (description)

- De même origine que le nom du dépôt, selon la formule : `<ce qu'il fait> for <pour qui>`.
- Format bilingue fusionné : `langue nationale | anglais`, la version en langue nationale d'abord, puis une barre verticale demi-chasse (un espace de chaque côté), puis la version anglaise. Exemple pour un projet chinois :

```text
轻量级 Go 命令行 JSON 处理工具 | A lightweight Go CLI for JSON processing
```

- Longueur : la version en langue nationale et la version anglaise ne dépassent chacune pas 120 caractères, le total bilingue ne dépassant pas 350 caractères (limite GitHub).
- Arbitrage en cas de dépassement du total bilingue : compresser en priorité la version anglaise plutôt que la version en langue nationale — la densité informationnelle du chinois étant plus élevée, compresser le chinois fait perdre davantage d'information ; lors de la compression, supprimer d'abord les épithètes et les déterminants redondants, puis fusionner les formulations synonymes, et enfin conserver la structure sujet-prédicat complète de chacune des deux versions linguistiques.
- Sans saut de ligne, sans syntaxe Markdown ni Emoji ; le style de ponctuation finale est identique dans les deux langues (point final ajouté partout ou nulle part).

### 5.2 Sujets (topics)

- Remplir les 20 (limite GitHub), couverture complète, sans laisser de place vide.
- Tous en anglais ; l'usage du chinois ou de toute autre langue est interdit ; entièrement en minuscules, reliés par `-`, sans espace ni caractère spécial.
- Couvrir intégralement les cinq catégories : langue, domaine, forme, écosystème, scénario ; des termes génériques comme documentation, open-source peuvent être ajoutés en complément.
- À définir dès la création du dépôt, sans laisser vide ; à revérifier une fois après un renommage ou un repositionnement du dépôt.

## Fichiers associés

- La conformité du nommage relève de la règle absolue H1, voir les [règles absolues](./hard-rules.md)
- L'audit des métadonnées relève de la dimension D10, voir la [matrice des dimensions d'audit](./review-dimension-matrix.md)
- Le document porteur est `docs/naming.md`, voir la [matrice documentaire](./document-matrix.md)
