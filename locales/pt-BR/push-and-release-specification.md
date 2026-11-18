# Especificação de push e publicação

> Problema que este arquivo resolve: definir a lista de ações antes, durante e depois do push, as regras de tag e de publicação, o fluxo de tratamento de incidentes, além de orientações completas de push no GitHub e uma matriz de tratamento de falhas.

## 1. Antes do push

1. `git status` limpo, sem arquivos sensíveis não rastreados.
2. `git log` sem WIP, sem `fix bug`, sem vazamento de dados pessoais.
3. Confirmar que o `.gitignore` está em vigor e que artefatos e dependências não estão rastreados.
4. Passar localmente em build, test e lint.
5. Executar a varredura completa de chaves (incluindo commits históricos).
6. Matriz de documentação completa (ver a [matriz de documentação](./document-matrix.md)).

## 2. Ações de push

7. Enviar o branch pessoal: `git push -u origin feat/xxx`.
8. O tronco passa apenas por PR, sem push direto.
9. É proibido `push --force`; para reescrever o próprio branch, usar `--force-with-lease`.
10. É proibido fazer rebase/amend em branch público já enviado.
11. Arquivo individual >50MB deve passar por LFS antes do push.
12. Confirmar a visibilidade do repositório antes do primeiro push: padrão private, e mudar para public apenas quando houver necessidade real de tornar público.

## 3. Tag e publicação

13. Formato de tag `vMAJOR.MINOR.PATCH`, obrigatoriamente annotated: `git tag -a v1.0.0 -m "release: 1.0.0"`.
14. A tag só deve ser criada depois que a CI estiver verde e as Release Notes prontas.
15. Mudanças incompatíveis devem usar `feat!:` ou `BREAKING CHANGE:`, com o caminho de migração indicado no CHANGELOG.

## 4. Phase 6 · Depois do push (Post-Push)

- criar a annotated tag;
- escrever as Release Notes;
- verificar a disponibilidade dos selos e dos links;
- confirmar que a CI está verde;
- confirmar que as informações da área About estão corretas (description / topics / links / social preview).

## 5. Tratamento de incidentes

16. **Chave já enviada por push**: rotacionar imediatamente → limpar com `git filter-repo` → o push forçado em branch protegido exige o fluxo de administrador → comunicado.
17. **Envio acidental de arquivo grande**: migração para LFS ou reescrita do histórico; não se deve apenas excluir o arquivo.

## 6. Especificação das orientações de push no GitHub

As orientações devem conter as sete partes abaixo, com os comandos em versão completa e executável.

### 6.1 Segurança prévia

1. Antes do push, fazer backup completo do repositório local e do repositório remoto; recomenda-se `git clone --mirror` para gerar um backup espelhado.
2. Confirmar que o repositório remoto não tem colaboradores, ou que os colaboradores já foram avisados para suspender os pushes.
3. Confirmar que o branch de destino não tem proteção contra push forçado habilitada.

### 6.2 Organização local

```bash
git status
git diff --name-status HEAD
git ls-files
```

Conferir as três saídas e confirmar que as alterações a commitar correspondem ao diretório local, sem arquivos temporários, artefatos de compilação ou documentação antiga remanescente. O `.gitignore` deve cobrir artefatos de compilação e arquivos de configuração locais.

### 6.3 Verificação de consistência

```bash
git fetch origin
git diff --name-status HEAD origin/{{分支名}}
```

Esse comando lista as diferenças entre os arquivos remotos e locais. Arquivos que existem no remoto e foram excluídos localmente devem ser removidos com `git rm` e commitados, para que a exclusão entre no histórico de versões.

### 6.4 Commit e push

```bash
git add -A
git commit -m "docs: 重建项目文档（README、README_EN、NOTICE）"
git push --force-with-lease origin {{分支名}}
```

Usar `--force-with-lease` em vez de `--force` recusa o push quando há novos commits de outras pessoas no remoto, evitando sobrescrever o trabalho alheio. Excluir o repositório remoto e recriá-lo é uma operação de alto risco, usada apenas em repositórios pessoais e com backup espelhado já concluído; as orientações devem indicar explicitamente o risco de perda de dados.

### 6.5 Verificação após o push

```bash
git ls-remote --heads origin
gh repo view --web
```

Confirmar item a item na interface web a lista de arquivos, a renderização do README, os links de troca de idioma e a validade dos links do NOTICE.

### 6.6 Matriz de tratamento de falhas

| Tipo de erro | Sintoma típico | Solução | Alerta de risco |
| --- | --- | --- | --- |
| Falha de autenticação | `Authentication failed`, `Permission denied (publickey)` | Trocar HTTPS por SSH e configurar a chave, ou usar `gh auth login` e depois fazer o push | Nenhum |
| Interrupção de rede | `Failed to connect`, `RPC failed` | Trocar de rede, configurar proxy, executar `git config --global http.postBuffer 524288000` | Nenhum |
| Arquivo acima do limite | `remote: error: File exceeds 100 MB` | Remover o arquivo grande do histórico de commits ou habilitar Git LFS | Após reescrever o histórico, avisar os colaboradores para clonar novamente |
| Conflito de maiúsculas e minúsculas | Nomes de arquivo com diferença de caixa geram entradas duplicadas | Corrigir com `git mv` e commitar | Nenhum |
| Conflito de histórico | `non-fast-forward`, `fetch first` | Preferir `git pull --rebase`; quando for realmente necessário sobrescrever, usar `--force-with-lease` | Commits alheios sobrescritos não são recuperáveis |
| Proteção de branch | `protected branch hook declined` | Fazer o merge pelo fluxo de PR, ou o administrador ajustar temporariamente as regras | Ajustes de regra devem ser registrados |
| Repositório corrompido | `fatal: not a git repository`, objetos ausentes | Clonar novamente e copiar as alterações da área de trabalho | Fazer backup da área de trabalho primeiro |

### 6.7 Reversão

Se for identificado um problema após a conclusão do push, usar `git revert` para gerar um commit inverso; não se deve fazer novo push forçado para sobrescrever um histórico já público.

## Arquivos relacionados

- Antes do push, deve-se passar pelos três portões do [portão de qualidade](./quality-gate.md)
- As linhas vermelhas de chaves e arquivos grandes estão em H3/H5/H12 das [regras absolutas](./hard-rules.md)
- A especificação de mensagens de commit pertence à dimensão D7, ver a [matriz de dimensões de revisão](./review-dimension-matrix.md)
- A responsabilidade da documentação de publicação `docs/release.md` está na [matriz de documentação](./document-matrix.md)
