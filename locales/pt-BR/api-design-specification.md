# Especificação de design de API

> Problema que este arquivo resolve: definir os princípios de consistência e as convenções do design de interfaces, garantindo que a API seja fácil de usar, previsível e evolutiva.

## 1. Princípios de design

1. Nomenclatura consistente: recursos e operações do mesmo tipo usam regras de nomenclatura uniformes.
2. Previsibilidade: operações com a mesma semântica têm a mesma estrutura.
3. Explícito em vez de implícito: valores padrão, campos obrigatórios e comportamento em caso de erro devem ser explícitos.
4. Compatibilidade retroativa: as alterações devem priorizar a manutenção da compatibilidade; alterações disruptivas devem ser versionadas (ver [especificação de gestão de versões](./version-management-specification.md)).

## 2. Convenções obrigatórias

1. **Nomenclatura**: regras de nomenclatura de recursos, métodos e campos.
2. **Parâmetros**: tipo, obrigatoriedade, valor padrão, faixa de valores.
3. **Erros**: estrutura uniforme de erro, códigos de erro, status HTTP ou mecanismo equivalente.
4. **Paginação e filtragem**: convenções de paginação, ordenação e filtragem em cenários de grande volume de dados.
5. **Idempotência**: garantia de idempotência das operações de escrita.
6. **Limitação de taxa e cota**: limites de frequência e resposta ao excesso.
7. **Versão**: estratégia de versão da API e forma de evolução.

## 3. Regras obrigatórias

1. As respostas de erro devem conter códigos de erro localizáveis e descrições, sem expor detalhes internos da implementação.
2. Alterações disruptivas devem elevar a versão e oferecer um período de migração (ver [especificação de registro de alterações](./changelog-specification.md)).
3. As interfaces devem ter documentação correspondente, com campos completos (ver [especificação de documentação de API](./api-documentation-specification.md)).

## Arquivos relacionados

- Para a forma de redigir a documentação de referência de API, ver a [especificação de documentação de API](./api-documentation-specification.md)
- Para questões de segurança, ver a [especificação de segurança e privacidade](./security-and-privacy-specification.md)
- O tratamento de erros é uma decisão de engenharia; ver [como escrever funcionalidades e decisões de engenharia](./features-and-engineering-tradeoffs-guide.md)
