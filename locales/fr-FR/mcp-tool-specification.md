# Spécification des outils MCP

> Problème que ce fichier résout : définir les règles de conception et de description des interfaces lors de l'exposition d'un ensemble de spécifications sous forme d'outils via le protocole de contexte de modèle (MCP), afin de garantir que les outils peuvent être correctement découverts et invoqués par le modèle.

## 1. Principes de conception des outils

1. Responsabilité unique : un outil fait une seule chose ; éviter les interfaces fourre-tout.
2. Description claire : la description de l'outil précise son usage et ses cas d'application, afin d'aider le modèle à déterminer quand l'invoquer.
3. Paramètres explicites : chaque paramètre possède un type, un caractère obligatoire ou non, une plage de valeurs et une description.
4. Sortie structurée : renvoyer des données structurées ; éviter les longs textes en prose.

## 2. Champs obligatoires

| Champ | Exigence |
| --- | --- |
| name | identifiant unique, en kebab-case minuscule |
| description | usage et conditions de déclenchement, concrets et évaluables |
| inputSchema | types des paramètres, champs obligatoires, contraintes |
| Valeur de retour | format structuré et description des champs |
| Erreur | format de retour en cas d'échec ; toute invention de résultat est interdite |

## 3. Outils liés à l'ensemble de spécifications

1. Type recherche documentaire : renvoyer le contenu d'une spécification selon le code de langue + l'identifiant (identifiants décrits dans la [spécification des métadonnées lisibles par machine](./machine-readable-metadata-specification.md)).
2. Type inventaire : renvoyer la liste des documents disponibles et leur correspondance linguistique.
3. Type validation : vérifier l'intégrité de la matrice documentaire (voir la [matrice documentaire](./document-matrix.md)) et l'état de la porte qualité (voir la [porte qualité](./quality-gate.md)).

## 4. Règles impératives

1. Un outil ne doit pas renvoyer PASS pour un résultat non vérifiable ; il doit indiquer SKIP et le motif (voir les [pratiques interdites](./prohibited-practices.md)).
2. La sortie doit être analysable par un programme et ne pas contenir de processus de réflexion interne.
3. Les éléments liés à la sécurité ne doivent pas être divulgués via les outils (voir la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)).

## Fichiers associés

- La structure des métadonnées est décrite dans la [spécification des métadonnées lisibles par machine](./machine-readable-metadata-specification.md)
- L'encapsulation des Skills est décrite dans la [spécification de rédaction des Skills](./skill-authoring-specification.md)
- Les conventions d'invocation des agents sont décrites dans la [spécification d'invocation des agents et de rédaction des prompts](./agent-invocation-and-prompt-specification.md)
