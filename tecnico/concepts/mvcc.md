---
title: "MVCC — Multi-Version Concurrency Control"
tipo: concept
dominio: tecnico
tags: [banco-de-dados, concorrência, transações, postgresql, mysql, oracle]
criado: 2026-05-14
atualizado: 2026-05-14
fontes: [tecnico/sources/2026-05-14-postgresql-mvcc-the-part-we-hate-the-most]
---

# MVCC — Multi-Version Concurrency Control

Mecanismo que permite múltiplas queries lerem e escreverem no banco simultaneamente sem se bloquearem, mantendo múltiplas **versões físicas** de cada linha lógica. Cada transação enxerga um snapshot consistente do banco no momento em que começou (*snapshot isolation*). Writers não bloqueiam readers.

Origem: dissertação de David Reed no MIT, 1978. Primeira implementação comercial: InterBase (1980s). Hoje presente em praticamente todo DBMS que suporta transações.

## Ideia central

O DBMS nunca sobrescreve uma linha existente. Em vez disso, cria uma nova versão física da linha para cada UPDATE. A versão antiga fica acessível a transações em andamento que precisam do estado anterior; quando nenhuma transação mais a enxerga, ela torna-se uma *dead tuple*.

## Decisões de design

Todo DBMS com MVCC precisa decidir:

1. **Como armazenar updates:** cópia inteira da linha (*append-only*) ou apenas o delta das mudanças.
2. **Como encontrar a versão correta:** ordem de traversal da version chain — N2O (newest-to-oldest) ou O2N (oldest-to-newest).
3. **Como remover versões expiradas:** vacuum, undo log, ou garbage collection automático.

Essas decisões são interdependentes. A escolha do PostgreSQL nos anos 1980 no item 1 criou as consequências nos itens 2 e 3 que existem até hoje.

## Abordagens comparadas

| DBMS | Armazenamento | Version chain | Índice secundário |
|---|---|---|---|
| PostgreSQL | Append-only (linha inteira) | O2N | Endereço físico |
| MySQL (InnoDB) | Delta (undo log) | N2O | Identificador lógico |
| Oracle | Delta (undo log) | N2O | Identificador lógico |

## PostgreSQL: append-only + O2N

PostgreSQL copia a linha inteira a cada UPDATE e armazena a nova versão no mesmo heap da tabela. A version chain usa ordem O2N — o índice aponta para a versão mais antiga; o DBMS percorre até encontrar a atual.

Para evitar a travessia completa, insere entradas em **todos os índices** para cada nova versão física. Isso amplifica I/O de escritas e tamanho dos índices.

A otimização [[tecnico/concepts/hot-update|HOT]] evita essa amplificação quando a nova versão cabe na mesma página e não toca colunas indexadas (~46% dos updates).

Versões expiradas são removidas pelo [[tecnico/concepts/autovacuum|autovacuum]], mas o espaço em disco só é devolvido com `VACUUM FULL` ou `pg_repack`, causando [[tecnico/concepts/table-bloat|table bloat]].

## Quatro problemas do modelo PostgreSQL

1. **Version Copying** — copia linha inteira mesmo que 1 de 1000 colunas mude.
2. **Table Bloat** — dead tuples acumulam; vacuum regular não devolve espaço ao SO.
3. **Secondary Index Maintenance** — todo update não-HOT atualiza todos os índices da tabela.
4. **Vacuum Management** — autovacuum difícil de tunar; bloqueado por transações longas.

Ver análise completa em [[tecnico/sources/2026-05-14-postgresql-mvcc-the-part-we-hate-the-most]].
