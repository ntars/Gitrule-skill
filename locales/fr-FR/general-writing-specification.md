# Spécification générale de rédaction

> Problème que ce fichier résout : définir le registre, l'exactitude, la cohérence terminologique, les règles de forme et les contenus interdits de tous les documents livrés, afin de garantir une formulation précise, sans ambiguïté et reproductible.

## 1. Registre

1. Employer la langue écrite, avec des phrases déclaratives et impératives.
2. Les formulations familières sont interdites, par exemple « 咱们 », « 超简单 », « 搞定 », « 贼快 », « 一键起飞 ».
3. Les points d'exclamation, points de suspension, abréviations issues d'Internet et émojis sont interdits.
4. Les phrases interrogatives, rhétoriques ou non, sont interdites en ouverture de section.

## 2. Exactitude

1. Chaque phrase doit exprimer une sémantique complète, sans dépendre d'une déduction contextuelle.
2. Les références vagues du type « il », « ceci », « concerné », « certains », « plusieurs » sont interdites ; lorsqu'une référence est nécessaire, employer le nom complet.
3. Les dates, numéros de version, chemins, commandes, noms de fonctions et noms de clés de configuration doivent être exacts et conformes à la réalité du projet.
4. Les commandes doivent être directement exécutables et comporter l'indication nécessaire du répertoire de travail courant.
5. Lorsqu'un numéro de version est mentionné, la sémantique de contrainte de version doit être précisée, par exemple `>=1.2.0 <2.0.0`.

## 3. Cohérence terminologique

1. Un terme est défini lors de sa première apparition, au format « terme chinois (English Term, abréviation) ».
2. Un même concept n'emploie qu'une seule formulation dans tout le document ; les termes des versions chinoise et anglaise se correspondent un à un.
3. Un tableau de correspondance terminologique chinois-anglais doit être maintenu, placé en annexe du README ou dans un fichier distinct ; les versions bilingues partagent le même tableau (gabarit dans la [collecte d'informations et gabarits](./information-collection-and-templates.md)).

## 4. Règles de forme

1. La hiérarchie des titres commence à `##` (`#` étant réservé au nom du projet) ; aucun niveau ne doit être sauté.
2. Chaque titre de niveau deux correspond à une section définie par la [spécification des sections du README](./readme-sections-specification.md), sans modification de l'ordre.
3. Les tableaux doivent avoir un en-tête et un nombre de colonnes homogène ; les commandes, chemins, code et noms de clés de configuration sont balisés en code en ligne.
4. Les blocs de code doivent porter une identification de langage ; les commandes multilignes doivent pouvoir être copiées et exécutées en bloc.
5. Les liens externes utilisent une URL complète, sans raccourcisseur ; les renvois internes utilisent une ancre en chemin relatif.
6. Une espace sépare le chinois de l'anglais et des chiffres ; la ponctuation chinoise et la ponctuation latine ne sont pas mélangées.

## 5. Convention d'espaces réservés

1. Les espaces réservés officiels des gabarits copiables s'écrivent uniformément `{{纯名}}`, par exemple `{{仓库地址}}` ; le nom ne doit contenir ni conjonction de choix exclusif du type « 或 », « ， », ni être rédigé sous forme de phrase explicative.
2. Un espace réservé officiel doit être enregistré dans le tableau de correspondance des espaces réservés du gabarit auquel il appartient ; l'entrée comprend la signification, un exemple et le caractère obligatoire ou non.
3. Le contenu entre accolades en langage naturel présent dans les exemples de spécification ou les indications de saisie n'est qu'illustratif, ne constitue pas un espace réservé officiel et n'est pas inscrit au tableau de correspondance ; lors de la génération du document final, il doit être entièrement remplacé par le contenu réel.
4. Il est interdit d'utiliser des accolades imbriquées, des accents graves ou un second espace réservé comme nom d'espace réservé.

## 6. Liste des interdictions

Ne doivent apparaître : aucun chiffre de performance non vérifié, aucune conclusion comparative sans source, aucune formulation d'engagement (par exemple « 保证兼容所有环境 », « 永久免费 »), aucune description dénigrante d'un projet tiers, aucun contenu promotionnel sans lien avec le projet.

## Fichiers associés

- Structure des sections : voir la [spécification des sections du README](./readme-sections-specification.md)
- Correspondance terminologique bilingue : voir la [spécification multilingue](./multilingual-specification.md)
- Évaluation qualité G1 (registre familier et ambiguïté) : voir la [porte qualité](./quality-gate.md)
