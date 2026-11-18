# Especificação de iniciação do projeto e requisitos

> Problema que este arquivo resolve: definir modelos e campos para a declaração de objetivos, a coleta de requisitos e a delimitação de escopo na fase de iniciação do projeto, assegurando que o projeto tenha, desde o início, uma base clara, verificável e rastreável.

## 1. Dispositivos normativos

1. O documento de iniciação do projeto deve responder a seis perguntas: o que é, por que fazer, até que ponto fazer, para quem não serve, quem usa e sob quais restrições.
2. Os requisitos devem ser classificados em três níveis, “obrigatório / recomendado / opcional”; as convenções de redação estão na [especificação geral de redação](./general-writing-specification.md).
3. Cada requisito deve ser verificável: apresentar critérios de aceite no formato Given/When/Then ou um limiar de métrica julgável.
4. Cada requisito deve ter numeração estável e origem definida; é vedado manter itens de requisito sem numeração.
5. Quando as informações forem insuficientes, marcar “【A confirmar: nome do campo】”; é vedado preencher por suposição; as regras estão em [coleta de informações e modelos](./information-collection-and-templates.md).
6. O escopo deve indicar simultaneamente os itens incluídos e os excluídos; não objetivos vazios significam escopo não delimitado.
7. Alterações de escopo devem registrar motivo, impacto e responsável pela decisão, e entrar no registro de alterações da [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md).

## 2. Modelo de documento de iniciação do projeto

```markdown
# Documento de iniciação do projeto: {{项目名称}}

Versão do documento: {{v0.1}} ｜ Estado: {{草稿 / 评审中 / 已批准}} ｜ Responsável pela decisão: {{姓名}} ｜ Data: {{YYYY-MM-DD}}

## Posicionamento em uma frase
Oferecer a {{目标用户}} {{核心能力}}, resolvendo {{当前痛点}}.
(≤60 caracteres; são vedados modificadores autoelogiosos como “poderoso”, “elegante” e “líder”)

## Contexto e motivação
- Situação atual: {{当前如何运作}}
- Limitações das soluções existentes: {{具体缺陷 1}}; {{具体缺陷 2}}
- Janela de oportunidade: {{时机、技术或市场变化}}
- Base da iniciação: {{工单号 / 访谈记录 / 数据指标，须可溯源}}

## Objetivos e não objetivos
| Tipo | Item | Resultado verificável |
| --- | --- | --- |
| Objetivo G1 | {{要达成的结果}} | {{可量化指标 + 阈值}} |
| Objetivo G2 | {{要达成的结果}} | {{可量化指标 + 阈值}} |
| Não objetivo N1 | {{明确不做的事}} | {{判定边界，说明为何排除}} |

## Critérios de sucesso
| Métrica | Linha de base | Valor-alvo | Forma de verificação | Momento de verificação |
| --- | --- | --- | --- | --- |
| {{指标名}} | {{当前值}} | {{目标值}} | {{如何测量}} | {{何时测量}} |

## Usuários-alvo
| Perfil de usuário | Cenário típico | Necessidade central | Alternativa atual |
| --- | --- | --- | --- |
| {{角色}} | {{何时何地}} | {{要完成的任务}} | {{现用方案}} |

## Restrições
- Técnicas: {{语言、平台、兼容性等限制}}
- De prazo: {{截止日期或窗口}}
- De recursos: {{人力、预算、基础设施}}
- De conformidade: {{许可证、隐私、行业规范}}

## Escopo
- Incluído: {{本期交付项}}
- Excluído: {{本期明确不交付项}}
- A confirmar: {{【待确认：字段名】}}

## Registro de decisões
| Data | Decisão | Responsável pela decisão | Base |
| --- | --- | --- | --- |
```

## 3. Modelo de item de requisito

