# Spécification de conception de bases de données

> Problème que ce fichier résout : définir les règles de conception des schémas de tables, des champs, des index et des migrations, afin de garantir la cohérence, l'évolutivité et la traçabilité des données.

## 1. Conventions de nommage

1. Les noms de tables et de champs utilisent un style de nommage unifié et une signification explicite.
2. Les clés primaires, les clés étrangères et les index suivent une règle de préfixe unifiée.
3. Les mots réservés et les abréviations doivent faire l'objet de conventions explicites, afin d'éviter toute ambiguïté.

## 2. Conception des champs

1. Chaque champ doit préciser son type, sa nullabilité, sa valeur par défaut et sa signification.
2. Les champs temporels utilisent un fuseau horaire et une précision unifiés.
3. Les champs sensibles à la précision, tels que les montants, utilisent un type décimal à virgule fixe, et non un type à virgule flottante.
4. Les champs d'état utilisent une énumération explicite, avec la signification des valeurs indiquée.

## 3. Index et contraintes

1. Les index sont conçus en fonction des scénarios de requête, afin d'éviter la sur-indexation.
2. L'intégrité est garantie par des contraintes, et non par une validation au niveau applicatif.
3. Les clés étrangères et les règles de cascade doivent être déclarées explicitement.

## 4. Gestion des migrations

1. Les changements de structure sont gérés par des scripts de migration, lesquels sont versionnés et commités dans le dépôt.
2. Les migrations doivent être réversibles ; les changements destructifs doivent être accompagnés d'un plan de migration des données.
3. Les scripts de migration doivent être validés en environnement de test avant d'être appliqués en production (voir la [spécification de déploiement et de restauration](./deployment-and-rollback-specification.md)).

## 5. Sécurité

1. Les données sensibles doivent être stockées chiffrées ou pseudonymisées (voir la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)).
2. Les chaînes de connexion à la base de données ne doivent pas être commitées dans le dépôt (règle absolue H3).

## Fichiers associés

- Lignes rouges sur les informations sensibles : [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)
- Gestion des changements : [spécification de déploiement et de restauration](./deployment-and-rollback-specification.md)
- Position dans l'architecture : [spécification des documents de conception d'architecture](./architecture-design-document-specification.md)
