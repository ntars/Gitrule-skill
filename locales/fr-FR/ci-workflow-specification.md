# Spécification des workflows d'intégration continue

> Problème que ce fichier résout : définir les conditions de déclenchement, le découpage des tâches, la stratégie de cache et la configuration de sécurité des workflows d'intégration continue `.github/workflows/*.yml`, afin de rendre le build, les tests et les vérifications reproductibles et auditables.

## 1. Principes de conception

1. **Responsabilité unique** : chaque workflow ne traite qu'une seule catégorie d'objectifs (build, tests, publication, déploiement de la documentation) ; la publication et les tests ne doivent pas être mélangés dans un même workflow.
2. **Retour rapide** : les vérifications légères (lint, formatage) passent en premier, les tâches longues (matrice de tests complète) ensuite.
3. **Reproductibilité** : verrouiller les versions des dépendances, utiliser des Actions à version figée ; le cache ne sert qu'à accélérer, sans modifier le résultat.
4. **Moindre privilège** : les workflows accordent les permissions par tâche, en lecture seule par défaut ; les tâches de publication élèvent leurs droits séparément (voir la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)).

## 2. Structure des fichiers

### 2.1 Nommage et chemin

- Le chemin est fixé à `.github/workflows/*.yml`.
- Le nom de fichier utilise des minuscules et des traits d'union, nommé selon la responsabilité, par exemple `ci.yml`, `release.yml`, `docs.yml`.
- Le champ `name` du workflow doit être sémantiquement cohérent avec le nom de fichier.

### 2.2 Blocs obligatoires

| Bloc | Rôle | Exigence |
| --- | --- | --- |
| `name` | Nom d'affichage du workflow | Concis, la responsabilité doit être lisible |
| `on` | Conditions de déclenchement | Préciser la branche, le chemin ou l'événement |
| `permissions` | Déclaration des permissions | Déclaration explicite, minimales par défaut |
| `jobs` | Ensemble des tâches | Découpage par responsabilité |

### 2.3 Conception des conditions de déclenchement

| Événement déclencheur | Applicable à | Attention |
| --- | --- | --- |
| `push` | Ligne principale et branches de version | Limiter le périmètre des branches, éviter un déclenchement sur toutes les branches |
| `pull_request` | Toutes les demandes de fusion | Garantir la vérification avant fusion |
| `workflow_dispatch` | Déclenchement manuel | Pour les opérations contrôlées : publication, restauration, etc. |
| `schedule` | Tâches planifiées | Pour la vérification des mises à jour de dépendances, les builds nocturnes |
| `release` | Actions après publication | Pour l'envoi des artefacts et les annonces |

## 3. Découpage des tâches

Ordre des étapes recommandé :

1. **Analyse statique** : formatage, lint, vérification des types.
2. **Build** : produire les artefacts de build, réutilisables par les tâches suivantes.
3. **Tests** : tests unitaires, tests d'intégration, parallélisables par matrice.
4. **Validation des artefacts** : vérifier la taille, la signature ou l'intégrité des artefacts de build.
5. **Publication** : exécutée uniquement si l'intégration continue est entièrement au vert et les conditions remplies (voir la [spécification de push et de publication](./push-and-release-specification.md)).

Les dépendances entre tâches sont déclarées via `needs`, afin de garantir l'interruption en cas d'échec ; les tâches suivantes ne doivent pas continuer en état d'échec.

## 4. Build matriciel

Utiliser `strategy.matrix` pour couvrir plusieurs versions et plateformes :

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    node-version: [18, 20, 22]
```

Exigences :

- Couvrir les versions minimale et la plus récente déclarées comme prises en charge par le projet (voir [note de compatibilité](./readme-sections-specification.md) section 14).
- Régler `fail-fast` sur `false`, afin que chaque combinaison s'exécute complètement et que les problèmes de compatibilité soient faciles à localiser.
- Ne pas dépasser trois dimensions de matrice, pour éviter l'explosion combinatoire.

## 5. Stratégie de cache

| Objet mis en cache | Clé suggérée | Attention |
| --- | --- | --- |
| Répertoire des dépendances | Hachage du lockfile du gestionnaire de paquets | Invalidation dès que le lockfile change |
| Artefacts de build | Hachage du code source et de la configuration | Cohérent avec les entrées du build |
| Chaîne d'outils | Numéro de version | Invalidation dès qu'une version est mise à jour |

Le cache accélère seulement, sans modifier le résultat du build ; en cas de succès du cache, les tests complets doivent tout de même être exécutés.

## 6. Configuration de sécurité

1. Les secrets sont injectés via les Secrets du dépôt ; leur écriture dans les fichiers de workflow ou les journaux est interdite.
2. Chaque workflow déclare explicitement `permissions`, avec `contents: read` par défaut.
3. Les Actions tierces sont référencées par version figée ou hachage de commit, pour éviter les étiquettes flottantes.
4. Lorsqu'une demande de fusion provient d'un Fork, l'injection de Secrets est interdite, afin de prévenir les attaques par élévation de privilèges.
5. Les tâches de publication sont séparées des vérifications principales et ne se déclenchent que sur une branche protégée ou un tag.

## 7. Badges d'état

Le workflow doit fournir au README un badge d'état, au format suivant :

```markdown
[![CI](https://github.com/{owner}/{repo}/actions/workflows/ci.yml/badge.svg)](https://github.com/{owner}/{repo}/actions/workflows/ci.yml)
```

Les paramètres et l'agencement des badges sont décrits dans la [spécification des badges](./badge-specification.md).

## 8. Pratiques interdites

1. L'écriture en dur de secrets ou d'adresses internes dans les workflows est interdite.
2. L'usage de `continue-on-error` pour masquer l'échec de tests est interdit.
3. La configuration de plusieurs règles de déclenchement conflictuelles pour une même condition est interdite.
4. L'exécution d'une publication alors que les vérifications de la ligne principale ont échoué est interdite.

## Fichiers associés

- Périmètre de responsabilité des fichiers : [matrice documentaire](./document-matrix.md)
- Build et tests en local : [spécification des tests](./testing-specification.md)
- Lien avec la publication : [spécification de push et de publication](./push-and-release-specification.md)
- Les vérifications automatisées relèvent de la dimension D9 : [matrice des dimensions de revue](./review-dimension-matrix.md)
- Lignes rouges sur les secrets : H3 des [règles absolues](./hard-rules.md)
