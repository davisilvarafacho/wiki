---
title: "The Part of PostgreSQL We Hate the Most"
tipo: source
dominio: tecnico
tags: [postgresql, mvcc, banco-de-dados, performance, vacuum, dead-tuples]
criado: 2026-05-14
atualizado: 2026-05-14
autor: Andy Pavlo
publicado: 2023-04-26
url: https://www.cs.cmu.edu/~pavlo/blog/2023/04/the-part-of-postgresql-we-hate-the-most.html
---

# The Part of PostgreSQL We Hate the Most

Andy Pavlo (CMU / OtterTune), 2023. Crítica técnica da implementação de MVCC do PostgreSQL com comparação sistemática a MySQL e Oracle.

## Sumário

- PostgreSQL é o DBMS "queridinho da internet" desde ~2018, mas sua implementação de [[tecnico/concepts/mvcc|MVCC]] é a pior entre os grandes DBMSs relacionais — opinião embasada por paper de 2018 no VLDB e dados de produção da OtterTune.
- PostgreSQL usa **append-only storage**: a cada UPDATE, copia a linha inteira para um novo slot físico. MySQL e Oracle gravam apenas o **delta** das mudanças (equivalente a um `git diff`).
- Utiliza ordem **O2N** (oldest-to-newest) na version chain: índices apontam para a versão mais antiga; o DBMS percorre a cadeia até a versão correta. A maioria dos DBMSs usa N2O.
- Para compensar a travessia O2N, PostgreSQL insere entradas em **todos os índices** para cada nova versão física, amplificando I/O de escritas e tamanho dos índices.
- Otimização **HOT** (Heap-Only Tuple): se a nova versão cabe na mesma página e não altera colunas indexadas, o DBMS reutiliza as entradas de índice existentes. Ocorre em ~46% dos updates.
- **Problema #1 — Version Copying:** uma mudança em 1 coluna de uma tabela com 1000 colunas gera nova versão com todas as 1000 colunas.
- **Problema #2 — Table Bloat:** dead tuples acumulam no espaço da tabela. O `VACUUM` regular remove as tuplas mas não devolve espaço ao SO — só `VACUUM FULL` ou `pg_repack` o fazem, a custo alto de performance.
- **Problema #3 — Secondary Index Maintenance:** todo update não-HOT atualiza todos os índices (primário + secundários), mesmo os nunca usados. Oracle/MySQL armazenam identificadores lógicos nos índices secundários, evitando isso. Este foi o motivo do [caso Uber de 2016](https://www.uber.com/blog/postgres-to-mysql-migration/).
- **Problema #4 — Vacuum Management:** `autovacuum_vacuum_scale_factor` padrão de 20% é alto demais para tabelas grandes (dispara só após 20M updates em tabela de 100M linhas). Transações longas bloqueiam o autovacuum, criando ciclo vicioso.
- O projeto `zheap` (EnterpriseDB, 2013–2021) tentou substituir o storage engine por delta storage, mas parece descontinuado.
- O design é legado dos anos 1980, anterior ao padrão log-structured dos anos 1990. Nenhum DBMS novo deveria implementar MVCC desta forma.

## Citações relevantes

> "We did not find another DBMS doing MVCC the way PostgreSQL does it. Its design is a relic of the 1980s and before the proliferation of log-structured system patterns from the 1990s."

> "Our analysis of OtterTune customers' PostgreSQL databases shows that roughly 46% of updates use the HOT optimization on average."

> "To love something is to be willing to work with its flaws."

## Takeaways

1. O custo oculto do PostgreSQL em workloads write-heavy está no MVCC: version copying, bloat e amplificação de índices.
2. Entender HOT updates é essencial para otimizar tabelas write-heavy — manter colunas indexadas estáveis e fillfactor menor que 100 favorece HOT.
3. Autovacuum precisa ser tuned por tabela em produção; o padrão global de 20% é insuficiente para tabelas grandes.
4. `VACUUM FULL` e `pg_repack` são "cirurgias pesadas" — evitar a necessidade delas é melhor do que saber executá-las.
5. MySQL e Oracle evitam os problemas #1 e #3 por design (delta storage + logical secondary indexes).

## Páginas relacionadas

- [[tecnico/concepts/mvcc]]
- [[tecnico/concepts/table-bloat]]
- [[tecnico/concepts/hot-update]]
- [[tecnico/concepts/autovacuum]]
- [[tecnico/entities/postgresql]]
- [[tecnico/entities/autores/andy-pavlo]]
