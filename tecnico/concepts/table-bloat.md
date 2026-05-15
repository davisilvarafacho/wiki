---
title: "Table Bloat"
tipo: concept
dominio: tecnico
tags: [postgresql, banco-de-dados, performance, storage, vacuum, dead-tuples]
criado: 2026-05-14
atualizado: 2026-05-14
fontes: [tecnico/sources/2026-05-14-postgresql-mvcc-the-part-we-hate-the-most]
---

# Table Bloat

Crescimento excessivo e persistente do tamanho físico de uma tabela (ou seus índices) causado pelo acúmulo de *dead tuples* — versões de linhas expiradas que ainda ocupam espaço em disco mas não são mais visíveis a nenhuma transação ativa.

## Causa no PostgreSQL

Consequência direta do modelo [[tecnico/concepts/mvcc|MVCC]] append-only do PostgreSQL: cada UPDATE gera uma nova versão física da linha; a versão antiga torna-se dead tuple após o commit. Em workloads write-heavy, dead tuples se acumulam mais rápido do que o [[tecnico/concepts/autovacuum|autovacuum]] consegue remover.

O mesmo mecanismo causa **index bloat**: como PostgreSQL insere entradas nos índices para cada versão física, índices também incham junto com a tabela.

## O que o VACUUM regular faz (e não faz)

- **Faz:** remove dead tuples das páginas da tabela e reorganiza as tuples vivas dentro de cada página.
- **Não faz:** devolve páginas vazias ao sistema operacional. O arquivo da tabela no disco permanece do mesmo tamanho.

Isso significa que mesmo após um VACUUM bem-sucedido, a tabela ainda ocupa o espaço original no disco.

## Soluções

| Solução | Devolve espaço ao SO | Impacto em produção |
|---|---|---|
| `VACUUM` | Não | Baixo — roda online |
| `VACUUM FULL` | Sim | Alto — bloqueia a tabela inteira |
| `pg_repack` | Sim | Médio — reescreve sem bloquear (requer extensão) |

> **Regra prática:** evitar a necessidade de `VACUUM FULL` é melhor do que saber executá-lo. A prevenção passa por tuning do autovacuum e evitar transações longas.

## Sintomas

- Scans sequenciais lentos: PostgreSQL carrega todas as páginas em memória, incluindo as repletas de dead tuples.
- Estatísticas desatualizadas: dead tuples distorcem a contagem de linhas que o query planner usa, levando a planos ruins.
- Uso de memória inflado durante queries.

> **Exemplo concreto:** tabela com 10M live tuples + 40M dead tuples, 1KB/tuple. Full scan carrega 50GB, sendo 40GB de lixo.
