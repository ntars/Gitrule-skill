# Spécification des gabarits d'issue et de PR

> Problème que ce fichier résout : définir la conception des champs, le format et les exigences de rédaction des formulaires structurés `.github/ISSUE_TEMPLATE/*.yml` et de la liste d'auto-vérification `.github/PULL_REQUEST_TEMPLATE.md`, afin que le signalement de problèmes et la soumission de changements disposent de contraintes de saisie exécutables.

## 1. Principes de conception

1. **La structure prime sur le texte libre** : les formulaires d'issue sont définis en YAML et guident la saisie par listes déroulantes, cases à cocher et champs obligatoires, afin de réduire les retours inexploitables.
2. **Minimisation des champs obligatoires** : ne conserver que les champs indispensables à la localisation du problème ; un champ facultatif ne doit pas être marqué comme obligatoire.
3. **Auto-vérification explicite** : le gabarit de PR énumère sous forme de liste des points de contrôle cochables, afin d'éviter que les contributeurs sautent des étapes critiques.
4. **Responsabilité unique** : le formulaire d'issue collecte des informations et ne porte pas la présentation du projet ; le gabarit de PR sert à l'auto-vérification et ne répète pas la description des fonctionnalités (voir la [Matrice documentaire](./document-matrix.md)).

## 2. Structure des formulaires d'issue

### 2.1 Fichiers et nommage

- Le chemin est fixé à `.github/ISSUE_TEMPLATE/*.yml`, un fichier par gabarit.
- Le nom de fichier utilise des minuscules et des traits d'union, par exemple `bug-report.yml`, `feature-request.yml`, `question.yml`.
- Fournir au minimum deux gabarits : « rapport de défaut » et « demande de fonctionnalité ».

### 2.2 Champs standard

| Champ | Type | Obligatoire | Usage |
| --- | --- | --- | --- |
| `name` | chaîne | Oui | Nom d'affichage du gabarit |
| `description` | chaîne | Oui | Description de l'usage du gabarit |
| `title` | préfixe de chaîne | Oui | Préfixe du titre de problème généré automatiquement |
| `labels` | tableau | Non | Étiquettes ajoutées automatiquement |
| `body` | tableau | Oui | Liste des champs du formulaire |

Types de champs courants dans `body` :

| Type | Cas d'usage | Exemple |
| --- | --- | --- |
| `markdown` | Texte explicatif, sans saisie | Consignes de remplissage |
| `textarea` | Description textuelle longue | Étapes de reproduction du problème |
| `input` | Texte court sur une ligne | Numéro de version |
| `dropdown` | Options limitées | Système d'exploitation, niveau de gravité |
| `checkboxes` | Confirmations multiples | Recherche préalable de doublons |

### 2.3 Liste des champs du rapport de défaut

1. Description du problème (`textarea`, obligatoire) : ce qui s'est produit.
2. Comportement attendu (`textarea`, obligatoire) : ce qui aurait dû se produire.
3. Étapes de reproduction (`textarea`, obligatoire) : listées et numérotées, reproductibles de façon autonome.
4. Environnement d'exécution (`input` ou `dropdown`) : système d'exploitation, environnement d'exécution, version du projet.
5. Journaux ou captures d'écran (`textarea`) : fournir les messages d'erreur ; les informations sensibles doivent être expurgées.
6. Confirmation de recherche de doublons (`checkboxes`, obligatoire) : les issues existantes ont été recherchées.

### 2.4 Liste des champs de la demande de fonctionnalité

1. Énoncé du problème (`textarea`, obligatoire) : quelle capacité manque actuellement.
2. Cas d'usage (`textarea`, obligatoire) : qui en a besoin et dans quelles circonstances.
3. Solution attendue (`textarea`) : comment la fonctionnalité devrait être mise en œuvre.
4. Solutions alternatives (`textarea`) : autres approches déjà envisagées.
5. Impact sur la compatibilité (`dropdown`) : présence ou non d'un changement incompatible.

## 3. Structure du gabarit de PR

### 3.1 Blocs indispensables

