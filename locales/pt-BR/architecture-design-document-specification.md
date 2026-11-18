# Especificação de documento de design de arquitetura

> Problema que este arquivo resolve: definir o modelo, os campos e a forma de redação do documento de arquitetura e do registro de decisão de arquitetura (ADR), descrevendo as fronteiras do sistema, as responsabilidades dos módulos, os atributos de qualidade e as decisões de compromisso relevantes, além de garantir a rastreabilidade das decisões.

## 1. Disposições normativas

1. O documento de arquitetura (`docs/architecture.md`) descreve apenas a estrutura e as fronteiras, sem exemplos de uso; as fronteiras de responsabilidade estão na [matriz de documentação](./document-matrix.md).
2. Cada decisão técnica relevante deve ter um ADR correspondente; uma decisão sem ADR é considerada uma decisão não registrada.
3. A numeração dos ADRs é contínua e permanentemente fixa; uma vez adotado, o histórico não é reescrito, e as mudanças de estado são registradas em um novo ADR com a marcação “substituído”.
4. A descrição da arquitetura deve ser coerente com a implementação do código; em caso de divergência entre código e documentação, prevalece o código e a documentação deve ser corrigida imediatamente.
5. Cada decisão de arquitetura deve poder ser rastreada até um ou mais requisitos; a relação de rastreamento está na [especificação de matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md).
6. Os atributos de qualidade devem apresentar metas mensuráveis e verificáveis; é proibido escrever apenas “alto desempenho” ou “alta disponibilidade”.

## 2. Modelo de documento de arquitetura

```markdown
# Design de arquitetura: {{项目名称}}

Versão do documento: {{v1.0}} ｜ Versão de código correspondente: {{tag}} ｜ Data da última verificação: {{YYYY-MM-DD}}

## Contexto do sistema
- Responsabilidade do sistema: {{一句话说明系统边界内的责任}}
- Atores externos: {{用户、上游系统、下游系统}}
- Entradas e saídas: {{进入系统的请求与系统产出的结果}}
- Fora das fronteiras: {{明确不由本系统承担的职责}}

## Divisão de módulos
| Módulo | Responsabilidade exclusiva | Interface externa | Módulos dos quais depende | Não é responsável por |
| --- | --- | --- | --- | --- |
| {{模块名}} | {{仅一件事}} | {{接口名}} | {{模块名}} | {{明确排除}} |

## Fluxo de dados crítico
1. {{触发点}} → {{模块 A}}: {{传递的数据}}
2. {{模块 A}} → {{模块 B}}: {{转换与传递}}
3. {{模块 B}} → {{结果}}: {{最终产出}}

## Escolhas tecnológicas
| Domínio | Escolha | Alternativas | Base da decisão | ADR |
| --- | --- | --- | --- | --- |
| {{语言 / 框架 / 存储}} | {{采用项}} | {{未采用项}} | {{取舍理由}} | {{ADR-000N}} |

## Atributos de qualidade
| Atributo | Valor-alvo | Forma de verificação | ADR relacionado |
| --- | --- | --- | --- |
| Desempenho | {{P95 延迟 < X ms}} | {{压测方式}} | {{ADR-000N}} |
| Disponibilidade | {{月度可用性 ≥ X%}} | {{监控统计}} | {{ADR-000N}} |
| Segurança | {{敏感数据零明文落盘}} | {{审计方式}} | {{ADR-000N}} |
| Escalabilidade | {{横向扩容至 N 节点无需改代码}} | {{扩容演练}} | {{ADR-000N}} |

## Restrições e decisões de compromisso
- Restrições técnicas: {{语言版本、平台、兼容性}}
- Soluções abandonadas e motivos: {{方案 A：原因}}
- Dívida técnica conhecida: {{债务项与偿还条件}}
```

## 3. Modelo de ADR

```markdown
# ADR-{{四位序号}}: {{决策标题}}

- Estado: {{提议 / 已采纳 / 已废弃 / 被 ADR-000N 替代}}
- Data: {{YYYY-MM-DD}}
- Responsável pela decisão: {{姓名}}
- Requisitos relacionados: {{REQ-001 / …}}

## Contexto
{{面临的客观问题与约束，须可验证，不写主观偏好}}

## Decisão
{{采用的方案，一句话陈述，须明确到可执行的程度}}

## Alternativas
| Solução | Vantagens | Desvantagens | Motivo da não adoção |
| --- | --- | --- | --- |
| {{方案 A}} | | | |
| {{方案 B（采用）}} | | | — |

## Consequências
- Positivas: {{获得的能力}}
- Negativas: {{引入的成本或限制}}
- Tarefas seguintes: {{需要跟进的事项}}

## Arquivos relacionados
- {{架构文档中受影响的章节}}
- {{替代或被引用的 ADR}}
```

## 4. Definição de campos

