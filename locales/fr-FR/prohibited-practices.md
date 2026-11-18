# Pratiques interdites

> Problème que ce fichier résout : rassembler tous les comportements interdits non négociables, afin de constituer la liste rouge définitive lors des audits et de la rédaction.

## I. Lignes rouges du pilotage et du push

1. Il est interdit de produire un « on peut pousser d'abord, on complétera ensuite » tant que les P0 ne sont pas à zéro.
2. Il est interdit d'inventer des résultats de vérification ; les éléments non vérifiables sont marqués `SKIP + raison` et ne doivent pas être notés PASS.
3. Il est interdit de livrer plusieurs documents fusionnés en un seul fichier.
4. Il est interdit d'entasser dans le README l'API complète, le guide de contribution et le journal des modifications.
5. Il est interdit d'utiliser `--force` pour pousser sur une branche publique, en aucune circonstance.
6. Il est interdit de traiter une clé compromise par un simple « commit de suppression ».
7. Il est interdit d'inventer un nom de dépôt en s'affranchissant de la [spécification de nommage des projets](./project-naming-specification.md).
8. Il est interdit d'inscrire le raisonnement interne dans un document livré.

## II. Lignes rouges de la rédaction documentaire

1. Il ne faut pas inventer de nom de projet, de fonctionnalité, de donnée de performance, de version de dépendance, de licence, d'information sur l'auteur ni de résultat de test.
2. Il ne faut pas copier le README, la documentation, le code, les images ou les textes d'autrui ; en cas de citation nécessaire, la source et la licence doivent être mentionnées.
3. Il ne faut pas choisir un type de licence sans confirmation préalable.
4. Il ne doit apparaître ni chiffre de performance non vérifié, ni conclusion comparative sans source, ni formulation d'engagement (par exemple « garanti », « gratuit à vie »), ni description dénigrante d'un projet tiers, ni contenu promotionnel sans lien avec le projet.
5. Il ne faut pas utiliser de ressources d'origine inconnue ; lorsqu'une image, une icône ou une police n'a pas de source et de licence, elle est marquée à confirmer et ne doit pas être utilisée directement.

## Fichiers associés

- Règles absolues dont la violation bloque toute action : voir les [règles absolues](./hard-rules.md)
- Traitement des incidents (fuite de clé, etc.) : voir la [spécification de push et de publication](./push-and-release-specification.md), section 5
- Contraintes impératives des rôles : voir les [rôles et responsabilités](./roles-and-responsibilities.md)
