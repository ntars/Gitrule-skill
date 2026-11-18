# Spécification de gestion des versions

> Problème que ce fichier résout : définir les règles de versionnage sémantique, l'enregistrement des décisions de version, les critères d'incrémentation et les relations de couplage, afin de garantir que le numéro de version exprime la nature du changement, soit analysable par les outils et cohérent avec les artefacts de publication.

## 1. Dispositions normatives

1. Le numéro de version suit le versionnage sémantique : `MAJOR.MINOR.PATCH`.
2. Le numéro de version ne comporte ni année, ni date, ni numéro de build comme élément sémantique principal ; un numéro de version publié ne doit jamais être réutilisé.
3. Les changements cassants doivent être traités de manière groupée lors de l'incrémentation majeure, avec indication du mode de migration.
4. Le numéro de version est identique au tag, dont le format est `vMAJOR.MINOR.PATCH` (voir la [spécification de push et de publication](./push-and-release-specification.md)).
5. Les versions préliminaires utilisent les suffixes `-alpha`, `-beta`, `-rc` et doivent être validées avant la publication de la version stable.

## 2. Format du numéro de version et critères d'incrémentation

| Position | Condition d'incrémentation | Type de commit déclencheur | Exemple |
| --- | --- | --- | --- |
| MAJOR | Changement cassant incompatible | `feat!:` / `fix!:` / `BREAKING CHANGE:` | `1.9.2 → 2.0.0` |
| MINOR | Nouvelle fonctionnalité rétrocompatible | `feat` | `1.2.3 → 1.3.0` |
| PATCH | Correction de défaut rétrocompatible | `fix` | `1.2.3 → 1.2.4` |

Format préliminaire : `vMAJOR.MINOR.PATCH-alpha.N` / `-beta.N` / `-rc.N`, le numéro commençant à 1 et croissant ; le suffixe est retiré lors de la publication de la version stable.

## 3. Gabarit d'enregistrement des décisions de version

```markdown
## Décision de version : {{X.Y.Z}}

- Date de décision : {{YYYY-MM-DD}}
- Décideur : {{姓名}}
- Version actuelle : {{X.Y.Z}}
- Version cible : {{X.Y.Z}}
- Position incrémentée : {{MAJOR / MINOR / PATCH}}
- Justification : {{列举触发的提交类型与变更内容}}

| Changement | Type de commit | Exigence rattachée | Rupture de compatibilité |
| --- | --- | --- | --- |
| {{变更描述}} | {{feat / fix / BREAKING CHANGE}} | {{REQ-NNN}} | {{是 / 否}} |

- Traitement du changement cassant : {{迁移指南链接 / 不适用}}
- Entrée du journal des modifications : {{链接}}
- tag : {{vX.Y.Z}}
- Contrôle de publication : {{已通过 / 待通过}}
```

## 4. Gabarit du registre des versions

```markdown
# Registre des versions : {{项目名称}}

| Version | Date de publication | Type | Changements principaux | tag | Journal des modifications | Statut |
| --- | --- | --- | --- | --- | --- | --- |
| {{X.Y.Z}} | {{YYYY-MM-DD}} | {{主版本 / 次版本 / 修订}} | {{一句话}} | {{vX.Y.Z}} | {{链接}} | {{当前 / 历史 / 已废弃}} |
| {{X.Y.Z-rc.1}} | {{YYYY-MM-DD}} | Préliminaire | {{一句话}} | {{vX.Y.Z-rc.1}} | {{链接}} | déjà remplacé |

Statut : actuelle / historique / dépréciée / remplacée
```

