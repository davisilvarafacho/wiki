---
title: "Spec Driven chegou no limite — Harness Engineering é o próximo passo"
tipo: source
dominio: tecnico
url: https://www.youtube.com/watch?v=dLs-Pbn8stU
autor: "Waldemar Neto"
publicado: desconhecido
capturado: 2026-05-17
tipo_fonte: youtube-video
tags: [harness-engineering, spec-driven, agentes-ia, multi-agent, feed-forward, feedback]
criado: 2026-05-17
atualizado: 2026-05-17
---

# Spec Driven chegou no limite — Harness Engineering é o próximo passo

Canal: [Waldemar Neto - Dev Lab](https://www.youtube.com/channel/UCqmJGTdcMIRXOZuukHZ8TqA) | [Vídeo](https://www.youtube.com/watch?v=dLs-Pbn8stU)

---

## Sumário

- **Problema central:** agentes de IA sem harness geram diffs de 3.000 linhas onde metade não compila — não por falha do modelo, mas por falta de ambiente estruturado.
- **Harness** = tudo que envolve o modelo: instruções, estrutura do repositório, linters, testes, arquivos de progresso, scripts de setup. É o onboarding do engenheiro-agente. [[tecnico/concepts/harness-engineering]]
- O conceito ganhou tração em fevereiro de 2026 simultaneamente em posts da OpenAI, Anthropic e blog de Martin Fowler. Conclusão convergente: o gargalo não é a inteligência do modelo, é a qualidade do ambiente.
- **Dois mecanismos de controle** (base da engenharia de controle):
  - *Feed forward*: instruções preventivas antes da execução — spec, agents.md, regras de arquitetura, skills. [[tecnico/concepts/feed-forward]]
  - *Feedback/sensores*: detecção e correção após execução — linters, testes, type checkers, review agent. Ambos são necessários, como rota + recálculo do GPS.
- **Spec Driven é feed forward puro.** Resolve dois problemas (One Shot Hero e Vitória Prematura), mas deixa quatro em aberto.
- **6 falhas documentadas pela Anthropic** em agentes sem harness:
  1. *One Shot Hero* — tenta implementar tudo de uma vez, estoura a janela de contexto
  2. *Vitória Prematura* — para no meio declarando pronto quando o contexto fica grande
  3. *Amnésia entre sessões* — cada sessão começa do zero sem saber o que foi feito
  4. *Falsa conclusão* — marca feature como pronta sem testar end-to-end de verdade
  5. *Agente único julgando a própria obra* — o implementador nunca é neutro ao validar
  6. *Slope acumulado de qualidade* — mesmo 5% de degradação por funcionalidade resulta em código horrível ao fim de um sistema inteiro
- **Multi-agent orchestration:** separar agente implementador e agente validador em processos distintos. O implementador vai "fazer de tudo para implementar", o validador vai "fazer de tudo para validar" — missões opostas garantem neutralidade. [[tecnico/concepts/multi-agent-orchestration]]
- **Framework PBQ** (próprio do autor): spec driven + progress files + contratos entre agentes + loop de autocorreção. Custou $0,51 para rodar uma implementação completa com evaluation.
- Contratos entre agentes: no início do sprint, o agente implementador lista o que vai fazer; o validador confere se bate com a spec. Sem essa concordância, o validador sugere coisas fora do escopo e gera loop infinito.
- O Claude Code já está se instrumentando para orquestração de múltiplos agentes (mencionado pelo autor a partir de código vazado).
- Framework **get done** (para Claude) está começando a implementar harness — ainda instável, mas vale acompanhar.

## Takeaways

- Spec Driven é metade do harness (a metade preventiva). A outra metade são os sensores e a orquestração.
- O que força qualidade não é instrução — são ferramentas externas que retornam 0 ou 1. O agente não deve ser juiz de si mesmo.
- Progress files + git disciplinado + scripts de bootstrap são os mecanismos concretos para resolver amnésia entre sessões.
- A viabilidade econômica de harness engineering (OpenAI com 1 milhão de linhas sem intervenção humana; PBQ por $0,51) sugere que é o caminho para automação de sistemas inteiros.

## Conceitos e entidades criados

- [[tecnico/concepts/harness-engineering]] — criado
- [[tecnico/concepts/feed-forward]] — criado
- [[tecnico/concepts/multi-agent-orchestration]] — criado
- [[tecnico/concepts/spec-driven]] — criado (stub)
- [[tecnico/entities/autores/waldemar-neto]] — criado
