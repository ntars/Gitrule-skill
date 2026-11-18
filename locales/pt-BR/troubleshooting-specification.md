# Especificação de solução de problemas

> Problema que este arquivo resolve: definir a estrutura, a forma de redação dos itens e o mecanismo de manutenção da documentação de solução de problemas (Troubleshooting / FAQ), para que os usuários consigam localizar a causa a partir do sintoma e resolver sozinhos os problemas comuns.

## 1. Cenários de aplicação

A documentação de solução de problemas deve ser fornecida nas seguintes situações:

1. A instalação ou a compilação falha por vários motivos comuns.
2. Há conflito entre itens de configuração e a mensagem de erro não é suficiente para indicar a solução.
3. Existem limitações conhecidas em determinada plataforma ou versão.
4. Os usuários repetem a mesma pergunta e a resposta pode ser padronizada.

## 2. Localização e nomenclatura de arquivos

1. Quando o conteúdo é pequeno, usar como uma seção do README, com o título “Perguntas frequentes” ou “Solução de problemas”.
2. Quando o conteúdo é extenso, criar um arquivo separado `docs/troubleshooting.md` ou `FAQ.md`, mantendo no README o link de entrada.
3. Agrupar os problemas por tema, como “instalação”, “configuração”, “execução”, “desempenho” e “rede”.

## 3. Estrutura da documentação

1. **Introdução**: o escopo dos problemas comuns cobertos por este documento e as versões aplicáveis.
2. **Índice de problemas**: listar os títulos dos problemas por tema, permitindo salto rápido.
3. **Itens de problema**: detalhar cada item segundo uma estrutura uniforme.
4. **Ainda sem solução**: indicar os canais de ajuda, como issues e fóruns de discussão.

## 4. Estrutura dos itens

Cada item de problema deve conter as seguintes partes:

| Parte | Conteúdo | Requisito |
| --- | --- | --- |
| Sintoma | A manifestação concreta vista pelo usuário | Incluir a mensagem de erro completa; não escrever apenas “erro” |
| Condição de disparo | Quando ocorre | Especificar versão, plataforma e operação |
| Causa | A causa raiz | Explicar o mecanismo, não apenas apresentar a conclusão |
| Solução | Passos executáveis | Listar de forma numerada, incluindo comandos ou configurações |
| Verificação | Como confirmar que foi corrigido | Apresentar a saída esperada |
| Relacionamento | Links para documentação ou issues pertinentes | Opcional |

## 5. Exemplo de redação de item

```markdown
### Erro `EACCES: permission denied` durante a instalação

**Sintoma**: ao executar `npm install -g <package>`, é exibida uma mensagem de permissão insuficiente.

**Condição de disparo**: instalação de pacote global como usuário comum em Linux ou macOS.

**Causa**: a permissão de escrita do diretório de instalação global pertence ao administrador do sistema; o usuário atual não tem direito de escrita.

**Solução**:

```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
npm install -g <package>
```

**Verificação**: a execução de `<package> --version` exibe o número da versão, o que indica sucesso.

## 6. Requisitos de redação

1. Usar no título do problema a expressão que o usuário pesquisaria, não jargão interno.
2. Preservar a mensagem de erro como está, para facilitar a comparação pelo usuário; informações sensíveis devem ser anonimizadas (ver [especificação de segurança e privacidade](./security-and-privacy-specification.md)).
3. A solução deve trazer o comando completo, sem presumir que o usuário já configurou variáveis de ambiente.
4. Um item resolve apenas um problema; não reunir várias causas.
5. Em caso de defeito conhecido, explicar o escopo de impacto e a forma de contorno, sem prometer prazo de correção.
6. Problemas relacionados a migração devem apontar para o guia de migração (ver [especificação de guia de migração](./migration-guide-specification.md)).

## 7. Mecanismo de manutenção

1. Quando a mesma pergunta se repetir mais de três vezes, o item deve ser criado ou reescrito.
2. Após cada atualização de versão, revisar todos os itens e remover o conteúdo que deixou de ser válido.
3. Cada item pode indicar a versão da última verificação, para facilitar a avaliação de sua aplicabilidade.
4. O índice de problemas deve ser atualizado em sincronia com a inclusão ou remoção de itens.

## 8. Práticas proibidas

1. É proibido transformar a documentação de solução de problemas em apresentação de funcionalidades.
2. É proibido apresentar apenas respostas sem valor diagnóstico, como “tente reiniciar”.
3. É proibido omitir a mensagem de erro e a condição de disparo.
4. É proibido manter itens já corrigidos ou que deixaram de ser válidos.

## Arquivos relacionados

- A alocação da seção no README está na [especificação de seções do README](./readme-sections-specification.md), capítulo 15
- Os requisitos de divulgação de problemas conhecidos estão na [especificação de seções do README](./readme-sections-specification.md), capítulo 15
- Problemas relacionados a atualização estão no [guia de migração](./migration-guide-specification.md)
- Os canais de coleta de problemas estão na [especificação de modelos de Issue e PR](./issue-and-pr-template-specification.md)
- A qualidade da documentação pertence à dimensão D12; ver [matriz de dimensões de revisão](./review-dimension-matrix.md)
