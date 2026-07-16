---
title: "Autovacuum"
tipo: concept
dominio: tecnico
tags: [postgresql, mvcc, manutenção, performance, dead-tuples, vacuum]
criado: 2026-05-14
atualizado: 2026-05-14
fontes: [tecnico/sources/2026-05-14-postgresql-mvcc-the-part-we-hate-the-most]
---

# Autovacuum

Processo de manutenção automática do [[tecnico/entities/postgresql|PostgreSQL]] responsável por remover *dead tuples* das tabelas e atualizar estatísticas do query planner. É a resposta operacional ao problema de acúmulo de versões obsoletas gerado pelo modelo [[tecnico/concepts/mvcc|MVCC]] append-only.

## O que faz

1. Executa scans sequenciais nas páginas modificadas desde o último run.
2. Identifica dead tuples (versões não visíveis a nenhuma transação ativa).
3. Remove as dead tuples e reorganiza as live tuples dentro de cada página.
4. Atualiza estatísticas das tabelas para o query planner (`pg_statistic`).

**Não devolve espaço ao sistema operacional** — esse trabalho é do `VACUUM FULL` ou `pg_repack`. Ver [[tecnico/concepts/table-bloat|table bloat]].

## Parâmetros-chave

- **`autovacuum_vacuum_scale_factor`** (padrão: `0.20`): fração da tabela que precisa ser modificada para disparar o vacuum. Em uma tabela de 100M linhas, só dispara após 20M updates — deixando acumular muitas dead tuples em tabelas grandes.
- **`autovacuum_vacuum_threshold`** (padrão: `50`): número mínimo absoluto de dead tuples antes de disparar (somado à condição do scale_factor).
- **`autovacuum_analyze_scale_factor`** / **`autovacuum_analyze_threshold`**: equivalentes para disparo de atualização de estatísticas.

> **Prática recomendada:** sobrescrever `autovacuum_vacuum_scale_factor` por tabela em tabelas grandes, usando valor menor (ex: `0.01`).
>
> ```sql
> ALTER TABLE orders SET (autovacuum_vacuum_scale_factor = 0.01);
> ```

## Vulnerabilidade: transações longas

O autovacuum **não pode remover** dead tuples ainda visíveis a alguma transação ativa — mesmo que ela nunca acesse aquelas linhas. Uma única transação longa bloqueia o vacuum de toda a base, criando ciclo vicioso:

```
dead tuples acumulam
  → estatísticas desatualizadas
    → planos ruins
      → queries mais lentas
        → mais transações longas
          → autovacuum mais bloqueado
```

Monitorar e matar transações `idle in transaction` longas é higiene essencial em produção.

## Monitoramento útil

```sql
-- tabelas com mais dead tuples
SELECT relname, n_dead_tup, n_live_tup, last_autovacuum
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;
```
