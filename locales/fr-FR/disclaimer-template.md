# Gabarit de clause de non-responsabilité

> Problème que ce fichier résout : fournir un gabarit générique de clause de non-responsabilité, directement copiable et applicable par simple remplacement des espaces réservés, afin que tout projet puisse délimiter à moindre coût la nature de son contenu, les limites de sa responsabilité et les obligations de l'utilisateur ; les consignes de remplissage et les variantes de scénario associées couvrent les projets personnels, d'entreprise, open source et propriétaires.

## 1. Mode d'emploi

1. Copier l'intégralité du contenu de la section 3 « Corps du gabarit » et créer le fichier `DISCLAIMER.md` à la racine du projet, ou l'intégrer comme section autonome de `README.md`.
2. Remplacer un à un les `{{...}}` conformément au tableau de correspondance des espaces réservés de la section 4 ; toute section non utilisée doit être supprimée, sans laisser d'espace réservé vide.
3. Adapter les clauses selon les variantes de scénario de la section 5 : les logiciels propriétaires privilégient la section 3.5, les projets open source doivent conserver la section 3.6 relative à l'articulation avec la licence.
4. Le présent gabarit est un texte de référence générique et ne constitue pas un avis juridique. En cas de publication officielle, de diffusion transfrontalière ou de secteur réglementé, il doit être validé par le service juridique avant utilisation ; la base figure à la section 2 de la [clause de non-responsabilité](./disclaimer.md).
5. Vérifier avant soumission : tous les espaces réservés sont remplacés, les coordonnées sont réellement accessibles et aucun conflit n'existe avec les clauses de [LICENSE](../../LICENSE).

## 2. Principes de personnalisation

- **Primauté de la légalité** : toutes les clauses de non-responsabilité ne prennent effet que dans les limites permises par le droit applicable ; il est interdit d'employer des formulations absolues telles que « exemption inconditionnelle de toute responsabilité », afin d'éviter l'invalidité de la clause entière.
- **Sans empiétement** : il ne doit pas être porté atteinte aux droits concédés par la licence, ni les réduire ; en cas de conflit, le texte de la licence prévaut, selon le principe de la [spécification LICENSE](./license-specification.md).
- **Vérifiable** : les coordonnées, la date d'entrée en vigueur et la dénomination de l'entité doivent être des informations réelles ; il est interdit de conserver des valeurs d'exemple.
- **Indépendance** : chaque clause est indépendante ; la nullité d'une seule clause n'affecte pas la validité des autres.

## 3. Corps du gabarit

Le contenu ci-dessous constitue le corps du gabarit à partir de la section 3.1 et peut être copié directement.

### 3.1 Objet et champ d'application de la déclaration

```markdown
# Clause de non-responsabilité

> La présente déclaration s'applique à l'ensemble des contenus publiés par {{项目名称}} (ci-après « le présent projet »), y compris le code source, la documentation, les gabarits, les exemples, les données et les ressources associées (ci-après collectivement « les contenus du projet »), qu'ils soient utilisés par lecture humaine, par appel programmatique ou par tout autre moyen.

1. La présente déclaration vise à clarifier la nature des contenus du projet, à signaler les risques d'utilisation et à préciser les limites de responsabilité ; elle ne constitue pas une restriction supplémentaire aux droits de quiconque, ni une révocation ou une réduction des droits concédés par la licence du projet.
2. Toute entité qui accède, copie, cite, adapte, diffuse ou utilise tout ou partie des contenus du projet (ci-après « l'utilisateur ») est réputée avoir lu et compris la présente déclaration.
3. La date de dernière mise à jour de la présente déclaration est le {{更新日期}}.
```

### 3.2 Nature du contenu

```markdown
## Nature du contenu

1. Les contenus du projet constituent {{内容性质描述}} et ne représentent pas une norme officielle, un avis juridique ou une conclusion de conseil professionnel d'une quelconque organisation, branche d'activité ou juridiction.
2. Les contenus du projet ne fournissent aucune garantie d'adéquation à une pile technique, un environnement d'exécution ou une exigence de conformité particuliers, et ne constituent pas un avis professionnel en matière juridique, de conformité, de sécurité, financière ou fiscale ; pour ces questions, l'utilisateur doit consulter lui-même des professionnels dûment qualifiés.
3. Les exemples, paramètres et informations statistiques figurant dans les contenus du projet ne servent qu'à illustrer une méthode ou à démontrer une écriture et ne doivent pas être repris directement comme valeurs recommandées en environnement de production ; leur validité est appréciée au regard de {{数据或示例的时点与范围说明}}.
```

### 3.3 Absence de garantie

