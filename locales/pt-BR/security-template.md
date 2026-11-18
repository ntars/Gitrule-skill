# Modelo de SECURITY

> Problema que este arquivo resolve: fornecer um modelo de política de segurança pronto para cópia, destinado à geração do SECURITY.md dos projetos, com definição das versões suportadas, dos canais de notificação de vulnerabilidades, do fluxo de resposta e dos princípios de divulgação; as instruções de preenchimento correspondentes cobrem a escolha do canal de notificação e o tratamento de informações sensíveis.

## 1. Instruções de uso

1. Copiar todo o conteúdo da seção 3, “Corpo do modelo”, e criar o arquivo `SECURITY.md` no diretório raiz do projeto.
2. Substituir os marcadores de posição conforme a seção 4; o canal de notificação deve ser um endereço real, acessível e que não exponha publicamente a superfície de ataque.
3. Recortar conforme os cenários da seção 5: projetos sem manutenção de múltiplas versões devem remover as linhas de versões antigas da tabela de versões suportadas.
4. As regras de segurança e os requisitos sobre informações sensíveis estão na [especificação de segurança e privacidade](./security-and-privacy-specification.md); a dimensão de governança comunitária está na [matriz de dimensões de revisão](./review-dimension-matrix.md).

## 2. Princípios de customização

- **Canal privado em primeiro lugar**: a notificação de vulnerabilidades deve usar canal privado; é proibido exigir que o relator divulgue detalhes em issues públicas.
- **Prazos explícitos**: indicar o prazo da primeira resposta e o do reparo, evitando promessas por prazo indeterminado.
- **Minimização da informação**: exigir do relator apenas as informações mínimas necessárias à reprodução; é proibido enviar dados reais de produção.
- **Consistência jurídica**: os princípios de divulgação devem estar em conformidade com a legislação aplicável e com as políticas da plataforma; setores regulados devem passar por validação jurídica.

## 3. Corpo do modelo

```markdown
# Política de segurança

> Este arquivo descreve o escopo de suporte de segurança e a forma de notificação de vulnerabilidades do {{项目名称}}, aplicando-se a pesquisadores de segurança, contribuidores e usuários.

## Versões suportadas

| Versão | Aceita relatórios de segurança |
| --- | --- |
| {{当前版本}} | Sim |
| {{上一版本}} | {{是否接受}} |
| Versões anteriores | Não |

## Canal de notificação

Não devem ser relatadas vulnerabilidades de segurança por meio de issues públicas, áreas de discussão ou canais sociais. O envio deve ser feito pelos seguintes canais privados:

- E-mail de segurança: {{真实可达的安全邮箱}}
- Portal de notificação privada: {{私有漏洞报告地址}}

Na ausência dos canais acima, entrar em contato com os mantenedores por {{备用私有联系方式}}.

## Conteúdo do relatório

Para aumentar a eficiência do tratamento, devem ser fornecidas, na medida do possível:

- versões e componentes afetados;
- tipo de vulnerabilidade e impacto potencial;
- passos mínimos de reprodução ou prova de conceito;
- direção de correção sugerida (opcional).

Não devem ser enviados dados reais de produção, chaves ou informações de identidade pessoal.

## Fluxo de resposta

| Etapa | Prazo | Descrição |
| --- | --- | --- |
| Confirmação de recebimento | {{首次响应时限}} | Os mantenedores confirmam o recebimento do relatório |
| Avaliação inicial | {{评估时限}} | Determinação de se o caso é um problema de segurança e de seu alcance |
| Correção e verificação | {{修复时限}} | Conclusão da correção e verificação; casos complexos são negociados à parte |
| Publicação | {{发布延迟}} após a conclusão da correção | Publicação do aviso de segurança e da versão corrigida |

## Princípios de divulgação

- Os mantenedores manterão sob sigilo a identidade do relator e o conteúdo do relatório até a publicação da correção.
- Sem o consentimento dos mantenedores, o relator não deve divulgar detalhes da vulnerabilidade antes da publicação da correção.
- Após a publicação da correção, os mantenedores agradecerão ao relator no aviso de segurança (mediante consentimento do relator).
- Pesquisas de segurança de boa-fé e em conformidade com esta política não serão responsabilizadas.

## Exceções e isenções

Esta política não constitui compromisso de garantia de segurança; o conteúdo do projeto é fornecido “no estado em que se encontra”, conforme detalhado na [isenção de responsabilidade](./DISCLAIMER.md) e na [LICENSE](./LICENSE).
```

