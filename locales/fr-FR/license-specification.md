# Spécification LICENSE

> Problème que ce fichier résout : définir l'annotation SPDX de la licence d'un projet, les exigences relatives au texte intégral du fichier LICENSE, l'emplacement de la ligne de copyright et les indications de licences multiples, ainsi que la règle interdisant toute inscription sans confirmation.

## Règles relatives à LICENSE

1. La licence du projet doit être explicitement indiquée dans le README au moyen de l'identifiant SPDX, et le fichier LICENSE correspondant doit être fourni.
2. Le fichier LICENSE doit contenir le texte intégral officiel en anglais de cette licence ; les clauses ne doivent pas être supprimées ni modifiées.
3. La ligne de copyright est placée en tête de fichier ou au chapitre 19 du README, au format décrit dans la [spécification des sections du README](./readme-sections-specification.md).
4. En cas de double licence ou de licences multiples, les conditions d'application et le mode de choix doivent être précisés.
5. Tant que le choix de licence n'a pas été confirmé par l'utilisateur, il ne doit pas être directement inscrit dans la documentation ; seules des solutions candidates et une description de leurs différences peuvent être proposées.

## Fichiers associés

- L'absence de LICENSE bloque le push et relève de la règle absolue H2, voir les [règles absolues](./hard-rules.md)
- L'appréciation de la compatibilité des licences des dépendances est décrite dans la [spécification de conformité open source](./open-source-compliance-specification.md)
- Les déclarations de tiers font l'objet d'un fichier distinct, voir la [spécification NOTICE](./notice-specification.md)
- L'exactitude de la licence relève des portes G7/G8, voir la [porte qualité](./quality-gate.md)
