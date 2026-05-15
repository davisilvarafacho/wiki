---
title: "HOT Update — Heap-Only Tuple"
tipo: concept
dominio: tecnico
tags: [postgresql, mvcc, otimização, storage, índices, performance]
criado: 2026-05-14
atualizado: 2026-05-14
fontes: [tecnico/sources/2026-05-14-postgresql-mvcc-the-part-we-hate-the-most]
---

# HOT Update — Heap-Only Tuple

Otimização do [[tecnico/entities/postgresql|PostgreSQL]] que evita a criação de novas entradas nos índices ao atualizar uma linha, reduzindo a amplificação de I/O causada pelo modelo [[tecnico/concepts/mvcc|MVCC]] append-only. Quando um update é HOT, o índice continua apontando para a versão antiga, e o PostgreSQL encontra a nova versão percorrendo a version chain dentro da mesma página heap.

## Condições para um HOT update

Ambas as condições devem ser satisfeitas simultaneamente:

1. O UPDATE **não modifica nenhuma coluna** referenciada por algum índice da tabela.
2. A nova versão da linha **cabe na mesma página** que a versão antiga (há espaço livre suficiente).

Se qualquer condição falhar, o update não é HOT e o PostgreSQL precisa inserir novas entradas em **todos** os índices da tabela — primário e secundários.

## Relevância prática

- Aproximadamente **46% dos updates** se qualificam como HOT (dado interno da OtterTune sobre bancos PostgreSQL em produção).
- Os outros 54% pagam o custo de atualizar todos os índices, mesmo os nunca utilizados.

## Como favorecer HOT updates

- Configurar **`fillfactor`** menor que 100% em tabelas write-heavy (ex: `fillfactor=70` reserva 30% de cada página para versões novas). Cria-se assim espaço livre na página sem precisar alocar nova página.
- Evitar indexar colunas que mudam com frequência.
- Identificar e remover índices não utilizados — se não existem, não precisam ser atualizados.

## Limitação

HOT é uma mitigação, não uma solução. Não resolve o problema fundamental de [[tecnico/concepts/table-bloat|table bloat]] (dead tuples ainda acumulam na mesma página) nem o de version copying (a linha inteira ainda é copiada).
