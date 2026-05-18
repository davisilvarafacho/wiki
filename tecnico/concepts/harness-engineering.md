---
title: "Harness Engineering"
tipo: concept
dominio: tecnico
tags: [agentes-ia, harness, spec-driven, feed-forward, feedback, multi-agent]
fontes: [tecnico/sources/2026-05-17-harness-engineering-waldemar-neto]
criado: 2026-05-17
atualizado: 2026-05-17
---

# Harness Engineering

O modelo (LLM) é o engenheiro. O **harness** é tudo que está ao redor dele: o ambiente operacional que transforma um modelo poderoso em um agente confiável.

Componentes do harness:

- **Feed forward** — instruções preventivas: spec, agents.md, regras de arquitetura, skills, documentação de progresso. Diz ao agente *o que* fazer e *como*. [[feed-forward]]
- **Sensores/feedback** — detecção pós-execução: linters, testes, type checkers, review agents. Detecta erros e permite autocorreção. O agente não julga; a ferramenta retorna 0 ou 1. [[feed-forward]]
- **Memória/estado** — progress files, git disciplinado, scripts de bootstrap que reconstroem o contexto entre sessões.
- **Orquestração** — separação entre agentes com missões distintas (implementador vs. validador). [[multi-agent-orchestration]]

## Por que é necessário

Analogia: um engenheiro brilhante contratado sem onboarding — sem README, sem arquitetura documentada, sem CI, sem testes — vai errar. Não por incompetência, mas por falta de contexto. O harness é o onboarding desse engenheiro.

O gargalo de desenvolvimento com agentes de IA já não é a inteligência do modelo. É a qualidade do ambiente onde ele opera. Esse diagnóstico convergiu em fevereiro de 2026 em posts da OpenAI, Anthropic e Martin Fowler.

## Relação com Spec Driven

[[spec-driven]] é um tipo de harness — especificamente, é feed forward puro. Resolve dois dos seis problemas clássicos (One Shot Hero e Vitória Prematura), mas não cobre:

- Amnésia entre sessões
- Validação real (sensores externos)
- Orquestração multi-agente
- Slope acumulado de qualidade

Harness Engineering completo = spec driven + sensores + orquestração + memória.

## Falhas de agente sem harness (documentadas pela Anthropic)

1. **One Shot Hero** — tenta implementar tudo de uma vez; estoura a janela de contexto
2. **Vitória Prematura** — declara pronto quando o contexto fica grande demais
3. **Amnésia entre sessões** — cada sessão começa do zero
4. **Falsa conclusão** — marca feature como pronta sem testar end-to-end
5. **Agente único julgando a própria obra** — o implementador nunca é neutro
6. **Slope acumulado** — 5% de degradação por funcionalidade = sistema horrível ao fim
