# Spécification d'invocation des agents et de rédaction des prompts

> Problème que ce fichier résout : définir le contrat de délégation et la manière de rédiger les prompts lors de l'invocation d'un agent sur un ensemble de spécifications, afin de garantir des invocations vérifiables, sans dépassement de périmètre ni dérive.

## 1. Principes d'invocation

1. Responsabilité unique : une invocation ne réalise qu'une seule chose ; exécuter une autre tâche « au passage » est interdit.
2. Séparation lecture/écriture : le sous-agent se limite à la lecture et à l'analyse ; l'écriture de fichiers et les opérations git sont exécutées de manière centralisée par l'orchestrateur (voir le [contrat de délégation aux sous-agents](./sub-agent-dispatch-contract.md)).
3. Exigence de preuve : les conclusions doivent être accompagnées de preuves (chemin + numéro de ligne / sortie de commande) ; une conclusion sans preuve est considérée comme invalide.
4. Absence de communication : les sous-agents ne communiquent pas directement entre eux ; tout passe par la synthèse de l'orchestrateur.

## 2. Structure du prompt

Le prompt d'invocation doit contenir quatre éléments :

```text
TASK:    <tâche en une phrase>
INPUT:   <contexte nécessaire, uniquement ce qui est utile>
OUTPUT:  <format de sortie structuré, tableau ou JSON, prose interdite>
FAIL:    <convention de retour en cas d'impossibilité, aucune invention>
```

## 3. Rédaction du prompt

1. Employer la langue écrite et l'impératif, fournir une information complète et ne pas s'appuyer sur des déductions contextuelles (voir la [spécification générale de rédaction](./general-writing-specification.md)).
2. Expliciter le format de sortie et le retour en cas d'échec, afin d'éviter toute improvisation du modèle.
3. Lorsqu'une spécification est citée, indiquer le chemin du fichier (voir la [spécification des métadonnées lisibles par machine](./machine-readable-metadata-specification.md)).
4. Unifier le format des gabarits et des espaces réservés (voir la [collecte d'informations et gabarits](./information-collection-and-templates.md)).

## 4. Règles impératives

1. Il ne doit pas être demandé à l'agent d'inventer des résultats de vérification ; tout élément non vérifiable doit être marqué SKIP avec son motif.
2. Le processus de réflexion interne ne doit pas être consigné dans les livrables (voir les [pratiques interdites](./prohibited-practices.md)).
3. Les éléments liés à la sécurité sont traités conformément à la [spécification de sécurité et de confidentialité](./security-and-privacy-specification.md).

## Fichiers associés

- Contrat de délégation : voir le [contrat de délégation aux sous-agents](./sub-agent-dispatch-contract.md)
- Métadonnées machine : voir la [spécification des métadonnées lisibles par machine](./machine-readable-metadata-specification.md)
- Encapsulation des Skills : voir la [spécification de rédaction des Skills](./skill-authoring-specification.md)
- Outils MCP : voir la [spécification des outils MCP](./mcp-tool-specification.md)
