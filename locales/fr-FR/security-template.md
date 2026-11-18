# Gabarit SECURITY

> Problème que ce fichier résout : fournir un gabarit de politique de sécurité directement copiable pour générer le SECURITY.md d'un projet, en précisant les versions prises en charge, le canal de signalement des vulnérabilités, le processus de réponse et les principes de divulgation ; les consignes de saisie associées couvrent le choix du canal de signalement et le traitement des informations sensibles.

## 1. Mode d'emploi

1. Copier l'intégralité du contenu de la section 3 « Corps du gabarit » et créer un fichier `SECURITY.md` à la racine du projet.
2. Remplacer les espaces réservés selon la section 4 ; le canal de signalement doit être une adresse réellement joignable et n'exposant pas publiquement la surface d'attaque.
3. Adapter le gabarit selon le scénario de la section 5 : un projet ne maintenant qu'une seule version supprime la ligne de l'ancienne version dans le tableau des versions prises en charge.
4. Les règles de sécurité et les exigences relatives aux informations sensibles figurent dans la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md) ; la dimension de gouvernance communautaire figure dans la [matrice des dimensions de revue](./review-dimension-matrix.md).

## 2. Principes de personnalisation

- **Priorité au canal privé** : le signalement des vulnérabilités passe par un canal privé ; il est interdit d'exiger du rapporteur qu'il divulgue des détails dans un sujet public.
- **Délais explicites** : indiquer les délais de première réponse et de correction, afin d'éviter un engagement sans terme.
- **Minimisation de l'information** : demander au rapporteur le minimum d'informations nécessaires à la reproduction ; la soumission de données de production réelles est interdite.
- **Conformité juridique** : les principes de divulgation doivent être conformes au droit applicable et aux politiques des plateformes ; les secteurs réglementés doivent faire l'objet d'une validation par le service juridique.

## 3. Corps du gabarit

```markdown
# Politique de sécurité

> Ce fichier décrit le périmètre de support de sécurité et les modalités de signalement des vulnérabilités de {{项目名称}} ; il s'adresse aux chercheurs en sécurité, aux contributeurs et aux utilisateurs.

## Versions prises en charge

| Version | Rapports de sécurité acceptés |
| --- | --- |
| {{当前版本}} | Oui |
| {{上一版本}} | {{是否接受}} |
| Versions antérieures | Non |

## Canal de signalement

Ne signalez pas les vulnérabilités de sécurité via des sujets publics, des espaces de discussion ou des canaux sociaux. Utilisez le canal privé suivant :

- Adresse de sécurité : {{真实可达的安全邮箱}}
- Portail de signalement privé : {{私有漏洞报告地址}}

En l'absence de ces canaux, contactez les mainteneurs via {{备用私有联系方式}}.

## Contenu du rapport

Pour accélérer le traitement, veuillez fournir autant que possible :

- la version et le composant concernés ;
- le type de vulnérabilité et son impact potentiel ;
- les étapes de reproduction minimales ou une preuve de concept ;
- la direction de correction suggérée (facultatif).

Ne soumettez pas de données de production réelles, de clés ni d'informations d'identité personnelle.

## Processus de réponse

| Étape | Délai | Description |
| --- | --- | --- |
| Accusé de réception | {{首次响应时限}} | Les mainteneurs confirment la réception du rapport |
| Évaluation initiale | {{评估时限}} | Détermination de la nature du problème de sécurité et de la portée de l'impact |
| Correction et vérification | {{修复时限}} | Réalisation et vérification de la correction, les problèmes complexes étant convenus séparément |
| Publication | {{发布延迟}} après la correction | Publication de l'avis de sécurité et de la version corrigée |

## Principes de divulgation

- Les mainteneurs gardent confidentiels l'identité du rapporteur et le contenu du rapport jusqu'à la publication de la correction.
- Sans l'accord des mainteneurs, le rapporteur ne doit pas divulguer les détails de la vulnérabilité avant la publication de la correction.
- Après la publication de la correction, les mainteneurs remercient le rapporteur dans l'avis de sécurité (avec son accord).
- Une recherche de sécurité menée de bonne foi et conforme à la présente politique n'entraîne aucune poursuite.

## Exceptions et clause de non-responsabilité

La présente politique ne constitue aucun engagement de garantie de sécurité ; le contenu du projet est fourni « en l'état », voir la [clause de non-responsabilité](./DISCLAIMER.md) et la [LICENSE](./LICENSE).
```