```markdown
### REQ-{{三位序号}}: {{需求标题}}

- Origem: {{工单号 / 访谈 / 竞品 / 推测}}
- Prioridade: {{必须 / 应当 / 可以}}
- Objetivo associado: {{G1 / G2 / …}}
- História de usuário: como {{角色}}, quero {{行为}} para que {{价值}}
- Critérios de aceite:
  1. Given {{前置条件}}
     When {{操作}}
     Then {{预期结果}}
  2. Given {{边界或异常前置条件}}
     When {{操作}}
     Then {{预期结果}}
- Estado: {{待确认 / 已确认 / 已实现 / 已验证 / 已废弃}}
- Rastreamento associado: {{见需求追踪矩阵中的需求 ID}}
```

## 4. Definição de campos

### 4.1 Campos do documento de iniciação

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Versão do documento | Sim | Texto | Versionamento semântico ou versão por data | `v0.1` |
| Estado | Sim | Enumeração | Rascunho / Em revisão / Aprovado | `评审中` |
| Responsável pela decisão | Sim | Texto | Pessoa com poder de decisão final sobre escopo e prioridade | `Zhang San` |
| Posicionamento em uma frase | Sim | Texto | Usuário-alvo + capacidade central + dor, ≤60 caracteres | Oferecer aos desenvolvedores front-end… |
| Base da iniciação | Sim | Texto | Pelo menos um registro rastreável; “decisão da equipe” é vedado | `ISSUE-142` |
| Objetivos / Não objetivos | Sim | Tabela | Cada objetivo com resultado verificável; pelo menos um não objetivo | `G1：冷启动 <2s` |
| Critérios de sucesso | Sim | Tabela | A métrica deve ter linha de base, limiar, forma e momento de medição | `错误率 <0.1%` |
| Restrições | Sim | Lista | As quatro categorias devem ser preenchidas; sem restrição, escrever “nenhuma” | `须兼容 Node 18+` |
| A confirmar | Não | Lista | Usar apenas o formato 【A confirmar: nome do campo】 | `【待确认：预算上限】` |

### 4.2 Campos do item de requisito

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| Numeração | Sim | `REQ-NNN` | Número de três dígitos, contínuo, sem reutilização nem reordenação | `REQ-007` |
| Origem | Sim | Texto | Rastreável até o registro concreto | `用户访谈 #3` |
| Prioridade | Sim | Enumeração | Obrigatório / Recomendado / Opcional | `必须` |
| Objetivo associado | Sim | Lista | Número G correspondente no documento de iniciação | `G1` |
| História de usuário | Sim | Texto | Os três elementos — perfil, comportamento e valor — completos | Como… quero… para que… |
| Critérios de aceite | Sim | Lista | Pelo menos 1 conjunto Given/When/Then, com limite ou exceção | ver modelo |
| Estado | Sim | Enumeração | Um dos cinco estados, apenas avançando, sem retroceder | `已确认` |

## 5. Instruções de preenchimento

1. **Posicionamento em uma frase**: escrever na estrutura de três partes “para quem + o que oferece + o que resolve”; se a frase deixa de fazer sentido ao remover os modificadores, faltam informações substanciais.
2. **Critérios de sucesso**: cada item deve ter simultaneamente linha de base e limiar. “Melhorar o desempenho” e “melhor experiência” são considerados inaceitáveis e devem ser reescritos como “tempo de inicialização P95 de 3s para <1.5s”.
3. **Não objetivos**: indicar o escopo explicitamente excluído e a fronteira de julgamento, não “veremos depois”; sem não objetivos não vazios, considera-se o escopo não delimitado.
4. **Numeração de requisitos**: uma vez atribuída, é fixa para sempre; ao tornar um requisito obsoleto, o estado muda para “Obsoleto” e a numeração não pode ser recuperada nem reutilizada.
5. **Critérios de aceite**: devem cobrir o caminho normal e pelo menos um caminho de limite ou exceção; condições sem julgamento objetivo (como “interface bonita”) devem ser convertidas em métricas ou itens de verificação verificáveis.
6. **Itens a confirmar**: a iniciação admite itens a confirmar, mas eles devem ser listados integralmente com um responsável pela confirmação indicado; antes do início do desenvolvimento devem ser zerados.

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| “Fazer uma ferramenta fácil de usar” | Sem usuário-alvo, sem resultado verificável | Acrescentar perfil de usuário e métrica com limiar |
| Não objetivos escritos como “nenhum” | Escopo não delimitado, sujeito a expansão | Listar os itens explicitamente excluídos neste ciclo |
| Requisito sem numeração, descrito direto no texto | Impossível rastrear e referenciar | Atribuir `REQ-NNN` e referenciar em todo o escopo |
| Critério de aceite escrito como “funciona normalmente” | Não julgável | Dividir em Given/When/Then |
| Conteúdo suposto tratado como requisito estabelecido | Origem não rastreável | Marcar a origem como “suposição” e converter em item a confirmar |

