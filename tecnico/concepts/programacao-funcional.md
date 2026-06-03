---
title: "Programação Funcional"
tipo: concept
dominio: tecnico
tags: [paradigma, funcional, imutabilidade, side-effects, clojure, scala, haskell]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-06-03-nubank-clojure-event-sourcing-pasquadev]
---

# Programação Funcional

Paradigma de programação que modela computação como avaliação de funções matemáticas. As duas propriedades centrais são [[tecnico/concepts/imutabilidade]] (dados não mudam depois de criados) e ausência de [[tecnico/concepts/side-effects]] (uma função só faz o que seu nome diz — nada mais, nada escondido).

## O que é

Uma função no sentido funcional puro:
- Recebe um input
- Processa
- Retorna um output
- Não altera estado externo, não depende de estado externo

Se você chamar a mesma função com os mesmos argumentos, sempre terá o mesmo resultado — isso se chama *referencialmente transparente* e é o que torna o código previsível, testável e debugável.

## Por que importa em sistemas grandes

O paper "Out of the Tar Pit" (Moseley & Marks) argumenta que mutable state e side effects são a fonte primária de complexidade acidental em sistemas de software grandes. O Nubank construiu toda a sua stack com essa premissa.

Bugs de estado compartilhado — aqueles que só aparecem com "alinhamentos cósmicos" de condições de runtime, são impossíveis de reproduzir e não têm teste — são estruturalmente impossíveis em código verdadeiramente funcional. Não porque o programador é cuidadoso, mas porque a linguagem/paradigma torna o estado mutável compartilhado inexpressável.

## Linguagens funcionais relevantes

- **[[tecnico/entities/clojure]]** — Lisp na JVM; imutabilidade por padrão; linguagem principal do Nubank
- **Scala** — funcional e orientado a objetos na JVM; usado em sistemas de alta escala (Spark, Kafka)
- **Haskell** — funcional puro; side effects isolados no sistema de tipos (monads)
- **Elixir** — funcional, baseado em Erlang; concorrência por atores; sistemas distribuídos tolerantes a falhas

## Relação com outros conceitos

- [[tecnico/concepts/event-sourcing]] — Event Sourcing aplica imutabilidade ao banco: eventos são fatos do passado, imutáveis; o estado é derivado, nunca persistido diretamente
- [[tecnico/concepts/side-effects]] — em programação funcional, side effects não são proibidos — são *explicitados e isolados*; a diferença é visibilidade vs. efeito oculto
- DDD (Domain-Driven Design) — programação funcional combinada com DDD produz domínios onde as regras de negócio ficam no centro, funções puras, e side effects (banco, e-mail, API) ficam na periferia

## A metáfora do futebol

Jogar futebol é simples — mas jogar futebol simples é muito difícil. Escrever código é simples — mas escrever código simples é muito difícil. Programação funcional é o paradigma que força a simplicidade: sistemas complexos são decompostos em funções pequenas, puras e composíveis.
