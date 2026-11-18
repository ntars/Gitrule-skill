# Regras absolutas

> Problema que este arquivo resolve: enumerar as regras invioláveis cuja violação, por si só, bloqueia o push e não admite o critério de “primeiro enviar e depois corrigir”.

## Tabela de regras absolutas

| # | Regra |
|---|---|
| H1 | O nome do repositório deve estar em conformidade com a [especificação de nomes de projeto](./project-naming-specification.md); maiúsculas e minúsculas, caracteres e comprimento devem ser integralmente conformes |
| H2 | Deve existir um arquivo `LICENSE`; a ausência de licença equivale à reserva de direitos por padrão e o projeto não deve ser tornado público |
| H3 | Não deve ser feito commit de nenhuma chave, token, chave privada, arquivo `.env`, AK/SK de provedor de nuvem nem string de conexão de banco de dados |
| H4 | Não deve ser feito commit de artefatos de compilação, diretórios de dependências, configuração de IDE nem arquivos temporários do sistema |
| H5 | Um arquivo individual não deve exceder 100 MB; acima de 50 MB deve ser usado LFS ou o arquivo deve ser excluído |
| H6 | Deve existir `README.md`, e ele deve conter: posicionamento em uma frase, instalação, exemplo mínimo executável e licença |
| H7 | O branch padrão deve ser protegido; é proibido o push direto para `main`/`master` |
| H8 | É proibido usar `git push --force` em branches públicos; em branches pessoais apenas `--force-with-lease` é permitido |
| H9 | Antes do push, `build` e `test` devem passar; se a CI estiver vermelha, não deve haver merge no branch principal |
| H10 | A mensagem de commit deve estar em conformidade com o Conventional Commits; são proibidos commits sem informação, como `wip`/`update`/`fix bug` |
| H11 | Cada documentação deve ser um arquivo independente com responsabilidade própria; é proibido acumular todo o conteúdo no README (ver [matriz de documentação](./document-matrix.md)) |
| H12 | Uma vez que uma chave tenha sido enviada por push, deve-se rotacionar a chave imediatamente e limpar o histórico; não deve ser feito apenas um commit de exclusão |

## Restrições de execução

- A violação de qualquer uma das regras **bloqueia o push**; não se admite o critério de “primeiro enviar e depois corrigir”.
- O resultado da avaliação de H1–H12 deve constar na lista de problemas do [formato do relatório de auditoria](./audit-report-format.md), com evidência em cada item (caminho:linha / saída de comando).
- Em caso de violação de H12, deve-se seguir o fluxo de tratamento de incidentes da [especificação de push e publicação](./push-and-release-specification.md).

## Arquivos relacionados

- Para os detalhes de nomenclatura, ver a [especificação de nomes de projeto](./project-naming-specification.md)
- Para as condições de liberação do portão, ver o [portão de qualidade](./quality-gate.md)
- Para o compêndio de práticas proibidas, ver [práticas proibidas](./prohibited-practices.md)
