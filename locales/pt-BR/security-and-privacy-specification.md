# Especificação de segurança e privacidade

> Problema que este arquivo resolve: definir a proteção de informações sensíveis, o inventário de privacidade de dados, o modelo de SECURITY.md e os campos de notificação de vulnerabilidades, garantindo que não haja vazamento antes da publicação, que o tratamento de dados seja conforme e que o canal de vulnerabilidades seja acessível.

## 1. Artigos da especificação

1. Não deve ser feito commit de chaves, tokens, chaves privadas, `.env`, AK/SK de provedor de nuvem nem strings de conexão de banco de dados (corresponde à regra absoluta H3).
2. A varredura de chaves deve cobrir a área de trabalho e o histórico completo, e ser executada antes do push (ver a [especificação de push e publicação](./push-and-release-specification.md)).
3. Domínios internos, IPs, dados pessoais e resíduos em registros devem ser removidos antes da publicação (corresponde à dimensão D1).
4. Uma vez que uma chave já tenha sido enviada por push, deve-se rotacioná-la imediatamente e limpar o histórico, não devendo ser feito apenas um commit de exclusão (corresponde a H12).
5. Indicar quais dados são coletados, a finalidade, o local de armazenamento e o prazo de retenção; o transporte e o armazenamento devem ser criptografados, e a exibição deve ser anonimizada.
6. O modelo de permissões segue o princípio do mínimo necessário; casos que envolvam dados transfronteiriços devem ser avaliados separadamente.
7. Oferecer um canal de notificação de vulnerabilidades que chegue diretamente ao mantenedor, com compromisso de confidencialidade e prazo de resposta; riscos conhecidos devem ser descritos com veracidade, sem promessa de segurança absoluta.

## 2. Modelo de autoverificação de informações sensíveis

```markdown
# Autoverificação de informações sensíveis: {{项目名称}}

Data da verificação: {{YYYY-MM-DD}} ｜ Executor: {{姓名}} ｜ Histórico coberto: {{是 / 否}}

| Item de verificação | Ferramenta / comando | Resultado | Tratamento |
| --- | --- | --- | --- |
| Chaves na área de trabalho | {{扫描工具}} | {{命中数}} | {{已清理 / 无}} |
| Chaves em commits históricos | {{扫描工具 --all}} | {{命中数}} | {{已轮换 / 无}} |
| Arquivos `.env` e de credenciais | `git ls-files \| grep -E ...` | {{文件数}} | {{已移除 / 无}} |
| Domínios / IPs internos | {{检索命令}} | {{命中数}} | {{已替换 / 无}} |
| Dados pessoais | {{检索命令}} | {{命中数}} | {{已脱敏 / 无}} |
| Resíduos em registros e snapshots | {{检查命令}} | {{命中数}} | {{已清理 / 无}} |

Conclusão: {{通过 / 不通过}}
- Lista de chaves rotacionadas: {{无 / 列出}}
- Revisor: {{姓名}}
```

## 3. Modelo de inventário de privacidade de dados

```markdown
# Inventário de privacidade de dados: {{项目名称}}

## Itens de dados
| Item de dados | Finalidade da coleta | Forma de coleta | Local de armazenamento | Prazo de retenção | Criptografia | Anonimização | Compartilhamento com terceiros |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{如邮箱}} | {{账号识别}} | {{用户填写}} | {{数据库字段}} | {{删除账号后 30 天}} | {{是}} | {{展示时掩码}} | {{无}} |

## Modelo de permissões
| Papel | Dados acessíveis | Base da permissão | Periodicidade de revisão |
| --- | --- | --- | --- |
| {{角色}} | {{最小必要范围}} | {{业务需要}} | {{每季度}} |

## Avaliação de conformidade
- Legislação aplicável por região: {{列举}}
- Transferência transfronteiriça de dados: {{无 / 评估结论与措施}}
- Resposta aos direitos do usuário: {{查询 / 更正 / 删除的渠道与时限}}
```

## 4. Modelo de SECURITY.md

```markdown
# Política de segurança

## Versões com suporte
| Versão | Aceita relatórios de segurança |
| --- | --- |
| {{最新主版本}} | Sim |
| {{旧版本}} | Não / apenas problemas graves |

## Canal de notificação
- Preferencial: {{私密渠道，如 GitHub Security Advisories}}
- Alternativo: {{加密邮箱}}
- Não deve ser usado um Issue público para notificar vulnerabilidades.

## Compromissos de resposta
| Etapa | Prazo |
| --- | --- |
| Confirmação de recebimento | {{2 个工作日}} |
| Confirmação inicial | {{5 个工作日}} |
| Correção e divulgação | {{视严重程度，目标 30 天}} |

## Fluxo de tratamento
Recebimento → confirmação → correção → divulgação → comunicado

## Riscos conhecidos
{{如实说明当前已知风险；无则写「暂无已知风险」，不得承诺绝对安全}}
```

