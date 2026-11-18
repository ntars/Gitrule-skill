# Spécification des métadonnées lisibles par machine

> Problème que ce fichier résout : définir la structure d'un inventaire de métadonnées destiné à une consommation programmatique par les experts, les Skills, MCP, la ligne de commande, etc., afin de garantir une exploitation stable et découvrable par la machine.

## 1. Objectifs de conception

1. Identifiant stable : chaque document possède un identifiant unique et immuable, destiné à être référencé par un programme.
2. Indépendance vis-à-vis de la langue : l'identifiant ne varie pas selon la langue ; la langue n'apparaît que dans le chemin.
3. Découvrabilité : l'inventaire énumère, pour tous les documents, le type, le chemin, la langue et le résumé.

## 2. Structure de l'inventaire

L'inventaire machine (manifest) doit contenir :

| Champ | Exigence |
| --- | --- |
| id | identifiant unique et stable, en kebab-case minuscule, sans langue ni version |
| title | titre du document |
| summary | phrase unique précisant le problème résolu |
| domain | domaine d'appartenance (l'un des sept domaines) |
| paths | correspondance code de langue → chemin relatif, par exemple `zh-CN`: `./locales/zh-CN/角色与职责.md` |
| version | version de l'ensemble de spécifications |

## 3. Règles impératives

1. L'ajout d'une langue se limite à ajouter une correspondance dans `paths`, sans modifier `id` ni les chemins des autres langues.
2. Le renommage d'un document doit conserver `id` inchangé et ne mettre à jour que `paths`.
3. L'identifiant et le chemin doivent correspondre aux fichiers réels ; la CI valide la validité de l'inventaire.
4. La présente spécification fournit un exemple d'inventaire copiable ; le projet cible doit créer une instance d'inventaire réelle selon les champs de la section 2 et veiller à ce que `paths` corresponde aux fichiers sur disque.

## 4. Exemple d'inventaire (copiable)

L'exemple ci-dessous énumère trois entrées de documents. L'inventaire réel doit couvrir l'ensemble des spécifications du répertoire de langue cible ; `id` ne varie pas selon la langue et `paths` ajoute une correspondance par code de langue.

```json
{
  "version": "1.0.0",
  "entries": [
    {
      "id": "role-and-responsibility",
      "title": "角色与职责",
      "summary": "定义执行者身份、职责边界、触发条件、适用范围与硬性约束",
      "domain": "总纲与治理",
      "paths": {
        "zh-CN": "./locales/zh-CN/角色与职责.md"
      },
      "version": "1.0.0"
    },
    {
      "id": "readme-standard-template",
      "title": "README标准模板",
      "summary": "提供可直接套用的通用 README 模板与占位符对照表",
      "domain": "命名与文档",
      "paths": {
        "zh-CN": "./locales/zh-CN/README标准模板.md"
      },
      "version": "1.0.0"
    },
    {
      "id": "machine-readable-metadata",
      "title": "机器可读元数据规范",
      "summary": "定义供专家、Skill、MCP、命令行消费的元数据清单结构",
      "domain": "AI 与机器适配",
      "paths": {
        "zh-CN": "./locales/zh-CN/机器可读元数据规范.md"
      },
      "version": "1.0.0"
    }
  ]
}
```

Lors de l'ajout d'une langue, il convient d'ajouter uniquement une correspondance dans le `paths` de l'entrée concernée, par exemple `"en-US": "./locales/en-US/role-and-responsibility.md"` ; `id` ne doit pas être modifié.

## Fichiers associés

- La manière dont les Skills consomment les métadonnées est décrite dans la [spécification de rédaction des Skills](./skill-authoring-specification.md)
- La manière dont les outils MCP exposent les documents est décrite dans la [spécification des outils MCP](./mcp-tool-specification.md)
- Les conventions d'invocation des agents sont décrites dans la [spécification d'invocation des agents et de rédaction des prompts](./agent-invocation-and-prompt-specification.md)