## 6. Exemplo completo

```markdown
# Documento de iniciação do projeto: markdown-lint-cli

Versão do documento: v0.1 ｜ Estado: Em revisão ｜ Responsável pela decisão: Li Si ｜ Data: 2026-11-18

## Posicionamento em uma frase
Fornecer aos redatores técnicos de chinês uma ferramenta de linha de comando para verificação de normas Markdown, resolvendo a inconsistência de estilo entre vários repositórios sem validação automática.

## Contexto e motivação
- Situação atual: os README de 12 repositórios são escritos manualmente por cada mantenedor, com estilos não uniformes.
- Limitações das soluções existentes: ferramentas genéricas de lint em inglês não suportam regras de espaçamento entre chinês e inglês; a revisão manual leva em média 25 minutos por documento.
- Janela de oportunidade: a equipe está unificando as páginas iniciais open source e precisa aplicar a norma de uma só vez.
- Base da iniciação: ata da reunião de revisão de documentação de 2026-11-10 com os mantenedores (ISSUE-142).

## Objetivos e não objetivos
| Tipo | Item | Resultado verificável |
| --- | --- | --- |
| Objetivo G1 | Verificar automaticamente 8 categorias de problemas de formatação | Taxa de detecção ≥95% em 50 documentos de amostra |
| Objetivo G2 | Manter controlável o tempo de uma verificação | Verificação de documento com 1000 linhas em <2s |
| Não objetivo N1 | Não oferecer polimento de conteúdo do documento | Apenas indicar o local da ocorrência da regra, sem reescrever o texto |

## Critérios de sucesso
| Métrica | Linha de base | Valor-alvo | Forma de verificação | Momento de verificação |
| --- | --- | --- | --- | --- |
| Tempo de revisão manual | 25 minutos por documento | <5 minutos por documento | Experimento comparativo com 5 mantenedores | Antes da publicação da v1.0 |

### REQ-001: Verificação de espaçamento na mistura de chinês e inglês
- Origem: ISSUE-142
- Prioridade: Obrigatório
- Objetivo associado: G1
- História de usuário: como mantenedor de documentação, quero que os espaços ausentes entre chinês e inglês sejam marcados automaticamente, para que a diagramação fique uniforme.
- Critérios de aceite:
  1. Given um documento contendo “使用Node.js开发”
     When executar a verificação
     Then exibir o número da linha e o aviso “falta espaço entre chinês e inglês”
  2. Given que o local já possui espaço no documento
     When executar a verificação
     Then não exibir ocorrência dessa regra
- Estado: Confirmado
```

## Arquivos relacionados

- Rastreamento do requisito ao design, aos testes e à publicação: [especificação da matriz de rastreabilidade de requisitos](./requirements-traceability-matrix-specification.md)
- Campos de informação e marcação de lacunas: [coleta de informações e modelos](./information-collection-and-templates.md)
- Divisão de fases e condições de entrada: [processo de execução](./execution-process.md)
- A nomenclatura ocorre após a conclusão da iniciação: [especificação de nomenclatura de projetos](./project-naming-specification.md)
- Descrição externa de alterações de escopo: [especificação de registro de alterações](./changelog-specification.md)
