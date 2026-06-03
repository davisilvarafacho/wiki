---
title: "Nubank"
tipo: entity
dominio: tecnico
tags: [nubank, fintech, clojure, datomic, event-sourcing, brasil]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-06-03-nubank-clojure-event-sourcing-pasquadev]
---

# Nubank

Maior banco digital da América Latina. Fundado no Brasil, chegou a 100 milhões de clientes. Serviços: conta, crédito, pagamentos — sistema financeiro completo em escala.

## Stack técnica

- **Linguagem principal:** [[tecnico/entities/clojure]] — funcional, roda na JVM; escolhido desde a fundação
- **Banco de dados:** [[tecnico/entities/datomic]] — banco imutável com Event Sourcing nativo
- **Paradigma:** [[tecnico/concepts/programacao-funcional]] + DDD + [[tecnico/concepts/event-sourcing]]

## Decisão arquitetural

A fundação intelectual das escolhas técnicas do Nubank vem do paper "Out of the Tar Pit" (Moseley & Marks): mutable state e side effects são a fonte primária de complexidade acidental em sistemas grandes. Com essa premissa, [[tecnico/entities/clojure]] (imutabilidade por padrão) e [[tecnico/entities/datomic]] (banco imutável) foram escolhas naturais.

O Nubank sabia que seria grande ou morreria tentando — o modelo de negócio não funciona em escala pequena. Então as decisões técnicas foram tomadas para sistemas de escala máxima desde o início.

## Por que Clojure na JVM

Acesso ao ecossistema maduro de bibliotecas Java sem precisar reinventá-las — reinventar seria um desvio da missão central (construir o banco). A JVM como runtime resolve infraestrutura; Clojure como linguagem resolve o paradigma.
