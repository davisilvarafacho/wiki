---
title: "Conexões persistentes de banco de dados"
tipo: concept
dominio: tecnico
tags: [banco-de-dados, performance, django, infraestrutura]
fontes: [tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]
criado: 2026-07-14
atualizado: 2026-07-14
---

# Conexões persistentes de banco de dados

Abrir uma conexão TCP com o banco de dados tem custo (handshake, autenticação, alocação de recursos no servidor). Frameworks web que fecham a conexão ao final de cada request pagam esse custo em toda requisição. Conexões persistentes mantêm a conexão aberta entre requests, amortizando esse custo.

## No Django: `CONN_MAX_AGE`

Por padrão, o Django fecha a conexão com o banco ao final de cada request. O parâmetro `CONN_MAX_AGE` (em `DATABASES`, em segundos) define por quanto tempo uma conexão pode ser reaproveitada antes de expirar:

```python
DATABASES = {
    "default": {
        ...
        "CONN_MAX_AGE": 300,  # 5 minutos
    }
}
```

## Caso real

Um relato documentado: ajustar `CONN_MAX_AGE` de 0 (padrão) para 300 segundos reduziu a carga do banco pela metade, permitindo fazer downgrade de uma instância AWS Aurora de `db.r5.8xlarge` para `db.r5.4xlarge` — corte de custo de infraestrutura mantendo performance.

## Cuidado

O número padrão de conexões concorrentes de um banco costuma ser baixo (ex: 100), o que não é suficiente em cenários de alta carga com muitos workers/pods mantendo conexões abertas simultaneamente. Aumentar `CONN_MAX_AGE` sem revisar o limite de conexões concorrentes do banco pode esgotá-lo — geralmente mitigado com um pooler de conexões (ex: PgBouncer) entre a aplicação e o banco.

## Ver também

- [[tecnico/entities/django]]
- [[tecnico/entities/postgresql]]
- [[tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]]
