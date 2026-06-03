---
title: "Event Sourcing"
tipo: concept
dominio: tecnico
tags: [event-sourcing, eventos, imutabilidade, cqrs, datomic, arquitetura]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-06-03-nubank-clojure-event-sourcing-pasquadev]
---

# Event Sourcing

Padrão arquitetural em que o estado de um sistema não é persistido diretamente — o que é persistido são os **eventos** (fatos imutáveis sobre o que aconteceu). O estado atual é sempre derivado reaplicando o histórico de eventos.

## Princípio fundamental

Em um banco de dados tradicional (state-based), você persiste o estado atual e sobrescreve quando muda:

```
conta: { saldo: 1000 }
→ saque de 200
conta: { saldo: 800 }   ← estado anterior perdido
```

Em Event Sourcing, você persiste os eventos:

```
evento: { tipo: "depósito", valor: 1200, ts: ... }
evento: { tipo: "saque", valor: 200, ts: ... }
→ saldo = reaplica eventos = 1000
```

O saldo não existe no banco. Ele é calculado na leitura.

## Por que eventos são imutáveis

Um evento é um **fato do passado**: "o saque de R$ 200 aconteceu no dia X às Y horas". Fatos não mudam. Se houve um erro, você não edita o evento — você cria um novo evento de correção. Isso preserva o histórico completo e auditável.

## Vantagens

- **Auditoria nativa** — o histórico completo é o modelo de dados, não um log separado; bancos financeiros, sistemas com requisitos regulatórios ganham isso de graça
- **Debugging 100% reproduzível** — para reproduzir qualquer bug, basta salvar os eventos que aconteceram e dar play no algoritmo; você consegue escrever testes para 100% dos bugs
- **Estado em qualquer ponto no tempo** — "como estava a conta em 15/03 às 14h?" é trivial
- **Flexibilidade de projeções** — o mesmo histórico de eventos pode gerar múltiplas visões (projeções) com algoritmos diferentes; se a regra de negócio muda, você reaplica os eventos com a nova lógica

## Desafios

- **Curva de aprendizado alta** — é uma mudança de paradigma; pensar em eventos em vez de estado é não-natural para quem vem de CRUD
- **Event log cresce indefinidamente** — necessidade de estratégia de snapshots (checkpoints periódicos do estado calculado) para não ter que reaplica todo o histórico em cada leitura
- **Raro no mercado** — sistemas com essa arquitetura geralmente são bancos, sistemas de trading, apostas esportivas — onde o histórico tem valor intrínseco

## Relação com CQRS

Event Sourcing e CQRS (Command Query Responsibility Segregation) são frequentemente usados juntos mas são conceitos distintos:
- **Event Sourcing** — como você persiste: eventos, não estado
- **CQRS** — como você lê: separação entre o modelo de escrita (comandos → eventos) e o modelo de leitura (projeções otimizadas para query)

## Relação com Datomic e Nubank

O [[tecnico/entities/datomic]] implementa Event Sourcing no nível do banco de dados — é a materialização dessa arquitetura como produto. O [[tecnico/entities/nubank]], ao escolher Datomic + [[tecnico/entities/clojure]], aplicou essa arquitetura em escala de 100M de clientes e sistema financeiro real.

## Relacionado

- [[tecnico/concepts/imutabilidade]]
- [[tecnico/concepts/programacao-funcional]]
- [[tecnico/entities/datomic]]
