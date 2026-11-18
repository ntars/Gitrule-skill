# Modelo de isenção de responsabilidade

> Problema que este arquivo resolve: oferecer um modelo genérico de isenção de responsabilidade, pronto para ser copiado e aplicado com a simples substituição dos marcadores de posição, de modo que qualquer projeto possa delimitar, com o menor custo, a natureza do próprio conteúdo, as fronteiras de responsabilidade e as obrigações do usuário; as instruções de preenchimento e as variantes por cenário abrangem projetos individuais, corporativos, de código aberto e de código fechado.

## 1. Instruções de uso

1. Copiar todo o conteúdo da seção 3 “Corpo do modelo”, criando o arquivo `DISCLAIMER.md` na raiz do projeto, ou incorporá-lo como seção independente do `README.md`.
2. Substituir cada `{{...}}` conforme a tabela de correspondência de marcadores da seção 4; seções inteiras não utilizadas devem ser excluídas, sem deixar marcadores vazios.
3. Ajustar as cláusulas conforme as variantes de cenário da seção 5: softwares de código fechado priorizam a seção 3.5, e projetos de código aberto devem manter a explicação da relação com a licença da seção 3.6.
4. Este modelo é texto de referência genérico e não constitui opinião jurídica. Em casos de publicação externa formal, distribuição transfronteiriça ou setores regulados, o uso deve ocorrer após aprovação jurídica, conforme a seção 2 da [isenção de responsabilidade](./disclaimer.md).
5. Verificação antes do commit: marcadores totalmente substituídos, dados de contato reais e acessíveis, e nenhum conflito com as cláusulas da [LICENSE](../../LICENSE).

## 2. Princípios de personalização

- **Legalidade em primeiro lugar**: todas as cláusulas de isenção produzem efeito apenas na medida permitida pela lei aplicável; é proibido escrever expressões absolutas como “isenção incondicional de toda e qualquer responsabilidade”, evitando a invalidade de toda a cláusula.
- **Sem extrapolação**: não se deve revogar nem reduzir os direitos concedidos pela licença; havendo conflito, prevalece o texto da licença, conforme o princípio da [especificação de LICENSE](./license-specification.md).
- **Verificável**: dados de contato, data de vigência e nome do sujeito devem ser informações reais; é proibido manter valores de exemplo.
- **Independência**: as cláusulas são independentes entre si, e a invalidade de uma não afeta a validade das demais.

## 3. Corpo do modelo

O conteúdo a partir da seção 3.1 constitui o corpo do modelo e pode ser copiado diretamente.

### 3.1 Finalidade e escopo da declaração

```markdown
# Isenção de responsabilidade

> Esta declaração aplica-se a todo o conteúdo publicado por {{项目名称}} (doravante denominado “este projeto”), incluindo código-fonte, documentação, modelos, exemplos, dados e materiais relacionados (doravante denominados “conteúdo do projeto”), independentemente de seu uso por leitura humana, chamada programática ou qualquer outro meio.

1. Esta declaração destina-se a esclarecer a natureza do conteúdo do projeto, alertar sobre riscos de uso e explicitar as fronteiras de responsabilidade; não constitui restrição adicional a direitos de qualquer sujeito, nem constitui revogação ou redução dos direitos concedidos pela licença do projeto.
2. Todo sujeito que acesse, copie, cite, adapte, distribua ou use a totalidade ou parte do conteúdo do projeto (doravante denominado “usuário”) é considerado como tendo lido e compreendido esta declaração.
3. A data da última atualização desta declaração é {{更新日期}}.
```

### 3.2 Natureza do conteúdo

```markdown
## Natureza do conteúdo

1. O conteúdo do projeto consiste em {{内容性质描述}} e não representa padrão oficial, opinião jurídica ou conclusão de consultoria profissional de qualquer organização, setor ou jurisdição.
2. O conteúdo do projeto não oferece promessa de aplicabilidade a qualquer stack tecnológico, ambiente de execução ou requisito de conformidade específico, nem constitui opinião profissional nas áreas jurídica, de conformidade, de segurança, financeira ou tributária; em assuntos dessas áreas, o usuário deve consultar profissionais com a habilitação correspondente.
3. Exemplos, parâmetros e informações estatísticas do conteúdo do projeto servem apenas para ilustrar métodos ou demonstrar formas de escrita e não devem ser tomados diretamente como valores recomendados para ambiente de produção, sendo sua validade delimitada por {{数据或示例的时点与范围说明}}.
```

### 3.3 Declaração de ausência de garantias

