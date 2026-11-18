# Especificação de design de banco de dados

> Problema que este arquivo resolve: definir as regras de design da estrutura de tabelas, campos, índices e migrações do banco de dados, garantindo consistência, evolução e rastreabilidade dos dados.

## 1. Convenções de nomenclatura

1. Nomes de tabelas e de campos devem seguir um estilo de nomenclatura uniforme e com significado claro.
2. Nomes de chaves primárias, chaves estrangeiras e índices devem seguir regras de prefixo uniformes.
3. Palavras reservadas e abreviações devem ter convenção explícita, evitando ambiguidade.

## 2. Design de campos

1. Cada campo deve definir explicitamente o tipo, a possibilidade de ser nulo, o valor padrão e o significado.
2. Campos de data e hora devem usar fuso horário e precisão uniformes.
3. Campos sensíveis à precisão, como valores monetários, devem usar tipos de ponto fixo, não de ponto flutuante.
4. Campos de estado devem usar enumerações explícitas, indicando o significado de cada valor.

## 3. Índices e restrições

1. Os índices devem ser projetados com base nos cenários de consulta, evitando indexação excessiva.
2. A integridade deve ser garantida por restrições, sem depender de validação na camada de aplicação.
3. Chaves estrangeiras e regras de cascata devem ser declaradas explicitamente.

## 4. Gestão de migrações

1. Alterações de estrutura devem ser geridas por scripts de migração, versionados e enviados ao repositório.
2. As migrações devem ser reversíveis; alterações disruptivas devem oferecer um plano de migração de dados.
3. Os scripts de migração devem ser validados em ambiente de testes antes de serem aplicados em produção (ver [especificação de implantação e reversão](./deployment-and-rollback-specification.md)).

## 5. Segurança

1. Dados sensíveis devem ser armazenados criptografados ou anonimizados (ver [especificação de segurança e privacidade](./security-and-privacy-specification.md)).
2. Strings de conexão do banco de dados não devem ser enviadas ao repositório (corresponde à regra absoluta H3).

## Arquivos relacionados

- As linhas vermelhas sobre informações sensíveis estão na [especificação de segurança e privacidade](./security-and-privacy-specification.md)
- A gestão de alterações está na [especificação de implantação e reversão](./deployment-and-rollback-specification.md)
- A posição na arquitetura está na [especificação de documento de design de arquitetura](./architecture-design-document-specification.md)