```markdown
## Absence de garantie

Dans toute la mesure permise par la loi, les contenus du projet sont fournis « en l'état », et {{主体名称}} n'accorde aucune garantie expresse ou implicite, y compris notamment :

- l'exactitude absolue, l'exhaustivité, l'absence d'erreur ou d'omission du contenu ;
- l'adéquation du contenu à un usage particulier, à un environnement particulier ou à une exigence de conformité particulière de l'utilisateur ;
- l'obtention nécessaire des résultats escomptés par la mise en œuvre des contenus du projet, ou le passage nécessaire de tout processus d'audit, de test, de publication ou de certification ;
- la disponibilité continue des contenus du projet, leur absence de modification, ou leur compatibilité avec les outils, plateformes et services tiers que l'utilisateur adopterait ultérieurement ;
- l'absence d'atteinte aux droits de tout tiers par les contenus du projet.
```

### 3.4 Responsabilité de l'utilisateur

```markdown
## Responsabilité de l'utilisateur

1. Avant d'adopter les contenus du projet, l'utilisateur doit évaluer de manière indépendante leur adéquation au regard du type de son propre projet, du droit applicable, des exigences sectorielles et de sa capacité de prise de risque, et décider lui-même s'il les adopte, quelles parties il adopte et comment il les ajuste.
2. Avant utilisation, l'utilisateur doit vérifier les gabarits, configurations, extraits de scripts et paramètres, y compris la validation syntaxique, la vérification du build, la validation par les tests et la revue de sécurité ; il ne doit pas les appliquer directement, sans vérification, à un environnement de production, à un service externe ou à un scénario impliquant des données sensibles.
3. Lorsque l'utilisateur adapte, retire, fusionne ou republie les contenus du projet, il doit vérifier lui-même la cohérence du résultat avec ses propres besoins et les clauses applicables, et assumer la responsabilité de la documentation, des configurations et des livrables ainsi produits.
4. L'utilisateur doit respecter le droit applicable et les règles internes de sa juridiction ainsi que du secteur d'activité du projet ; les contenus du projet ne se substituent pas à l'exécution des obligations correspondantes.
```

### 3.5 Limitation de responsabilité

```markdown
## Limitation de responsabilité

1. Dans toute la mesure permise par la loi, {{主体名称}} n'assume aucune responsabilité pour toute perte, tout dommage, toute responsabilité, tout frais ou toute dépense découlant ou prétendument découlant des situations suivantes, que ce soit sur un fondement contractuel, délictuel (y compris la négligence) ou tout autre fondement juridique, et que l'entité ait été ou non informée de la possibilité correspondante :
   - l'utilisation, la citation, la copie, l'adaptation, la diffusion ou la mise en œuvre de tout ou partie des contenus du projet ;
   - les décisions prises, les actions engagées ou les abstentions sur la base des contenus du projet ;
   - les résultats d'exécution, dans un flux de travail, de la documentation, des configurations et des gabarits établis conformément aux contenus du projet ;
   - les interruptions, échecs ou anomalies de données résultant de problèmes de compatibilité entre les contenus du projet et des outils, plateformes ou services tiers ;
   - la modification, la suspension de la fourniture ou l'arrêt de la maintenance des contenus du projet.
2. Les pertes et dommages visés à l'alinéa précédent comprennent notamment : les pertes directes, les pertes indirectes, les pertes accessoires, les pertes consécutives, les dommages punitifs, ainsi que la perte de bénéfices, la perte de revenus, l'interruption d'activité, la perte ou la corruption de données, l'atteinte à la réputation, les coûts d'approvisionnement supplémentaires et les réclamations de tiers.
3. Les clauses limitatives de la présente déclaration ne prennent effet que dans les limites permises par le droit applicable. Si une juridiction n'autorise pas la limitation ou l'exclusion d'une responsabilité déterminée, ces limitations ne s'appliquent pas dans cette juridiction, les autres clauses demeurant en vigueur.
```

### 3.6 Contenus tiers et articulation avec la licence

```markdown
## Contenus tiers et articulation avec la licence

1. Les liens externes, outils, services, icônes, polices et ressources cités dans les contenus du projet sont fournis par les tiers concernés et soumis à leurs propres conditions ; {{主体名称}} n'assume aucune responsabilité quant à leur contenu, leur disponibilité, leur exactitude, leur sécurité ou leur licéité, et n'exprime aucune approbation. L'utilisateur doit vérifier lui-même leurs conditions et leur adéquation ; les obligations de licence relatives aux ressources tierces ne sont ni transférées ni supprimées du fait de leur citation dans les contenus du projet.
2. Le présent projet est distribué sous licence {{许可证名称及 SPDX 标识符}}, dont le texte intégral figure dans [LICENSE](./LICENSE). La présente déclaration est une explication, du point de vue de l'utilisateur, des clauses d'exonération de la licence ; elle ne remplace pas, ne modifie pas et n'affaiblit pas ces clauses.
3. En cas de conflit d'interprétation entre la présente déclaration et les clauses de la licence, le texte de la licence prévaut. Aucune formulation de la présente déclaration ne peut être interprétée comme une redevance supplémentaire, une condition ou une restriction aux droits concédés.
4. En cas de republication des contenus du projet ou de contenus qui en dérivent, les mentions de droit d'auteur et de licence doivent être conservées conformément aux exigences de la licence, et la présente déclaration peut y être jointe afin que les utilisateurs en aval connaissent les limites de responsabilité.
```

