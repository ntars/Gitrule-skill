# Spécification de sécurité et de confidentialité

> Problème que ce fichier résout : définir la protection des informations sensibles, la liste des données personnelles, le gabarit SECURITY.md et les champs de signalement des vulnérabilités, afin de garantir l'absence de fuite avant publication, la conformité du traitement des données et l'accessibilité du canal de signalement des vulnérabilités.

## 1. Dispositions de la spécification

1. Il est interdit de committer des clés, des jetons, des clés privées, des fichiers `.env`, des AK/SK de fournisseur cloud ou des chaînes de connexion à une base de données (correspond à la règle absolue H3).
2. L'analyse des clés doit couvrir l'espace de travail et l'historique complet, et être exécutée avant le push (voir la [spécification de push et de publication](./push-and-release-specification.md)).
3. Les noms de domaine internes, les adresses IP, les données personnelles et les résidus dans les journaux doivent être nettoyés avant la publication (correspond à la dimension D1).
4. Dès qu'une clé a été poussée, il faut immédiatement la renouveler et nettoyer l'historique ; un commit de suppression seul est interdit (correspond à H12).
5. Préciser quelles données sont collectées, leur finalité, leur lieu de stockage et leur durée de conservation ; chiffrer le transport et le stockage, et masquer les données à l'affichage.
6. Le modèle de permissions suit le principe du minimum nécessaire ; les données faisant l'objet d'un transfert transfrontalier doivent faire l'objet d'une évaluation distincte.
7. Fournir un canal de signalement des vulnérabilités joignant directement les mainteneurs, en s'engageant sur la confidentialité et sur des délais de réponse ; décrire honnêtement les risques connus, sans promettre une sécurité absolue.

## 2. Gabarit d'auto-contrôle des informations sensibles

```markdown
# Auto-contrôle des informations sensibles : {{项目名称}}

Date de contrôle : {{YYYY-MM-DD}} ｜ Exécutant : {{姓名}} ｜ Historique couvert : {{是 / 否}}

| Point de contrôle | Outil / commande | Résultat | Traitement |
| --- | --- | --- | --- |
| Clés dans l'espace de travail | {{扫描工具}} | {{命中数}} | {{已清理 / 无}} |
| Clés dans les commits historiques | {{扫描工具 --all}} | {{命中数}} | {{已轮换 / 无}} |
| Fichiers `.env` et d'identifiants | `git ls-files \| grep -E ...` | {{文件数}} | {{已移除 / 无}} |
| Noms de domaine / IP internes | {{检索命令}} | {{命中数}} | {{已替换 / 无}} |
| Données personnelles | {{检索命令}} | {{命中数}} | {{已脱敏 / 无}} |
| Résidus dans les journaux et instantanés | {{检查命令}} | {{命中数}} | {{已清理 / 无}} |

Conclusion : {{通过 / 不通过}}
- Liste des clés renouvelées : {{无 / 列出}}
- Vérificateur : {{姓名}}
```

## 3. Gabarit de liste des données personnelles

```markdown
# Liste des données personnelles : {{项目名称}}

## Éléments de données
| Élément de données | Finalité de la collecte | Mode de collecte | Lieu de stockage | Durée de conservation | Chiffrement | Masquage | Partage avec des tiers |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{如邮箱}} | {{账号识别}} | {{用户填写}} | {{数据库字段}} | {{删除账号后 30 天}} | {{是}} | {{展示时掩码}} | {{无}} |

## Modèle de permissions
| Rôle | Données accessibles | Fondement de la permission | Période de revue |
| --- | --- | --- | --- |
| {{角色}} | {{最小必要范围}} | {{业务需要}} | {{每季度}} |

## Évaluation de conformité
- Réglementation applicable par région : {{列举}}
- Transfert transfrontalier de données : {{无 / 评估结论与措施}}
- Réponse aux droits des utilisateurs : {{查询 / 更正 / 删除的渠道与时限}}
```

## 4. Gabarit SECURITY.md

```markdown
# Politique de sécurité

## Versions prises en charge
| Version | Rapports de sécurité acceptés |
| --- | --- |
| {{最新主版本}} | Oui |
| {{旧版本}} | Non / Problèmes graves uniquement |

## Canal de signalement
- Préféré : {{私密渠道，如 GitHub Security Advisories}}
- De secours : {{加密邮箱}}
- Ne signalez pas les vulnérabilités via une issue publique.

## Engagements de réponse
| Étape | Délai |
| --- | --- |
| Accusé de réception | {{2 个工作日}} |
| Confirmation initiale | {{5 个工作日}} |
| Correction et divulgation | {{视严重程度，目标 30 天}} |

## Processus de traitement
Réception → Confirmation → Correction → Divulgation → Annonce

## Risques connus
{{如实说明当前已知风险；无则写「暂无已知风险」，不得承诺绝对安全}}
```

