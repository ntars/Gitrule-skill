# Modelo de código de conduta

> Problema que este arquivo resolve: fornecer um modelo de código de conduta pronto para cópia, a fim de que o projeto gere o CODE_OF_CONDUCT.md, definindo o compromisso de participação, os comportamentos esperados, os comportamentos inaceitáveis, as responsabilidades de execução e o canal de denúncia; as instruções de preenchimento que o acompanham cobrem a origem da adaptação e a declaração de versão.

## 1. Instruções de uso

1. Copiar todo o conteúdo do modelo de texto (seção 3) e criar com ele o arquivo `CODE_OF_CONDUCT.md` no diretório raiz do projeto.
2. Substituir os marcadores de posição conforme a tabela de correspondência de campos (seção 4), sendo obrigatório que o canal de denúncia seja um endereço real e acessível.
3. Caso se adote ou se adapte um código de conduta que possua versão própria, deve-se declarar a versão e a licença conforme as instruções de preenchimento (seção 5), segundo os requisitos da fonte, com fundamento no item 8 da seção 1 da [especificação de código de conduta](./code-of-conduct-specification.md).
4. Vincular este arquivo no [modelo de guia de contribuição](./contribution-guide-template.md) e na seção de contribuição do README, mantendo a acessibilidade nos dois sentidos.

## 2. Princípios de customização

- **Agnóstico à tecnologia**: o código não contém conteúdo técnico, apenas normas de comportamento na participação, com fronteiras definidas na [matriz de documentação](./document-matrix.md).
- **Executável**: o tratamento por níveis deve indicar as condições de acionamento e as medidas; é proibido registrar apenas princípios sem consequências.
- **Acessibilidade**: o canal de denúncia deve ser real e eficaz; é proibido deixar endereços de exemplo.
- **Origem em conformidade**: a adaptação de códigos de terceiros deve preservar seus requisitos de atribuição e licença, conforme a [especificação de conformidade open source](./open-source-compliance-specification.md).

## 3. Modelo de texto

```markdown
# Código de conduta

## Nosso compromisso

Nós, na condição de participantes, contribuidores e mantenedores do {{项目名称}}, nos comprometemos a construir em conjunto um ambiente de participação aberto, acolhedor e livre de assédio, independentemente de idade, tipo físico, condição de deficiência, raça, identidade e expressão de gênero, nível de experiência, escolaridade, posição socioeconômica, nacionalidade, aparência ou orientação sexual.

## Escopo de aplicação

Este código aplica-se aos espaços do projeto, às issues, aos pull requests, às revisões de código, aos canais sociais e aos ambientes públicos em que uma pessoa apareça na condição de representante do projeto.

## Comportamentos esperados

- Respeitar pontos de vista e experiências distintos e comunicar-se com boa-fé.
- Aceitar feedback construtivo e concentrar-se no problema, não na pessoa.
- Considerar o interesse coletivo da comunidade e evitar prejudicar o projeto e seus participantes.
- Ter paciência com iniciantes e oferecer sugestões de melhoria acionáveis.

## Comportamentos inaceitáveis

- Ataques pessoais e manifestações insultuosas ou depreciativas.
- Manifestações discriminatórias e assédio com base em qualquer característica protegida.
- Assédio público ou privado, perseguição e contato contínuo sem consentimento.
- Divulgação não autorizada de informações privadas de terceiros.
- Outros comportamentos razoavelmente considerados inadequados em ambiente profissional.

## Responsabilidades de execução

Os mantenedores do projeto são responsáveis por esclarecer a aplicação deste código e julgar as violações, tendo o direito de remover, editar ou rejeitar conteúdos que não estejam em conformidade com ele. Os mantenedores devem exercer suas funções de forma consistente e imparcial e abster-se de forma proativa em controvérsias que os envolvam.

## Medidas disciplinares

As violações são tratadas por níveis, conforme a gravidade:

| Nível | Situação aplicável | Medida |
| --- | --- | --- |
| Nível um (Correction) | Ofensa involuntária, conduta levemente inadequada | Advertência e esclarecimento em âmbito privado |
| Nível dois (Warning) | Reincidência ou violação explícita | Advertência pública e prazo para correção |
| Nível três (Temporary Ban) | Assédio grave, ataque malicioso | Suspensão temporária da permissão de participação |
| Nível quatro (Permanent Ban) | Conduta grave contínua ou irreparável | Banimento permanente com manutenção de registro |

## Canal de denúncia

Em caso de sofrimento ou de identificação de conduta que viole este código, deve-se contatar a equipe de mantenedores por meio de {{真实可达的举报邮箱或渠道}}. Todas as denúncias serão tratadas de forma confidencial, e os mantenedores não devem revelar a identidade do denunciante à pessoa denunciada, salvo com o consentimento expresso do denunciante.

## Atribuição e origem

{{准则来源声明}}
```