### 3.7 Modification et entrée en vigueur

```markdown
## Modification et entrée en vigueur

1. La présente déclaration est révisée en tant que de besoin par {{维护主体}} en fonction des mises à jour de contenu et des nécessités de conformité ; après révision, la version la plus récente figurant dans {{仓库地址或发布渠道}} fait foi.
2. La présente déclaration entre en vigueur à compter du {{生效日期}}. L'utilisateur qui continue d'utiliser les contenus du projet après la révision de la déclaration est régi par la version révisée ; s'il n'approuve pas le contenu de la révision, il doit cesser l'utilisation.
3. Les clauses de la présente déclaration sont indépendantes les unes des autres. La nullité ou l'inopposabilité d'une clause n'affecte pas la validité des autres clauses.
4. Contact : {{真实可达的联系邮箱或渠道}}.
```

## 4. Tableau de correspondance des espaces réservés et définition des champs

| Espace réservé | Obligatoire | Définition du champ | Exemple de saisie |
| --- | --- | --- | --- |
| `{{项目名称}}` | Oui | Nom public du projet, identique à la première ligne du README | `FooBar` |
| `{{主体名称}}` | Oui | Dénomination complète de l'entité qui assume ou décline la responsabilité ; pour un projet personnel, indiquer le nom de la personne, pour un projet d'entreprise, la dénomination légale | `Société technologique Exemple SARL` |
| `{{维护主体}}` | Oui | Organisation ou personne chargée de réviser la déclaration | `Équipe de maintenance FooBar` |
| `{{更新日期}}` | Oui | Date de la dernière révision de la présente déclaration, au format uniforme AAAA-MM-JJ | `2026-11-18` |
| `{{生效日期}}` | Oui | Date d'entrée en vigueur de la présente déclaration, pouvant être identique à la date de mise à jour | `2026-11-18` |
| `{{内容性质描述}}` | Oui | En une phrase, ce qu'est le projet et son degré de maturité | `Implémentation d'exemple à destination des développeurs, composant non destiné à la production` |
| `{{数据或示例的时点与范围说明}}` | Non | Moment de collecte et champ d'application des données ou paramètres des exemples | `Statistiques d'octobre 2026 sur 120 échantillons` |
| `{{许可证名称及 SPDX 标识符}}` | Oui | Nom complet et identifiant SPDX de la licence du projet | `Licence MIT (MIT)` |
| `{{仓库地址或发布渠道}}` | Oui | Emplacement de publication faisant autorité pour la dernière version de la déclaration | `https://github.com/owner/repo` |
| `{{真实可达的联系邮箱或渠道}}` | Oui | Adresse réelle permettant à l'utilisateur de joindre les mainteneurs | `security@example.com` |

## 5. Consignes de remplissage et variantes de scénario

| Scénario | Clauses à conserver | Clauses pouvant être supprimées | Points d'ajustement |
| --- | --- | --- | --- |
| Projet personnel | 3.1 / 3.2 / 3.3 / 3.5 / 3.7 | 3.4 peut être allégée | Indiquer le nom réel comme dénomination de l'entité ; utiliser pour le contact une adresse électronique conservée à long terme |
| Projet d'entreprise | Toutes les clauses | Aucune | Indiquer la dénomination légale du registre du commerce comme dénomination de l'entité ; publication après validation par le service juridique |
| Projet open source | Toutes les clauses, en particulier 3.6 | Aucune | Conserver l'explication de l'articulation avec la licence ; ne pas réduire les droits concédés par la licence |
| Logiciel propriétaire | 3.1 / 3.2 / 3.3 / 3.4 / 3.5 / 3.7 | Les alinéas 2 à 4 de 3.6 peuvent être supprimés | Supprimer les formulations relatives à la licence open source et renvoyer au contrat de licence utilisateur final |
| Prototype expérimental | 3.1 / 3.2 / 3.3 / 3.7 | 3.5 peut être allégée | Mentionner explicitement « prototype » dans la nature du contenu, afin d'éviter qu'il soit pris pour une version stable |
| Traitement de données personnelles | Toutes les clauses | Aucune | Ajouter les rôles de traitement des données, les durées de conservation et le canal d'exercice des droits des personnes concernées ; voir également la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md) |

