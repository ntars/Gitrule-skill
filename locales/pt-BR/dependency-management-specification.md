# Especificação de gerenciamento de dependências

> Problema que este arquivo resolve: definir os modelos e campos de solicitação de inclusão de dependência, inventário de dependências, bloqueio e atualização, garantindo build reproduzível, dependências rastreáveis e conformidade de licenças.

## 1. Dispositivos normativos

1. A inclusão de uma nova dependência deve justificar a finalidade, a licença e o estado de manutenção (ver [especificação de conformidade de código aberto](./open-source-compliance-specification.md)).
2. Deve-se dar preferência a dependências com licença compatível e comunidade ativa; é proibido incluir dependências de origem desconhecida ou licença indefinida.
3. A versão da dependência deve ser gravada no lockfile e commitada no repositório, garantindo build reproduzível em ambiente limpo (correspondente à regra absoluta H9 e à dimensão D5).
4. O número de versão deve bloquear a versão efetivamente resolvida, sem usar expressões de intervalo como entrega final.
5. A atualização de dependências deve contar com o auxílio de ferramentas automatizadas e, após a atualização, deve passar pela CI; vulnerabilidades devem ser tratadas com prontidão ou ter medidas de mitigação registradas.
6. O inventário de dependências deve permanecer coerente com o NOTICE (ver [especificação de NOTICE](./notice-specification.md)).

## 2. Modelo de solicitação de inclusão de dependência

```markdown
## Solicitação de inclusão de dependência: {{包名}}

- Número da solicitação: {{DEP-NNN}}
- Solicitante: {{姓名}}
- Finalidade: {{一句话说明解决什么问题}}
- Possível implementar internamente: {{是 / 否；是则说明为何仍引入}}
- Avaliação de alternativas: {{已评估的替代包及未选原因}}

| Campo | Valor |
| --- | --- |
| Nome do pacote | {{包名}} |
| Versão incluída | {{精确版本号}} |
| Licença | {{SPDX ID}} |
| Compatibilidade de licença | {{兼容 / 不兼容 / 需法务确认}} |
| Data da última publicação | {{YYYY-MM-DD}} |
| Estado de manutenção | {{活跃 / 低频 / 停滞}} |
| Downloads semanais | {{数值}} |
| Número de dependências transitivas | {{数值}} |
| Vulnerabilidades conhecidas | {{无 / CVE 编号与处置}} |
| Impacto no tamanho do pacote | {{增量 KB}} |

- Conclusão: {{批准 / 拒绝 / 有条件批准}}
- Aprovador: {{姓名}}
```

## 3. Modelo de inventário de dependências

```markdown
# Inventário de dependências: {{项目名称}}

Data de atualização: {{YYYY-MM-DD}} ｜ lockfile: {{路径}} ｜ Ferramenta de geração: {{工具与版本}}

| Dependência | Versão incluída | Versão bloqueada | Tipo | Licença | Finalidade | Última revisão |
| --- | --- | --- | --- | --- | --- | --- |
| {{包名}} | {{^1.2.0}} | {{1.2.3}} | Direta / Indireta | {{MIT}} | {{用途}} | {{YYYY-MM-DD}} |

## Registro de atualizações
| Data | Dependência | Mudança de versão | Motivo | Resultado da verificação |
| --- | --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{包名}} | {{1.2.2 → 1.2.3}} | {{安全修复}} | {{CI 全绿}} |

## Exceções e mitigação
| Dependência | Problema | Medida de mitigação | Data de revisão |
| --- | --- | --- | --- |
| {{包名}} | {{漏洞 / 停滞}} | {{限制使用范围}} | {{YYYY-MM-DD}} |
```

## 4. Definição dos campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Número da solicitação | Sim | `DEP-NNN` | Sequencial, sem reutilização | `DEP-007` |
| Finalidade | Sim | Texto | Explicar o problema resolvido; proibido “facilitar o desenvolvimento” | `Analisar a configuração TOML` |
| Avaliação de alternativas | Sim | Texto | Avaliar ao menos 1 alternativa | `Avaliou-se o toml-js, descartado por manutenção estagnada` |
| Versão incluída | Sim | Versão exata | Não usar `^` nem `~` | `1.2.3` |
| Versão bloqueada | Sim | Versão exata | Coerente com o lockfile | `1.2.3` |
| Licença | Sim | SPDX ID | Coerente com a grafia da [especificação de LICENSE](./license-specification.md) | `MIT` |
| Estado de manutenção | Sim | Enumeração | Ativa / baixa frequência / estagnada, com a base da classificação | `Ativa (commits nos últimos 30 dias)` |
| Número de dependências transitivas | Sim | Número | Em excesso, explicar impacto de tamanho e risco | `12` |
| Vulnerabilidades conhecidas | Sim | Texto | Escrever “nenhuma” quando não houver; não deixar em branco | `Nenhuma` |
| Data de revisão | Sim | Data | Itens de exceção exigem data de revisão | `2026-12-31` |