```markdown
## Declaração de ausência de garantias

Na máxima extensão permitida pela lei, o conteúdo do projeto é fornecido “no estado em que se encontra”, e {{主体名称}} não oferece qualquer garantia expressa ou implícita, incluindo, entre outras:

- a exatidão, integridade, ausência de erros ou de omissões do conteúdo;
- a adequação do conteúdo à finalidade específica, ao ambiente específico ou aos requisitos específicos de conformidade do usuário;
- que a implementação conforme o conteúdo do projeto necessariamente alcance o resultado esperado, ou necessariamente passe por qualquer processo de auditoria, teste, publicação ou certificação;
- que o conteúdo do projeto permaneça disponível, não sofra alterações ou permaneça compatível com ferramentas, plataformas e serviços de terceiros adotados posteriormente pelo usuário;
- que o conteúdo do projeto não viole direitos de terceiros.
```

### 3.4 Responsabilidade do usuário

```markdown
## Responsabilidade do usuário

1. Antes de adotar o conteúdo do projeto, o usuário deve avaliar de forma independente sua aplicabilidade, considerando o tipo de projeto, a legislação aplicável, as exigências setoriais e sua própria tolerância a riscos, e decidir por conta própria se o adota, quais partes adota e como ajustá-las.
2. Antes do uso, o usuário deve validar modelos, configurações, trechos de script e parâmetros, incluindo validação de sintaxe, verificação de build, verificação de testes e revisão de segurança; não deve aplicá-los diretamente, sem validação, em ambiente de produção, em serviços externos ou em cenários que envolvam dados sensíveis.
3. Ao adaptar, suprimir, mesclar ou republicar o conteúdo do projeto, o usuário deve verificar por conta própria se o resultado é coerente com suas necessidades e com as cláusulas aplicáveis, respondendo pela documentação, pelas configurações e pelos entregáveis daí decorrentes.
4. O usuário deve cumprir a legislação aplicável e as normas internas de sua jurisdição e do setor em que o projeto se insere; o conteúdo do projeto não substitui o cumprimento das obrigações correspondentes.
```

### 3.5 Limitação de responsabilidade

```markdown
## Limitação de responsabilidade

1. Na máxima extensão permitida pela lei, {{主体名称}} não responde por qualquer perda, dano, responsabilidade, custo ou despesa decorrente ou alegadamente decorrente das situações abaixo, seja com fundamento em contrato, ato ilícito (inclusive culpa) ou outra razão jurídica, e independentemente de o sujeito ter sido informado da possibilidade:
   - uso, citação, cópia, adaptação, distribuição ou implementação da totalidade ou de parte do conteúdo do projeto;
   - decisões tomadas, ações praticadas ou ações deixadas de praticar com base no conteúdo do projeto;
   - resultados de execução, em fluxos de trabalho, de documentações, configurações e modelos elaborados conforme o conteúdo do projeto;
   - interrupções, falhas ou anomalias de dados causadas por problemas de compatibilidade entre o conteúdo do projeto e ferramentas, plataformas ou serviços de terceiros;
   - alteração, suspensão do fornecimento ou descontinuidade da manutenção do conteúdo do projeto.
2. As perdas e danos referidos no parágrafo anterior incluem, entre outros: perdas diretas, indiretas, incidentais e consequenciais, danos punitivos, bem como lucros cessantes, perda de receita, interrupção de negócios, perda ou corrupção de dados, dano à reputação, custos adicionais de aquisição e reclamações de terceiros.
3. As cláusulas de limitação desta declaração produzem efeito apenas na medida permitida pela lei aplicável. Se qualquer jurisdição não permitir a limitação ou exclusão de determinada responsabilidade, tal limitação não se aplica nessa jurisdição, permanecendo válidas as demais cláusulas.
```

### 3.6 Conteúdo de terceiros e relação com a licença

```markdown
## Conteúdo de terceiros e relação com a licença

1. Links externos, ferramentas, serviços, ícones, fontes e materiais citados no conteúdo do projeto são fornecidos pelos respectivos terceiros e sujeitos às suas próprias condições; {{主体名称}} não se responsabiliza por seu conteúdo, disponibilidade, exatidão, segurança ou legalidade, nem manifesta endosso. O usuário deve verificar por conta própria suas condições e aplicabilidade, e as obrigações de licença de recursos de terceiros não se transferem nem se extinguem pela citação no conteúdo do projeto.
2. Este projeto adota a licença {{许可证名称及 SPDX 标识符}}, cujo texto integral está em [LICENSE](./LICENSE). Esta declaração é uma explicação, do lado do uso, da cláusula de isenção da licença e não substitui, modifica ou enfraquece as cláusulas dessa licença.
3. Havendo conflito de interpretação entre esta declaração e as cláusulas da licença, prevalece o texto da licença. Nenhuma expressão desta declaração deve ser interpretada como cobrança adicional, condição ou restrição aos direitos concedidos.
4. Ao republicar o conteúdo do projeto ou conteúdo derivado, devem ser mantidos o aviso de direitos autorais e o aviso de licença conforme exigido pela licença, podendo ser anexada esta declaração para que usuários posteriores conheçam as fronteiras de responsabilidade.
```

