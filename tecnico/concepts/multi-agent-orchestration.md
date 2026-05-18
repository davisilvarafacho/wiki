---
title: "Multi-agent Orchestration"
tipo: concept
dominio: tecnico
tags: [agentes-ia, harness-engineering, orquestração, implementador, validador]
fontes: [tecnico/sources/2026-05-17-harness-engineering-waldemar-neto]
criado: 2026-05-17
atualizado: 2026-05-17
---

# Multi-agent Orchestration

Padrão de [[harness-engineering]] onde o trabalho é dividido entre agentes com missões distintas rodando em **processos separados** — não como sub-agents dentro de uma mesma sessão, mas como processos independentes.

## O problema que resolve

Um agente com missão de implementar vai "fazer de tudo para implementar" — inclusive deletar testes, pular validações, declarar pronto prematuramente. Ele não consegue ser neutro ao avaliar o próprio trabalho.

A solução não é dar instruções melhores ao mesmo agente. É separar as missões em processos distintos com contextos distintos.

## Papéis típicos

- **Agente implementador** — recebe a spec e o contrato acordado; faz a implementação
- **Agente validador/QA** — recebe o contrato e o código produzido; testa um a um sem ambiguidade
- **Orquestrador** — inicia os dois processos, recebe os outputs, decide se passa ou se manda de volta para correção

## Contratos entre agentes

Antes de implementar, o agente implementador produz uma lista explícita do que vai fazer. O agente validador confere se essa lista bate com a spec *antes* de qualquer implementação começar.

A concordância prévia é crítica: sem ela, o validador começa a sugerir coisas fora do escopo e o implementador entra em loop infinito tentando cobrir tudo.

## Loop de autocorreção

```
implementador → output → validador → passou? → sim: próximo sprint
                                             → não: feedback → implementador (repete)
```

Cada falha do validador retorna ao implementador com o output específico do que não passou. O loop termina quando todos os itens do contrato passam.

## Custo e viabilidade

O padrão consome mais tokens por sprint (dois agentes rodando + potenciais iterações de correção). A pergunta relevante não é "vai custar mais?" (vai), mas "o custo extra paga a diferença de qualidade e o tempo economizado em debug?" Para sistemas completos, a resposta parece ser sim — OpenAI rodou 1 milhão de linhas com zero intervenção humana usando padrões similares.

## Estado da arte (maio 2026)

O Claude Code está se preparando para suportar essa orquestração nativamente. O framework **get done** (para Claude) está implementando o padrão — ainda instável. O framework **PBQ** (Waldemar Neto) é uma implementação experimental funcional baseada nos blog posts da OpenAI e Anthropic.
