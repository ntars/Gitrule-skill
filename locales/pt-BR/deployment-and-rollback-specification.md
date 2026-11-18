# Especificação de implantação e reversão

> Problema que este arquivo resolve: definir modelos, campos e critérios de execução da lista de implantação, da solicitação de mudança e do plano de reversão, garantindo que a entrada em produção seja controlável, o estado consultável e as falhas rapidamente recuperáveis.

## 1. Dispositivos normativos

1. Antes da implantação deve-se passar pela CI, pela revisão de código e pelo portão de qualidade (ver [portão de qualidade](./quality-gate.md)).
2. A implantação baseia-se em uma versão de publicação já marcada com tag, sem uso de commits sem marcação (ver [especificação de gerenciamento de versões](./version-management-specification.md)).
3. A configuração de ambiente é separada do código; configurações sensíveis são injetadas pelo gerenciamento de configuração e não entram no repositório (ver [especificação de segurança e privacidade](./security-and-privacy-specification.md)).
4. Alterações de estrutura do banco de dados são executadas por scripts de migração e devem ser compatíveis com versões anteriores (ver [especificação de design de banco de dados](./database-design-specification.md)).
5. Cada implantação deve registrar número de versão, horário, operador e conteúdo da alteração; implantação sem registro é considerada não conforme.
6. Cada versão deve ter um plano de reversão previamente preparado; sem plano de reversão, a entrada em produção é vedada.
7. Após a implantação devem ser executadas a verificação de integridade e a validação de fumaça; somente com ambas aprovadas a publicação pode ser encerrada.

## 2. Modelo de lista de implantação

```markdown
# Lista de implantação: {{项目名称}} {{版本号}}

Versão: {{vX.Y.Z}} ｜ tag: {{vX.Y.Z}} ｜ Ambiente de destino: {{预发布 / 生产}} ｜ Horário previsto: {{YYYY-MM-DD HH:MM}}

## Verificações prévias
- [ ] CI toda verde, endereço da execução do fluxo de trabalho: {{URL}}
- [ ] Revisão de código aprovada, aprovador: {{姓名}}
- [ ] Portões de qualidade A/B/C todos PASS
- [ ] Registro de alterações e Release Notes prontos
- [ ] Plano de reversão revisado, ver o fim desta seção
- [ ] Script de migração do banco de dados revisado e compatível com versões anteriores
- [ ] Lista de alterações de configuração confirmada (itens injetados que não entram no repositório)

## Conteúdo da alteração
| Item de alteração | Tipo | Escopo de impacto | Requisito associado | Forma de verificação |
| --- | --- | --- | --- | --- |
| {{功能 / 配置 / 数据迁移}} | {{新增 / 修改 / 移除}} | {{受影响模块}} | {{REQ-NNN}} | {{如何确认}} |

## Etapas de execução
1. {{步骤，含具体命令或平台操作}}
2. {{灰度比例与观察时长}}
3. {{全量放量条件}}

## Verificação de integridade e fumaça
| Item de verificação | Condição de julgamento | Forma de execução | Resultado |
| --- | --- | --- | --- |
| Serviço ativo | {{HTTP 200}} | {{命令}} | {{通过 / 未通过}} |
| Caminho crítico | {{主流程完成}} | {{命令}} | {{通过 / 未通过}} |
| Taxa de erro | {{< X%}} | {{监控面板}} | {{通过 / 未通过}} |

## Registro de implantação
| Item | Valor |
| --- | --- |
| Horário real da implantação | {{YYYY-MM-DD HH:MM}} |
| Operador | {{姓名}} |
| Aprovador | {{姓名}} |
| Número de versão real | {{vX.Y.Z}} |
| Resultado | {{成功 / 回滚 / 中止}} |

## Plano de reversão
- Versão de destino da reversão: {{vX.Y.Z}}
- Condição de disparo: {{错误率 > X% 持续 N 分钟 / 冒烟失败 / 数据异常}}
- Responsável pela decisão: {{姓名}}
- Etapas de reversão: {{具体命令或操作}}
- Compatibilidade de dados: {{是否需要数据回滚；如果需要，说明方式}}
```

## 3. Modelo de registro de implantação

```markdown
## {{YYYY-MM-DD}} {{vX.Y.Z}} → {{环境}}

- Número de versão: {{vX.Y.Z}}
- tag: {{vX.Y.Z}}
- Horário: {{HH:MM}}
- Operador / Aprovador: {{姓名 / 姓名}}
- Resumo da alteração: {{一句话}}
- Verificação de integridade: {{通过 / 未通过}}
- Resultado: {{成功 / 回滚}}
- Publicação associada: {{Release Notes URL}}
- Observações: {{异常与处理记录；无则写「无」}}
```

## 4. Definição de campos

