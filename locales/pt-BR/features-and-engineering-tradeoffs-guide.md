# Como escrever funcionalidades e decisões de engenharia

> Problema que este arquivo resolve: definir a redação dos capítulos “Funcionalidades principais” e “Detalhes de design e decisões de engenharia” do README, apresentando, respectivamente, a estrutura em cinco partes das funcionalidades e as dez categorias de cobertura obrigatória das decisões de engenharia.

## 1. Redação das funcionalidades principais

Cada funcionalidade é escrita segundo a estrutura de cinco partes a seguir; a ausência de qualquer parte impede que seja listada como funcionalidade.

1. **Nome da funcionalidade**: no máximo 15 caracteres, em sintagma nominal.
2. **Valor**: o problema concreto resolvido e a consequência de não resolvê-lo.
3. **Forma de implementação**: a tecnologia, o mecanismo ou o algoritmo adotado, indicando os arquivos ou funções críticos.
4. **Diferenciação**: as dimensões de comparação com soluções comuns, que devem ser objetivamente verificáveis.
5. **Evidência**: dados de teste, resultados de benchmark, localização no código, itens de configuração ou passos reproduzíveis.

Restrições:
1. A evidência deve ser reproduzível; funcionalidades sem evidência possível devem ser marcadas com “【Pendente: forma de verificação】” e não podem ser substituídas por descrições qualitativas.
2. Evidências de desempenho devem indicar o ambiente e o método de teste.
3. O objeto de comparação deve ser uma solução nomeada; é vedado usar referências vagas como “a solução tradicional” ou “outras ferramentas”.

## 2. Redação dos detalhes de design e das decisões de engenharia

Cada item é escrito segundo três partes — “cenário → forma de tratamento → motivo” —, explicando por que se optou por esse design e não por outro.

Categorias de cobertura obrigatória:
1. Entradas anômalas e casos de limite (valores nulos, comprimentos excessivos, caracteres inválidos, valores numéricos extremos)
2. Estratégias de timeout, tentativa novamente, backoff, circuit breaker e degradação
3. Níveis de cache, política de invalidação, proteção contra cache penetration e cache avalanche
4. Controle de concorrência, granularidade de locks, consistência de dados e idempotência
5. Otimização de memória e de armazenamento (processamento em lotes, leitura e escrita em streaming, compressão)
6. Medidas de segurança (autenticação e autorização, limitação de taxa, validação de entrada, anonimização de informações sensíveis)
7. Detalhes de interação (prevenção de toque acidental, confirmação secundária, possibilidade de desfazer, estados de carregamento e vazio)
8. Base para os valores dos parâmetros padrão
9. Estratégia de compatibilidade retroativa e adaptação multiplataforma
10. Tratamento de rede fraca e modo offline, recuperação de estado

## Arquivos relacionados

- Correspondem aos capítulos 4 e 5 do README; ver [especificação de seções do README](./readme-sections-specification.md)
- A redação de dados de desempenho deve seguir os requisitos de exatidão; ver [especificação geral de redação](./general-writing-specification.md)
- As evidências das funcionalidades e a cobertura das decisões de compromisso pertencem aos portões G4/G5; ver [portão de qualidade](./quality-gate.md)
