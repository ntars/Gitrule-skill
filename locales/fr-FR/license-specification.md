# Spécification LICENSE

> Problème que ce fichier résout : définir l'annotation SPDX de la licence d'un projet, les exigences relatives au texte intégral du fichier LICENSE, l'emplacement de la ligne de copyright, le mécanisme de détection de GitHub, la disposition des fichiers en cas de licences par couches ainsi que le processus de confirmation, et la règle interdisant toute inscription sans confirmation.

## 1. Règles de base

1. La licence du projet doit être explicitement indiquée dans le README au moyen de l'identifiant SPDX, et le fichier LICENSE correspondant doit être fourni.
2. Le fichier LICENSE doit contenir le texte intégral officiel en anglais de cette licence ; les clauses ne doivent être ni supprimées ni modifiées. Reformuler, réordonner les paragraphes ou remettre en forme en Markdown fait échouer la détection automatique.
3. La ligne de copyright est placée en tête de fichier ou au chapitre 19 du README, au format décrit dans la [spécification des sections du README](./readme-sections-specification.md).

## 2. Mécanisme de détection de GitHub

GitHub détermine la licence d'un dépôt à l'aide de l'outil open source licensee. Le résultat conditionne le badge de la page du dépôt, le champ `license` de l'API, et le fait qu'une recherche par mot-clé `license` aboutisse ou non. Les règles sont les suivantes :

1. Seuls deux emplacements sont analysés : la racine du projet et un répertoire `LICENSES/` de premier niveau. Les fichiers de même nom situés dans `locales/`, `docs/` ou d'autres sous-répertoires ne participent pas à la détermination.
2. À la racine, les fichiers sont notés selon leur nom, la note la plus haute l'emportant : `LICENSE` vaut 1.00, `LICENSE.md` 0.95, `COPYING` 0.90, les formes suffixées telles que `LICENSE-MIT` 0.70.
3. Dans un répertoire `LICENSES/` de premier niveau, un nom de fichier au format identifiant SPDX avec une extension `.txt`, `.md`, `.markdown` ou `.html` vaut 1.00 ; tout le reste vaut 0.00.
4. Le contenu doit correspondre étroitement au texte intégral officiel de la licence. Un fichier ne contenant qu'une mention du type « ce projet utilise la licence X » ne sera pas détecté, et le résultat qu'il produirait serait une valeur non standard.
5. Lorsque plusieurs licences distinctes sont détectées, le résultat au niveau du projet peut ne pas renvoyer de licence précise, et la page du dépôt affiche `View license` ou `Other`.
6. Les déclarations en langage naturel du README ne participent pas. Écrire « ce projet est sous licence MIT » ne le fait pas détecter comme MIT.

Par conséquent : **la déclaration du README et le fichier LICENSE sont deux mécanismes indépendants, et les deux sont nécessaires.** De plus, lorsque plusieurs fichiers de licence existent à la racine, celui qui sera finalement signalé dépend à la fois de la note du nom de fichier et de la correspondance du contenu, et n'est pas prévisible ; en pratique, les dépôts sous double licence n'ont signalé qu'une seule des deux.

## 3. Disposition des fichiers en cas de licences par couches

Les licences par couches signifient que différentes parties d'un dépôt relèvent de licences différentes, par exemple le code sous MIT et la documentation sous CC BY 4.0. La disposition se décide dans cet ordre :

| Option | Ce qui va à la racine | Résultat de la détection | Condition d'emploi |
| --- | --- | --- | --- |
| Couche unique (par défaut) | Un seul `LICENSE` | Détection stable de cette licence | Toutes les couches relèvent de la même licence, ou l'écart ne change pas les obligations des utilisateurs |
| Couches avec explication | `LICENSE` porte la licence principale, plus un `LICENSING.md` | Détection stable de la licence du `LICENSE` racine | Le découpage en couches est nécessaire et le badge doit rester explicite |
| Couches avec REUSE | `LICENSES/` de premier niveau contient chaque texte intégral | Peut dégénérer en valeur non standard | Uniquement si l'aval exige explicitement la conformité REUSE |

Compromis :