Tableau des erreurs fréquentes :

| Rédaction erronée | Conséquence | Rédaction correcte |
| --- | --- | --- |
| « Le présent projet n'assume aucune responsabilité » | Formulation absolue, facilement jugée nulle | « Dans toute la mesure permise par la loi, n'assume aucune responsabilité… » |
| « Le droit d'interprétation finale appartient à l'auteur » | Conflit avec les droits concédés par la licence, source de litige | « En cas de conflit, le texte de la licence prévaut » |
| Laisser `test@example.com` comme coordonnées | Inaccessible, perte du canal de communication | Saisir une adresse électronique réelle et valable à long terme |
| Recopier la déclaration d'un autre projet sans changer l'entité | Entité inadaptée, déclaration privée de sens | Remplacer un à un les espaces réservés et vérifier la cohérence de l'entité |

## 6. Exemple complet

Voici un exemple rempli pour un projet open source personnel, fourni à titre de référence de format uniquement et à ne pas recopier directement comme déclaration propre.

```markdown
# Clause de non-responsabilité

> La présente déclaration s'applique à l'ensemble des contenus publiés par DemoCLI (ci-après « le présent projet »), y compris le code source, la documentation, les gabarits, les exemples, les données et les ressources associées (ci-après collectivement « les contenus du projet »).

1. La présente déclaration vise à clarifier la nature des contenus du projet, à signaler les risques d'utilisation et à préciser les limites de responsabilité ; elle ne constitue pas une restriction supplémentaire aux droits de quiconque, ni une révocation ou une réduction des droits concédés par la licence du projet.
2. Toute entité qui accède, copie, cite, adapte, diffuse ou utilise tout ou partie des contenus du projet est réputée avoir lu et compris la présente déclaration.
3. La date de dernière mise à jour de la présente déclaration est le 2026-11-18.

## Nature du contenu

1. Les contenus du projet constituent un outil en ligne de commande d'exemple à destination des développeurs et ne représentent pas une norme officielle, un avis juridique ou une conclusion de conseil professionnel d'une quelconque organisation, branche d'activité ou juridiction.
2. Les contenus du projet ne fournissent aucune garantie d'adéquation à une pile technique, un environnement d'exécution ou une exigence de conformité particuliers, et ne constituent pas un avis professionnel en matière juridique, de conformité, de sécurité, financière ou fiscale.
3. Les paramètres d'exemple figurant dans les contenus du projet ne servent qu'à démontrer une écriture et ne doivent pas être repris directement comme valeurs recommandées en environnement de production.

## Absence de garantie

Dans toute la mesure permise par la loi, 张三 n'accorde aucune garantie expresse ou implicite, y compris notamment l'exactitude absolue du contenu, son adéquation à un usage particulier, l'obtention nécessaire des résultats escomptés par la mise en œuvre, la disponibilité continue et l'absence d'atteinte aux droits de tiers.

## Limitation de responsabilité

Dans toute la mesure permise par la loi, 张三 n'assume aucune responsabilité pour toute perte résultant de l'utilisation, de l'adaptation ou de la mise en œuvre des contenus du projet, que ce soit sur un fondement contractuel, délictuel ou tout autre fondement juridique. Si une juridiction n'autorise pas la limitation ou l'exclusion d'une responsabilité déterminée, ces limitations ne s'appliquent pas dans cette juridiction, les autres clauses demeurant en vigueur.

## Contenus tiers et articulation avec la licence

Le présent projet est distribué sous licence MIT (MIT), dont le texte intégral figure dans [LICENSE](./LICENSE). La présente déclaration est une explication, du point de vue de l'utilisateur, des clauses d'exonération de la licence ; elle ne remplace pas, ne modifie pas et n'affaiblit pas ces clauses ; en cas de conflit d'interprétation, le texte de la licence prévaut.

## Modification et entrée en vigueur

La présente déclaration entre en vigueur à compter du 2026-11-18, est révisée par l'équipe de mainteneurs de DemoCLI, et la version la plus récente figurant dans https://github.com/example/democli fait foi. Les clauses sont indépendantes les unes des autres. Contact : maintainer@example.com.
```

## Fichiers associés

- Déclaration concrète de ce projet : [clause de non-responsabilité](./disclaimer.md)
- Règles relatives à la licence : [spécification LICENSE](./license-specification.md)
- Sécurité et confidentialité : [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)
- Conformité open source : [spécification de conformité open source](./open-source-compliance-specification.md)
- Conventions rédactionnelles générales : [spécification rédactionnelle générale](./general-writing-specification.md)
- Retour à l'index en chinois simplifié : [README](./README.md)
- Retour à l'accueil du dépôt : [README](../../README.md)