### 3.7 Alteração e vigência

```markdown
## Alteração e vigência

1. Esta declaração é revisada oportunamente por {{维护主体}} conforme necessidades de atualização de conteúdo e de conformidade; após a revisão, prevalece a versão mais recente em {{仓库地址或发布渠道}}.
2. Esta declaração entra em vigor em {{生效日期}}. Se o usuário continuar a usar o conteúdo do projeto após a revisão da declaração, prevalece a versão revisada; se não concordar com o conteúdo revisado, deve cessar o uso.
3. As cláusulas desta declaração são independentes entre si. A declaração de invalidade ou de inexequibilidade de qualquer cláusula não afeta a validade das demais.
4. Contato: {{真实可达的联系邮箱或渠道}}.
```

## 4. Tabela de correspondência de marcadores e definição dos campos

| Marcador de posição | Obrigatório | Definição do campo | Exemplo de preenchimento |
| --- | --- | --- | --- |
| `{{项目名称}}` | Sim | Nome externo do projeto, coerente com a primeira linha do README | `FooBar` |
| `{{主体名称}}` | Sim | Nome completo do sujeito que assume ou renuncia à responsabilidade; projetos individuais usam o nome da pessoa, projetos corporativos usam a razão social | `某某科技有限公司` |
| `{{维护主体}}` | Sim | Organização ou pessoa responsável por revisar a declaração | `FooBar 维护团队` |
| `{{更新日期}}` | Sim | Data da última revisão desta declaração, no formato uniforme YYYY-MM-DD | `2026-11-18` |
| `{{生效日期}}` | Sim | Data em que esta declaração começa a vigorar, podendo ser igual à data de atualização | `2026-11-18` |
| `{{内容性质描述}}` | Sim | Uma frase que explica o que é o projeto e em que nível de maturidade está | `Implementação de exemplo para referência de desenvolvedores, não um componente de nível de produção` |
| `{{数据或示例的时点与范围说明}}` | Não | Momento de coleta e escopo de aplicação dos dados ou parâmetros dos exemplos | `2026 年 10 月对 120 个样本的统计` |
| `{{许可证名称及 SPDX 标识符}}` | Sim | Nome completo da licença do projeto e identificador SPDX | `Licença MIT (MIT)` |
| `{{仓库地址或发布渠道}}` | Sim | Local de publicação autorizado da versão mais recente da declaração | `https://github.com/owner/repo` |
| `{{真实可达的联系邮箱或渠道}}` | Sim | Endereço real pelo qual o usuário pode contatar os mantenedores | `security@example.com` |

## 5. Instruções de preenchimento e variantes por cenário

| Cenário | Cláusulas obrigatórias | Cláusulas que podem ser suprimidas | Pontos de ajuste |
| --- | --- | --- | --- |
| Projeto individual | 3.1 / 3.2 / 3.3 / 3.5 / 3.7 | 3.4 pode ser simplificada | Nome do sujeito deve ser o nome real da pessoa; contato deve ser um e-mail mantido a longo prazo |
| Projeto corporativo | Todas as cláusulas | Nenhuma | Nome do sujeito deve ser a razão social do registro comercial; publicação somente após aprovação jurídica |
| Projeto de código aberto | Todas as cláusulas, especialmente 3.6 | Nenhuma | Manter a explicação da relação com a licença; não reduzir os direitos concedidos pela licença |
| Software de código fechado | 3.1 / 3.2 / 3.3 / 3.4 / 3.5 / 3.7 | Parágrafos 2 a 4 da 3.6 podem ser excluídos | Remover menções a licença de código aberto e passar a citar o contrato de licença de usuário final |
| Protótipo experimental | 3.1 / 3.2 / 3.3 / 3.7 | 3.5 pode ser simplificada | Marcar explicitamente “protótipo” na natureza do conteúdo, evitando que seja tomado como versão estável |
| Tratamento de dados pessoais | Todas as cláusulas | Nenhuma | Acrescentar papéis no tratamento de dados, prazo de retenção e canal de direitos do titular; ver também [especificação de segurança e privacidade](./security-and-privacy-specification.md) |

