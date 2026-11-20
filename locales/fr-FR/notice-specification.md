# Spécification NOTICE

> Problème que ce fichier résout : définir les sept parties que le fichier NOTICE doit contenir ainsi que les exigences de cohérence avec le README, afin de garantir que les déclarations de tiers constituent un fichier distinct et que les informations sont exactes.

## 1. Fichier distinct

NOTICE constitue un fichier distinct ; il ne doit pas être fusionné avec le README, ni remplacé par une liste dans le README. Il doit contenir les parties suivantes :

1. **Déclaration du projet lui-même** : nom du projet, titulaire des droits, année, licence, identifiant SPDX.
2. **Inventaire des composants tiers** : énumération élément par élément selon les champs de l'inventaire des dépendances de la [spécification de conformité open source](./open-source-compliance-specification.md).
3. **Annexe du texte intégral des licences** : lorsque la licence exige la reproduction du texte intégral, joindre le texte original de chaque licence ; le texte original reste en anglais et n'est pas traduit.
4. **Déclaration de modification** : emplacement et contenu des modifications apportées au code tiers.
5. **Déclaration de provenance des ressources et des données**.
6. **Clause de non-responsabilité** : conserver le texte original en anglais, une traduction en chinois pouvant être jointe en regard.
7. **Points à confirmer** : les éléments dont la licence ou la propriété des droits ne peut être vérifiée doivent porter explicitement la mention « à confirmer ».

## 2. Exigences de cohérence

Les informations relatives aux composants et aux licences figurant dans NOTICE et aux chapitres 6 (pile technique et inventaire des dépendances), 19 (copyright et licence) et 20 (déclaration de conformité NOTICE) du README doivent être parfaitement identiques ; aucune divergence ne doit apparaître dans les versions, les identifiants de licence ou les titulaires des droits.

## 3. Mode de déclaration des licences par couches

Lorsque le projet adopte des licences par couches, la « déclaration du projet lui-même » de la section 1 doit être scindée par couche et ne doit pas se limiter à la licence principale.

1. Chaque couche occupe une ligne indiquant : la portée d'application (par exemple « le code source sous `cli/` et `mcp/` »), le nom de la licence, l'identifiant SPDX et l'emplacement du texte intégral.
2. L'expression SPDX résultant de la réunion des couches doit être identique mot pour mot au chapitre 19 du README ; on ne doit pas lire `MIT AND CC-BY-4.0` d'un côté et seulement `MIT` de l'autre.
3. Indiquez en une phrase le fondement du découpage, par exemple « les besoins de réutilisation diffèrent entre le code et la documentation », afin que les mainteneurs suivants puissent rattacher un fichier à sa couche.
4. Si du contenu ne peut être rattaché à aucune couche, listez son chemin dans les « points à confirmer » ; ne l'imputez pas par défaut à la licence principale.
5. La clause de non-responsabilité doit être formulée de manière identique au chapitre 19 du README et dans `LICENSING.md` s'il existe, en précisant que le choix de licence et la répartition en couches sont confirmés par le porteur du projet et que les outils et modèles ne constituent pas un avis juridique.

## Fichiers associés

- Les champs de l'inventaire des dépendances et la méthode de collecte sont décrits dans la [spécification de conformité open source](./open-source-compliance-specification.md)
- Les exigences relatives au texte intégral des licences sont décrites dans la [spécification LICENSE](./license-specification.md)
- Les chapitres concernés du README sont décrits dans la [spécification des sections du README](./readme-sections-specification.md)
- La cohérence relève des portes G7–G9, voir la [porte qualité](./quality-gate.md)
