# Spécification de conformité open source

> Problème que ce fichier résout : définir le périmètre de collecte de la conformité open source, les champs de la liste des dépendances, la méthode de collecte, l'évaluation de compatibilité des licences, le marquage des modifications et les règles de citation des ressources, afin de garantir des déclarations complètes et vérifiables.

## 1. Périmètre de collecte

Quatre catégories de sources doivent être couvertes : dépendances directes, dépendances indirectes et transitives, chaîne d'outils de build et de développement, ressources (icônes, polices, images, fichiers audio, jeux de données, origine d'algorithmes).

## 2. Champs de la liste des dépendances

| Champ | Exigence |
| --- | --- |
| Nom du composant | Identique au dépôt officiel |
| Version | Version réellement verrouillée, et non expression de plage |
| Mode de référence | Dépendance directe ou dépendance indirecte |
| Titulaire des droits | Nom complet du titulaire du droit d'auteur déclaré officiellement |
| Licence | Identifiant SPDX, en cas de licences multiples le mode de combinaison doit être précisé |
| Adresse officielle | URL complète du dépôt ou de la page d'accueil |
| Usage dans ce projet | Emplacement d'appel ou fonctionnalité précise |
| Modification | Oui ou non |
| Description des modifications | Fichiers modifiés, contenu des modifications, motif ; écrire « aucune » si non modifié |
| Emplacement du texte de licence | Chemin dans le projet ou lien vers le fichier |

Le gabarit de tableau de la liste des dépendances figure dans la [collecte d'informations et gabarits](./information-collection-and-templates.md).

## 3. Méthode de collecte

Utiliser la commande correspondant à la pile technique pour générer l'arbre de dépendances, puis compléter élément par élément les informations de licence et de copyright : `npm ls --all`, `pip freeze`, `go mod graph`, `cargo tree`, `mvn dependency:tree`, `gradle dependencies`, `composer show --tree`. L'analyse des licences peut recourir à des outils tels que `license-checker`, `pip-licenses`, `cargo-license` ; les résultats de l'analyse doivent être vérifiés manuellement, la sortie d'un outil ne pouvant être directement retenue comme conclusion finale.

## 4. Compatibilité des licences

1. La compatibilité entre la licence du projet et la licence de chaque dépendance doit être évaluée, en vérifiant en priorité la portée de contagion des licences GPL, AGPL, LGPL et MPL.
2. Pour les dépendances sous Apache-2.0, il faut confirmer que les exigences relatives au fichier NOTICE sont satisfaites.
3. Les licences de ressources (telles que les polices SIL OFL, la série CC) doivent faire l'objet d'une vérification distincte des exigences d'attribution et de diffusion.
4. Lorsque la compatibilité ne peut être déterminée, marquer « 【à confirmer : compatibilité des licences】 » et préciser le motif du doute.

## 5. Marquage des modifications du code d'autrui

1. Conserver en tête de fichier la mention de copyright et la mention de licence d'origine.
2. Indiquer dans le NOTICE le chemin des fichiers modifiés, un résumé du contenu des modifications et la date de modification.
3. Reporter ces informations dans la section correspondante du README.

## 6. Citations et ressources

1. La citation de documentation ou d'extraits de code d'autrui doit mentionner l'adresse source, l'auteur et la licence.
2. Les images, icônes et polices doivent documenter leur source et leur licence ; en cas d'absence, marquer « à confirmer », sans utilisation directe.
3. L'utilisation de ressources d'origine inconnue est interdite.

## Fichiers associés

- Conversion de la liste des dépendances en NOTICE : voir la [spécification NOTICE](./notice-specification.md)
- Choix de licence et exigences de texte intégral : voir la [spécification LICENSE](./license-specification.md)
- Authenticité des dépendances et des copyrights : portes G6–G9 et G13, voir la [porte qualité](./quality-gate.md)
