# Spécification de conception d'API

> Problème que ce fichier résout : définir les principes de cohérence et les conventions de conception des interfaces, afin de garantir des API faciles à utiliser, prévisibles et évolutives.

## 1. Principes de conception

1. Cohérence du nommage : les ressources et opérations de même nature utilisent des règles de nommage unifiées.
2. Prévisibilité : des opérations de sémantique identique ont une structure identique.
3. L'explicite prime sur l'implicite : les valeurs par défaut, les champs obligatoires et le comportement en cas d'erreur doivent être explicites.
4. Compatibilité ascendante : les changements privilégient la compatibilité ; les changements incompatibles doivent être versionnés (voir la [spécification de gestion des versions](./version-management-specification.md)).

## 2. Conventions obligatoires

1. **Nommage** : règles de nommage des ressources, des méthodes et des champs.
2. **Paramètres** : type, caractère obligatoire, valeur par défaut, plage de valeurs.
3. **Erreurs** : structure d'erreur unifiée, codes d'erreur, statut HTTP ou mécanisme équivalent.
4. **Pagination et filtrage** : conventions de pagination, de tri et de filtrage pour les scénarios à fort volume de données.
5. **Idempotence** : garantie d'idempotence des opérations d'écriture.
6. **Limitation de débit et quotas** : limitation de fréquence et réponse en cas de dépassement.
7. **Version** : stratégie de version d'API et mode d'évolution.

## 3. Règles impératives

1. La réponse d'erreur doit contenir un code d'erreur localisable et une explication, sans exposer de détails d'implémentation interne.
2. Tout changement incompatible doit entraîner une montée de version et prévoir une période de migration (voir la [spécification du journal des modifications](./changelog-specification.md)).
3. Chaque interface doit disposer d'une documentation correspondante, avec des champs complets (voir la [spécification de documentation d'API](./api-documentation-specification.md)).

## Fichiers associés

- Rédaction de la documentation de référence d'API : [spécification de documentation d'API](./api-documentation-specification.md)
- Aspects de sécurité : [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)
- Le traitement des erreurs relève des arbitrages d'ingénierie : [guide de rédaction des fonctionnalités et arbitrages d'ingénierie](./features-and-engineering-tradeoffs-guide.md)
