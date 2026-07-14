---
title: "N+1 Queries"
tipo: concept
dominio: tecnico
tags: [orm, performance, banco-de-dados, django]
fontes: [tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios, tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]
criado: 2026-07-14
atualizado: 2026-07-14
---

# N+1 Queries

Padrão de acesso a dados ineficiente onde uma query inicial (1) busca uma lista de N registros, e cada registro dispara uma query adicional para buscar dados relacionados — resultando em N+1 queries no total em vez de uma ou duas. É o problema de performance mais comum e mais barato de evitar em aplicações com ORM.

## Como aparece no Django

Ao iterar sobre um queryset e acessar um campo de relacionamento (foreign key, one-to-one) dentro do loop, o ORM dispara uma query separada por iteração:

```python
# 11 queries: 1 para buscar os posts + 10 para buscar o autor de cada um
for post in Post.objects.all()[:10]:
    print(post.autor.nome)
```

## Solução

- **`select_related()`** — para relacionamentos foreign key/one-to-one. Gera um `JOIN` SQL, trazendo os dados relacionados na mesma query. Eficácia depende do tamanho das tabelas envolvidas, já que o ORM precisa montar a query de JOIN.
- **`prefetch_related()`** — para relacionamentos many-to-many/many-to-one (reverse FK). Faz uma query separada, mas só uma, e junta os resultados em Python.
- Ferramentas como `django-debug-toolbar` ajudam a visualizar quantas queries uma view dispara e identificar o padrão N+1 na prática.

## Por que importa em escala

Cada query adicional multiplicada por milhões de requests é a alavanca de maior impacto em performance de aplicações Django — reduzir queries é citado como a otimização de maior retorno antes de qualquer outra (caching, infraestrutura, etc.).

## Ver também

- [[tecnico/entities/django]]
- [[tecnico/entities/postgresql]]
- [[tecnico/concepts/reducao-de-transferencia-de-dados]] — princípio complementar: depois de reduzir o número de queries, reduzir o que cada uma transporta