## 5. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Version actuelle | Oui | `X.Y.Z` | Identique au tag le plus récent | `1.2.3` |
| Version cible | Oui | `X.Y.Z` | Une seule position incrémentée | `1.3.0` |
| Position incrémentée | Oui | Énumération | MAJOR / MINOR / PATCH | `MINOR` |
| Justification | Oui | Liste | Énumère les changements déclencheurs, « mise à jour de routine » est interdit | `Ajout du support TOML` |
| Traitement du changement cassant | Obligatoire sous condition | Lien | Obligatoire en cas d'incrémentation MAJOR | `[guide de migration]` |
| Entrée du journal des modifications | Oui | Lien | Pointe vers la section de version correspondante | `[1.3.0]` |
| tag | Oui | `vX.Y.Z` | Correspondance biunivoque avec le numéro de version | `v1.3.0` |
| Date de publication | Oui | `YYYY-MM-DD` | Correspond à la date de pose du tag | `2026-11-20` |
| Statut | Oui | Énumération | actuelle / historique / dépréciée / remplacée | `actuelle` |

## 6. Instructions de saisie

1. **Une seule position** : chaque publication n'incrémente qu'une position ; si des commits feat et BREAKING CHANGE coexistent, retenir la position la plus haute (MAJOR) et intégrer les autres changements à cette version.
2. **Regroupement des ruptures** : plusieurs changements cassants sont fusionnés dans une même version majeure, afin d'éviter des incrémentations MAJOR successives.
3. **Réutilisation interdite** : un numéro de version publié est définitivement occupé ; en cas de retrait de publication, incrémenter PATCH et publier une version révisée, sans réutiliser le numéro d'origine.
4. **Versions préliminaires** : `alpha` sert à la validation interne, `beta` à l'essai public, `rc` à la version candidate ; chaque niveau doit passer la CI.
5. **Contrôle de cohérence** : le numéro de version doit être identique dans le tag, le journal des modifications, les Release Notes, l'enregistrement de déploiement et le registre des versions ; en cas d'incohérence, le tag fait foi et les autres sont corrigés.
6. **Couplage** : la justification de l'incrémentation provient du type défini dans la [spécification de message de commit](./commit-message-specification.md) ; la communication externe est décrite dans la [spécification du journal des modifications](./changelog-specification.md) ; le chemin de mise à niveau dans la [spécification de guide de migration](./migration-guide-specification.md).

Erreurs courantes :

| Rédaction erronée | Problème | Mode de correction |
| --- | --- | --- |
| `v2026.11` | La date sert d'élément sémantique principal | Remplacer par `v2.1.0` |
| Deux positions incrémentées pour une même version | Sémantique confuse | N'incrémenter que la position la plus haute |
| Réutilisation d'un numéro de version retiré | Impossible de distinguer les artefacts | Incrémenter PATCH et publier une version révisée |
| Incrémentation MAJOR sans guide de migration | Les utilisateurs ne peuvent pas mettre à niveau | Ajouter le guide de migration et le lien |
| Numéro de version présent uniquement dans le tag | Registre et journal incohérents | Synchroniser les cinq emplacements |

## 7. Exemple complet

```markdown
## Décision de version : 2.0.0

- Date de décision : 2026-12-01
- Décideur : 李四
- Version actuelle : 1.9.2
- Version cible : 2.0.0
- Position incrémentée : MAJOR
- Justification : le format du fichier de configuration passe d'un objet à un chemin de fichier, ce qui constitue un changement incompatible.

| Changement | Type de commit | Exigence rattachée | Rupture de compatibilité |
| --- | --- | --- | --- |
| Configuration par chemin de fichier | BREAKING CHANGE | REQ-021 | Oui |
| Ajout de l'analyse TOML | feat | REQ-001 | Non |

- Traitement du changement cassant : [guide de migration v2.0]
- Entrée du journal des modifications : [2.0.0]
- tag : v2.0.0
- Contrôle de publication : réussi
```

## Fichiers associés

- Types de commit et marqueurs de rupture : [spécification de message de commit](./commit-message-specification.md)
- tag et Release Notes : [spécification de push et de publication](./push-and-release-specification.md)
- Entrées du journal des modifications : [spécification du journal des modifications](./changelog-specification.md)
- Chemin de mise à niveau : [spécification de guide de migration](./migration-guide-specification.md)
- Source de la version cible : [spécification de feuille de route](./roadmap-specification.md)
- Cohérence des versions dans l'enregistrement de déploiement : [spécification de déploiement et de restauration](./deployment-and-rollback-specification.md)
