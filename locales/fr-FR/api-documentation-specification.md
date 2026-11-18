# Spécification de documentation d'API

> Problème que ce fichier résout : définir la structure et les champs d'une documentation de référence d'API complète, comme base de rédaction de docs/api.md, en la séparant strictement des contenus de type tutoriel.

## 1. Structure obligatoire

Chaque entrée d'API doit contenir :

| Champ | Exigence |
| --- | --- |
| Signature de l'interface | Méthode, chemin ou prototype de fonction, complet et copiable |
| Paramètres | Nom, type, caractère obligatoire, valeur par défaut, plage de valeurs, description |
| Valeur de retour | Type et description de la structure |
| Codes d'erreur | Code d'erreur, condition de déclenchement, mode de traitement |
| Exemple d'appel | Exemple minimal exécutable, avec le langage indiqué |
| Limitation de débit et quotas | Limitation de fréquence d'appel, quotas, traitement du dépassement |

## 2. Règles impératives

1. Les paramètres et les valeurs de retour doivent préciser leur type et leurs contraintes ; les valeurs par défaut ne doivent pas être omises.
2. Les codes d'erreur doivent être listés de façon complète ; la simple mention « une erreur peut survenir » est interdite.
3. Les blocs de code doivent indiquer l'identifiant de langage, et les exemples doivent être exécutables de façon autonome.
4. Ce fichier ne contient que des informations de référence, sans tutoriel, contexte ni explication de conception (tutoriels et contexte : voir la [spécification des sections du README](./readme-sections-specification.md)).

## 3. Exigences de cohérence

Les signatures d'interface de la documentation d'API doivent être cohérentes avec l'implémentation réelle du code ; le nommage des paramètres doit être conforme aux exigences de précision de la [spécification de rédaction générale](./general-writing-specification.md) ; pour la terminologie, voir le [glossaire](./glossary.md).

## Fichiers associés

- Périmètre de responsabilité de la documentation : [matrice documentaire](./document-matrix.md)
- Spécification de conception d'API (comment concevoir les interfaces) : [spécification de conception d'API](./api-design-specification.md)
- La qualité de la documentation relève de la dimension D12 : [matrice des dimensions de revue](./review-dimension-matrix.md)
