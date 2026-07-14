---
title: "Django"
tipo: entity
dominio: tecnico
tags: [python, web-framework, orm, backend, stack-principal]
fontes: [tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios, tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]
criado: 2026-07-14
atualizado: 2026-07-14
---

# Django

Framework web em Python, "batteries included" (ORM, admin, auth, migrations). Stack de backend principal do usuário, geralmente combinado com Django Rest Framework (DRF) para expor APIs consumidas por frontend em React + Mantine.

## Características gerais

- ORM próprio, síncrono por padrão — não é o mais rápido entre ORMs Python nem assíncrono nativamente
- Servido em produção tipicamente via Gunicorn (WSGI), que também não é assíncrono nativamente — pode ser combinado com workers uvicorn/hypercorn
- DRF é a extensão padrão para expor APIs REST; seus serializers genéricos priorizam correção (validação) sobre performance de leitura

## Performance em escala

Ver [[tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]] para uma compilação de técnicas: resolução do problema de [[tecnico/concepts/n-plus-1-queries|N+1 queries]] via `select_related`/`prefetch_related`, [[tecnico/concepts/caching|caching]] em múltiplos níveis, [[tecnico/entities/celery|Celery]] para tarefas assíncronas, [[tecnico/concepts/particionamento-de-tabelas|particionamento de tabelas]] em bases grandes, e [[tecnico/concepts/desnormalizacao|desnormalização]] como último recurso.

Quando o ORM ou a natureza síncrona do Django viram o gargalo real, as alternativas citadas são reescrever a camada de API em FastAPI (assíncrono nativo) ou trocar o ORM por SQLAlchemy/PonyORM.

## Infraestrutura e conexões (fonte: Nicolae Godina)

Ver [[tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]] para uma segunda fonte, com ênfase complementar em infraestrutura: [[tecnico/entities/docker|Docker]] + [[tecnico/entities/kubernetes|Kubernetes]] para empacotamento e orquestração, monitoramento proativo de métricas (CPU por pod/nó, tráfego), e [[tecnico/concepts/conexoes-persistentes|conexões persistentes]] via `CONN_MAX_AGE` — caso relatado de corte de 50% na carga do banco. Também cobre [[tecnico/concepts/operacoes-em-lote|operações em lote]] (`bulk_create`/`bulk_update`) e [[tecnico/concepts/reducao-de-transferencia-de-dados|redução de transferência de dados]] via `.only()`/`.defer()`.

## Ver também

- [[tecnico/entities/postgresql]] — banco de dados comum em stacks Django
- [[tecnico/entities/celery]]
- [[tecnico/entities/docker]]
- [[tecnico/entities/kubernetes]]
- [[tecnico/concepts/n-plus-1-queries]]
- [[tecnico/concepts/caching]]
- [[tecnico/concepts/conexoes-persistentes]]
- [[tecnico/concepts/operacoes-em-lote]]
- [[tecnico/concepts/reducao-de-transferencia-de-dados]]
