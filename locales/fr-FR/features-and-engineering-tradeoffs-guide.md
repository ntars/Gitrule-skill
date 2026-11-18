# Rédaction des fonctionnalités et des arbitrages d'ingénierie

> Problème que ce fichier résout : définir la rédaction des deux chapitres « Fonctionnalités clés » et « Détails de conception et arbitrages d'ingénierie » du README, en fournissant respectivement la structure en cinq parties des fonctionnalités et les dix catégories à couverture obligatoire des arbitrages d'ingénierie.

## 1. Rédaction des fonctionnalités clés

Chaque fonctionnalité est rédigée selon la structure en cinq parties ci-dessous ; l'absence d'une seule partie interdit de la lister comme fonctionnalité.

1. **Nom de la fonctionnalité** : 15 caractères maximum, sous forme de groupe nominal.
2. **Valeur** : le problème concret résolu, ainsi que les conséquences en cas de non-résolution.
3. **Mode de mise en œuvre** : la technologie, le mécanisme ou l'algorithme employé, en indiquant les fichiers ou fonctions clés.
4. **Différenciation** : les dimensions de comparaison avec les solutions courantes, lesquelles doivent être objectivement évaluables.
5. **Preuves** : données de test, résultats de référence, emplacement du code, options de configuration ou étapes reproductibles.

Contraintes :
1. Les preuves doivent être reproductibles ; une fonctionnalité dont les preuves ne peuvent être fournies doit porter la mention « 【à compléter : mode de vérification】 » et ne doit pas être remplacée par une description qualitative.
2. Les preuves de performance doivent préciser l'environnement et la méthode de test.
3. Les objets de comparaison doivent être des solutions nommées ; les désignations vagues du type « solution traditionnelle » ou « autre outil » sont interdites.

## 2. Rédaction des détails de conception et des arbitrages d'ingénierie

Chaque élément est rédigé selon la structure en trois parties « scénario → mode de traitement → raison », en expliquant pourquoi cette conception a été retenue plutôt qu'une autre.

Catégories à couverture obligatoire :
1. Entrées anormales et cas limites (valeurs nulles, longueur excessive, caractères illégaux, valeurs numériques extrêmes)
2. Stratégies de délai d'attente, de nouvelle tentative, de retrait progressif, de disjoncteur et de dégradation
3. Niveaux de cache, stratégies d'invalidation, protection contre la pénétration et l'effondrement du cache
4. Contrôle de concurrence, granularité des verrous, cohérence des données et idempotence
5. Optimisation de la mémoire et du stockage (traitement par lots, lecture/écriture en flux, compression)
6. Mesures de sécurité (authentification, limitation de débit, validation des entrées, masquage des informations sensibles)
7. Détails d'interaction (protection contre les erreurs de manipulation, double confirmation, annulation possible, états de chargement et états vides)
8. Justification des valeurs des paramètres par défaut
9. Stratégies de compatibilité ascendante et d'adaptation multiplateforme
10. Traitement des réseaux faibles et du mode hors ligne, restauration d'état

## Fichiers associés

- Correspond aux chapitres 4 et 5 du README, voir la [spécification des sections du README](./readme-sections-specification.md)
- La rédaction des données de performance doit respecter les exigences d'exactitude, voir la [spécification générale de rédaction](./general-writing-specification.md)
- Les preuves des fonctionnalités et la couverture des arbitrages relèvent des portes G4/G5, voir la [porte qualité](./quality-gate.md)
