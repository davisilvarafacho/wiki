---
title: "Imutabilidade"
tipo: concept
dominio: tecnico
tags: [imutabilidade, funcional, estado, concorrencia]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-06-03-nubank-clojure-event-sourcing-pasquadev]
---

# Imutabilidade

Propriedade de um dado ou estrutura que, uma vez criado, não pode ser alterado. Mutações geram novos valores em vez de modificar os existentes.

## O problema que resolve

Em sistemas orientados a objetos com estado mutável compartilhado:
- Objeto A é instanciado com valor X
- Objeto B recebe referência ao mesmo objeto
- Objeto B muda o valor sem Objeto A saber
- Objeto A opera assumindo X, mas encontra Y
- Bug não reproduzível: depende da ordem de execução, do timing, do estado global

Esses bugs só aparecem em produção com condições específicas ("alinhamentos cósmicos"), são impossíveis de replicar em testes e quase impossíveis de corrigir com confiança. A imutabilidade torna esse cenário estruturalmente impossível: se o dado não pode mudar, ninguém pode mudar ele sem você saber.

## Imutabilidade em banco de dados

O princípio se estende ao banco. Um banco de dados mutável tradicional sobrescreve o estado — o passado é perdido. Um banco imutável (como o [[tecnico/entities/datomic]]) nunca apaga o que foi escrito: novos estados se acumulam, e o histórico completo é sempre acessível.

Isso é o que torna o [[tecnico/concepts/event-sourcing]] possível e poderoso: eventos são imutáveis por natureza (são fatos do passado), e a imutabilidade do banco garante que o histórico nunca seja corrompido.

## Relacionado

- [[tecnico/concepts/programacao-funcional]]
- [[tecnico/concepts/event-sourcing]]
- [[tecnico/concepts/side-effects]]