`PULL_REQUEST_TEMPLATE.md` doit contenir les blocs suivants, dans un ordre fixe :

1. Description du changement : ce que fait cette modification et le numéro d'issue correspondant.
2. Type de changement : à cocher (fonctionnalité, correction, documentation, refactorisation, tests, etc. ; voir la [Spécification des messages de commit](./commit-message-specification.md)).
3. Liste d'auto-vérification : points de contrôle cochables.
4. Changement incompatible : écrire « aucun » en l'absence de changement de ce type ; sinon, indiquer le mode de migration (voir la [Spécification du guide de migration](./migration-guide-specification.md)).
5. Documentation concernée : mise à jour synchronisée du README, du CHANGELOG et de la documentation de l'API.

### 3.2 Exemple de liste d'auto-vérification

```markdown
## Liste d'auto-vérification

- [ ] La compilation locale réussit
- [ ] Les tests concernés réussissent ; les nouvelles fonctionnalités sont couvertes par des tests
- [ ] Le message de commit a été rédigé selon la [Spécification des messages de commit](./commit-message-specification.md)
- [ ] La documentation a été mise à jour ou il a été confirmé qu'aucune mise à jour n'est nécessaire
- [ ] Aucun secret, aucune donnée privée et aucun fichier volumineux n'a été introduit
```

## 4. Gabarits copiables

### 4.1 Formulaire de rapport de défaut

À enregistrer sous `.github/ISSUE_TEMPLATE/bug-report.yml` :

```yaml
name: Rapport de défaut
description: Signaler une anomalie fonctionnelle reproductible
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Veuillez rechercher les issues existantes avant de soumettre, afin d'éviter les doublons.
        Ne collez ni secret, ni jeton, ni information personnelle privée.
  - type: checkboxes
    id: duplicate-check
    attributes:
      label: Recherche de doublons
      options:
        - label: J'ai recherché les issues existantes et confirmé qu'il ne s'agit pas d'un doublon
          required: true
  - type: textarea
    id: description
    attributes:
      label: Description du problème
      description: Ce qui s'est réellement produit
      placeholder: Après l'exécution de la commande install, le code de sortie du programme est 1
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Comportement attendu
      description: Ce qui aurait dû se produire
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Étapes de reproduction
      description: Listez et numérotez afin que d'autres puissent reproduire de façon autonome
      placeholder: |
        1. Exécuter la commande
        2. Observer la sortie
        3. Une anomalie apparaît
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Version du projet
      placeholder: v1.0.0
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: Système d'exploitation
      options:
        - macOS
        - Linux
        - Windows
        - Autre
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Journaux ou captures d'écran
      description: Fournir les messages d'erreur ; les informations sensibles doivent être expurgées
      render: shell
  - type: checkboxes
    id: security
    attributes:
      label: Confirmation de sécurité de l'information
      options:
        - label: Confirmation obtenue : aucun secret, jeton ni donnée personnelle n'est inclus
          required: true
```

### 4.2 Formulaire de demande de fonctionnalité

À enregistrer sous `.github/ISSUE_TEMPLATE/feature-request.yml` :

```yaml
name: Demande de fonctionnalité
description: Proposer une nouvelle capacité ou une suggestion d'amélioration
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Énoncé du problème
      description: Quelle capacité manque actuellement
    validations:
      required: true
  - type: textarea
    id: scenario
    attributes:
      label: Cas d'usage
      description: Qui a besoin de cette capacité et dans quelles circonstances
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Solution attendue
      description: Comment la mise en œuvre est souhaitée
  - type: textarea
    id: alternatives
    attributes:
      label: Solutions alternatives
      description: Autres approches déjà envisagées
  - type: dropdown
    id: breaking
    attributes:
      label: Présence d'un changement incompatible
      options:
        - Non
        - Oui
        - Incertain
    validations:
      required: true
```

### 4.3 Gabarit de PR

À enregistrer sous `.github/PULL_REQUEST_TEMPLATE.md` :

````markdown
## Description du changement

{{变更说明}}

## Type de changement