## 5. Definição dos campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Histórico coberto | Sim | Enumeração | Deve ser “sim” para que o item seja aprovado | `是` |
| Item de verificação.Resultado | Sim | Numérico | Preencher o número de ocorrências; é proibido escrever “provavelmente não há” | `0` |
| Lista de chaves rotacionadas | Condicionalmente obrigatório | Lista | Obrigatório quando houver chaves encontradas; listar as credenciais rotacionadas | `API_KEY 已轮换` |
| Item de dados.Prazo de retenção | Sim | Texto | Duração concreta; não se admite “longo prazo” | `账号删除后 30 天` |
| Item de dados.Compartilhamento com terceiros | Sim | Texto | Se não houver, escrever “nenhum” | `无` |
| Versões com suporte | Sim | Tabela | Indicar claramente quais versões aceitam relatórios | `2.x：是` |
| Canal de notificação | Sim | Texto | Pelo menos um canal não público | `Security Advisories` |
| Prazo de resposta | Sim | Duração | Valor numérico em cada etapa | `2 个工作日` |

## 6. Instruções de preenchimento

1. **Varredura do histórico**: a varredura de chaves deve incluir todo o histórico do git; varrer apenas a área de trabalho é considerado inválido.
2. **Chaves encontradas**: ao detectar uma chave já enviada por push, rotacionar primeiro e só depois limpar o histórico; a ordem não deve ser invertida (corresponde a H12).
3. **Anonimização**: campos sensíveis exibidos na interface e nos registros devem ser mascarados; é proibido imprimir tokens, documentos de identidade e números de telefone por inteiro.
4. **Prazo de retenção**: “retenção permanente” é reprovado; deve-se indicar um prazo explícito ou um evento que dispare a exclusão.
5. **Versões com suporte**: listar no mínimo a versão principal atual; quando versões antigas não tiverem suporte, isso deve ser explicitado, para evitar relatórios indevidos.
6. **Canal de notificação**: deve ser um canal não público; divulgar vulnerabilidades em Issue público amplia o risco.
7. **Riscos conhecidos**: listar com veracidade; “este sistema é absolutamente seguro” é uma expressão proibida.

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| Apenas excluir a chave no commit, sem rotacionar | Viola H12 | Rotacionar primeiro e depois limpar o histórico |
| Autoverificação que varre apenas a área de trabalho | Vazamentos no histórico passam despercebidos | Incluir a varredura do histórico |
| Retenção de dados escrita como “permanente” | Sem limite | Indicar prazo concreto |
| Vulnerabilidade notificada por Issue público | Amplia a superfície de exposição | Usar canal privado e registrá-lo no SECURITY.md |
| Prometer “segurança absoluta” | Afirmação inverídica | Descrever com veracidade os riscos conhecidos |

## 7. Exemplo completo

```markdown
## Autoverificação de informações sensíveis: markdown-lint-cli

Data da verificação: 2026-11-18 ｜ Executor: Wang Wu ｜ Histórico coberto: sim

| Item de verificação | Ferramenta / comando | Resultado | Tratamento |
| --- | --- | --- | --- |
| Chaves na área de trabalho | gitleaks detect | 0 | Nenhuma |
| Chaves em commits históricos | gitleaks detect --log-opts=--all | 0 | Nenhuma |
| Arquivos `.env` e de credenciais | git ls-files | 0 | Nenhum |
| Domínios / IPs internos | busca por expressão regular | 0 | Nenhum |

Conclusão: aprovado
- Lista de chaves rotacionadas: nenhuma
- Revisor: Li Si
```

## Arquivos relacionados

- Linhas vermelhas de chaves H3/H12: [regras absolutas](./hard-rules.md)
- Tratamento de incidentes com chaves vazadas: [especificação de resposta a incidentes](./incident-response-specification.md)
- Execução da varredura antes do push: [especificação de push e publicação](./push-and-release-specification.md)
- Anonimização de registros: [especificação de observabilidade](./observability-specification.md)
- Limites da documentação de SECURITY: [matriz de documentação](./document-matrix.md)
- Redação de riscos conhecidos no README: [especificação de seções do README](./readme-sections-specification.md)
- Convenções de conduta da comunidade: [especificação de código de conduta](./code-of-conduct-specification.md)
