# Spécification multilingue

> Problème que ce fichier résout : définir la disposition des fichiers par répertoire de code de langue, le changement de langue, la cohérence des traductions, la cohérence du code et les règles de synchronisation des modifications unilatérales.

## 1. Disposition des répertoires

1. Le `README.md` à la racine du dépôt ne sert qu'à la page d'accueil du projet et à la navigation linguistique ; il ne porte pas le corps des spécifications.
2. Les spécifications concrètes sont réparties à plat dans le répertoire `locales/<language-code>/`, par exemple `locales/zh-CN/角色与职责.md`.
3. Le code de langue suit le style BCP 47, par exemple `zh-CN`, `en-US`, `ja-JP`, `ko-KR` ; le code de langue n'apparaît que dans le nom du répertoire, jamais dans le nom du fichier.
4. **Le nom de fichier doit être dans la langue concernée** : le répertoire chinois utilise des noms de fichier chinois (`角色与职责.md`), le répertoire anglais des noms en minuscules avec traits d'union (`roles-and-responsibilities.md`), et de même pour les autres langues ; il est interdit de conserver des noms de fichier chinois dans un répertoire non chinois.
5. Les noms de fichier des différents répertoires de langue ne doivent pas nécessairement se correspondre mot pour mot, mais une correspondance biunivoque est obligatoire : la même spécification a la même responsabilité de contenu dans chaque répertoire de langue, et la correspondance est consignée dans le champ `paths` du fichier de manifeste (voir la [spécification des métadonnées lisibles par machine](./machine-readable-metadata-specification.md)).
6. Le chinois simplifié et l'anglais constituent les versions de la première vague ; pour les autres langues, le tableau des langues du `README.md` racine indique « à compléter » ou « terminé », et une langue sans répertoire créé ne doit pas proposer de lien vide.
7. L'ajout d'une langue se limite à créer le répertoire de langue correspondant et à traduire chaque document ; les fichiers des langues existantes ne sont pas modifiés ; seules les autres langues déjà terminées sont mises à jour lorsqu'une révision de la langue source doit être synchronisée.

## 2. Changement de langue

1. Le `README.md` de chaque répertoire de langue doit proposer en tête des liens de changement de langue.
2. Les liens utilisent des chemins relatifs au répertoire de langue courant, par exemple la forme employée dans le répertoire chinois simplifié :
   `[English](../en-US/README.md) | [简体中文](./README.md)`.
3. Le texte des liens utilise l'autodésignation dans la langue cible, par exemple `English`, `简体中文`, `日本語`, sans abréviations du type `CN`, `EN`.
4. Les liens de changement ne pointent que vers des répertoires de langue existants ; les répertoires de langue non créés sont signalés globalement par le tableau des langues du `README.md` racine, afin de ne laisser aucun lien mort dans le corps du texte.

## 3. Cohérence des traductions

1. La traduction doit être intégrale : le nombre de sections, leur ordre, le nombre de colonnes des tableaux et le nombre de blocs de code doivent être identiques à la langue source ; aucune production de type résumé ou traduction automatique non relue n'est admise.
2. Dans les blocs de code, les commandes, chemins, noms de clés de configuration, noms d'espaces réservés et valeurs de paramètres restent inchangés ; seuls les commentaires et les textes explicatifs sont traduits. Par exemple, dans une clôture d'arborescence comme `├── SKILL.md   obligatoire : métadonnées + processus principal`, les glyphes de branche et les chemins restent inchangés, tandis que la description qui suit doit être traduite.
3. **Les champs de gabarit destinés à l'utilisateur doivent être localisés** : dans la configuration `yaml` d'un formulaire d'issue, `name`, `label`, `description`, `placeholder` et les options de liste déroulante s'affichent directement sur la page GitHub et doivent être traduits dans la langue cible ; les champs structurés `type`, `id`, `labels`, `required`, `render` restent en anglais. Le critère est « cet élément est-il montré à une personne », et non « se trouve-t-il dans un bloc de code ». Par le même principe, le corps des gabarits copiables placé dans un bloc `markdown` est toujours traduit.
4. Les termes sont unifiés selon le tableau de correspondance terminologique chinois-anglais de la [collecte d'informations et gabarits](./information-collection-and-templates.md) ; un même concept utilise le même jeu de correspondances dans toutes les langues.
5. Toute modification unilatérale doit être synchronisée dans toutes les langues déjà terminées, et le journal des mises à jour doit consigner les codes de langue et la version synchronisés ; sans synchronisation achevée, la révision ne peut pas être considérée comme terminée.
6. La vérification de cohérence relève de la porte G10, voir la [porte qualité](./quality-gate.md).

## 4. Textes juridiques

1. Le NOTICE est fourni par défaut en version chinoise ; les textes juridiques que sont le texte original des licences, les mentions de copyright et les clauses de non-responsabilité conservent leur version anglaise originale, sans traduction ni réécriture.
2. Un texte juridique nécessitant un affichage bilingue chinois-anglais doit présenter côte à côte l'original et la traduction, en indiquant « traduction fournie à titre indicatif, l'original fait foi ».
3. Le traitement linguistique des textes juridiques est décrit dans la [spécification NOTICE](./notice-specification.md) et la [clause de non-responsabilité](./disclaimer.md).

## Fichiers associés

- Navigation linguistique racine : [accueil du dépôt](../../README.md)
- Manifeste des langues et identifiants stables : [spécification des métadonnées lisibles par machine](./machine-readable-metadata-specification.md)
- Base du nombre et de l'ordre des sections : les 20 sections de la [spécification des sections du README](./readme-sections-specification.md)
- Gabarit du tableau terminologique : voir la [collecte d'informations et gabarits](./information-collection-and-templates.md)
- Norme rédactionnelle : voir la [spécification générale de rédaction](./general-writing-specification.md)
- La synchronisation bilingue relève de la porte G10, voir la [porte qualité](./quality-gate.md)
