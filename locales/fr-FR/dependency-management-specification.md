# Spécification de gestion des dépendances

> Problème que ce fichier résout : définir les gabarits et champs de demande d'introduction de dépendance, d'inventaire des dépendances, de verrouillage et de mise à jour, afin de garantir un build reproductible, des dépendances traçables et une conformité des licences.

## 1. Dispositions de la spécification

1. L'introduction d'une nouvelle dépendance doit préciser son usage, sa licence et son état de maintenance (voir la [spécification de conformité open source](./open-source-compliance-specification.md)).
2. Il convient de privilégier les dépendances à licence compatible et à communauté active ; l'introduction de dépendances d'origine inconnue ou de licence indéterminée est interdite.
3. La version des dépendances doit être inscrite dans le lockfile et celui-ci doit être commité dans le dépôt, afin de garantir la reproductibilité du build en environnement propre (règles absolues H9 et dimension D5).
4. Le numéro de version doit verrouiller la version réellement résolue ; les expressions de plage ne doivent pas être utilisées pour la livraison finale.
5. La mise à jour des dépendances doit s'appuyer sur des outils d'automatisation et passer l'intégration continue après mise à jour ; les vulnérabilités doivent être traitées sans délai ou faire l'objet de mesures d'atténuation consignées.
6. L'inventaire des dépendances doit rester cohérent avec le fichier NOTICE (voir la [spécification NOTICE](./notice-specification.md)).

## 2. Gabarit de demande d'introduction de dépendance

```markdown
## Demande d'introduction de dépendance : {{包名}}

- Numéro de demande : {{DEP-NNN}}
- Demandeur : {{姓名}}
- Usage : {{一句话说明解决什么问题}}
- Développement interne possible : {{是 / 否；是则说明为何仍引入}}
- Évaluation des alternatives : {{已评估的替代包及未选原因}}

| Champ | Valeur |
| --- | --- |
| Nom du paquet | {{包名}} |
| Version introduite | {{精确版本号}} |
| Licence | {{SPDX ID}} |
| Compatibilité de licence | {{兼容 / 不兼容 / 需法务确认}} |
| Dernière publication | {{YYYY-MM-DD}} |
| État de maintenance | {{活跃 / 低频 / 停滞}} |
| Téléchargements hebdomadaires | {{数值}} |
| Nombre de dépendances transitives | {{数值}} |
| Vulnérabilités connues | {{无 / CVE 编号与处置}} |
| Impact sur la taille du paquet | {{增量 KB}} |

- Conclusion : {{批准 / 拒绝 / 有条件批准}}
- Approbateur : {{姓名}}
```

## 3. Gabarit d'inventaire des dépendances

```markdown
# Inventaire des dépendances : {{项目名称}}

Mise à jour : {{YYYY-MM-DD}} ｜ lockfile : {{路径}} ｜ outil de génération : {{工具与版本}}

| Dépendance | Version introduite | Version verrouillée | Type | Licence | Usage | Dernière revue |
| --- | --- | --- | --- | --- | --- | --- |
| {{包名}} | {{^1.2.0}} | {{1.2.3}} | directe / indirecte | {{MIT}} | {{用途}} | {{YYYY-MM-DD}} |

## Historique des mises à jour
| Date | Dépendance | Évolution de version | Raison | Résultat de vérification |
| --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{包名}} | {{1.2.2 → 1.2.3}} | {{安全修复}} | {{CI 全绿}} |

## Exceptions et atténuation
| Dépendance | Problème | Mesure d'atténuation | Date de réexamen |
| --- | --- | --- | --- |
| {{包名}} | {{漏洞 / 停滞}} | {{限制使用范围}} | {{YYYY-MM-DD}} |
```

## 4. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Numéro de demande | Oui | `DEP-NNN` | Continu, sans réutilisation | `DEP-007` |
| Usage | Oui | Texte | Décrit le problème résolu, « facilite le développement » est interdit | `Analyse de fichiers de configuration TOML` |
| Évaluation des alternatives | Oui | Texte | Évaluer au moins une alternative | `toml-js évalué, non retenu pour cause de maintenance stagnante` |
| Version introduite | Oui | Version exacte | Ne pas utiliser `^` ni `~` | `1.2.3` |
| Version verrouillée | Oui | Version exacte | Conforme au lockfile | `1.2.3` |
| Licence | Oui | SPDX ID | Conforme à la notation de la [spécification LICENSE](./license-specification.md) | `MIT` |
| État de maintenance | Oui | Énumération | Actif / faible fréquence / stagnante, avec critère de détermination | `Actif (commits dans les 30 derniers jours)` |
| Nombre de dépendances transitives | Oui | Valeur | Si trop élevé, préciser l'impact sur la taille et les risques | `12` |
| Vulnérabilités connues | Oui | Texte | Écrire « aucune » s'il n'y en a pas, ne jamais laisser vide | `Aucune` |
| Date de réexamen | Oui | Date | Les exceptions doivent avoir une date de réexamen | `2026-12-31` |

