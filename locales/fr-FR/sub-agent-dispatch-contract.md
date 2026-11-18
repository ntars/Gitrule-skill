# Contrat de délégation aux sous-agents

> Problème que ce fichier résout : définir les quatre éléments et les contraintes de collaboration qui doivent être explicités lors de la délégation d'une tâche à un sous-agent, afin de garantir des conclusions structurées, vérifiables et exemptes de dérive des règles.

## 1. Les quatre éléments de la délégation

Chaque délégation doit expliciter les quatre éléments suivants :

```text
TASK:    <tâche en une phrase>
INPUT:   <fichiers/contexte nécessaires, uniquement ce qui est utile>
OUTPUT:  <format structuré, tableau ou JSON, prose interdite>
FAIL:    <ce qu'il faut renvoyer en cas d'impossibilité, plutôt qu'inventer>
```

## 2. Contraintes

- Un sous-agent ne traite qu'une seule chose à la fois ; « écrire aussi le README au passage » est interdit.
- Un sous-agent peut uniquement lire et produire des propositions ; **l'écriture de fichiers et les opérations git sont exécutées exclusivement par l'orchestrateur**.
- Les conclusions d'un sous-agent doivent être accompagnées de preuves (chemin de fichier + numéro de ligne / sortie de commande) ; une conclusion sans preuve est considérée comme invalide.
- Les sous-agents ne communiquent pas directement entre eux ; tout passe par la synthèse de l'orchestrateur, afin d'éviter toute dérive des règles.

## Fichiers associés

- Les destinataires et les dimensions de la délégation sont décrits dans la [matrice des dimensions de revue](./review-dimension-matrix.md)
- La délégation de rédaction documentaire est décrite dans la [matrice documentaire](./document-matrix.md)
- La délégation intervient aux phases 2 et 4 du [processus d'exécution](./execution-process.md)