### 4.1 Campos do documento de arquitetura

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Versão de código correspondente | Sim | tag | Coerente com a tag da [especificação de gestão de versões](./version-management-specification.md) | `v1.2.0` |
| Data da última verificação | Sim | data | Deve ser atualizada após cada alteração de código | `2026-11-18` |
| Responsabilidade exclusiva do módulo | Sim | texto | Um módulo descreve apenas uma coisa | `Analisar e validar regras de Markdown` |
| Não é responsável por | Sim | texto | Delimitar a fronteira e evitar desvio de responsabilidade | `Não é responsável pela reescrita de texto` |
| Base da decisão em escolhas tecnológicas | Sim | texto | Deve citar o número do ADR | `Ver ADR-0002` |
| Valor-alvo de atributo de qualidade | Sim | métrica | Com unidade e limite, verificável | `P95 < 150ms` |
| Dívida técnica conhecida | Não | lista | Indicar a condição de disparo da quitação | `Substituir o analisador na v2` |

### 4.2 Campos do ADR

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Número | Sim | `ADR-NNNN` | Número de quatro dígitos, contínuo e permanentemente fixo | `ADR-0002` |
| Estado | Sim | enumeração | Proposto / Adotado / Descartado / Substituído | `Adotado` |
| Requisitos relacionados | Sim | lista | Números REQ do documento de iniciação correspondente | `REQ-001` |
| Contexto | Sim | texto | Expor restrições objetivas; proibido “eu acho” | `Requer compatibilidade com Node 18` |
| Decisão | Sim | texto | Uma frase, executável | `Adotar remark como analisador` |
| Alternativas | Sim | tabela | Conter ao menos 1 solução não adotada | Ver modelo |
| Motivo da rejeição | Sim | texto | Deve ser indicado para cada solução não adotada | Ver modelo |
| Consequências | Sim | lista | Itens positivos, negativos e tarefas seguintes completos | Ver modelo |

## 5. Instruções de preenchimento

1. **Divisão de módulos**: se a “responsabilidade exclusiva” de uma linha contiver duas coisas ligadas por “e” ou “bem como”, ela deveria ser dividida em dois módulos.
2. **Fluxo de dados**: numerar em ordem cronológica e indicar o conteúdo dos dados transmitidos; é proibido escrever apenas setas com nomes de módulos.
3. **Atributos de qualidade**: cada item deve ter valor-alvo, forma de verificação e referência a ADR; a ausência de qualquer um deles torna o item incompleto.
4. **Contexto do ADR**: descrever o problema e as restrições, não a decisão em si; a decisão aparece uma única vez na seção “Decisão”.
5. **Alternativas**: mesmo havendo uma única solução, deve-se registrar “considerou-se a implementação própria, não adotada por custo de manutenção elevado”; a ausência de alternativas indica argumentação insuficiente.
6. **Mudança de estado**: não alterar o corpo do ADR original; criar um novo ADR e mudar o estado do original para “substituído pelo ADR-000N”.
7. **Dívida técnica**: deve indicar a condição de disparo da quitação; é proibido listar apenas o fenômeno.

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| Exemplos de chamada de API no documento de arquitetura | Sobreposição com a [especificação de documentação de API](./api-documentation-specification.md) | Mover para a documentação de API e manter apenas os nomes de interface na arquitetura |
| “O sistema precisa de alto desempenho” | Sem limite, não verificável | Indicar a meta de latência P95 e a forma de teste de carga |
| ADR apenas com a decisão, sem alternativas | Não argumentado | Acrescentar ao menos 1 solução não adotada e o motivo |
| Alterar o corpo de um ADR já adotado | Histórico reescrito | Criar um novo ADR indicando a relação de substituição |
| Decisão sem vínculo com requisitos | Cadeia de rastreamento rompida | Acrescentar o número REQ relacionado |

## 6. Exemplo completo

```markdown
# ADR-0002: adotar remark como camada de análise de Markdown

- Estado: adotado
- Data: 2026-11-18
- Responsável pela decisão: Li Si
- Requisitos relacionados: REQ-001 e REQ-004

## Contexto
É necessário oferecer suporte a GFM e à localização de nós de texto em chinês, e as dependências de runtime devem ser compatíveis com Node 18; o limite de esforço da equipe para manter um analisador é de 0.5 pessoa-mês por trimestre.

## Decisão
Adotar o ecossistema remark como única camada de análise de Markdown, com as regras implementadas na forma de plugins.

## Alternativas
| Solução | Vantagens | Desvantagens | Motivo da não adoção |
| --- | --- | --- | --- |
| Analisador próprio | Controle total | Exige manutenção de casos de borda a longo prazo | Excede o limite de esforço |
| marked | Leve | Capacidade fraca de localização de nós em chinês | Não atende ao REQ-004 |

## Consequências
- Positivas: a compatibilidade com GFM é mantida pela upstream e a localização de nós atende aos critérios de aceitação.
- Negativas: mudanças na API de plugins exigem acompanhamento da versão upstream.
- Tarefas seguintes: fixar a versão principal do remark na CI e assinar as notificações de release da ferramenta.
```

## Arquivos relacionados

- Fronteiras de responsabilidade e conteúdo proibido: [matriz de documentação](./document-matrix.md)
- Rastreamento reverso da decisão para o requisito: [especificação de matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md)
- Redação externa das decisões de engenharia: [como escrever funcionalidades e decisões de engenharia](./features-and-engineering-tradeoffs-guide.md)
- Convenções de design de interface: [especificação de design de API](./api-design-specification.md)
- Modelo de dados e migração: [especificação de design de banco de dados](./database-design-specification.md)
- Uniformização de termos: [glossário](./glossary.md)