| Campo | Obrigatório | Tipo | Pontos de preenchimento | Exemplo |
| --- | --- | --- | --- | --- |
| tag | Sim | Texto | Totalmente coerente com a tag da [especificação de gerenciamento de versões](./version-management-specification.md) | `v1.2.0` |
| Ambiente de destino | Sim | Enumeração | Pré-produção / Produção, sem uso cruzado de configuração | `Produção` |
| Item de alteração.Tipo | Sim | Enumeração | Novo / Alteração / Remoção | `Alteração` |
| Requisito associado | Sim | Lista | Numeração REQ; sem alteração de requisito, escrever “nenhum” | `REQ-007` |
| Proporção de canário | Não | Percentual | Obrigatório na liberação gradual | `10% → 50% → 100%` |
| Condição de julgamento | Sim | Limiar | Observável e julgável | `HTTP 200` |
| Número de versão real | Sim | Texto | Divergência em relação à versão prevista deve ser justificada | `v1.2.1` |
| Condição de disparo da reversão | Sim | Limiar + duração | Formulações como “sensação de anormalidade” são vedadas | `Taxa de erro >1% por 5 minutos` |
| Compatibilidade de dados | Sim | Texto | Indicar claramente se há necessidade de reversão de dados | `Sem necessidade de reversão de dados` |

## 5. Instruções de preenchimento

1. **Verificações prévias**: marcar item a item; é vedado marcar o bloco inteiro de uma só vez; qualquer item não concluído interrompe a implantação.
2. **Conteúdo da alteração**: cada item deve estar associado a uma numeração REQ; alterações puramente operacionais sem requisito associado devem registrar “nenhum” e justificar a base da alteração.
3. **Verificação de integridade**: deve ser uma condição automaticamente julgável; “o serviço parece normal” é inaceitável.
4. **Condição de disparo da reversão**: deve apresentar simultaneamente o limiar e a duração, evitando disparos falsos por oscilações momentâneas.
5. **Liberação gradual**: após cada faixa de liberação deve-se observar o período definido e registrar a conclusão da observação antes de avançar à faixa seguinte.
6. **Registro de implantação**: acrescentar por ordem cronológica, sem substituir o histórico; o número de versão deve coincidir com o push, a tag e as Release Notes.
7. **Execução da reversão**: a reversão de código usa `git revert` para gerar um commit inverso; é vedado fazer push forçado sobre histórico já público (ver [especificação de push e publicação](./push-and-release-specification.md)).

Erros comuns:

| Redação incorreta | Problema | Forma de correção |
| --- | --- | --- |
| Implantar com commit sem tag | Versão não reproduzível | Marcar a tag antes de implantar |
| Plano de reversão escrito como “se houver problema, reverter” | Sem condição de disparo nem etapas | Acrescentar limiar, responsável pela decisão e etapas |
| Alteração de banco incompatível com a versão antiga | Dados indisponíveis após a reversão | Adotar o método de três etapas: expandir, migrar, contrair |
| Registro de implantação preenchido depois | Estado não confiável | Registrar no momento da implantação |
| Verificação de integridade limitada à página inicial | Caminho crítico não validado | Acrescentar casos de fumaça do fluxo principal |

## 6. Exemplo completo

```markdown
# Lista de implantação: markdown-lint-cli v1.0.0

Versão: v1.0.0 ｜ tag: v1.0.0 ｜ Ambiente de destino: Produção ｜ Horário previsto: 2026-11-20 10:00

## Verificações prévias
- [x] CI toda verde: https://github.com/example/markdown-lint-cli/actions/runs/123
- [x] Revisão de código aprovada, aprovador: Li Si
- [x] Portões de qualidade A/B/C todos PASS
- [x] Registro de alterações e Release Notes prontos
- [x] Plano de reversão revisado
- [x] Sem migração de banco de dados
- [x] Lista de alterações de configuração confirmada: nenhuma

## Conteúdo da alteração
| Item de alteração | Tipo | Escopo de impacto | Requisito associado | Forma de verificação |
| --- | --- | --- | --- | --- |
| Regra de espaçamento entre chinês e inglês | Novo | Mecanismo de regras | REQ-001 | Executar TC-001 |
| Saída de relatório da CLI | Alteração | Módulo de relatório | REQ-007 | Executar TC-012 |

## Etapas de execução
1. Obter a tag v1.0.0 e validar a soma de verificação
2. Canário de 10%, observar por 10 minutos
3. Com taxa de erro <0.1%, liberar até 100%

## Verificação de integridade e fumaça
| Item de verificação | Condição de julgamento | Forma de execução | Resultado |
| --- | --- | --- | --- |
| Serviço ativo | HTTP 200 | curl /healthz | Aprovado |
| Caminho crítico | Verificação de 50 documentos concluída | script shell | Aprovado |
| Taxa de erro | <0.1% | painel de monitoramento | Aprovado |

## Plano de reversão
- Versão de destino da reversão: v0.9.3
- Condição de disparo: taxa de erro >1% por 5 minutos
- Responsável pela decisão: Li Si
- Etapas de reversão: alternar a etiqueta de implantação para v0.9.3 e executar a verificação de compatibilidade de dados
- Compatibilidade de dados: sem alteração de banco de dados, não há necessidade de reversão de dados
```

## Arquivos relacionados

- Regras de versão e tag: [especificação de gerenciamento de versões](./version-management-specification.md)
- Ações de push e tratamento de incidentes: [especificação de push e publicação](./push-and-release-specification.md)
- Classificação de incidentes e retrospectiva: [especificação de resposta a incidentes](./incident-response-specification.md)
- Suporte de métricas e alertas: [especificação de observabilidade](./observability-specification.md)
- Scripts de migração e compatibilidade: [especificação de design de banco de dados](./database-design-specification.md)
- Injeção de configuração sensível: [especificação de segurança e privacidade](./security-and-privacy-specification.md)
