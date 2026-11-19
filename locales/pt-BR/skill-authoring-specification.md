# Especificação de redação de Skill

> Problema que este arquivo resolve: definir a estrutura, as condições de acionamento e a forma de carregamento progressivo ao encapsular o conjunto de especificações como Skill, garantindo que o Skill seja descobrível, sustentável e não duplique conteúdo.

## 1. Estrutura de diretórios

O Skill adota a estrutura de “ponto de entrada + recursos sob demanda”:

```text
skill-name/
├── SKILL.md          obrigatório: metadados + fluxo principal
├── references/       corpo da especificação, carregado sob demanda
└── assets/           modelos e recursos (opcional)
```

## 2. Requisitos do SKILL.md

1. Os metadados incluem `name` e `description`; a descrição deve explicitar “o que faz + quando usar”, de modo a permitir o acionamento.
2. O corpo mantém apenas as regras e o fluxo centrais permanentes; conteúdos detalhados de consulta vão para `references/`.
3. Adotar redação imperativa ou infinitiva, evitando a segunda pessoa.
4. Ao referenciar recursos, indicar o caminho explícito e a condição de “quando ler”.

## 3. Regras obrigatórias

1. O corpo da especificação é mantido em um único lugar: o Skill referencia os arquivos deste conjunto de especificações e não copia o texto integral, evitando a divergência entre duas cópias.
2. Um Skill faz apenas uma coisa; é proibido concentrar múltiplas responsabilidades no mesmo Skill.
3. As condições de acionamento devem indicar frases concretas, evitando acionamentos demasiado amplos.
4. A versão é atualizada em sincronia com a versão do conjunto de especificações.

## Arquivos relacionados

- A estrutura da lista de metadados está em [especificação de metadados legíveis por máquina](./machine-readable-metadata-specification.md)
- A responsabilidade única da documentação está em [matriz de documentação](./document-matrix.md)
- As convenções de invocação de Agent estão em [especificação de invocação de Agent e de prompts](./agent-invocation-and-prompt-specification.md)
