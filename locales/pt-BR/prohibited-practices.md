# Práticas proibidas

> Problema que este arquivo resolve: reunir todas as condutas proibidas que não podem ser violadas, servindo como a lista definitiva de linhas vermelhas para auditoria e redação.

## 1. Linhas vermelhas de controle geral e push

1. É proibido emitir “pode enviar primeiro, depois se completa” enquanto o P0 não estiver zerado.
2. É proibido inventar resultados de verificação; itens que não podem ser verificados devem ser marcados como `SKIP + motivo`, e não deve ser escrito PASS.
3. É proibido entregar vários documentos consolidados em um único arquivo.
4. É proibido inserir no README a API completa, o guia de contribuição e o registro de alterações.
5. É proibido usar `--force` em push para branches públicos, em nenhuma circunstância.
6. É proibido tratar chaves já vazadas apenas com um “commit de exclusão”.
7. É proibido criar nomes de repositório próprios em desacordo com a [especificação de nomes de projeto](./project-naming-specification.md).
8. É proibido escrever o processo de raciocínio interno na documentação entregue.

## 2. Linhas vermelhas de redação de documentação

1. Não devem ser inventados nomes de projeto, funcionalidades, dados de desempenho, versões de dependências, licenças, informações de autor nem resultados de testes.
2. Não devem ser copiados READMEs, documentações, códigos, imagens ou textos de terceiros; quando a citação for realmente necessária, a fonte e a licença devem ser indicadas.
3. Não deve ser escolhido o tipo de licença sem confirmação prévia.
4. Não devem constar números de desempenho não verificados, conclusões comparativas sem fonte, afirmações promissórias (como “garantia” e “gratuito para sempre”), descrições depreciativas de projetos de terceiros nem conteúdo promocional alheio ao projeto.
5. Não devem ser usados materiais de origem desconhecida; quando faltarem fonte e licença de imagens, ícones ou fontes tipográficas, deve-se marcar como pendente de confirmação e não usá-los diretamente.

## Arquivos relacionados

- Para as regras absolutas cuja violação bloqueia o processo, ver [regras absolutas](./hard-rules.md)
- Para o tratamento de incidentes (vazamento de chaves etc.), ver a seção 5 da [especificação de push e publicação](./push-and-release-specification.md)
- Para as restrições obrigatórias de papéis, ver [papéis e responsabilidades](./roles-and-responsibilities.md)