1. Ne placez pas plusieurs fichiers de licence à la racine. En pratique, chaque dépôt sous double licence n'a signalé qu'une seule de ses deux licences ; l'autre est restée invisible sur la page du dépôt et dans l'API, ce qui équivaut à ne déclarer publiquement qu'une seule licence.
2. La disposition REUSE entre en conflit avec la clarté du badge : plusieurs licences dans `LICENSES/` sont lues comme plusieurs licences, ce qui achète un `reuse lint` au vert au prix d'un résultat de détection ambigu. Les deux ne peuvent être pleinement satisfaits en même temps ; le projet doit choisir.
3. Avec l'option « couches avec explication », le nom de fichier `LICENSING.md` ne correspond ni au motif `LICENSE` ni au motif `COPYING`, il n'est donc pas pris pour un fichier de licence et n'affecte pas la détection du `LICENSE` racine.
4. Quelle que soit la disposition retenue, le chapitre 19 du README doit indiquer l'expression SPDX (par exemple `MIT AND CC-BY-4.0`) et la portée de chaque couche. C'est le seul endroit où l'information survit au niveau de la lecture humaine.

## 4. Décision de découpage et processus de confirmation

Les licences par couches ont une portée juridique. Avant toute rédaction ou optimisation, confirmez tour à tour ; n'inventez rien.

1. N'introduisez pas de découpage de votre propre initiative. Lorsque l'utilisateur ne l'a pas explicitement demandé, traitez le projet comme monocouche et indiquez dans le rapport : « Si un découpage est nécessaire, les options candidates et leurs différences sont les suivantes. »
2. Toute proposition de découpage doit en exposer les fondements : ce que chaque couche couvre réellement, les licences candidates et la différence de leurs obligations, l'effet sur les utilisateurs en aval, et la manière dont le résultat de la détection changerait.
3. Confirmez au moins deux fois avant d'écrire : d'abord la combinaison (quelle licence pour quelle couche), ensuite la disposition des fichiers (quelle licence dans le fichier racine, faut-il créer `LICENSES/`).
4. Confirmez de nouveau avant de pousser. Une fois les fichiers générés, indiquez explicitement « Les fichiers ont été générés ; veuillez les vérifier et les valider vous-même » et ne validez ni ne poussez jamais à la place de l'utilisateur.
5. Les options non confirmées ne vont que dans un rapport ou un fichier temporaire ; elles ne doivent pas être écrites en tant que `LICENSE`, `LICENSES/` ou `LICENSING.md`.
6. Lorsqu'une partie ne peut être rattachée à aucune couche, marquez « [à confirmer : rattachement de couche] » et listez les fichiers concernés ; ne classez pas par défaut.

## 5. Exigences relatives à la clause de non-responsabilité

Les textes de licence ont force juridique. Les modèles et les outils ne fournissent que des règles de décision et une disposition de fichiers, et ne constituent pas un avis juridique.

1. Le chapitre 19 du README ou le fichier `LICENSING.md` doit contenir une clause de non-responsabilité précisant que le choix de licence est confirmé par le porteur du projet.
2. La clause de non-responsabilité doit correspondre à celle du NOTICE ; elle ne doit pas exister d'un côté et manquer de l'autre.
3. N'affirmez pas que « l'examen de conformité est terminé ». Indiquez seulement que « la disposition des fichiers et les annotations SPDX ont été vérifiées selon les règles quant à leur complétude ».
4. L'effet juridique des licences par couches suit le texte intégral de chaque licence. Le texte descriptif du dépôt n'est qu'un index et ne modifie pas les clauses.

## Fichiers associés

- L'absence de LICENSE bloque le push et relève de la règle absolue H2, voir les [règles absolues](./hard-rules.md)
- L'appréciation de la compatibilité des licences des dépendances est décrite dans la [spécification de conformité open source](./open-source-compliance-specification.md)
- Les déclarations de tiers font l'objet d'un fichier distinct, voir la [spécification NOTICE](./notice-specification.md)
- L'exactitude de la licence relève des portes G7/G8, voir la [porte qualité](./quality-gate.md)