## 4. Tabela de correspondência de marcadores de posição e definição de campos

| Marcador de posição | Obrigatório | Definição do campo | Exemplo de preenchimento |
| --- | --- | --- | --- |
| `{{项目名称}}` | Sim | Nome público do projeto | `FooBar` |
| `{{当前版本}}` | Sim | Versão mais recente em manutenção ou `main` | `v2.3.0` |
| `{{上一版本}}` | Não | Versão anterior ainda em manutenção | `v2.2.x` |
| `{{是否接受}}` | Sim | Se essa versão aceita relatórios de segurança | `Sim` |
| `{{真实可达的安全邮箱}}` | Sim | E-mail dedicado a relatórios de segurança | `security@example.com` |
| `{{私有漏洞报告地址}}` | Sim | Portal de notificação privada | `https://github.com/owner/repo/security/advisories/new` |
| `{{备用私有联系方式}}` | Não | Alternativa quando o canal principal estiver indisponível | `Mensagem direta pela conta dos mantenedores` |
| `{{首次响应时限}}` | Sim | Prazo para confirmar o recebimento do relatório | `3 dias úteis` |
| `{{评估时限}}` | Sim | Prazo para concluir a avaliação inicial | `7 dias úteis` |
| `{{修复时限}}` | Sim | Prazo para concluir a correção | `30 dias` |
| `{{发布延迟}}` | Sim | Intervalo até a publicação após a correção | `7 dias` |

## 5. Instruções de preenchimento e variantes por cenário

| Cenário | Seções obrigatórias | Seções recortáveis | Pontos de ajuste |
| --- | --- | --- | --- |
| Projeto de versão única | Canal de notificação, conteúdo do relatório, fluxo de resposta, princípios de divulgação | Remover as linhas de versões antigas da tabela de versões suportadas | Indicar `main` ou a tag mais recente como versão atual |
| Manutenção de múltiplas versões | Todas | Nenhuma | Listar linha a linha as versões que ainda aceitam relatórios |
| Projeto pessoal | Todas | A tabela de versões suportadas pode ser simplificada | Usar no canal privado um e-mail mantido a longo prazo |
| Projeto corporativo | Todas | Nenhuma | Os prazos devem ser consistentes com a política interna de segurança e validados juridicamente |
| Setor regulado | Todas | Nenhuma | Acrescentar obrigações de notificação regulatória e requisitos de retenção de dados |

Comparação de erros comuns:

| Redação incorreta | Consequência | Redação correta |
| --- | --- | --- |
| “Relate vulnerabilidades em uma Issue” | Divulgação pública de detalhes, ampliando o risco | Usar canal privado |
| “Trataremos o quanto antes” | Sem expectativa clara, o relator não consegue avaliar | Indicar prazos por etapa |
| Prazo escrito como “correção em 24 horas” | Promessa excessiva, impossível de cumprir | Indicar faixa razoável e ressalvar que casos complexos são negociados à parte |
| Não exigir anonimização | O relator pode enviar dados reais de produção | Proibir explicitamente o envio de dados reais e chaves |

## 6. Exemplo completo

A seguir, um exemplo preenchido do trecho do canal de notificação, apenas como referência de formato.

```markdown
## Canal de notificação

Não devem ser relatadas vulnerabilidades de segurança por meio de issues públicas, áreas de discussão ou canais sociais. O envio deve ser feito pelos seguintes canais privados:

- E-mail de segurança: security@example.com
- Portal de notificação privada: https://github.com/example/democli/security/advisories/new

Não devem ser enviados dados reais de produção, chaves ou informações de identidade pessoal.
```

## Arquivos relacionados

- Especificação correspondente: [especificação de segurança e privacidade](./security-and-privacy-specification.md)
- Modelos complementares: [modelo de código de conduta](./code-of-conduct-template.md), [modelo de guia de contribuição](./contribution-guide-template.md), [modelo de isenção de responsabilidade](./disclaimer-template.md)
- Dimensão de notificação de vulnerabilidades: [matriz de dimensões de revisão](./review-dimension-matrix.md)
- Tratamento de incidentes de vazamento de chaves: [especificação de push e publicação](./push-and-release-specification.md)
- Voltar ao índice em chinês simplificado: [README](./README.md)
