# Spécification de la promotion open source

> Problème que ce fichier résout : définir les canaux de promotion, le rythme de publication, les éléments de la page d'accueil et les règles d'animation de communauté des projets open source avant et après leur publication, afin que le projet bénéficie, sur la base d'une documentation utilisable, d'une visibilité à la hauteur de ses utilisateurs cibles.

La liste des canaux et les principes de ce fichier s'inspirent du chapitre consacré à la promotion du « Guide de roaming GitHub » de phodal ; ce projet, fort de 11 362 star, a validé l'adéquation de ces pratiques à la communauté open source sinophone.

## 1. Principes de base

1. **La qualité avant la promotion** : la promotion ne fait qu'amplifier une qualité existante, elle ne répare pas ce qui manque. Aucune promotion ne doit être lancée avant que le README, les exemples, la documentation et les tests soient prêts.
2. **Le projet ne se résume pas à sa promotion** : outre le code et le README, il faut préparer une documentation détaillée, des programmes d'exemple et un mécanisme de réponse aux questions.
3. **Motivation explicite** : la promotion sert un objectif concret (acquérir des premiers utilisateurs, recruter des contributeurs, recueillir des retours) ; il est interdit de promouvoir dans le seul but d'obtenir des star.
4. **Adéquation des canaux** : choisir les canaux en fonction de la pile technique du projet et des utilisateurs cibles, en évitant une diffusion indifférenciée.
5. **Présentation honnête** : il est interdit de fabriquer des chiffres de star, de téléchargement ou des cas d'usage ; les comparaisons de fonctionnalités doivent reposer sur des faits vérifiables.

## 2. Liste de préparation avant publication

| Catégorie | Exigence | Base d'appréciation |
| --- | --- | --- |
| Page d'accueil | Le README passe le contrôle des quatre questions (quoi / quel problème / fonctionnalités / exemple) | [Spécification des sections du README](./readme-sections-specification.md) |
| Accroche en une phrase | Catégorie et qualificatifs explicites, reformulable de manière autonome | Idem, section 1.1 |
| Exemple | Fournir un hello world exécutable en deux étapes au plus | [Gabarit standard du README](./readme-standard-template.md) |
| Documentation | Installation, configuration et documentation d'API complètes | [Matrice documentaire](./document-matrix.md) |
| Licence | LICENSE présent et cohérent avec l'identification du README | [Spécification LICENSE](./license-specification.md) |
| Conformité | Le NOTICE couvre les dépendances tierces | [Spécification NOTICE](./notice-specification.md) |
| Point d'entrée communautaire | Gabarits d'Issue, guide de contribution et code de conduite en place | [Spécification du guide de contribution](./contribution-guide-specification.md) |
| Mécanisme de réponse | Responsable de la réponse aux questions et délai de réponse explicites | [Spécification de la réponse aux incidents](./incident-response-specification.md) |

Lancer la promotion sans avoir achevé la liste ci-dessus constitue une pratique interdite par la présente spécification.

## 3. Classification des canaux

### 3.1 Communautés techniques internationales

| Canal | Contenu adapté | Points d'attention |
| --- | --- | --- |
| Hacker News | Implémentation technique, ingénierie approfondie | Le titre doit rester factuel, éviter le langage marketing |
| Sections Reddit correspondantes | Bibliothèques, outils, cadres applicatifs | Respecter les règles d'auto-promotion de chaque section |
| Lobsters | Programmation système, pratiques d'ingénierie | La communauté est sensible au marketing |
| Lettres d'information techniques (JavaScript Weekly, etc.) | Bibliothèques et outils | Fournir un résumé concis du projet |
| Blog officiel et site de documentation | Présentation approfondie et notes de version | Servir de point d'atterrissage aux autres canaux |

### 3.2 Communautés techniques sinophones

| Canal | Contenu adapté |
| --- | --- |
| Juejin | Front-end, mobile, pratiques d'ingénierie |
| Developer Headlines | Projets techniques généralistes |
| V2EX | Outils, logiciels de productivité, projets de start-up |
| Zhihu | Décryptage technique et arbitrages de conception |
| Compte officiel WeChat | Articles longs approfondis, séries de tutoriels |
| Geek Headlines | Actualité technique généraliste |

