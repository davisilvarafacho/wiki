---
title: "Clojure"
tipo: entity
dominio: tecnico
tags: [clojure, lisp, jvm, funcional, nubank]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-06-03-nubank-clojure-event-sourcing-pasquadev]
---

# Clojure

Linguagem de programação funcional da família Lisp, criada por Rich Hickey em 2007. Roda na JVM (Java Virtual Machine), o que dá acesso ao ecossistema completo de bibliotecas Java.

## Características principais

- **Funcional** — imutabilidade como default; estruturas de dados persistentes e imutáveis
- **Lisp** — sintaxe homoicônica (código é dado); macros poderosas; REPL interativo
- **JVM** — interoperabilidade com Java; acesso a bibliotecas maduras; performance da JVM
- **Dinâmica** — tipagem dinâmica; desenvolvimento interativo via REPL

## Por que o Nubank escolheu Clojure

Ver [[tecnico/entities/nubank]]. A combinação de [[tecnico/concepts/programacao-funcional]] com o ecossistema da JVM resolveu dois problemas ao mesmo tempo: o paradigma correto para sistemas complexos e acesso a infraestrutura madura sem reinventar a roda.

## Relacionado

- [[tecnico/entities/datomic]] — banco de dados imutável criado pelo mesmo autor (Rich Hickey)
- [[tecnico/concepts/programacao-funcional]]
