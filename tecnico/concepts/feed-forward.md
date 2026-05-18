---
title: "Feed Forward e Feedback em sistemas de agentes"
tipo: concept
dominio: tecnico
tags: [agentes-ia, harness-engineering, controle-de-sistemas, feed-forward, sensores]
fontes: [tecnico/sources/2026-05-17-harness-engineering-waldemar-neto]
criado: 2026-05-17
atualizado: 2026-05-17
---

# Feed Forward e Feedback em sistemas de agentes

Da engenharia de controle, dois mecanismos complementares para dirigir o comportamento de um sistema:

## Feed Forward (preventivo)

Instruções dadas *antes* da execução para aumentar a chance de acerto. Opera antes de qualquer erro acontecer.

Em sistemas de agentes de IA:
- Spec / plano de features
- `agents.md`, `CLAUDE.md` e arquivos de instrução
- Regras de arquitetura e convenções de código
- Skills e templates pré-definidos
- Progress files que descrevem o estado atual

É preventivo: reduz a probabilidade de o agente fazer a coisa errada.

## Feedback / Sensores (corretivo)

Observação do resultado *após* a execução, com sinal de correção quando algo saiu errado.

Em sistemas de agentes de IA:
- Linters e formatters
- Test runners (unitários, integração, e2e)
- Type checkers
- Review agents independentes

É corretivo: detecta erros e permite autocorreção. O ponto crítico é que **o agente não deve ser o juiz** — a ferramenta externa retorna 0 ou 1 sem ambiguidade. Se o agente julga sua própria implementação, ele vai "achar que tá bom o suficiente" sem rodar os testes.

## A analogia do GPS

Feed forward = a rota traçada antes de sair. Feedback = o recálculo quando você erra a saída.

Só a rota: você se perde no primeiro erro. Só o recálculo: você sai sem direção nenhuma. Precisa dos dois.

## Onde isso se encaixa no harness

[[harness-engineering]] é composto por feed forward + feedback + memória + orquestração. Spec Driven ([[spec-driven]]) cobre o feed forward. O que a maioria dos frameworks deixa descoberto são os sensores (feedback) e a orquestração ([[multi-agent-orchestration]]).