### 3.3 Canaux propres au projet

1. Les points d'entrée communautaires du README du projet (Discussions, Discord) ;
2. Le compte social dédié au projet, utilisé pour publier les versions et les activités ;
3. Le site de documentation et le site d'exemples, servant de pages de réception du trafic externe.

## 4. Rythme de publication

1. **Phase de préchauffage** : achever la liste de la section 2, préparer les éléments tels que l'accroche en une phrase, les captures d'écran et le GIF de démonstration.
2. **Phase de lancement** : publier sur 1 ou 2 canaux les plus adaptés, en évitant de saturer plusieurs plateformes avec le même contenu.
3. **Phase de réponse** : maintenir un rythme de réponse élevé dans les 72 heures suivant le lancement, traiter les Issue et les retours.
4. **Phase d'itération** : mettre à jour en continu au rythme des publications de version, chaque publication étant accompagnée de ses notes de changement.
5. **Phase de capitalisation** : rassembler les questions récurrentes dans une FAQ et en nourrir la documentation.

## 5. Exigences relatives aux éléments de la page d'accueil

| Élément | Spécification | Usage |
| --- | --- | --- |
| Accroche en une phrase | 60 caractères au plus en chinois / 25 mots au plus en anglais ; la Description du dépôt adopte le format bilingue combiné « langue nationale \| anglais », voir la section 5 de la [spécification de nommage des projets](./project-naming-specification.md) | Description du dépôt, résumé social |
| Capture d'écran | Double version thème clair et thème sombre, largeur maîtrisée | Premier écran du README |
| GIF de démonstration | Volume maîtrisé après compression, illustrant le parcours principal | Section de démonstration du README |
| Logo | Format SVG, avec double version claire et sombre | Premier écran et cartes sociales |
| Tableau comparatif des fonctionnalités | Fondé sur des faits vérifiables, incluant les cas non applicables | README ou site de documentation |

Les éléments doivent être mis à jour en même temps que les versions, afin d'éviter d'afficher une interface obsolète.

## 6. Animation de communauté

1. Offrir aux primo-contributeurs un point d'entrée explicite, tel que l'étiquette `good first issue`.
2. La réponse aux questions doit être tracée, afin d'éviter la répétition des mêmes questions.
3. Le code de conduite s'applique à tous les canaux communautaires, voir la [spécification du code de conduite](./code-of-conduct-specification.md).
4. Les remerciements aux contributeurs sont regroupés en un seul endroit, afin d'éviter leur dispersion dans le corps du texte.
5. Il est interdit d'obtenir une attention artificielle par des moyens incitatifs tels que l'échange de star ou de likes mutuels.

## 7. Pratiques interdites

1. Il est interdit de promouvoir tant que la liste de qualité n'est pas achevée.
2. Il est interdit de fabriquer ou d'exagérer les données et les cas d'usage du projet.
3. Il est interdit de saturer plusieurs canaux avec le même contenu.
4. Il est interdit de dénigrer des projets similaires pour valoriser sa propre image.
5. Il est interdit de recourir à des procédés incitatifs pour obtenir des star.

## Fichiers associés

- Les quatre questions de la page d'accueil et l'accroche en une phrase figurent dans la [spécification des sections du README](./readme-sections-specification.md)
- Les spécifications des éléments visuels figurent dans la [spécification de mise en page visuelle du README](./readme-visual-layout-specification.md)
- Les règles relatives aux points d'entrée communautaires figurent dans la [spécification du guide de contribution](./contribution-guide-specification.md)
- Le mécanisme de réponse aux questions figure dans la [spécification de la réponse aux incidents](./incident-response-specification.md)
- Les notes de version publiées figurent dans la [spécification de push et de publication](./push-and-release-specification.md)
- La source de l'étude figure dans le [rapport d'enquête sur les gabarits de README](./readme-template-research-report.md)
