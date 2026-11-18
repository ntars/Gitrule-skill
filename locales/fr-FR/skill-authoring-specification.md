# Spécification de rédaction des Skills

> Problème que ce fichier résout : définir la structure, les conditions de déclenchement et le mode de chargement progressif à respecter lors de l'encapsulation d'un ensemble de spécifications sous forme de Skill, afin de garantir un Skill découvrable, maintenable et sans duplication de contenu.

## 1. Structure des répertoires

Un Skill adopte la structure « point d'entrée + ressources à la demande » :

```text
skill-name/
├── SKILL.md          obligatoire : métadonnées + processus principal
├── references/       corps des spécifications, chargé à la demande
└── assets/           gabarits et ressources (facultatif)
```

## 2. Exigences relatives à SKILL.md

1. Les métadonnées contiennent `name` et `description` ; la description doit préciser « ce qui est fait + quand l'utiliser » afin de faciliter le déclenchement.
2. Le corps du document ne conserve que les règles et processus principaux résidents ; les contenus détaillés de type tables de référence sont placés dans `references/`.
3. Employer l'impératif ou l'infinitif et éviter la deuxième personne.
4. Lorsqu'une ressource est citée, indiquer le chemin explicite et la condition « quand la lire ».

## 3. Règles impératives

1. Le corps des spécifications n'est maintenu qu'à un seul endroit : le Skill référence les fichiers du présent ensemble de spécifications sans en recopier le texte intégral, afin d'éviter une double dérive.
2. Un Skill ne fait qu'une seule chose ; empiler plusieurs responsabilités dans un même Skill est interdit.
3. Les conditions de déclenchement doivent citer des formulations concrètes, afin d'éviter un déclenchement trop large.
4. La version est mise à jour en synchronisation avec la version de l'ensemble de spécifications.

## Fichiers associés

- La structure de la liste des métadonnées est décrite dans la [spécification des métadonnées lisibles par machine](./machine-readable-metadata-specification.md)
- La responsabilité unique des documents est décrite dans la [matrice documentaire](./document-matrix.md)
- Les conventions d'invocation des agents sont décrites dans la [spécification d'invocation des agents et de rédaction des prompts](./agent-invocation-and-prompt-specification.md)