Comparação de erros comuns:

| Escrita incorreta | Consequência | Escrita correta |
| --- | --- | --- |
| “Este projeto não assume qualquer responsabilidade” | Expressão absoluta, facilmente considerada inválida | “Na máxima extensão permitida pela lei, não assume...” |
| “O direito de interpretação final pertence ao autor” | Conflita com a concessão da licença e gera controvérsia | “Havendo conflito, prevalece o texto da licença” |
| Contato preenchido com `test@example.com` | Inacessível, canal de comunicação perdido | Preencher um e-mail real e válido a longo prazo |
| Copiar a declaração de outro projeto sem alterar o sujeito | Sujeito incorreto, declaração sem sentido | Substituir cada marcador e verificar a coerência do sujeito |

## 6. Exemplo completo

Segue um exemplo preenchido de projeto individual de código aberto, apenas como referência de formato, que não deve ser copiado diretamente como declaração própria.

```markdown
# Isenção de responsabilidade

> Esta declaração aplica-se a todo o conteúdo publicado por DemoCLI (doravante denominado “este projeto”), incluindo código-fonte, documentação, modelos, exemplos, dados e materiais relacionados (doravante denominados “conteúdo do projeto”).

1. Esta declaração destina-se a esclarecer a natureza do conteúdo do projeto, alertar sobre riscos de uso e explicitar as fronteiras de responsabilidade; não constitui restrição adicional a direitos de qualquer sujeito, nem constitui revogação ou redução dos direitos concedidos pela licença do projeto.
2. Todo sujeito que acesse, copie, cite, adapte, distribua ou use a totalidade ou parte do conteúdo do projeto é considerado como tendo lido e compreendido esta declaração.
3. A data da última atualização desta declaração é 2026-11-18.

## Natureza do conteúdo

1. O conteúdo do projeto consiste em uma ferramenta de linha de comando de exemplo para referência de desenvolvedores e não representa padrão oficial, opinião jurídica ou conclusão de consultoria profissional de qualquer organização, setor ou jurisdição.
2. O conteúdo do projeto não oferece promessa de aplicabilidade a qualquer stack tecnológico, ambiente de execução ou requisito de conformidade específico, nem constitui opinião profissional nas áreas jurídica, de conformidade, de segurança, financeira ou tributária.
3. Os parâmetros de exemplo do conteúdo do projeto servem apenas para demonstrar formas de escrita e não devem ser tomados diretamente como valores recomendados para ambiente de produção.

## Declaração de ausência de garantias

Na máxima extensão permitida pela lei, Zhang San não oferece qualquer garantia expressa ou implícita, incluindo, entre outras, exatidão absoluta do conteúdo, adequação a finalidade específica, alcance necessário do resultado esperado, disponibilidade contínua e não violação de direitos de terceiros.

## Limitação de responsabilidade

Na máxima extensão permitida pela lei, Zhang San não responde por qualquer perda decorrente do uso, adaptação ou implementação do conteúdo do projeto, seja com fundamento em contrato, ato ilícito ou outra razão jurídica. Se qualquer jurisdição não permitir a limitação ou exclusão de determinada responsabilidade, tal limitação não se aplica nessa jurisdição, permanecendo válidas as demais cláusulas.

## Conteúdo de terceiros e relação com a licença

Este projeto adota a licença MIT (MIT), cujo texto integral está em [LICENSE](./LICENSE). Esta declaração é uma explicação, do lado do uso, da cláusula de isenção da licença e não substitui, modifica ou enfraquece as cláusulas dessa licença; havendo conflito de interpretação, prevalece o texto da licença.

## Alteração e vigência

Esta declaração entra em vigor em 2026-11-18, é revisada pela equipe de manutenção do DemoCLI e prevalece a versão mais recente em https://github.com/example/democli. As cláusulas são independentes entre si. Contato: maintainer@example.com.
```

## Arquivos relacionados

- Declaração concreta deste projeto: [isenção de responsabilidade](./disclaimer.md)
- Regras de licença: [especificação de LICENSE](./license-specification.md)
- Segurança e privacidade: [especificação de segurança e privacidade](./security-and-privacy-specification.md)
- Conformidade de código aberto: [especificação de conformidade de código aberto](./open-source-compliance-specification.md)
- Convenções de escrita geral: [especificação de escrita geral](./general-writing-specification.md)
- Voltar ao índice em chinês simplificado: [README](./README.md)
- Voltar à página principal do repositório: [README](../../README.md)
