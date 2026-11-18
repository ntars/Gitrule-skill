# Spécification de push et de publication

> Problème que ce fichier résout : définir la liste des actions avant, pendant et après le push, les règles de tag et de publication, le processus de traitement des incidents, ainsi que le guide complet de push vers GitHub et la matrice de traitement des échecs.

## 1. Avant le push

1. `git status` est propre, aucun fichier sensible non suivi.
2. `git log` ne contient ni WIP, ni `fix bug`, ni fuite d'informations personnelles.
3. Vérifier que `.gitignore` est effectif, que les artefacts et les dépendances ne sont pas suivis.
4. Le build, les tests et le lint passent en local.
5. Exécuter une analyse complète des secrets (y compris l'historique des commits).
6. La matrice documentaire est complète (voir la [matrice documentaire](./document-matrix.md)).

## 2. Actions de push

7. Pousser la branche personnelle : `git push -u origin feat/xxx`.
8. La branche principale passe uniquement par PR, jamais par un push direct.
9. `push --force` est interdit ; pour réécrire sa propre branche, utiliser `--force-with-lease`.
10. Le rebase et l'amend sont interdits sur une branche publique déjà poussée.
11. Un fichier de plus de 50 Mo passe d'abord par LFS avant le push.
12. Vérifier la visibilité du dépôt avant le premier push : privé par défaut, ne passer en public qu'en cas de besoin confirmé.

## 3. tag et publication

13. Format du tag `vMAJOR.MINOR.PATCH`, obligatoirement annoté : `git tag -a v1.0.0 -m "release: 1.0.0"`.
14. Le tag n'est posé qu'une fois la CI verte et les Release Notes prêtes.
15. Un changement cassant doit utiliser `feat!:` ou `BREAKING CHANGE:`, et le CHANGELOG doit indiquer le mode de migration.

## 4. Phase 6 · Après le push (Post-Push)

- poser un tag annoté ;
- rédiger les Release Notes ;
- vérifier la disponibilité des badges et des liens ;
- confirmer que la CI est verte ;
- confirmer l'exactitude des informations de la zone About (description / topics / liens / social preview).

## 5. Traitement des incidents

16. **Secret déjà poussé** : rotation immédiate → nettoyage avec `git filter-repo` → le push forcé sur une branche protégée passe par la procédure administrateur → annonce.
17. **Gros fichier poussé par erreur** : migration vers LFS ou réécriture de l'historique, la simple suppression du fichier est insuffisante.

## 6. Spécification du guide de push vers GitHub

Le guide doit comporter les sept parties suivantes, les commandes étant fournies en version complète et exécutable.

### 6.1 Sécurité préalable

1. Avant le push, sauvegarder intégralement le dépôt local et le dépôt distant ; l'usage de `git clone --mirror` pour produire une sauvegarde miroir est recommandé.
2. Vérifier que le dépôt distant n'a pas de collaborateur, ou que les collaborateurs ont été prévenus de suspendre leurs push.
3. Vérifier que la branche cible n'a pas activé la protection contre les push forcés.

### 6.2 Préparation locale

```bash
git status
git diff --name-status HEAD
git ls-files
```

Vérifier les trois sorties, confirmer que les changements à commiter correspondent au répertoire local, sans fichier temporaire, artefact de build ni documentation obsolète résiduelle. `.gitignore` doit couvrir les artefacts de build et les fichiers de configuration locaux.

### 6.3 Contrôle de cohérence

```bash
git fetch origin
git diff --name-status HEAD origin/{{分支名}}
```

Cette commande liste les différences de fichiers entre le dépôt distant et le local. Pour un fichier présent à distance et déjà supprimé en local, exécuter `git rm` en local puis commiter, afin que la suppression entre dans l'historique des versions.

### 6.4 Commit et push

```bash
git add -A
git commit -m "docs: 重建项目文档（README、README_EN、NOTICE）"
git push --force-with-lease origin {{分支名}}
```

Utiliser `--force-with-lease` plutôt que `--force`, afin de refuser le push lorsque de nouveaux commits d'autres personnes existent à distance et d'éviter d'écraser leur travail. Supprimer puis recréer le dépôt distant est une opération à haut risque, à n'utiliser que sur un dépôt personnel après sauvegarde miroir complète ; le guide doit signaler explicitement le risque de perte de données.

### 6.5 Vérification après le push

```bash
git ls-remote --heads origin
gh repo view --web
```

Confirmer item par item dans l'interface web la liste des fichiers, le rendu du README, les liens de changement de langue et la validité du lien NOTICE.

### 6.6 Matrice de traitement des échecs

| Type d'erreur | Manifestation typique | Traitement | Avertissement de risque |
| --- | --- | --- | --- |
| Échec d'authentification | `Authentication failed`, `Permission denied (publickey)` | Passer de HTTPS à SSH et configurer la clé, ou utiliser `gh auth login` avant le push | Aucun |
| Interruption réseau | `Failed to connect`, `RPC failed` | Changer de réseau, configurer un proxy, exécuter `git config --global http.postBuffer 524288000` | Aucun |
| Fichier hors limite | `remote: error: File exceeds 100 MB` | Retirer le gros fichier de l'historique des commits ou activer Git LFS | Après réécriture de l'historique, prévenir les collaborateurs de recloner |
| Conflit de casse | Noms de fichiers de casse différente provoquant des entrées en double | Corriger avec `git mv` puis commiter | Aucun |
| Conflit d'historique | `non-fast-forward`, `fetch first` | Privilégier `git pull --rebase` ; en cas de recouvrement nécessaire, utiliser `--force-with-lease` | L'écrasement des commits d'autrui est irréversible |
| Protection de branche | `protected branch hook declined` | Fusionner via le processus PR, ou faire ajuster temporairement les règles par un administrateur | Tout ajustement de règle doit être enregistré |
| Dépôt corrompu | `fatal: not a git repository`, objets manquants | Recloner puis copier les modifications de l'espace de travail | Sauvegarder d'abord l'espace de travail |

### 6.7 Restauration

Si un problème est constaté après le push, utiliser `git revert` pour générer un commit inverse ; il est interdit de recourir à nouveau à un push forcé pour écraser un historique déjà rendu public.

## Fichiers associés

- Avant le push, les trois niveaux de la [porte qualité](./quality-gate.md) doivent être franchis
- Les lignes rouges relatives aux secrets et aux gros fichiers figurent dans H3/H5/H12 des [règles absolues](./hard-rules.md)
- La spécification des messages de commit relève de la dimension D7, voir la [matrice des dimensions d'audit](./review-dimension-matrix.md)
- La responsabilité du document de publication `docs/release.md` figure dans la [matrice documentaire](./document-matrix.md)
