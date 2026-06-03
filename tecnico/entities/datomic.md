---
title: "Datomic"
tipo: entity
dominio: tecnico
tags: [datomic, banco-de-dados, imutabilidade, event-sourcing, clojure, nubank]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-06-03-nubank-clojure-event-sourcing-pasquadev]
---

# Datomic

Banco de dados imutável criado por Rich Hickey (o mesmo criador do [[tecnico/entities/clojure]]). Implementa [[tecnico/concepts/event-sourcing]] no nível do banco: dados escritos nunca são deletados ou sobrescritos — o histórico completo é sempre preservado.

## O que significa "imutável" no Datomic

Não significa que nada muda. Significa que você nunca perde o histórico dos estados anteriores à medida que as coisas mudam. Cada write é um novo fato (datom) acrescentado ao histórico — os fatos anteriores permanecem intactos.

Isso permite:
- Consultar o estado do banco em qualquer ponto no tempo
- Rastrear a evolução de qualquer dado
- Auditoria completa e nativa (sem log separado)
- Debugging de produção com replay do estado histórico

## Por que é relevante para bancos financeiros

Bancos têm requisitos de auditoria e regulatórios que exigem histórico completo de todas as transações. Com Datomic, isso é o modelo de dados padrão — não uma feature adicional. O que em bancos tradicionais exigiria tabelas de log separadas e processos de reconciliação é nativo no Datomic.

## Relação com o Nubank

[[tecnico/entities/nubank]] usa Datomic como banco principal, combinado com [[tecnico/entities/clojure]] e a arquitetura de [[tecnico/concepts/event-sourcing]]. A escolha foi motivada pelo paper "Out of the Tar Pit" e pelo insight de que imutabilidade resolve a categoria de bugs mais difícil em sistemas grandes.

## Relacionado

- [[tecnico/concepts/event-sourcing]]
- [[tecnico/concepts/imutabilidade]]
- [[tecnico/entities/clojure]]
