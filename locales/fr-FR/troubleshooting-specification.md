# Spécification de dépannage

> Problème que ce fichier résout : définir la structure de la documentation de dépannage (Troubleshooting / FAQ), les règles de rédaction des entrées et le mécanisme de maintenance, afin que les utilisateurs puissent localiser la cause à partir du symptôme et résoudre eux-mêmes les problèmes courants.

## 1. Cas d'application

La documentation de dépannage est obligatoire dans les situations suivantes :

1. L'échec d'installation ou de build présente plusieurs causes courantes.
2. Des options de configuration entrent en conflit et le message d'erreur ne suffit pas à indiquer la solution.
3. Une plateforme ou une version donnée présente des limitations connues.
4. Les utilisateurs posent de manière répétée la même question et la réponse peut être normalisée.

## 2. Emplacement et nommage des fichiers

1. Lorsque le contenu est limité, l'intégrer comme section du README, sous le titre « Questions fréquentes » ou « Dépannage ».
2. Lorsque le contenu est volumineux, créer un fichier distinct `docs/troubleshooting.md` ou `FAQ.md`, le README conservant un lien d'entrée.
3. Les problèmes sont regroupés par thème, par exemple « installation », « configuration », « exécution », « performances », « réseau ».

## 3. Structure du document

1. **Introduction** : périmètre des problèmes courants couverts et versions concernées.
2. **Index des problèmes** : liste des titres de problèmes par thème, avec navigation rapide.
3. **Entrées de problème** : développées une à une selon une structure unifiée.
4. **Toujours bloqué** : renvoi vers les canaux d'assistance tels que les issues et les espaces de discussion.

## 4. Structure d'une entrée

Chaque entrée de problème doit comporter les parties suivantes :

| Partie | Contenu | Exigence |
| --- | --- | --- |
| Symptôme | Manifestation concrète constatée par l'utilisateur | Inclure le message d'erreur complet, ne pas écrire seulement « erreur » |
| Condition de déclenchement | Quand le problème survient | Préciser la version, la plateforme et l'opération |
| Cause | Cause racine | Expliquer le mécanisme, ne pas se limiter à une conclusion |
| Solution | Étapes exécutables | Numérotées, avec commandes ou configuration |
| Vérification | Comment confirmer la correction | Indiquer la sortie attendue |
| Liens | Documentation ou issue associée | Facultatif |

## 5. Exemple de rédaction d'une entrée

```markdown
### Message `EACCES: permission denied` à l'installation

**Symptôme** : l'exécution de `npm install -g <package>` signale un manque de permissions.

**Condition de déclenchement** : installation d'un paquet global en tant qu'utilisateur ordinaire sous Linux ou macOS.

**Cause** : le droit d'écriture du répertoire d'installation globale appartient à l'administrateur système, l'utilisateur courant ne peut pas y écrire.

**Solution** :

```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
npm install -g <package>
```

**Vérification** : l'exécution de `<package> --version` affiche le numéro de version, ce qui indique un succès.

## 6. Exigences rédactionnelles

1. Le titre du problème reprend la formulation que l'utilisateur rechercherait, et non un terme interne.
2. Les messages d'erreur sont conservés tels quels, pour faciliter la comparaison par l'utilisateur ; les informations sensibles doivent être masquées (voir la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md)).
3. La solution fournit la commande complète, sans supposer que l'utilisateur a déjà défini des variables d'environnement.
4. Une entrée ne résout qu'un seul problème, sans fusionner plusieurs causes.
5. Lorsqu'un défaut connu est concerné, préciser le périmètre d'impact et la parade, sans promettre de délai de correction.
6. Les problèmes liés à une migration renvoient au guide de migration (voir la [spécification de guide de migration](./migration-guide-specification.md)).

## 7. Mécanisme de maintenance

1. Lorsqu'une même question est posée plus de trois fois, il faut ajouter ou réécrire une entrée.
2. Après une montée de version, réexaminer toutes les entrées et supprimer les contenus devenus obsolètes.
3. Chaque entrée peut indiquer la dernière version vérifiée, afin de juger de sa validité.
4. L'index des problèmes est mis à jour en même temps que les ajouts et suppressions d'entrées.

## 8. Pratiques interdites

1. Il est interdit de transformer la documentation de dépannage en présentation de fonctionnalités.
2. Il est interdit de se limiter à des réponses sans valeur diagnostique telles que « essayez de redémarrer ».
3. Il est interdit d'omettre le message d'erreur et la condition de déclenchement.
4. Il est interdit de conserver des entrées corrigées ou obsolètes.

## Fichiers associés

- Le rattachement de la section du README figure au chapitre 15 de la [spécification des sections de README](./readme-sections-specification.md)
- L'exigence de divulgation des problèmes connus figure au chapitre 15 de la [spécification des sections de README](./readme-sections-specification.md)
- Les problèmes liés à la mise à niveau figurent dans la [spécification de guide de migration](./migration-guide-specification.md)
- Les canaux de collecte des problèmes figurent dans la [spécification des gabarits d'Issue et de PR](./issue-and-pr-template-specification.md)
- La qualité documentaire relève de la dimension D12, voir la [matrice des dimensions d'audit](./review-dimension-matrix.md)