## 5. Instruções de preenchimento

1. **Avaliação de implementação interna**: primeiro responder “é possível implementar com a biblioteca padrão ou com capacidade existente”; se for possível e ainda assim se optar por incluir a dependência, o motivo deve ser justificado.
2. **Licença**: deve ser um SPDX ID; `UNLICENSED` e licenças personalizadas devem ser convertidas em “requer confirmação jurídica” e não devem ser incluídas diretamente.
3. **Estado de manutenção**: basear-se na data da última publicação e na resposta a issues; é proibido “parece que alguém mantém”.
4. **Bloqueio de versão**: na entrega, o lockfile deve conter a versão exata resolvida; o `package.json` pode manter expressões de intervalo, mas o lockfile deve ser exato.
5. **Ritmo de atualização**: ativar a atualização automatizada e confirmar manualmente o merge; cada atualização deve passar pela CI e verificar mudanças de licença.
6. **Tratamento de vulnerabilidades**: priorizar a atualização para uma versão segura; quando não for possível atualizar, registrar a medida de mitigação e a data de revisão e incluí-las no registro de riscos da [especificação de resposta a incidentes](./incident-response-specification.md).
7. **Sincronia do inventário**: após incluir ou remover dependências, atualizar simultaneamente o inventário e o NOTICE; os três (lockfile, inventário e NOTICE) devem estar coerentes.

Erros comuns:

| Escrita incorreta | Problema | Forma de correção |
| --- | --- | --- |
| “Usar uma biblioteca para tratar a configuração” | Sem nome de pacote nem finalidade | Escrever nome do pacote, versão e problema resolvido |
| Licença escrita como “código aberto” | Impossível julgar a compatibilidade | Escrever o SPDX ID |
| Lockfile não commitado | Build não reproduzível | Commitar o lockfile (correspondente a H9) |
| Número de dependências transitivas em branco | Risco invisível | Preencher o valor concreto |
| Vulnerabilidade sem medida de mitigação | Risco não acompanhado | Acrescentar medida e data de revisão |

## 6. Exemplo completo

```markdown
## Solicitação de inclusão de dependência: remark

- Número da solicitação: DEP-001
- Solicitante: Wang Wu
- Finalidade: atuar como camada de análise de Markdown, sustentando a necessidade de localização de nós do mecanismo de regras (REQ-001, REQ-004).
- Possível implementar internamente: não; uma implementação interna não cobriria os casos de fronteira do GFM dentro do limite de esforço disponível.
- Avaliação de alternativas: avaliou-se o marked, não escolhido por capacidade insuficiente de localização de nós em chinês.

| Campo | Valor |
| --- | --- |
| Nome do pacote | remark |
| Versão incluída | 15.0.1 |
| Licença | MIT |
| Compatibilidade de licença | Compatível |
| Data da última publicação | 2026-11-02 |
| Estado de manutenção | Ativa (commits nos últimos 30 dias) |
| Downloads semanais | 4,200,000 |
| Número de dependências transitivas | 18 |
| Vulnerabilidades conhecidas | Nenhuma |
| Impacto no tamanho do pacote | +42 KB |

- Conclusão: aprovado, a ser implementado junto com o ADR-0002
- Aprovador: Li Si
```

## Arquivos relacionados

- Julgamento de compatibilidade de licença: [especificação de conformidade de código aberto](./open-source-compliance-specification.md)
- Marcação SPDX de licença: [especificação de LICENSE](./license-specification.md)
- Coerência do NOTICE: [especificação de NOTICE](./notice-specification.md)
- Build reproduzível pertence à dimensão D5: [matriz de dimensões de auditoria](./review-dimension-matrix.md)
- Atualização automatizada pertence à dimensão D9: [matriz de dimensões de auditoria](./review-dimension-matrix.md)
- Testes e tratamento de vulnerabilidades: [especificação de testes](./testing-specification.md), [especificação de segurança e privacidade](./security-and-privacy-specification.md)
- Relação com decisões de arquitetura: [especificação de documento de projeto de arquitetura](./architecture-design-document-specification.md)
