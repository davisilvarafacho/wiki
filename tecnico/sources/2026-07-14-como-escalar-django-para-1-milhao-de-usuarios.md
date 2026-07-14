---
title: "How to scale a Django application to serve one million users?"
tipo: source
dominio: tecnico
url: "https://tarekeesa7.medium.com/how-to-scale-a-django-application-to-serve-one-million-users-f3f4237660c8"
autor: "Tarek Eissa"
publicado: 2024-05-24
capturado: 2026-07-14
tipo_fonte: blog-post
tags: [django, performance, escalabilidade, orm, caching, celery, drf]
criado: 2026-07-14
atualizado: 2026-07-14
---

# How to scale a Django application to serve one million users?

Compilação de recomendações de performance para Django, feita por Tarek Eissa a partir de artigos, livros e vídeos, com algumas implementadas pelo próprio autor. Cobertura ampla e rasa — cada tópico é um ponteiro para investigação mais profunda, não um guia definitivo.

## Sumário

- **Reduzir queries** é a alavanca de maior impacto (banco de dados é o gargalo mais comum). Usar `django-debug-toolbar` para identificar o problema de [[tecnico/concepts/n-plus-1-queries|N+1 queries]] e resolver com `select_related()` (FK/one-to-one), `prefetch_related()` (many-to-many/many-to-one), `annotate()`/`aggregate()`, `Q` objects e F-expressions (operações no banco em vez de Python)
- **Gunicorn**: não é assíncrono nativamente; considerar uvicorn/hypercorn. Workers recomendados: `(2 × cores) + 1` — 4-12 workers servem de centenas a milhares de req/s
- **Serializers do DRF** fazem validação mesmo em leitura (`read_only`), o que custa performance; alternativas mais rápidas: Serpy, Marshmallow (um caso citado reduziu custo de serialização em 99%)
- **Paginação** sempre, via `Paginator`/`ListView.paginate_by` ou paginação nativa do DRF
- **Índices de banco** (`db_index=True`) aceleram busca mas custam em escrita e espaço — balancear
- **Motores de busca dedicados** (ElasticSearch, Solr, Whoosh, Xapian) para buscas textuais pesadas, em vez de reimplementar
- **Remover middleware não usado** (ex: messages, flatpages, locale) — cada um custa um passo por request
- **[[tecnico/concepts/caching|Caching]]**: memcached, redis, database cache, filesystem cache — em múltiplos níveis (site inteiro, view via `@cache_page`, fragmentos). Cache em memória (memcached/redis) é efêmero — some com reboot
- **[[tecnico/entities/celery|Celery]]** para tarefas assíncronas (envio de email, chamadas a terceiros) — não bloquear a resposta esperando I/O de terceiros
- **[[tecnico/concepts/particionamento-de-tabelas|Particionamento de tabelas]]** quando passam de milhões de registros (Postgres 10+, via `django-postgres-extra`); considerar também réplicas de leitura com um master de escrita
- **CDN** para estáticos — delega a tarefa e ganha proximidade geográfica com o usuário (ver [[tecnico/concepts/anycast]])
- **[[tecnico/concepts/desnormalizacao|Desnormalização]]** como último recurso: armazenar valores derivados (ex: contagens) em vez de recalcular a cada request
- **Plugins de terceiros** (analytics, chat) podem degradar performance — usar `async`/`defer` ou remover
- **Interpretadores alternativos** (PyPy) otimizam via análise de tipos, mas nem sempre são 100% compatíveis — último recurso
- **Swig** permite escrever gargalos em C/C++/Go/Java e importar em Python — para quando o problema é CPU-bound e Python puro não basta
- **ORMs/frameworks alternativos**: Django ORM não é o mais rápido nem assíncrono; considerar SQLAlchemy, PonyORM, ou migrar a camada de API para FastAPI se o objetivo é uma API pura (sem os outros componentes do Django)

## Citações relevantes

> "The most important action to take is to reduce the number of queries and the impact of each one of them. You can reduce the impact of your queries by 90%, and I am not exaggerating."

> "With 4–12 workers you can serve from hundreds to thousands of requests per second."

> "You should only use this option [denormalization] to solve your Django performance problems if you have already exhausted the other options."

## Takeaways

- A ordem de prioridade implícita no artigo é: **queries → configuração de infra (gunicorn) → serialização → paginação/índices → caching/async → particionamento/CDN → desnormalização → trocar linguagem/interpretador/framework**. Ou seja: otimizar o que já existe antes de reescrever ou trocar de stack
- N+1 queries e falta de paginação são os erros mais baratos de evitar e mais caros quando ignorados em escala
- Denormalização, PyPy e Swig são apresentados explicitamente como **últimos recursos** — sinal de que a maioria das aplicações nunca deveria precisar chegar lá
- O artigo é uma lista de ponteiros, não um tutorial — cada tópico merece página própria conforme a wiki for encontrando fontes mais profundas

## Páginas relacionadas

- [[tecnico/entities/django]] — entidade criada
- [[tecnico/entities/celery]] — entidade criada
- [[tecnico/entities/autores/tarek-eissa]] — autor criado (stub)
- [[tecnico/concepts/n-plus-1-queries]] — conceito criado
- [[tecnico/concepts/caching]] — conceito criado
- [[tecnico/concepts/desnormalizacao]] — conceito criado
- [[tecnico/concepts/particionamento-de-tabelas]] — conceito criado
- [[tecnico/entities/postgresql]] — mencionado (particionamento, versão 10+)
- [[tecnico/concepts/anycast]] — mencionado (base de CDN)