## 4. Tableau de correspondance des espaces réservés et définition des champs

| Espace réservé | Obligatoire | Définition du champ | Exemple de saisie |
| --- | --- | --- | --- |
| `{{项目名称}}` | Oui | Nom public du projet | `FooBar` |
| `{{当前版本}}` | Oui | Dernière version maintenue ou `main` | `v2.3.0` |
| `{{上一版本}}` | Non | Version précédente encore maintenue | `v2.2.x` |
| `{{是否接受}}` | Oui | Indique si cette version accepte les rapports de sécurité | `oui` |
| `{{真实可达的安全邮箱}}` | Oui | Adresse dédiée aux rapports de sécurité | `security@example.com` |
| `{{私有漏洞报告地址}}` | Oui | Portail de signalement privé | `https://github.com/owner/repo/security/advisories/new` |
| `{{备用私有联系方式}}` | Non | Canal de secours si le canal principal est indisponible | `通过维护者账号私信` |
| `{{首次响应时限}}` | Oui | Délai d'accusé de réception du rapport | `3 jours ouvrés` |
| `{{评估时限}}` | Oui | Délai d'achèvement de l'évaluation initiale | `7 jours ouvrés` |
| `{{修复时限}}` | Oui | Délai d'achèvement de la correction | `30 jours` |
| `{{发布延迟}}` | Oui | Intervalle avant la publication après correction | `7 jours` |

## 5. Consignes de saisie et variantes selon le scénario

| Scénario | Sections à conserver | Sections à adapter | Points d'ajustement |
| --- | --- | --- | --- |
| Projet mono-version | Canal de signalement, contenu du rapport, processus de réponse, principes de divulgation | Supprimer la ligne de l'ancienne version dans le tableau des versions prises en charge | Indiquer `main` ou le dernier tag comme version courante |
| Maintenance multi-version | Toutes | Aucune | Énumérer ligne par ligne les versions acceptant encore les rapports |
| Projet personnel | Toutes | Le tableau des versions prises en charge peut être simplifié | Utiliser une adresse de sécurité conservée à long terme |
| Projet d'entreprise | Toutes | Aucune | Les délais doivent être conformes au dispositif de sécurité interne et validés par le service juridique |
| Secteur réglementé | Toutes | Aucune | Ajouter les obligations de notification réglementaire et les exigences de conservation des données |

Correspondance des erreurs fréquentes :

| Formulation erronée | Conséquence | Formulation correcte |
| --- | --- | --- |
| « Veuillez signaler les vulnérabilités dans une issue » | Divulgation publique des détails, risque accru | Utiliser un canal privé |
| « Nous traiterons dès que possible » | Aucune attente claire, le rapporteur ne peut juger | Indiquer des délais par étape |
| Délai indiqué « correction sous 24 heures » | Engagement excessif, impossible à tenir | Indiquer une plage raisonnable et préciser que les problèmes complexes sont convenus séparément |
| Absence d'exigence de masquage | Le rapporteur peut soumettre des données de production réelles | Interdire explicitement la soumission de données réelles et de clés |

## 6. Exemple complet

Voici un exemple de saisie du paragraphe relatif au canal de signalement, à titre de référence de format uniquement.

```markdown
## Canal de signalement

Ne signalez pas les vulnérabilités de sécurité via des sujets publics, des espaces de discussion ou des canaux sociaux. Utilisez le canal privé suivant :

- Adresse de sécurité : security@example.com
- Portail de signalement privé : https://github.com/example/democli/security/advisories/new

Ne soumettez pas de données de production réelles, de clés ni d'informations d'identité personnelle.
```

## Fichiers associés

- Spécification correspondante : [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)
- Gabarits complémentaires : [gabarit de code de conduite](./code-of-conduct-template.md), [gabarit de guide de contribution](./contribution-guide-template.md), [gabarit de clause de non-responsabilité](./disclaimer-template.md)
- Dimension de signalement des vulnérabilités : [matrice des dimensions de revue](./review-dimension-matrix.md)
- Traitement d'un incident de fuite de clé : [spécification de push et de publication](./push-and-release-specification.md)
- Retour à l'index en chinois simplifié : [README](./README.md)
