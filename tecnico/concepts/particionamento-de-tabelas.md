---
title: "Particionamento de tabelas"
tipo: concept
dominio: tecnico
tags: [performance, banco-de-dados, postgresql, escalabilidade]
fontes: [tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]
criado: 2026-07-14
atualizado: 2026-07-14
---

# Particionamento de tabelas

Dividir uma tabela grande em partes menores (partições) para que cada busca percorra só a parte relevante, em vez da tabela inteira. Critério comum: período de tempo — uma partição por ano, por exemplo, com a mais recente sendo a mais consultada.

## Quando faz sentido

Quando uma tabela passa de milhões de registros e buscas começam a demorar porque percorrem o histórico inteiro, mesmo quando só o período recente importa.

## Implementação

Depende do banco. No [[tecnico/entities/postgresql|PostgreSQL]], particionamento nativo existe a partir da versão 10; [django-postgres-extra](https://django-postgres-extra.readthedocs.io/en/master/table_partitioning.html) cobre o que falta na integração com o Django ORM.

Complementar: **réplicas de leitura** — uma instância master para escrita e réplicas dedicadas para leitura, distribuindo a carga de queries.

## Ver também

- [[tecnico/entities/postgresql]]
- [[tecnico/entities/django]]
- [[tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]]
