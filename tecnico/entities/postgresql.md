---
title: "PostgreSQL"
tipo: entity
dominio: tecnico
tags: [banco-de-dados, sql, open-source, relacional, mvcc]
criado: 2026-05-14
atualizado: 2026-07-14
fontes: [tecnico/sources/2026-05-14-postgresql-mvcc-the-part-we-hate-the-most, tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]
---

# PostgreSQL

DBMS relacional open-source, o mais popular para novas aplicações desde ~2018. Confiável, rico em features, extensível e bem-adequado para a maioria dos workloads operacionais.

## Características gerais

- Totalmente ACID, suporta transações com [[tecnico/concepts/mvcc|MVCC]] para controle de concorrência.
- Extensível: suporta extensões, tipos customizados, funções em múltiplas linguagens (PL/pgSQL, Python, etc.).
- Popular em cloud: AWS RDS, Aurora, Supabase, Neon, entre outros, são baseados em PostgreSQL.
- Predecessores: MySQL dominou nos anos 2000, MongoDB nos anos 2010.

## Ponto fraco: implementação de MVCC

A implementação de MVCC do PostgreSQL é baseada em **append-only storage** e **O2N version chains** — um design dos anos 1980 que gera quatro problemas estruturais em workloads write-heavy:

1. **Version Copying** — copia a linha inteira em cada UPDATE (vs. delta no MySQL/Oracle).
2. **Table Bloat** — dead tuples acumulam; `VACUUM` regular não devolve espaço ao SO.
3. **Secondary Index Maintenance** — todo update não-HOT atualiza todos os índices.
4. **Vacuum Management** — [[tecnico/concepts/autovacuum|autovacuum]] difícil de tunar; bloqueado por transações longas.

Otimização mitigante: [[tecnico/concepts/hot-update|HOT update]] (~46% dos updates se qualificam).

Ver análise detalhada em [[tecnico/sources/2026-05-14-postgresql-mvcc-the-part-we-hate-the-most]].

## Comparação com concorrentes em MVCC

MySQL (InnoDB) e Oracle armazenam **deltas** das mudanças (não a linha inteira) e usam **identificadores lógicos** nos índices secundários (não endereços físicos), evitando os problemas #1 e #3.

## Gestão de índices e monitoramento

Índices aceleram SELECT mas penalizam INSERT/UPDATE — o Django ORM pode gerar índices redundantes que exigem checagem e remoção manual. [pghero](https://github.com/ankane/pghero) é citado como dashboard de performance para identificar slow queries e índices duplicados. Ver [[tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]].

## Histórico relevante

- Projetado por Michael Stonebraker (Berkeley), com suporte a MVCC desde o design original de 1987.
- O projeto `zheap` (EnterpriseDB, 2013–2021) tentou modernizar o storage engine com delta storage, mas parece descontinuado.
- **Caso Uber (2016):** migraram de PostgreSQL para MySQL por problemas de write amplification em tabelas com muitos índices secundários — o exemplo mais famoso dos problemas #3 e #4.