## 5. Instructions de saisie

1. **Évaluation du développement interne** : répondre d'abord à la question « une implémentation avec la bibliothèque standard ou les capacités existantes est-elle possible » ; si l'introduction a lieu malgré la faisabilité interne, la raison doit être exposée.
2. **Licence** : doit être un SPDX ID ; `UNLICENSED` et les licences personnalisées doivent être requalifiées en « à confirmer par le juridique » et ne peuvent être introduites directement.
3. **État de maintenance** : se fonder sur la date de dernière publication et la réactivité aux issues ; « il semble y avoir de la maintenance » est interdit.
4. **Verrouillage de version** : à la livraison, le lockfile doit contenir la version exacte résolue ; `package.json` peut conserver une expression de plage, mais le lockfile doit être exact.
5. **Rythme de mise à jour** : activer les mises à jour automatisées, avec confirmation humaine de la fusion ; chaque mise à jour doit passer l'intégration continue et faire l'objet d'une vérification du changement de licence.
6. **Traitement des vulnérabilités** : privilégier la montée vers une version sûre ; en cas d'impossibilité, consigner les mesures d'atténuation et la date de réexamen, et inscrire le risque au registre prévu par la [spécification de réponse aux incidents](./incident-response-specification.md).
7. **Synchronisation de l'inventaire** : après l'introduction ou le retrait d'une dépendance, mettre à jour l'inventaire des dépendances et le NOTICE ; les trois éléments (lockfile, inventaire, NOTICE) doivent être cohérents.

Erreurs fréquentes :

| Formulation erronée | Problème | Correction |
| --- | --- | --- |
| « Utiliser une bibliothèque pour gérer la configuration » | Aucun nom de paquet ni usage précis | Indiquer le nom du paquet, la version et le problème résolu |
| Licence indiquée comme « open source » | Compatibilité non déterminable | Indiquer le SPDX ID |
| Lockfile non commité | Build non reproductible | Commiter le lockfile (règle absolue H9) |
| Nombre de dépendances transitives laissé vide | Risque invisible | Renseigner la valeur exacte |
| Vulnérabilité sans mesure d'atténuation | Risque non suivi | Ajouter la mesure et la date de réexamen |

## 6. Exemple complet

```markdown
## Demande d'introduction de dépendance : remark

- Numéro de demande : DEP-001
- Demandeur : Wang Wu
- Usage : servir de couche d'analyse Markdown pour répondre au besoin de localisation de nœuds du moteur de règles (REQ-001, REQ-004).
- Développement interne possible : non ; un développement interne ne permettrait pas de couvrir les cas limites GFM dans la limite des ressources disponibles.
- Évaluation des alternatives : marked a été évalué, non retenu en raison de capacités insuffisantes de localisation de nœuds en chinois.

| Champ | Valeur |
| --- | --- |
| Nom du paquet | remark |
| Version introduite | 15.0.1 |
| Licence | MIT |
| Compatibilité de licence | Compatible |
| Dernière publication | 2026-11-02 |
| État de maintenance | Actif (commits dans les 30 derniers jours) |
| Téléchargements hebdomadaires | 4 200 000 |
| Nombre de dépendances transitives | 18 |
| Vulnérabilités connues | Aucune |
| Impact sur la taille du paquet | +42 Ko |

- Conclusion : approuvée, mise en œuvre avec l'ADR-0002
- Approbateur : Li Si
```

## Fichiers associés

- Détermination de la compatibilité des licences : [spécification de conformité open source](./open-source-compliance-specification.md)
- Notation SPDX des licences : [spécification LICENSE](./license-specification.md)
- Cohérence du NOTICE : [spécification NOTICE](./notice-specification.md)
- Le build reproductible relève de la dimension D5 : [matrice des dimensions de revue](./review-dimension-matrix.md)
- La mise à jour automatisée relève de la dimension D9 : [matrice des dimensions de revue](./review-dimension-matrix.md)
- Tests et traitement des vulnérabilités : [spécification des tests](./testing-specification.md), [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)
- Lien avec les décisions d'architecture : [spécification des documents de conception d'architecture](./architecture-design-document-specification.md)