## 4. Tabela de correspondência de marcadores de posição e definição de campos

| Marcador de posição | Obrigatório | Definição do campo | Exemplo de preenchimento |
| --- | --- | --- | --- |
| `{{项目名称}}` | Sim | Nome externo do projeto, idêntico à primeira linha do README | `FooBar` |
| `{{真实可达的举报邮箱或渠道}}` | Sim | Endereço real pelo qual os mantenedores podem ser contatados diretamente | `conduct@example.com` |
| `{{准则来源声明}}` | Sim | Em caso de criação original, escrever “original”; em caso de adaptação, escrever o nome da fonte, a versão e a licença | `Adaptado do Contributor Covenant 2.1 (CC BY 4.0)` |

## 5. Instruções de preenchimento e variantes de cenário

| Cenário | Pontos de ajuste |
| --- | --- |
| Projeto individual | Indicar a própria pessoa como mantenedora; usar no canal de denúncia um e-mail mantido a longo prazo |
| Projeto corporativo | Definir expressamente o jurídico ou a equipe de comunidade como sujeito de execução; as medidas disciplinares devem ser coerentes com as normas internas |
| Adoção de código conhecido | Preservar integralmente o texto original e a versão, acrescentando apenas o canal de denúncia e a atribuição |
| Projeto multilíngue | Fazer corresponder cláusula a cláusula as versões em cada idioma; indicar a versão em inglês ou em chinês como versão autoritativa |

Comparação de erros frequentes:

| Redação incorreta | Consequência | Redação correta |
| --- | --- | --- |
| Escrever apenas “comunicação acolhedora é bem-vinda” | Sem base de execução, impossível julgar em caso de controvérsia | Enumerar comportamentos esperados, comportamentos inaceitáveis e tratamento por níveis |
| Deixar um e-mail de exemplo no canal de denúncia | Inacessível, o mecanismo de denúncia torna-se ineficaz | Preencher um endereço real e válido a longo prazo |
| Adaptar o código sem atribuição | Violação dos requisitos de licença da fonte | Declarar a origem, a versão e a licença |

## 6. Exemplo completo

A seguir, um trecho de cenário de adaptação, apenas como referência de formato.

```markdown
## Canal de denúncia

Em caso de sofrimento ou de identificação de conduta que viole este código, deve-se contatar a equipe de mantenedores por meio de conduct@example.com. Todas as denúncias serão tratadas de forma confidencial.

## Atribuição e origem

Este código foi adaptado do Contributor Covenant na versão 2.1 e segue a licença CC BY 4.0 Internacional.
```

## Arquivos relacionados

- Especificação correspondente: [especificação de código de conduta](./code-of-conduct-specification.md)
- Modelos complementares: [modelo de guia de contribuição](./contribution-guide-template.md), [modelo de SECURITY](./security-template.md)
- Dimensão de governança da comunidade: [matriz de dimensões de revisão](./review-dimension-matrix.md)
- Voltar ao índice em chinês simplificado: [README](./README.md)
