---
title: "Spec Driven Development"
tipo: concept
dominio: tecnico
tags: [agentes-ia, harness-engineering, feed-forward, spec, planejamento]
fontes: [tecnico/sources/2026-05-17-harness-engineering-waldemar-neto]
criado: 2026-05-17
atualizado: 2026-05-17
---

# Spec Driven Development

*Stub — a ser expandido quando houver fonte dedicada.*

Metodologia de desenvolvimento com agentes de IA onde o trabalho começa por uma especificação estruturada — user stories, acceptance criteria, tasks — antes de qualquer geração de código.

## O que resolve

Dentro do framework de [[harness-engineering]], spec driven cobre a camada de **feed forward** ([[feed-forward]]): instrui o agente *antes* da execução sobre o que fazer e o que significa "pronto".

Falhas clássicas que spec driven resolve:
- **One Shot Hero** — a spec quebra o sistema em sprints/tasks menores
- **Vitória Prematura** — a spec define criteriosamente o que significa concluído

## O que não resolve sozinho

Spec driven é feed forward puro. Não cobre:
- Amnésia entre sessões (falta progress files, bootstrap scripts)
- Validação real (falta sensores externos — linters, testes forçados)
- Orquestração multi-agente ([[multi-agent-orchestration]])
- Slope acumulado de qualidade

Harness engineering completo = spec driven + sensores + orquestração + memória entre sessões.

## Referências

- [[tecnico/sources/2026-05-17-harness-engineering-waldemar-neto]] — análise de Waldemar Neto posicionando spec driven dentro do harness