- [ ] Fonctionnalité (feat)
- [ ] Correction (fix)
- [ ] Documentation (docs)
- [ ] Format (style)
- [ ] Refactorisation (refactor)
- [ ] Tests (test)
- [ ] Compilation ou chaîne d'outils (build / ci)

## Liste d'auto-vérification

- [ ] La compilation locale réussit
- [ ] Les tests concernés réussissent ; les nouvelles fonctionnalités sont couvertes par des tests
- [ ] Le message de commit a été rédigé selon la spécification des messages de commit
- [ ] La documentation a été mise à jour ou il a été confirmé qu'aucune mise à jour n'est nécessaire
- [ ] Aucun secret, aucune donnée privée et aucun fichier volumineux n'a été introduit

## Changement incompatible

{{破坏性变更说明}}

## Documentation concernée

- [ ] README synchronisé ou aucune mise à jour nécessaire
- [ ] CHANGELOG enregistré
- [ ] Documentation de l'API synchronisée ou aucune mise à jour nécessaire
````

### 4.4 Tableau de correspondance des espaces réservés

| Espace réservé | Obligatoire | Points de saisie |
| --- | --- | --- |
| `{{变更说明}}` | Oui | Énoncer en une phrase le contenu de la modification et joindre le numéro d'issue sous la forme `#nombre` |
| `{{破坏性变更说明}}` | Oui | Écrire « aucun » en l'absence de changement incompatible ; sinon, indiquer les étapes de migration et faire un lien vers le guide de migration |

Les champs `name`, `description`, `title` et `labels` des formulaires YAML sont des métadonnées du gabarit, à remplacer selon la situation réelle du projet ; les types de champs et les valeurs `required` du `body` sont ajustés selon les listes de champs des sections 2 et 3, sans réduction des champs obligatoires.

### 4.5 Exemple de remplissage complet

Exemple de remplissage d'un rapport de défaut :

````markdown
## Description du problème

Après l'exécution de `npm run build`, le processus se termine avec le code de sortie 1.

## Comportement attendu

La compilation réussit et produit le répertoire `dist/`.

## Étapes de reproduction

1. Récupérer l'étiquette v1.0.0
2. Exécuter `npm ci`
3. Exécuter `npm run build` et observer le code de sortie 1

## Version du projet

v1.0.0

## Système d'exploitation

macOS

## Journaux ou captures d'écran

```
Error: Cannot find module 'mdlint-core'
```

## Confirmation de sécurité de l'information

- [x] Confirmation obtenue : aucun secret, jeton ni donnée personnelle n'est inclus
````

## 5. Exigences de rédaction

1. Les descriptions de champs utilisent l'impératif ou l'indicatif, sans tournure familière.
2. Chaque champ obligatoire est accompagné d'un exemple de saisie ou d'une exigence de format.
3. Le texte d'aide doit expliquer « pourquoi cette information est nécessaire », en évitant les demandes vagues.
4. Les champs concernant la vie privée doivent rappeler l'exigence d'expurgation (voir la [Spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)).
5. Les gabarits évoluent avec le projet ; les champs obsolètes doivent être supprimés et non s'accumuler durablement.

## 6. Pratiques interdites

1. Interdiction de fusionner tous les types de problèmes dans un unique gabarit en texte libre.
2. Interdiction de définir des champs obligatoires sans rapport avec la localisation du problème.
3. Interdiction d'insérer dans les gabarits une présentation du projet ou du contenu marketing.
4. Interdiction que le gabarit de PR omette la liste d'auto-vérification et la déclaration de changement incompatible.

## Fichiers associés

- Périmètre de responsabilité des fichiers : voir la [Matrice documentaire](./document-matrix.md)
- Processus de contribution : voir la [Spécification du guide de contribution](./contribution-guide-specification.md)
- Normes de revue : voir la [Spécification de la revue de code](./code-review-specification.md)
- Migration des changements incompatibles : voir la [Spécification du guide de migration](./migration-guide-specification.md)
- Le contrôle de gouvernance communautaire relève de la dimension D14, voir la [Matrice des dimensions d'audit](./review-dimension-matrix.md)
