# Processo de execução

> Problema que este arquivo resolve: definir a sequência completa de fases da iniciação do projeto até a entrega, as condições de entrada e os produtos de cada fase, bem como as regras de questionamento bloqueante quando as informações forem insuficientes.

## 1. Fluxo de push do controle geral (Phase 0–6)

### Phase 0 · Iniciação do projeto (Project Init)

Saída: 3 candidatos de nome de projeto + justificativa da escolha + conclusão da busca de nomes duplicados + tabela de metadados do repositório (description / topics / branch padrão / visibilidade / license). Para as regras de nomenclatura, ver a [especificação de nomes de projeto](./project-naming-specification.md).

### Phase 1 · Inventário (Inventory)

Varredura do repositório, gerando um inventário estruturado:
- Stack tecnológico, arquivos de entrada, gerenciador de pacotes, lockfile
- Documentação existente, documentação ausente
- Top 10 maiores arquivos do repositório por tamanho
- CI / modelos / regras de proteção já existentes
- Estado atual do git: arquivos não rastreados, alterações não commitadas, commits suspeitos no histórico

### Phase 2 · Auditoria paralela (Audit)

Conforme a [matriz de dimensões de revisão](./review-dimension-matrix.md), distribuir as dimensões aos subagentes para execução paralela; a forma de despacho consta no [contrato de despacho de subagentes](./sub-agent-dispatch-contract.md). Cada subagente retorna apenas conclusões estruturadas, sem prosa longa.

### Phase 3 · Correção (Fix)

Listar as pendências na ordem P0 → P1 → P2, indicando o agente responsável e a ação prevista. Não é permitido entrar na Phase 5 enquanto o P0 não estiver zerado.

### Phase 4 · Geração de documentação (Docs)

Conforme a [matriz de documentação](./document-matrix.md), distribuir arquivo a arquivo aos agentes de documentação. **Escrever apenas um arquivo por vez, validar após escrever e só então passar ao próximo.**

### Phase 5 · Push (Push)

Executar conforme a [especificação de push e publicação](./push-and-release-specification.md), ecoando o resultado item a item.

### Phase 6 · Pós-push (Post-Push)

Criar a tag, escrever as Release Notes, validar a disponibilidade dos selos e links, confirmar que a CI está verde e confirmar que as informações da área About estão corretas.

## 2. Fluxo de geração de documentação (fases 0–5)

Avançar na ordem das fases; não é permitido entrar na fase seguinte enquanto a anterior não estiver concluída.

| Fase | Nome | Condição de entrada | Produto |
| --- | --- | --- | --- |
| 0 | Verificação de informações | Recebimento desta especificação e dos materiais do projeto | Lista de informações confirmadas, lista de informações ausentes |
| 1 | Questionamento bloqueante | Existência de campos obrigatórios ausentes (ver [coleta de informações e modelos](./information-collection-and-templates.md)) | Lista estruturada de perguntas, agrupada por campo |
| 2 | Confirmação do esqueleto | Campos obrigatórios completos | Sumário de seções do README e tópicos essenciais de cada seção, para confirmação do usuário |
| 3 | Geração de documentação | Confirmação do esqueleto pelo usuário, ou manifestação explícita de que a confirmação não é necessária | Todos os entregáveis |
| 4 | Portão de qualidade | Geração da documentação concluída | Resultado da avaliação item a item do [portão de qualidade](./quality-gate.md) |
| 5 | Entrega | Todos os portões aprovados ou itens reprovados já marcados | Saída na ordem do [formato do relatório de auditoria](./audit-report-format.md), com guia de push anexo |

## 3. Regras de questionamento da fase 1

1. Perguntar agrupando por campo, com no máximo 15 itens por rodada.
2. Cada pergunta deve indicar sua finalidade e as seções afetadas, para facilitar a priorização pelo usuário.
3. Quando o usuário declarar explicitamente que determinado item não pode ser fornecido, marcar “【pendente de confirmação: nome do campo】” no local correspondente da documentação e consolidar ao final do texto.
4. Quando o usuário responder “conforme seu julgamento”, valores sugeridos podem ser apresentados, mas devem ser marcados como “【valor sugerido, pendente de confirmação do usuário】”.

## Arquivos relacionados

- Para papéis e responsabilidades, ver [papéis e responsabilidades](./roles-and-responsibilities.md)
- Para campos obrigatórios e marcação de itens ausentes, ver [coleta de informações e modelos](./information-collection-and-templates.md)
- Para o julgamento do portão, ver o [portão de qualidade](./quality-gate.md)
