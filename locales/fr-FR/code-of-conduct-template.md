# Gabarit de code de conduite

> Problème que ce fichier résout : fournir un gabarit de code de conduite directement copiable, permettant à un projet de générer le fichier CODE_OF_CONDUCT.md en précisant l'engagement de participation, les comportements attendus, les comportements inacceptables, la responsabilité d'application et le canal de signalement ; les consignes de remplissage associées couvrent la provenance de l'adaptation et la déclaration de version.

## 1. Mode d'emploi

1. Copier l'intégralité du contenu de la section 3 « Corps du gabarit » et créer le fichier `CODE_OF_CONDUCT.md` à la racine du projet.
2. Remplacer les espaces réservés conformément à la section 4 ; le canal de signalement doit impérativement être une adresse réellement accessible.
3. En cas d'adoption ou d'adaptation d'un code de conduite disposant d'une version, déclarer la version et la licence selon les exigences de provenance à la section 5, sur la base de la section 1, point 8 de la [spécification du code de conduite](./code-of-conduct-specification.md).
4. Créer un lien vers ce fichier dans le [gabarit de guide de contribution](./contribution-guide-template.md) et dans la section contribution du README, afin de garantir une accessibilité bidirectionnelle.

## 2. Principes de personnalisation

- **Indépendant de la technique** : le code ne contient aucun contenu technique et ne régit que les normes de comportement de participation ; les limites figurent dans la [matrice documentaire](./document-matrix.md).
- **Applicable** : le traitement gradué doit préciser les conditions de déclenchement et les mesures ; il est interdit de n'énoncer que des principes sans mentionner les conséquences.
- **Accessibilité** : le canal de signalement doit être réel et valide ; il est interdit de laisser une adresse d'exemple.
- **Provenance conforme** : l'adaptation d'un code tiers doit conserver ses exigences d'attribution et de licence, voir la [spécification de conformité open source](./open-source-compliance-specification.md).

## 3. Corps du gabarit

```markdown
# Code de conduite

## Notre engagement

En tant que participants, contributeurs et mainteneurs de {{项目名称}}, nous nous engageons à créer ensemble un environnement de participation ouvert, bienveillant et exempt de harcèlement, sans considération d'âge, de morphologie, de situation de handicap, d'origine ethnique, d'identité et d'expression de genre, de niveau d'expérience, de niveau d'études, de statut socio-économique, de nationalité, d'apparence ou d'orientation sexuelle.

## Champ d'application

Le présent code s'applique aux espaces du projet, aux tickets, aux demandes de fusion, aux revues de code, aux canaux sociaux, ainsi qu'aux espaces publics où une personne intervient en tant que représentante du projet.

## Comportements attendus

- Respecter les points de vue et les expériences divergents, communiquer avec bienveillance.
- Accepter les retours constructifs, se concentrer sur le problème lui-même et non sur les personnes.
- Se soucier de l'intérêt collectif de la communauté, éviter de nuire au projet et à ses participants.
- Faire preuve de patience envers les nouveaux arrivants, formuler des suggestions d'amélioration concrètes.

## Comportements inacceptables

- Attaques personnelles, propos insultants ou dénigrants.
- Propos discriminatoires et harcèlement fondés sur une caractéristique protégée.
- Harcèlement public ou privé, traque, contacts insistants sans consentement.
- Publication non autorisée d'informations relevant de la vie privée d'autrui.
- Tout autre comportement raisonnablement considéré comme inapproprié dans un cadre professionnel.

## Responsabilité d'application

Les mainteneurs du projet sont chargés de clarifier l'application du présent code, d'arbitrer les violations et ont le droit de supprimer, modifier ou refuser tout contenu non conforme au présent code. Les mainteneurs doivent exercer leurs fonctions de manière cohérente et impartiale, et se récuser d'eux-mêmes en cas de litige les concernant.

## Mesures d'application

Les violations font l'objet d'un traitement gradué selon leur gravité :

| Niveau | Situation applicable | Mesure |
| --- | --- | --- |
| Premier | Offense involontaire, manquement mineur | Rappel et explication en privé |
| Deuxième | Récidive ou violation caractérisée | Avertissement public, correction dans un délai fixé |
| Troisième | Harcèlement grave, attaque malveillante | Suspension temporaire du droit de participation |
| Quatrième | Comportement grave persistant ou irréparable | Bannissement permanent avec conservation du dossier |

## Canal de signalement

En cas de subissement ou de constatation d'un comportement contraire au présent code, veuillez contacter l'équipe de mainteneurs via {{真实可达的举报邮箱或渠道}}. Tous les signalements seront traités de manière confidentielle ; les mainteneurs ne doivent pas divulguer l'identité de la personne signalante à la personne mise en cause, sauf accord explicite de la personne signalante.

## Attribution et provenance

{{准则来源声明}}
```