## 5. Définition des champs

| Champ | Obligatoire | Type | Points clés de saisie | Exemple |
| --- | --- | --- | --- | --- |
| Historique couvert | Oui | Énumération | « Oui » est indispensable pour prononcer un passage | `oui` |
| Point de contrôle.Résultat | Oui | Numérique | Indiquer le nombre d'occurrences, « probablement rien » est interdit | `0` |
| Liste des clés renouvelées | Obligatoire sous condition | Liste | Obligatoire en cas de détection de clé, énumérer les identifiants renouvelés | `API_KEY renouvelée` |
| Élément de données.Durée de conservation | Oui | Texte | Durée concrète, « long terme » est interdit | `30 jours après suppression du compte` |
| Élément de données.Partage avec des tiers | Oui | Texte | Écrire « aucun » s'il n'y en a pas | `aucun` |
| Versions prises en charge | Oui | Tableau | Préciser quelles versions acceptent les rapports | `2.x : oui` |
| Canal de signalement | Oui | Texte | Au moins un canal non public | `Security Advisories` |
| Délai de réponse | Oui | Durée | Une valeur numérique pour chaque étape | `2 jours ouvrés` |

## 6. Consignes de saisie

1. **Analyse de l'historique** : l'analyse des clés doit inclure l'historique git complet ; une analyse limitée à l'espace de travail est considérée comme invalide.
2. **Détection de clé** : dès qu'une clé déjà poussée est découverte, renouveler d'abord puis nettoyer l'historique, l'ordre ne doit pas être inversé (correspond à H12).
3. **Masquage** : les champs sensibles affichés ou présents dans les journaux doivent être masqués ; l'affichage complet de jetons, de numéros d'identité ou de numéros de téléphone est interdit.
4. **Durée de conservation** : « conservation à long terme » n'est pas acceptable ; il faut indiquer une durée précise ou l'événement déclenchant la suppression.
5. **Versions prises en charge** : indiquer au minimum la version majeure courante ; lorsque les anciennes versions ne sont pas prises en charge, l'écrire explicitement afin d'éviter les signalements erronés.
6. **Canal de signalement** : il doit être non public ; divulguer une vulnérabilité dans une issue publique élargit le risque.
7. **Risques connus** : les énumérer honnêtement ; « ce système est absolument sûr » constitue une formulation interdite.

Erreurs fréquentes :

| Formulation erronée | Problème | Correction |
| --- | --- | --- |
| Supprimer la clé par un commit sans la renouveler | Violation de H12 | Renouveler d'abord, puis nettoyer l'historique |
| Auto-contrôle limité à l'espace de travail | Fuite dans l'historique non détectée | Ajouter l'analyse de l'historique |
| Conservation des données écrite « permanente » | Sans limite | Indiquer une durée précise |
| Vulnérabilité signalée via une issue publique | Élargit la surface d'exposition | Passer à un canal privé et l'inscrire dans SECURITY.md |
| Promesse de « sécurité absolue » | Déclaration inexacte | Remplacer par une description honnête des risques connus |

## 7. Exemple complet

```markdown
## Auto-contrôle des informations sensibles : markdown-lint-cli

Date de contrôle : 2026-11-18 ｜ Exécutant : Wang Wu ｜ Historique couvert : oui

| Point de contrôle | Outil / commande | Résultat | Traitement |
| --- | --- | --- | --- |
| Clés dans l'espace de travail | gitleaks detect | 0 | aucun |
| Clés dans les commits historiques | gitleaks detect --log-opts=--all | 0 | aucun |
| Fichiers `.env` et d'identifiants | git ls-files | 0 | aucun |
| Noms de domaine / IP internes | recherche par expression régulière | 0 | aucun |

Conclusion : conforme
- Liste des clés renouvelées : aucune
- Vérificateur : Li Si
```

## Fichiers associés

- Lignes rouges relatives aux clés H3/H12 : [règles absolues](./hard-rules.md)
- Traitement d'incident en cas de fuite de clé : [spécification de réponse aux incidents](./incident-response-specification.md)
- Exécution de l'analyse avant push : [spécification de push et de publication](./push-and-release-specification.md)
- Masquage des journaux : [spécification d'observabilité](./observability-specification.md)
- Périmètre du document SECURITY : [matrice documentaire](./document-matrix.md)
- Formulation des risques connus dans le README : [spécification des sections de README](./readme-sections-specification.md)
- Règles de conduite communautaire : [spécification du code de conduite](./code-of-conduct-specification.md)