## 4. Tableau de correspondance des espaces réservés et définition des champs

| Espace réservé | Obligatoire | Définition du champ | Exemple de saisie |
| --- | --- | --- | --- |
| `{{项目名称}}` | Oui | Nom public du projet, identique à la première ligne du README | `FooBar` |
| `{{真实可达的举报邮箱或渠道}}` | Oui | Adresse réelle permettant de joindre directement les mainteneurs | `conduct@example.com` |
| `{{准则来源声明}}` | Oui | Écrire « original » en cas de création originale ; en cas d'adaptation, indiquer le nom de la source, la version et la licence | `Adapté de Contributor Covenant 2.1 (CC BY 4.0)` |

## 5. Consignes de remplissage et variantes de scénario

| Scénario | Points d'ajustement |
| --- | --- |
| Projet personnel | Indiquer le mainteneur lui-même ; utiliser pour le canal de signalement une adresse électronique conservée à long terme |
| Projet d'entreprise | Identifier clairement le service juridique ou l'équipe communautaire comme entité d'application ; les mesures d'application doivent être cohérentes avec les règles internes |
| Adoption d'un code connu | Conserver son texte intégral original et sa version, en ne complétant que le canal de signalement et l'attribution |
| Projet multilingue | Les clauses de chaque version linguistique doivent se correspondre une à une ; désigner la version anglaise ou chinoise comme version de référence et le préciser |

Tableau des erreurs fréquentes :

| Rédaction erronée | Conséquence | Rédaction correcte |
| --- | --- | --- |
| Se limiter à « les échanges courtois sont les bienvenus » | Aucune base d'application, impossibilité d'arbitrer en cas de litige | Énumérer les comportements attendus, les comportements inacceptables et le traitement gradué |
| Laisser une adresse électronique fictive comme canal de signalement | Inaccessible, mécanisme de signalement inopérant | Saisir une adresse réelle et valable à long terme |
| Adapter un code sans mention d'attribution | Non-respect des exigences de licence de la source | Déclarer la source, la version et la licence |

## 6. Exemple complet

Voici un extrait d'un scénario d'adaptation, fourni à titre de référence de format uniquement.

```markdown
## Canal de signalement

En cas de subissement ou de constatation d'un comportement contraire au présent code, veuillez contacter l'équipe de mainteneurs via conduct@example.com. Tous les signalements seront traités de manière confidentielle.

## Attribution et provenance

Le présent code est adapté de Contributor Covenant 2.1, sous licence CC BY 4.0.
```

## Fichiers associés

- Spécification correspondante : [spécification du code de conduite](./code-of-conduct-specification.md)
- Gabarits complémentaires : [gabarit de guide de contribution](./contribution-guide-template.md), [gabarit SECURITY](./security-template.md)
- Dimension de gouvernance communautaire : [matrice des dimensions de revue](./review-dimension-matrix.md)
- Retour à l'index en chinois simplifié : [README](./README.md)
